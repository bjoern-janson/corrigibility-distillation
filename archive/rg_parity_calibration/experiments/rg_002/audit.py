"""Pre-execution sentinel and static audit for RG-002."""
from __future__ import annotations

import inspect
import json
import platform
import sys
from pathlib import Path

from instrument_v2 import OpcodeCounterV2
from rg_002 import EXPECTED_RG001_BLOB, git_blob_sha1


def sentinel_one_line(): return 7


def sentinel_multi_line():
    value = 0
    for i in range(3):
        value += i
    return value


def audit(rg001_dir: Path) -> dict[str, object]:
    rg001_path = rg001_dir / "rg_001.py"
    one_counter = OpcodeCounterV2((sentinel_one_line.__code__,))
    _, one = one_counter.run(sentinel_one_line)
    multi_counter = OpcodeCounterV2((sentinel_multi_line.__code__,))
    _, multi = multi_counter.run(sentinel_multi_line)
    tracer_source = inspect.getsource(OpcodeCounterV2.trace)
    checks = {
        "rg001_realizer_blob_exact": git_blob_sha1(rg001_path) == EXPECTED_RG001_BLOB,
        "one_line_sentinel_positive": one > 0,
        "multi_line_sentinel_positive": multi > 0,
        "tracer_activates_on_call": 'event in ("call", "line")' in tracer_source,
        "tracer_activates_on_line": 'event in ("call", "line")' in tracer_source,
    }
    return {
        "passed": all(checks.values()),
        "checks": checks,
        "sentinel_counts": {"one_line": one, "multi_line": multi},
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
    }


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--rg001-dir", type=Path, required=True)
    args = p.parse_args()
    print(json.dumps(audit(args.rg001_dir), indent=2, sort_keys=True))
