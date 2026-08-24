# RIL-003 — Provenance-Separated Transfer Preregistration

Status: **PROSPECTIVE; TEST GENERATOR / SHARED-INFORMATION BOUNDARY / REPRESENTATION PAIR FROZEN; NO HELD-OUT TARGET INSTANCE EXISTS AT FREEZE**

Rung: **RIL-3 — provenance-separated representation-induced transfer**

Parent evidence:

```text
RIL-001 = REPRESENTATION_INDUCED_LEVERAGE, CLOSED
RIL-002 = FAMILY_WIDE_LEVERAGE, CLOSED
```

RIL-003 is not another family-transfer assay. Its sole purpose is to test whether the already-frozen AST→SEM8 representation change retains computational leverage on target instances whose target-specific information was unavailable when the representation pair was selected and frozen.

Nothing in RIL-003 may rewrite the closed corpus, CGP-001, RIL-001, or RIL-002.

## 1. Sole question and claim ceiling

RIL-003 asks:

> **Does the exact AST→SEM8 representation pair inherited from RIL-001/RIL-002 preserve and reduce the counted computational cost of the frozen FS007 decision/update procedure on prospectively generated Boolean target instances whose target-specific identities were unavailable during representation selection?**

The strongest possible positive claim is:

> **provenance-separated representation-induced transfer within the exact shared 3-input Boolean schema and frozen resource contract.**

A positive RIL-003 result does **not** by itself establish `representation-induced generality`. That stronger phrase requires repeated positive results across independently constituted held-out regimes.

## 2. Mandatory provenance order

The scientific order is frozen as:

```text
Q_test frozen
-> I_shared whitelist frozen
-> R0/R1 frozen
-> STOP
-> later generic implementation / implementation freeze
-> pre-reveal audit
-> held-out entropy pulse becomes available
-> F_test instantiated exactly once from Q_test
-> target manifest frozen
-> member execution
-> A_fixed_i / P_i
-> Lambda vector
-> result / audit
-> STOP
```

At this preregistration freeze the sequence stops after `R0/R1 frozen`.

No held-out target may be instantiated, revealed, inspected, scored, or used to alter the representation pair in the preregistration commit.

## 3. Frozen held-out generator `Q_test`

### 3.1 Object/type schema

Every target is a deterministic total Boolean function

\[
f:\{0,1\}^3\rightarrow\{0,1\}.
\]

Inputs are the ordered coordinates:

```text
(x, y, z)
```

with canonical pattern order:

```text
000, 001, 010, 011, 100, 101, 110, 111
```

A target is represented extensionally by exactly eight output bits in that order. The first output bit is the most-significant bit of the stable hexadecimal target ID.

### 3.2 Valid input domain

Only the complete eight-pattern domain `Boolean^3` is valid.

No larger arity, continuous input, stateful target, hidden context variable, or task-dependent coordinate system is part of RIL-003.

### 3.3 Valid output semantics

Each local pattern maps to exactly one bit in `{0,1}`.

No probabilistic, multi-valued, sequence-valued, or authority-bearing target output is admissible.

### 3.4 Complexity bound

The held-out target object is bounded extensionally:

```text
input arity             = 3
input alphabet          = {0,1}
output alphabet         = {0,1}
truth-table length      = 8
target state            = none
target memory           = none
```

Eligibility additionally requires that all three variables are essential:

```text
x essential
y essential
z essential
```

where variable `v` is essential iff at least one pair of inputs differing only in `v` receives different target outputs.

No target is included or excluded using:

```text
READ_ONCE_PROGRAMS membership
FANOUT_PROGRAMS membership
minimal AST size
canonical fanout program
exact M0/M1 ceiling
RIL-001/RIL-002 leverage magnitude
predicted AST evaluation cost
predicted SEM8 evaluation cost
```

This is deliberate: RIL-003 target eligibility is defined from the shared extensional schema, not from whether a target is known to be friendly to the inherited representation.

### 3.5 Prior-target exclusion set

The only permitted use of RIL-001/RIL-002 target-specific identities inside `Q_test` is exact negative exclusion so that no held-out target is literally one of the previously tested targets.

Frozen excluded truth-table IDs:

