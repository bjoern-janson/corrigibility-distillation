"""Frozen pre-reveal generator and provenance contract for RIL-003."""
from __future__ import annotations

import hashlib
import importlib
import json
import os
import platform
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from random import Random
from types import SimpleNamespace
from typing import Sequence

RIL003_PREREGISTRATION_COMMIT = "c5acae018aec09afc9ceece152bb9cdc7a39e112"
RIL003_GENERATOR_CONTRACT_GIT_BLOB = "f7113a3e07a8c7c6261107ae8eb8bc80f11d20bf"
RIL002_TERMINAL_COMMIT = "e0d43408ed2a07c3cc6bca181f433ab819c0577f"
RIL001_IMPLEMENTATION_COMMIT = "a0f8f795a805e8f579fd608fbcaa83dcfa6ef60f"
RIL001_RESULT_COMMIT = "a8dfb2aa7e72b5f28c497bbe071408c9be0113a3"

EXPECTED_INHERITED_BLOBS = {
    "contract.py": "2f4b18721cddaabfb0ea118adada2ea0161659de",
    "algorithm.py": "e64d5b08e69330cdc08dd0cc8ea85f238ae04593",
    "instrument.py": "ac8bf7b728bc3ad25847e597770fbc97dbc0c613",
    "audit.py": "eddf91309839c4bc38cec3f6c1b48528a4ab5a02",
}

TARGET_TIME_UTC = datetime(2026, 8, 26, 12, 0, 0, tzinfo=timezone.utc)
TARGET_TIME_TEXT = "2026-08-26T12:00:00.000Z"
EXPECTED_ALL_ESSENTIAL_COUNT = 218
EXPECTED_ELIGIBLE_COUNT = 193
SAMPLE_SIZE = 24
RANK_DOMAIN = b"RIL-003|TARGET-RANK|"

PRIOR_EXCLUDED_VALUES = (
    0x17,
    0x1B, 0x1D, 0x27, 0x2E, 0x35, 0x3A,
    0x47, 0x4E, 0x53, 0x5C, 0x72, 0x74,
    0x8B, 0x8D, 0xA3, 0xAC, 0xB1, 0xB8,
    0xC5, 0xCA, 0xD1, 0xD8, 0xE2, 0xE4,
)


class RIL3ContractError(RuntimeError):
    pass


class RevealNotAvailable(RIL3ContractError):
    pass


@dataclass(frozen=True)
class TargetSpec:
    member_id: str
    truth_table: tuple[int, ...]
    hex_id: str
    rank_digest: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


