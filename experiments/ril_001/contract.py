"""Frozen source, representation, and data contract for RIL-001."""
from __future__ import annotations

import hashlib
import importlib.util
import sys
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from types import ModuleType
from typing import Callable, Sequence

PREREGISTRATION_COMMIT = "204fe919159145ac9c29f1becfb92b0c511af02b"
PARENT_REPOSITORY = "bjoern-janson/future-sufficiency"
PARENT_COMMIT = "2f4ca824e02b89df0c23d64de312c4f93a4c8a41"
PARENT_SOURCE_PATH = "experiments/meta_language_repair.py"
PARENT_SOURCE_GIT_BLOB = "f74d85f5f9d0c7842dc50e34ae2718699108fff6"
PARENT_METHOD_GIT_BLOB = "9ac2883c797e99af27fd092b262f5cb6ce8ece70"

EXPECTED_READ_ONCE_COUNT = 94
EXPECTED_FANOUT_COUNT = 127
EXPECTED_M0_CEILING = 0.875
EXPECTED_M1_CEILING = 1.0
EXPECTED_N_BITS = 18
EXPECTED_TRAIN_TASKS = 50
EXPECTED_TEST_TASKS = 25
EXPECTED_PROBE_PATTERNS_PER_TASK = 4
EXPECTED_HELDOUT_EXAMPLES = 3000
EXPECTED_FUTURE_HORIZON = 100
EXPECTED_LOW_REPAIR_COST = 5.0
EXPECTED_MAX_FANOUT_NODES = 9
TASK_SPLIT_SEED = 7
PROBE_SEED = 17
HELDOUT_SEED = 31

TIMING_REPETITIONS = 15
TIMING_WARMUP_POLICY = "none; every measured arm runs in a fresh process"
TIMING_ORDER = "alternating by repetition: even R0_AST->R1_SEM8; odd R1_SEM8->R0_AST"


class RILContractError(RuntimeError):
    pass


class Representation(str, Enum):
    R0_AST = "R0_AST"
    R1_SEM8 = "R1_SEM8"


@dataclass(frozen=True)
class CandidateIdentity:
    candidate_id: str
    canonical_size: int
    canonical_name: str
    insertion_index: int


@dataclass(frozen=True)
class CandidateView:
    identity: CandidateIdentity
    payload: object


@dataclass(frozen=True)
class SearchOutcome:
    candidate: CandidateView
    accuracy: float


@dataclass(frozen=True)
class TransformState:
    fanout_enabled: bool
    base: SearchOutcome
    fanout: SearchOutcome
    selected: SearchOutcome
    gain: float
    estimated_repair_value: float


@dataclass(frozen=True)
class WorkStats:
    m0_candidate_visits: int
    m1_candidate_visits: int
    probe_score_comparisons: int
    heldout_predictions: int


@dataclass(frozen=True)
class ArmResult:
    representation: str
    base_accuracy: float
    fanout_accuracy: float
    gain: float
    estimated_repair_value: float
    repaired: bool
    fanout_enabled: bool
    selected_candidate_id: str
    selected_canonical_size: int
    selected_canonical_name: str
    selected_semantic_tuple: tuple[int, ...]
    transfer_accuracy: float
    heldout_predictions: tuple[int, ...]
    construction_rule_after: str
    goal_rule_mutated: bool
    authority_expanded: bool
    work_stats: WorkStats

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class SourceAudit:
    source_git_blob: str
    read_once_count: int
    fanout_count: int
    m0_ceiling: float
    m1_ceiling: float
    constants_match: bool

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class PreservationReport:
    passed: bool
    items: dict[str, bool]
    details: dict[str, object]

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


Predictor = Callable[[object, tuple[int, int, int]], int]


