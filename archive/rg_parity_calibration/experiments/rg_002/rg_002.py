"""RG-002 instrumentation-repair assay over the frozen RG-001 realizers."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from instrument_v2 import count_cost_v2

EXPECTED_RG001_BLOB = "9a074faf9579e57060de7f1df10093c2a080b8a3"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def load_rg001(rg001_dir: Path):
    path = (rg001_dir / "rg_001.py").resolve()
    observed = git_blob_sha1(path)
    if observed != EXPECTED_RG001_BLOB:
        raise RuntimeError(f"RG-001 realizer blob mismatch: {observed}")
    p = str(rg001_dir.resolve())
    if p not in sys.path:
        sys.path.insert(0, p)
    spec = importlib.util.spec_from_file_location("rg001_frozen_for_rg002", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load frozen RG-001 module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run_validity(rg001) -> dict[str, object]:
    return {
        "R0_LOOP12": rg001.validity_for(rg001.build_r0, rg001.predict_r0),
        "R1_LUT6": rg001.validity_for(rg001.build_r1, rg001.predict_r1),
    }


def run_cost(rg001) -> dict[str, object]:
    r0 = count_cost_v2(
        build=rg001.build_r0,
        predict=rg001.predict_r0,
        build_codes=(rg001.build_r0.__code__,),
        predict_codes=(rg001.predict_r0.__code__,),
        nested_build_codes=(),
    )
    r1 = count_cost_v2(
        build=rg001.build_r1,
        predict=rg001.predict_r1,
        build_codes=(rg001.build_r1.__code__,),
        predict_codes=(rg001.predict_r1.__code__,),
        nested_build_codes=(rg001._parity6_loop.__code__,),
    )
    return {
        "R0_LOOP12": r0,
        "R1_LUT6": r1,
        "lambda_C": r0["total_opcodes"] / r1["total_opcodes"],
    }


def run_robustness(rg001) -> dict[str, object]:
    r0 = rg001.robustness_for(rg001.build_r0, rg001.predict_r0)
    r1 = rg001.robustness_for(rg001.build_r1, rg001.predict_r1)
    set0 = {i for i, v in enumerate(r0["vector"]) if v == "1"}
    set1 = {i for i, v in enumerate(r1["vector"]) if v == "1"}
    return {
        "R0_LOOP12": r0,
        "R1_LUT6": r1,
        "B1_subset_B0": set1.issubset(set0),
        "B1_proper_subset_B0": set1 < set0,
    }


def adjudicate(validity, cost, robustness) -> str:
    v0 = bool(validity["R0_LOOP12"]["valid"])
    v1 = bool(validity["R1_LUT6"]["valid"])
    if not (v0 and v1):
        return "INVALID_REALIZER"
    if int(cost["R0_LOOP12"]["construction_opcodes"]) <= 0 or int(cost["R1_LUT6"]["construction_opcodes"]) <= 0:
        return "NOT_EVALUABLE"
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
    parser.add_argument("--rg001-dir", type=Path, required=True)
    parser.add_argument("--mode", choices=("validity", "cost", "robustness", "all"), required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rg001 = load_rg001(args.rg001_dir)

    if args.mode == "validity":
        payload: object = run_validity(rg001)
    elif args.mode == "cost":
        payload = run_cost(rg001)
    elif args.mode == "robustness":
        payload = run_robustness(rg001)
    else:
        validity = run_validity(rg001)
        cost = run_cost(rg001)
        if cost["R0_LOOP12"]["construction_opcodes"] <= 0 or cost["R1_LUT6"]["construction_opcodes"] <= 0:
            payload = {"validity": validity, "cost": cost, "robustness": None, "verdict": "NOT_EVALUABLE"}
        else:
            robustness = run_robustness(rg001)
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