```text
RIL-001:
0x17

RIL-002:
0x1B 0x1D 0x27 0x2E 0x35 0x3A
0x47 0x4E 0x53 0x5C 0x72 0x74
0x8B 0x8D 0xA3 0xAC 0xB1 0xB8
0xC5 0xCA 0xD1 0xD8 0xE2 0xE4
```

No distance-to-prior-target, structural-similarity, canonical-program, prior leverage, or prior result information may be used to rank or filter remaining targets.

### 3.6 Eligible universe

Let `U` be all 256 Boolean truth tables over the frozen pattern order.

Let `Ess3(f)` mean all three variables are essential.

Let `E_prior` be the exact 25-target exclusion set above.

Then:

\[
U_{\rm eligible}
=
\{f\in U:\mathrm{Ess3}(f)\}
\setminus E_{\rm prior}.
\]

The expected cardinality, fixed prospectively, is:

```text
all-three-essential Boolean truth tables = 218
prior exact targets excluded             = 25
eligible held-out universe               = 193
```

Any later generator implementation that does not reproduce `|U_eligible| = 193` makes RIL-003 `NOT_EVALUABLE`; it may not repair the rule after target reveal.

### 3.7 Family size

The held-out family size is frozen as:

\[
n=24.
\]

Sampling is without replacement from the 193-member eligible universe.

The number 24 is fixed before target instantiation and matches the RIL-002 member count only for comparability of record shape. It is not a stopping rule and may not change after target reveal.

### 3.8 Future public entropy source

Actual target identities must remain unavailable at this freeze.

The future sampling entropy is frozen as the **NIST Randomness Beacon 2.0** pulse:

```text
target time:
2026-08-26T12:00:00.000Z
```

Use the first Beacon 2.0 pulse whose timestamp is **greater than or equal to** that target time.

The sampling seed material is the pulse's 512-bit `outputValue`, decoded from hexadecimal bytes.

Rules:

```text
- do not query or substitute an earlier pulse
- do not choose among multiple future pulses
- do not substitute OS randomness, another beacon, a block hash, or a manual seed
- if the specified/next pulse is temporarily unavailable, do not generate targets from another source
- record the exact pulse timestamp, chain/pulse identifiers, outputValue, and pulse package digest in the later target-reveal manifest
```

The Beacon value is public randomness for auditable selection, not a secret cryptographic key.

### 3.9 Deterministic sampling rule

After the frozen future pulse exists:

1. Enumerate all 193 eligible truth tables.
2. Encode each stable target ID as uppercase ASCII `TT_XX`, where `XX` is the two-digit hexadecimal truth-table value.
3. Decode the Beacon `outputValue` into exactly 64 bytes.
4. For every eligible target `t`, compute:

```text
rank_digest(t)
=
SHA256(
    b"RIL-003|TARGET-RANK|"
    + beacon_output_bytes
    + b"|"
    + target_id_ascii
)
```

5. Sort all 193 targets lexicographically by `rank_digest(t)`, breaking any impossible/accidental digest tie by ascending target ID.
6. Select the first 24.
7. Preserve that ordered list as `F_test`.
8. Commit the target-reveal manifest before any member cost execution.

No rejection sampling, redraw, substitution, manual balancing, family reshaping, or post-reveal eligibility change is allowed.

### 3.10 Target-reveal freeze

The later target-reveal artifact must contain at minimum:

```text
Beacon target time
actual pulse timestamp
chain identifier
pulse identifier
outputValue
digest of complete pulse package
eligible-universe cardinality = 193
ordered 24 target IDs
ordered 24 truth tables
ordered-family canonical SHA-256
statement that no target cost/preservation result existed before reveal commit
```

The target reveal is a new freeze boundary. Execution may not precede it.

## 4. Frozen shared-information boundary `I_shared`

RIL-003 uses a whitelist.

Information not explicitly listed below is not admissible for representation selection/construction under this assay.

### 4.1 Whitelisted shared schema/interface information

The following may be known before target reveal:

