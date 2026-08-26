# Corrigible Inheritance Assay v0.1 — Independent Hostile Constitution Review

Status: `REVIEW_FAIL / CONSTITUTION_REPAIR_REQUIRED / NOT_EXECUTED / NON_AUTHORIZING`

Reviewed frozen artifacts:

- `assays/CORRIGIBLE_INHERITANCE_ORACLE_V0_1.json`
- `assays/CORRIGIBLE_INHERITANCE_ASSAY_V0_1.md`

Oracle freeze commit: `829b8182831cfb7ff4d5b8c81aea1df9b7ed2f43`

Constitution commit: `fb5ac52b732045cd9d109e314a8092ee429fde31`

Scientific observations: `0`

Execution authorized: `false`

## Review terminal

```text
HOSTILE_CONSTITUTION_REVIEW_FAIL
CONSTITUTION_REPAIR_REQUIRED
IMPLEMENTATION_NOT_OPENED
SCIENTIFIC_EXECUTION_NOT_OPENED
```

The current v0.1 constitution must not proceed to implementation or execution.

## G1 — Oracle isolation / information flow

**FAIL.**

The oracle file is referee-side by declaration, but the successor-visible evidence channel currently leaks information that the architecture ladder is supposed to test as inherited structure.

For `e_local`, the visible event states:

```text
target = M0:d1
For dependent d1 only, the inherited authorization is revoked:
alpha must no longer be accepted.
No authority change is asserted for d2.
```

This exposes, through the evidence channel itself:

- the affected dependent (`d1`);
- the authority transition (`AUTHORIZED -> REVOKED`);
- the required operative change (`alpha` must no longer be accepted);
- the unaffected dependent status (`d2` unchanged).

Those facts overlap materially with `A*`, `D*`, `O*`, and the intended selective revision route.

`e_perp` likewise tells the successor that the event "carries no authority over M0 or its dependents," which supplies the authority classification that `G_A` is supposed to test.

Therefore the current visible evidence is not merely evidence from which authority must be derived; it partially contains the referee verdict.

Required repair: successor-visible events must be pre-authority evidence/state facts, not direct authority or operative instructions. The oracle may map those facts to `A*`, `D*`, and `O*`, but the successor may receive that mapping only through the inheritance architecture under test.

## G2 — Projection indistinguishability

**FAIL / NOT YET REVIEWABLE MECHANICALLY.**

The constitution requires an exact `P_chi` and exact serialized package `V_chi`, and requires byte-for-byte equality across cases whenever constitutionally available inherited information is identical.

However, the frozen artifacts specify only field membership:

```text
chi_0 = M
chi_1 = M + I + A
chi_2 = M + I + A + D
chi_3 = M + I + A + D + R
```

They do not freeze:

- an exact projection function;
- package schema;
- canonical serialization;
- exact package bytes;
- package hashes.

Thus `V_chi(c1) == V_chi(c2)` is currently a required property of a future implementation rather than a frozen constituted object. Architecture identity and hidden-channel absence cannot yet be reviewed at the byte boundary.

Required repair: prospectively freeze canonical `P_chi`, `V_chi` schema/serialization, and expected hashes or exact materialized package bytes before implementation.

## G3 — Ground-truth integrity

**FAIL.**

The current synthetic ground truth is too close to a restatement of the successor-visible instruction.

In `e_local`, the visible event already says the authorization is revoked and that `alpha` must no longer be accepted. The oracle then records:

```text
A*(d1) = REVOKED
O*(d1) = REJECT
```

This is internally consistent, but it does not cleanly discriminate whether the successor inherited authority/revision capacity or simply followed an explicit normative event.

The identity oracle is also under-bound:

```text
I* = { structure_id: M0 }
```

while `G_I` is intended to establish the identity of the actual inherited object carrying authority. A wrong or altered `M` that retains the label `M0` could satisfy the stated identity check unless exact bytes are independently bound.

Required repair:

- define visible evidence as non-normative evidence/state;
- keep authority/operative interpretation referee-side;
- bind `I*` to exact `M` bytes or a frozen cryptographic identity, not merely a label.

## G4 — Architecture separation

**FAIL.**

Two independent defects prevent clean separation.

