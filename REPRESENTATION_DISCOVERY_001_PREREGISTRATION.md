# Representation Discovery 001 — Preregistration

**Status:** `PREREGISTRATION FROZEN / NO LEARNER DESIGNED / NO LEARNER IMPLEMENTED / NO TEST INSTANCES GENERATED / NO EXECUTION`  
**Experiment ID:** `RD-001`  
**Parent program head:** `3d68471635dc3e88253763d9221ebeb88a61c013`  
**RIL-003:** `UNTOUCHED / FROZEN PRE-REVEAL`  
**Scope:** finite, fully enumerable planning calibration for representation-induced discovery leverage

---

## 0. Scientific question

RD-001 asks:

\[
\boxed{
\textbf{
Can a system prospectively acquire a reusable representation that reduces the
search required to solve unseen finite planning problems, without importing
unrevealed target-specific information into representation acquisition or use?
}
}
\]

The intended compression is:

\[
\boxed{
\textbf{compress uncertainty without importing the answer.}
}
\]

RD-001 is **not** a test of general reasoning, general intelligence, emergent abstraction, world-model learning, or a universal representation theory.

The maximum positive claim is bounded to the frozen finite planning family defined below.

---

## 1. Freeze order

The experiment is frozen in the following order:

\[
\boxed{
\text{task family}
\rightarrow
\text{test generator}
\rightarrow
R_0,R_\star
\rightarrow
R_L\text{ acquisition protocol}
\rightarrow
\text{information firewall}
\rightarrow
\text{cost accounting}
\rightarrow
\text{trap cases}
\rightarrow
\text{verdicts}.
}
\]

The learner architecture is deliberately **not** chosen in this artifact.

No implementation of \(R_L\) is permitted until:

1. the task generator is implemented and frozen;
2. the native baseline \(R_0\) is implemented and frozen;
3. the oracle structural control \(R_\star\) is implemented and frozen;
4. the cost instrumentation is implemented and frozen;
5. the training-side available-leverage calibration has been run and passed;
6. the information-firewall audit has passed.

Failure before step 6 terminates RD-001 before learner design.

---

# 2. Task family

## 2.1 Family name

The frozen family is the **finite identity-sensitive token planning family**.

Each instance contains:

- a finite directed graph \(G=(V,E)\);
- a finite set of tokens \(T=\{1,\ldots,k\}\);
- one unique native identity label for every token;
- one static binary descriptor \(z_i\in\{0,1\}^p\) for every token;
- edge labels drawn from a finite gate alphabet;
- a deterministic native transition rule;
- an identity-invariant goal condition over occupied goal vertices;
- at least one valid native solution.

The entire native state space is finite and must be exhaustively enumerable.

### Frozen parameter ranges

Unless a later implementation audit demonstrates that these ranges violate tractable exhaustive enumeration **before any learner is designed**, the implementation must use:

\[
\boxed{
p=4}
\]

static descriptor bits per token, with:

\[
|V|\in\{7,8,9\},
\qquad
k\in\{3,4,5\}.
\]

At most one token may occupy a vertex.

A native state is therefore an ordered identity-sensitive placement:

\[
s=(v_1,\ldots,v_k),
\]

with \(v_i\in V\) and \(v_i\neq v_j\) for \(i\neq j\).

The raw state-space ceiling for a fixed \((|V|,k)\) is:

\[
\frac{|V|!}{(|V|-k)!},
\]

which is small enough for exhaustive native-state enumeration under the frozen ranges.

## 2.2 Native actions

A primitive action is:

\[
\operatorname{MOVE}(i,u\rightarrow v),
\]

where token \(i\) currently occupies \(u\), \((u,v)\in E\), and \(v\) is unoccupied.

Whether the move is admissible may additionally depend on the edge label and the token descriptor \(z_i\).

No learned representation may add new native actions, delete native actions, weaken the goal predicate, or change the native transition function.

## 2.3 Hidden structural signature

Each generated family realization has a hidden structural signature \(\theta\).

\(\theta\) determines which descriptor distinctions can affect admissible future transitions under the frozen operation signature.

It includes:

- a nonempty relevant descriptor subset \(J\subset\{1,2,3,4\}\), with \(|J|\in\{1,2\}\);
- at least one edge-label gate whose admissibility depends on a bit in \(J\);
- descriptor coordinates in \(J^c\) that never affect native transitions or the goal predicate;
- at least one delayed gate condition under which two tokens that are locally indistinguishable before the gate become behaviorally distinguishable later because they differ on \(J\).

The realized value of \(\theta\) is **oracle-side information**.

It is not an input to \(R_L\).

The learner must infer reusable representational structure only from the permitted training interface.

## 2.4 Goal condition

Goals are identity-invariant.

A goal is defined by required occupancy of designated goal vertices or goal regions, not by native token IDs.

Therefore a token identity is consequential only through its effect on admissible future behavior, not because the goal explicitly names that token.

This prevents the experiment from trivializing the representation problem by putting identity dependence directly in the goal label.

---

# 3. Train, calibration, and held-out test generation

## 3.1 Dataset roles

The generator produces three nonoverlapping roles:

\[
\mathcal Q_{cal},
\qquad
\mathcal Q_{train},
\qquad
\mathcal Q_{test}.
\]

- \(\mathcal Q_{cal}\): pre-learner calibration for verifying that representational leverage exists under \(R_\star\);
- \(\mathcal Q_{train}\): the only task data available for representation acquisition;
- \(\mathcal Q_{test}\): prospectively held-out scientific evaluation.

Frozen suite sizes are:

\[
\boxed{
|\mathcal Q_{cal}|=24,
\qquad
|\mathcal Q_{train}|=48,
\qquad
|\mathcal Q_{test}|=48.
}
\]

## 3.2 Generator balance requirements

Every suite must contain both:

\[
\boxed{\text{safe-to-collapse distinctions}}
\]

and:

\[
\boxed{\text{future-consequential distinctions}}.
\]

The generator must satisfy all of the following by deterministic rejection sampling under its frozen seed:

1. every instance is finite and exhaustively enumerable;
2. every instance has at least one native solution;
3. every instance contains at least one pair of tokens differing only in native identity and/or descriptor coordinates that are irrelevant under \(\theta\);
4. at least half of the instances in each suite contain a designated delayed-consequence trap pair;
5. every relevant descriptor coordinate in \(J\) receives at least one behavioral witness in \(\mathcal Q_{train}\);
6. irrelevant descriptor coordinates in \(J^c\) receive variation in \(\mathcal Q_{train}\), so the learner cannot identify relevance merely from lack of variation;
7. test instances use fresh graph layouts and fresh native token identities not present in the training suite;
8. no test goal, test solution, test graph, or test native state graph is available during representation acquisition.

## 3.3 Seed procedure

The **seed derivation procedure is frozen now; the held-out test seed itself must not exist from the learner's perspective before \(R_L\) is frozen.**

The generator implementation contract must freeze one public, append-only randomness beacon and its exact network/chain identifier **before learner design**.

No fallback beacon is permitted after learner design.

The suite seeds are derived as follows:

- calibration seed: first eligible beacon value after generator-implementation freeze, domain-separated by `RD001/CAL`;
- training seed: the next eligible beacon value, domain-separated by `RD001/TRAIN`;
- test seed: the first eligible beacon value strictly after the \(R_L\) acquisition artifact has been frozen, domain-separated by `RD001/TEST`.

Each seed is:

\[
\operatorname{SHA256}(b\parallel h_{prereg}\parallel tag),
\]

where \(b\) is the frozen beacon value, \(h_{prereg}\) is the Git commit containing this preregistration, and `tag` is the domain-separation string above.

The implementation contract must specify the exact byte encoding before any beacon value is consumed.

If the frozen beacon is unavailable or provenance cannot be established, the affected suite is `NOT_EVALUABLE`; no substitute randomness source may be introduced post hoc.

---

# 4. Representation arms

RD-001 has exactly three representation arms.

## 4.1 \(R_0\): native identity-sensitive representation

\[
\boxed{R_0=\text{native identity-sensitive state}.}
\]

The visited-state key contains:

- every native token identity;
- every token position;
- every static token descriptor.

Two native states are equal under \(R_0\) iff they are exactly equal as native labeled states.

No symmetry reduction is permitted in \(R_0\).

## 4.2 \(R_\star\): oracle structural control