```text
S1  input type: three ordered Boolean coordinates (x,y,z)
S2  complete input domain: {0,1}^3
S3  canonical coordinate/pattern order:
    000,001,010,011,100,101,110,111
S4  output type: one Boolean bit
S5  target object is a deterministic total 8-entry truth table
S6  all generated targets must have x,y,z essential
S7  held-out family size n=24
S8  exact Q_test eligibility/sampling procedure in this preregistration
S9  exact prior-target exclusion set, for exclusion only
S10 frozen FS007 candidate languages and canonical candidate identities/order
S11 frozen FS007 exhaustive search / tie-break / gain / value / update semantics
S12 frozen repair cost, horizon, task/probe/held-out sizes, and data-generation seeds
S13 frozen authority and scope boundary
S14 frozen resource-accounting contract:
    CPython instruction events by region + inherited memory non-regression gate
S15 historical fact that AST/SEM8 produced positive RIL-001 and RIL-002 results
S16 exact frozen definitions of R0_AST and R1_SEM8
```

This whitelist supplies enough interface/type information to keep the transformation well-typed.

### 4.2 Forbidden held-out target-specific information

Before the representation pair is frozen, none of the following may be available to or influence representation selection/construction:

```text
T1  future Beacon outputValue
T2  actual sampled held-out target IDs
T3  actual sampled held-out truth tables
T4  target-specific probe labels
T5  target-specific held-out labels/predictions
T6  target membership in M0 or M1
T7  exact M0/M1 ceiling for any sampled target
T8  canonical best program for any sampled target
T9  minimal AST/program size for any sampled target
T10 target-specific repair gain/value/decision
T11 target-specific expected AST or SEM8 cost
T12 target-specific opcode/memory/timing result
T13 target-derived clustering, feature engineering, similarity score, or expected leverage
T14 any cache, feature, lookup, index, compilation, or code path derived from sampled target identity
```

The governing provenance condition is:

\[
\mathcal I_{\rm target}^{\rm test}
\notin
\mathcal I_{\rm select}(R_1).
\]

Shared schema overlap is allowed; held-out target-specific information is not.

## 5. Frozen representation selection rule

RIL-003 does not perform a new representation search.

The representation-selection rule is the constant inherited pair:

\[
R_0=\texttt{R0\_AST},
\qquad
R_1=\texttt{R1\_SEM8}.
\]

Exact operative meanings:

```text
R0_AST:
candidate payload = frozen canonical Program AST
prediction         = program.evaluate_local((x,y,z))

R1_SEM8:
candidate payload = frozen exact 8-pattern semantic tuple
prediction         = semantic_tuple[4*x + 2*y + z]
```

RIL-003 is allowed to test this pair because it was selected and frozen before the future RIL-003 target instances exist.

Forbidden after this freeze:

```text
SEM8 tuning
new semantic features
new indexing scheme
target-specific lookup
target-specific cache
new compilation
new JIT
vectorization
new batching available to one arm
pruning
early stopping
candidate reordering
changed representation payload
changed tie-break
changed search/update rule
"minor" adaptation after target reveal
```

Any representation change after the target-reveal boundary requires a new assay identifier and cannot be scored as RIL-003.

## 6. Frozen corrective procedure and conditions

For each later held-out target `F_i`, RIL-003 applies the same frozen FS007 decision/update procedure used by RIL-001/RIL-002:

```text
target-labelled probe examples
-> exhaustive M0/read-once search
-> exhaustive M1/fanout search
-> gain = max(0, a1-a0)
-> estimated_repair_value = FUTURE_HORIZON * gain
-> strict estimated_repair_value > LOW_REPAIR_COST
-> persist/read fanout_enabled
-> select canonical winner under the frozen tie-break
-> evaluate selected result on the frozen held-out construction
```

The target label function for a revealed truth table `t` is:

```text
(x,y,z) -> t[4*x + 2*y + z]
```

Frozen conditions inherited from RIL-001/RIL-002:

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

A target may or may not cause the repair to be adopted. RIL-003 tests the cost of the same frozen decision/update transformation under the held-out target, not a preselected positive-repair-only subset.

## 7. Fixed-algorithm gate

For every target `i`, the scientific object is:

\[
G_i=
(A_{\rm fixed}^{(i)},P_i,\Lambda_i).
\]

The arm intervention may select only the inherited AST-vs-SEM8 candidate prediction primitive.

