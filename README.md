# Corrigibility Distillation

A provenance-preserving research repository for extracting bounded claims about corrective systems, preserving nulls, and opening new experiments only after the prior evidence ceiling has been frozen.

## Current state

| Lane | Status | Strongest earned result |
|---|---|---|
| Corpus Distillation | **CLOSED** | Recurring corrective constraints and three local necessities; no common reducible core, substitutability, or full cross-repository mechanism interface was demonstrated. |
| CGP-001 | **CLOSED / NOT EVALUABLE** | The attempted NSS→FS corridor failed before composition because the bridge was not semantically well-typed. `H_CG` was not tested. |
| RIL-001 | **CLOSED / REPRESENTATION_INDUCED_LEVERAGE** | For one frozen FS007 correction, AST→SEM8 reduced counted computational work while preserving semantic identity, scope, authority, required operations, and memory. |
| RIL-002 | **CLOSED / FAMILY_WIDE_LEVERAGE** | The unchanged RIL-001 representation pair transferred full leverage across every member of a prospectively frozen 24-member family. |
| RIL-3 | **NOT OPENED** | Provenance-separated generalization remains untested. |

See [`STATUS.md`](STATUS.md) for the exact ledger, [`ROADMAP.md`](ROADMAP.md) for unearned future rungs, and [`AGENTS.md`](AGENTS.md) for execution discipline.

## Frozen corpus result

The canonical 14-repository boundary is [`CORPUS.md`](CORPUS.md). The closed distillation lane established:

```text
Phase 1 inventory                 COMPLETE
Phase 2 substitutability          0 / 182 YES or PARTIAL
L4 full mechanism interfaces      0
L4' bounded evidence transport    1
local necessity                   3 NECESSARY
                                  5 NOT DEMONSTRATED
                                  1 DISCONFIRMED
necessity relations               0 DEPENDENT
                                  0 INDEPENDENT
                                  2 NOT COMPARABLE
                                  1 NOT DEMONSTRATED
common reducible core             NOT EARNED
global minimization               CLOSED
L5 / L6                           CLOSED
```

Nothing downstream rewrites this record.

## CGP-001 — pre-composition null

CGP-001 attempted a prospective NSS→FS corridor. The independent translation audit found:

```text
A_trans = FAIL
failed criteria = [8, 9]
CGP-001 = NOT EVALUABLE
primary arms = NOT RUN
H_CG = NOT TESTED
```

The two failures were semantic-role mismatch and search-scope mismatch. The attempted corridor was never faithfully constituted. See [`CGP_001_PREREGISTRATION.md`](CGP_001_PREREGISTRATION.md) and [`CGP_001_TRANSLATION_AUDIT.md`](CGP_001_TRANSLATION_AUDIT.md).

## RIL-001 — single-function leverage

RIL-001 held fixed the correction, algorithm, scope, required operations, and authority while varying only representation:

```text
R0 = canonical Program AST
R1 = existing exact 8-pattern semantic tuple (SEM8)
```

All preservation gates passed. Counted work fell from `9,825,003` to `4,094,613` instruction events:

```text
Lambda_F^op = 2.399495
```

with equal search/update work and no peak-memory increase. See [`RIL_001_RESULT.md`](RIL_001_RESULT.md).

## RIL-002 — family transfer

RIL-002 did **not** redesign the representation. It inherited the exact RIL-001 AST/SEM8 pair and prospectively froze the family before any new leverage results.

The inclusion rule selected every full-support 3-input Boolean target that:

```text
is exactly representable in frozen M1/fanout
is not exactly representable in frozen M0/read-once
uses x, y, and z essentially
is not the RIL-001 majority target
```

This yields exactly 24 members. See [`RIL_002_PREREGISTRATION.md`](RIL_002_PREREGISTRATION.md) and [`RIL_002_FAMILY.json`](RIL_002_FAMILY.json).

Terminal result:

```text
P_i                                  PASS 24/24
A_fixed dynamic equality             PASS 24/24
Lambda_i^op > 1                      PASS 24/24
memory non-regression                PASS 24/24
held-out transfer accuracy = 1.0     PASS 24/24
family status                        FAMILY_WIDE_LEVERAGE
kappa_F^op                           1.0
full_RIL_coverage                    1.0
Lambda range                         2.376157 .. 2.393112
```

See [`RIL_002_RESULT.md`](RIL_002_RESULT.md) and [`RIL_002_FINAL_AUDIT.md`](RIL_002_FINAL_AUDIT.md).

The earned claim is **bounded family transfer of representation-induced computational leverage**. It is not provenance-separated generalization.

## Current empirical separation

The downstream assays now supply one bounded example on each side of an important distinction:

```text
Constraint / existence question:
    can the proposed transformation be constituted with valid semantic typing?
    CGP-001: attempted corridor failed here.

Affordance / cost question:
    once a transformation is already valid, can representation change its cost?
    RIL-001: yes for one function.
    RIL-002: yes across the frozen related family.
```

This is an empirical program structure, not a universal theory.

## Claim ceiling

RIL-002 does **not** establish:

```text
provenance-separated representation-induced generalization
resource-boundary amplification
broad effective generality on constrained hardware
universal affordance geometry
intelligence = representation
a common corrigibility architecture
```

Those require new prospective experiments.

## Repository map

```text
CORPUS.md                         frozen corpus boundary
NECESSITY_AUDIT.md                frozen local-necessity record
CGP_001_*                         closed CGP-001 preregistration/null/provenance
RIL_001_PREREGISTRATION.md        frozen single-function contract
RIL_001_PRE_EXECUTION_AUDIT.md    frozen pre-cost audit
RIL_001_RESULT.*                  terminal RIL-001 result
RIL_001_FINAL_AUDIT.md            terminal RIL-001 audit
RIL_002_PREREGISTRATION.md        frozen family-transfer contract
RIL_002_FAMILY.json               frozen 24-member family
RIL_002_PRE_EXECUTION_AUDIT.md    frozen pre-execution audit
RIL_002_RESULT.*                  terminal family-transfer result
RIL_002_FINAL_AUDIT.md            terminal RIL-002 audit
experiments/                      frozen apparatus
STATUS.md                         mutable current ledger
ROADMAP.md                        conjectural future ladder
AGENTS.md                         execution rules
```

## Governing rule

> **Preserve the scientific identity of the transformation before claiming anything about making it cheaper. Preserve every null and every claim ceiling.**
