"""Deterministic CPython opcode instrumentation for RG-001."""
from __future__ import annotations

import sys
from types import CodeType
from typing import Callable, Iterable

DOMAIN = range(4096)


class OpcodeCounter:
    def __init__(self, codes: Iterable[CodeType]):
        self.codes = frozenset(codes)
        self.count = 0

    def trace(self, frame, event, arg):
        if event == "call":
            if frame.f_code in self.codes:
                frame.f_trace_opcodes = True
            return self.trace
        if event == "opcode" and frame.f_code in self.codes:
            self.count += 1
        return self.trace

    def run(self, fn: Callable[[], object]) -> tuple[object, int]:
        previous = sys.gettrace()
        if previous is not None:
            raise RuntimeError("RG-001 requires no pre-existing Python trace function")
        try:
            sys.settrace(self.trace)
            value = fn()
        finally:
            sys.settrace(None)
        return value, self.count


def count_cost(*, build, predict, build_codes, predict_codes, nested_build_codes) -> dict[str, int]:
    build_counter = OpcodeCounter(tuple(build_codes) + tuple(nested_build_codes))
    state, construction = build_counter.run(build)

    prediction_counter = OpcodeCounter(tuple(predict_codes))

    def exhaustive_prediction_sweep() -> None:
        for x in DOMAIN:
            predict(state, x)

    _, prediction = prediction_counter.run(exhaustive_prediction_sweep)
    return {
        "construction_opcodes": construction,
        "prediction_opcodes": prediction,
        "total_opcodes": construction + prediction,
        "prediction_calls": 4096,
    }
