from __future__ import annotations

import copy
import json
import random
import sys
from pathlib import Path
from typing import Any


def load_family(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _nodes(case: dict[str, Any]) -> tuple[set[str], set[str]]:
    standings = set(case["standings"])
    warrants = set(case["primitive_warrants"])
    if standings & warrants:
        raise ValueError("standing and warrant namespaces must be disjoint")
    return standings, warrants


def validate_case(case: dict[str, Any]) -> None:
    standings, warrants = _nodes(case)
    support_sets = case["support_sets"]

    if set(support_sets) != standings:
        raise ValueError("every standing must have exactly one support_sets entry")

    for standing, routes in support_sets.items():
        if not isinstance(routes, list) or not routes:
            raise ValueError(f"{standing}: support route family must be nonempty")
        for route in routes:
            if not isinstance(route, list) or not route:
                raise ValueError(f"{standing}: sufficient support set must be nonempty")
            if len(route) != len(set(route)):
                raise ValueError(f"{standing}: duplicate member inside support set")
            unknown = set(route) - standings - warrants
            if unknown:
                raise ValueError(f"{standing}: unknown support member(s): {sorted(unknown)}")

    active = set(case["initial_active_warrants"])
    if not active <= warrants:
        raise ValueError("initial_active_warrants contains unknown warrant")

    challenge = case["challenge"]
    if challenge["standing"] not in standings:
        raise ValueError("challenge standing is unknown")
    if challenge["invalidated_warrant"] not in active:
        raise ValueError("challenge warrant must initially be active")

    replacement = case.get("replacement")
    if replacement is not None:
        if replacement["standing"] not in standings:
            raise ValueError("replacement standing is unknown")
        if replacement["successor_warrant"] not in warrants:
            raise ValueError("replacement warrant is unknown")
        if replacement["successor_warrant"] in active:
            raise ValueError("canonical replacement warrant must be inactive before successor evidence")
        if replacement["successor_evidence_id"] == challenge["counterevidence_id"]:
            raise ValueError("counterevidence and successor evidence must be distinct")

    deps = {
        s: {x for route in support_sets[s] for x in route if x in standings}
        for s in standings
    }
    temporary: set[str] = set()
    permanent: set[str] = set()

    def visit(node: str) -> None:
        if node in permanent:
            return
        if node in temporary:
            raise ValueError("standing dependency cycle detected")
        temporary.add(node)
        for parent in deps[node]:
            visit(parent)
        temporary.remove(node)
        permanent.add(node)

    for standing in standings:
        visit(standing)


def closure(case: dict[str, Any], active_warrants: set[str]) -> dict[str, bool]:
    validate_case(case)
    standings, warrants = _nodes(case)
    if not active_warrants <= warrants:
        raise ValueError("active_warrants contains unknown warrant")

    memo: dict[str, bool] = {}
    visiting: set[str] = set()

    def available(node: str) -> bool:
        if node in warrants:
            return node in active_warrants
        if node in memo:
            return memo[node]
        if node in visiting:
            raise ValueError("standing dependency cycle detected")
        visiting.add(node)
        routes = case["support_sets"][node]
        value = any(all(available(member) for member in route) for route in routes)
        visiting.remove(node)
        memo[node] = value
        return value

    return {standing: available(standing) for standing in sorted(standings)}


def evaluate_case(case: dict[str, Any]) -> dict[str, Any]:
    validate_case(case)
    active0 = set(case["initial_active_warrants"])
    invalidated = case["challenge"]["invalidated_warrant"]
    active1 = active0 - {invalidated}

    phase0 = closure(case, active0)
    phase1 = closure(case, active1)

    challenged = case["challenge"]["standing"]
    if not phase0[challenged]:
        raise ValueError("challenged standing must be valid before challenge")
    if phase1[challenged]:
        raise ValueError("challenge must invalidate the challenged standing in canonical RG001 cases")

    directly_invalidated = [challenged]
    dependency_deferred = sorted(
        s for s in phase0 if s != challenged and phase0[s] and not phase1[s]
    )
    preserved = sorted(s for s in phase0 if phase0[s] and phase1[s])

    result: dict[str, Any] = {
        "case_id": case["case_id"],
        "phase_0": phase0,
        "phase_1": phase1,
        "classification": {
            "directly_invalidated": directly_invalidated,
            "dependency_deferred": dependency_deferred,
            "preserved": preserved,
        },
    }

    replacement = case.get("replacement")
    if replacement is not None:
        successor = replacement["standing"]
        successor_warrant = replacement["successor_warrant"]

        if phase1[successor]:
            raise ValueError("replacement firewall violated by semantic case constitution")

        active2 = active1 | {successor_warrant}
        phase2 = closure(case, active2)
        if not phase2[successor]:
            raise ValueError("successor evidence does not enable replacement under frozen support semantics")
        result["phase_2"] = phase2
        result["replacement_firewall"] = {
            "valid_after_counterevidence_only": phase1[successor],
            "valid_after_successor_evidence": phase2[successor],
        }

    return result


def flatten_incidence(case: dict[str, Any]) -> set[tuple[str, str]]:
    """Forget sufficient-set grouping and retain only parent->standing incidence."""
    return {
        (member, standing)
        for standing, routes in case["support_sets"].items()
        for route in routes
        for member in route
    }


def rename_case(case: dict[str, Any], seed: int) -> tuple[dict[str, Any], dict[str, str]]:
    """Opaque, type-preserving permutation used only for semantic invariance tests."""
    rng = random.Random(seed)
    renamed = copy.deepcopy(case)

    standings = list(case["standings"])
    warrants = list(case["primitive_warrants"])

    s_targets = [f"s_perm_{seed}_{i}" for i in range(len(standings))]
    w_targets = [f"w_perm_{seed}_{i}" for i in range(len(warrants))]
    rng.shuffle(s_targets)
    rng.shuffle(w_targets)

    mapping = dict(zip(standings, s_targets)) | dict(zip(warrants, w_targets))

    renamed["standings"] = [mapping[x] for x in standings]
    renamed["primitive_warrants"] = [mapping[x] for x in warrants]
    renamed["support_sets"] = {
        mapping[s]: [[mapping[x] for x in route] for route in routes]
        for s, routes in case["support_sets"].items()
    }
    renamed["initial_active_warrants"] = [
        mapping[x] for x in case["initial_active_warrants"]
    ]
    renamed["challenge"]["standing"] = mapping[case["challenge"]["standing"]]
    renamed["challenge"]["invalidated_warrant"] = mapping[
        case["challenge"]["invalidated_warrant"]
    ]

    replacement = renamed.get("replacement")
    if replacement is not None:
        replacement["standing"] = mapping[case["replacement"]["standing"]]
        replacement["successor_warrant"] = mapping[
            case["replacement"]["successor_warrant"]
        ]

    return renamed, mapping


def _map_phase(phase: dict[str, bool], mapping: dict[str, str]) -> dict[str, bool]:
    return {mapping[k]: v for k, v in phase.items()}


def assert_permutation_equivariance(case: dict[str, Any], seed: int) -> None:
    original = evaluate_case(case)
    permuted_case, mapping = rename_case(case, seed)
    permuted = evaluate_case(permuted_case)

    if _map_phase(original["phase_0"], mapping) != permuted["phase_0"]:
        raise AssertionError("phase_0 permutation equivariance failed")
    if _map_phase(original["phase_1"], mapping) != permuted["phase_1"]:
        raise AssertionError("phase_1 permutation equivariance failed")
    if "phase_2" in original and _map_phase(original["phase_2"], mapping) != permuted["phase_2"]:
        raise AssertionError("phase_2 permutation equivariance failed")


def audit_family(family: dict[str, Any], permutation_seeds: range = range(32)) -> dict[str, Any]:
    cases = family["cases"]
    if len(cases) != 8:
        raise AssertionError("RG001 v0.1 family must contain exactly 8 cases")

    by_id = {case["case_id"]: case for case in cases}
    if len(by_id) != len(cases):
        raise AssertionError("case ids must be unique")

    results = {case_id: evaluate_case(case) for case_id, case in by_id.items()}

    a = by_id["RG001-C04"]
    b = by_id["RG001-C05"]
    if flatten_incidence(a) != flatten_incidence(b):
        raise AssertionError("matched pair must alias under flattened pairwise incidence")
    if results["RG001-C04"]["phase_1"] == results["RG001-C05"]["phase_1"]:
        raise AssertionError("matched pair must differ under sufficient-support semantics")
    if results["RG001-C04"]["phase_1"]["s_h"] is not False:
        raise AssertionError("C04 H must contract")
    if results["RG001-C05"]["phase_1"]["s_h"] is not True:
        raise AssertionError("C05 H must survive")

    permutation_checks = 0
    for case in cases:
        for seed in permutation_seeds:
            assert_permutation_equivariance(case, seed)
            permutation_checks += 1

    return {
        "status": "PASS",
        "case_count": len(cases),
        "permutation_checks": permutation_checks,
        "matched_pair": {
            "cases": ["RG001-C04", "RG001-C05"],
            "flattened_pairwise_incidence_equal": True,
            "post_challenge_semantics_differ": True,
            "c04_s_h_valid_after_challenge": False,
            "c05_s_h_valid_after_challenge": True,
        },
        "results": results,
        "realizers_admitted": False,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} RG001_CASE_FAMILY.json", file=sys.stderr)
        return 2
    family = load_family(argv[1])
    print(json.dumps(audit_family(family), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
