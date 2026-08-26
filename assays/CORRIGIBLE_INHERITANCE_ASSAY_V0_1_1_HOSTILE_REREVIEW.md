# Corrigible Inheritance Assay v0.1.1 — Hostile Technical Re-review

Status: `HOSTILE_TECHNICAL_REREVIEW_PASS / REVIEWER_INDEPENDENCE_NOT_ESTABLISHED / NOT_EXECUTED / NON_AUTHORIZING`

Scientific observations: `0`

Implementation: `NOT_OPENED`

Scientific execution: `NOT_OPENED`

Execution authorized: `false`

Reviewed repaired artifacts:

- `assays/CORRIGIBLE_INHERITANCE_ORACLE_V0_1_1.json`
- `assays/CORRIGIBLE_INHERITANCE_ASSAY_V0_1_1.md`
- `assays/corrigible-inheritance-v0.1.1/V0.json`
- `assays/corrigible-inheritance-v0.1.1/V1.json`
- `assays/corrigible-inheritance-v0.1.1/V2.json`
- `assays/corrigible-inheritance-v0.1.1/V3.json`
- `assays/corrigible-inheritance-v0.1.1/E0.json`
- `assays/corrigible-inheritance-v0.1.1/E_PERP.json`
- `assays/corrigible-inheritance-v0.1.1/E_LOCAL.json`
- `assays/corrigible-inheritance-v0.1.1/T_COMMON.json`

Oracle-successor freeze commit: `0cbfe852ec16ee4b427ca7393b87e17cfcf8ef9f`

Last preconstitution materialization commit: `bffda28c25af9d1d80d3fe5f317c570e36131ede`

Constitution-successor commit: `d7dec5ccc055ba3275fb75cd6998dff28ee798b9`

## Review terminal

```text
SUBSTANTIVE_HOSTILE_REREVIEW: PASS
INDEPENDENT_REVIEW_GATE: NOT_SATISFIED
IMPLEMENTATION: NOT_OPENED
SCIENTIFIC_EXECUTION: NOT_OPENED
SCIENTIFIC_OBSERVATIONS: 0
```

The v0.1.1 repair resolves the constitution defects identified by the v0.1 hostile review at the specification/materialization layer. However, this re-review was performed by the same assistant workflow that authored the repair. It therefore does **not** claim reviewer independence and does not satisfy the constitution's independent-review gate.

## R1 — Raw evidence non-normativity

**PASS.**

The exact successor-visible raw evidence values are:

```text
E0      = {"observed_state":"s17","probe":"probe_q7"}
E_PERP  = {"observed_state":"s42","probe":"probe_qx"}
E_LOCAL = {"observed_state":"s42","probe":"probe_q7"}
```

They contain no dependent identifier, authority label/transition, valid/invalid judgment, required action/output, unaffected-dependent statement, case id/class, or oracle result.

The original v0.1 answer-key leak is absent.

The opaque state token `s42` has no free-standing normative meaning. `E_LOCAL` becomes authority-relevant only through inherited `A`, which maps `probe_q7` to `alpha`, identifies `s17` as the expected state, and freezes mismatch semantics.

Therefore the constituted path is now:

```text
raw E -> inherited A semantics -> authority state
```

rather than:

```text
normative instruction -> obedience
```

## R2 — Projection materialization / case indistinguishability

**PASS at the frozen-byte layer.**

Each `V_i` is materialized exactly once before constitution and reused across every case. No case-specific projection occurs after freeze.

Observed materializations contain only the constituted component subsets:

```text
V0 = M
V1 = M + I + A
V2 = M + I + A + D
V3 = M + I + A + D + R
```

No `V_i` contains case id/class, evidence content, oracle state, architecture ordinal/name, or harness metadata.

Thus for fixed `i`:

```text
V_i(e0) = V_i(e_perp) = V_i(e_local)
```

by construction.

Frozen canonical SHA-256 identities are:

```text
V0 = 73f1f3f70f8c02ffd3e831516f751c5a99a29b2c3359be85fa00e9e1a094b9bc
V1 = 36102d7b11c30b47bc41cfd687e256fa8285282e0a8d13d1def4a3806409904b
V2 = dc856e3df00dc8e23fcf3c560fb4ecb97b2a3464f05be4593f55c71ac155e91e
V3 = 87bd48167107faedb713b6d7296c949c83319df0476feea80b0ea16b686ad152
```

Frozen evidence identities are:

```text
E0      = b6598b749e2ed8e58a610037ba3e488a013a4107b11970f38808cafa77eaa0f7
E_PERP  = ff94d30bb83d66e86a563583a902c657cb570bb127c06ebdbec7952fdeb53914
E_LOCAL = c0567082c98ec4f18d7b82b4d3e59b6520b54c63ab4cde722c270925ac8cfc6a
```

Future implementation must still prove that only file **bytes**, not filenames/paths/metadata, cross the successor boundary. That is an implementation-review burden, not an unresolved constitution ambiguity.

## R3 — Ground-truth / object identity

**PASS.**

`I*` no longer consists merely of the label `M0`.

The frozen object is canonically:

```text
{"kind":"synthetic_mapping","outputs":{"alpha":"ACCEPT","beta":"ACCEPT"}}
```

