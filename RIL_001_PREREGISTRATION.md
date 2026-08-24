# RIL-001 — Representation-Induced Leverage Preregistration

Status: **PROSPECTIVE; SCIENTIFIC CONTENT FROZEN BY THE FIRST COMMIT THAT ADDS THIS FILE**

This file opens a new evidence-generating lane. It does not reopen the frozen corpus-distillation lane, does not reinterpret CGP-001, and does not promote the Quake analogy, constraint geometry, affordance geometry, or `A(R)` into an earned theory.

At freeze time no RIL-001 implementation, benchmark result, cost trace, timing result, preservation verdict, or scientific outcome exists. The commit that first adds this file is the preregistration anchor. Any scientifically meaningful change after seeing a primary RIL-001 cost result requires a new assay identifier.

## 1. Sole question and hypothesis

RIL-001 asks:

> **Can changing only the operative representation reduce the computational cost of one already-demonstrated corrective transformation while preserving what that transformation means, its scope, its authority ceiling, and every required operation?**

The general motivating object is only a candidate notation:

\[
\mathcal A(R)=(\Omega_R,\tau_R,c_R,\mathcal C_R).
\]

RIL-001 does not test that general object. It tests one bounded instance.

For the frozen RIL-001 instance:

\[
H_{\rm RIL001}: P(F,D,R_0,R_1)=1 \land C^{\rm op}_{R_1}(F)<C^{\rm op}_{R_0}(F).
\]

The matched null is:

\[
H_0: P(F,D,R_0,R_1)=1 \land C^{\rm op}_{R_1}(F)\ge C^{\rm op}_{R_0}(F).
\]

If the fixed-algorithm gate fails, the assay is `NOT_EVALUABLE`. If preservation fails, the attempted representation change is `DISQUALIFIED_PRESERVATION_FAILURE`; that is not evidence for `H_0` because the two arms no longer realize the same corrective transformation.

The strongest possible positive conclusion is only:

> **Under the exact frozen FS007 condition and cost model, the semantic-table representation realizes the same corrective transformation with lower measured computational work than the AST representation without increasing the frozen memory cost.**

Nothing universal about corrigibility, learning, representation, or affordance geometry follows from one positive assay.

## 2. Frozen parent and source authority

The single scientific parent is Future Sufficiency Experiment 007.

- Repository: `bjoern-janson/future-sufficiency`
- Commit: `2f4ca824e02b89df0c23d64de312c4f93a4c8a41`
- Python source: `experiments/meta_language_repair.py`
- Git blob: `f74d85f5f9d0c7842dc50e34ae2718699108fff6`
- Method description: `experiments/meta_language_repair.md`
- Git blob: `9ac2883c797e99af27fd092b262f5cb6ce8ece70`

The parent implementation already constructs:

```text
READ_ONCE_PROGRAMS : semantic tuple -> canonical Program AST
FANOUT_PROGRAMS    : semantic tuple -> canonical Program AST
```

where each semantic tuple is the exact output of the canonical program over all eight `LOCAL_PATTERNS`. RIL-001 therefore does not invent a target-specific cache or a new semantic representation after seeing task labels. Both candidate coordinate systems are already present in the frozen parent object.

The frozen parent claim remains local: Experiment 007 demonstrates a bounded, cost-sensitive `read_once -> fanout_allowed` representation-generator repair and held-out reuse in its finite supplied Boolean setting. RIL-001 tests only the cost of realizing one already-demonstrated positive condition.

## 3. Frozen corrective function `F`

The tested corrective transformation is exactly the mutable learner path of FS007 for the low-cost insufficient condition:

```text
NEEDS_FANOUT probe examples
-> exhaustive M0/read-once search
-> exhaustive M1/fanout search
-> gain = max(0, a1 - a0)
-> estimated_repair_value = FUTURE_HORIZON * gain
-> compare estimated_repair_value > LOW_REPAIR_COST
-> persist fanout_allowed when warranted
-> select the same canonical best program
-> evaluate the selected result on the held-out test split
```

The scientific identity of `F` includes all of the following:

1. the exact M0 and M1 semantic candidate sets;
2. exhaustive candidate evaluation rather than pruning or heuristic search;
3. the frozen accuracy objective;
4. the frozen canonical tie-break inherited from `preferable(program, other)`;
5. the exact `max(0, a1-a0)` gain rule;
6. the exact future-value formula;
7. the strict `estimated_repair_value > repair_cost` adoption rule;
8. the `fanout_enabled` persistent generator-state update;
9. the selected program's semantic identity and canonical identity;
10. held-out evaluation on the frozen test-task construction;
11. `goal_rule_mutated = false` and `authority_expanded = false`.

