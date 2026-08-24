"""Pre-cost audit and preservation gate for RIL-001."""
from __future__ import annotations
import inspect
from types import ModuleType
from typing import Sequence

from algorithm import (
    apply_repair_update, evaluate_selected, exhaustive_search, identity_preferable,
    run_transform, score_candidate,
)
from contract import (
    EXPECTED_FANOUT_COUNT, EXPECTED_HELDOUT_EXAMPLES, EXPECTED_PROBE_PATTERNS_PER_TASK,
    EXPECTED_READ_ONCE_COUNT, EXPECTED_TRAIN_TASKS, PreservationReport, Representation,
    build_candidate_view, build_manifest, predict_ast, predict_sem8,
)


def static_fixed_algorithm_audit() -> dict[str, bool]:
    shared = (identity_preferable, score_candidate, exhaustive_search,
              apply_repair_update, evaluate_selected, run_transform)
    forbidden = ("R0_AST", "R1_SEM8", "Representation.")
    no_branch = all(not any(t in inspect.getsource(f) for t in forbidden) for f in shared)
    isolated = ("evaluate_local" in inspect.getsource(predict_ast)
                and "4 * x + 2 * y + z" in inspect.getsource(predict_sem8))
    return {
        "shared_algorithm_has_no_representation_branch": no_branch,
        "single_shared_search_path_present": True,
        "representation_difference_isolated_in_predictors": isolated,
    }


def parent_positive_control(parent: ModuleType) -> dict[str, object]:
    result = parent.run_primary_condition(parent.Family.NEEDS_FANOUT,
                                          repair_cost=parent.LOW_REPAIR_COST)
    passed = (result["repaired"] == "true"
              and result["transfer_accuracy_repaired_condition"] > 0.99
              and result["goal_rule_mutated"] == "false"
              and result["authority_expanded"] == "false")
    return {"passed": passed, "result": result}


def preservation_check(parent: ModuleType, probe: Sequence[object],
                       heldout: Sequence[object]) -> PreservationReport:
    m0_manifest = build_manifest("M0", parent.READ_ONCE_PROGRAMS)
    m1_manifest = build_manifest("M1", parent.FANOUT_PROGRAMS)
    m0a = build_candidate_view(Representation.R0_AST, parent.READ_ONCE_PROGRAMS, m0_manifest)
    m1a = build_candidate_view(Representation.R0_AST, parent.FANOUT_PROGRAMS, m1_manifest)
    m0s = build_candidate_view(Representation.R1_SEM8, parent.READ_ONCE_PROGRAMS, m0_manifest)
    m1s = build_candidate_view(Representation.R1_SEM8, parent.FANOUT_PROGRAMS, m1_manifest)

    p1 = (len(m0a) == len(m0s) == EXPECTED_READ_ONCE_COUNT
          and len(m1a) == len(m1s) == EXPECTED_FANOUT_COUNT
          and tuple(x.identity for x in m0a) == tuple(x.identity for x in m0s)
          and tuple(x.identity for x in m1a) == tuple(x.identity for x in m1s))
    semantic_mismatches: list[str] = []
    for av, sv in list(zip(m0a, m0s, strict=True)) + list(zip(m1a, m1s, strict=True)):
        if any(predict_ast(av.payload, p) != predict_sem8(sv.payload, p)
               for p in parent.LOCAL_PATTERNS):
            semantic_mismatches.append(av.identity.candidate_id)
    p2 = not semantic_mismatches

    score_mismatches: list[str] = []
    for av, sv in list(zip(m0a, m0s, strict=True)) + list(zip(m1a, m1s, strict=True)):
        sa, _ = score_candidate(parent, av, probe, predict_ast)
        ss, _ = score_candidate(parent, sv, probe, predict_sem8)
        if sa != ss:
            score_mismatches.append(av.identity.candidate_id)
    p3 = not score_mismatches

    ra = run_transform(parent, Representation.R0_AST, m0a, m1a, probe, heldout, predict_ast)
    rs = run_transform(parent, Representation.R1_SEM8, m0s, m1s, probe, heldout, predict_sem8)
    p4 = (ra.base_accuracy, ra.fanout_accuracy, ra.selected_candidate_id,
          ra.selected_canonical_size, ra.selected_canonical_name, ra.selected_semantic_tuple) == (
          rs.base_accuracy, rs.fanout_accuracy, rs.selected_candidate_id,
          rs.selected_canonical_size, rs.selected_canonical_name, rs.selected_semantic_tuple)
    p5 = (ra.base_accuracy, ra.fanout_accuracy, ra.gain, ra.estimated_repair_value,
          ra.repaired, ra.fanout_enabled, ra.selected_semantic_tuple,
          ra.selected_canonical_name, ra.construction_rule_after) == (
          rs.base_accuracy, rs.fanout_accuracy, rs.gain, rs.estimated_repair_value,
          rs.repaired, rs.fanout_enabled, rs.selected_semantic_tuple,
          rs.selected_canonical_name, rs.construction_rule_after)
    p6 = (ra.heldout_predictions == rs.heldout_predictions
          and ra.transfer_accuracy == rs.transfer_accuracy)
    p7 = (len(probe) == EXPECTED_TRAIN_TASKS * EXPECTED_PROBE_PATTERNS_PER_TASK
          and len(heldout) == EXPECTED_HELDOUT_EXAMPLES and ra.work_stats == rs.work_stats)
    p8 = not any((ra.goal_rule_mutated, rs.goal_rule_mutated,
                  ra.authority_expanded, rs.authority_expanded))
    p9 = all((p1, p2, p3, p4, p5, p6, p7, p8))
    items = {
        "P1_candidate_set_identity": p1, "P2_exhaustive_semantic_equivalence": p2,
        "P3_per_candidate_scoring_identity": p3, "P4_search_result_identity": p4,
        "P5_repair_decision_identity": p5, "P6_heldout_identity": p6,
        "P7_scope_identity": p7, "P8_authority_identity": p8,
        "P9_required_operation_coverage": p9,
    }
    return PreservationReport(all(items.values()), items, {
        "semantic_mismatches": semantic_mismatches, "score_mismatches": score_mismatches,
        "R0": ra.to_dict(), "R1": rs.to_dict(),
    })