\[
\boxed{R_\star=\text{oracle structural representation}.}
\]

\(R_\star\) is evaluator-side only.

Using hidden structural signature \(\theta\), it canonicalizes native token identities exactly within token classes that are equivalent under the complete frozen future transition/goal signature.

It may collapse native identity and descriptor distinctions only when those distinctions cannot affect any admissible future native transition or the goal predicate under the frozen family.

\(R_\star\) exists only to measure the **available representational leverage ceiling**.

Its acquisition cost is:

\[
\boxed{C_{acquire}(R_\star)=\mathrm{NA}.}
\]

It must never be reported as zero-cost learned structure.

No information from \(R_\star\), its equivalence classes, its canonical keys, or its hidden structural labels is available to \(R_L\).

## 4.3 \(R_L\): learner-acquired representation

\[
\boxed{R_L=\text{learner-acquired candidate representation}.}
\]

The term **quotient** is deliberately not granted to \(R_L\) in advance.

\(R_L\) becomes eligible for a safe-equivalence interpretation only after exact held-out behavior and trap preservation have passed.

### Frozen output class

To prevent arbitrary code from hiding a solver inside the representation, the learner may output only a **candidate token-classification / canonicalization schema**.

Concretely, the acquisition artifact may specify:

1. a partition of the finite descriptor alphabet \(\{0,1\}^4\) into learned token classes;
2. whether native identity must be retained within each learned class;
3. a deterministic class-label encoding;
4. a deterministic state-key canonicalization rule that sorts/canonicalizes tokens only according to the learned classes and retained-identity flag.

The learned artifact may **not** contain:

- graph-specific test data;
- test goals;
- test solutions;
- test-state lookup tables;
- action recommendations;
- heuristic values indexed by test state;
- target IDs;
- oracle class labels;
- executable search code;
- instance-specific caches produced after test reveal.

The solver remains frozen BFS for all three arms.

Thus the learner is allowed to discover **which token distinctions should remain visible to the visited-state key**, not how to solve any particular held-out instance.

---

# 5. Solver protocol

All three arms use the same native breadth-first search procedure.

The native transition generator always operates on a concrete native state.

The only arm-specific search substitution is the visited-set key:

\[
K_0(s)=R_0(s),
\qquad
K_\star(s)=R_\star(s),
\qquad
K_L(s)=R_L(s).
\]

Successor generation, action ordering, queue discipline, goal checking, tie-breaking, termination conditions, and native action semantics must be byte-for-byte identical across arms except for the representation-key function and representation-specific bookkeeping required to construct that key.

This design deliberately avoids assuming that \(R_L\) already defines a valid quotient transition system.

An unsafe learned merge can therefore prune a native state that was required for a later solution, and that failure remains observable.

---

# 6. Representation acquisition protocol

## 6.1 Permitted acquisition inputs

The acquisition procedure may access only \(\mathcal Q_{train}\) through the frozen training interface.

Permitted information is:

- native graph structure for training instances;
- native token identities and descriptors for training instances;
- native initial states;
- training goal predicates;
- native transition queries on training states/actions;
- any training-side exhaustive enumeration produced through those same native primitives.

All acquisition work is counted in \(C_{acquire}(R_L)\).

## 6.2 Forbidden acquisition inputs

The acquisition procedure may not access:

- \(\theta\) directly;
- \(R_\star\) outputs or labels;
- oracle equivalence classes;
- \(\mathcal Q_{test}\) seeds, graphs, states, goals, solutions, or target IDs;
- future beacon values used to instantiate \(\mathcal Q_{test}\);
- evaluator-only trap labels;
- hidden generator metadata not present in the native training interface;
- any post-test feedback.

## 6.3 Freeze boundary

The complete \(R_L\) acquisition artifact must be frozen before the held-out test seed is available.

The freeze includes:

- acquisition source code;
- dependency/runtime identity;
- all learned parameters;
- learned descriptor partition;
- identity-retention flags;
- canonicalization code or declarative equivalent;
- all acquisition logs required for cost accounting;
- cryptographic digests of the final artifact.

After this freeze, \(R_L\) is immutable for RD-001.

No test-specific fine-tuning, patching, class splitting, exception list, cache, or representation repair is permitted.

---

# 7. Information firewall

