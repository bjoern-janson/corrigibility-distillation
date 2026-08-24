# Research Execution Instructions

Scientific history is append-only at the level of frozen claims. Later positives do not rewrite earlier nulls, and later conjectures do not become historical evidence.

## Current lane state

```text
Corpus Distillation  CLOSED
CGP-001              CLOSED / NOT EVALUABLE
RIL-001              CLOSED / REPRESENTATION_INDUCED_LEVERAGE
RIL-002              CLOSED / FAMILY_WIDE_LEVERAGE
RIL-003              PREREGISTERED / TARGETS UNREVEALED / NOT IMPLEMENTED
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
```

Mutable narrative files may summarize later state but may not silently strengthen these records.

## RIL-003 preregistration boundary

RIL-003 is open **only** at the preregistration layer.

Frozen now:

```text
Q_test
I_shared whitelist
I_target_test forbidden set
R0 = R0_AST
R1 = R1_SEM8
future public entropy rule
held-out family size n=24
member gate G_i=(A_fixed_i,P_i,Lambda_i)
claim ceiling
```

Not present now:

```text
held-out target IDs
held-out truth tables
implementation
target reveal manifest
preservation output
opcode/memory/timing output
Lambda vector
scientific verdict
```

Do not instantiate or infer target identities before the target-reveal phase.

## Q_test discipline

Eligible targets are all 3-input Boolean truth tables for which x,y,z are all essential, excluding exactly the 25 previously tested RIL-001/RIL-002 truth tables.

Expected counts:

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

Held-out target-specific information is forbidden from representation selection/construction, including:

```text
actual target IDs/truth tables
target labels
target M0/M1 status
exact target ceilings
best/canonical target programs
repair outcomes
expected or observed target costs
target-derived features/clusters/similarity
any target-specific cache/index/compilation/code path
```

## Representation freeze

RIL-003 performs no new representation search.

```text
R0_AST:
    candidate payload = frozen canonical Program AST
    prediction = program.evaluate_local((x,y,z))

R1_SEM8:
    candidate payload = frozen exact 8-pattern semantic tuple
    prediction = semantic_tuple[4*x + 2*y + z]
```

No tuning, new features, indexing changes, target-specific lookup/cache, JIT, vectorization, batching asymmetry, pruning, early stopping, candidate reordering, tie-break change, or “minor adaptation” is permitted after this freeze.

## Next legal phase — not yet authorized by this file

A later explicit instruction may begin **generic implementation without target reveal**.

If opened, the intended order is:

```text
implement generic frozen apparatus
-> implementation freeze
-> pre-reveal source/A_fixed/instrumentation audit
-> wait until frozen future Beacon pulse exists
-> instantiate F_test exactly once
-> freeze target reveal manifest
-> execute member preservation gates
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

**Freeze the territory generator. Whitelist shared information. Freeze the coordinates. Do not let held-out target-specific information exist before the protocol says it may exist.**
