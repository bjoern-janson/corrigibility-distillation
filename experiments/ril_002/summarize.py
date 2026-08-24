"""Frozen RIL-002 post-execution member and family adjudicator."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from family_contract import load_family, prediction_digest


def read(path: Path) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def adjudicate_member(root: Path, member_id: str, global_audit_pass: bool) -> dict[str, object]:
    d = root / member_id
    preservation = read(d / "preservation.json")
    p = bool(preservation["passed"])
    if not p:
        return {
            "member_id": member_id, "A_fixed": global_audit_pass, "P": False,
            "C_op_R0": None, "C_op_R1": None, "Lambda_op": None,
            "memory_R0": None, "memory_R1": None,
            "member_status": "PRESERVATION_FAILURE",
            "selected_canonical_identity": preservation["details"]["R0"]["selected_canonical_name"],
            "heldout_prediction_digest": preservation["heldout_prediction_digest_R0"],
        }
    op0, op1 = read(d / "opcode_R0_AST.json"), read(d / "opcode_R1_SEM8.json")
    mem0, mem1 = read(d / "memory_R0_AST.json"), read(d / "memory_R1_SEM8.json")
    counts0, counts1 = op0["counts"], op1["counts"]
    dynamic_equal = counts0["search"] == counts1["search"] and counts0["update"] == counts1["update"]
    a_fixed = bool(global_audit_pass and dynamic_equal)
    c0, c1 = int(op0["C_op"]), int(op1["C_op"])
    m0, m1 = int(mem0["peak_incremental_bytes"]), int(mem1["peak_incremental_bytes"])
    lam = c0 / c1 if a_fixed else None
    if not a_fixed:
        status = "NOT_EVALUABLE"
    elif c1 < c0 and m1 <= m0:
        status = "REPRESENTATION_INDUCED_LEVERAGE"
    elif c1 < c0 and m1 > m0:
        status = "COMPUTE_FOR_MEMORY_TRADEOFF"
    else:
        status = "NO_DEMONSTRATED_LEVERAGE"
    return {
        "member_id": member_id,
        "A_fixed": a_fixed,
        "P": True,
        "C_op_R0": c0,
        "C_op_R1": c1,
        "Lambda_op": lam,
        "memory_R0": m0,
        "memory_R1": m1,
        "member_status": status,
        "dynamic_search_equal": counts0["search"] == counts1["search"],
        "dynamic_update_equal": counts0["update"] == counts1["update"],
        "selected_canonical_identity": preservation["details"]["R0"]["selected_canonical_name"],
        "heldout_prediction_digest": preservation["heldout_prediction_digest_R0"],
    }


def family_status(rows: list[dict[str, object]]) -> str:
    if any(r["member_status"] == "NOT_EVALUABLE" for r in rows):
        return "FAMILY_NOT_FULLY_EVALUABLE"
    if any(r["member_status"] == "PRESERVATION_FAILURE" for r in rows):
        return "FAMILY_PRESERVATION_NOT_UNIVERSAL"
    full = [r["member_status"] == "REPRESENTATION_INDUCED_LEVERAGE" for r in rows]
    if all(full):
        return "FAMILY_WIDE_LEVERAGE"
    if any(full):
        return "HETEROGENEOUS_LEVERAGE"
    return "NO_FAMILY_LEVERAGE"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", type=Path, required=True)
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument("--pre-exec-audit", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    members = load_family(args.family)
    pre = read(args.pre_exec_audit)
    global_pass = bool(pre["passed"])
    rows = [adjudicate_member(args.results_dir, m.member_id, global_pass) for m in members]
    valid = [r for r in rows if r["A_fixed"] and r["P"]]
    compute_positive = [r for r in valid if r["Lambda_op"] is not None and r["Lambda_op"] > 1]
    full_positive = [r for r in valid if r["member_status"] == "REPRESENTATION_INDUCED_LEVERAGE"]
    payload = {
        "assay": "RIL-002",
        "family_status": family_status(rows),
        "member_count": len(rows),
        "members": rows,
        "leverage_vector": [r["Lambda_op"] for r in rows],
        "kappa_F_op": (len(compute_positive) / len(valid)) if valid else None,
        "full_RIL_coverage": (len(full_positive) / len(valid)) if valid else None,
        "valid_member_count": len(valid),
        "claim_ceiling": "bounded family transfer only; not provenance-separated generalization",
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
