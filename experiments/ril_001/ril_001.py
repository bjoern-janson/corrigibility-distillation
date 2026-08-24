"""Command-line entry point for the frozen RIL-001 apparatus."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

from audit import parent_positive_control, preservation_check, static_fixed_algorithm_audit
from contract import (Representation, RILContractError, build_dataset, import_parent,
                      parse_representation, verify_parent)
from instrument import execution_manifest, memory_run, opcode_run, timing_run


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--mode", choices=("source-audit", "parent-positive-control",
        "preservation", "opcode", "memory", "timing", "manifest", "static-audit"), required=True)
    parser.add_argument("--arm", choices=tuple(x.value for x in Representation))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    parent = import_parent(args.parent)
    source = verify_parent(parent)
    probe, heldout = build_dataset(parent)
    if args.mode == "source-audit":
        payload: object = source.to_dict()
    elif args.mode == "parent-positive-control":
        payload = parent_positive_control(parent)
    elif args.mode == "preservation":
        payload = preservation_check(parent, probe, heldout).to_dict()
    elif args.mode == "static-audit":
        payload = static_fixed_algorithm_audit()
    elif args.mode == "manifest":
        payload = execution_manifest()
    else:
        if args.arm is None:
            raise RILContractError(f"--arm required for {args.mode}")
        arm = parse_representation(args.arm)
        payload = {"opcode": opcode_run, "memory": memory_run, "timing": timing_run}[args.mode](
            parent, arm, probe, heldout)
    if args.output:
        write_json(args.output, payload)
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
