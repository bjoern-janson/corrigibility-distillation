# RD-001 — Pre-Calibration Audit v2

**Status:** `PASS / SCIENTIFIC CALIBRATION MAY OPEN / NO LEARNER DESIGNED / NO TEST SEED`

## 1. Frozen anchors

```text
preregistration
  bb0a85182a59a498568fa2905a49802af35b56b4

failed v1 implementation freeze
  4ffa3f7810baa8c3cc62e37de44b265114acd5d6

v1 pre-calibration audit failure
  85206fc996e2a3039a6662ba999d4072284f0b16

v2 source repair
  0ed228ec9ebc8008647136bf7380c3bd99c92f02

v2 implementation refreeze
  7d5fb20d73f47dab4d6dae72ad3ad16ad6443ea7

v2 selected beacon request
  e2b4fb441f0ae9d2a6aa5f9949725808c0f7b4e0

v2 raw beacon custody commit
  dbd0b253cbf43b65ece4fee939d623349e2b73cb

v2 seed derivation record
  f0efb372d3c1183f1a27cdf1a90db69669ebf125

v2 calibration-manifest freeze
  0d872a6d767c2ce94bba0de29d90e883d2230fde
```

RIL-003 remains untouched and frozen pre-reveal.

---

## 2. Source identity

Frozen scientific source:

`experiments/rd_001/rd001.py`

Git blob:

`76176ac583f12512ddfa0d7441fbb40ec4c7b077`

SHA-256 of exact UTF-8 source bytes:

`08cc82e528b400617c72e768811748b936315e3195c0658e374d3262799c95e2`

The v1-to-v2 scientific-source diff was audited as exactly:

```text
3 additions
1 deletion
```

corresponding only to:

1. reject any gate whose ordered `(u,v)` pair is already occupied by any edge;
2. reject any instance with duplicate ordered edge pairs;
3. assert the same invariant in the deterministic self-test.

`R0`, `R_STAR`, BFS policy, counter categories/weights, task parameters, trap rule, and scientific verdicts were not changed.

---

## 3. Beacon custody

Frozen drand chain hash:

`8990e7a9aaed2ffed73dbd7092123d6f289930540d7651336225dc172e51b2ce`

V2 implementation-refreeze timestamp:

`2026-08-24T20:51:01Z`

Unique first eligible round:

```text
round = 6405789
scheduled time = 2026-08-24T20:51:30Z
```

The round was selected and committed before its bytes were consumed.

Two frozen relays were then queried by a custody-only GitHub Actions transport job:

- `api.drand.sh` chain-hash endpoint;
- `drand.cloudflare.com` chain-hash endpoint.

The parsed beacon objects agreed exactly.

Captured randomness:

`24ee3fa7b7832d19d911e6cd510bba5e6a8e98977d72dd011a1412dac894a470`

Internal consistency check:

```text
SHA256(raw signature bytes) == randomness
PASS
```

The two relay raw-byte SHA-256 values differ because the JSON field serialization order differs; their parsed JSON objects are identical. Both raw byte strings are preserved in base64 in `RD001_CALIBRATION_BEACON_RAW_V2.json`.

No later beacon round was substituted.

---

## 4. Seed derivation

Frozen formula:

`SHA256(raw32(randomness) || raw20(prereg_commit) || UTF8("RD001/CAL"))`

Derived seed:

`1ee66660adc596f5d0104e3310f4dedb3602b4f5379eda13011c5519a3a17b6f`

No scientific arm result was computed before seed derivation or manifest materialization.

---

## 5. Manifest identity

Complete frozen calibration manifest:

`RD001_CALIBRATION_MANIFEST_V2.json`

Manifest freeze commit:

`0d872a6d767c2ce94bba0de29d90e883d2230fde`

Git blob:

`4fd841f85d6694c5cd3a397aa416490d42d571ba`

SHA-256 of exact manifest bytes:

`01f0211272291ad9c553a5cd7ff31128f981cd0e5892a97dc18484549b562d86`

A custody-only GitHub Actions job regenerated the manifest from the frozen v2 source and frozen CAL seed and refused to commit unless both of the following exact hashes matched:

```text
source   08cc82e528b400617c72e768811748b936315e3195c0658e374d3262799c95e2
manifest 01f0211272291ad9c553a5cd7ff31128f981cd0e5892a97dc18484549b562d86
```

Frozen suite diagnostics:

```text
role            = CAL
count           = 24
unique layouts  = 24
n counts        = {7:9, 8:7, 9:8}
k counts        = {3:12, 4:9, 5:3}
|J| counts      = {1:10, 2:14}
```

---

## 6. Full pre-calibration semantic audit

Using the exact frozen manifest and exact frozen v2 source, but **without invoking the scientific `calibrate` comparison**, the following were checked on all 24 instances:

1. exactly one edge per ordered `(u,v)` pair;
2. the designated safe pair has identical projection on `J`;
3. every irrelevant coordinate varies across the safe pair;
4. every relevant coordinate has both descriptor values represented;
5. every relevant coordinate has a corresponding gated native edge;
6. `R_STAR` preserves the designated future-consequence trap;
7. every native placement was exhaustively grouped by `R_STAR` key;
8. within every `R_STAR` key class, all native states have identical goal truth value;
9. within every `R_STAR` key class, all native states have identical sets of successor `R_STAR` keys;
10. both designated trap witness states are reachable from the native initial state.

Results:

```text
24 / 24 semantic audits                   = PASS
24 / 24 trap pairs                        = BOTH STATES REACHABLE
all enumerated native state spaces        = fully reachable
largest native state space exhaustively checked = 15120 placements
R_STAR congruence                         = PASS ON EVERY NATIVE PLACEMENT
```

No cost ratio, `delta C_search`, `delta C_fresh`, leverage vector, or gate verdict was inspected during this semantic audit.

---

## 7. Information-role audit

```text
R_L learner design         = NOT OPENED
R_L implementation         = NONE
Q_train scientific suite   = NOT MATERIALIZED
TEST beacon                = UNAVAILABLE BY DESIGN
TEST seed                  = UNAVAILABLE BY DESIGN
Q_test                     = NOT GENERATED
oracle J                   = evaluator-side only
scientific cost comparison = NOT RUN
```

The workflow files introduced after beacon-round selection are custody/transport utilities only. They do not alter or execute the scientific arm comparison and are not inputs to either representation arm.

---

## 8. Audit verdict

```text
GENERATOR CONSTITUTION       = PASS
R0 CONSTITUTION              = PASS
R_STAR SEMANTIC CONSTITUTION = PASS
BFS CONSTITUTION             = PASS
COST COUNTER FREEZE          = PASS
BEACON CUSTODY               = PASS
SEED DERIVATION              = PASS
MANIFEST FREEZE              = PASS
INFORMATION FIREWALL         = PASS FOR PRE-LEARNER CALIBRATION
PRE-CALIBRATION AUDIT        = PASS
```

The next and only now-permitted scientific operation is:

```text
python experiments/rd_001/rd001.py calibrate \
  --manifest RD001_CALIBRATION_MANIFEST_V2.json \
  --out RD001_CALIBRATION_RESULT_V2.json
```

If the available-leverage gate fails, RD-001 stops before learner design. If it passes, learner design becomes permitted but is not automatically opened by this audit.
