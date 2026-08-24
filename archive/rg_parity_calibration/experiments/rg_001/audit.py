"""Static/pre-execution audits for the frozen RG-001 apparatus."""
from __future__ import annotations

import inspect
import platform
import sys

import rg_001


def static_audit() -> dict[str, object]:
    r0_source = inspect.getsource(rg_001.predict_r0)
    r1_build_source = inspect.getsource(rg_001.build_r1) + inspect.getsource(rg_001._parity6_loop)
    r1_predict_source = inspect.getsource(rg_001.predict_r1)

    checks = {
        "domain_size_4096": len(tuple(rg_001.DOMAIN)) == 4096,
        "memory_bytes_64": rg_001.MEMORY_BYTES == 64,
        "fault_count_512": len(rg_001.FAULTS) == 512,
        "r0_prediction_does_not_read_memory": ".memory" not in r0_source,
        "r1_build_has_no_bit_count": "bit_count" not in r1_build_source,
        "r1_prediction_uses_frozen_masks": "0x3F" in r1_predict_source and "& 1" in r1_predict_source,
        "reference_uses_bit_count_only_for_adjudication": "bit_count" in inspect.getsource(rg_001.reference_parity12),
        "trace_api_available": hasattr(sys, "settrace"),
    }
    return {
        "passed": all(checks.values()),
        "checks": checks,
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
    }


if __name__ == "__main__":
    import json
    print(json.dumps(static_audit(), indent=2, sort_keys=True))
