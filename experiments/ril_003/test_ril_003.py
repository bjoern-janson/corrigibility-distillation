"""Pre-reveal tests for the RIL-003 apparatus.

These tests never instantiate the future held-out family.
"""
from __future__ import annotations

import json
from datetime import timedelta

import pytest

from generator_contract import (
    EXPECTED_ALL_ESSENTIAL_COUNT, EXPECTED_ELIGIBLE_COUNT, PRIOR_EXCLUDED_VALUES,
    SAMPLE_SIZE, TARGET_TIME_UTC, RevealNotAvailable, eligible_universe_summary,
    materialize_target_manifest, truth_table_from_value, value_from_truth_table,
)


def test_truth_table_roundtrip_all_values() -> None:
    for value in range(256):
        assert value_from_truth_table(truth_table_from_value(value)) == value


def test_frozen_universe_counts_only() -> None:
    summary = eligible_universe_summary()
    assert summary == {
        "all_three_essential_count": EXPECTED_ALL_ESSENTIAL_COUNT,
        "prior_exact_exclusion_count": len(PRIOR_EXCLUDED_VALUES),
        "eligible_count": EXPECTED_ELIGIBLE_COUNT,
        "sample_size": SAMPLE_SIZE,
    }
    assert EXPECTED_ALL_ESSENTIAL_COUNT == 218
    assert EXPECTED_ELIGIBLE_COUNT == 193
    assert len(PRIOR_EXCLUDED_VALUES) == 25


def test_reveal_refuses_before_frozen_boundary_without_selecting_targets() -> None:
    synthetic = {
        "pulse": {
            "version": "2.0",
            "timeStamp": "2026-08-26T12:00:00.000Z",
            "chainIndex": 1,
            "pulseIndex": 1,
            "outputValue": "00" * 64,
        }
    }
    package = json.dumps(synthetic, sort_keys=True).encode("utf-8")
    with pytest.raises(RevealNotAvailable):
        materialize_target_manifest(package, now_utc=TARGET_TIME_UTC - timedelta(seconds=1))