RIL-001 does not test the fixed-meta-language control and does not test the later XOR reuse rung. Those are outside this assay so that only one already-earned corrective transformation is costed.

## 4. Frozen conditions `D`

The condition is exactly:

```text
family                 = Family.NEEDS_FANOUT
repair_cost            = LOW_REPAIR_COST = 5.0
future_horizon          = FUTURE_HORIZON = 100
N_BITS                  = 18
TRAIN_TASKS             = 50
TEST_TASKS              = 25
PROBE_PATTERNS_PER_TASK = 4
HELDOUT_EXAMPLES        = 3000
MAX_FANOUT_NODES        = 9
task_split_seed         = 7
probe_seed              = 17
heldout_seed            = 31
```

The local truth-table domain remains exactly the eight 3-bit `LOCAL_PATTERNS` in parent order.

The reference arm must reproduce the parent structural invariants before the leverage comparison is evaluable:

```text
len(READ_ONCE_PROGRAMS) = 94
len(FANOUT_PROGRAMS)    = 127
exact M0 majority ceiling = 0.875
exact M1 majority ceiling = 1.0
```

It must also reproduce the parent's positive low-cost repair behavior on the frozen condition. A source mismatch, count mismatch, ceiling mismatch, failed repair, or failed held-out positive-control check makes RIL-001 `NOT_EVALUABLE`; no fallback implementation is allowed.

No task, label, cost, horizon, candidate, semantic tuple, seed, held-out set, authority rule, or success criterion may differ by arm.

## 5. Required operation signature `Omega_req`

Both representations must support the same required operations:

```text
O1  enumerate every M0 candidate exactly once per exhaustive pass
O2  enumerate every M1 candidate exactly once per exhaustive pass
O3  evaluate a candidate on any of the eight local input patterns
O4  score exact empirical accuracy on the frozen probe examples
O5  compare candidate accuracies
O6  apply the frozen canonical size/string tie-break
O7  expose the same selected candidate semantic function
O8  compute gain and estimated repair value
O9  apply the strict repair-cost decision
O10 persist/read fanout_enabled
O11 evaluate the selected candidate on held-out examples
O12 expose the same goal/authority boundary flags
```

RIL-001 earns no claim about operations outside this exact signature.

## 6. Frozen representations

### 6.1 `R0_AST` — canonical program-tree representation

`R0_AST` uses the canonical `Program` object stored as the value of each frozen parent dictionary entry.

Candidate prediction is exactly the parent operation:

```python
program.evaluate_local((x, y, z))
```

No AST simplification, compilation, memoization, bytecode generation, vectorization, JIT, or target-specific cache is allowed.

### 6.2 `R1_SEM8` — exact semantic-table representation

`R1_SEM8` uses the already-present dictionary key for the same parent entry: the exact eight-output semantic tuple produced by the frozen parent `semantics(program)` function.

For parent `LOCAL_PATTERNS = product((0,1), repeat=3)`, the index of `(x,y,z)` is fixed as:

```text
index = 4*x + 2*y + z
```

Candidate prediction is:

```python
semantic_tuple[index]
```

`R1_SEM8` may not call `target`, inspect `Family`, inspect `hidden` outside the shared scorer, inspect repair cost or horizon during representation construction, or build any task-specific table. It may consume only semantic keys already present in the frozen parent dictionaries plus shared candidate-identity metadata.

### 6.3 Shared identity sidecar

Canonical identity is not allowed to change with representation. A shared read-only manifest supplies, for every parent entry:

```text
candidate_id
canonical size = program.size()
canonical name = str(program)
parent insertion index
```

The sidecar is identical in both arms and is used only for identity, order checking, and the frozen tie-break. It may not contain task labels, accuracies, repair values, or results.

The one-to-one experimental candidate unit is therefore:

```text
same candidate_id
+ same canonical metadata
+ R0 payload = Program AST
or
+ R1 payload = existing semantic tuple
```

## 7. Fixed algorithm gate `A_fixed`

Representation is the only permitted intervention.

The implementation must expose one shared exhaustive-search/control-flow procedure used by both arms. The arm parameter may select only the representation-specific prediction primitive described in section 6.

The following must be identical across arms:

- candidate manifests and candidate order;
- probe and held-out example order;
- number of M0 candidate visits;
- number of M1 candidate visits;
- number of candidate/example score comparisons;
- accuracy accumulation logic;
- tie-break logic;
- gain and value calculations;
- repair threshold;
- state-update code;
- held-out evaluation loop;
- result serialization.