def git_blob_sha1_bytes(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def import_parent(source_path: Path) -> ModuleType:
    source_path = source_path.resolve()
    if not source_path.is_file():
        raise RILContractError(f"missing frozen parent source: {source_path}")
    blob = git_blob_sha1_bytes(source_path.read_bytes())
    if blob != PARENT_SOURCE_GIT_BLOB:
        raise RILContractError(
            f"parent source blob mismatch: expected {PARENT_SOURCE_GIT_BLOB}, got {blob}"
        )
    spec = importlib.util.spec_from_file_location("ril001_frozen_fs007", source_path)
    if spec is None or spec.loader is None:
        raise RILContractError("cannot construct import spec for frozen parent")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def verify_parent(parent: ModuleType) -> SourceAudit:
    constants_match = all((
        parent.N_BITS == EXPECTED_N_BITS,
        parent.TRAIN_TASKS == EXPECTED_TRAIN_TASKS,
        parent.TEST_TASKS == EXPECTED_TEST_TASKS,
        parent.PROBE_PATTERNS_PER_TASK == EXPECTED_PROBE_PATTERNS_PER_TASK,
        parent.HELDOUT_EXAMPLES == EXPECTED_HELDOUT_EXAMPLES,
        parent.FUTURE_HORIZON == EXPECTED_FUTURE_HORIZON,
        parent.LOW_REPAIR_COST == EXPECTED_LOW_REPAIR_COST,
        parent.MAX_FANOUT_NODES == EXPECTED_MAX_FANOUT_NODES,
        tuple(parent.LOCAL_PATTERNS)
        == tuple((x, y, z) for x in (0, 1) for y in (0, 1) for z in (0, 1)),
    ))
    if not constants_match:
        raise RILContractError("frozen parent constants/order mismatch")
    if len(parent.READ_ONCE_PROGRAMS) != EXPECTED_READ_ONCE_COUNT:
        raise RILContractError("read-once candidate count mismatch")
    if len(parent.FANOUT_PROGRAMS) != EXPECTED_FANOUT_COUNT:
        raise RILContractError("fanout candidate count mismatch")
    m0 = parent.exact_ceiling(parent.READ_ONCE_PROGRAMS, parent.Family.NEEDS_FANOUT)
    m1 = parent.exact_ceiling(parent.FANOUT_PROGRAMS, parent.Family.NEEDS_FANOUT)
    if m0.accuracy != EXPECTED_M0_CEILING or m1.accuracy != EXPECTED_M1_CEILING:
        raise RILContractError("frozen majority ceiling mismatch")
    return SourceAudit(PARENT_SOURCE_GIT_BLOB, len(parent.READ_ONCE_PROGRAMS),
                       len(parent.FANOUT_PROGRAMS), m0.accuracy, m1.accuracy, True)


def build_dataset(parent: ModuleType) -> tuple[list[object], list[object]]:
    train_tasks, test_tasks = parent.make_task_split(seed=TASK_SPLIT_SEED)
    probe = parent.make_probe_examples(train_tasks, parent.Family.NEEDS_FANOUT, seed=PROBE_SEED)
    heldout = parent.make_heldout_examples(test_tasks, parent.Family.NEEDS_FANOUT, seed=HELDOUT_SEED)
    if len(probe) != EXPECTED_TRAIN_TASKS * EXPECTED_PROBE_PATTERNS_PER_TASK:
        raise RILContractError("probe-set size mismatch")
    if len(heldout) != EXPECTED_HELDOUT_EXAMPLES:
        raise RILContractError("heldout-set size mismatch")
    return probe, heldout


def build_manifest(language: str, programs: dict[tuple[int, ...], object]) -> tuple[CandidateIdentity, ...]:
    if language not in ("M0", "M1"):
        raise RILContractError(f"unknown language: {language}")
    return tuple(
        CandidateIdentity(f"{language}:{i:03d}", program.size(), str(program), i)
        for i, program in enumerate(programs.values())
    )


def build_candidate_view(representation: Representation,
                         programs: dict[tuple[int, ...], object],
                         manifest: Sequence[CandidateIdentity]) -> tuple[CandidateView, ...]:
    if len(programs) != len(manifest):
        raise RILContractError("manifest/candidate length mismatch")
    if representation is Representation.R0_AST:
        payloads = tuple(programs.values())
    elif representation is Representation.R1_SEM8:
        payloads = tuple(programs.keys())
    else:
        raise RILContractError(f"unmapped representation: {representation}")
    return tuple(CandidateView(identity, payload)
                 for identity, payload in zip(manifest, payloads, strict=True))


def predict_ast(payload: object, values: tuple[int, int, int]) -> int:
    return payload.evaluate_local(values)  # type: ignore[attr-defined,no-any-return]


def predict_sem8(payload: object, values: tuple[int, int, int]) -> int:
    x, y, z = values
    return payload[4 * x + 2 * y + z]  # type: ignore[index,no-any-return]


def predictor_for(representation: Representation) -> Predictor:
    if representation is Representation.R0_AST:
        return predict_ast
    if representation is Representation.R1_SEM8:
        return predict_sem8
    raise RILContractError(f"unmapped representation: {representation}")


def parse_representation(text: str) -> Representation:
    try:
        return Representation(text)
    except ValueError as exc:
        raise RILContractError(f"unknown representation: {text}") from exc
