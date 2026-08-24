# RIL-002 — Family-Transfer Preregistration

Status: **PROSPECTIVE FAMILY FROZEN; NO RIL-002 LEVERAGE MEASUREMENT MAY PRECEDE THIS FILE'S FIRST COMMIT**

Rung: **RIL-2 — family transfer**

Parent positive result: `RIL-001 = REPRESENTATION_INDUCED_LEVERAGE`, terminal commit `a8dfb2aa7e72b5f28c497bbe071408c9be0113a3`.

RIL-002 is not a repetition of RIL-001 and is not a test of provenance-separated generalization. It asks whether the **same representation pair already frozen by RIL-001** transfers its leverage across a prospectively defined, exhaustive bounded family of related corrective targets.

Nothing in RIL-002 may rewrite the closed corpus, CGP-001, or RIL-001.

## 1. Sole question and claim ceiling

RIL-002 asks:

> **Does the already-frozen `R1_SEM8` representation preserve and reduce the counted cost of the same low-cost read-once → fanout correction procedure across every member of a prospectively frozen family of full-support fanout-needed Boolean targets?**

Representations are inherited literally:

```text
R0 = R0_AST
R1 = R1_SEM8
```

No new representation engineering, target-specific cache, vectorization, compilation, JIT, pruning, candidate reordering, or representation-specific search logic is permitted.

The strongest possible RIL-002 claim is bounded family transfer:

> **The frozen RIL-001 representation pair exhibited a specified leverage profile across the exact frozen RIL-002 family under the inherited correction, scope, authority, cost accounting, and preservation rules.**

RIL-002 cannot establish provenance-separated generalization, resource-boundary amplification, broad effective generality, or a universal affordance geometry.

## 2. Frozen scientific parents

### 2.1 RIL-001

```text
preregistration       204fe919159145ac9c29f1becfb92b0c511af02b
implementation freeze a0f8f795a805e8f579fd608fbcaa83dcfa6ef60f
pre-execution audit   6b3b865f3fce07fe835e169d80ec8f72f192f4bf
terminal result       a8dfb2aa7e72b5f28c497bbe071408c9be0113a3
```

RIL-001 established one bounded existence witness. Its representation pair is treated as fixed prior apparatus, not redesigned for RIL-002.

### 2.2 Future Sufficiency Experiment 007

```text
repository  bjoern-janson/future-sufficiency
commit      2f4ca824e02b89df0c23d64de312c4f93a4c8a41
source      experiments/meta_language_repair.py
blob        f74d85f5f9d0c7842dc50e34ae2718699108fff6
```

The parent objects used to define the family are exactly:

```text
LOCAL_PATTERNS
READ_ONCE_PROGRAMS
FANOUT_PROGRAMS
MAX_FANOUT_NODES = 9
```

No RIL-002 cost result participates in family selection.

## 3. Family-inclusion rule `K`

Let `f` be an 8-bit Boolean truth table over the frozen `LOCAL_PATTERNS` order:

```text
000, 001, 010, 011, 100, 101, 110, 111
```

The first truth-table output is the most-significant bit of the stable hexadecimal member ID.

Define variable `v in {x,y,z}` to be **essential** for `f` iff there exists a pair of local patterns differing only in `v` on which `f` differs.

A truth table is in the RIL-002 family iff all four conditions hold:

```text
K1  f is a semantic key of frozen FANOUT_PROGRAMS.
K2  f is not a semantic key of frozen READ_ONCE_PROGRAMS.
K3  x, y, and z are all essential for f.
K4  f is not the RIL-001 NEEDS_FANOUT majority target.
```

Formally:

\[
K(f)=
[f\in\mathrm{keys}(M1)]
\land
[f\notin\mathrm{keys}(M0)]
\land
[\mathrm{Ess}(f)=\{x,y,z\}]
\land
[f\neq f_{\mathrm{RIL001}}].
\]

The excluded RIL-001 target is:

```text
truth table  00010111
hex          0x17
```

`K` was fixed before any RIL-002 R0/R1 leverage execution.

## 4. Frozen family `F`

