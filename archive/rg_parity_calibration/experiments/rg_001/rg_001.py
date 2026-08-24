"""RG-001: frozen 12-bit parity realization-geometry assay."""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

from instrument import count_cost

DOMAIN = range(4096)
MEMORY_BYTES = 64
FAULTS = tuple((j, b) for j in range(MEMORY_BYTES) for b in range(8))


@dataclass(frozen=True)
class RealizationState:
    memory: bytearray


class RG001Error(RuntimeError):
    pass


def reference_parity12(x: int) -> int:
    if not 0 <= x < 4096:
        raise ValueError("x outside frozen 12-bit domain")
    return x.bit_count() & 1


def build_r0() -> RealizationState:
    return RealizationState(bytearray(MEMORY_BYTES))


def predict_r0(state: RealizationState, x: int) -> int:
    p = 0
    v = x
    for _ in range(12):
        p ^= v & 1
        v >>= 1
    return p


def _parity6_loop(x: int) -> int:
    p = 0
    v = x
    for _ in range(6):
        p ^= v & 1
        v >>= 1
    return p


def build_r1() -> RealizationState:
    memory = bytearray(MEMORY_BYTES)
    for i in range(MEMORY_BYTES):
        memory[i] = _parity6_loop(i)
    return RealizationState(memory)


def predict_r1(state: RealizationState, x: int) -> int:
    lo = x & 0x3F
    hi = (x >> 6) & 0x3F
    return (state.memory[lo] & 1) ^ (state.memory[hi] & 1)


def validity_for(build, predict) -> dict[str, object]:
    state = build()
    mismatches: list[int] = []
    for x in DOMAIN:
        if predict(state, x) != reference_parity12(x):
            mismatches.append(x)
    return {
        "valid": not mismatches,
        "domain_size": 4096,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
    }


def robustness_for(build, predict) -> dict[str, object]:
    vector: list[int] = []
    preserved_faults: list[str] = []
    for j, b in FAULTS:
        state = build()
        state.memory[j] ^= 1 << b
        preserved = True
        # Complete-domain evaluation is mandatory even after a mismatch.
        for x in DOMAIN:
            if predict(state, x) != reference_parity12(x):
                preserved = False
        vector.append(int(preserved))
        if preserved:
            preserved_faults.append(f"{j}:{b}")
    return {
        "fault_count": len(FAULTS),
        "preserved_count": sum(vector),
        "vector": "".join(str(v) for v in vector),
        "preserved_faults": preserved_faults,
    }


def run_validity() -> dict[str, object]:
    return {
        "R0_LOOP12": validity_for(build_r0, predict_r0),
        "R1_LUT6": validity_for(build_r1, predict_r1),
    }


def run_cost() -> dict[str, object]:
    r0 = count_cost(
        build=build_r0,
        predict=predict_r0,
        build_codes=(build_r0.__code__,),
        predict_codes=(predict_r0.__code__,),
        nested_build_codes=(),
    )
    r1 = count_cost(
        build=build_r1,
        predict=predict_r1,
        build_codes=(build_r1.__code__,),
        predict_codes=(predict_r1.__code__,),
        nested_build_codes=(_parity6_loop.__code__,),
    )
    return {
        "R0_LOOP12": r0,
        "R1_LUT6": r1,
        "lambda_C": r0["total_opcodes"] / r1["total_opcodes"],
    }


def run_robustness() -> dict[str, object]:
    r0 = robustness_for(build_r0, predict_r0)
    r1 = robustness_for(build_r1, predict_r1)
    set0 = {i for i, v in enumerate(r0["vector"]) if v == "1"}
    set1 = {i for i, v in enumerate(r1["vector"]) if v == "1"}
    return {
        "R0_LOOP12": r0,
        "R1_LUT6": r1,
        "B1_subset_B0": set1.issubset(set0),
        "B1_proper_subset_B0": set1 < set0,
    }


def adjudicate(validity: dict[str, object], cost: dict[str, object], robustness: dict[str, object]) -> str:
    v0 = bool(validity["R0_LOOP12"]["valid"])
    v1 = bool(validity["R1_LUT6"]["valid"])
    if not (v0 and v1):
        return "INVALID_REALIZER"
    if int(cost["R1_LUT6"]["total_opcodes"]) >= int(cost["R0_LOOP12"]["total_opcodes"]):
        return "NO_COST_SEPARATION"
    if bool(robustness["B1_proper_subset_B0"]):
        return "COST_ROBUSTNESS_TRADEOFF"
    return "COST_ONLY"


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("validity", "cost", "robustness", "all"), required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.mode == "validity":
        payload: object = run_validity()
    elif args.mode == "cost":
        payload = run_cost()
    elif args.mode == "robustness":
        payload = run_robustness()
    else:
        validity = run_validity()
        cost = run_cost()
        robustness = run_robustness()
        payload = {
            "validity": validity,
            "cost": cost,
            "robustness": robustness,
            "verdict": adjudicate(validity, cost, robustness),
        }

    if args.output:
        write_json(args.output, payload)
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
