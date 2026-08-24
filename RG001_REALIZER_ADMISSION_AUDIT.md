# RG-001 Realizer Admission Audit v0.1

**Object:** `RG001_REALIZER_ADMISSION_AUDIT_V0.1`  
**Admission contract:** `RG001_REALIZER_ADMISSION_CONTRACT_V0.1`  
**Contract freeze:** `426062c5baa32ea192b99b9a1c8de574eff6eb1e`  
**Status:** `FAIL / FUNCTION_EQUIVALENCE_NOT_CONSTITUTED`  
**RG-001 preregistration:** `NOT OPENED`  
**V_F / C_F / B_F:** `NOT RUN`

## 1. Scope

This audit asks only whether the two frozen candidate native surfaces can faithfully inhabit the already-frozen `F_LCC` case geometry through structure-preserving transport pairs

\[
T_r:X_F\rightarrow X_r,
\qquad
D_r:Y_r\rightarrow Y_F
\]

without adapter-side closure, route rescue, expected-result lookup, semantic kernel growth, or case-specific behavior.

No reference-oracle outcome was used to choose an adapter realization. No cost or robustness coordinate was measured.

## 2. Decisive frozen obligation

The admission death test is the already-frozen matched pair:

\[
C04:\mathcal Q(H)=\{\{G,w_a\}\}
\]

versus

\[
C05:\mathcal Q(H)=\{\{G\},\{w_a\}\}.
\]

The flattened parent-to-standing incidence is the same, but sufficient-support grouping differs.

A faithful admitted realizer must therefore retain, in its own operative semantics, the distinction between:

```text
one conjunctive support route
and
two independently sufficient alternative routes
```

The adapter may expose those routes. It may not compute the OR-of-routes consequence on behalf of the realizer.

## 3. SSI-CALC v0.1 admission

Frozen native source:

```text
repo    bjoern-janson/ssi
commit  362594d4337a1c72556b501b6477ff624db919e1
SPEC    research/ssi_calc/v0_1/SPEC.md
        blob ac443b2f616817977613bd32e1ba8fe5db7b3194
checker research/ssi_calc/v0_1/checker.py
        blob 293d373d13bd68b40ed2e5b0f8754146638981d6
```

### What the native surface supplies

SSI-CALC v0.1 is a typed **request/certificate adjudicator**. One case supplies objects, facts, authority edges, and one request; the checker runs the frozen R1-R11 pipeline and returns one certificate.

Its frozen rule kernel covers declaration, admission, licensing, equivalence, substitution, congruence, transport, quotient, composition, preservation, and reopening. Its own specification explicitly does not claim universal semantics.

The native surface can carry typed objects/facts and can check explicit conjunctive/compositional obligations when a matching frozen rule exists.

### Failure

There is no native operation in the frozen R1-R11 checker that takes an arbitrary family of sufficient support sets for one standing and maintains that standing as valid iff **any one** complete route remains effective after a primitive warrant withdrawal.

For C05, a transport can expose the two routes as separate facts/requests/authority structures, but obtaining the frozen standing-level consequence requires one of the following:

```text
run one native adjudication per route and OR the certificates in D_r
preselect the route that survives the known challenge
materialize a derived standing-validity fact outside R1-R11
add a new closure/alternative-support rule to SSI-CALC
```

All four are forbidden by the admission contract. The first and third make the decoder an `F_LCC` closure engine; the second is target/challenge-dependent rescue; the fourth changes the frozen realizer.

Therefore the first decisive failed gate is:

```text
A6_NATIVE_DEPENDENCY_CONSEQUENCE = FAIL
```

and specifically:

```text
A8_ALTERNATIVE_ROUTE_NON_ALIASING = FAIL
A14_NO_SEMANTIC_INVENTION         = FAIL
```

A pure `D_r` cannot recover the required C05 standing semantics from one native checker certificate without computing semantics absent from the frozen native surface.

Terminal:

\[
\boxed{A_{trans}^{RG}(SSI\!\mbox{-}CALC)=FAIL}
\]

```text
SSI-CALC = FUNCTION_EQUIVALENCE_NOT_CONSTITUTED
```

This does **not** mean SSI-CALC fails its own authority-transfer task or that `V_F=0`. `V_F` is not reached.

## 4. OpenCore Nano V0 admission

Frozen native source:

```text
repo    bjoern-janson/opencore
commit  d85aac9fa35ea4ba21afebc73b9cb8970c2a1dbf
spec    crank/NANO_V0.md
        blob 3a6becedc054ce474f1baee80510aa08ef9dac20
kernel  crank/nano.py
        blob d31dacaf893a58a8280c01704fe666a404c1f56c
```

