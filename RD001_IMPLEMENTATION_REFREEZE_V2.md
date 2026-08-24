# RD-001 — Pre-Learner Implementation Refreeze v2

**Status:** `V2 IMPLEMENTATION FROZEN / PRE-CALIBRATION / NO LEARNER DESIGNED / NO TEST SEED`

**Preregistration:** `bb0a85182a59a498568fa2905a49802af35b56b4`  
**Preserved failed v1 freeze:** `4ffa3f7810baa8c3cc62e37de44b265114acd5d6`  
**v1 audit failure record:** `85206fc996e2a3039a6662ba999d4072284f0b16`  
**v2 source repair commit:** `0ed228ec9ebc8008647136bf7380c3bd99c92f02`  
**RIL-003:** `UNTOUCHED / FROZEN PRE-REVEAL`

This is a new implementation freeze created before any scientific RD-001 calibration beacon was consumed or any scientific `R0/R_STAR` result observed.

The only semantic repair relative to v1 is enforcement of a simple directed labeled graph: one edge at most for each ordered `(u,v)` pair, independent of edge label, plus an explicit generator-validity and self-test assertion of that invariant.

No task-family parameter, suite size, descriptor rule, `R0` definition, `R_STAR` equivalence criterion, BFS policy, trap criterion, cost-counter category/weight, scientific gate, or learner constraint was changed in response to performance evidence. No performance evidence existed.

---

## 1. Frozen source identity

Path:

`experiments/rd_001/rd001.py`

v2 Git blob:

`76176ac583f12512ddfa0d7441fbb40ec4c7b077`

SHA-256 of the exact UTF-8 v2 source bytes at authoring/audit time:

`08cc82e528b400617c72e768811748b936315e3195c0658e374d3262799c95e2`

The source remains Python-standard-library-only and contains no `R_L` learner implementation or learner design.

---

## 2. v2 repair invariant

For every accepted generated instance:

```text
len({(edge.u, edge.v) for edge in edges}) == len(edges)
```

Gate placement rejects a candidate ordered pair whenever **any** edge already occupies that pair, regardless of label.

This makes the preregistered primitive action:

`MOVE(i, u -> v)`

unambiguous with respect to the unique edge label on `(u,v)`.

The invariant is checked by both the candidate-validity gate and the deterministic DEV self-test.

---

## 3. Frozen scientific apparatus inherited unchanged

Except for Section 2, v2 inherits the frozen v1 constitution verbatim in scientific role:

- finite identity-sensitive token planning family;
- `p=4`, `n in {7,8,9}`, `k in {3,4,5}`;
- hidden relevant descriptor subset `J`, `|J| in {1,2}`;
- safe-to-collapse and future-consequential descriptor distinctions;
- identity-invariant goals;
- deterministic SHA-256 counter-mode generator PRNG;
- `R0` native identity-sensitive key;
- `R_STAR` exact descriptor projection on evaluator-only `J` followed by within-class position canonicalization;
- concrete-native-state BFS with only the visited key differing by arm;
- native replay verification;
- unit-weight abstract event counter;
- `C_fresh = C_instantiate + C_search + C_verify`;
- exact structural state-space diagnostic reported separately from cost;
- designated delayed-consequence trap preservation requirement;
- no learner design before the available-leverage gate passes.

The v1 implementation contract remains historical evidence of the failed pre-calibration freeze and is not rewritten.

---

## 4. DEV-only semantic audit before v2 scientific freeze

No scientific seed was used.

### Deterministic self-test

The v2 source passed:

```text
RD001 SELFTEST PASS
```

using only the fixed non-scientific string `RD001 NONSCIENTIFIC SELFTEST`.

### Exhaustive `R_STAR` congruence audit

On 12 additional DEV-only generated instances spanning all allowed vertex counts, token counts represented in the sample, both `|J|` values, and native state spaces up to 15,120 placements, every native placement was exhaustively grouped by `R_STAR` key.