First, the current `e_local` evidence supplies information intended to distinguish `chi_1`, `chi_2`, and `chi_3`. A successor can learn the affected dependent and required action directly from the event rather than through `D` and `R`. In the extreme, even `chi_0` could appear locally correct by following the event text.

Second, the assay freezes inheritance information sets but not the successor transition/operator that consumes them. A later implementation could choose a powerful generic interpreter, a narrow rule engine, or architecture-specific logic. Those choices could determine whether a given information set appears sufficient.

Therefore an observed architecture difference would not yet be uniquely attributable to inherited `I/A/D/R` information.

Required repair: constitute the successor transition semantics independently and prospectively. The operator must be identical across architecture conditions except for the inherited package, or each architecture-specific operator must itself be frozen as part of the tested object with an explicit claim ceiling.

## G5 — Gate precedence / failure localization

**FAIL.**

The constitution says downstream gates should not be interpreted or credited after an upstream failure, but it does not freeze a machine-level gate state of `NOT_OPENED`.

Required precedence is stronger:

```text
G_I = FAIL => G_A = G_P = G_R = G_O = NOT_OPENED
G_A = FAIL => G_P = G_R = G_O = NOT_OPENED
G_P = FAIL => G_R and G_O = NOT_OPENED
```

Raw downstream behavior may be preserved as non-authorizing diagnostic data, but downstream gate outcomes must not be assigned PASS/FAIL after the causal precondition is absent.

There is also overlap between `G_R` and `G_O`.

Current `G_R` is:

```text
O_successor == O*
```

over the full operative state. Therefore if `d1` is correctly revised but `d2` is incorrectly changed, `G_R` already fails. `G_O` then fails again. Under shallowest-failure precedence, `F_O` cannot cleanly become the primary locus.

Required repair:

```text
G_R = required operative change on affected dependents only
G_O = preservation on unaffected dependents only
```

or freeze another non-overlapping partition with equivalent identifiability.

## G6 — Over-revision / claim ceiling

**MIXED: claim ceiling PASS; over-revision adjudication FAIL pending G5 repair.**

The explicit nonclaims and positive claim ceiling are appropriately narrow. The assay does not claim White Rabbit capitalization, invention, general corrigibility, general inheritance, universal `chi_3` sufficiency, or a theory of intelligence.

However, because `G_R` and `G_O` overlap, the promised failure distinction between under-revision and over-revision is not currently cleanly realized.

After repairing the gate partition, the local contradiction design remains a strong control because it requires:

```text
affected dependent changes
AND
unaffected dependent remains unchanged
```

The claim ceiling should otherwise remain unchanged.

## G7 — Execution non-authorization

**PASS.**

The review found no scientific runner or executable assay implementation in the PR. The changed files at the review boundary are Markdown/JSON/bookkeeping artifacts only.

All frozen authority surfaces state:

```text
scientific observations = 0
execution authorized = false / NONE
```

The constitution explicitly forbids implementation acquiring scientific authority before hostile review and requires a separate later authorization before scientific execution.

Therefore:

```text
NON_AUTHORIZING != EXECUTION_READY
```

is currently preserved.

## Required constitution repair set

Before hostile re-review, repair at least the following:

1. Replace direct normative successor-visible evidence with pre-authority evidence/state facts.
2. Freeze exact `P_chi` and canonical `V_chi` serialization/materialization, with immutable identities.
3. Hash-bind the exact inherited `M` at `G_I`.
4. Prospectively constitute the successor transition/operator so architecture sufficiency is attributable to inherited information rather than post-freeze implementation choice.
5. Make gate states explicitly `PASS / FAIL / NOT_OPENED` with causal precedence.
6. Split affected-dependent operative revision (`G_R`) from unaffected-dependent preservation (`G_O`).
7. Re-review oracle isolation and architecture separation after those repairs.

No implementation work is opened by this review.

## Current authority state

```text
artifact: CORRIGIBLE_INHERITANCE_ASSAY_V0.1
oracle: FROZEN_HISTORICAL_INPUT
constitution: REVIEW_FAILED
scientific observations: 0
implementation: NOT_OPENED
execution: NOT_OPENED
execution authorized: false
next action: CONSTITUTION_REPAIR
```

**STOP.**
