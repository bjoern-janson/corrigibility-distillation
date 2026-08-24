"""Pre-reveal static audit for RIL-003. Never instantiates held-out targets."""
from __future__ import annotations

import ast
import inspect
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

from generator_contract import (
    TARGET_TIME_UTC, build_target_dataset, eligible_universe_summary,
    materialize_target_manifest, verify_generator_contract, verify_inherited_blobs,
)

FORBIDDEN_NETWORK_IMPORT_ROOTS = {"requests", "urllib", "http", "socket"}


def _network_imports_in_source(source: str) -> list[str]:
    tree = ast.parse(source)
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in FORBIDDEN_NETWORK_IMPORT_ROOTS:
                    found.add(alias.name)
        elif isinstance(node, ast.ImportFrom) and node.module:
            root = node.module.split(".")[0]
            if root in FORBIDDEN_NETWORK_IMPORT_ROOTS:
                found.add(node.module)
    return sorted(found)


def no_reveal_artifacts(repo_root: Path) -> dict[str, object]:
    forbidden = [
        repo_root / "RIL_003_TARGET_MANIFEST.json",
        repo_root / "RIL_003_RESULT.json",
        repo_root / "RIL_003_RESULT.md",
        repo_root / "RIL_003_FINAL_AUDIT.md",
    ]
    present = [str(p.relative_to(repo_root)) for p in forbidden if p.exists()]
    result_dir = repo_root / "experiments" / "ril_003" / "results"
    if result_dir.exists():
        present.extend(str(p.relative_to(repo_root)) for p in result_dir.rglob("*") if p.is_file())
    return {"passed": not present, "forbidden_artifacts_present": present}


def static_pre_reveal_audit(repo_root: Path, generator_contract_path: Path,
                            ril001_dir: Path, inherited: SimpleNamespace,
                            parent: object) -> dict[str, object]:
    generator = verify_generator_contract(generator_contract_path)
    inherited_blobs = verify_inherited_blobs(ril001_dir)
    source = inherited.contract.verify_parent(parent).to_dict()
    inherited_static = inherited.audit.static_fixed_algorithm_audit()

    universe = eligible_universe_summary()
    dataset_source = inspect.getsource(build_target_dataset)
    dataset_common = all(token not in dataset_source for token in ("R0_AST", "R1_SEM8", "Representation"))

    reveal_source = inspect.getsource(materialize_target_manifest)
    wall_clock_gate_present = "now < TARGET_TIME_UTC" in reveal_source

    module_sources = (
        inspect.getsource(sys.modules["generator_contract"]),
        inspect.getsource(sys.modules[__name__]),
    )
    network_imports = sorted({name for source_text in module_sources
                              for name in _network_imports_in_source(source_text)})
    offline_only = not network_imports
    monitoring_ok = hasattr(sys, "monitoring") and hasattr(sys.monitoring.events, "INSTRUCTION")
    artifacts = no_reveal_artifacts(repo_root)
    boundary_in_future_at_audit = datetime.now(timezone.utc) < TARGET_TIME_UTC

    representations_frozen = (
        inherited.contract.Representation.R0_AST.value == "R0_AST"
        and inherited.contract.Representation.R1_SEM8.value == "R1_SEM8"
        and "evaluate_local" in inspect.getsource(inherited.contract.predict_ast)
        and "4 * x + 2 * y + z" in inspect.getsource(inherited.contract.predict_sem8)
    )

    passed = all((
        generator["passed"], inherited_blobs["passed"], source["constants_match"],
        all(inherited_static.values()), universe["eligible_count"] == 193,
        dataset_common, wall_clock_gate_present, offline_only, monitoring_ok,
        artifacts["passed"], representations_frozen,
    ))
    return {
        "passed": passed,
        "generator_contract": generator,
        "eligible_universe_counts_only": universe,
        "inherited_blob_identity": inherited_blobs,
        "parent_source_audit": source,
        "inherited_RIL001_static_A_fixed": inherited_static,
        "target_dataset_has_no_representation_branch": dataset_common,
        "reveal_requires_wall_clock_boundary": wall_clock_gate_present,
        "apparatus_has_no_network_fetch_path": offline_only,
        "forbidden_network_imports": network_imports,
        "cpython_instruction_monitoring_available": monitoring_ok,
        "representations_match_frozen_R0_R1": representations_frozen,
        "no_target_or_result_artifacts": artifacts,
        "entropy_boundary_in_future_at_audit": boundary_in_future_at_audit,
        "held_out_targets_instantiated_by_this_audit": False,
    }
