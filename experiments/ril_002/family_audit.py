"""Pre-execution audits and member preservation checks for RIL-002."""
from __future__ import annotations

import inspect
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Sequence

from family_contract import (
    EXCLUDED_RIL001_TRUTH_TABLE, MemberSpec, RIL2ContractError, build_member_dataset,
    essential_variables, load_family, prediction_digest, verify_inherited_blobs,
)


def _best_for_table(programs: dict[tuple[int, ...], object], table: tuple[int, ...]) -> tuple[float, object]:
    best_acc = -1.0
    best_program: object | None = None
    for semantic, program in programs.items():
        acc = sum(int(a == b) for a, b in zip(semantic, table, strict=True)) / 8
        if best_program is None or acc > best_acc:
            best_acc, best_program = acc, program
        elif acc == best_acc and (program.size(), str(program)) < (best_program.size(), str(best_program)):
            best_program = program
    if best_program is None:
        raise RIL2ContractError("empty program language in family audit")
    return best_acc, best_program


def family_selection_audit(parent: object, members: Sequence[MemberSpec]) -> dict[str, object]:
    selected: list[tuple[int, ...]] = []
    for table in parent.FANOUT_PROGRAMS.keys():
        if table in parent.READ_ONCE_PROGRAMS:
            continue
        if essential_variables(table) != frozenset((0, 1, 2)):
            continue
        if tuple(table) == EXCLUDED_RIL001_TRUTH_TABLE:
            continue
        selected.append(tuple(table))
    selected.sort(key=lambda t: int("".join(str(x) for x in t), 2))
    frozen = [m.truth_table for m in members]
    member_checks: dict[str, object] = {}
    all_ceiling = True
    all_canonical = True
    for m in members:
        m0_acc, _ = _best_for_table(parent.READ_ONCE_PROGRAMS, m.truth_table)
        m1_acc, m1_program = _best_for_table(parent.FANOUT_PROGRAMS, m.truth_table)
        ceiling_ok = (m0_acc == m.m0_exact_ceiling == 0.875 and m1_acc == m.m1_exact_ceiling == 1.0)
        canonical_ok = (str(m1_program) == m.canonical_m1_program and m1_program.size() == m.canonical_m1_size)
        all_ceiling = all_ceiling and ceiling_ok
        all_canonical = all_canonical and canonical_ok
        member_checks[m.member_id] = {
            "m0_exact_ceiling": m0_acc,
            "m1_exact_ceiling": m1_acc,
            "canonical_m1_name": str(m1_program),
            "canonical_m1_size": m1_program.size(),
            "ceiling_match": ceiling_ok,
            "canonical_match": canonical_ok,
        }
    exact_family = tuple(selected) == tuple(frozen)
    return {
        "passed": exact_family and all_ceiling and all_canonical and len(members) == 24,
        "exact_K_enumeration_match": exact_family,
        "member_count": len(members),
        "all_ceiling_facts_match": all_ceiling,
        "all_canonical_m1_programs_match": all_canonical,
        "member_checks": member_checks,
    }


def static_pre_execution_audit(ril001_dir: Path, inherited: SimpleNamespace) -> dict[str, object]:
    inherited_blobs = verify_inherited_blobs(ril001_dir)
    inherited_static = inherited.audit.static_fixed_algorithm_audit()
    dataset_source = inspect.getsource(build_member_dataset)
    dataset_common = all(token not in dataset_source for token in ("R0_AST", "R1_SEM8", "Representation"))
    monitoring_ok = hasattr(sys, "monitoring") and hasattr(sys.monitoring.events, "INSTRUCTION")
    passed = (inherited_blobs["passed"] and all(inherited_static.values()) and dataset_common and monitoring_ok)
    return {
        "passed": passed,
        "inherited_blob_identity": inherited_blobs,
        "inherited_RIL001_static_A_fixed": inherited_static,
        "member_dataset_has_no_representation_branch": dataset_common,
        "cpython_instruction_monitoring_available": monitoring_ok,
    }


def member_preservation(parent: object, member: MemberSpec, inherited: SimpleNamespace) -> dict[str, object]:
    probe, heldout = build_member_dataset(parent, member, inherited)
    report = inherited.audit.preservation_check(parent, probe, heldout)
    payload = report.to_dict()
    r0 = payload["details"]["R0"]
    r1 = payload["details"]["R1"]
    payload["member_id"] = member.member_id
    payload["truth_table"] = "".join(str(x) for x in member.truth_table)
    payload["heldout_prediction_digest_R0"] = prediction_digest(r0["heldout_predictions"])
    payload["heldout_prediction_digest_R1"] = prediction_digest(r1["heldout_predictions"])
    return payload


def parent_and_family_audit(parent: object, family_path: Path, ril001_dir: Path,
                            inherited: SimpleNamespace) -> dict[str, object]:
    source = inherited.contract.verify_parent(parent).to_dict()
    members = load_family(family_path)
    family = family_selection_audit(parent, members)
    static = static_pre_execution_audit(ril001_dir, inherited)
    positive = inherited.audit.parent_positive_control(parent)
    passed = family["passed"] and static["passed"] and positive["passed"]
    return {
        "passed": passed,
        "source_audit": source,
        "family_selection_audit": family,
        "static_A_fixed_and_instrumentation": static,
        "inherited_RIL001_parent_positive_control": positive,
    }
