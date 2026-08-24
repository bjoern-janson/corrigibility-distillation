# RD-001 — Pre-Calibration Audit v1

**Status:** `IMPLEMENTATION AUDIT FAIL / SCIENTIFIC CALIBRATION NOT OPENED / NO LEARNER DESIGNED`

Audited implementation freeze:

`4ffa3f7810baa8c3cc62e37de44b265114acd5d6`

Audited source:

`experiments/rd_001/rd001.py`

Git blob:

`fc8408e5eaba924625b647ccebe81ea43165c0e6`

Previously selected calibration round under this now-failed freeze:

`6405769`

**No bytes from that round were consumed, no calibration manifest was generated, and no R0/R_STAR scientific comparison was executed.**

---

## 1. Audit purpose

The preregistered sequence requires constitution and audit of the generator, native semantics, oracle control, BFS, and counter before the available-leverage calibration is opened.

This audit used only non-scientific `DEV` seeds. It did not inspect any scientific calibration result.

---

## 2. Defect found

The v1 gate-placement code rejected a proposed gated edge only when an identical `FREE` edge object already existed:

```python
if u==v or Edge(u,v) in E: continue
```

Because the edge object's equality includes gate fields, two differently gated edges could rarely occupy the same ordered vertex pair `(u,v)` when `|J|=2`.

A DEV audit observed such an instance:

```text
n = 7
k = 5
J = (1,3)
ordered pair = (1,0)
parallel labels = B1=0 and B3=0
```

The preregistered primitive native action is only:

`MOVE(i, u -> v)`.

It contains no edge-label identifier. Therefore two differently gated edges at the same ordered pair create an ambiguity about which gate constitutes the action's admissibility.

The v1 path verifier compounded the ambiguity by scanning outgoing edges and selecting the first edge with destination `v`. A path produced through a later matching gated edge could therefore be checked against a different gate.

This is an implementation-semantic defect, not a scientific result.

---

## 3. Classification

```text
FAILURE LOCUS                    = MECHANISM / OPERATIONAL SEMANTICS
SCIENTIFIC CALIBRATION           = NOT OPENED
AVAILABLE-LEVERAGE VERDICT       = NONE
R_L LEARNER DESIGN               = NOT OPENED
R_L IMPLEMENTATION               = NONE
TEST SEED                        = UNAVAILABLE BY DESIGN
RIL-003                          = UNTOUCHED / PRE-REVEAL
```

The failure does **not** establish that the task family lacks representational leverage.

It establishes only that v1 did not unambiguously constitute the preregistered native action semantics.

---

## 4. Permitted minimal repair

Because the defect was found before any scientific calibration beacon was consumed or any calibration result observed, the v1 historical freeze remains preserved and a new implementation freeze may be created.

The minimal repair is:

1. enforce a simple directed labeled graph: at most one edge for each ordered `(u,v)` pair, irrespective of label;
2. reject any generated instance violating that invariant;
3. add the invariant to the deterministic self-test/audit surface;
4. leave the task family, descriptor construction, `R0`, `R_STAR`, BFS policy, cost weights, trap semantics, suite sizes, and scientific verdicts otherwise unchanged.

A repaired implementation must receive a **new implementation freeze timestamp** and therefore a new first-eligible calibration beacon round. Round `6405769` is permanently ineligible for the repaired implementation.

---

## 5. Additional DEV-only semantic checks

Before the repaired scientific freeze, a candidate containing only the minimal simple-edge repair was stress-tested on non-scientific DEV seeds.

For 12 varied generated instances spanning:

- `n in {7,8,9}`;
- `k in {3,4,5}`;
- `|J| in {1,2}`;
- native state spaces up to `15,120` placements;

an exhaustive congruence audit grouped **every native placement** by its `R_STAR` key and checked that all members of each key class had:

1. the same native goal truth value; and
2. the same set of successor `R_STAR` keys under native transitions.

Result:

```text
12 / 12 instances = PASS
```

The same DEV sample also checked reachability of both designated delayed-consequence trap states from the native initial state:

```text
12 / 12 trap pairs = BOTH STATES REACHABLE
```

These are implementation audits only. They are not evidence of available computational leverage and do not enter the scientific calibration.

---

## 6. Stop state

```text
V1 IMPLEMENTATION FREEZE         = PRESERVED / FAILED PRE-CALIBRATION AUDIT
V1 SELECTED BEACON ROUND         = 6405769 / NOT CONSUMED / RETIRED
SCIENTIFIC CALIBRATION           = NOT OPENED
REPAIR                           = PERMITTED ONLY AS NEW IMPLEMENTATION FREEZE
LEARNER                          = NOT DESIGNED
SCIENTIFIC RESULT                = NONE
```
