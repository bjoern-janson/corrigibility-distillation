"""Fresh-process opcode accounting runner for CGP-001.

The runner deliberately has a small bootstrap boundary.  Argument parsing,
reading the manifest's allowed-file table, and constructing the trace callback
happen before tracing.  File/hash/checkout verification, imports, experiment
dispatch, and construction of the in-memory arm record happen after tracing.
Serialization happens only after tracing has stopped.

This module is apparatus, not an outcome evaluator.  It neither interprets an
arm result nor supplies any repair/adoption decision.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Iterator, Mapping
from contextlib import contextmanager
from dataclasses import dataclass
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import time
from types import CodeType, FrameType
from typing import Any


PREREGISTRATION_ANCHOR = "669a94aac6c07484323dde3b0fb64df5b9ec4bca"
FS_COMMIT = "2f4ca824e02b89df0c23d64de312c4f93a4c8a41"
NSS_COMMIT = "307c24576ebea951be04d187c61e7428f4f0e184"

ARMS = (
    "FS_ONLY",
    "NSS_ONLY",
    "NSS_TO_FS",
    "SHUFFLED_NSS_TO_FS",
)

EXECUTION_MANIFEST_RELATIVE = Path(
    "experiments/cgp_001/execution_manifest.json"
)
TRANSLATION_AUDIT_RELATIVE = Path("CGP_001_TRANSLATION_AUDIT.md")

_ARM_SLUGS = {
    "FS_ONLY": "fs_only",
    "NSS_ONLY": "nss_only",
    "NSS_TO_FS": "nss_to_fs",
    "SHUFFLED_NSS_TO_FS": "shuffled_nss_to_fs",
}

_ARM_RESULT_FIELDS = {
    "schema_version",
    "arm",
    "parent_commits",
    "source_verification",
    "unrotated_allocation_vector",
    "applied_allocation_vector",
    "conditions",
    "later_family_reuse",
    "operation_diagnostics",
    "generator_state",
    "stages",
}

_CONDITION_FIELDS = {
    "index",
    "condition_name",
    "family",
    "repair_cost",
    "task_seed",
    "probe_seed",
    "heldout_seed",
    "probe_count",
    "heldout_count",
    "allocation",
    "nss",
    "base_result",
    "fanout_result",
    "selected_result",
    "estimated_repair_value",
    "m1_status",
    "fanout_enabled",
    "score_calls",
    "heldout_accuracy",
    "state_before_authority",
    "state_after_authority",
}

_CONDITION_NAMES = (
    "INSUFFICIENT_LOW",
    "INSUFFICIENT_HIGH",
    "SUFFICIENT_LOW",
    "NOVEL_REUSE_REPAIR",
)

_OPERATION_DIAGNOSTIC_FIELDS = {
    "M0_candidates_scored",
    "M1_candidates_scored",
    "reuse_candidates_scored",
    "program_example_evaluations",
    "program_node_evaluations",
    "source_records",
    "emitted_records",
    "apparatus_equivalence_source_records",
    "primary_translation_source_records",
    "signature_calls",
    "apparatus_signature_equivalence_calls",
    "apparatus_m0_pair_program_evaluations",
    "apparatus_m0_pair_program_node_evaluations",
    "hash_group_insertions",
    "label_set_insertions",
    "collision_decisions",
    "expanded_signatures",
    "NSS_generated_predicate_evaluations",
    "heldout_reuse_examples",
    "FS_value_adoption_decisions",
    "selected_node_count",
    "generator_state",
    "stages",
}

PHASES = (
    "C_generator_construct",
    "C_case_generation",
    "C_M0_search",
    "C_translation",
    "C_NSS_gate",
    "C_M1_search",
    "C_FS_value_authority",
    "C_heldout_reuse",
    "C_control",
)

CONTROL_PHASE = "C_control"

EXPECTED_RUNTIME = {
    "python": (3, 12, 13),
    "system": "Windows",
    "os_version": "10.0.26200.0",
    "pythonhashseed": "0",
}

FS_FILES = {
    "experiments/meta_language_repair.py": (
        "f23a48e06802a08441eed492752fa5223e564587ec78b2f447ba464737aa37db"
    ),
    "experiments/meta_language_repair.md": (
        "7f6ad9e3bdf0c89d3233f518f79603b20a2b722e148323bcd8c4bb20de76e804"
    ),
}

NSS_FILES = {
    "src/negative_space_search/operator_discovery_v0_7.py": (
        "f0814d8b9a68446e49d50117a127e91ab1cabfd9ccc4dcf8f4bba6949099d62e"
    ),
    "src/negative_space_search/language_boundary_v0_6.py": (
        "18a7f29861018a4a7171494851e4d9b5158ed4064f2f28d792118424943f5ae4"
    ),
    "src/negative_space_search/basis_v0_5.py": (
        "e792665fad4d2c5791fa91be9845c413902e06384c19c1196c4aae596ed54db1"
    ),
    "src/negative_space_search/representation_v0_4.py": (
        "7f337bc7336688dbd871fe475c7e2d13e640180d84269745b181eae80d52183a"
    ),
}

_SHA256_PATTERN = re.compile(r"[0-9a-f]{64}\Z")
_GIT_SHA_PATTERN = re.compile(r"[0-9a-f]{40}\Z")
_RUNNER_MAIN_STARTED = False


class RunnerContractError(RuntimeError):
    """The frozen runner, manifest, runtime, or trace contract was violated."""


def _canonical_path(path: Path | str) -> str:
    """Return a case-normalized, symlink-resolved absolute path key."""

    return os.path.normcase(os.path.realpath(os.fspath(path)))


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _is_beneath(path_key: str, root_key: str) -> bool:
    try:
        return os.path.commonpath((path_key, root_key)) == root_key
    except ValueError:
        return False


@dataclass(frozen=True)
class AllowedFile:
    path: Path
    canonical_path: str
    sha256: str


@dataclass(frozen=True)
class ManifestBootstrap:
    path: Path
    allowed_files: Mapping[str, AllowedFile]


@dataclass(frozen=True)
class VerifiedManifest:
    path: Path
    implementation_anchor: str
    translation_audit_anchor: str
    translation_audit_path: Path
    translation_audit_sha256: str
    arm_output_paths: Mapping[str, Path]
    arm_attempt_paths: Mapping[str, Path]
    allowed_files: Mapping[str, AllowedFile]


def _read_manifest_document(path: Path) -> dict[str, object]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise RunnerContractError(f"cannot read manifest: {error}") from error
    if not isinstance(document, dict):
        raise RunnerContractError("manifest root must be an object")
    return document


def _parse_allowed_files(document: Mapping[str, object]) -> dict[str, AllowedFile]:
    raw_allowed = document.get("allowed_files")
    if not isinstance(raw_allowed, dict) or not raw_allowed:
        raise RunnerContractError(
            "manifest allowed_files must be a non-empty absolute-path-to-SHA256 object"
        )

    allowed: dict[str, AllowedFile] = {}
    for raw_path, raw_digest in raw_allowed.items():
        if not isinstance(raw_path, str) or not isinstance(raw_digest, str):
            raise RunnerContractError("allowed_files keys and values must be strings")
        candidate = Path(raw_path)
        if not candidate.is_absolute():
            raise RunnerContractError(f"allowed file path is not absolute: {raw_path}")
        if _SHA256_PATTERN.fullmatch(raw_digest) is None:
            raise RunnerContractError(f"invalid SHA-256 for allowed file: {raw_path}")
        canonical = _canonical_path(candidate)
        if canonical in allowed:
            raise RunnerContractError(
                f"duplicate canonical path in allowed_files: {raw_path}"
            )
        allowed[canonical] = AllowedFile(candidate, canonical, raw_digest)
    return allowed


def _read_manifest_bootstrap(path: Path) -> ManifestBootstrap:
    """Read only the allowed-file table needed to construct the trace callback."""

    document = _read_manifest_document(path)
    return ManifestBootstrap(path=path, allowed_files=_parse_allowed_files(document))


def _parse_arm_path_map(
    document: Mapping[str, object],
    field: str,
) -> dict[str, Path]:
    raw_paths = document.get(field)
    if not isinstance(raw_paths, dict) or set(raw_paths) != set(ARMS):
        raise RunnerContractError(f"manifest {field} must contain exactly the four arms")
    parsed: dict[str, Path] = {}
    canonical_paths: set[str] = set()
    for arm in ARMS:
        raw_path = raw_paths.get(arm)
        if not isinstance(raw_path, str) or not Path(raw_path).is_absolute():
            raise RunnerContractError(f"manifest {field}.{arm} must be absolute")
        path = Path(raw_path)
        canonical = _canonical_path(path)
        if canonical in canonical_paths:
            raise RunnerContractError(f"manifest {field} contains duplicate paths")
        canonical_paths.add(canonical)
        parsed[arm] = path
    return parsed


def _read_manifest_verified(
    path: Path,
    bootstrap: ManifestBootstrap,
) -> VerifiedManifest:
    """Validate every authority-bearing manifest field under opcode tracing."""

    document = _read_manifest_document(path)
    if document.get("preregistration_anchor") != PREREGISTRATION_ANCHOR:
        raise RunnerContractError("manifest preregistration anchor mismatch")

    implementation_anchor = document.get("implementation_anchor")
    if (
        not isinstance(implementation_anchor, str)
        or _GIT_SHA_PATTERN.fullmatch(implementation_anchor) is None
    ):
        raise RunnerContractError(
            "manifest implementation_anchor must be a lowercase 40-hex commit"
        )

    if document.get("translation_audit_status") != "PASS":
        raise RunnerContractError("manifest translation_audit_status must be PASS")
    translation_audit_anchor = document.get("translation_audit_anchor")
    if (
        not isinstance(translation_audit_anchor, str)
        or _GIT_SHA_PATTERN.fullmatch(translation_audit_anchor) is None
    ):
        raise RunnerContractError(
            "manifest translation_audit_anchor must be a lowercase 40-hex commit"
        )
    raw_audit_path = document.get("translation_audit_path")
    if not isinstance(raw_audit_path, str) or not Path(raw_audit_path).is_absolute():
        raise RunnerContractError("manifest translation_audit_path must be absolute")
    translation_audit_path = Path(raw_audit_path)
    translation_audit_sha256 = document.get("translation_audit_sha256")
    if (
        not isinstance(translation_audit_sha256, str)
        or _SHA256_PATTERN.fullmatch(translation_audit_sha256) is None
    ):
        raise RunnerContractError(
            "manifest translation_audit_sha256 must be lowercase SHA-256"
        )

    arm_output_paths = _parse_arm_path_map(document, "arm_output_paths")
    arm_attempt_paths = _parse_arm_path_map(document, "arm_attempt_paths")
    if {
        _canonical_path(path) for path in arm_output_paths.values()
    } & {
        _canonical_path(path) for path in arm_attempt_paths.values()
    }:
        raise RunnerContractError("manifest output and attempt paths must be disjoint")

    allowed = _parse_allowed_files(document)
    if allowed != bootstrap.allowed_files:
        raise RunnerContractError("manifest allowed_files changed after trace bootstrap")

    audit_key = _canonical_path(translation_audit_path)
    audit_entry = allowed.get(audit_key)
    if audit_entry is None:
        raise RunnerContractError("translation audit path must appear in allowed_files")
    if audit_entry.sha256 != translation_audit_sha256:
        raise RunnerContractError(
            "translation audit digest does not match its allowed_files entry"
        )

    return VerifiedManifest(
        path=path,
        implementation_anchor=implementation_anchor,
        translation_audit_anchor=translation_audit_anchor,
        translation_audit_path=translation_audit_path,
        translation_audit_sha256=translation_audit_sha256,
        arm_output_paths=arm_output_paths,
        arm_attempt_paths=arm_attempt_paths,
        allowed_files=allowed,
    )


@dataclass(frozen=True)
class OpcodeSnapshot:
    total: int
    phases: Mapping[str, int]
    files: Mapping[str, int]
    unclassified_project_opcodes: int
    unexpected_project_files: tuple[str, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "total": self.total,
            "phases": dict(self.phases),
            "files": dict(self.files),
            "unclassified_project_opcodes": self.unclassified_project_opcodes,
            "unexpected_project_files": list(self.unexpected_project_files),
        }


class OpcodeCounter:
    """Count opcode events in manifest-authorized project frames by phase."""

    def __init__(
        self,
        *,
        allowed_files: Mapping[str, AllowedFile],
        project_roots: tuple[Path, ...],
    ) -> None:
        self._allowed_files = dict(allowed_files)
        self._project_roots = tuple(_canonical_path(root) for root in project_roots)
        self._phase = CONTROL_PHASE
        self._phase_stack: list[str] = []
        self._phase_counts = {phase: 0 for phase in PHASES}
        self._file_counts = {
            entry.canonical_path: 0 for entry in self._allowed_files.values()
        }
        self._total = 0
        self._unclassified_project_opcodes = 0
        self._unexpected_project_files: set[str] = set()
        self._code_classification: dict[CodeType, tuple[str, bool, bool]] = {}
        self._active = False
        self._trace_code = self._trace.__code__

    def _is_project_file(self, path_key: str) -> bool:
        return any(_is_beneath(path_key, root) for root in self._project_roots)

    def _configure_frame(self, frame: FrameType) -> None:
        frame.f_trace_lines = False
        frame.f_trace_opcodes = True

    def _classify_code(self, code: CodeType) -> tuple[str, bool, bool]:
        cached = self._code_classification.get(code)
        if cached is not None:
            return cached

        filename = code.co_filename
        if not filename or filename.startswith("<"):
            classified = ("", False, False)
        else:
            path_key = _canonical_path(filename)
            classified = (
                path_key,
                path_key in self._allowed_files,
                self._is_project_file(path_key),
            )
        self._code_classification[code] = classified
        return classified

    def _trace(
        self,
        frame: FrameType,
        event: str,
        arg: object,
    ) -> Callable[[FrameType, str, object], object] | None:
        del arg
        if not self._active or frame.f_code is self._trace_code:
            return None

        path_key, allowed, project_owned = self._classify_code(frame.f_code)

        if project_owned and not allowed:
            self._unexpected_project_files.add(path_key)
            raise RunnerContractError(
                f"unapproved project frame entered under opcode tracing: {path_key}"
            )

        if not allowed and not project_owned:
            return None

        if event == "call":
            self._configure_frame(frame)
            return self._trace

        if event != "opcode":
            return self._trace

        if self._phase not in self._phase_counts:
            self._unclassified_project_opcodes += 1
            return self._trace

        self._phase_counts[self._phase] += 1
        self._file_counts[path_key] += 1
        self._total += 1
        return self._trace

    def start(self) -> None:
        if self._active:
            raise RunnerContractError("opcode counter is already active")
        self._phase = CONTROL_PHASE
        self._active = True
        sys.settrace(self._trace)

        # sys.settrace applies automatically to future frames.  Attach it to
        # already-running allowed project frames so the post-install runner
        # path is included exactly as preregistered.
        frame: FrameType | None = sys._getframe()
        while frame is not None:
            path_key, allowed, project_owned = self._classify_code(frame.f_code)
            if project_owned and not allowed:
                self._unexpected_project_files.add(path_key)
                self._active = False
                sys.settrace(None)
                raise RunnerContractError(
                    "unapproved already-running project frame at trace start: "
                    f"{path_key}"
                )
            if allowed or project_owned:
                frame.f_trace = self._trace
                self._configure_frame(frame)
            frame = frame.f_back

    def stop(self) -> None:
        if not self._active:
            raise RunnerContractError("opcode counter is not active")
        if self._phase_stack:
            raise RunnerContractError("cannot stop with an active nested phase")

        # This assignment is the precise end boundary.  The callback returns
        # None for every later event; serialization therefore cannot be billed.
        self._active = False
        sys.settrace(None)

        frame: FrameType | None = sys._getframe()
        while frame is not None:
            frame.f_trace = None
            frame = frame.f_back

    @contextmanager
    def phase(self, name: str) -> Iterator[None]:
        if name not in self._phase_counts:
            raise RunnerContractError(f"unknown opcode phase: {name}")
        if not self._active:
            raise RunnerContractError("phase used while opcode counter is inactive")

        previous = self._phase
        self._phase_stack.append(previous)
        self._phase = name
        try:
            yield
        finally:
            restored = self._phase_stack.pop()
            if restored != previous:
                raise RunnerContractError("opcode phase stack corruption")
            self._phase = restored

    def snapshot(self) -> OpcodeSnapshot:
        if self._active:
            raise RunnerContractError("cannot snapshot an active opcode counter")

        phase_total = sum(self._phase_counts.values())
        file_total = sum(self._file_counts.values())
        if phase_total != self._total or file_total != self._total:
            raise RunnerContractError("opcode phase/file totals do not sum exactly")
        if self._unclassified_project_opcodes:
            files = ", ".join(sorted(self._unexpected_project_files))
            raise RunnerContractError(
                "unclassified project opcodes detected"
                + (f": {files}" if files else "")
            )

        return OpcodeSnapshot(
            total=self._total,
            phases=dict(self._phase_counts),
            files=dict(sorted(self._file_counts.items())),
            unclassified_project_opcodes=0,
            unexpected_project_files=(),
        )


def _verify_allowed_files(manifest: VerifiedManifest) -> None:
    for entry in manifest.allowed_files.values():
        if not entry.path.is_file():
            raise RunnerContractError(f"allowed file does not exist: {entry.path}")
        observed = _sha256(entry.path)
        if observed != entry.sha256:
            raise RunnerContractError(
                f"allowed file SHA-256 mismatch: {entry.path}; "
                f"expected {entry.sha256}, observed {observed}"
            )


def _git_head(root: Path) -> str:
    try:
        completed = subprocess.run(
            (
                "git",
                "-c",
                f"safe.directory={root.resolve().as_posix()}",
                "-C",
                os.fspath(root),
                "rev-parse",
                "HEAD",
            ),
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise RunnerContractError(f"cannot verify checkout commit at {root}") from error
    return completed.stdout.strip()


def _git_diff_is_clean_at_anchor(
    root: Path,
    anchor: str,
    relative_paths: tuple[str, ...],
) -> bool:
    """Return whether required working files equal their committed anchor blobs."""

    for relative in relative_paths:
        try:
            exists = subprocess.run(
                (
                    "git",
                    "-c",
                    f"safe.directory={root.resolve().as_posix()}",
                    "-C",
                    os.fspath(root),
                    "cat-file",
                    "-e",
                    f"{anchor}:{relative}",
                ),
                check=False,
                capture_output=True,
            )
        except OSError as error:
            raise RunnerContractError(
                f"cannot resolve committed file {anchor}:{relative}"
            ) from error
        if exists.returncode != 0:
            raise RunnerContractError(
                f"required committed file is absent: {anchor}:{relative}"
            )

    try:
        completed = subprocess.run(
            (
                "git",
                "-c",
                f"safe.directory={root.resolve().as_posix()}",
                "-C",
                os.fspath(root),
                "diff",
                "--quiet",
                anchor,
                "--",
                *relative_paths,
            ),
            check=False,
            capture_output=True,
        )
    except OSError as error:
        raise RunnerContractError(
            f"cannot verify implementation files at {root}"
        ) from error
    if completed.returncode not in (0, 1):
        raise RunnerContractError(
            f"git diff failed while verifying implementation files at {root}"
        )
    return completed.returncode == 0


def _git_is_ancestor(root: Path, ancestor: str, descendant: str) -> bool:
    try:
        completed = subprocess.run(
            (
                "git",
                "-c",
                f"safe.directory={root.resolve().as_posix()}",
                "-C",
                os.fspath(root),
                "merge-base",
                "--is-ancestor",
                ancestor,
                descendant,
            ),
            check=False,
            capture_output=True,
        )
    except OSError as error:
        raise RunnerContractError(
            f"cannot verify commit ancestry {ancestor} -> {descendant}"
        ) from error
    if completed.returncode not in (0, 1):
        raise RunnerContractError(
            f"invalid or unavailable commit ancestry {ancestor} -> {descendant}"
        )
    return completed.returncode == 0


def _git_commit_parents(root: Path, commit: str) -> tuple[str, ...]:
    try:
        completed = subprocess.run(
            (
                "git",
                "-c",
                f"safe.directory={root.resolve().as_posix()}",
                "-C",
                os.fspath(root),
                "show",
                "-s",
                "--format=%P",
                commit,
            ),
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise RunnerContractError(f"cannot resolve commit parents for {commit}") from error
    raw = completed.stdout.strip()
    return () if not raw else tuple(raw.split())


def _git_changed_paths(root: Path, parent: str, child: str) -> frozenset[str]:
    try:
        completed = subprocess.run(
            (
                "git",
                "-c",
                f"safe.directory={root.resolve().as_posix()}",
                "-C",
                os.fspath(root),
                "diff",
                "--name-only",
                "--no-renames",
                parent,
                child,
                "--",
            ),
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError) as error:
        raise RunnerContractError(
            f"cannot resolve changed paths for {parent} -> {child}"
        ) from error
    return frozenset(
        line.strip().replace("\\", "/")
        for line in completed.stdout.splitlines()
        if line.strip()
    )


def _verify_direct_parent_and_paths(
    *,
    repository_root: Path,
    parent: str,
    child: str,
    expected_paths: frozenset[str],
    label: str,
) -> None:
    parents = _git_commit_parents(repository_root, child)
    if parents != (parent,):
        raise RunnerContractError(
            f"{label} must have exactly direct parent {parent}; observed {parents!r}"
        )
    observed_paths = _git_changed_paths(repository_root, parent, child)
    if observed_paths != expected_paths:
        raise RunnerContractError(
            f"{label} changed-path set mismatch; "
            f"expected={sorted(expected_paths)!r}, observed={sorted(observed_paths)!r}"
        )


def _verify_checkout(
    *,
    root: Path,
    expected_commit: str,
    expected_files: Mapping[str, str],
    allowed_files: Mapping[str, AllowedFile],
) -> None:
    if not root.is_dir():
        raise RunnerContractError(f"checkout root does not exist: {root}")
    observed_commit = _git_head(root)
    if observed_commit != expected_commit:
        raise RunnerContractError(
            f"checkout commit mismatch at {root}: "
            f"expected {expected_commit}, observed {observed_commit}"
        )

    for relative, expected_digest in expected_files.items():
        path = root / Path(relative)
        canonical = _canonical_path(path)
        manifest_entry = allowed_files.get(canonical)
        if manifest_entry is None:
            raise RunnerContractError(f"frozen source absent from allowed_files: {path}")
        if manifest_entry.sha256 != expected_digest:
            raise RunnerContractError(
                f"manifest digest does not match preregistration for {path}"
            )
        if _sha256(path) != expected_digest:
            raise RunnerContractError(f"frozen source hash mismatch: {path}")


def _verify_runtime() -> None:
    observed_python = sys.version_info[:3]
    if observed_python != EXPECTED_RUNTIME["python"]:
        raise RunnerContractError(
            f"Python runtime mismatch: expected {EXPECTED_RUNTIME['python']}, "
            f"observed {observed_python}"
        )
    if platform.system() != EXPECTED_RUNTIME["system"]:
        raise RunnerContractError(
            f"operating system mismatch: expected {EXPECTED_RUNTIME['system']}, "
            f"observed {platform.system()}"
        )
    windows_version = sys.getwindowsversion()
    observed_os_version = (
        f"{windows_version.major}.{windows_version.minor}."
        f"{windows_version.build}.0"
    )
    if observed_os_version != EXPECTED_RUNTIME["os_version"]:
        raise RunnerContractError(
            f"OS version mismatch: expected {EXPECTED_RUNTIME['os_version']}, "
            f"observed {observed_os_version}"
        )
    if os.environ.get("PYTHONHASHSEED") != EXPECTED_RUNTIME["pythonhashseed"]:
        raise RunnerContractError("PYTHONHASHSEED must be exactly 0")


def _implementation_paths(repository_root: Path) -> tuple[Path, ...]:
    return (
        Path(__file__).resolve(),
        repository_root / "experiments" / "cgp_001" / "cgp_001.py",
        repository_root / "experiments" / "cgp_001" / "test_translation.py",
        repository_root
        / "experiments"
        / "cgp_001"
        / "contracts"
        / "translation_contract.json",
        repository_root
        / "experiments"
        / "cgp_001"
        / "contracts"
        / "evaluation_contract.json",
        repository_root
        / "experiments"
        / "cgp_001"
        / "fixtures"
        / "translation_fixtures.json",
    )


def _verify_runner_is_allowed(
    *,
    allowed_files: Mapping[str, AllowedFile],
    repository_root: Path,
) -> None:
    for path in _implementation_paths(repository_root):
        if _canonical_path(path) not in allowed_files:
            raise RunnerContractError(f"required CGP implementation file not allowed: {path}")


def _verify_implementation_binding(
    *,
    repository_root: Path,
    implementation_anchor: str,
) -> None:
    required = _implementation_paths(repository_root)
    relative = tuple(
        path.relative_to(repository_root).as_posix()
        for path in required
    )
    if not _git_diff_is_clean_at_anchor(
        repository_root,
        implementation_anchor,
        relative,
    ):
        raise RunnerContractError(
            "required CGP implementation files differ from implementation_anchor"
        )


def _verify_frozen_lineage(
    *,
    manifest: VerifiedManifest,
    repository_root: Path,
    execution_anchor: str,
) -> None:
    implementation_paths = frozenset(
        path.relative_to(repository_root).as_posix()
        for path in _implementation_paths(repository_root)
    )
    _verify_direct_parent_and_paths(
        repository_root=repository_root,
        parent=PREREGISTRATION_ANCHOR,
        child=manifest.implementation_anchor,
        expected_paths=implementation_paths,
        label="implementation commit",
    )
    _verify_direct_parent_and_paths(
        repository_root=repository_root,
        parent=manifest.implementation_anchor,
        child=manifest.translation_audit_anchor,
        expected_paths=frozenset({TRANSLATION_AUDIT_RELATIVE.as_posix()}),
        label="translation-audit commit",
    )
    _verify_direct_parent_and_paths(
        repository_root=repository_root,
        parent=manifest.translation_audit_anchor,
        child=execution_anchor,
        expected_paths=frozenset({EXECUTION_MANIFEST_RELATIVE.as_posix()}),
        label="execution-manifest commit",
    )


def _verify_execution_manifest_binding(
    *,
    manifest: VerifiedManifest,
    repository_root: Path,
    execution_anchor: str,
) -> str:
    expected_path = (repository_root / EXECUTION_MANIFEST_RELATIVE).resolve()
    if _canonical_path(manifest.path) != _canonical_path(expected_path):
        raise RunnerContractError(
            "execution manifest must be the fixed repository-local path "
            f"{expected_path}"
        )
    relative = EXECUTION_MANIFEST_RELATIVE.as_posix()
    if not _git_diff_is_clean_at_anchor(
        repository_root,
        execution_anchor,
        (relative,),
    ):
        raise RunnerContractError(
            "execution manifest differs from the execution-manifest HEAD blob"
        )
    return _sha256(expected_path)


def _verify_translation_audit_binding(
    *,
    manifest: VerifiedManifest,
    repository_root: Path,
) -> None:
    expected_path = repository_root / TRANSLATION_AUDIT_RELATIVE
    if _canonical_path(manifest.translation_audit_path) != _canonical_path(
        expected_path
    ):
        raise RunnerContractError(
            "translation audit path must be repository-root "
            "CGP_001_TRANSLATION_AUDIT.md"
        )
    relative = expected_path.relative_to(repository_root).as_posix()
    if not _git_diff_is_clean_at_anchor(
        repository_root,
        manifest.translation_audit_anchor,
        (relative,),
    ):
        raise RunnerContractError(
            "translation audit artifact differs from translation_audit_anchor"
        )
    try:
        nonempty_lines = tuple(
            line.strip()
            for line in expected_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    except (OSError, UnicodeError) as error:
        raise RunnerContractError("cannot read translation audit artifact") from error
    expected_header = (
        "# CGP-001 Translation Audit",
        "A_TRANS=PASS",
        f"PREREGISTRATION_ANCHOR={PREREGISTRATION_ANCHOR}",
        f"IMPLEMENTATION_ANCHOR={manifest.implementation_anchor}",
    )
    if nonempty_lines[:4] != expected_header:
        raise RunnerContractError(
            "translation audit artifact lacks the exact PASS authority header"
        )


def _verify_arm_artifact_paths(
    *,
    manifest: VerifiedManifest,
    repository_root: Path,
    arm: str,
    output_path: Path,
) -> Path:
    expected_outputs = {
        name: (
            repository_root
            / "experiments"
            / "cgp_001"
            / "results"
            / "raw"
            / f"{slug}.json"
        ).resolve()
        for name, slug in _ARM_SLUGS.items()
    }
    expected_attempts = {
        name: (
            repository_root
            / "experiments"
            / "cgp_001"
            / "results"
            / "attempts"
            / f"{slug}.attempt.json"
        ).resolve()
        for name, slug in _ARM_SLUGS.items()
    }
    for name in ARMS:
        if _canonical_path(manifest.arm_output_paths[name]) != _canonical_path(
            expected_outputs[name]
        ):
            raise RunnerContractError(
                f"manifest output path for {name} is not the frozen path"
            )
        if _canonical_path(manifest.arm_attempt_paths[name]) != _canonical_path(
            expected_attempts[name]
        ):
            raise RunnerContractError(
                f"manifest attempt path for {name} is not the frozen path"
            )
    if _canonical_path(output_path) != _canonical_path(expected_outputs[arm]):
        raise RunnerContractError(
            f"--output does not match the manifest-bound path for {arm}"
        )
    return expected_attempts[arm]


def _verify_exact_allowed_file_set(
    *,
    manifest: VerifiedManifest,
    repository_root: Path,
    fs_root: Path,
    nss_root: Path,
) -> None:
    expected = {
        *(_canonical_path(path) for path in _implementation_paths(repository_root)),
        *(_canonical_path(fs_root / relative) for relative in FS_FILES),
        *(_canonical_path(nss_root / relative) for relative in NSS_FILES),
        _canonical_path(manifest.translation_audit_path),
    }
    observed = set(manifest.allowed_files)
    if observed != expected:
        missing = sorted(expected - observed)
        extra = sorted(observed - expected)
        raise RunnerContractError(
            "allowed_files is not the exact frozen execution set; "
            f"missing={missing!r}, extra={extra!r}"
        )


def _load_experiment_exact(path: Path) -> object:
    """Execute the SHA-bound CGP module from its exact verified path."""

    resolved = path.resolve()
    module_name = "_cgp001_frozen_implementation"
    spec = importlib.util.spec_from_file_location(module_name, resolved)
    if spec is None or spec.loader is None:
        raise RunnerContractError(f"cannot construct exact import spec for {resolved}")
    module = importlib.util.module_from_spec(spec)
    previous = sys.modules.get(module_name)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        if previous is None:
            sys.modules.pop(module_name, None)
        else:
            sys.modules[module_name] = previous
        raise
    observed_file = getattr(module, "__file__", None)
    if observed_file is None or _canonical_path(observed_file) != _canonical_path(
        resolved
    ):
        raise RunnerContractError("exact CGP import resolved to an unexpected file")
    return module


def _verify_fresh_interpreter_module_state() -> None:
    forbidden = {
        "_cgp001_frozen_implementation",
        "_cgp001_frozen_fs007_meta_language_repair",
        "negative_space_search",
        "negative_space_search.operator_discovery_v0_7",
        "negative_space_search.language_boundary_v0_6",
        "negative_space_search.basis_v0_5",
        "negative_space_search.representation_v0_4",
    }
    present = sorted(name for name in forbidden if name in sys.modules)
    if present:
        raise RunnerContractError(
            f"runner requires a fresh child interpreter; preloaded modules={present!r}"
        )


def _write_output_exclusively(path: Path, document: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(document, handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as error:
        raise RunnerContractError(f"refusing to overwrite output: {path}") from error


def _verify_new_artifact_target(path: Path, *, role: str) -> None:
    if path.exists():
        raise RunnerContractError(
            f"refusing to execute with an existing {role}: {path}"
        )
    ancestor = path.parent
    while not ancestor.exists() and ancestor != ancestor.parent:
        ancestor = ancestor.parent
    if ancestor.exists() and not ancestor.is_dir():
        raise RunnerContractError(f"{role} ancestor is not a directory: {ancestor}")


def _write_attempt_exclusively(
    path: Path,
    *,
    arm: str,
    manifest: VerifiedManifest,
    execution_anchor: str,
    execution_manifest_sha256: str,
    output_path: Path,
) -> None:
    """Durably consume the one allowed attempt before outcome-bearing work."""

    marker = {
        "schema_version": "cgp-001-arm-attempt-v1",
        "status": "STARTED_IRREVERSIBLE_ATTEMPT",
        "arm": arm,
        "preregistration_anchor": PREREGISTRATION_ANCHOR,
        "implementation_anchor": manifest.implementation_anchor,
        "translation_audit_anchor": manifest.translation_audit_anchor,
        "execution_anchor": execution_anchor,
        "execution_manifest_sha256": execution_manifest_sha256,
        "output_path": os.fspath(output_path),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(marker, handle, indent=2, sort_keys=True, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as error:
        raise RunnerContractError(
            f"arm attempt has already been consumed: {path}"
        ) from error


def _require_exact_keys(
    value: Mapping[str, object],
    expected: set[str],
    *,
    label: str,
) -> None:
    observed = set(value)
    if observed != expected:
        raise RunnerContractError(
            f"{label} keys mismatch; "
            f"missing={sorted(expected - observed)!r}, "
            f"extra={sorted(observed - expected)!r}"
        )


def _require_plain_int(value: object, *, label: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise RunnerContractError(f"{label} must be an integer >= {minimum}")
    return value


def _require_finite_number(value: object, *, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise RunnerContractError(f"{label} must be a finite number")
    converted = float(value)
    if not math.isfinite(converted):
        raise RunnerContractError(f"{label} must be a finite number")
    return converted


def _validate_json_value(value: object, *, label: str) -> None:
    active: set[int] = set()

    def visit(item: object, path: str, depth: int) -> None:
        if depth > 64:
            raise RunnerContractError(f"{path} exceeds the JSON nesting limit")
        if item is None or isinstance(item, (str, bool)):
            return
        if type(item) is int:
            return
        if type(item) is float:
            if not math.isfinite(item):
                raise RunnerContractError(f"{path} contains a non-finite float")
            return
        if isinstance(item, list):
            identity = id(item)
            if identity in active:
                raise RunnerContractError(f"{path} contains a container cycle")
            active.add(identity)
            try:
                for index, child in enumerate(item):
                    visit(child, f"{path}[{index}]", depth + 1)
            finally:
                active.remove(identity)
            return
        if isinstance(item, dict):
            identity = id(item)
            if identity in active:
                raise RunnerContractError(f"{path} contains a container cycle")
            active.add(identity)
            try:
                for key, child in item.items():
                    if not isinstance(key, str):
                        raise RunnerContractError(f"{path} contains a non-string key")
                    visit(child, f"{path}.{key}", depth + 1)
            finally:
                active.remove(identity)
            return
        raise RunnerContractError(
            f"{path} contains non-JSON value type {type(item).__name__}"
        )

    visit(value, label, 0)


def _validate_search_result(value: object, *, label: str) -> None:
    if value is None:
        return
    if not isinstance(value, dict):
        raise RunnerContractError(f"{label} must be an object or null")
    _require_exact_keys(
        value,
        {"accuracy", "program", "program_nodes", "semantics"},
        label=label,
    )
    accuracy = _require_finite_number(value["accuracy"], label=f"{label}.accuracy")
    if not 0.0 <= accuracy <= 1.0:
        raise RunnerContractError(f"{label}.accuracy must lie in [0, 1]")
    if not isinstance(value["program"], str) or not value["program"]:
        raise RunnerContractError(f"{label}.program must be a non-empty string")
    _require_plain_int(value["program_nodes"], label=f"{label}.program_nodes", minimum=1)
    semantics = value["semantics"]
    if (
        not isinstance(semantics, list)
        or len(semantics) != 8
        or any(type(bit) is not int or bit not in (0, 1) for bit in semantics)
    ):
        raise RunnerContractError(f"{label}.semantics must be eight integer bits")


def _validate_condition(
    value: object,
    *,
    index: int,
    expected_allocation: str,
) -> None:
    label = f"arm_result.conditions[{index}]"
    if not isinstance(value, dict):
        raise RunnerContractError(f"{label} must be an object")
    _require_exact_keys(value, _CONDITION_FIELDS, label=label)
    if value["index"] != index or value["condition_name"] != _CONDITION_NAMES[index]:
        raise RunnerContractError(f"{label} has the wrong frozen identity/order")
    if value["allocation"] != expected_allocation:
        raise RunnerContractError(f"{label}.allocation disagrees with the applied vector")
    if value["m1_status"] not in ("EVALUATED", "NOT_EVALUATED"):
        raise RunnerContractError(f"{label}.m1_status is invalid")
    if type(value["fanout_enabled"]) is not bool:
        raise RunnerContractError(f"{label}.fanout_enabled must be boolean")
    for field in ("task_seed", "probe_seed", "probe_count", "heldout_count", "score_calls"):
        _require_plain_int(value[field], label=f"{label}.{field}")
    if value["heldout_seed"] is not None:
        _require_plain_int(value["heldout_seed"], label=f"{label}.heldout_seed")
    repair_cost = _require_finite_number(value["repair_cost"], label=f"{label}.repair_cost")
    if repair_cost < 0.0:
        raise RunnerContractError(f"{label}.repair_cost must be non-negative")
    if value["estimated_repair_value"] is not None:
        _require_finite_number(
            value["estimated_repair_value"],
            label=f"{label}.estimated_repair_value",
        )
    if value["heldout_accuracy"] is not None:
        heldout_accuracy = _require_finite_number(
            value["heldout_accuracy"],
            label=f"{label}.heldout_accuracy",
        )
        if not 0.0 <= heldout_accuracy <= 1.0:
            raise RunnerContractError(f"{label}.heldout_accuracy must lie in [0, 1]")
    for field in ("base_result", "fanout_result", "selected_result"):
        _validate_search_result(value[field], label=f"{label}.{field}")
    if value["base_result"] is None or value["selected_result"] is None:
        raise RunnerContractError(f"{label} must contain base and selected results")
    if value["nss"] is not None and not isinstance(value["nss"], dict):
        raise RunnerContractError(f"{label}.nss must be an object or null")
    for field in ("state_before_authority", "state_after_authority"):
        if value[field] is not None and not isinstance(value[field], dict):
            raise RunnerContractError(f"{label}.{field} must be an object or null")


def _validate_arm_result(arm_result: object, *, arm: str) -> dict[str, object]:
    """Validate evidence post-trace and before snapshot/envelope serialization."""

    if not isinstance(arm_result, dict):
        raise RunnerContractError("run_arm must return a plain JSON object")
    _validate_json_value(arm_result, label="arm_result")
    _require_exact_keys(arm_result, _ARM_RESULT_FIELDS, label="arm_result")
    if arm_result["schema_version"] != "cgp-001-arm-v1":
        raise RunnerContractError("arm_result schema_version mismatch")
    if arm_result["arm"] != arm:
        raise RunnerContractError("arm_result arm mismatch")

    parent_commits = arm_result["parent_commits"]
    if not isinstance(parent_commits, dict):
        raise RunnerContractError("arm_result.parent_commits must be an object")
    if parent_commits != {"nss": NSS_COMMIT, "fs": FS_COMMIT}:
        raise RunnerContractError("arm_result parent commit binding mismatch")

    source_verification = arm_result["source_verification"]
    if not isinstance(source_verification, dict):
        raise RunnerContractError("arm_result.source_verification must be an object")
    required_source_fields = {
        "nss_commit",
        "fs_commit",
        "nss_file_hashes",
        "fs_file_hashes",
        "current_language_expression_count",
        "read_once_program_count",
        "fanout_program_count",
        "eight_pattern_signature_m0_equivalence",
    }
    _require_exact_keys(
        source_verification,
        required_source_fields,
        label="arm_result.source_verification",
    )
    if (
        source_verification["nss_commit"] != NSS_COMMIT
        or source_verification["fs_commit"] != FS_COMMIT
        or source_verification["current_language_expression_count"] != 78
        or source_verification["read_once_program_count"] != 94
        or source_verification["fanout_program_count"] != 127
        or source_verification["eight_pattern_signature_m0_equivalence"] is not True
    ):
        raise RunnerContractError("arm_result source verification values mismatch")

    unrotated = arm_result["unrotated_allocation_vector"]
    applied = arm_result["applied_allocation_vector"]
    if not isinstance(applied, list) or len(applied) != 4:
        raise RunnerContractError("applied allocation vector must contain four decisions")
    if any(decision not in ("INVOKE", "SKIP") for decision in applied):
        raise RunnerContractError("applied allocation vector contains an invalid decision")
    if arm == "FS_ONLY":
        if unrotated is not None or applied != ["INVOKE"] * 4:
            raise RunnerContractError("FS_ONLY allocation vectors violate the frozen schema")
    else:
        if not isinstance(unrotated, list) or len(unrotated) != 4:
            raise RunnerContractError(
                "NSS arm unrotated allocation vector must contain four decisions"
            )
        if any(decision not in ("INVOKE", "SKIP") for decision in unrotated):
            raise RunnerContractError("unrotated vector contains an invalid decision")
        expected_applied = (
            [unrotated[-1], *unrotated[:-1]]
            if arm == "SHUFFLED_NSS_TO_FS"
            else unrotated
        )
        if applied != expected_applied:
            raise RunnerContractError("applied allocation vector violates arm semantics")

    conditions = arm_result["conditions"]
    if not isinstance(conditions, list) or len(conditions) != 4:
        raise RunnerContractError("arm_result.conditions must contain exactly four records")
    for index, condition in enumerate(conditions):
        _validate_condition(condition, index=index, expected_allocation=applied[index])
        if arm == "FS_ONLY" and condition["nss"] is not None:
            raise RunnerContractError("FS_ONLY condition unexpectedly contains NSS evidence")
        if arm != "FS_ONLY" and condition["nss"] is None:
            raise RunnerContractError("NSS arm condition is missing its gate record")

    later = arm_result["later_family_reuse"]
    if not isinstance(later, dict):
        raise RunnerContractError("later_family_reuse must be an object")
    _require_exact_keys(
        later,
        {
            "probe_seed",
            "heldout_seed",
            "probe_count",
            "heldout_count",
            "result",
            "heldout_accuracy",
            "generator",
        },
        label="arm_result.later_family_reuse",
    )
    for field in ("probe_seed", "heldout_seed", "probe_count", "heldout_count"):
        _require_plain_int(later[field], label=f"later_family_reuse.{field}")
    _validate_search_result(later["result"], label="later_family_reuse.result")
    if later["result"] is None:
        raise RunnerContractError("later_family_reuse.result must be present")
    reuse_accuracy = _require_finite_number(
        later["heldout_accuracy"], label="later_family_reuse.heldout_accuracy"
    )
    if not 0.0 <= reuse_accuracy <= 1.0:
        raise RunnerContractError("later_family_reuse.heldout_accuracy must lie in [0, 1]")
    if later["generator"] not in ("read_once", "fanout_allowed"):
        raise RunnerContractError("later_family_reuse.generator is invalid")

    diagnostics = arm_result["operation_diagnostics"]
    if not isinstance(diagnostics, dict):
        raise RunnerContractError("operation_diagnostics must be an object")
    _require_exact_keys(
        diagnostics,
        _OPERATION_DIAGNOSTIC_FIELDS,
        label="arm_result.operation_diagnostics",
    )
    for key, value in diagnostics.items():
        if key not in ("selected_node_count", "generator_state", "stages"):
            _require_plain_int(value, label=f"operation_diagnostics.{key}")
    if diagnostics["generator_state"] != arm_result["generator_state"]:
        raise RunnerContractError("diagnostic/top-level generator_state mismatch")
    if diagnostics["stages"] != arm_result["stages"]:
        raise RunnerContractError("diagnostic/top-level stages mismatch")
    if not isinstance(arm_result["generator_state"], dict):
        raise RunnerContractError("generator_state must be an object")
    if not isinstance(arm_result["stages"], list) or any(
        not isinstance(stage, str) for stage in arm_result["stages"]
    ):
        raise RunnerContractError("stages must be a list of strings")
    return arm_result


def _parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--arm", required=True, choices=ARMS)
    parser.add_argument("--fs-root", required=True, type=Path)
    parser.add_argument("--nss-root", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    global _RUNNER_MAIN_STARTED
    if _RUNNER_MAIN_STARTED:
        raise RunnerContractError("runner main may execute only once per interpreter")
    _RUNNER_MAIN_STARTED = True

    # Frozen bootstrap boundary: do not verify files or import experiment code
    # before the counter is active.
    args = _parse_args(argv)
    fs_root = args.fs_root.resolve()
    nss_root = args.nss_root.resolve()
    manifest_path = args.manifest.resolve()
    output_path = args.output.resolve()
    repository_root = Path(__file__).resolve().parents[2]
    expected_manifest_path = (repository_root / EXECUTION_MANIFEST_RELATIVE).resolve()
    if _canonical_path(manifest_path) != _canonical_path(expected_manifest_path):
        raise RunnerContractError(
            f"--manifest must be the fixed repository-local path {expected_manifest_path}"
        )
    bootstrap = _read_manifest_bootstrap(manifest_path)
    counter = OpcodeCounter(
        allowed_files=bootstrap.allowed_files,
        project_roots=(repository_root, fs_root, nss_root),
    )
    started_ns = time.perf_counter_ns()

    counter.start()
    try:
        manifest = _read_manifest_verified(manifest_path, bootstrap)
        _verify_runtime()
        _verify_allowed_files(manifest)
        _verify_runner_is_allowed(
            allowed_files=manifest.allowed_files,
            repository_root=repository_root,
        )
        observed_execution_anchor = _git_head(repository_root)
        _verify_frozen_lineage(
            manifest=manifest,
            repository_root=repository_root,
            execution_anchor=observed_execution_anchor,
        )
        execution_manifest_sha256 = _verify_execution_manifest_binding(
            manifest=manifest,
            repository_root=repository_root,
            execution_anchor=observed_execution_anchor,
        )
        _verify_implementation_binding(
            repository_root=repository_root,
            implementation_anchor=manifest.implementation_anchor,
        )
        _verify_translation_audit_binding(
            manifest=manifest,
            repository_root=repository_root,
        )
        _verify_exact_allowed_file_set(
            manifest=manifest,
            repository_root=repository_root,
            fs_root=fs_root,
            nss_root=nss_root,
        )
        attempt_path = _verify_arm_artifact_paths(
            manifest=manifest,
            repository_root=repository_root,
            arm=args.arm,
            output_path=output_path,
        )
        _verify_new_artifact_target(output_path, role="arm output")
        _verify_new_artifact_target(attempt_path, role="arm attempt marker")
        _verify_checkout(
            root=fs_root,
            expected_commit=FS_COMMIT,
            expected_files=FS_FILES,
            allowed_files=manifest.allowed_files,
        )
        _verify_checkout(
            root=nss_root,
            expected_commit=NSS_COMMIT,
            expected_files=NSS_FILES,
            allowed_files=manifest.allowed_files,
        )
        _verify_fresh_interpreter_module_state()

        with counter.phase("C_generator_construct"):
            experiment = _load_experiment_exact(
                repository_root / "experiments" / "cgp_001" / "cgp_001.py"
            )

        run_arm = getattr(experiment, "run_arm", None)
        if not callable(run_arm):
            raise RunnerContractError("CGP implementation does not expose callable run_arm")
        issue_execution_capability = getattr(
            experiment,
            "_issue_execution_capability",
            None,
        )
        if not callable(issue_execution_capability):
            raise RunnerContractError(
                "CGP implementation does not expose its private capability issuer"
            )

        execution_capability = issue_execution_capability(
            arm=args.arm,
            fs_root=fs_root,
            nss_root=nss_root,
            preregistration_anchor=PREREGISTRATION_ANCHOR,
            implementation_anchor=manifest.implementation_anchor,
            translation_audit_anchor=manifest.translation_audit_anchor,
            execution_anchor=observed_execution_anchor,
        )
        _write_attempt_exclusively(
            attempt_path,
            arm=args.arm,
            manifest=manifest,
            execution_anchor=observed_execution_anchor,
            execution_manifest_sha256=execution_manifest_sha256,
            output_path=output_path,
        )

        arm_result = run_arm(
            arm=args.arm,
            fs_root=fs_root,
            nss_root=nss_root,
            phase=counter.phase,
            execution_capability=execution_capability,
        )
    finally:
        counter.stop()

    stopped_ns = time.perf_counter_ns()
    arm_result = _validate_arm_result(arm_result, arm=args.arm)
    snapshot = counter.snapshot()
    envelope: dict[str, Any] = {
        "schema_version": "cgp-001-opcode-arm-v1",
        "preregistration_anchor": PREREGISTRATION_ANCHOR,
        "implementation_anchor": manifest.implementation_anchor,
        "translation_audit_anchor": manifest.translation_audit_anchor,
        "translation_audit_sha256": manifest.translation_audit_sha256,
        "execution_anchor": observed_execution_anchor,
        "execution_manifest_path": os.fspath(manifest.path),
        "execution_manifest_sha256": execution_manifest_sha256,
        "attempt_path": os.fspath(attempt_path),
        "arm": args.arm,
        "arm_result": arm_result,
        "opcode_cost": snapshot.to_dict(),
        "wall_clock_ns": stopped_ns - started_ns,
    }
    _write_output_exclusively(output_path, envelope)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