The core no-leakage requirement is:

\[
\boxed{
D_{pre}(\omega_1)=D_{pre}(\omega_2)
\Longrightarrow
R_L(\omega_1)=R_L(\omega_2)
}
\]

for paired worlds differing only in unrevealed target-specific information at representation-acquisition time.

Operationally:

- the learner may know the public task-family definition and generator distribution;
- it may observe permitted training data;
- it may not know the realized held-out test seed or any data derived from it;
- changing only the future held-out test realization must not change the frozen \(R_L\) artifact.

The evaluator, oracle structural control, trap labels, test generator, and learner are separate epistemic roles.

Any post hoc evaluator transformation that repairs \(R_L\), reassigns learned classes, chooses a favorable interpretation, or searches alternative canonicalizations is forbidden.

A failed firewall audit yields:

`INFORMATION_FIREWALL_FAIL / TEST_NOT_OPENED`.

---

# 8. Cost accounting

RD-001 freezes the accounting identity:

\[
\boxed{
C_{total}
=
C_{acquire}
+
C_{instantiate}
+
C_{search}
+
C_{verify}.
}
\]

## 8.1 Acquisition cost

\(C_{acquire}(R_L)\) includes every operation used to produce the frozen learned representation from permitted training data.

It includes training-state enumeration, transition queries, descriptor analysis, candidate-class evaluation, internal search, and any validation performed by the acquisition procedure.

For \(R_0\), acquisition cost is zero because no learned structure is acquired.

For \(R_\star\), acquisition cost is `NA` because it is an oracle calibration control and is ineligible for autonomous-acquisition claims.

## 8.2 Fresh-instance instantiation cost

\(C_{instantiate}(X,R)\) includes every operation required after a fresh instance is revealed but before BFS starts.

For \(R_L\), this includes at minimum:

- descriptor-to-class mapping;
- any representation-specific tables built from the fresh instance;
- initialization of canonicalization machinery;
- any native-to-representation preprocessing.

Fresh-instance preprocessing may not inspect solutions or perform search without being charged here.

If fresh-instance instantiation performs work equivalent to solving the task, that work remains part of the total and cannot be hidden outside \(C_{search}\).

## 8.3 Search cost

\(C_{search}\) is **all counted work from BFS start until a candidate solution is produced or the search terminates**.

It must include representation machinery, not merely BFS expansion count.

At minimum the frozen instrumentation must count:

- native successor attempts;
- native successor states generated;
- representation-key construction;
- descriptor reads used by the key;
- canonicalization comparisons/moves;
- hashing or deterministic key-index work;
- visited-set membership/insertion work;
- queue insertion/removal work;
- goal checks;
- duplicate detections;
- decoding or reconstruction work required before candidate output.

The exact abstract-machine counting semantics and unit weights must be frozen in the implementation contract **before learner design**.

No cost category or weight may be changed after \(R_L\) is designed or after any held-out result is observed.

Wall-clock time may be reported as secondary metadata only.

## 8.4 Verification cost

Every candidate solution is replayed against the native \(R_0\) transition semantics.

\(C_{verify}\) includes all work needed to confirm:

- every action is natively admissible;
- the native final state satisfies the native goal;
- the reported path is the path actually returned by the frozen BFS arm.

Verification never repairs a failed candidate.

## 8.5 Primary per-instance record

For every held-out instance \(i\), report the complete raw count vector for every arm plus:

\[
\Lambda_i(R)=
\frac{C_{instantiate,i}(R_0)+C_{search,i}(R_0)+C_{verify,i}(R_0)}
{C_{instantiate,i}(R)+C_{search,i}(R)+C_{verify,i}(R)}.
\]

The primary result is the full vector:

\[
\boxed{(\Lambda_1,\ldots,\Lambda_N)}
\]

with no hidden averaging.

Aggregate cost is reported only alongside the complete per-instance record.

---

# 9. Required diagnostic records

For every arm and every test instance, record at least:

\[
\boxed{
\begin{aligned}
N_{states}\;&\text{ unique visited keys},\\
N_{generated}\;&\text{ native successors generated},\\
N_{expanded}\;&\text{ native representatives expanded},\\
N_{duplicates}\;&\text{ generated states rejected by visited-key collision},\\
C_{instantiate}\;&\text{ fresh-instance representation cost},\\
C_{search}\;&\text{ complete counted search work},\\
C_{verify}\;&\text{ native replay cost}.
\end{aligned}
}
\]

