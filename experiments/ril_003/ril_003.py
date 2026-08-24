"""Command-line entry point for frozen RIL-003 apparatus.

Pre-reveal modes cannot contact the Beacon or instantiate held-out targets.
The later reveal mode requires a captured Beacon package file and enforces the
frozen wall-clock boundary before target selection.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from generator_contract import (
    RIL3ContractError, build_target_dataset, execution_manifest, load_inherited,
    load_target_manifest, materialize_target_manifest, target_by_id,
    verify_generator_contract,
)
from member_audit import member_preservation
from pre_reveal_audit import static_pre_reveal_audit


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--generator-contract", type=Path, required=True)
    parser.add_argument("--parent", type=Path, required=True)
    parser.add_argument("--ril001-dir", type=Path, required=True)
    parser.add_argument("--mode", choices=(
        "pre-reveal-audit", "execution-manifest", "reveal-targets",
        "preservation", "opcode", "memory",
    ), required=True)
    parser.add_argument("--beacon-package", type=Path)
    parser.add_argument("--target-manifest", type=Path)
    parser.add_argument("--member")
    parser.add_argument("--arm", choices=("R0_AST", "R1_SEM8"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    inherited = load_inherited(args.ril001_dir)
    parent = inherited.contract.import_parent(args.parent)
    verify_generator_contract(args.generator_contract)

    if args.mode == "pre-reveal-audit":
        payload: object = static_pre_reveal_audit(
            args.repo_root, args.generator_contract, args.ril001_dir, inherited, parent)
    elif args.mode == "execution-manifest":
        inherited.contract.verify_parent(parent)
        payload = execution_manifest(inherited)
    elif args.mode == "reveal-targets":
        if args.beacon_package is None:
            raise RIL3ContractError("--beacon-package required for reveal-targets")
        # No network access: caller must supply the exact captured NIST pulse package.
        payload = materialize_target_manifest(args.beacon_package.read_bytes())
    else:
        if args.target_manifest is None or args.member is None:
            raise RIL3ContractError(f"--target-manifest and --member required for {args.mode}")
        targets = load_target_manifest(args.target_manifest)
        target = target_by_id(targets, args.member)
        inherited.contract.verify_parent(parent)
        if args.mode == "preservation":
            payload = member_preservation(parent, target, inherited)
        else:
            if args.arm is None:
                raise RIL3ContractError(f"--arm required for {args.mode}")
            rep = inherited.contract.parse_representation(args.arm)
            probe, heldout = build_target_dataset(parent, target, inherited)
            runner = inherited.instrument.opcode_run if args.mode == "opcode" else inherited.instrument.memory_run
            payload = runner(parent, rep, probe, heldout)
            payload["member_id"] = target.member_id
            payload["truth_table"] = "".join(str(x) for x in target.truth_table)

    if args.output:
        write_json(args.output, payload)
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
