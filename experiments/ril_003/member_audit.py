"""Post-reveal member preservation audit for frozen RIL-003 targets."""
from __future__ import annotations

from types import SimpleNamespace

from generator_contract import TargetSpec, build_target_dataset, prediction_digest


def member_preservation(parent: object, target: TargetSpec, inherited: SimpleNamespace) -> dict[str, object]:
    probe, heldout = build_target_dataset(parent, target, inherited)
    report = inherited.audit.preservation_check(parent, probe, heldout)
    payload = report.to_dict()
    r0 = payload["details"]["R0"]
    r1 = payload["details"]["R1"]
    payload["member_id"] = target.member_id
    payload["truth_table"] = "".join(str(x) for x in target.truth_table)
    payload["heldout_prediction_digest_R0"] = prediction_digest(r0["heldout_predictions"])
    payload["heldout_prediction_digest_R1"] = prediction_digest(r1["heldout_predictions"])
    return payload