def git_blob_sha1_bytes(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def canonical_json_bytes(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")


def verify_generator_contract(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    observed = git_blob_sha1_bytes(data)
    if observed != RIL003_GENERATOR_CONTRACT_GIT_BLOB:
        raise RIL3ContractError(
            f"generator contract blob mismatch: expected {RIL003_GENERATOR_CONTRACT_GIT_BLOB}, got {observed}"
        )
    raw = json.loads(data.decode("utf-8"))
    q = raw.get("Q_test", {})
    if q.get("sample_size") != SAMPLE_SIZE:
        raise RIL3ContractError("generator sample-size mismatch")
    entropy = q.get("entropy", {})
    if entropy.get("target_time_utc") != TARGET_TIME_TEXT:
        raise RIL3ContractError("generator target-time mismatch")
    if entropy.get("seed_field") != "outputValue":
        raise RIL3ContractError("generator entropy field mismatch")
    if q.get("eligibility", {}).get("expected_eligible_count_after_exclusion") != EXPECTED_ELIGIBLE_COUNT:
        raise RIL3ContractError("generator eligible-count contract mismatch")
    return {"passed": True, "git_blob": observed, "sample_size": SAMPLE_SIZE,
            "target_time_utc": TARGET_TIME_TEXT}


def verify_inherited_blobs(ril001_dir: Path) -> dict[str, object]:
    observed: dict[str, str] = {}
    for name, expected in EXPECTED_INHERITED_BLOBS.items():
        path = ril001_dir / name
        if not path.is_file():
            raise RIL3ContractError(f"missing inherited RIL-001 file: {path}")
        observed[name] = git_blob_sha1_bytes(path.read_bytes())
        if observed[name] != expected:
            raise RIL3ContractError(
                f"inherited blob mismatch for {name}: expected {expected}, got {observed[name]}"
            )
    return {"passed": True, "expected": dict(EXPECTED_INHERITED_BLOBS), "observed": observed}


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
            raise RIL3ContractError(f"stale/wrong inherited module loaded for {name}")
        setattr(modules, name, module)
    return modules


def truth_table_from_value(value: int) -> tuple[int, ...]:
    if not 0 <= value <= 0xFF:
        raise RIL3ContractError("truth-table value out of range")
    return tuple((value >> shift) & 1 for shift in range(7, -1, -1))


def value_from_truth_table(table: Sequence[int]) -> int:
    if len(table) != 8 or any(int(x) not in (0, 1) for x in table):
        raise RIL3ContractError("invalid truth table")
    value = 0
    for bit in table:
        value = (value << 1) | int(bit)
    return value


def target_id(value: int) -> str:
    return f"TT_{value:02X}"


def essential_variables(table: Sequence[int]) -> frozenset[int]:
    if len(table) != 8:
        raise RIL3ContractError("essentiality requires 8-entry table")
    essential: set[int] = set()
    for var in range(3):
        mask = 1 << (2 - var)
        for idx in range(8):
            if int(table[idx]) != int(table[idx ^ mask]):
                essential.add(var)
                break
    return frozenset(essential)


def eligible_values() -> tuple[int, ...]:
    all_essential = [v for v in range(256)
                     if essential_variables(truth_table_from_value(v)) == frozenset((0, 1, 2))]
    if len(all_essential) != EXPECTED_ALL_ESSENTIAL_COUNT:
        raise RIL3ContractError(
            f"all-essential universe mismatch: expected {EXPECTED_ALL_ESSENTIAL_COUNT}, got {len(all_essential)}"
        )
    excluded = set(PRIOR_EXCLUDED_VALUES)
    eligible = tuple(v for v in all_essential if v not in excluded)
    if len(eligible) != EXPECTED_ELIGIBLE_COUNT:
        raise RIL3ContractError(
            f"eligible universe mismatch: expected {EXPECTED_ELIGIBLE_COUNT}, got {len(eligible)}"
        )
    return eligible


def eligible_universe_summary() -> dict[str, object]:
    # Deliberately returns counts only; pre-reveal audit does not publish the eligible ID list.
    eligible_values()
    return {
        "all_three_essential_count": EXPECTED_ALL_ESSENTIAL_COUNT,
        "prior_exact_exclusion_count": len(PRIOR_EXCLUDED_VALUES),
        "eligible_count": EXPECTED_ELIGIBLE_COUNT,
        "sample_size": SAMPLE_SIZE,
    }


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


def build_target_dataset(parent: object, target: TargetSpec, inherited: SimpleNamespace) -> tuple[list[object], list[object]]:
    c = inherited.contract
    train_tasks, test_tasks = parent.make_task_split(seed=c.TASK_SPLIT_SEED)
    probe = make_probe_examples(parent, train_tasks, target.truth_table, seed=c.PROBE_SEED)
    heldout = make_heldout_examples(parent, test_tasks, target.truth_table, seed=c.HELDOUT_SEED,
                                    count=c.EXPECTED_HELDOUT_EXAMPLES)
    expected_probe = c.EXPECTED_TRAIN_TASKS * c.EXPECTED_PROBE_PATTERNS_PER_TASK
    if len(probe) != expected_probe or len(heldout) != c.EXPECTED_HELDOUT_EXAMPLES:
        raise RIL3ContractError("target dataset size mismatch")
    return probe, heldout


def prediction_digest(predictions: Sequence[int]) -> str:
    return hashlib.sha256(bytes(int(x) for x in predictions)).hexdigest()


def parse_iso_utc(text: str) -> datetime:
    normalized = text[:-1] + "+00:00" if text.endswith("Z") else text
    value = datetime.fromisoformat(normalized)
    if value.tzinfo is None:
        raise RIL3ContractError("Beacon timestamp is not timezone-aware")
    return value.astimezone(timezone.utc)


def _pulse_object(package: object) -> dict[str, object]:
    if not isinstance(package, dict):
        raise RIL3ContractError("Beacon package must be a JSON object")
    pulse = package.get("pulse", package)
    if not isinstance(pulse, dict):
        raise RIL3ContractError("Beacon pulse object missing")
    return pulse


def _first_present(pulse: dict[str, object], names: tuple[str, ...]) -> object:
    for name in names:
        if name in pulse:
            return pulse[name]
    raise RIL3ContractError(f"Beacon field missing: one of {names}")


def validate_beacon_package_bytes(package_bytes: bytes) -> dict[str, object]:
    package = json.loads(package_bytes.decode("utf-8"))
    pulse = _pulse_object(package)
    timestamp_text = str(_first_present(pulse, ("timeStamp", "time")))
    timestamp = parse_iso_utc(timestamp_text)
    if timestamp < TARGET_TIME_UTC:
        raise RevealNotAvailable("Beacon pulse precedes frozen target time")
    output_value = str(_first_present(pulse, ("outputValue",)))
    try:
        output_bytes = bytes.fromhex(output_value)
    except ValueError as exc:
        raise RIL3ContractError("Beacon outputValue is not hexadecimal") from exc
    if len(output_bytes) != 64:
        raise RIL3ContractError(f"Beacon outputValue must decode to 64 bytes, got {len(output_bytes)}")
    chain_id = _first_present(pulse, ("chainIndex", "chainId"))
    pulse_id = _first_present(pulse, ("pulseIndex", "pulseId"))
    version = str(pulse.get("version", "2.0"))
    if version != "2.0":
        raise RIL3ContractError(f"unexpected Beacon version: {version}")
    uri = pulse.get("uri")
    if uri is not None and not str(uri).startswith("https://beacon.nist.gov/beacon/2.0/"):
        raise RIL3ContractError("Beacon URI is not NIST Beacon 2.0")
    return {
        "timestamp": timestamp.isoformat().replace("+00:00", "Z"),
        "chain_id": chain_id,
        "pulse_id": pulse_id,
        "output_value": output_value.upper(),
        "output_bytes": output_bytes,
        "package_sha256": hashlib.sha256(package_bytes).hexdigest(),
        "version": version,
        "uri": uri,
    }


def rank_digest(output_bytes: bytes, value: int) -> bytes:
    if len(output_bytes) != 64:
        raise RIL3ContractError("ranking requires exactly 64 Beacon bytes")
    return hashlib.sha256(RANK_DOMAIN + output_bytes + b"|" + target_id(value).encode("ascii")).digest()


def select_targets(output_bytes: bytes) -> tuple[TargetSpec, ...]:
    ranked = sorted(((rank_digest(output_bytes, v), v) for v in eligible_values()),
                    key=lambda row: (row[0], row[1]))
    chosen = ranked[:SAMPLE_SIZE]
    return tuple(TargetSpec(target_id(v), truth_table_from_value(v), f"0x{v:02X}", digest.hex())
                 for digest, v in chosen)


def family_sha256(targets: Sequence[TargetSpec]) -> str:
    rows = [{"member_id": t.member_id,
             "truth_table": "".join(str(x) for x in t.truth_table),
             "hex": t.hex_id,
             "rank_digest": t.rank_digest}
            for t in targets]
    return hashlib.sha256(canonical_json_bytes(rows)).hexdigest()


def materialize_target_manifest(package_bytes: bytes, *, now_utc: datetime | None = None) -> dict[str, object]:
    now = (now_utc or datetime.now(timezone.utc)).astimezone(timezone.utc)
    if now < TARGET_TIME_UTC:
        raise RevealNotAvailable(
            f"RIL-003 target reveal forbidden before {TARGET_TIME_TEXT}; current={now.isoformat()}"
        )
    pulse = validate_beacon_package_bytes(package_bytes)
    targets = select_targets(pulse["output_bytes"])  # type: ignore[arg-type]
    rows = [{"member_id": t.member_id,
             "truth_table": "".join(str(x) for x in t.truth_table),
             "hex": t.hex_id,
             "rank_digest": t.rank_digest}
            for t in targets]
    return {
        "assay": "RIL-003",
        "status": "TARGETS REVEALED; MANIFEST MUST BE COMMITTED BEFORE EXECUTION",
        "preregistration_commit": RIL003_PREREGISTRATION_COMMIT,
        "beacon_target_time": TARGET_TIME_TEXT,
        "beacon_actual_pulse_timestamp": pulse["timestamp"],
        "beacon_chain_id": pulse["chain_id"],
        "beacon_pulse_id": pulse["pulse_id"],
        "beacon_outputValue": pulse["output_value"],
        "beacon_package_sha256": pulse["package_sha256"],
        "eligible_universe_count": EXPECTED_ELIGIBLE_COUNT,
        "targets": rows,
        "targets_sha256_canonical_json": family_sha256(targets),
        "statement": "No target-specific preservation/cost result is generated by target materialization.",
    }


def load_target_manifest(path: Path) -> tuple[TargetSpec, ...]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if raw.get("assay") != "RIL-003" or raw.get("preregistration_commit") != RIL003_PREREGISTRATION_COMMIT:
        raise RIL3ContractError("target manifest identity mismatch")
    if raw.get("eligible_universe_count") != EXPECTED_ELIGIBLE_COUNT:
        raise RIL3ContractError("target manifest eligible count mismatch")
    output_value = str(raw.get("beacon_outputValue", ""))
    try:
        output_bytes = bytes.fromhex(output_value)
    except ValueError as exc:
        raise RIL3ContractError("target manifest Beacon outputValue is not hexadecimal") from exc
    if len(output_bytes) != 64:
        raise RIL3ContractError("target manifest Beacon outputValue must decode to 64 bytes")
    pulse_time = parse_iso_utc(str(raw.get("beacon_actual_pulse_timestamp", "")))
    if pulse_time < TARGET_TIME_UTC:
        raise RIL3ContractError("target manifest pulse precedes frozen target time")

    rows = raw.get("targets")
    if not isinstance(rows, list) or len(rows) != SAMPLE_SIZE:
        raise RIL3ContractError("target manifest member count mismatch")
    targets: list[TargetSpec] = []
    seen: set[str] = set()
    for row in rows:
        member_id = str(row["member_id"])
        if member_id in seen:
            raise RIL3ContractError(f"duplicate target: {member_id}")
        seen.add(member_id)
        table = tuple(int(ch) for ch in str(row["truth_table"]))
        value = value_from_truth_table(table)
        if member_id != target_id(value) or str(row["hex"]) != f"0x{value:02X}":
            raise RIL3ContractError(f"target identity mismatch: {member_id}")
        if value in PRIOR_EXCLUDED_VALUES or essential_variables(table) != frozenset((0, 1, 2)):
            raise RIL3ContractError(f"target violates Q_test: {member_id}")
        targets.append(TargetSpec(member_id, table, f"0x{value:02X}", str(row["rank_digest"])))
    digest = family_sha256(targets)
    if raw.get("targets_sha256_canonical_json") != digest:
        raise RIL3ContractError("target manifest canonical digest mismatch")
    expected = select_targets(output_bytes)
    observed_identity = tuple((t.member_id, t.truth_table, t.rank_digest) for t in targets)
    expected_identity = tuple((t.member_id, t.truth_table, t.rank_digest) for t in expected)
    if observed_identity != expected_identity:
        raise RIL3ContractError("target manifest does not reproduce Q_test ranking from Beacon outputValue")
    return tuple(targets)


def target_by_id(targets: Sequence[TargetSpec], member_id: str) -> TargetSpec:
    for target in targets:
        if target.member_id == member_id:
            return target
    raise RIL3ContractError(f"unknown RIL-003 target: {member_id}")


def execution_manifest(inherited: SimpleNamespace) -> dict[str, object]:
    try:
        affinity = sorted(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        affinity = None
    return {
        "assay": "RIL-003",
        "preregistration_commit": RIL003_PREREGISTRATION_COMMIT,
        "ril001_implementation_commit": RIL001_IMPLEMENTATION_COMMIT,
        "ril001_result_commit": RIL001_RESULT_COMMIT,
        "ril002_terminal_commit": RIL002_TERMINAL_COMMIT,
        "generator_contract_blob": RIL003_GENERATOR_CONTRACT_GIT_BLOB,
        "inherited_blobs": dict(EXPECTED_INHERITED_BLOBS),
        "target_time_utc": TARGET_TIME_TEXT,
        "sample_size": SAMPLE_SIZE,
        "expected_eligible_count": EXPECTED_ELIGIBLE_COUNT,
        "representations": {"R0": "R0_AST", "R1": "R1_SEM8"},
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "affinity": affinity,
    }
