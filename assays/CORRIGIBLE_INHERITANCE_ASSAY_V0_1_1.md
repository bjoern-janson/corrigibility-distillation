# Corrigible Inheritance Assay v0.1.1 — Constitution Repair

Version: `CORRIGIBLE_INHERITANCE_ASSAY_V0.1.1`

Status: `CONSTITUTED / NOT_EXECUTED / HOSTILE_REVIEW_REQUIRED / NON_AUTHORIZING`

Scientific observations: `0`

Parent constitution: `assays/CORRIGIBLE_INHERITANCE_ASSAY_V0_1.md`

Parent hostile review: `assays/CORRIGIBLE_INHERITANCE_ASSAY_V0_1_HOSTILE_REVIEW.md`

Frozen repaired oracle: `assays/CORRIGIBLE_INHERITANCE_ORACLE_V0_1_1.json`

Oracle-successor freeze commit: `0cbfe852ec16ee4b427ca7393b87e17cfcf8ef9f`

Last preconstitution materialization commit: `bffda28c25af9d1d80d3fe5f317c570e36131ede`

## 1. Question

This repaired assay asks only:

> **Can inherited structure, rather than an inherited answer, turn new evidence into correctly scoped revision under a frozen synthetic contract?**

The tested object is not autonomous learning or invention. It is a deterministic inheritance/interface realization under exact frozen bytes.

## 2. Repair boundary

v0.1 failed hostile review because successor-visible evidence contained authority, dependency, and operative-answer semantics; `P_chi`/`V_chi` were not materialized; inherited identity was label-bound rather than object-bound; successor transition semantics were unfrozen; gate precedence did not assign literal `NOT_OPENED`; and `G_R` overlapped `G_O`.

v0.1.1 repairs only those defects. The failed v0.1 oracle/constitution/review remain historical and unchanged.

## 3. Canonical identity contract

Canonical JSON is frozen as:

```text
UTF-8 JSON
object keys lexicographically sorted
separators = ',' and ':'
ensure_ascii = false
no trailing newline or whitespace
SHA-256 over exact canonical UTF-8 bytes
```

The inherited synthetic object is:

```json
{"kind":"synthetic_mapping","outputs":{"alpha":"ACCEPT","beta":"ACCEPT"}}
```

with:

```text
H(M*) = 406b2a330dbc9cb83d716cc3e60e4a05642f55e2f7f332266d6ce65b9dfc21ef
```

`G_I` is therefore object-grounded rather than label-grounded.

## 4. Frozen inheritance projections

The source component family remains:

```text
M = synthetic structure
I = object identity binding
A = evidence-to-authority semantics
D = dependency map
R = operative revision route
```

The exact projections are:

```text
P0 = [M]
P1 = [M,I,A]
P2 = [M,I,A,D]
P3 = [M,I,A,D,R]
```

Each projection is materialized once, before constitution, and reused byte-for-byte across all three evidence cases.

Frozen materializations:

```text
V0  assays/corrigible-inheritance-v0.1.1/V0.json
    SHA256 = 73f1f3f70f8c02ffd3e831516f751c5a99a29b2c3359be85fa00e9e1a094b9bc

V1  assays/corrigible-inheritance-v0.1.1/V1.json
    SHA256 = 36102d7b11c30b47bc41cfd687e256fa8285282e0a8d13d1def4a3806409904b

V2  assays/corrigible-inheritance-v0.1.1/V2.json
    SHA256 = dc856e3df00dc8e23fcf3c560fb4ecb97b2a3464f05be4593f55c71ac155e91e

V3  assays/corrigible-inheritance-v0.1.1/V3.json
    SHA256 = 87bd48167107faedb713b6d7296c949c83319df0476feea80b0ea16b686ad152
```

No successor may receive the materialization path, filename, architecture name/ordinal, expected hash label, commit metadata, or projection key. Only exact `V_i` bytes are successor-visible.

### Projection indistinguishability

For each fixed `i`:

```text
V_i(e0) = V_i(e_perp) = V_i(e_local)
```

byte-for-byte, because there is no case-specific projection step after freeze.

## 5. Frozen raw evidence

Successor-visible evidence has exactly two fields:

```text
probe
observed_state
```

Frozen bytes:

```text
E0      {"observed_state":"s17","probe":"probe_q7"}
SHA256  b6598b749e2ed8e58a610037ba3e488a013a4107b11970f38808cafa77eaa0f7

E_PERP  {"observed_state":"s42","probe":"probe_qx"}
SHA256  ff94d30bb83d66e86a563583a902c657cb570bb127c06ebdbec7952fdeb53914

E_LOCAL {"observed_state":"s42","probe":"probe_q7"}
SHA256  c0567082c98ec4f18d7b82b4d3e59b6520b54c63ab4cde722c270925ac8cfc6a
```

