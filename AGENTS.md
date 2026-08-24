# Research Execution Instructions

Scientific history is append-only at the level of frozen claims.

## Lane state

```text
Corpus Distillation   CLOSED
CGP-001               CLOSED / NOT EVALUABLE
RIL-001               CLOSED / REPRESENTATION_INDUCED_LEVERAGE
RIL-002               FAMILY FROZEN / NOT IMPLEMENTED / NOT EXECUTED
RIL-3+                NOT OPENED
```

## Frozen records

Do not rewrite:

```text
CORPUS.md
NECESSITY_AUDIT.md
CGP_001_PREREGISTRATION.md
CGP_001_TRANSLATION_AUDIT.md
experiments/cgp_001/*
RIL_001_PREREGISTRATION.md
RIL_001_PRE_EXECUTION_AUDIT.md
RIL_001_RESULT.md
RIL_001_RESULT.json
RIL_001_FINAL_AUDIT.md
experiments/ril_001/* at implementation freeze a0f8f795...
RIL_002_PREREGISTRATION.md
RIL_002_FAMILY.json
```

Mutable narrative files may summarize later state but may not silently strengthen frozen evidence.

## RIL-001 ceiling

RIL-001 earned one bounded existence witness:

```text
P1-P9              PASS
C_op R0            9,825,003
C_op R1            4,094,613
Lambda_F^op        2.399494897320
memory R0/R1       206,757 / 206,757 bytes
status              REPRESENTATION_INDUCED_LEVERAGE
```

It does not establish family leverage or generality.

## RIL-002 scientific object

RIL-002 is a **family-transfer** assay.

The representation pair is inherited and immutable:

```text
R0 = R0_AST
R1 = R1_SEM8
```

The family-freeze anchor is:

```text
d35d998eea7e9b06ae0516dbcb9019955052ef6f
```

The family is exactly the 24 members in `RIL_002_FAMILY.json`.

Inclusion rule:

```text
K1  in frozen FANOUT_PROGRAMS semantics
K2  not in frozen READ_ONCE_PROGRAMS semantics
K3  x,y,z all essential
K4  exclude RIL-001 target 0x17
```

No member may be added, removed, replaced, or selected based on expected/observed leverage.

## RIL-002 implementation firewall

Do not implement unless explicitly instructed.

If opened, the implementation must:

1. reuse the frozen RIL-001 representation pair without redesign;
2. preserve one shared algorithm for both arms;
3. use the same task split, probe seed, held-out seed, repair cost, horizon, candidate languages, tie-break, precision, authority, and cost regions;
4. instantiate family labels only as `truth_table[4*x + 2*y + z]`;
5. freeze implementation before any RIL-002 leverage result is read;
6. audit source integrity / `A_fixed` / instrumentation before primary execution;
7. execute all 24 members without replacement;
8. adjudicate each `P_i` before interpreting `Lambda_i`;
9. publish the ordered leverage vector and member statuses before any aggregate;
10. stop after the final audit.

Any representation change motivated by this family requires a new assay identifier.

## RIL-002 member adjudication

For every member:

```text
G_i = (A_fixed^(i), P_i, Lambda_i)
```

Preservation is noncompensatory. A cheaper member with `P_i=0` is not leverage.

Inherited member classes:

```text
NOT_EVALUABLE
PRESERVATION_FAILURE
NO_DEMONSTRATED_LEVERAGE
COMPUTE_FOR_MEMORY_TRADEOFF
REPRESENTATION_INDUCED_LEVERAGE
```

Family summaries may not erase these member records.

## Aggregation discipline

The primary object is:

```text
Lambda_vector = (Lambda_1, ..., Lambda_24)
```

Do not replace it by a mean.

Finite-family coverage may be reported descriptively, but:

```text
coverage != population probability
family members != independent statistical samples
RIL-2 transfer != RIL-3 provenance-separated generality
```

## Claim ceiling

Even a family-wide positive result can establish only transfer of this already-selected representation pair across this exact bounded family under the frozen FS007-derived setup.

It cannot establish:

```text
provenance-separated representation-induced generality
resource-boundary amplification
universal affordance geometry
broad constrained-hardware generality
intelligence = representation
```

## Current next legal action

There is no remaining family-selection work under RIL-002.

The next legal scientific event, only if explicitly opened, is implementation against the frozen family.

## Final rule

**Freeze the species before counting the rabbits.**
