"""Command-line entry point for frozen RIL-002 family-transfer apparatus."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from family_audit import member_preservation, parent_and_family_audit
from family_contract import (
    RIL2ContractError, build_member_dataset, execution_manifest, load_family,
    load_inherited, member_by_id,
)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--family", type=Path, required=True)
    parser.add_argument("--ril001-dir", type=Path, required=True)
    parser.add_argument("--mode", choices=("pre-exec-audit", "manifest", "preservation", "opcode", "memory"), required=True)
    parser.add_argument("--member")
    parser.add_argument("--arm", choices=("R0_AST", "R1_SEM8"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    inherited = load_inherited(args.ril001_dir)
    parent = inherited.contract.import_parent(args.parent)
    members = load_family(args.family)

    if args.mode == "pre-exec-audit":
        payload: object = parent_and_family_audit(parent, args.family, args.ril001_dir, inherited)
    elif args.mode == "manifest":
        inherited.contract.verify_parent(parent)
        payload = execution_manifest(inherited)
    else:
        if args.member is None:
            raise RIL2ContractError(f"--member required for {args.mode}")
        member = member_by_id(members, args.member)
        inherited.contract.verify_parent(parent)
        if args.mode == "preservation":
            payload = member_preservation(parent, member, inherited)
        else:
            if args.arm is None:
                raise RIL2ContractError(f"--arm required for {args.mode}")
            rep = inherited.contract.parse_representation(args.arm)
            probe, heldout = build_member_dataset(parent, member, inherited)
            runner = inherited.instrument.opcode_run if args.mode == "opcode" else inherited.instrument.memory_run
            payload = runner(parent, rep, probe, heldout)
            payload["member_id"] = member.member_id
            payload["truth_table"] = "".join(str(x) for x in member.truth_table)

    if args.output:
        write_json(args.output, payload)
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