Shared and arm-equal:

```text
candidate sets/order
candidate visits
probe examples/order
held-out examples/order
exhaustive search
score accumulation
canonical tie-break
gain calculation
repair-value calculation
repair decision
state update
held-out evaluation
precision
authority/scope
result serialization
```

If the inherited fixed-algorithm intervention cannot be instantiated for the revealed target regime, the affected member is `NOT_EVALUABLE`; RIL-003 may not redesign the intervention after target reveal.

## 8. Member preservation gate

For every target `F_i`, `P_i=1` requires exact arm identity for all preregistered semantic/scientific outputs, including at minimum:

```text
candidate sets/order
candidate semantics on all 8 input patterns
per-candidate probe scores
M0 winner / accuracy
M1 winner / accuracy
gain
estimated repair value
repair/adoption decision
fanout_enabled
selected semantic function
selected canonical identity
all 3,000 held-out predictions
held-out accuracy
scope / seeds / precision / criteria
goal_rule_mutated = false
authority_expanded = false
required-operation coverage
```

If:

\[
P_i=0,
\]

then:

```text
member_status = PRESERVATION_FAILURE
```

and any raw cost values for that member are provenance only:

\[
P_i=0
\Rightarrow
\Lambda_i\text{ has no scientific leverage interpretation}.
\]

## 9. Cost and leverage

RIL-003 inherits the RIL-001/RIL-002 cost accounting.

For each preservation-valid evaluable target:

\[
\Lambda_i^{op}
=
\frac{C^{op}_{R0,i}}{C^{op}_{R1,i}}.
\]

Primary computational work is the frozen CPython instruction-event accounting with the same region semantics.

The memory non-regression gate remains member-local.

No hidden representation construction, translation, target-specific cache construction, preprocessing, or setup cost may be omitted.

## 10. Primary result object

The primary scientific record is the ordered target/member table plus:

\[
\boldsymbol{\Lambda}
=
(\Lambda_1,\ldots,\Lambda_{24}),
\]

using `NA` wherever leverage is uninterpretable because `A_fixed` or `P` failed.

Do not replace the vector by a mean.

A heterogeneous vector is a valid scientific result and may expose the boundary of the inherited affordance.

Any family-level summary is secondary to member records.

## 11. RIL-003 interpretation ceiling

A positive result may earn only:

```text
PROVENANCE_SEPARATED_REPRESENTATION_INDUCED_TRANSFER
```

within this exact generator, shared schema, substrate/runtime, frozen representation pair, and correction procedure.

It does not earn:

```text
representation-induced generality
resource-boundary amplification
broad effective generality
universal affordance geometry
general constrained-hardware capability amplification
```

A stronger generality claim requires repeated positive evidence across independently constituted held-out regimes.

## 12. Failure/null preservation

Possible scientifically meaningful outcomes include:

```text
global NOT_EVALUABLE
member NOT_EVALUABLE
member PRESERVATION_FAILURE
member NO_DEMONSTRATED_LEVERAGE
member COMPUTE_FOR_MEMORY_TRADEOFF
member REPRESENTATION_INDUCED_LEVERAGE
heterogeneous leverage vector
zero-transfer vector
positive provenance-separated transfer
```

No null may be repaired away under RIL-003 after target reveal.

## 13. Current state at preregistration freeze

At the first commit containing this preregistration and its machine-readable generator contract:

```text
Q_test                    FROZEN
I_shared whitelist        FROZEN
forbidden target info     FROZEN
R0/R1                     FROZEN: inherited AST / SEM8
future entropy rule       FROZEN
held-out target instances DO NOT EXIST / NOT REVEALED
RIL-003 implementation    DOES NOT EXIST
target reveal manifest    DOES NOT EXIST
RIL-003 execution         NOT RUN
Lambda vector             DOES NOT EXIST
RIL-003 verdict           NONE
RIL-4                     NOT OPENED
```

The immediate sequence is terminal at:

```text
Q_test
-> I_shared
-> R0/R1
-> STOP
```

## 14. Governing rule

> **Freeze the territory generator, freeze what the representation is allowed to know, freeze the coordinates, and only then let the territory exist.**
