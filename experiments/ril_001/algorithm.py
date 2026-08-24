"""Single shared corrective algorithm for both RIL-001 representations."""
from __future__ import annotations
from types import ModuleType
from typing import Sequence

from contract import (
    ArmResult, CandidateView, EXPECTED_FUTURE_HORIZON, EXPECTED_LOW_REPAIR_COST,
    Predictor, Representation, RILContractError, SearchOutcome, TransformState,
    WorkStats, build_candidate_view, build_manifest, predictor_for,
)


def identity_preferable(left: CandidateView, right: CandidateView) -> bool:
    return (left.identity.canonical_size, left.identity.canonical_name) < (
        right.identity.canonical_size, right.identity.canonical_name)


def score_candidate(parent: ModuleType, candidate: CandidateView,
                    examples: Sequence[object], predictor: Predictor) -> tuple[float, int]:
    correct = 0
    comparisons = 0
    for example in examples:
        values = parent.local_values(example)
        predicted = predictor(candidate.payload, values)
        if predicted == example.hidden:
            correct += 1
        comparisons += 1
    return correct / len(examples), comparisons


def exhaustive_search(parent: ModuleType, candidates: Sequence[CandidateView],
                      examples: Sequence[object], predictor: Predictor) -> tuple[SearchOutcome, int, int]:
    best: SearchOutcome | None = None
    visits = 0
    comparisons = 0
    for candidate in candidates:
        accuracy, n = score_candidate(parent, candidate, examples, predictor)
        visits += 1
        comparisons += n
        outcome = SearchOutcome(candidate, accuracy)
        if best is None or outcome.accuracy > best.accuracy:
            best = outcome
        elif outcome.accuracy == best.accuracy and identity_preferable(outcome.candidate, best.candidate):
            best = outcome
    if best is None:
        raise RILContractError("empty candidate language")
    return best, visits, comparisons


def apply_repair_update(base: SearchOutcome, fanout: SearchOutcome, *,
                        repair_cost: float, future_horizon: int) -> TransformState:
    gain = max(0.0, fanout.accuracy - base.accuracy)
    value = future_horizon * gain
    enabled = value > repair_cost
    return TransformState(enabled, base, fanout, fanout if enabled else base, gain, value)


def evaluate_selected(parent: ModuleType, selected: CandidateView,
                      heldout: Sequence[object], predictor: Predictor) -> tuple[tuple[int, ...], float]:
    predictions: list[int] = []
    correct = 0
    for example in heldout:
        predicted = predictor(selected.payload, parent.local_values(example))
        predictions.append(predicted)
        if predicted == example.hidden:
            correct += 1
    return tuple(predictions), correct / len(heldout)


def semantic_key_for_candidate(programs: dict[tuple[int, ...], object],
                               candidate: CandidateView) -> tuple[int, ...]:
    keys = tuple(programs.keys())
    i = candidate.identity.insertion_index
    if not 0 <= i < len(keys):
        raise RILContractError("candidate insertion index out of range")
    return keys[i]


def run_transform(parent: ModuleType, representation: Representation,
                  m0: Sequence[CandidateView], m1: Sequence[CandidateView],
                  probe: Sequence[object], heldout: Sequence[object],
                  predictor: Predictor) -> ArmResult:
    base, m0_visits, m0_comp = exhaustive_search(parent, m0, probe, predictor)
    fanout, m1_visits, m1_comp = exhaustive_search(parent, m1, probe, predictor)
    state = apply_repair_update(base, fanout, repair_cost=EXPECTED_LOW_REPAIR_COST,
                                future_horizon=EXPECTED_FUTURE_HORIZON)
    predictions, transfer = evaluate_selected(parent, state.selected.candidate, heldout, predictor)
    selected_programs = parent.FANOUT_PROGRAMS if state.fanout_enabled else parent.READ_ONCE_PROGRAMS
    semantic = semantic_key_for_candidate(selected_programs, state.selected.candidate)
    return ArmResult(
        representation.value, state.base.accuracy, state.fanout.accuracy, state.gain,
        state.estimated_repair_value, state.fanout_enabled, state.fanout_enabled,
        state.selected.candidate.identity.candidate_id,
        state.selected.candidate.identity.canonical_size,
        state.selected.candidate.identity.canonical_name, semantic, transfer, predictions,
        "fanout_allowed" if state.fanout_enabled else "read_once", False, False,
        WorkStats(m0_visits, m1_visits, m0_comp + m1_comp, len(predictions)),
    )


def build_and_run_arm(parent: ModuleType, representation: Representation,
                      probe: Sequence[object], heldout: Sequence[object]) -> ArmResult:
    m0_manifest = build_manifest("M0", parent.READ_ONCE_PROGRAMS)
    m1_manifest = build_manifest("M1", parent.FANOUT_PROGRAMS)
    m0 = build_candidate_view(representation, parent.READ_ONCE_PROGRAMS, m0_manifest)
    m1 = build_candidate_view(representation, parent.FANOUT_PROGRAMS, m1_manifest)
    return run_transform(parent, representation, m0, m1, probe, heldout, predictor_for(representation))
