# RD-001 — Pre-Learner Implementation Contract

**Status:** `IMPLEMENTATION FROZEN / PRE-CALIBRATION / NO LEARNER DESIGNED / NO TEST SEED`  
**Experiment:** `RD-001`  
**Preregistration commit:** `bb0a85182a59a498568fa2905a49802af35b56b4`  
**Parent apparatus commit:** `b1075491753ee4cb53577743daf6e8fb20455ea9`  
**RIL-003:** `UNTOUCHED / FROZEN PRE-REVEAL`

This contract constitutes only the generator, native arm `R0`, oracle structural control `R_STAR`, shared BFS, abstract cost counter, structural diagnostics, and pre-learner calibration machinery.

It does **not** design or implement `R_L`.

---

## 1. Frozen executable

Path:

`experiments/rd_001/rd001.py`

Git blob at the parent apparatus commit:

`fc8408e5eaba924625b647ccebe81ea43165c0e6`

Authoring-side SHA-256 of the exact UTF-8 source bytes:

`8ab45108602d0dc09cc15d782e30caa0b1bc7854e4fc812bd1fe81b0c1436ea9`

The implementation uses only the Python standard library.

A deterministic non-scientific self-test exists as:

`python rd001.py selftest`

The self-test uses the fixed string `RD001 NONSCIENTIFIC SELFTEST`; it is not a calibration seed and cannot contribute scientific evidence.

The self-test must pass before scientific calibration execution.

---

## 2. Frozen generator concretization

The preregistered finite identity-sensitive token planning family is concretized as follows.

### 2.1 Descriptors

Each token has a four-bit descriptor. Bit indices are `0,1,2,3`, with bit `0` the least-significant bit in the integer encoding.

For each generated instance the hidden structural signature chooses:

- `|J| in {1,2}`;
- `J` uniformly through the frozen deterministic PRNG path;
- one descriptor pair that has the same projection on `J` but differs on **every** coordinate in `J^c`;
- one descriptor that flips every coordinate in `J` relative to the base descriptor.

Thus every accepted instance contains both a safe-to-collapse pair and a future-consequential descriptor distinction.

### 2.2 Native identities

The local token set remains ordered as `1..k` for native transition semantics.

The native identity label stored in `R0` is globally namespaced as:

`<ROLE>-<accepted-instance-index>-T<local-index>`.

This satisfies the preregistered fresh-identity requirement without changing the local action semantics.

### 2.3 Graph and edge alphabet

For `n in {7,8,9}` vertices, a candidate graph contains:

1. a randomly permuted bidirectional free cycle over all vertices;
2. two to four additional directed `FREE` chords;
3. exactly one descriptor-gated directed edge for every bit in `J`.

The gate alphabet is:

- `FREE`;
- `Bj=0`;
- `Bj=1`.

A gated edge is admissible to token `i` iff descriptor bit `j` of that token equals the gate value.

Gate sources are chosen outside the initial occupied vertices.

### 2.4 Initial and goal states

The initial state assigns the first `k` vertices of the frozen random vertex permutation to the ordered native tokens.

The goal is an identity-invariant occupancy set of exactly `k` vertices. Native token IDs are never named by the goal predicate.

### 2.5 Trap construction

Every accepted instance, not merely half, contains a designated delayed-consequence trap.

Tokens `0` and `2` differ on every relevant descriptor coordinate in `J`. The primary trap uses the first relevant gate.

Evaluator-side trap states are identical except that those two tokens exchange the gate-source position and a spare position. In one state the token at the gate source satisfies the gate; in the swapped state it does not.

A representation preserves the designated trap only if these two future-different native states have distinct visited keys.

### 2.6 Rejection sampling

Candidate generation is deterministic under the suite seed. A candidate is rejected unless:

- the safe pair has identical `J` projection;
- every irrelevant coordinate varies across that pair;
- every relevant coordinate has both descriptor values represented and has a corresponding gate;
- the oracle structural control preserves the designated trap;
- native `R0` BFS finds and natively verifies at least one solution;
- the layout hash has not already appeared in the suite or supplied exclusion set.

No candidate is accepted or rejected because it gives a favorable `R_STAR/R0` cost ratio.

The generator may not be tuned after the calibration result is observed.

---

## 3. Frozen deterministic PRNG

Suite generation uses a SHA-256 counter-mode PRNG implemented in the frozen executable.

Given a 32-byte suite seed and role string, the PRNG root is:

`SHA256(seed || UTF8(role))`.

Each counter block is:

`SHA256(root || uint64_be(counter))`.

`randbelow(n)` uses 64-bit rejection sampling to avoid modulo bias.

The generator implementation, not Python's `random` module, determines all scientific randomness after seed derivation.

---

## 4. Frozen representations

### 4.1 R0

`R0` is the preregistered native identity-sensitive visited key.

For every token it emits, in native token order:

`(native_identity, position, full_4_bit_descriptor)`.

No symmetry reduction occurs.

### 4.2 R_STAR

`R_STAR` receives evaluator-only `J`.

Its token class is exactly the descriptor projection onto `J`.

For each state it:

1. buckets token positions by exact `J` projection;
2. sorts positions within each class;
3. emits classes in deterministic lexicographic class-label order.

It therefore discards native identity and descriptor coordinates in `J^c`, and no others.

`R_STAR` is an oracle calibration control only. Its acquisition cost is `NA`.

---

## 5. Frozen BFS

All arms use the same native BFS.

Frozen shared semantics include:

- native successor generation on concrete native states;
- native token order as action-order primary key;
- sorted outgoing edges as action-order secondary key;
- FIFO queue;
- identity-invariant native goal check;
- first-seen representative retained on visited-key collision;
- no heuristic;
- no arm-specific successor rule;
- no arm-specific goal rule;
- no post-search repair.

