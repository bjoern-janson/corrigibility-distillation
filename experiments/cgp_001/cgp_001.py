"""Frozen CGP-001 apparatus.

This module implements the preregistered translation, the literal NSS v0.7
allocation mechanism, and the FS007 execution seam.  Importing it has no
outcome-bearing side effects, and it intentionally provides no command-line
entry point.  CGP arms may be entered only through :func:`run_arm` after the
apparatus and translation audit have been frozen.
"""

from __future__ import annotations

from contextlib import AbstractContextManager
from dataclasses import asdict, dataclass
from hashlib import sha256
import importlib
import importlib.machinery
import importlib.util
from itertools import product
from pathlib import Path
import subprocess
import sys
from types import ModuleType
from typing import Any, Callable, Iterable, Mapping, Sequence


NSS_COMMIT = "307c24576ebea951be04d187c61e7428f4f0e184"
FS_COMMIT = "2f4ca824e02b89df0c23d64de312c4f93a4c8a41"
PREREGISTRATION_ANCHOR = "669a94aac6c07484323dde3b0fb64df5b9ec4bca"

NSS_HASHES: Mapping[str, str] = {
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

FS_HASHES: Mapping[str, str] = {
    "experiments/meta_language_repair.py": (
        "f23a48e06802a08441eed492752fa5223e564587ec78b2f447ba464737aa37db"
    ),
    "experiments/meta_language_repair.md": (
        "7f6ad9e3bdf0c89d3233f518f79603b20a2b722e148323bcd8c4bb20de76e804"
    ),
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

ARM_NAMES = (
    "FS_ONLY",
    "NSS_ONLY",
    "NSS_TO_FS",
    "SHUFFLED_NSS_TO_FS",
)

NOT_EVALUATED = "NOT_EVALUATED"
INVOKE = "INVOKE"
SKIP = "SKIP"


class TranslationContractError(ValueError):
    """The pure FS-to-NSS record translation failed closed."""


class ApparatusVerificationError(RuntimeError):
    """A frozen parent source or source-level invariant did not verify."""


class ArmContractError(RuntimeError):
    """An arm request would violate the frozen execution contract."""


_EXECUTION_CAPABILITY_ISSUER = object()


def _is_lower_git_sha(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 40
        and all(character in "0123456789abcdef" for character in value)
    )


class _ExecutionCapability:
    """Opaque, runner-issued, one-use authorization for one frozen arm.

    This is a protocol boundary rather than a security sandbox.  Its private
    issuer is called by ``opcode_runner`` only after that runner has verified
    the committed PASS translation audit and the full implementation/audit/
    execution lineage.  Binding the arm and parent roots prevents accidental
    reuse for a different substantive execution.
    """

    __slots__ = (
        "_issuer",
        "_arm",
        "_fs_root",
        "_nss_root",
        "_preregistration_anchor",
        "_implementation_anchor",
        "_translation_audit_anchor",
        "_execution_anchor",
        "_consumed",
    )

    def __init__(
        self,
        *,
        issuer: object,
        arm: str,
        fs_root: Path,
        nss_root: Path,
        preregistration_anchor: str,
        implementation_anchor: str,
        translation_audit_anchor: str,
        execution_anchor: str,
    ) -> None:
        if issuer is not _EXECUTION_CAPABILITY_ISSUER:
            raise ArmContractError("execution capability issuer is not authorized")
        if arm not in ARM_NAMES:
            raise ArmContractError(f"cannot issue capability for unknown arm: {arm}")
        if preregistration_anchor != PREREGISTRATION_ANCHOR:
            raise ArmContractError("execution capability preregistration mismatch")
        for label, anchor in (
            ("implementation", implementation_anchor),
            ("translation audit", translation_audit_anchor),
            ("execution", execution_anchor),
        ):
            if not _is_lower_git_sha(anchor):
                raise ArmContractError(
                    f"execution capability {label} anchor is not lowercase 40-hex"
                )

        self._issuer = issuer
        self._arm = arm
        self._fs_root = Path(fs_root).resolve()
        self._nss_root = Path(nss_root).resolve()
        self._preregistration_anchor = preregistration_anchor
        self._implementation_anchor = implementation_anchor
        self._translation_audit_anchor = translation_audit_anchor
        self._execution_anchor = execution_anchor
        self._consumed = False

    def _consume(self, *, arm: str, fs_root: Path, nss_root: Path) -> None:
        if self._issuer is not _EXECUTION_CAPABILITY_ISSUER:
            raise ArmContractError("execution capability issuer binding is invalid")
        if self._consumed:
            raise ArmContractError("execution capability has already been consumed")

        # Consume before validating request bindings.  A malformed attempt may
        # not retain a reusable authorization for a second substantive call.
        self._consumed = True
        if self._arm != arm:
            raise ArmContractError("execution capability arm binding mismatch")
        if self._fs_root != Path(fs_root).resolve():
            raise ArmContractError("execution capability FS-root binding mismatch")
        if self._nss_root != Path(nss_root).resolve():
            raise ArmContractError("execution capability NSS-root binding mismatch")

    def __copy__(self) -> object:
        raise ArmContractError("execution capability cannot be copied")

    def __deepcopy__(self, memo: object) -> object:
        del memo
        raise ArmContractError("execution capability cannot be copied")

    def __reduce__(self) -> object:
        raise ArmContractError("execution capability cannot be serialized")


def _issue_execution_capability(
    *,
    arm: str,
    fs_root: Path,
    nss_root: Path,
    preregistration_anchor: str,
    implementation_anchor: str,
    translation_audit_anchor: str,
    execution_anchor: str,
) -> object:
    """Private runner bridge; issuance is not itself an execution entry point."""

    return _ExecutionCapability(
        issuer=_EXECUTION_CAPABILITY_ISSUER,
        arm=arm,
        fs_root=fs_root,
        nss_root=nss_root,
        preregistration_anchor=preregistration_anchor,
        implementation_anchor=implementation_anchor,
        translation_audit_anchor=translation_audit_anchor,
        execution_anchor=execution_anchor,
    )


@dataclass(frozen=True)
class VerifiedParents:
    """Exact imported parent modules after source verification."""

    fs: ModuleType
    nss_language: ModuleType
    nss_operator: ModuleType
    fs_root: Path
    nss_root: Path
    verification_diagnostics: Mapping[str, int]


@dataclass(frozen=True)
class ConditionSpec:
    index: int
    name: str
    family_name: str
    repair_cost: float
    task_seed: int
    probe_seed: int
    heldout_seed: int | None


CONDITION_SPECS = (
    ConditionSpec(0, "INSUFFICIENT_LOW", "NEEDS_FANOUT", 5.0, 7, 17, 31),
    ConditionSpec(1, "INSUFFICIENT_HIGH", "NEEDS_FANOUT", 20.0, 7, 17, 31),
    ConditionSpec(2, "SUFFICIENT_LOW", "BASE_SUFFICIENT", 5.0, 7, 17, 31),
    ConditionSpec(3, "NOVEL_REUSE_REPAIR", "NEEDS_FANOUT", 5.0, 13, 41, None),
)


@dataclass
class _ConditionRuntime:
    spec: ConditionSpec
    probe: list[Any]
    heldout: list[Any] | None
    learner: Any
    base_result: Any
    fanout_result: Any | None = None
    selected_result: Any | None = None
    estimated_repair_value: float | None = None
    m1_status: str = NOT_EVALUATED
    allocation: str | None = None
    nss_record: dict[str, Any] | None = None
    heldout_accuracy: float | None = None
    state_before_authority: dict[str, Any] | None = None
    state_after_authority: dict[str, Any] | None = None


def _digest(path: Path) -> str:
    hasher = sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def _git_head(root: Path) -> str:
    try:
        completed = subprocess.run(
            [
                "git",
                "-c",
                f"safe.directory={root.resolve().as_posix()}",
                "-C",
                str(root),
                "rev-parse",
                "HEAD",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ApparatusVerificationError(
            f"cannot resolve frozen checkout commit: {root}"
        ) from exc
    return completed.stdout.strip()


def _verify_checkout(
    root: Path,
    *,
    expected_commit: str,
    expected_hashes: Mapping[str, str],
) -> None:
    if not root.is_dir():
        raise ApparatusVerificationError(f"checkout is not a directory: {root}")
    head = _git_head(root)
    if head != expected_commit:
        raise ApparatusVerificationError(
            f"checkout commit mismatch at {root}: expected {expected_commit}, got {head}"
        )
    for relative, expected in expected_hashes.items():
        path = root / relative
        if not path.is_file():
            raise ApparatusVerificationError(f"missing frozen source: {path}")
        observed = _digest(path)
        if observed != expected:
            raise ApparatusVerificationError(
                f"source hash mismatch for {path}: expected {expected}, got {observed}"
            )


def _assert_module_path(module: ModuleType, expected: Path) -> None:
    observed_name = getattr(module, "__file__", None)
    if observed_name is None or Path(observed_name).resolve() != expected.resolve():
        raise ApparatusVerificationError(
            f"module path mismatch for {module.__name__}: expected {expected}, got {observed_name}"
        )


def _import_nss(nss_root: Path) -> tuple[ModuleType, ModuleType]:
    source_root = (nss_root / "src").resolve()
    package_root = (source_root / "negative_space_search").resolve()
    package_name = "negative_space_search"

    # The repository package initializer imports additional, unfrozen modules.
    # Install a namespace package rooted at the pinned package directory so
    # relative imports load only the four SHA-bound NSS modules and never
    # execute ``negative_space_search/__init__.py``.
    existing_package = sys.modules.get(package_name)
    if existing_package is None:
        package = ModuleType(package_name)
        package.__package__ = package_name
        package.__path__ = [str(package_root)]  # type: ignore[attr-defined]
        package_spec = importlib.machinery.ModuleSpec(
            package_name,
            loader=None,
            is_package=True,
        )
        package_spec.submodule_search_locations = [str(package_root)]
        package.__spec__ = package_spec
        sys.modules[package_name] = package
    else:
        existing_paths = tuple(
            Path(item).resolve()
            for item in getattr(existing_package, "__path__", ())
        )
        if existing_paths != (package_root,) or getattr(existing_package, "__file__", None):
            raise ApparatusVerificationError(
                "conflicting negative_space_search package is already imported"
            )

    language = importlib.import_module(
        "negative_space_search.language_boundary_v0_6"
    )
    operator = importlib.import_module(
        "negative_space_search.operator_discovery_v0_7"
    )
    _assert_module_path(
        language,
        nss_root / "src/negative_space_search/language_boundary_v0_6.py",
    )
    _assert_module_path(
        operator,
        nss_root / "src/negative_space_search/operator_discovery_v0_7.py",
    )
    _assert_module_path(
        importlib.import_module("negative_space_search.basis_v0_5"),
        nss_root / "src/negative_space_search/basis_v0_5.py",
    )
    _assert_module_path(
        importlib.import_module("negative_space_search.representation_v0_4"),
        nss_root / "src/negative_space_search/representation_v0_4.py",
    )
    return language, operator


_FS_MODULE_NAME = "_cgp001_frozen_fs007_meta_language_repair"


def _import_fs(fs_root: Path) -> ModuleType:
    expected = (fs_root / "experiments/meta_language_repair.py").resolve()
    existing = sys.modules.get(_FS_MODULE_NAME)
    if existing is not None:
        _assert_module_path(existing, expected)
        return existing

    spec = importlib.util.spec_from_file_location(_FS_MODULE_NAME, expected)
    if spec is None or spec.loader is None:
        raise ApparatusVerificationError(f"cannot load frozen FS module: {expected}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[_FS_MODULE_NAME] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(_FS_MODULE_NAME, None)
        raise
    _assert_module_path(module, expected)
    return module


def _require_int_bit(value: Any, label: str) -> int:
    if type(value) is not int or value not in (0, 1):
        raise TranslationContractError(f"{label} must be integer 0 or 1")
    return value


def _validate_record(record: Any) -> tuple[tuple[int, int, int], int, int]:
    try:
        bits = record.bits
        task = record.task
        args = task.args
        hidden = record.hidden
        raw_id = record.raw_id
    except AttributeError as exc:
        raise TranslationContractError("malformed FS probe record") from exc

    if not isinstance(bits, tuple) or len(bits) != 18:
        raise TranslationContractError("bits must be a tuple of length 18")
    normalized_bits = tuple(
        _require_int_bit(value, f"bits[{index}]")
        for index, value in enumerate(bits)
    )
    if not isinstance(args, tuple) or len(args) != 3:
        raise TranslationContractError("task.args must be a tuple of arity three")
    if any(type(index) is not int for index in args):
        raise TranslationContractError("task indices must be integers")
    if len(set(args)) != 3:
        raise TranslationContractError("task indices must be distinct")
    if any(index < 0 or index >= 18 for index in args):
        raise TranslationContractError("task index out of range")
    normalized_hidden = _require_int_bit(hidden, "hidden")
    if type(raw_id) is not int:
        raise TranslationContractError("raw_id must be an integer")

    local = tuple(normalized_bits[index] for index in args)
    return local, normalized_hidden, raw_id  # type: ignore[return-value]


def translate_examples(examples: Sequence[Any]) -> tuple[Any, ...]:
    """Apply the frozen, stateless FS-record to NSS-episode translation.

    The function accepts exactly the released probe-record sequence.  It does
    not receive a condition, family, model result, cost, horizon, target,
    persistence state, or any downstream observation.
    """

    if isinstance(examples, (str, bytes)):
        raise TranslationContractError("examples must be a record sequence")
    try:
        records = tuple(examples)
    except TypeError as exc:
        raise TranslationContractError("examples must be a record sequence") from exc
    if not records:
        raise TranslationContractError("empty probe sequence")

    validated: list[tuple[tuple[int, int, int], int, int]] = []
    seen_raw_ids: set[int] = set()
    for record in records:
        local, hidden, raw_id = _validate_record(record)
        if raw_id in seen_raw_ids:
            raise TranslationContractError(f"duplicate raw_id: {raw_id}")
        seen_raw_ids.add(raw_id)
        validated.append((local, hidden, raw_id))

    validated.sort(key=lambda item: (item[0], item[1], item[2]))
    try:
        language_module = importlib.import_module(
            "negative_space_search.language_boundary_v0_6"
        )
        language_episode = language_module.LanguageEpisode
    except (ImportError, AttributeError) as exc:
        raise ApparatusVerificationError(
            "frozen NSS LanguageEpisode is unavailable; source verification must run first"
        ) from exc

    translated: list[Any] = []
    for sorted_index, (local, hidden, _raw_id) in enumerate(validated, start=1):
        pairs = tuple(
            (0.0, 0.0) if bit == 0 else (0.0, 1.0)
            for bit in local
        )
        x, y, z = local
        translated.append(
            language_episode(
                episode_id=f"cgp001_e{sorted_index:04d}",
                paired_measurements=pairs,
                surface_hint=0.0,
                ordered_trace=(float(x), float(y), float(z), 0.0),
                prediction=0.0,
                outcome=0.0,
                selected_action="fs_probe_record",
                timestamp=sorted_index,
                cost=0.0,
                resolving_probe=f"fs_output_{hidden}",
            )
        )
    return tuple(translated)


def canonical_episode_records(episodes: Iterable[Any]) -> tuple[dict[str, Any], ...]:
    """Return a canonical value-level representation for fixtures and audits."""

    return tuple(asdict(episode) for episode in episodes)


def _verify_signature_equivalence(parents: VerifiedParents) -> dict[str, int]:
    fs = parents.fs
    language = parents.nss_language
    patterns = tuple(product((0, 1), repeat=3))
    examples: list[Any] = []
    for raw_id, values in enumerate(patterns):
        bits = [0] * 18
        for index, value in enumerate(values):
            bits[index] = value
        examples.append(
            fs.Example(
                bits=tuple(bits),
                task=fs.Task((0, 1, 2)),
                hidden=0,
                raw_id=raw_id,
            )
        )

    episodes = translate_examples(examples)
    by_trace = {
        tuple(int(value) for value in episode.ordered_trace[:3]): episode
        for episode in episodes
    }
    if set(by_trace) != set(patterns):
        raise ApparatusVerificationError("translation did not preserve all eight patterns")

    programs = tuple(fs.READ_ONCE_PROGRAMS.values())
    signature_calls = 0
    m0_program_evaluations = 0
    m0_program_node_evaluations = 0
    for left in patterns:
        for right in patterns:
            left_signature = language.current_language_signature(by_trace[left])
            right_signature = language.current_language_signature(by_trace[right])
            signature_calls += 2
            signature_equal = left_signature == right_signature
            full_m0_equal = True
            for program in programs:
                left_value = program.evaluate_local(left)
                right_value = program.evaluate_local(right)
                m0_program_evaluations += 2
                m0_program_node_evaluations += 2 * program.size()
                if left_value != right_value:
                    full_m0_equal = False
                    break
            if signature_equal != full_m0_equal or full_m0_equal != (left == right):
                raise ApparatusVerificationError(
                    "78-expression signature is not equivalent to full M0 on all patterns"
                )
    return {
        "signature_calls": signature_calls,
        "m0_program_evaluations": m0_program_evaluations,
        "m0_program_node_evaluations": m0_program_node_evaluations,
    }


def verify_apparatus(*, fs_root: Path, nss_root: Path) -> VerifiedParents:
    """Verify and import the exact frozen parent apparatus, failing closed."""

    fs_root = Path(fs_root).resolve()
    nss_root = Path(nss_root).resolve()
    _verify_checkout(nss_root, expected_commit=NSS_COMMIT, expected_hashes=NSS_HASHES)
    _verify_checkout(fs_root, expected_commit=FS_COMMIT, expected_hashes=FS_HASHES)

    nss_language, nss_operator = _import_nss(nss_root)
    fs = _import_fs(fs_root)

    if len(nss_language.current_language()) != 78:
        raise ApparatusVerificationError("unexpected NSS current-language count")
    if len(fs.READ_ONCE_PROGRAMS) != 94:
        raise ApparatusVerificationError("unexpected FS M0 program count")
    if len(fs.FANOUT_PROGRAMS) != 127:
        raise ApparatusVerificationError("unexpected FS M1 program count")
    expected_constants = {
        "N_BITS": 18,
        "TRAIN_TASKS": 50,
        "TEST_TASKS": 25,
        "PROBE_PATTERNS_PER_TASK": 4,
        "HELDOUT_EXAMPLES": 3000,
        "FUTURE_HORIZON": 100,
        "MAX_FANOUT_NODES": 9,
    }
    for name, expected in expected_constants.items():
        if getattr(fs, name, None) != expected:
            raise ApparatusVerificationError(
                f"unexpected FS constant {name}: {getattr(fs, name, None)!r}"
            )

    provisional = VerifiedParents(
        fs,
        nss_language,
        nss_operator,
        fs_root,
        nss_root,
        {},
    )
    verification_diagnostics = _verify_signature_equivalence(provisional)
    return VerifiedParents(
        fs,
        nss_language,
        nss_operator,
        fs_root,
        nss_root,
        verification_diagnostics,
    )


def _allocation_record(parents: VerifiedParents, examples: Sequence[Any]) -> dict[str, Any]:
    translated = translate_examples(examples)
    policy = parents.nss_operator.BoundaryGatedGenericSynthesizer()
    policy.fit(translated)
    expanded = int(policy.expanded_signature_count)
    allocation = SKIP if expanded == 0 else INVOKE
    return {
        "allocation": allocation,
        "source_record_count": len(examples),
        "emitted_record_count": len(translated),
        "current_language_expression_count": len(parents.nss_language.current_language()),
        "true_collision_signature_count": int(policy.true_collision_signature_count),
        "detected_collision_signature_count": int(
            policy.detected_collision_signature_count
        ),
        "expanded_signature_count": expanded,
        "adequate_signature_count": int(policy.adequate_signature_count),
        "nss_search_cost": int(policy.search_cost),
        "nss_representation_cost": int(policy.representation_cost),
        "generated_operators": {
            key: value.name
            for key, value in sorted(policy.generated_operators.items())
        },
    }


def nss_allocate(*, parents: VerifiedParents, examples: Sequence[Any]) -> dict[str, Any]:
    """Run one fresh exact NSS v0.7 policy and project search opportunity."""

    return _allocation_record(parents, examples)


def _make_datasets(fs: ModuleType) -> tuple[list[dict[str, Any]], list[Any], list[Any]]:
    conditions: list[dict[str, Any]] = []
    reuse_train_tasks: list[Any] | None = None
    reuse_test_tasks: list[Any] | None = None
    for spec in CONDITION_SPECS:
        train_tasks, test_tasks = fs.make_task_split(seed=spec.task_seed)
        family = getattr(fs.Family, spec.family_name)
        probe = fs.make_probe_examples(train_tasks, family, seed=spec.probe_seed)
        heldout = None
        if spec.heldout_seed is not None:
            heldout = fs.make_heldout_examples(
                test_tasks,
                family,
                seed=spec.heldout_seed,
            )
        conditions.append(
            {
                "spec": spec,
                "probe": probe,
                "heldout": heldout,
            }
        )
        if spec.index == 3:
            reuse_train_tasks = train_tasks
            reuse_test_tasks = test_tasks

    if reuse_train_tasks is None or reuse_test_tasks is None:
        raise ArmContractError("missing frozen reuse condition")
    xor_probe = fs.make_probe_examples(
        reuse_train_tasks,
        fs.Family.NOVEL_XOR,
        seed=43,
    )
    xor_heldout = fs.make_heldout_examples(
        reuse_test_tasks,
        fs.Family.NOVEL_XOR,
        seed=47,
    )
    return conditions, xor_probe, xor_heldout


def _run_m0(fs: ModuleType, datasets: list[dict[str, Any]]) -> list[_ConditionRuntime]:
    runtimes: list[_ConditionRuntime] = []
    for dataset in datasets:
        base, calls = fs.exhaustive_search(fs.READ_ONCE_PROGRAMS.values(), dataset["probe"])
        if calls != 94:
            raise ArmContractError(f"M0 candidate count mismatch: {calls}")
        learner = fs.MetaRepairLearner()
        learner.base_result = base
        learner.selected_result = base
        learner.score_calls = calls
        runtimes.append(
            _ConditionRuntime(
                spec=dataset["spec"],
                probe=dataset["probe"],
                heldout=dataset["heldout"],
                learner=learner,
                base_result=base,
                selected_result=base,
            )
        )
    return runtimes


def _search_m1(fs: ModuleType, runtime: _ConditionRuntime) -> None:
    result, calls = fs.exhaustive_search(fs.FANOUT_PROGRAMS.values(), runtime.probe)
    if calls != 127:
        raise ArmContractError(f"M1 candidate count mismatch: {calls}")
    runtime.learner.fanout_result = result
    runtime.learner.score_calls += calls
    runtime.fanout_result = result
    runtime.m1_status = "EVALUATED"


def _result_semantics(fs: ModuleType, result: Any | None) -> list[int] | None:
    if result is None:
        return None
    return [int(value) for value in fs.semantics(result.program)]


def _state_record(fs: ModuleType, runtime: _ConditionRuntime) -> dict[str, Any]:
    learner = runtime.learner
    return {
        "base_semantics": _result_semantics(fs, learner.base_result),
        "fanout_semantics": _result_semantics(fs, learner.fanout_result),
        "selected_semantics": _result_semantics(fs, learner.selected_result),
        "fanout_enabled": bool(learner.fanout_enabled),
        "score_calls": int(learner.score_calls),
    }


def _apply_fs_authority(fs: ModuleType, runtime: _ConditionRuntime) -> None:
    if runtime.fanout_result is None:
        raise ArmContractError("FS authority cannot evaluate an unscored M1 result")
    runtime.state_before_authority = _state_record(fs, runtime)
    gain = max(0.0, runtime.fanout_result.accuracy - runtime.base_result.accuracy)
    estimated = fs.FUTURE_HORIZON * gain
    runtime.learner.estimated_repair_value = estimated
    runtime.estimated_repair_value = estimated
    if estimated > runtime.spec.repair_cost:
        runtime.learner.fanout_enabled = True
        runtime.learner.selected_result = runtime.fanout_result
    else:
        runtime.learner.selected_result = runtime.base_result
    runtime.selected_result = runtime.learner.selected_result
    runtime.state_after_authority = _state_record(fs, runtime)


def _serialize_search_result(fs: ModuleType, result: Any | None) -> dict[str, Any] | None:
    if result is None:
        return None
    return {
        "accuracy": float(result.accuracy),
        "program": str(result.program),
        "program_nodes": int(result.program.size()),
        "semantics": _result_semantics(fs, result),
    }


def _serialize_condition(fs: ModuleType, runtime: _ConditionRuntime) -> dict[str, Any]:
    return {
        "index": runtime.spec.index,
        "condition_name": runtime.spec.name,
        "family": runtime.spec.family_name,
        "repair_cost": runtime.spec.repair_cost,
        "task_seed": runtime.spec.task_seed,
        "probe_seed": runtime.spec.probe_seed,
        "heldout_seed": runtime.spec.heldout_seed,
        "probe_count": len(runtime.probe),
        "heldout_count": 0 if runtime.heldout is None else len(runtime.heldout),
        "allocation": runtime.allocation,
        "nss": runtime.nss_record,
        "base_result": _serialize_search_result(fs, runtime.base_result),
        "fanout_result": _serialize_search_result(fs, runtime.fanout_result),
        "selected_result": _serialize_search_result(fs, runtime.selected_result),
        "estimated_repair_value": runtime.estimated_repair_value,
        "m1_status": runtime.m1_status,
        "fanout_enabled": bool(runtime.learner.fanout_enabled),
        "score_calls": int(runtime.learner.score_calls),
        "heldout_accuracy": runtime.heldout_accuracy,
        "state_before_authority": runtime.state_before_authority,
        "state_after_authority": runtime.state_after_authority,
    }


def run_arm(
    *,
    arm: str,
    fs_root: Path,
    nss_root: Path,
    phase: Callable[[str], AbstractContextManager[Any]],
    execution_capability: object,
) -> dict[str, Any]:
    """Execute one frozen arm.

    The frozen runner must first verify the committed ``A_trans=PASS`` artifact
    and complete lineage, then issue the opaque one-use capability.  There is
    no unguarded substantive execution entry point.
    """

    if type(execution_capability) is not _ExecutionCapability:
        raise ArmContractError("a runner-issued execution capability is required")
    execution_capability._consume(
        arm=arm,
        fs_root=Path(fs_root),
        nss_root=Path(nss_root),
    )
    if arm not in ARM_NAMES:
        raise ArmContractError(f"unknown arm: {arm}")
    if not callable(phase):
        raise ArmContractError("phase must be a context-manager factory")

    with phase("C_generator_construct"):
        parents = verify_apparatus(fs_root=Path(fs_root), nss_root=Path(nss_root))
        fs = parents.fs

    with phase("C_case_generation"):
        datasets, xor_probe, xor_heldout = _make_datasets(fs)

    with phase("C_M0_search"):
        runtimes = _run_m0(fs, datasets)

    nss_records: list[dict[str, Any]] = []
    unrotated: list[str] = []
    with phase("C_translation"):
        if arm != "FS_ONLY":
            translated_batches = [
                translate_examples(runtime.probe)
                for runtime in runtimes
            ]
        else:
            translated_batches = []

    with phase("C_NSS_gate"):
        if arm != "FS_ONLY":
            for runtime, translated in zip(runtimes, translated_batches):
                policy = parents.nss_operator.BoundaryGatedGenericSynthesizer()
                policy.fit(translated)
                expanded = int(policy.expanded_signature_count)
                allocation = SKIP if expanded == 0 else INVOKE
                record = {
                    "allocation": allocation,
                    "source_record_count": len(runtime.probe),
                    "emitted_record_count": len(translated),
                    "current_language_expression_count": 78,
                    "true_collision_signature_count": int(
                        policy.true_collision_signature_count
                    ),
                    "detected_collision_signature_count": int(
                        policy.detected_collision_signature_count
                    ),
                    "expanded_signature_count": expanded,
                    "adequate_signature_count": int(policy.adequate_signature_count),
                    "nss_search_cost": int(policy.search_cost),
                    "nss_representation_cost": int(policy.representation_cost),
                    "generated_operators": {
                        key: value.name
                        for key, value in sorted(policy.generated_operators.items())
                    },
                }
                nss_records.append(record)
                unrotated.append(allocation)

    with phase("C_control"):
        if arm == "FS_ONLY":
            applied = [INVOKE] * len(runtimes)
        elif arm == "SHUFFLED_NSS_TO_FS":
            applied = [unrotated[-1], *unrotated[:-1]]
        else:
            applied = list(unrotated)
        if len(applied) != 4:
            raise ArmContractError("allocation vector must contain four decisions")
        if arm == "SHUFFLED_NSS_TO_FS" and sorted(applied) != sorted(unrotated):
            raise ArmContractError("shuffled allocation changed the decision multiset")
        for runtime, allocation in zip(runtimes, applied):
            runtime.allocation = allocation
        if arm != "FS_ONLY":
            for runtime, record in zip(runtimes, nss_records):
                runtime.nss_record = record

    with phase("C_M1_search"):
        if arm == "FS_ONLY":
            for runtime in runtimes:
                _search_m1(fs, runtime)
        elif arm in ("NSS_TO_FS", "SHUFFLED_NSS_TO_FS"):
            for runtime in runtimes:
                if runtime.allocation == INVOKE:
                    _search_m1(fs, runtime)
        elif arm == "NSS_ONLY":
            pass

    with phase("C_FS_value_authority"):
        if arm != "NSS_ONLY":
            for runtime in runtimes:
                if runtime.fanout_result is not None:
                    _apply_fs_authority(fs, runtime)

    with phase("C_heldout_reuse"):
        for runtime in runtimes[:3]:
            if runtime.heldout is None or runtime.selected_result is None:
                raise ArmContractError("primary held-out evaluation is unavailable")
            runtime.heldout_accuracy = float(
                fs.transfer_accuracy(runtime.selected_result, runtime.heldout)
            )
        reuse_learner = runtimes[3].learner
        xor_result = reuse_learner.search_current_generator(xor_probe)
        xor_accuracy = float(fs.transfer_accuracy(xor_result, xor_heldout))

    with phase("C_control"):
        condition_records = [_serialize_condition(fs, runtime) for runtime in runtimes]
        m0_program_node_sum = sum(
            program.size() for program in fs.READ_ONCE_PROGRAMS.values()
        )
        m1_program_node_sum = sum(
            program.size() for program in fs.FANOUT_PROGRAMS.values()
        )
        m0_search_program_examples = sum(
            len(runtime.probe) * 94 for runtime in runtimes
        )
        m1_search_program_examples = sum(
            len(runtime.probe) * 127
            for runtime in runtimes
            if runtime.fanout_result is not None
        )
        primary_heldout_program_examples = sum(
            len(runtime.heldout)
            for runtime in runtimes[:3]
            if runtime.heldout is not None
        )
        xor_library = (
            fs.FANOUT_PROGRAMS
            if reuse_learner.fanout_enabled
            else fs.READ_ONCE_PROGRAMS
        )
        xor_program_node_sum = (
            m1_program_node_sum
            if reuse_learner.fanout_enabled
            else m0_program_node_sum
        )
        xor_search_program_examples = len(xor_library) * len(xor_probe)
        xor_heldout_program_examples = len(xor_heldout)
        program_example_evaluations = (
            parents.verification_diagnostics["m0_program_evaluations"]
            + m0_search_program_examples
            + m1_search_program_examples
            + primary_heldout_program_examples
            + xor_search_program_examples
            + xor_heldout_program_examples
        )
        program_node_evaluations = (
            parents.verification_diagnostics["m0_program_node_evaluations"]
            + sum(len(runtime.probe) * m0_program_node_sum for runtime in runtimes)
            + sum(
                len(runtime.probe) * m1_program_node_sum
                for runtime in runtimes
                if runtime.fanout_result is not None
            )
            + sum(
                len(runtime.heldout) * runtime.selected_result.program.size()
                for runtime in runtimes[:3]
                if runtime.heldout is not None and runtime.selected_result is not None
            )
            + len(xor_probe) * xor_program_node_sum
            + len(xor_heldout) * xor_result.program.size()
        )
        generator_state = {
            runtime.spec.name: (
                "fanout_allowed" if runtime.learner.fanout_enabled else "read_once"
            )
            for runtime in runtimes
        }
        generator_state["NOVEL_XOR_REUSE"] = (
            "fanout_allowed" if reuse_learner.fanout_enabled else "read_once"
        )
        stages = [
            "SOURCE_VERIFY",
            "CASE_GENERATE",
            "M0_SEARCH",
            *( [] if arm == "FS_ONLY" else ["TRANSLATE", "NSS_SIGNATURE", "NSS_ALLOCATE"] ),
            *( [] if arm == "NSS_ONLY" else ["FS_M1_SEARCH", "FS_VALUE", "FS_MUTATION"] ),
            "HELDOUT_REUSE",
            "COST_CONTROL_COMPARE",
        ]
        result = {
            "schema_version": "cgp-001-arm-v1",
            "arm": arm,
            "parent_commits": {"nss": NSS_COMMIT, "fs": FS_COMMIT},
            "source_verification": {
                "nss_commit": NSS_COMMIT,
                "fs_commit": FS_COMMIT,
                "nss_file_hashes": dict(NSS_HASHES),
                "fs_file_hashes": dict(FS_HASHES),
                "current_language_expression_count": 78,
                "read_once_program_count": 94,
                "fanout_program_count": 127,
                "eight_pattern_signature_m0_equivalence": True,
            },
            "unrotated_allocation_vector": None if arm == "FS_ONLY" else unrotated,
            "applied_allocation_vector": applied,
            "conditions": condition_records,
            "later_family_reuse": {
                "probe_seed": 43,
                "heldout_seed": 47,
                "probe_count": len(xor_probe),
                "heldout_count": len(xor_heldout),
                "result": _serialize_search_result(fs, xor_result),
                "heldout_accuracy": xor_accuracy,
                "generator": (
                    "fanout_allowed" if reuse_learner.fanout_enabled else "read_once"
                ),
            },
            "operation_diagnostics": {
                "M0_candidates_scored": (
                    sum(94 for _ in runtimes)
                    + (0 if reuse_learner.fanout_enabled else len(xor_library))
                ),
                "M1_candidates_scored": sum(
                    127 for runtime in runtimes if runtime.fanout_result is not None
                ) + (len(xor_library) if reuse_learner.fanout_enabled else 0),
                "reuse_candidates_scored": len(xor_library),
                "program_example_evaluations": program_example_evaluations,
                "program_node_evaluations": program_node_evaluations,
                "source_records": 8 + sum(
                    record["source_record_count"] for record in nss_records
                ),
                "emitted_records": 8 + sum(
                    record["emitted_record_count"] for record in nss_records
                ),
                "apparatus_equivalence_source_records": 8,
                "primary_translation_source_records": sum(
                    record["source_record_count"] for record in nss_records
                ),
                "signature_calls": parents.verification_diagnostics["signature_calls"] + sum(
                    record["emitted_record_count"] for record in nss_records
                ),
                "apparatus_signature_equivalence_calls": (
                    parents.verification_diagnostics["signature_calls"]
                ),
                "apparatus_m0_pair_program_evaluations": (
                    parents.verification_diagnostics["m0_program_evaluations"]
                ),
                "apparatus_m0_pair_program_node_evaluations": (
                    parents.verification_diagnostics["m0_program_node_evaluations"]
                ),
                "hash_group_insertions": sum(
                    record["emitted_record_count"] for record in nss_records
                ),
                "label_set_insertions": sum(
                    record["emitted_record_count"] for record in nss_records
                ),
                "collision_decisions": sum(
                    record["true_collision_signature_count"]
                    + record["adequate_signature_count"]
                    for record in nss_records
                ),
                "expanded_signatures": sum(
                    record["expanded_signature_count"] for record in nss_records
                ),
                "NSS_generated_predicate_evaluations": sum(
                    record["nss_search_cost"] for record in nss_records
                ),
                "heldout_reuse_examples": (
                    primary_heldout_program_examples
                    + len(xor_probe)
                    + len(xor_heldout)
                ),
                "FS_value_adoption_decisions": sum(
                    runtime.estimated_repair_value is not None for runtime in runtimes
                ),
                "selected_node_count": {
                    runtime.spec.name: runtime.selected_result.program.size()
                    for runtime in runtimes
                    if runtime.selected_result is not None
                }
                | {"NOVEL_XOR_REUSE": xor_result.program.size()},
                "generator_state": generator_state,
                "stages": stages,
            },
            "generator_state": generator_state,
            "stages": stages,
        }
    return result