Forbidden arm-specific changes include:

```text
pruning
short-circuit search
candidate reordering
batching available only to one arm
vectorization available only to one arm
parallelism
memoization created from probe or held-out data
early stopping
changed precision
changed candidate language
changed search budget
changed adoption rule
changed authority rule
```

A static diff/audit of the frozen implementation must establish that the only scientific branch is `R0_AST` versus `R1_SEM8` candidate prediction and representation construction. If `A_fixed` cannot be established, RIL-001 is `NOT_EVALUABLE` and no leverage verdict is permitted.

## 8. Preservation predicate `P`

`P(F,D,R0,R1)=1` only if every item below passes exactly.

### P1 — Candidate-set identity

M0 and M1 candidate IDs are bijective across arms with exact counts `94` and `127` and no added, removed, duplicated, or reordered scientific candidate.

### P2 — Exhaustive semantic equivalence

For every candidate in both languages and every one of the eight local patterns:

```text
predict_R0(candidate, pattern) == predict_R1(candidate, pattern)
```

This comparison is frozen before the primary cost verdict is read.

### P3 — Per-candidate scoring identity

On the frozen probe set, every candidate's empirical accuracy must match exactly across representations.

### P4 — Search-result identity

The best M0 and M1 candidates must have identical empirical accuracy, semantic tuple, canonical size, and canonical name across arms.

### P5 — Repair-decision identity

The arms must produce exactly the same:

```text
base accuracy
fanout accuracy
gain
estimated_repair_value
repair decision
fanout_enabled state
selected semantic function
selected canonical program identity
construction_rule_after
```

### P6 — Held-out identity

Every held-out prediction and the aggregate held-out transfer accuracy must match exactly across arms.

### P7 — Scope identity

All frozen `D` values, candidate languages, examples, seeds, precision, and evaluation criteria must be byte-for-byte or value-for-value identical as applicable.

### P8 — Authority identity

Both arms must preserve:

```text
goal_rule_mutated = false
authority_expanded = false
```

Neither representation receives any new action, objective, goal, or evaluator authority.

### P9 — Required-operation coverage

Every operation in `Omega_req` must be executable under `R1_SEM8` with the same scientific semantics as under `R0_AST`.

If any preservation item fails, the terminal status is:

```text
DISQUALIFIED_PRESERVATION_FAILURE
```

A cheaper non-preserving arm receives no partial leverage credit.

## 9. Frozen cost vector

RIL-001 instantiates computational cost as:

\[
c_R(F)=
(c_{\rm translation}^{op},
 c_{\rm eval}^{op},
 c_{\rm search}^{op},
 c_{\rm update}^{op},
 c_{\rm memory},
 c_{\rm wall}).
\]

All cost components are measured on the same frozen condition.

### 9.1 Deterministic opcode accounting — primary

The primary computational unit is a CPython opcode event under one exact Python interpreter build recorded in the execution manifest.

Opcode tracing is performed in a dedicated non-timing run using Python opcode tracing. The tracing harness itself is excluded. Regions are frozen as:

- `c_translation^op`: construction of the arm-specific candidate views from the already-imported frozen parent dictionaries;
- `c_eval^op`: only representation-specific candidate prediction during all M0/M1 probe scoring and selected-candidate held-out prediction;
- `c_search^op`: shared exhaustive-search bookkeeping outside the representation-specific prediction primitive;
- `c_update^op`: shared gain/value/adoption/state-update logic.

The primary scalar computational cost is:

\[
C_R^{op}=c_{translation}^{op}+c_{eval}^{op}+c_{search}^{op}+c_{update}^{op}.
\]

The preregistered leverage ratio is:

\[
\Lambda_F^{op}(R_0\to R_1)=
\frac{C_{R_0}^{op}(F)}{C_{R_1}^{op}(F)}.
\]

A positive computational-leverage result requires strictly `Lambda_F^op > 1` after all preservation gates pass.

`c_search^op` and `c_update^op` must be exactly equal across arms. If they differ, `A_fixed` fails and the assay is `NOT_EVALUABLE` rather than a leverage result.

### 9.2 Memory — co-primary non-regression gate

`c_memory` is peak incremental traced memory, in bytes, from immediately after frozen parent import and dataset construction through arm-view construction and completion of `F`, measured in fresh processes using the same Python build.

The already-imported parent dictionaries are common baseline state and are not subtracted differently by arm. Arm-specific view construction must be symmetric except for payload reference (`Program` value versus semantic-tuple key).

