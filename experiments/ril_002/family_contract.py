"""Frozen RIL-002 family, inheritance, and dataset contract."""
from __future__ import annotations

import hashlib
import importlib
import json
import os
import platform
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from random import Random
from types import SimpleNamespace
from typing import Sequence

RIL002_PREREGISTRATION_COMMIT = "d35d998eea7e9b06ae0516dbcb9019955052ef6f"
RIL001_RESULT_COMMIT = "a8dfb2aa7e72b5f28c497bbe071408c9be0113a3"
RIL001_IMPLEMENTATION_COMMIT = "a0f8f795a805e8f579fd608fbcaa83dcfa6ef60f"
FAMILY_MEMBERS_SHA256 = "d51b9b51e37f82a316dfcbd1461b766b52f34941283d1af3d1189c2546b472b1"
EXPECTED_MEMBER_COUNT = 24
EXCLUDED_RIL001_TRUTH_TABLE = (0, 0, 0, 1, 0, 1, 1, 1)
EXPECTED_INHERITED_BLOBS = {
    "contract.py": "2f4b18721cddaabfb0ea118adada2ea0161659de",
    "algorithm.py": "e64d5b08e69330cdc08dd0cc8ea85f238ae04593",
    "instrument.py": "ac8bf7b728bc3ad25847e597770fbc97dbc0c613",
    "audit.py": "eddf91309839c4bc38cec3f6c1b48528a4ab5a02",
}


class RIL2ContractError(RuntimeError):
    pass