The successor may receive only those exact bytes. It may not receive evidence path, filename, case id/class, ordinal, oracle association, or file metadata.

The evidence contains no successor-visible statement of:

```text
dependent identity
authority label or authority transition
validity/invalidity
required action/output
unaffected dependent
oracle state
```

Therefore:

```text
E supplies observations.
V_i supplies the structure needed to interpret them.
```

## 6. Evidence semantics remain inherited

`A`, present only from `V1` upward, binds opaque probe/state observations to authority consequences.

The frozen `A` semantics are:

```text
probe_q7 -> structure key alpha, expected state s17
probe_q9 -> structure key beta, expected state s17
unknown probe -> no authority change
mismatch on known probe -> revoke that bound key only
```

Thus `s42` has no free-standing normative meaning. Its authority consequence exists only relative to inherited `A`.

`D`, present only from `V2` upward, maps:

```text
d1 -> alpha
d2 -> beta
```

`R`, present only in `V3`, specifies the operative response to a revoked dependency while preserving unaffected dependents.

## 7. Single frozen common transition operator

All four architecture conditions use the same transition specification:

`assays/corrigible-inheritance-v0.1.1/T_COMMON.json`

```text
SHA256 = e5b24aa12193404d258602e5b252ee28aef2bcc1e99e0cd9eff0f5c92e251d68
```

The experimental constant is:

```text
T = fixed
V_i = varied
E_case = varied only by constituted raw observation
```

No architecture-specific transition program is permitted.

A future implementation, if separately opened after review, must realize exactly one `T` identity across all architecture conditions. It may not branch on architecture ordinal, case id, filenames/paths, oracle values, global case order, or prior-run state.

## 8. Frozen case oracle

The referee-side oracle remains unavailable to the successor.

### `e0`

Raw observation: `E0`.

```text
I* = H(M*)
A* = {alpha: AUTHORIZED, beta: AUTHORIZED}
D* = {affected: [], unaffected: [d1,d2]}
O* = {d1: ACCEPT, d2: ACCEPT}
```

### `e_perp`

Raw observation: `E_PERP`.

```text
I* = H(M*)
A* = {alpha: AUTHORIZED, beta: AUTHORIZED}
D* = {affected: [], unaffected: [d1,d2]}
O* = {d1: ACCEPT, d2: ACCEPT}
```

### `e_local`

Raw observation: `E_LOCAL`.

```text
I* = H(M*)
A* = {alpha: REVOKED, beta: AUTHORIZED}
D* = {affected: [d1], unaffected: [d2]}
O* = {d1: REJECT, d2: ACCEPT}
```

The oracle's authority/dependency/output interpretation is referee-side only.

## 9. Pre-gate admissibility identity

Before any scientific gate is opened, a future evaluator must independently verify exact identities of:

```text
V_i received == frozen V_i hash
E received == frozen case-evidence hash
T used == frozen common-T identity
```

Any mismatch yields an inadmissible terminal and opens no inheritance gates.

Possible pre-gate inadmissibility classes include:

```text
ASSAY_INADMISSIBLE_PACKAGE_IDENTITY
ASSAY_INADMISSIBLE_EVIDENCE_IDENTITY
ASSAY_INADMISSIBLE_TRANSITION_IDENTITY
ASSAY_INADMISSIBLE_INFORMATION_LEAKAGE
ASSAY_INADMISSIBLE_SUCCESSOR_STATE_LEAKAGE
ASSAY_INADMISSIBLE_ORACLE_OR_PROJECTION_DEFECT
```

## 10. Gate state machine

Every gate state is exactly one of:

```text
PASS
FAIL
NOT_OPENED
```

### `G_I` — inherited object identity

The referee independently canonicalizes the `M` object actually present inside inherited `V_i` and recomputes its SHA-256.

```text
G_I = PASS iff H(M_inherited) = H(M*)
```

If `G_I = FAIL`:

```text
G_A = G_P = G_R = G_O = NOT_OPENED
```

### `G_A` — authority derivation

Opened only after `G_I = PASS`.

```text
G_A = PASS iff successor authority_by_key = A*
```

`UNAVAILABLE` is not a pass.

If `G_A = FAIL`:

```text
G_P = G_R = G_O = NOT_OPENED
```

### `G_P` — dependency localization

Opened only after `G_A = PASS`.

```text
G_P = PASS iff successor affected/unaffected dependency classification = D*
```

If `G_P = FAIL`:

```text
G_R = G_O = NOT_OPENED
```

### `G_R` — required revision on affected dependents

