# RIL-001 — Terminal Result

Status: **`REPRESENTATION_INDUCED_LEVERAGE`**

Preregistration: `204fe919159145ac9c29f1becfb92b0c511af02b`  
Implementation freeze: `a0f8f795a805e8f579fd608fbcaa83dcfa6ef60f`  
Pre-execution audit: `6b3b865f3fce07fe835e169d80ec8f72f192f4bf`

## Terminal gate

```text
source integrity = PASS
A_fixed static = PASS
P1-P9 = PASS
A_fixed dynamic search equality = PASS
A_fixed dynamic update equality = PASS
C_op(R1) < C_op(R0) = PASS
memory(R1) <= memory(R0) = PASS
```

Therefore the exact preregistered terminal status is:

```text
REPRESENTATION_INDUCED_LEVERAGE
```

## Same correction

Both arms produced exactly the same scientific transformation:

```text
base empirical accuracy = 0.89
fanout empirical accuracy = 1.0
gain = 0.11
estimated repair value = 11.0
repair cost = 5.0
fanout_enabled = true
selected candidate = M1:126
selected canonical program = and(or(and(x,y),z),or(x,y))
held-out transfer accuracy = 1.0
construction rule after = fanout_allowed
goal_rule_mutated = false
authority_expanded = false
```

Every one of the 3,000 held-out predictions matched exactly. Prediction-vector SHA-256: `50bc66ed6fa692f9a0736de2f4b28792f89075caad3cf3820cf0c49bae0ae383`.

## Primary counted computational work

| Region | R0 AST | R1 SEM8 |
|---|---:|---:|
| translation | 64,727 | 64,737 |
| evaluation | 6,485,600 | 755,200 |
| search | 3,274,609 | 3,274,609 |
| update | 67 | 67 |
| **total `C_op`** | **9,825,003** | **4,094,613** |

The shared search and update regions are exactly equal, satisfying the dynamic `A_fixed` gate.

\[
\Lambda_F^{op}(R_0\to R_1)=\frac{9825003}{4094613}=2.399495.
\]

R1 uses **58.325% fewer counted CPython instruction events** overall. The evaluation primitive alone uses 8.588x fewer instruction events.

## Memory gate

```text
R0_AST peak incremental traced memory = 206,757 bytes
R1_SEM8 peak incremental traced memory = 206,757 bytes
delta = 0 bytes
```

The preregistered non-regression gate passes exactly.

## Confirmatory wall time

Fifteen fresh-process runs per arm, alternating order, no warm-up:

```text
R0_AST median = 48.193 ms
R1_SEM8 median = 19.712 ms
median ratio R0/R1 = 2.445x
```

Wall time is confirmatory only and did not determine the verdict.

## Earned claim

> **Under the exact frozen FS007 low-cost `NEEDS_FANOUT` function, condition, candidate languages, CPython implementation, and representation pair, changing only the operative representation from canonical AST evaluation to the parent's already-existing exact semantic tuple reduced counted computational work while preserving the correction's semantic identity, scope, required operations, and authority ceiling, with no increase in the preregistered peak-memory metric.**

This is one bounded existence witness for representation-induced computational leverage.

## Claim ceiling

RIL-001 does **not** establish family leverage, held-out representation-induced generality, resource-boundary amplification, a universal affordance geometry, a common corrigibility architecture, or any later RIL rung. `RIL-2` is **not opened** by this file.

## Stop

RIL-001 is terminal after publication of this result and final audit. No optimization or repair of the frozen apparatus is permitted under this assay identifier.