Applying `K` exhaustively to the frozen parent semantic libraries yields exactly **24 members**.

The authoritative machine-readable family is:

```text
RIL_002_FAMILY.json
```

The canonical JSON SHA-256 of its `members` array is:

```text
d51b9b51e37f82a316dfcbd1461b766b52f34941283d1af3d1189c2546b472b1
```

No member may be added, removed, substituted, grouped away, or renamed after leverage results are observed under RIL-002.

The stable member IDs are the truth-table hexadecimal codes:

```text
TT_1B TT_1D TT_27 TT_2E TT_35 TT_3A
TT_47 TT_4E TT_53 TT_5C TT_72 TT_74
TT_8B TT_8D TT_A3 TT_AC TT_B1 TT_B8
TT_C5 TT_CA TT_D1 TT_D8 TT_E2 TT_E4
```

A derived property of the complete frozen family — **not an additional selection filter** — is:

```text
exact M0/read-once ceiling = 0.875 for every member
exact M1/fanout ceiling    = 1.000 for every member
```

Thus every member occupies the same exact representational-gap class as the RIL-001 majority target while being a different target function.

The family is exhaustive under `K`; it is not a random sample and its members must not be treated as independent statistical draws.

## 5. Frozen correction and conditions

For each `F_i`, the correction procedure remains the RIL-001 low-cost FS007 path:

```text
target-labelled probe examples
-> exhaustive M0/read-once search
-> exhaustive M1/fanout search
-> gain = max(0, a1-a0)
-> estimated_repair_value = FUTURE_HORIZON * gain
-> strict estimated_repair_value > LOW_REPAIR_COST
-> persist fanout_allowed when warranted
-> select the same canonical winner under the frozen tie-break
-> evaluate on the frozen held-out construction
```

All members use the inherited constants and seeds unless a later implementation audit shows literal reuse is impossible, in which case RIL-002 is `NOT_EVALUABLE` rather than repaired:

```text
repair_cost            = 5.0
future_horizon          = 100
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

For a family member with truth table `t`, the shared target operation is exactly:

```text
(x,y,z) -> t[4*x + 2*y + z]
```

This target lookup is shared by both representation arms and is not part of the R0/R1 intervention.

## 6. Fixed-representation and fixed-algorithm firewall

RIL-002 inherits:

```text
R0_AST:
    prediction = program.evaluate_local((x,y,z))

R1_SEM8:
    prediction = semantic_tuple[4*x + 2*y + z]