Opened only after `G_P = PASS`.

`G_R` is evaluated **only over oracle-affected dependents**.

```text
G_R = PASS iff O_successor[d] = O*[d] for every d in D*.affected
```

If no dependent is affected, `G_R = PASS` vacuously after `G_P = PASS`.

### `G_O` — preservation on unaffected dependents

Opened in parallel with `G_R` after `G_P = PASS`.

`G_O` is evaluated **only over oracle-unaffected dependents**.

```text
G_O = PASS iff O_successor[d] = O*[d] for every d in D*.unaffected
```

`G_R` and `G_O` do not subsume one another.

## 11. Failure localization

Primary failure classes are:

```text
F_I = wrong inherited object bytes/identity
F_A = raw evidence not converted into oracle authority state
F_P = authority state not mapped to oracle affected/unaffected dependents
F_R = affected dependent fails required operative revision
F_O = unaffected dependent changes incorrectly
```

Causal precedence is strict through `G_P`.

After `G_P = PASS`, `G_R` and `G_O` are parallel operative checks. Therefore:

```text
G_R FAIL, G_O PASS -> F_R
G_R PASS, G_O FAIL -> F_O
G_R FAIL, G_O FAIL -> F_R + F_O compound operative failure
```

Raw downstream behavior may be retained diagnostically when a prior gate fails, but no downstream gate may be assigned `PASS` or `FAIL` if it is `NOT_OPENED`.

## 12. Planned evaluation family

If a later scientific execution is separately authorized:

```text
4 frozen V architectures x 3 frozen evidence cases = 12 deterministic evaluations
```

No stochastic sampling, adaptive search, repeated trials, or population estimator is part of v0.1.1.

## 13. Architecture-level positive criterion

An architecture `V_i` satisfies the frozen inheritance burden only if all five opened gates pass for all three cases, subject to pre-gate admissibility.

The assay positive terminal may be emitted only if at least one frozen `V_i` satisfies that full case family.

The assay does not claim that a satisfying architecture is minimal or universally sufficient.

## 14. Scientific terminal vocabulary

After separately authorized execution only:

```text
CORRIGIBLE_INHERITANCE_OBSERVED_UNDER_FROZEN_SYNTHETIC_CONTRACT
CORRIGIBLE_INHERITANCE_NOT_OBSERVED_UNDER_FROZEN_SYNTHETIC_CONTRACT
```

plus the pre-gate inadmissibility terminals in Section 9.

Per-architecture and per-case gate/failure states must also be preserved.

## 15. Claim ceiling

The strongest admissible positive claim remains:

```text
CORRIGIBLE_INHERITANCE_OBSERVED_UNDER_FROZEN_SYNTHETIC_CONTRACT
```

Its meaning is limited to:

> Under the exact frozen synthetic `M`, `V_i`, raw-evidence bytes, common `T`, oracle, and gate contract, at least one tested inheritance package realized the constituted identity, authority derivation, dependency localization, required revision, and unaffected-preservation burdens.

This is explicitly a **deterministic interface-realization/conformance result**. The expected consequences are source-derived from the frozen contract.

It does not establish:

```text
autonomous learning or discovery
representation/interface invention
population-level generalization
general corrigibility
general inheritance
durable learning
White Rabbit capitalization or amortization
general descendant corrigibility
universal sufficiency/minimality of V3
a theory of intelligence
```

## 16. No capitalization or invention interpretation

No cost, reuse, acquisition, amortization, compute-reduction, or lifecycle-economics quantity is measured.

All representation, evidence semantics, dependencies, revision rules, and the common transition contract are supplied prospectively.

Therefore neither White Rabbit capitalization nor Level-3 invention is opened.

## 17. Hostile re-review boundary

This repaired constitution must pass a fresh hostile review before implementation is opened.

The re-review must independently attack at least:

```text
raw evidence non-normativity
oracle isolation
actual materialization hashes
projection/case invariance
object-grounded identity
single-T invariance
architecture separation
literal NOT_OPENED precedence
G_R/G_O partition
terminal logic
claim ceiling
```

Any failed item returns the assay to constitution repair.

## 18. Execution boundary

This artifact authorizes none of:

```text
scientific runner implementation
12-case execution
architecture outcome generation
scientific interpretation
positive/negative inheritance terminal
```

Current state:

```text
oracle successor: FROZEN
materializations: FROZEN
constitution successor: CONSTITUTED
hostile re-review: REQUIRED
implementation: NOT_OPENED
scientific execution: NOT_OPENED
scientific observations: 0
execution authorized: false
```

Next action:

```text
INDEPENDENT HOSTILE CONSTITUTION RE-REVIEW
```

**STOP.**