A full RIL-001 positive requires:

```text
c_memory(R1_SEM8) <= c_memory(R0_AST)
```

If semantic preservation passes and opcode cost falls but this memory gate fails, the terminal status is:

```text
COMPUTE_FOR_MEMORY_TRADEOFF
```

That is not promoted to `REPRESENTATION_INDUCED_LEVERAGE` in RIL-001.

### 9.3 Wall-clock time — confirmatory only

`c_wall` is measured only in separate untraced timing runs after implementation freeze. Both arms run in fresh processes on the same machine/interpreter build. Run order is alternated deterministically and the execution manifest records CPU, OS, Python build, power/performance mode when observable, process-affinity policy, warm-up policy, and repetition count.

Wall time cannot rescue a failed opcode or preservation result and cannot by itself earn leverage. It is reported only as a confirmatory implementation-level consequence.

## 10. Representation-construction firewall

Representation construction is part of the experiment and part of cost.

RIL-001 specifically forbids the common shortcut:

```text
precompute target-specific answers for R1
then call the lookup cost the representation cost
```

The only R1 semantic table allowed is the exact semantic key already created by the frozen parent candidate-library construction before task-specific scoring. No additional semantic-table generation from probe or held-out examples is permitted.

Both arms construct experimental candidate views after the parent libraries already exist. `c_translation^op` for both arms is counted from that common boundary.

## 11. Execution sequence and leakage firewall

The mandatory sequence is:

```text
RIL_001_PREREGISTRATION.md
-> FREEZE
-> implementation + unit/identity tests
-> FREEZE IMPLEMENTATION
-> A_fixed/source/instrumentation audit
-> if audit fails: NOT_EVALUABLE -> STOP
-> primary R0/R1 execution
-> preservation gate P
-> cost verdict
-> result artifact
-> STOP
```

Before the implementation freeze, developers may run tests needed to verify source loading, candidate identity, all-eight-pattern semantic equivalence, fail-closed behavior, and instrumentation mechanics. They may not run the frozen primary condition through both costed arms, inspect `Lambda_F^op`, compare primary wall times, or tune representation code using primary cost results.

After any primary cost result is observed, no change to representation construction, evaluator code, cost boundaries, counters, source pins, candidate order, datasets, or scoring may be made under RIL-001. A repair or optimization becomes a new assay.

No result artifact may silently rewrite this preregistration.

## 12. Terminal taxonomy

Use exactly one terminal scientific status:

### `NOT_EVALUABLE`

Use when the frozen parent cannot be reproduced, source integrity fails, `A_fixed` fails, opcode/memory instrumentation is invalid, or the intended representation intervention cannot be isolated.

### `DISQUALIFIED_PRESERVATION_FAILURE`

Use when `A_fixed` passes but any item in `P` fails. No cost comparison is interpreted as leverage.

### `NO_DEMONSTRATED_LEVERAGE`

Use only when `P=1`, memory does not increase, and:

```text
C_op(R1) >= C_op(R0)
```

### `COMPUTE_FOR_MEMORY_TRADEOFF`

Use only when `P=1` and:

```text
C_op(R1) < C_op(R0)
c_memory(R1) > c_memory(R0)
```

This is evidence of a resource tradeoff, not the full RIL-001 target.

### `REPRESENTATION_INDUCED_LEVERAGE`

Use only when:

```text
A_fixed = PASS
P = 1
C_op(R1) < C_op(R0)
c_memory(R1) <= c_memory(R0)
```

Then report `Lambda_F^op` plus the complete cost vector. Wall-clock timing remains confirmatory.

## 13. Claim ceiling

Even a positive result establishes only a bounded existence witness:

\[
\exists (F,D,R_0,R_1):
P=1 \land C^{op}_{R_1}(F)<C^{op}_{R_0}(F)
\]

for this exact FS007 function, condition, candidate languages, Python implementation, and representation pair.

It does **not** establish:

- a universal affordance geometry;
- that representations generally contain algorithms;
- that correction is always representation-relative;
- that semantic-table representations are globally superior;
- that compute/memory tradeoffs disappear outside this condition;
- that the Quake inverse-square-root example and FS007 instantiate one mechanism;
- that CGP, SRE, Future Sufficiency, or Corrigible Compression reduce to one theory;
- that a common corrigibility architecture has been found;
- any reopening of corpus distillation or global minimization.

## 14. Governing rule

\[
\boxed{
\textbf{Change the coordinates. Hold the correction fixed. Count every cost.}
}
\]

If the cheaper representation stops doing the same correction, it is not leverage.
