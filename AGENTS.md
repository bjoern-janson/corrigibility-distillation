# Research Execution Instructions

## Purpose

This repository preserves one closed corpus-distillation program and two downstream prospective experimental lanes.

Scientific history must remain append-only at the level of frozen claims. Do not rewrite a frozen artifact merely because a later experiment changes the surrounding interpretation.

## Current lane state

### Corpus Distillation

```text
CLOSED
```

Frozen summary:

```text
Phase 1 inventory                        COMPLETE
Phase 2 substitutability                 0/182
L4 full mechanism interfaces             0
L4' bounded evidence/provenance handoff  1
local necessity                          3 NECESSARY
                                         5 NOT DEMONSTRATED
                                         1 DISCONFIRMED
necessity relations                      0 DEPENDENT
                                         0 INDEPENDENT
                                         2 NOT COMPARABLE
                                         1 NOT DEMONSTRATED
common core                              NOT EARNED
minimization                             CLOSED
L5 / L6                                  CLOSED
```

Do not reopen the corpus lane unless explicitly instructed to create new evidence. New downstream experiments never alter historical L3/L4/L5/L6 counts.

### CGP-001

```text
CLOSED / NOT EVALUABLE
```

Frozen terminal state:

```text
A_trans              FAIL
failed criteria      [8, 9]
primary execution    NOT AUTHORIZED / NOT RUN
L0-L3                 NOT REACHED
H_CG                  NOT TESTED
```

Do not repair, rerun, reinterpret, or score CGP-001. Any repaired corridor requires a new prospective identifier such as `CGP-002`.

The recovered apparatus under `experiments/cgp_001/` is historical apparatus, not an invitation to run the primary arms.

### RIL-001

```text
PREREGISTERED / NOT IMPLEMENTED / NOT EXECUTED
```

Frozen preregistration:

```text
RIL_001_PREREGISTRATION.md
anchor = 204fe919159145ac9c29f1becfb92b0c511af02b
```

Do not change its scientific content.

## Frozen artifacts

Treat the following as scientific records, not editable design drafts:

```text
CORPUS.md
NECESSITY_AUDIT.md
CGP_001_PREREGISTRATION.md
CGP_001_TRANSLATION_AUDIT.md
experiments/cgp_001/*
RIL_001_PREREGISTRATION.md
```

`README.md`, `STATUS.md`, `ROADMAP.md`, `AGENTS.md`, and provenance notes may be updated to reflect later state, but may not contradict or silently strengthen frozen evidence.

## Governing evidence rules

Preserve these distinctions:

```text
mechanism != function != invariant
recurrence != necessity
local necessity != universal necessity
same abstract lesson != shared semantic type
serialization compatibility != interface compatibility
candidate != oracle != evaluator
possibility != authority
search allocation != repair/adoption authority
adapter correctness != evidence for the predicted corridor
cheapness != semantic preservation
formal possibility != empirical leverage
```

On contradiction or failure:

1. generate competing explanations;
2. discriminate with independent evidence where possible;
3. revise only the shallowest supported layer;
4. preserve unaffected frozen structure;
5. retest only under a new authorized prospective object when the old protocol forbids repair;
6. keep nulls and `NOT EVALUABLE` outcomes visible.

## RIL-001 scientific object

The sole question is:

> Can changing only the operative representation reduce computational cost for one already-demonstrated FS007 corrective transformation while preserving transformation identity, scope, authority, and required operations?

Frozen intervention:

```text
A                  fixed
F                  fixed
D                  fixed
Omega_req          fixed
authority ceiling  fixed
R                  varied
```

Representations:

```text
R0_AST
    parent canonical Program AST
    prediction = program.evaluate_local((x,y,z))

R1_SEM8
    parent exact 8-pattern semantic tuple
    prediction = semantic_tuple[4*x + 2*y + z]
```

Do not add target-dependent caches, JITs, vectorization, pruning, candidate reordering, different precision, altered candidate sets, unequal batching, or representation-specific search logic.

## RIL-001 implementation sequence

Do not begin implementation unless explicitly instructed.

Once opened, follow exactly:

```text
1. verify frozen parent source / constants
2. implement one shared algorithm with representation-specific prediction only
3. freeze implementation before reading the primary leverage verdict
4. establish A_fixed / instrumentation validity
5. run preservation predicate P
6. if P fails -> DISQUALIFIED_PRESERVATION_FAILURE -> STOP
7. if A_fixed/instrumentation fails -> NOT_EVALUABLE -> STOP
8. only after gates pass, reveal and score frozen primary cost
9. write RIL_001_RESULT.md
10. write independent RIL_001_AUDIT.md
11. STOP
```

No observed result may motivate a scientific change inside `RIL-001`; use `RIL-002` for repairs or extensions.

## RIL-001 preservation gate

All preregistered preservation items are noncompensatory.

At minimum verify exact identity of:

```text
M0/M1 candidate sets and order
candidate semantics on all 8 local patterns
per-candidate probe scores
M0/M1 winners and canonical identity
gain / estimated value / repair decision
fanout_enabled state
selected semantic function
held-out predictions and aggregate transfer
D / seeds / precision / criteria
goal and authority flags
required-operation coverage
```

A cheaper arm with `P=0` is not partial leverage.

## RIL-001 cost interpretation

Primary computational cost is the preregistered opcode accounting, including applicable representation construction/translation overhead.

Do not hide work in setup, preprocessing, caching, translation, or shared state.

Memory is a co-primary non-regression gate. Wall-clock timing is confirmatory only.

Terminal classes are exactly:

```text
NOT_EVALUABLE
DISQUALIFIED_PRESERVATION_FAILURE
NO_DEMONSTRATED_LEVERAGE
COMPUTE_FOR_MEMORY_TRADEOFF
REPRESENTATION_INDUCED_LEVERAGE
```

Do not invent an intermediate positive class after seeing results.

## Larger RIL roadmap

`ROADMAP.md` contains conjectural future rungs:

```text
RIL-1 single earned function
RIL-2 function family
RIL-3 held-out functions
RIL-4 resource-boundary amplification
RIL-5 broad effective generality on constrained substrate
```

Only RIL-1 currently has a preregistered assay.

Objects such as:

```text
A(R) = (Omega_R, tau_R, c_R, C_R)
Omega_eff(R;B)
representation payback horizon n*
```

are candidate notation / roadmap concepts. They are not earned theory and must not be cited as a result of the closed corpus, CGP-001, or an unexecuted RIL-001.

## Claim ceiling

A positive RIL-001 result can establish only a bounded statement of this form:

> Under the exact frozen FS007 condition and cost model, `R1_SEM8` realizes the same preregistered corrective transformation with lower measured computational work than `R0_AST` while satisfying the frozen preservation and memory gates.

It cannot establish:

```text
representation-induced generality
resource-boundary amplification
universal affordance geometry
intelligence = representation
common corrigibility architecture
general hardware-capability amplification
```

Those require separate prospective evidence.

## Final rule

**Change the coordinates. Hold the correction fixed. Count every cost. Preserve every null.**