For every key class, the audit required:

1. identical native goal truth value for all class members; and
2. identical sets of successor `R_STAR` keys under native transitions.

Result:

```text
12 / 12 = PASS
```

### Trap reachability audit

For those same 12 DEV instances, the complete native reachable-state graph from the initial state was enumerated and both designated trap witness states were checked for reachability.

Result:

```text
12 / 12 = BOTH TRAP STATES REACHABLE
```

These checks validate semantic constitution only. No `R_STAR/R0` cost ratio from them is admitted as scientific evidence or used to tune v2.

---

## 5. Frozen beacon network and seed encoding

The v2 scientific calibration retains the previously frozen League of Entropy drand default mainnet identity:

```text
chain_hash = 8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce
genesis    = 1595431050
period     = 30 seconds
```

For round `r >= 1`:

`T(r) = 1595431050 + 30*(r-1)`.

Let `t_v2_freeze` be the UTC committer timestamp of the Git commit that adds this v2 refreeze artifact.

The only eligible v2 calibration round is the unique first round satisfying:

`T(r) > t_v2_freeze`.

The v1-selected round `6405769` is retired and may not be reused.

The calibration seed encoding remains exactly:

`SHA256(raw32(drand_randomness) || raw20(prereg_commit) || UTF8("RD001/CAL"))`

where:

`prereg_commit = bb0a85182a59a498568fa2905a49802af35b56b4`.

No fallback network, later favorable round, or changed byte encoding is permitted.

---

## 6. v2 execution order

After this v2 refreeze commit exists:

1. obtain its UTC committer timestamp;
2. calculate and record the unique first eligible drand round **before obtaining that round's bytes**;
3. capture the exact official beacon package for that round;
4. verify round identity, relay provenance, and `randomness = SHA256(signature)` internal consistency;
5. derive the calibration seed exactly once;
6. materialize exactly 24 `CAL` instances with the frozen v2 source;
7. commit the complete calibration manifest before executing the scientific arm comparison;
8. perform a pre-calibration custody/constitution audit;
9. execute `R0` and `R_STAR` under the frozen counter;
10. publish complete raw per-instance records before interpretation.

No `TRAIN` suite, `R_L`, test seed, or test instance may be opened as part of this calibration.

---

## 7. Available-leverage gate

The preregistered gate is unchanged:

```text
all R_STAR native correctness bits = 1
all R_STAR trap-preservation bits  = 1
sum C_fresh(R_STAR) < sum C_fresh(R0)
```

If false:

`AVAILABLE_LEVERAGE_NOT_DEMONSTRATED / LEARNER_NOT_DESIGNED`.

If true:

`AVAILABLE_LEVERAGE_DEMONSTRATED`.

A pass permits learner design as a later phase; it does not itself constitute a learned-representation result.

---

## 8. Stop state at v2 freeze

```text
RD-001 PREREGISTRATION          = FROZEN
V1 IMPLEMENTATION               = PRESERVED / AUDIT FAIL / RETIRED
V1 BEACON ROUND 6405769         = RETIRED / NOT CONSUMED
V2 GENERATOR                    = FROZEN
V2 R0                           = FROZEN
V2 R_STAR                       = FROZEN
V2 BFS                          = FROZEN
V2 COST COUNTER                 = FROZEN
V2 SEMANTIC DEV AUDIT           = PASS
V2 CALIBRATION ROUND            = NOT YET SELECTED
V2 CALIBRATION BEACON BYTES     = NOT CAPTURED
V2 CALIBRATION MANIFEST         = NOT MATERIALIZED
AVAILABLE-LEVERAGE CALIBRATION = NOT RUN
R_L LEARNER DESIGN              = NOT OPENED
R_L IMPLEMENTATION              = NONE
TEST SEED                       = UNAVAILABLE BY DESIGN
TEST INSTANCES                  = NOT GENERATED
SCIENTIFIC RESULT               = NONE
```