```

The scientific intervention is still representation only.

For every member `i`, the implementation must establish:

\[
G_i=(A_{\rm fixed}^{(i)},P_i,\Lambda_i).
\]

The same shared algorithm, candidate order, exhaustive-search policy, tie-break, update rule, precision, authority boundary, and cost-region definitions must apply to every member and both arms.

Any representation modification motivated by the RIL-002 family or by an observed family result requires a new assay identifier.

## 7. Member-level preservation and leverage

Each member is adjudicated independently.

At minimum, `P_i=1` requires exact arm identity for:

```text
candidate sets and order
all candidate semantics on all eight patterns
per-candidate probe scores
M0 and M1 winning accuracy
M0 and M1 canonical winner identity
gain
estimated repair value
repair decision
fanout_enabled state
selected semantic function
selected canonical program
all 3,000 held-out predictions
scope / seeds / precision / evaluation criteria
goal_rule_mutated = false
authority_expanded = false
required-operation coverage
```

If `P_i=0`, member `i` receives:

```text
PRESERVATION_FAILURE
```

and its raw cost may be retained for provenance but may not be interpreted as leverage.

For each evaluable preservation-valid member:

\[
\Lambda_i^{op}
=
\frac{C^{op}_{R0,i}}{C^{op}_{R1,i}}.
\]

The inherited memory non-regression gate also remains member-local.

Member classes are:

```text
NOT_EVALUABLE
PRESERVATION_FAILURE
NO_DEMONSTRATED_LEVERAGE
COMPUTE_FOR_MEMORY_TRADEOFF
REPRESENTATION_INDUCED_LEVERAGE
```

## 8. Primary family record

The primary scientific object is the ordered member record plus leverage vector:

\[
\boldsymbol{\Lambda}
=
(\Lambda_1,\ldots,\Lambda_{24}),
\]

with `NA` for members whose leverage is scientifically uninterpretable because `A_fixed` or `P` failed.

Do not replace this vector by a mean.

The machine-readable primary table must include, for every member:

```text
member_id
truth_table
A_fixed
P
C_op_R0
C_op_R1
Lambda_op
memory_R0
memory_R1
member_status
selected canonical identity
held-out prediction digest
```

Any aggregate is secondary to these records.

## 9. Family-level descriptive quantities

For the exact frozen family, report the compute-leverage coverage fraction:

\[
\kappa_{\mathcal F}^{op}
=
\frac{
|\{i:A_{\rm fixed}^{(i)}=1\land P_i=1\land\Lambda_i^{op}>1\}|
}{
|\{i:A_{\rm fixed}^{(i)}=1\land P_i=1\}|
}.
\]

This is **coverage of the finite frozen family**, not a population probability.

Also report full-RIL coverage, which additionally requires the inherited memory non-regression gate.

No independence assumption, p-value, or population-frequency inference is licensed by this deterministic family enumeration.

## 10. Family-level terminal interpretation

Use the member records first. The family summary may then use:

### `FAMILY_WIDE_LEVERAGE`

Every one of the 24 members is evaluable, preservation-valid, has `Lambda_op > 1`, and satisfies the memory non-regression gate.

### `HETEROGENEOUS_LEVERAGE`

The family is sufficiently evaluable to expose a mixed leverage profile: at least one preservation-valid member earns full leverage and at least one preservation-valid member does not.

### `NO_FAMILY_LEVERAGE`

No preservation-valid evaluable member earns full representation-induced leverage.

### `FAMILY_PRESERVATION_NOT_UNIVERSAL`

At least one member has `P_i=0`. Other members retain their own valid member-level statuses, but no universal family-preservation claim is allowed.

### `FAMILY_NOT_FULLY_EVALUABLE`

At least one member cannot instantiate the inherited fixed-algorithm/cost intervention. Other member records remain visible, but no family-wide result may be claimed.

These statuses do not erase member-level outcomes.

## 11. Leakage firewall

RIL-002 is a **family-transfer** study only.

Permitted selection information:

```text
frozen RIL-001 representation pair
frozen FS007 M0/M1 semantic libraries
truth-table semantics
essential-variable relation
RIL-001 target identity for exclusion
```

Forbidden before family freeze:

```text
any RIL-002 R0/R1 opcode comparison
any RIL-002 memory comparison
any RIL-002 wall-time comparison
any family-member leverage result
any member inclusion/exclusion based on expected or observed speedup
```

Because the representation was originally selected with knowledge of FS007 structure, a positive RIL-002 result cannot establish RIL-3 provenance-separated generalization.

## 12. Mandatory sequence

```text
define K
-> enumerate F exhaustively
-> freeze this preregistration + RIL_002_FAMILY.json
-> STOP family selection
-> implementation
-> freeze implementation
-> pre-execution source/A_fixed/instrumentation audit
-> if global audit fails: NOT_EVALUABLE -> STOP
-> execute frozen member records
-> evaluate P_i before interpreting Lambda_i
-> publish full leverage vector and family summary
-> final audit
-> STOP
```

No member may be replaced after execution begins.

## 13. Current state at freeze

At the first commit containing this file and `RIL_002_FAMILY.json`:

```text
K                         FROZEN
family                    FROZEN: 24 members
R0/R1                     inherited and frozen
RIL-002 implementation    DOES NOT EXIST
RIL-002 primary execution NOT RUN
RIL-002 leverage vector   DOES NOT EXIST
RIL-002 family verdict    NONE
RIL-3                     NOT OPENED
```

## 14. Governing rule

> **Freeze the species before counting the rabbits.**

RIL-002 may test transfer across this family. It may not redesign the representation to make the family look transferable.
