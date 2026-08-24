# RG-001 — Terminal Result

Status: **NOT_EVALUABLE — PRIMARY COST INSTRUMENTATION FAILED THE FROZEN CONTRACT**

## Frozen anchors

```text
preregistration freeze  7b2d5e5d7a36b563cdf95dd10a680a8748a56240
implementation freeze   64877fa2042ee2bdf837dc19192b3f40d03a56d3
pre-execution audit     0390c37372386fb593da359c23c18b5ed7bab827
```

## Validity

The first primary gate was executed exactly as frozen:

```text
R0_LOOP12  4096 / 4096 exact, 0 mismatches
R1_LUT6    4096 / 4096 exact, 0 mismatches
```

Therefore:

```text
V0 = 1
V1 = 1
```

## Cost instrumentation failure

The frozen opcode-cost run returned:

```text
R0_LOOP12 construction_opcodes = 0
R0_LOOP12 prediction_opcodes   = 634725
R1_LUT6 construction_opcodes   = 5229
R1_LUT6 prediction_opcodes     = 98280
```

`R0_LOOP12 construction_opcodes = 0` is impossible for the nonempty Python `build_r0` function and violates the preregistered requirement that one construction be counted in `C`.

A diagnostic trace performed after observing the anomaly established the shallow mechanism:

```text
CPython 3.13.5
setting frame.f_trace_opcodes = True only at the function `call` event
-> one-line build_r0 reaches a `line` event but emits no opcode events to this tracer configuration

setting frame.f_trace_opcodes = True at the subsequent `line` event
-> build_r0 opcode events become visible
```

This is an instrumentation/interface failure, not evidence about the scientific cost relation.

The observed `lambda_C` from the invalid cost record receives **no scientific interpretation**.

## Robustness

The preregistered order was:

```text
validity -> cost -> robustness
```

Because the cost gate became invalid, robustness was **not run** under RG-001.

## Terminal verdict

```text
RG-001 = NOT_EVALUABLE
failure locus = measurement / instrumentation
validity = PASS for both realizers
cost = INVALID / UNINTERPRETABLE
robustness = NOT RUN
realization-geometry claim = NOT TESTED BY RG-001
RIL-003 = UNTOUCHED
```

No frozen RG-001 apparatus file is repaired under this identifier.