Also record:

\[
\boxed{\text{correctness mask}}
\]

and:

\[
\boxed{\text{trap-preservation mask}.}
\]

A correctness or trap-preservation failure is never averaged away by lower cost on other cases.

---

# 10. Delayed-consequence trap cases

A designated trap pair consists of two tokens or native states that are indistinguishable under an overaggressive collapse at the start of the task but become distinguishable under a later admissible operation.

Schematically:

\[
s_a\sim_{local}s_b
\]

while:

\[
\exists o_{future}:
O_{future}(s_a)\neq O_{future}(s_b).
\]

Every trap instance must contain a concrete future witness showing why the distinction matters.

The witness must be generated and stored evaluator-side before held-out adjudication and must not be exposed to \(R_L\).

For the frozen \(R_L\) output class, a trap is preserved iff the learned state-key schema retains enough distinction that the designated future-different native states do not become an unsafe visited-key collision.

The trap-preservation mask is binary per designated trap.

Any zero in the trap-preservation mask makes the positive-leverage claim ineligible, regardless of aggregate speedup.

Thus:

\[
\boxed{
\text{cheap wrong search}
\neq
\text{representational leverage}.
}
\]

---

# 11. Pre-learner available-leverage gate

Before any \(R_L\) learner is designed, run \(R_0\) and \(R_\star\) on \(\mathcal Q_{cal}\) using the frozen solver and accounting implementation.

The gate passes only if:

1. \(R_\star\) preserves exact native correctness on every calibration instance;
2. every calibration trap is preserved by \(R_\star\);
3. aggregate fresh-instance counted cost under \(R_\star\) is strictly lower than under \(R_0\):

\[
\sum_{i\in\mathcal Q_{cal}} C_{fresh,i}(R_\star)
<
\sum_{i\in\mathcal Q_{cal}} C_{fresh,i}(R_0),
\]

where

\[
C_{fresh}=C_{instantiate}+C_{search}+C_{verify}.
\]

If this gate fails, RD-001 terminates as:

`AVAILABLE_LEVERAGE_NOT_DEMONSTRATED / LEARNER_NOT_DESIGNED`.

The experiment must not respond by redesigning the family around a learner.

---

# 12. Held-out adjudication

After \(R_L\) is frozen and the test beacon value becomes available:

1. materialize \(\mathcal Q_{test}\) exactly once;
2. freeze the generated test manifest before any arm runs;
3. run \(R_0\), \(R_\star\), and \(R_L\) under the same solver/counter implementation;
4. verify every returned solution natively;
5. compute correctness and trap masks;
6. publish the complete per-instance raw records before interpretation.

No learner modification or test regeneration is permitted after step 1.

---

# 13. Verdicts

Verdicts are mutually constrained as follows.

## 13.1 Protocol / constitution verdicts

### `NOT_EVALUABLE`

Use when a required frozen artifact, provenance record, counter implementation, generator identity, or randomness-beacon condition is not constituted.

### `INFORMATION_FIREWALL_FAIL`

Use when hidden target-specific information could have influenced \(R_L\), directly or through an evaluator/adapter side channel.

No scientific leverage claim is permitted after this verdict.

### `AVAILABLE_LEVERAGE_NOT_DEMONSTRATED`

Use when \(R_\star\) fails the pre-learner calibration gate.

The learner is not designed.

## 13.2 Learned-representation verdicts

### `UNSAFE_COMPRESSION`

Use if any held-out correctness bit or any trap-preservation bit for \(R_L\) is zero.

Cost reduction cannot rescue this verdict.

### `NO_LEARNED_COMPRESSION`

Use when \(R_L\) preserves exact held-out correctness and all traps but does not reduce aggregate fresh-instance counted cost relative to \(R_0\).

### `LEARNED_REPRESENTATIONAL_LEVERAGE`

Use only when all of the following hold:

1. information firewall passes;
2. every held-out correctness bit for \(R_L\) is one;
3. every trap-preservation bit for \(R_L\) is one;
4. aggregate fresh-instance cost is lower:

\[
\sum_{i\in\mathcal Q_{test}}C_{fresh,i}(R_L)
<
\sum_{i\in\mathcal Q_{test}}C_{fresh,i}(R_0);
\]

5. the full per-instance leverage vector and raw count vectors are published.

This verdict does **not** require acquisition cost to have paid back.

### `NON_AMORTIZING_REPRESENTATION_DISCOVERY`

Use when `LEARNED_REPRESENTATIONAL_LEVERAGE` passes but, over the frozen \(|\mathcal Q_{test}|=48\) horizon,

\[
C_{acquire}(R_L)
+
\sum_i C_{fresh,i}(R_L)
\ge
\sum_i C_{fresh,i}(R_0).
\]

This means useful coordinates were learned and useful on fresh instances, but the acquisition bill did not pay back over the preregistered horizon.

### `AMORTIZED_LEVERAGE`

Use only when `LEARNED_REPRESENTATIONAL_LEVERAGE` passes and:

\[
\boxed{
C_{acquire}(R_L)
+
\sum_i C_{fresh,i}(R_L)
<
\sum_i C_{fresh,i}(R_0).
}
\]

This is the strongest RD-001 verdict.

---

# 14. Interpretation matrix

The following outcomes remain scientifically distinct.

\[
R_\star\ll R_0,
\qquad
R_L\approx R_0
\]

means:

> useful representational leverage exists, but the acquisition procedure did not discover it.

\[
R_\star\ll R_0,
\qquad
R_L\ll R_0,
\qquad
\text{all safety masks}=1
\]

means:

> the learner acquired useful representational structure that reduced fresh-instance search cost.

\[
R_L\ll R_0,
\qquad
\text{some safety mask}=0
\]

means:

> the learner found compression, but not an admissible future-preserving representation.

\[
R_L\ll R_0,
\qquad
\text{all safety masks}=1,
\qquad
C_{acquire}\text{ prevents payback}
\]

means:

> representation discovery succeeded locally but did not amortize over the frozen horizon.

None of these outcomes may be collapsed into a generic `SUCCESS` or `FAILURE` label.

---

# 15. Claim ceiling

The strongest admissible positive statement is:

> **On a fully enumerable finite planning family, a prospectively frozen learner acquired a reusable representation that reduced exhaustive search on held-out instances while preserving exact native task behavior, with target-specific test information unavailable during representation acquisition.**

If and only if the acquisition bill also pays back over the frozen test horizon, add:

> **The measured savings exceeded the counted representation-acquisition cost over the preregistered horizon.**

RD-001 does **not** establish:

- general reasoning improvement;
- general AI efficiency;
- universal representation-induced discovery leverage;
- autonomous ontology invention;
- a general quotient-learning theorem;
- a universal relation between compression and intelligence;
- that the learned representation is optimal;
- that \(R_L\) recovered \(R_\star\) unless that relation is separately demonstrated;
- any result about natural-language reasoning, neural models, distributed agents, or open-world tasks;
- a new corrigibility architecture;
- any modification to RIL-003 or its reveal protocol.

---

# 16. Current stop state

At this preregistration freeze:

```text
RD-001 PREREGISTRATION        = FROZEN
TASK FAMILY SPECIFICATION     = FROZEN AT CONTRACT LEVEL
GENERATOR IMPLEMENTATION      = NOT OPENED
R0 IMPLEMENTATION             = NOT OPENED
R_STAR IMPLEMENTATION         = NOT OPENED
COST COUNTER IMPLEMENTATION   = NOT OPENED
AVAILABLE-LEVERAGE CALIBRATION= NOT RUN
R_L LEARNER DESIGN            = NOT OPENED
R_L IMPLEMENTATION            = NONE
R_L ACQUISITION               = NOT RUN
TEST SEED                     = UNAVAILABLE BY DESIGN
TEST INSTANCES                = NOT GENERATED
HELD-OUT EXECUTION            = NOT RUN
SCIENTIFIC RESULT             = NONE
```

The next permitted work is **generator / baseline / oracle-control / counter constitution and audit**, not learner design.

The governing question remains:

\[
\boxed{
\textbf{
Can the system discover coordinates that make its own search cheaper,
without secretly doing the search while constructing or applying those coordinates?
}
}
\]