@dataclass(frozen=True)
class MemberSpec:
    member_id: str
    truth_table: tuple[int, ...]
    hex_id: str
    canonical_m1_program: str
    canonical_m1_size: int
    m0_exact_ceiling: float
    m1_exact_ceiling: float

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def git_blob_sha1_bytes(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def verify_inherited_blobs(ril001_dir: Path) -> dict[str, object]:
    ril001_dir = ril001_dir.resolve()
    observed: dict[str, str] = {}
    for name, expected in EXPECTED_INHERITED_BLOBS.items():
        path = ril001_dir / name
        if not path.is_file():
            raise RIL2ContractError(f"missing inherited RIL-001 file: {path}")
        observed[name] = git_blob_sha1_bytes(path.read_bytes())
        if observed[name] != expected:
            raise RIL2ContractError(
                f"inherited blob mismatch for {name}: expected {expected}, got {observed[name]}"
            )
    return {
        "passed": True,
        "ril001_implementation_commit": RIL001_IMPLEMENTATION_COMMIT,
        "expected": dict(EXPECTED_INHERITED_BLOBS),
        "observed": observed,
    }


def load_inherited(ril001_dir: Path) -> SimpleNamespace:
    verify_inherited_blobs(ril001_dir)
    p = str(ril001_dir.resolve())
    if p not in sys.path:
        sys.path.insert(0, p)
    modules = SimpleNamespace()
    for name in ("contract", "algorithm", "instrument", "audit"):
        module = importlib.import_module(name)
        expected_path = (ril001_dir / f"{name}.py").resolve()
        if Path(module.__file__).resolve() != expected_path:
            raise RIL2ContractError(f"stale/wrong inherited module loaded for {name}")
        setattr(modules, name, module)
    return modules


def _canonical_members_bytes(members: object) -> bytes:
    return json.dumps(members, sort_keys=True, separators=(",", ":")).encode("utf-8")


def load_family(path: Path) -> tuple[MemberSpec, ...]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    members_raw = raw.get("members")
    if not isinstance(members_raw, list):
        raise RIL2ContractError("family members missing/not list")
    digest = hashlib.sha256(_canonical_members_bytes(members_raw)).hexdigest()
    if digest != FAMILY_MEMBERS_SHA256 or raw.get("members_sha256_canonical_json") != digest:
        raise RIL2ContractError("family members hash mismatch")
    if len(members_raw) != EXPECTED_MEMBER_COUNT:
        raise RIL2ContractError("family member count mismatch")
    members: list[MemberSpec] = []
    seen: set[str] = set()
    for row in members_raw:
        member_id = row["member_id"]
        if member_id in seen:
            raise RIL2ContractError(f"duplicate family member: {member_id}")
        seen.add(member_id)
        table = tuple(int(ch) for ch in row["truth_table"])
        if len(table) != 8 or any(x not in (0, 1) for x in table):
            raise RIL2ContractError(f"invalid truth table for {member_id}")
        expected_hex = f"0x{int(row['truth_table'], 2):02X}"
        if row["hex"] != expected_hex or member_id != f"TT_{expected_hex[2:]}":
            raise RIL2ContractError(f"member id/hex mismatch: {member_id}")
        members.append(MemberSpec(
            member_id, table, row["hex"], row["canonical_m1_program"],
            int(row["canonical_m1_size"]), float(row["m0_exact_ceiling"]),
            float(row["m1_exact_ceiling"]),
        ))
    if tuple(m.hex_id for m in members) != tuple(sorted((m.hex_id for m in members), key=lambda x: int(x, 16))):
        raise RIL2ContractError("family order is not ascending truth-table value")
    return tuple(members)


def member_by_id(members: Sequence[MemberSpec], member_id: str) -> MemberSpec:
    for member in members:
        if member.member_id == member_id:
            return member
    raise RIL2ContractError(f"unknown member id: {member_id}")


def essential_variables(table: Sequence[int]) -> frozenset[int]:
    essential: set[int] = set()
    for var in range(3):
        mask = 1 << (2 - var)
        for idx in range(8):
            other = idx ^ mask
            if table[idx] != table[other]:
                essential.add(var)
                break
    return frozenset(essential)


def target_value(table: Sequence[int], values: tuple[int, int, int]) -> int:
    x, y, z = values
    return int(table[4 * x + 2 * y + z])


def make_probe_examples(parent: object, tasks: Sequence[object], table: Sequence[int], *, seed: int) -> list[object]:
    rng = Random(seed)
    examples: list[object] = []
    raw_id = 0
    for task in tasks:
        patterns = list(parent.LOCAL_PATTERNS)
        rng.shuffle(patterns)
        for values in patterns[: parent.PROBE_PATTERNS_PER_TASK]:
            bits = [rng.randrange(2) for _ in range(parent.N_BITS)]
            parent.set_local_pattern(bits, task, values)
            examples.append(parent.Example(
                bits=tuple(bits), task=task, hidden=target_value(table, values), raw_id=raw_id,
            ))
            raw_id += 1
    return examples


def make_heldout_examples(parent: object, tasks: Sequence[object], table: Sequence[int], *, seed: int,
                          count: int, raw_offset: int = 1_000_000) -> list[object]:
    tasks = list(tasks)
    rng = Random(seed)
    examples: list[object] = []
    for index in range(count):
        task = rng.choice(tasks)
        values = rng.choice(parent.LOCAL_PATTERNS)
        bits = [rng.randrange(2) for _ in range(parent.N_BITS)]
        parent.set_local_pattern(bits, task, values)
        examples.append(parent.Example(
            bits=tuple(bits), task=task, hidden=target_value(table, values), raw_id=raw_offset + index,
        ))
    return examples


def build_member_dataset(parent: object, member: MemberSpec, inherited: SimpleNamespace) -> tuple[list[object], list[object]]:
    c = inherited.contract
    train_tasks, test_tasks = parent.make_task_split(seed=c.TASK_SPLIT_SEED)
    probe = make_probe_examples(parent, train_tasks, member.truth_table, seed=c.PROBE_SEED)
    heldout = make_heldout_examples(
        parent, test_tasks, member.truth_table, seed=c.HELDOUT_SEED,
        count=c.EXPECTED_HELDOUT_EXAMPLES,
    )
    expected_probe = c.EXPECTED_TRAIN_TASKS * c.EXPECTED_PROBE_PATTERNS_PER_TASK
    if len(probe) != expected_probe or len(heldout) != c.EXPECTED_HELDOUT_EXAMPLES:
        raise RIL2ContractError("member dataset size mismatch")
    return probe, heldout


def prediction_digest(predictions: Sequence[int]) -> str:
    return hashlib.sha256(bytes(int(x) for x in predictions)).hexdigest()


def execution_manifest(inherited: SimpleNamespace) -> dict[str, object]:
    try:
        affinity = sorted(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        affinity = None
    return {
        "assay": "RIL-002",
        "preregistration_commit": RIL002_PREREGISTRATION_COMMIT,
        "parent_ril001_result_commit": RIL001_RESULT_COMMIT,
        "inherited_ril001_implementation_commit": RIL001_IMPLEMENTATION_COMMIT,
        "family_members_sha256": FAMILY_MEMBERS_SHA256,
        "inherited_blobs": dict(EXPECTED_INHERITED_BLOBS),
        "parent_repository": inherited.contract.PARENT_REPOSITORY,
        "parent_commit": inherited.contract.PARENT_COMMIT,
        "parent_source_git_blob": inherited.contract.PARENT_SOURCE_GIT_BLOB,
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "affinity": affinity,
        "timing": "not a primary RIL-002 measure",
    }
