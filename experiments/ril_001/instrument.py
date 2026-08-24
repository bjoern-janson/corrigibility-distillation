"""Frozen RIL-001 opcode, memory, timing, and environment instrumentation."""
from __future__ import annotations
import os
import platform
import sys
import time
import tracemalloc
from types import ModuleType
from typing import Sequence

from algorithm import (apply_repair_update, build_and_run_arm, evaluate_selected,
                       exhaustive_search, run_transform, score_candidate)
from contract import (
    PARENT_COMMIT, PARENT_METHOD_GIT_BLOB, PARENT_REPOSITORY, PARENT_SOURCE_GIT_BLOB,
    PREREGISTRATION_COMMIT, Representation, RILContractError, TIMING_ORDER,
    TIMING_REPETITIONS, TIMING_WARMUP_POLICY, build_candidate_view, build_manifest,
    predict_ast, predict_sem8,
)


class OpcodeCounter:
    """Count CPython ``sys.monitoring`` INSTRUCTION events by frozen region."""
    TOOL_ID = sys.monitoring.OPTIMIZER_ID

    def __init__(self, parent: ModuleType) -> None:
        self.counts = {"translation": 0, "eval": 0, "search": 0, "update": 0}
        self._stack: list[str | None] = []
        self._root = {
            build_manifest.__code__: "translation", build_candidate_view.__code__: "translation",
            predict_ast.__code__: "eval", predict_sem8.__code__: "eval",
            parent.Program.evaluate_local.__code__: "eval", run_transform.__code__: "search",
            exhaustive_search.__code__: "search", score_candidate.__code__: "search",
            evaluate_selected.__code__: "search", apply_repair_update.__code__: "update",
        }
        self._active = False

    def _start_cb(self, code: object, offset: int) -> None:
        self._stack.append(self._root.get(code, self._stack[-1] if self._stack else None))

    def _return_cb(self, code: object, offset: int, *args: object) -> None:
        if self._stack:
            self._stack.pop()

    def _instruction_cb(self, code: object, offset: int) -> None:
        if self._stack and self._stack[-1] is not None:
            self.counts[self._stack[-1]] += 1  # type: ignore[index]

    def start(self) -> None:
        if self._active:
            raise RILContractError("opcode monitor already active")
        m = sys.monitoring
        try:
            m.use_tool_id(self.TOOL_ID, "RIL-001 opcode counter")
        except ValueError as exc:
            raise RILContractError("CPython monitoring tool id unavailable") from exc
        m.register_callback(self.TOOL_ID, m.events.PY_START, self._start_cb)
        m.register_callback(self.TOOL_ID, m.events.PY_RETURN, self._return_cb)
        m.register_callback(self.TOOL_ID, m.events.PY_UNWIND, self._return_cb)
        m.register_callback(self.TOOL_ID, m.events.INSTRUCTION, self._instruction_cb)
        m.set_events(self.TOOL_ID, m.events.PY_START | m.events.PY_RETURN |
                     m.events.PY_UNWIND | m.events.INSTRUCTION)
        self._active = True

    def stop(self) -> None:
        if not self._active:
            return
        m = sys.monitoring
        m.set_events(self.TOOL_ID, m.events.NO_EVENTS)
        for event in (m.events.PY_START, m.events.PY_RETURN, m.events.PY_UNWIND, m.events.INSTRUCTION):
            m.register_callback(self.TOOL_ID, event, None)
        m.free_tool_id(self.TOOL_ID)
        self._active = False
        self._stack.clear()


def opcode_run(parent: ModuleType, representation: Representation,
               probe: Sequence[object], heldout: Sequence[object]) -> dict[str, object]:
    counter = OpcodeCounter(parent)
    counter.start()
    try:
        result = build_and_run_arm(parent, representation, probe, heldout)
    finally:
        counter.stop()
    return {"representation": representation.value,
            "instrumentation": "CPython sys.monitoring INSTRUCTION events",
            "counts": dict(counter.counts), "C_op": sum(counter.counts.values()),
            "result": result.to_dict()}


def memory_run(parent: ModuleType, representation: Representation,
               probe: Sequence[object], heldout: Sequence[object]) -> dict[str, object]:
    tracemalloc.start()
    try:
        result = build_and_run_arm(parent, representation, probe, heldout)
        current, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return {"representation": representation.value, "peak_incremental_bytes": peak,
            "terminal_current_bytes": current, "result": result.to_dict()}


def timing_run(parent: ModuleType, representation: Representation,
               probe: Sequence[object], heldout: Sequence[object]) -> dict[str, object]:
    start = time.perf_counter_ns()
    result = build_and_run_arm(parent, representation, probe, heldout)
    elapsed = time.perf_counter_ns() - start
    return {"representation": representation.value, "elapsed_ns": elapsed,
            "result": result.to_dict()}


def execution_manifest() -> dict[str, object]:
    try:
        affinity = sorted(os.sched_getaffinity(0))
    except (AttributeError, OSError):
        affinity = None
    return {
        "preregistration_commit": PREREGISTRATION_COMMIT,
        "parent_repository": PARENT_REPOSITORY, "parent_commit": PARENT_COMMIT,
        "parent_source_git_blob": PARENT_SOURCE_GIT_BLOB,
        "parent_method_git_blob": PARENT_METHOD_GIT_BLOB,
        "python_version": sys.version, "python_implementation": platform.python_implementation(),
        "python_executable": sys.executable, "platform": platform.platform(),
        "machine": platform.machine(), "processor": platform.processor(),
        "cpu_count": os.cpu_count(), "affinity": affinity,
        "timing_repetitions": TIMING_REPETITIONS,
        "timing_warmup_policy": TIMING_WARMUP_POLICY, "timing_order": TIMING_ORDER,
    }
