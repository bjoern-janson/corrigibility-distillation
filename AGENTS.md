# Research Execution Instructions

## Purpose

This repository preserves a closed corpus-distillation program and completed downstream prospective assays. Scientific history is append-only at the level of frozen claims.

## Current lane state

### Corpus Distillation

`CLOSED`.

Do not alter the frozen corpus, necessity counts, L3/L4/L5/L6 record, common-core conclusion, or minimization closure through later experiments.

### CGP-001

`CLOSED / NOT EVALUABLE`.

```text
A_trans           FAIL
failed criteria   [8,9]
primary execution NOT RUN
H_CG              NOT TESTED
```

Do not repair, rerun, score, or reinterpret CGP-001. Any new corridor requires a new preregistration.

### RIL-001

`CLOSED / REPRESENTATION_INDUCED_LEVERAGE`.

Anchors:

```text
preregistration       204fe919159145ac9c29f1becfb92b0c511af02b
implementation freeze a0f8f795a805e8f579fd608fbcaa83dcfa6ef60f
pre-execution audit   6b3b865f3fce07fe835e169d80ec8f72f192f4bf
```

Terminal bounded result:

```text
P1-P9                  PASS
c_search equality      PASS
c_update equality      PASS
C_op R0                9,825,003
C_op R1                4,094,613
Lambda_F^op            2.399494897320
peak memory R0         206,757 bytes
peak memory R1         206,757 bytes
terminal status        REPRESENTATION_INDUCED_LEVERAGE
```

Do not optimize, repair, rerun as a primary assay, change instrumentation, or strengthen its claim under `RIL-001`.

## Frozen scientific records

Treat these as immutable scientific records:

```text
CORPUS.md
NECESSITY_AUDIT.md
CGP_001_PREREGISTRATION.md
CGP_001_TRANSLATION_AUDIT.md
experiments/cgp_001/*
RIL_001_PREREGISTRATION.md
RIL_001_PRE_EXECUTION_AUDIT.md
experiments/ril_001/ implementation files at a0f8f795...
RIL_001_RESULT.md
RIL_001_RESULT.json
RIL_001_FINAL_AUDIT.md
```

Mutable narrative files (`README.md`, `STATUS.md`, `ROADMAP.md`, `AGENTS.md`) may summarize later state but may not change frozen evidence.

## Governing evidence distinctions

Preserve:

```text
mechanism != function != invariant
recurrence != necessity
local necessity != universal necessity
same abstract lesson != shared semantic type
serialization compatibility != interface compatibility
candidate != oracle != evaluator
possibility != authority
search allocation != repair/adoption authority
adapter correctness != corridor evidence
cheapness != semantic preservation
formal possibility != empirical leverage
single-function leverage != family leverage
family leverage != held-out generality
```

On failure or contradiction, revise the shallowest supported layer and preserve every unaffected null or positive result.

## RIL-001 claim ceiling

The earned claim is exactly bounded to the frozen FS007 low-cost `NEEDS_FANOUT` function, condition, candidate languages, CPython 3.13.5 implementation, and AST-vs-existing-SEM8 representation pair.

RIL-001 does not establish:

```text
representation-induced family leverage
held-out representation-induced generality
resource-boundary amplification
universal affordance geometry
intelligence = representation
general hardware-capability amplification
common corrigibility architecture
```

## Future RIL work

`ROADMAP.md` contains conjectural rungs RIL-2 through RIL-5. They are **not opened by default**.

Any future experiment must:

1. receive a new identifier and prospective preregistration;
2. state exactly which RIL-001 fact is used as prior evidence;
3. freeze its own `F`, `D`, representation choice/learning procedure, preservation predicate, budget/cost vector, and null;
4. prevent training/representation selection from seeing held-out transformation outcomes where held-out generality is tested;
5. count representation construction/learning cost where applicable;
6. preserve authority/scope identity before interpreting cost;
7. stop at its own claim ceiling.

Do not turn the roadmap objects `A(R)`, `Omega_eff(R;B)`, or payback horizon `n*` into established theory merely because RIL-001 is positive.

## No currently authorized experiment

At the present repository state there is no automatically authorized RIL-002, RIL-2, CGP-002, composition study, or theory-expansion task. A new lane begins only by explicit prospective instruction.

## Final rule

**Change the coordinates. Hold the correction fixed. Count every cost. Preserve every null.**