### What the native surface supplies

Nano V0 is a semantically agnostic transition typechecker plus append-only journal. A `License` has a tuple of `Precondition`s; therefore a single license naturally represents conjunctive support.

Current standings are stored in `_current` as one `_Current` record per `StandingKey`, containing exactly one current `receipt_id` and one producing `license_id`. A receipt is effective only when its producing license remains active and **all** parent receipts remain effective. Parent receipts are collected from license preconditions.

This natively gives a clean conjunctive dependency lineage and transitive invalidation after upstream revocation.

### Failure

C04 is compatible with that native shape: one H-producing receipt can depend on both G and `w_a`.

C05 is not. Two alternative licenses can be *registered*, one supported by G and one by `w_a`, but one current H standing still has only one current producing receipt. Nano V0 contains no native multi-provenance current standing, OR-of-receipts effectiveness rule, or automatic failover from an invalidated current receipt to another independently sufficient license.

Possible repairs are all forbidden:

```text
choose the w_a route in advance because it survives the registered challenge
create route-specific shadow standings and OR them in D_r
on G revocation, have the adapter re-issue H under the w_a license
change Nano to retain multiple live receipts per StandingKey
```

The first and third are adapter-side route rescue; the second makes the decoder the alternative-support semantics; the fourth changes the frozen realizer.

Therefore the first decisive failed gate is:

```text
A6_NATIVE_DEPENDENCY_CONSEQUENCE = FAIL
```

and specifically:

```text
A8_ALTERNATIVE_ROUTE_NON_ALIASING = FAIL
A14_NO_SEMANTIC_INVENTION         = FAIL
```

Terminal:

\[
\boxed{A_{trans}^{RG}(Nano)=FAIL}
\]

```text
OpenCore Nano V0 = FUNCTION_EQUIVALENCE_NOT_CONSTITUTED
```

This does **not** negate Nano V0's own frozen transition-contract result. It means only that the isolated Nano V0 surface cannot faithfully inhabit the externally constituted `F_LCC` support-hypergraph semantics under the registered adapter ceiling.

## 5. Gate summary

The shallowest shared failure is A6: native dependency consequence.

| Gate | SSI-CALC v0.1 | Nano V0 | Note |
|---|---|---|---|
| A1 source identity | PASS | PASS | exact commits/blobs pinned |
| A2 total structural transport | PASS | PASS | frozen objects/routes can be serialized/exposed |
| A3 no semantic mutation | PASS | PASS | no mutation required for structural encoding |
| A4 hyperedge preservation | PASS | PASS | grouping can be represented explicitly |
| A5 challenge locality | PASS | PASS | designated warrant can be represented as the local challenge object |
| A6 native dependency consequence | **FAIL** | **FAIL** | no native arbitrary OR-of-sufficient-routes standing semantics |
| A7-A13 | NOT REACHED | NOT REACHED | terminal failure already established |
| A14 no semantic invention | **FAIL** | **FAIL** | repairing A6/A8 requires adapter or kernel semantics |

A8 is recorded as a specific witness to A6 even though the sequential gate has already terminated.

## 6. Terminal adjudication

The preregistration gate required:

\[
A_{trans}^{RG}(SSI\!\mbox{-}CALC)=PASS
\land
A_{trans}^{RG}(Nano)=PASS.
\]

Observed:

\[
\boxed{
A_{trans}^{RG}(SSI\!\mbox{-}CALC)=FAIL,
\qquad
A_{trans}^{RG}(Nano)=FAIL.
}
\]

Therefore:

```text
RG-001 REALIZER ADMISSION       FAIL
FUNCTION_EQUIVALENCE            NOT CONSTITUTED
RG-001 PREREGISTRATION          NOT OPENED
V_F                             NOT RUN
C_F                             NOT RUN
B_F                             NOT RUN
A_F                             NA
```

No adapter repair is authorized under RG-001 v0.1. Any future experiment that changes either native realizer, adds a closure layer, weakens `F_LCC`, or changes the adapter ceiling requires a new assay identifier.

## 7. Earned claim

> Under the frozen `F_LCC` sufficient-support semantics and the frozen non-inventive adapter contract, neither SSI-CALC v0.1 nor isolated OpenCore Nano V0 constituted the required alternative-sufficient-support behavior at the native realizer layer. The main-line RG-001 comparison therefore terminates at realizer admission and does not reach function validity or realization-coordinate measurement.

This is a **translation/admission null**, not evidence that the two systems are generally incapable, not a common-core result, and not evidence about RIL-003.

> **Constitute the object first; admit the realizers second. If admission fails, stop before comparison.**