The only scientific arm difference in this calibration is the visited-state key plus the bookkeeping required to construct it.

Every returned path is replayed against native transition and goal semantics.

---

## 6. Frozen cost counter

The abstract machine uses **unit weight for every explicitly emitted counter event** in the frozen source.

The calibration quantity is:

`C_fresh = C_instantiate + C_search + C_verify`.

`C_search` includes representation machinery. In particular, the frozen source charges events for:

- successor attempts and generated successors;
- occupancy scans and descriptor gate checks;
- native-state copying;
- representation-key reads and emitted atoms;
- deterministic hash-mix abstractions;
- `R_STAR` bucketing, canonical comparisons, moves, and writes;
- visited lookup/insertion and duplicate detection;
- queue operations;
- goal checks;
- path reconstruction.

`C_instantiate` charges arm-specific fresh-instance representation setup.

`C_verify` charges native replay.

No counter category or weight may change after this implementation freeze.

Python wall-clock time is secondary metadata only and is not part of the scientific gate.

### Diagnostic work excluded from C_fresh

The following evaluator-side work is diagnostic or suite-construction work and is not arm-specific fresh-instance solving cost:

- generator rejection checks;
- generator-side native solvability validation;
- exhaustive enumeration used to report exact structural state-space counts.

These operations may not influence which arm wins and are not hidden inside either arm's `C_fresh`.

---

## 7. Frozen structural diagnostic

For each calibration instance report separately:

- exact native state-space count `|S_0| = n!/(n-k)!`;
- exact number of distinct `R_STAR` keys over all native placements;
- their ratio;
- `C_search(R0) - C_search(R_STAR)`;
- `C_fresh(R0) - C_fresh(R_STAR)`.

Structural state-space enumeration is not itself evidence of computational leverage. The available-leverage gate remains the preregistered fresh-cost gate.

---

## 8. Frozen public randomness beacon

RD-001 uses the **League of Entropy drand default mainnet**.

Frozen chain identity:

- chain hash: `8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce`
- scheme: chained BLS mainnet (`default`)
- period: `30` seconds
- genesis Unix time: `1595431050`
- distributed public key: `868f005eb8e6e4ca0a47c8a77ceaa5309a47978a7c71bc5cce96366b5d7a569937c529eeda66c7293784a9402801af31`

Frozen retrieval path shape:

`https://api.drand.sh/<CHAIN_HASH>/public/<ROUND>`

A second official relay may be used only to establish byte-for-byte relay agreement for the same already-selected round; it may not select a different round.

### 8.1 Calibration-round eligibility

Let `t_freeze` be the UTC committer timestamp of the Git commit that adds this implementation contract.

For round `r >= 1`, its scheduled time is frozen as:

`T(r) = 1595431050 + 30*(r-1)`.

The calibration beacon is the **unique first round** satisfying:

`T(r) > t_freeze`.

No later favorable round may be substituted.

### 8.2 Seed byte encoding

Let `b` be the 32 raw bytes obtained by hex-decoding the selected drand `randomness` field.

Let `h_prereg` be the 20 raw bytes obtained by hex-decoding:

`bb0a85182a59a498568fa2905a49802af35b56b4`.

The calibration seed is exactly:

`SHA256(b || h_prereg || UTF8("RD001/CAL"))`.

The later training and test domain tags remain exactly `RD001/TRAIN` and `RD001/TEST` under the preregistration. No test beacon or test seed is permitted before `R_L` freeze.

---

## 9. Pre-calibration execution order

After this commit exists:

1. identify its UTC committer timestamp;
2. compute the first eligible drand round from Section 8;
3. capture the exact beacon package for that round;
4. verify round identity and internal `randomness = SHA256(signature)` consistency and record relay provenance;
5. derive the `RD001/CAL` seed exactly once;
6. materialize exactly 24 `CAL` instances;
7. freeze the complete calibration manifest before running the scientific `R0/R_STAR` comparison;
8. audit manifest identity, suite count, constraints, code identity, counter identity, and no-learner state;
9. only then execute the calibration;
10. publish complete raw per-instance records before interpretation.

No `TRAIN` or `TEST` scientific result is needed for the available-leverage gate.

---

## 10. Available-leverage gate

The gate remains:

`sum_i C_fresh,i(R_STAR) < sum_i C_fresh,i(R0)`

and:

- every `R_STAR` calibration result is natively correct;
- every designated trap is preserved.

If the gate fails, the terminal verdict is:

`AVAILABLE_LEVERAGE_NOT_DEMONSTRATED / LEARNER_NOT_DESIGNED`.

No generator, oracle representation, BFS, trap, or cost-counter tuning is permitted in response.

If the gate passes, the only newly permitted next phase is learner design under the frozen preregistration and this implementation boundary.

---

## 11. Stop state at this freeze

```text
RD-001 PREREGISTRATION         = FROZEN
GENERATOR IMPLEMENTATION       = FROZEN
R0 IMPLEMENTATION              = FROZEN
R_STAR IMPLEMENTATION          = FROZEN
BFS                             = FROZEN
COST COUNTER                    = FROZEN
BEACON NETWORK / SEED ENCODING = FROZEN
CALIBRATION BEACON              = NOT YET CAPTURED
CALIBRATION MANIFEST            = NOT YET MATERIALIZED
AVAILABLE-LEVERAGE CALIBRATION = NOT RUN
R_L LEARNER DESIGN             = NOT OPENED
R_L IMPLEMENTATION             = NONE
TEST SEED                       = UNAVAILABLE BY DESIGN
TEST INSTANCES                  = NOT GENERATED
```
