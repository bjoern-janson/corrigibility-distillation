# RIL-002 — Terminal Family-Transfer Result

Status: **`FAMILY_WIDE_LEVERAGE`**

Family freeze: `d35d998eea7e9b06ae0516dbcb9019955052ef6f`  
Implementation freeze: `d46dffe2b76c910470223d7f49c6e983ee39b873`  
Pre-execution audit: `8cd6b830f82f93717b4b6f42f768135a2e8f816d`  
Parent RIL-001 result: `a8dfb2aa7e72b5f28c497bbe071408c9be0113a3`

## Terminal gates

```text
frozen family members                         24
A_fixed static/global                         PASS
P_i                                            PASS 24/24
dynamic c_search equality                     PASS 24/24
dynamic c_update equality                     PASS 24/24
Lambda_i^op > 1                               PASS 24/24
memory non-regression                         PASS 24/24
selected frozen canonical target identity     PASS 24/24
held-out transfer accuracy = 1.0               PASS 24/24
```

Therefore the preregistered family status is:

```text
FAMILY_WIDE_LEVERAGE
```

The finite-family coverage quantities are:

```text
kappa_F^op       = 1.0
full_RIL_coverage = 1.0
```

These are coverage fractions for the exact frozen 24-member family, not population probabilities.

## Ordered leverage vector

The primary family object is the ordered vector, not its mean:

| Member | C_op R0 | C_op R1 | Lambda_op |
|---|---:|---:|---:|
| TT_1B | 9,746,823 | 4,094,433 | 2.380506165323 |
| TT_1D | 9,746,817 | 4,094,427 | 2.380508188325 |
| TT_27 | 9,746,799 | 4,094,409 | 2.380514257369 |
| TT_2E | 9,728,655 | 4,094,265 | 2.376166418148 |
| TT_35 | 9,746,775 | 4,094,385 | 2.380522349510 |
| TT_3A | 9,728,623 | 4,094,233 | 2.376177174089 |
| TT_47 | 9,746,831 | 4,094,441 | 2.380503467995 |
| TT_4E | 9,728,679 | 4,094,289 | 2.376158351303 |
| TT_53 | 9,746,831 | 4,094,441 | 2.380503467995 |
| TT_5C | 9,728,683 | 4,094,293 | 2.376157006839 |
| TT_72 | 9,728,683 | 4,094,293 | 2.376157006839 |
| TT_74 | 9,728,603 | 4,094,213 | 2.376183896637 |
| TT_8B | 9,746,627 | 4,094,237 | 2.380572253145 |
| TT_8D | 9,746,623 | 4,094,233 | 2.380573601942 |
| TT_A3 | 9,746,693 | 4,094,303 | 2.380549998376 |
| TT_AC | 9,797,383 | 4,093,993 | 2.393111810401 |
| TT_B1 | 9,746,651 | 4,094,261 | 2.380564160419 |
| TT_B8 | 9,797,411 | 4,094,021 | 2.393102282573 |
| TT_C5 | 9,746,583 | 4,094,193 | 2.380587090057 |
| TT_CA | 9,797,411 | 4,094,021 | 2.393102282573 |
| TT_D1 | 9,746,663 | 4,094,273 | 2.380560114091 |
| TT_D8 | 9,797,395 | 4,094,005 | 2.393107727030 |
| TT_E2 | 9,797,453 | 4,094,063 | 2.393087991074 |
| TT_E4 | 9,797,399 | 4,094,009 | 2.393106365912 |

Descriptive vector range:

```text
min Lambda_op    = 2.376157006839
median Lambda_op = 2.380536173943
max Lambda_op    = 2.393111810401
```

No member-level failure was averaged away.

## Preservation and scientific identity

For every member, both arms used the inherited RIL-001 representation pair unchanged:

```text
R0 = R0_AST
R1 = R1_SEM8
```

Every member passed the full preservation predicate before its leverage was interpreted. For all 24 members:

- the same candidate sets/order and exhaustive search policy were used;
- per-candidate semantics and probe scores matched across arms;
- the same M0/M1 winners, repair decision, selected semantic function, and canonical program were obtained;
- the selected canonical M1 program exactly matched the program frozen in `RIL_002_FAMILY.json`;
- all 3,000 held-out predictions matched across arms;
- held-out transfer accuracy was exactly `1.0` in both arms;
- `goal_rule_mutated = false` and `authority_expanded = false`;
- dynamic search and update instruction counts were arm-equal.

The inherited memory gate also passed for every member:

```text
R0 peak incremental traced memory = 206,709 bytes
R1 peak incremental traced memory = 206,709 bytes
```

## Earned claim

> **Across the exact prospectively frozen 24-member RIL-002 family, the same AST→SEM8 representation change inherited unchanged from RIL-001 reduced counted computational work for every member while preserving each correction's semantic identity, scope, required operations, authority ceiling, and memory non-regression gate.**

This earns **bounded family transfer of representation-induced computational leverage**.

## Claim ceiling

RIL-002 does **not** establish provenance-separated generalization. The representation pair was selected with knowledge of FS007 structure before this family-transfer assay. It also does not establish resource-boundary amplification, broad effective generality, or a universal affordance geometry.

Therefore:

```text
RIL-002 = FAMILY_WIDE_LEVERAGE, CLOSED
RIL-3   = NOT OPENED
```

## Execution interruption provenance

The initial fresh-process resource batch exceeded the shell execution timeout after several completed members. Completed result files were left unchanged. Execution resumed only for missing member/arm resource files; no apparatus changed and no completed record was overwritten. Scientific values were not interpreted until the full matrix was complete and the dynamic fixed-algorithm equality gate had been checked.

## Stop

No optimization, repair, member replacement, or representation redesign is permitted under `RIL-002` after this terminal result.