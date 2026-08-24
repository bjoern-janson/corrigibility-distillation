# Research Execution Instructions

Scientific history is append-only at the level of frozen claims. Later positives do not rewrite earlier nulls, and later conjectures do not become historical evidence.

## Current lane state

```text
Corpus Distillation  CLOSED
CGP-001              CLOSED / NOT EVALUABLE
RIL-001              CLOSED / REPRESENTATION_INDUCED_LEVERAGE
RIL-002              CLOSED / FAMILY_WIDE_LEVERAGE
RIL-003              IMPLEMENTATION FROZEN / PRE-REVEAL AUDIT PASS / TARGETS UNREVEALED
RIL-4+               NOT OPENED
```

## Immutable scientific records

Treat as frozen:

```text
CORPUS.md
NECESSITY_AUDIT.md
CGP_001_PREREGISTRATION.md
CGP_001_TRANSLATION_AUDIT.md
experiments/cgp_001/*
RIL_001_PREREGISTRATION.md
RIL_001_PRE_EXECUTION_AUDIT.md
experiments/ril_001/* at a0f8f795...
RIL_001_RESULT.*
RIL_001_FINAL_AUDIT.md
RIL_002_PREREGISTRATION.md
RIL_002_FAMILY.json
RIL_002_PRE_EXECUTION_AUDIT.md
experiments/ril_002/* at d46dffe2...
RIL_002_RESULT.*
RIL_002_FINAL_AUDIT.md
RIL_003_PREREGISTRATION.md
RIL_003_GENERATOR_CONTRACT.json
experiments/ril_003/* at f54d9e1a...
RIL_003_PRE_REVEAL_AUDIT.md
```

Mutable narrative files may summarize later state but may not silently strengthen these records.

## RIL-003 frozen provenance boundary

Scientific anchors:

```text
preregistration freeze   c5acae018aec09afc9ceece152bb9cdc7a39e112
implementation freeze    f54d9e1a4d8ef35404824d2172ace173af387a96
pre-reveal audit         013435145d7d93985cd056926cfad710dd63e662
entropy target time      2026-08-26T12:00:00.000Z
```

Frozen now:

```text
Q_test
I_shared whitelist
I_target_test forbidden set
R0 = R0_AST
R1 = R1_SEM8
future public entropy rule
held-out family size n=24
generic execution apparatus
member gate G_i=(A_fixed_i,P_i,Lambda_i)
claim ceiling
```

Still absent:

```text
held-out target IDs
held-out truth tables
target reveal manifest
member preservation output
opcode/memory output
Lambda vector
scientific verdict
```

## Pre-reveal apparatus discipline

The implementation is immutable under RIL-003 after `f54d9e1a...`.

It must retain these properties:

```text
exact inherited RIL-001 contract/algorithm/instrument/audit blobs
no Beacon network client
reveal requires externally captured pulse package
wall-clock reveal gate at 2026-08-26T12:00:00.000Z
Q_test eligible count = 193
sample size = 24
manifest selection recomputed from recorded outputValue
no representation-specific branch outside inherited AST/SEM8 predictor primitive
```

Do not modify the frozen apparatus after observing any future Beacon or target information. Any such change requires a new assay identifier.

## Q_test discipline

Eligible targets are all 3-input Boolean truth tables for which x,y,z are all essential, excluding exactly the 25 previously tested RIL-001/RIL-002 truth tables.

```text
all-essential targets  218
excluded prior targets  25
eligible universe       193
future sample            24
```

Eligibility must not use M0/M1 membership, canonical program size, exact ceilings, prior leverage, or predicted representation cost.

The later target sample is determined only by the preregistered future NIST Randomness Beacon 2.0 pulse and frozen SHA-256 ranking rule. No redraw, substitution, balancing, or post-reveal family shaping is permitted.

## Shared-information whitelist

Shared schema/interface information is allowed because the test must remain well-typed. The exact whitelist is in `RIL_003_PREREGISTRATION.md` and `RIL_003_GENERATOR_CONTRACT.json`.

Held-out target-specific information remains forbidden from representation selection/construction, including target IDs/truth tables, labels, M0/M1 status, exact ceilings, best programs, repair outcomes, expected/observed costs, target-derived features, and target-specific caches or compilation.

## Next legal transition

Before the frozen entropy boundary, do not perform any target-specific operation.

After the first admissible future Beacon pulse is captured:

```text
validate pulse package
-> materialize F_test exactly once from frozen Q_test
-> commit RIL_003_TARGET_MANIFEST.json
-> audit pulse/manifest provenance
-> only then execute member preservation
-> interpret Lambda only where P_i=1
-> publish ordered Lambda vector
-> final audit
-> STOP
```

No target execution may precede the reveal-manifest freeze.

## Claim ceiling

A positive RIL-003 result can earn only:

```text
PROVENANCE_SEPARATED_REPRESENTATION_INDUCED_TRANSFER
```

It cannot by itself establish representation-induced generality, resource-boundary amplification, broad constrained-hardware generality, or universal affordance geometry.

## Final rule

**Freeze the territory generator. Whitelist shared information. Freeze the coordinates and apparatus. Do not let held-out target-specific information enter until the protocol says it may exist.**
