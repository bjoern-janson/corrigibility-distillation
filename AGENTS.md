# Research Execution Instructions

## Purpose

Scientific history in this repository is append-only at the level of frozen claims. Later positive results do not rewrite earlier nulls, and later conjectures do not become historical evidence.

## Current lane state

```text
Corpus Distillation  CLOSED
CGP-001              CLOSED / NOT EVALUABLE
RIL-001              CLOSED / REPRESENTATION_INDUCED_LEVERAGE
RIL-002              CLOSED / FAMILY_WIDE_LEVERAGE
RIL-3                NOT OPENED
```

## Immutable scientific records

Treat as frozen records:

```text
CORPUS.md
NECESSITY_AUDIT.md
CGP_001_PREREGISTRATION.md
CGP_001_TRANSLATION_AUDIT.md
experiments/cgp_001/*
RIL_001_PREREGISTRATION.md
RIL_001_PRE_EXECUTION_AUDIT.md
experiments/ril_001/* at implementation freeze a0f8f795...
RIL_001_RESULT.md
RIL_001_RESULT.json
RIL_001_FINAL_AUDIT.md
RIL_002_PREREGISTRATION.md
RIL_002_FAMILY.json
RIL_002_PRE_EXECUTION_AUDIT.md
experiments/ril_002/* at implementation freeze d46dffe2...
RIL_002_RESULT.md
RIL_002_RESULT.json
RIL_002_FINAL_AUDIT.md
```

Mutable narrative files (`README.md`, `STATUS.md`, `ROADMAP.md`, `AGENTS.md`) may summarize later state but may not silently strengthen frozen evidence.

## Evidence distinctions

Preserve:

```text
mechanism != function != invariant
recurrence != necessity
local necessity != universal necessity
same abstract lesson != shared semantic type
serialization compatibility != interface compatibility
possibility != authority
cheapness != semantic preservation
single-function leverage != family transfer
family transfer != provenance-separated generalization
held-out name difference != selection-information separation
resource speedup != resource-boundary amplification
```

On failure or contradiction, revise the shallowest supported layer and preserve unaffected records.

## Closed CGP-001

Do not repair, rerun, score, or reinterpret CGP-001. Its terminal state is:

```text
A_trans          FAIL
failed criteria  [8, 9]
primary arms     NOT RUN
H_CG             NOT TESTED
```

Any repaired cross-mechanism corridor needs a new prospective identifier.

## Closed RIL-001

RIL-001 established one bounded existence witness:

```text
same frozen correction
same algorithm
same scope / authority
R0_AST -> R1_SEM8
C_op 9,825,003 -> 4,094,613
Lambda_F^op = 2.399495
memory non-regression PASS
```

Do not optimize or rerun the frozen apparatus under `RIL-001`.

## Closed RIL-002

RIL-002 tested **transfer**, not new representation design. It inherited the exact RIL-001 pair and froze an exhaustive 24-member family before any new leverage results.

Terminal result:

```text
P_i                              PASS 24/24
A_fixed dynamic equality         PASS 24/24
Lambda_i^op > 1                  PASS 24/24
memory non-regression            PASS 24/24
held-out transfer = 1.0          PASS 24/24
family status                    FAMILY_WIDE_LEVERAGE
kappa_F^op                       1.0
full_RIL_coverage                1.0
```

The claim ceiling is bounded family transfer. Do not relabel it as `representation-induced generality` or `RIL-3`.

No member may be removed after the fact and no new member may be added to strengthen or weaken the closed RIL-002 claim.

## RIL-3 is not opened

A future provenance-separated generalization experiment must receive a new prospective identifier and freeze an information firewall before any held-out result.

At minimum it must define:

```text
I_select(R)     all information allowed to influence representation selection/construction
I_test          held-out correction information
selection rule  g such that R = g(I_select)
freeze point    R becomes immutable before I_test is revealed to the selection process
F_train / F_test or equivalent test objects
preservation predicate per test object
cost / memory accounting
null and terminal taxonomy
claim ceiling
```

The intended firewall is stronger than different function names:

```text
I_select(R) ∩ I_test = empty
```

or an operationally equivalent causal/provenance separation established prospectively.

Do not use RIL-002 member outcomes to redesign a representation and then call the same family held out.

## Larger roadmap

RIL-4 and RIL-5 remain conjectural. Objects such as:

```text
A(R) = (Omega_R, tau_R, c_R, C_R)
Omega_eff(R;B)
representation payback horizon n*
```

are research notation, not established universal theory.

## No currently authorized experiment

There is no automatically authorized `RIL-3`, `RIL-003`, `CGP-002`, resource-boundary assay, or theory-expansion task. New work begins only by explicit prospective instruction.

## Final rule

**Change the coordinates only when the experiment says coordinates may change. Hold the scientific object fixed. Count every cost. Preserve every null. Never promote transfer into generalization without a provenance firewall.**