with:

```text
H(M*) = 406b2a330dbc9cb83d716cc3e60e4a05642f55e2f7f332266d6ce65b9dfc21ef
```

`G_I` requires referee-side recomputation of the actual inherited `M` subobject. A mutated object retaining the label `M0` does not satisfy the gate.

## R4 — Common transition / architecture separation

**PASS at the constituted transition-specification layer.**

One common transition specification is frozen:

```text
T_COMMON SHA256 = e5b24aa12193404d258602e5b252ee28aef2bcc1e99e0cd9eff0f5c92e251d68
```

and the constitution requires:

```text
T = fixed
V_i = varied
```

The transition specification consumes only component presence/content and raw evidence. It forbids case id, evidence filename/path, architecture name/ordinal, oracle state, global case order, prior-run state, or other harness information.

The repaired information path is separable:

```text
A: raw probe/state -> authority by structure key
D: structure key -> affected/unaffected dependent
R: affected authority state -> operative revision
```

Therefore `E` no longer bypasses `A`, `D`, or `R`.

Important claim ceiling: because `T`, `A`, `D`, and `R` are all prospectively supplied and deterministic, the architecture outcome pattern is substantially source-derived. A later execution is therefore a deterministic interface-realization/conformance test, not discovery of autonomous corrigibility or learned correction semantics.

### Future implementation identity burden

No executable `T` exists yet. Therefore no `H(T_impl)` can or should be claimed at this stage.

If implementation is later opened, implementation review must freeze one exact implementation identity and establish:

```text
same H(T_impl) across V0,V1,V2,V3
```

plus conformance to the frozen `T_COMMON` specification before scientific execution can open.

This future burden does not invalidate the current constitution because implementation remains `NOT_OPENED`.

## R5 — Literal gate precedence

**PASS.**

The repaired constitution uses the exact gate states:

```text
PASS / FAIL / NOT_OPENED
```

and freezes:

```text
G_I FAIL => G_A,G_P,G_R,G_O NOT_OPENED
G_A FAIL => G_P,G_R,G_O NOT_OPENED
G_P FAIL => G_R,G_O NOT_OPENED
```

Raw downstream behavior may be retained diagnostically but cannot acquire a downstream gate result when the causal prerequisite failed.

This repairs the v0.1 "do not credit/interpret" ambiguity.

## R6 — Required revision vs over-revision

**PASS.**

`G_R` and `G_O` are now disjoint:

```text
G_R evaluates only D*.affected
G_O evaluates only D*.unaffected
```

After `G_P = PASS`, they open in parallel.

Therefore the local case can distinguish:

```text
G_R FAIL, G_O PASS -> F_R
G_R PASS, G_O FAIL -> F_O
G_R FAIL, G_O FAIL -> F_R + F_O
```

Under-revision and collateral over-revision are no longer double-counted through a full-state `G_R` equality test.

## R7 — Controls / local contradiction

**PASS for the stated deterministic purpose.**

The case family retains three distinct burdens:

```text
E0: expected observation on a known probe
E_PERP: mismatching observation on an unknown probe
E_LOCAL: mismatching observation on a known probe
```

Because the observation tokens themselves are non-normative, the controls discriminate:

```text
always revise
never revise
revise only under inherited evidence-authority semantics
```

The local oracle still requires selective change:

```text
d1 -> REJECT
d2 -> ACCEPT
```

without exposing that answer in the evidence bytes.

## R8 — Terminal logic / claim ceiling

**PASS.**

The positive terminal remains:

```text
CORRIGIBLE_INHERITANCE_OBSERVED_UNDER_FROZEN_SYNTHETIC_CONTRACT
```

but its meaning is now explicitly restricted to deterministic realization/conformance under the exact frozen synthetic contract.

The constitution explicitly denies autonomous learning/discovery, invention, population generalization, general corrigibility/inheritance, White Rabbit capitalization/amortization, universal V3 minimality/sufficiency, and a theory of intelligence.

No stronger claim is earned by a future pass.

## R9 — Execution non-authorization

**PASS.**

The PR contains no scientific runner or executable assay implementation. The repaired additions are oracle/constitution/materialization/specification artifacts only.

Current authority remains:

```text
implementation = NOT_OPENED
scientific execution = NOT_OPENED
scientific observations = 0
execution authorized = false
```

No 12-case run is permitted by this review.

## R10 — Reviewer independence

**NOT ESTABLISHED.**

This technical re-review was performed within the same assistant workflow that authored the v0.1.1 repair. It is adversarial in method but not independent in reviewer provenance.

Therefore it must not be represented as satisfying the constitution's requirement for an **independent** hostile review.

A distinct reviewer/review process must inspect the exact v0.1.1 frozen artifacts before implementation can be opened.

## Current authority state

```text
artifact: CORRIGIBLE_INHERITANCE_ASSAY_V0.1.1
oracle successor: FROZEN
materializations: FROZEN
constitution successor: CONSTITUTED
substantive hostile technical re-review: PASS
independent review gate: NOT_SATISFIED
implementation: NOT_OPENED
scientific execution: NOT_OPENED
scientific observations: 0
execution authorized: false
next action: INDEPENDENT HOSTILE REVIEW OF V0.1.1
```

**STOP.**
