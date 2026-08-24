# RG-002 — Realization Geometry Instrumentation-Repair Preregistration

Status: **PROSPECTIVE REPAIR ASSAY; SCIENTIFIC OBJECT INHERITED UNCHANGED FROM RG-001; NOT AN INDEPENDENT REPLICATION**

Branch: `rg-001-realization-geometry`

Parent null: `RG-001 = CLOSED / NOT_EVALUABLE` due to a CPython opcode-tracing defect that failed to count one-line `build_r0` construction opcodes.

## 1. Purpose

RG-002 asks the same bounded scientific question as RG-001 using the same preselected function, realizers, shared substrate, validity criterion, robustness perturbation universe, and claim ceiling. The only permitted change is repair of the opcode tracer so the preregistered construction region is actually counted.

RG-002 is not blind to the failed RG-001 cost attempt. It therefore cannot be presented as an independent replication. It is a prospective measurement-layer repair of a scientific object that was frozen before the RG-001 primary result existed.

## 2. Inherited scientific object — immutable

Exactly inherit from `RG_001_PREREGISTRATION.md`:

```text
F              PARITY12 over x=0..4095
r0             LOOP12
r1             LUT6
aux memory     64 bytes for both realizers
V              exact equality on all 4096 inputs
Delta          all 512 one-bit flips in the shared 64-byte auxiliary region
B_F(r)         exact set of faults preserving full-domain validity
primary object (V0,C0,B0; V1,C1,B1)
```

The frozen RG-001 operative realizer blob must remain exactly:

```text
experiments/rg_001/rg_001.py
9a074faf9579e57060de7f1df10093c2a080b8a3
```

No function, realizer, mask, memory size, reference semantics, fault set, domain order, or robustness procedure may change under RG-002.

## 3. Sole repair: opcode tracer activation

RG-001 used `sys.settrace` and set:

```python
frame.f_trace_opcodes = True
```

only on target-frame `call` events. On CPython 3.13.5 this missed opcodes in the one-line `build_r0` function before opcode tracing became active.

RG-002 freezes the corrected rule:

```text
for target code frames:
    on event == "call": set frame.f_trace_opcodes = True
    on event == "line": set frame.f_trace_opcodes = True
    on event == "opcode": increment count
```

No other instrumentation semantics may change.

The counted cost regions remain exactly:

```text
one realizer construction
one exhaustive ascending prediction sweep x=0..4095
```

The shared harness, reference function, tracer implementation, serialization, and robustness execution remain excluded.

## 4. Pre-execution sentinel audit

Before primary execution, the corrected tracer must be tested only on two synthetic sentinel functions unrelated to `PARITY12`:

```text
one-line sentinel returning a constant
multi-line sentinel with a small loop
```

Both must produce strictly positive opcode counts.

The sentinel audit must not call `build_r0`, `build_r1`, `predict_r0`, `predict_r1`, exhaustive validity, primary cost, or robustness.

## 5. Execution order

```text
RG-002 preregistration freeze
-> corrected tracer implementation
-> implementation freeze
-> sentinel/static pre-execution audit
-> validity
-> cost
-> robustness
-> result
-> final audit
-> STOP
```

If either construction region still records zero opcodes, RG-002 is `NOT_EVALUABLE` and robustness is not run.

## 6. Outcome taxonomy

Inherited unchanged:

```text
NOT_EVALUABLE
INVALID_REALIZER
NO_COST_SEPARATION
COST_ONLY
COST_ROBUSTNESS_TRADEOFF
```

For `COST_ROBUSTNESS_TRADEOFF`:

```text
V0 = V1 = 1
C1 < C0
B1 proper subset of B0
```

## 7. Claim ceiling

Maximum positive claim remains:

> **Under the exact frozen 12-bit parity function, CPython 3.13.5 opcode-cost contract, two frozen realizers, and one-bit auxiliary-memory fault model, the experiment demonstrates a bounded cost/robustness separation between two valid realizations of the same function.**

This does not establish realization geometry as a theory, biological affordance migration, representation-induced generality, environmental autonomy, hardware-independent cost relations, or any RIL-003 result.

## 8. RIL-003 firewall

RG-002 inherits the RG-001 firewall unchanged. No Beacon, target, manifest, RIL-003 result, or RIL-003 apparatus modification is permitted.
