# RG-001 Realizer Admission Contract v0.1

**Object:** `RG001_REALIZER_ADMISSION_CONTRACT_V0.1`  
**Status:** `FROZEN_ADMISSION_CONTRACT / ADAPTERS_NOT_YET_CONSTITUTED`  
**Semantic parent:** `F_LCC_SEMANTIC_CONSTITUTION_V0.1`  
**Case family:** `RG001_CASE_FAMILY_V0.1`  
**Realizers named:** SSI-CALC v0.1 reference checker; OpenCore Nano V0  
**Validity/cost/robustness execution:** `NOT AUTHORIZED BY THIS ARTIFACT`

## 1. Sole question

For each candidate realizer `r`, independently:

\[
\boxed{\text{Can }r\text{ faithfully inhabit the already-frozen }F_{\mathrm{LCC}}?}
\]

Constitute a transport pair

\[
T_r:X_F\rightarrow X_r,
\qquad
D_r:Y_r\rightarrow Y_F
\]

without changing `F_LCC`, changing the eight-case family, reading reference-oracle outcomes, or implementing missing semantic closure inside the adapter.

This is an **admission/translation gate**, not the RG-001 validity experiment.

## 2. Frozen semantic inputs

The adapter must inherit, without modification:

```text
RG001_F_LCC_SEMANTIC_CONSTITUTION.md
RG001_CASE_FAMILY.json
experiments/rg_001/reference_evaluator.py
experiments/rg_001/test_reference_evaluator.py
RG001_CASE_FAMILY_AUDIT.md
```

The decisive matched pair remains:

\[
\boxed{C04:\mathcal Q(H)=\{\{G,w_a\}\}}
\]

versus

\[
\boxed{C05:\mathcal Q(H)=\{\{G\},\{w_a\}\}}.
\]

After withdrawal of `G`'s warrant, the frozen semantics require:

```text
C04: H contracts
C05: H survives
```

A representation that aliases this pair is inadmissible.

## 3. Frozen candidate source surfaces

### SSI-CALC

Repository: `bjoern-janson/ssi`  
Commit: `362594d4337a1c72556b501b6477ff624db919e1`

Admitted native surface for adapter constitution:

```text
research/ssi_calc/v0_1/SPEC.md
  git blob ac443b2f616817977613bd32e1ba8fe5db7b3194
research/ssi_calc/v0_1/checker.py
  git blob 293d373d13bd68b40ed2e5b0f8754146638981d6
```

The checker exposes the frozen R1-R11 derivation pipeline (`DECLARE`, `ADMIT`, `LICENSE`, `EQUIV`, `SUBSTITUTE`, `CONGRUENCE`, `TRANSPORT`, `QUOTIENT`, `COMPOSE`, `PRESERVE`, `REOPEN`) over typed objects, facts, authority edges, and a request.

No later SSI compiler/runtime layer may be substituted under RG-001 v0.1 after this freeze.

### OpenCore Nano

Repository: `bjoern-janson/opencore`  
Commit: `d85aac9fa35ea4ba21afebc73b9cb8970c2a1dbf`

Admitted native surface for adapter constitution:

```text
crank/nano.py
  git blob d31dacaf893a58a8280c01704fe666a404c1f56c
crank/NANO_V0.md
  git blob 3a6becedc054ce474f1baee80510aa08ef9dac20
```

Nano is treated exactly as its frozen V0 surface describes it: a semantically agnostic transition typechecker plus append-only journal whose trusted inputs are typed standings, preconditions, effect grants, preservation obligations, and revocation state.

No Mini+Nano composition, later ARO machinery, attack harness, or target-specific extension may be imported into the RG-001 Nano adapter.

## 4. What adapters may do

An adapter may only perform **structure-preserving transport** needed to express the already-frozen semantic object in a candidate's existing native vocabulary.

Allowed examples:

```text
opaque renaming / namespace allocation
serialization and deserialization
one frozen standing -> one native object/standing identifier
one frozen warrant -> one native evidence/warrant-bearing object
one frozen sufficient support set -> one explicit native contract/fact structure
one frozen challenge event -> withdrawal/revocation of exactly its designated warrant
mechanical decoding of native status/state into the frozen standing namespace
```

The adapter may expose structure to the realizer. It may not decide the structure's semantic consequence for the realizer.

## 5. What adapters may not do

Forbidden:

```text
reference_evaluator import/call
reference-oracle result lookup
case-id -> expected-outcome table
hand-authored expected phase labels
adapter-side closure computation
adapter-side descendant computation
adapter-side OR-of-routes rescue
adapter-side transitive invalidation
adapter-side successor authorization
post-challenge repair chosen from expected result
case-specific code paths keyed by C01..C08
label-specific behavior defeated by opaque permutation
cost, timing, opcode, memory, or robustness instrumentation
cross-realizer comparison
new SSI-CALC rule
new Nano kernel primitive
semantic change to F_LCC or RG001_CASE_FAMILY.json
```

If a native realizer cannot supply a required semantic consequence without one of these forbidden operations, the correct result is admission failure.

## 6. Admission gates

For each `r` separately, all gates A1-A14 must pass.

### A1 — source identity

`T_r` and `D_r` target only the exact frozen native source surface named above.

### A2 — total typed transport

`T_r` is defined for all eight frozen cases and every frozen standing, warrant, support set, challenge, and C08 successor event needed by those cases.

### A3 — no semantic mutation

The adapter does not add, delete, regroup, weaken, strengthen, or infer any sufficient support set.

### A4 — hyperedge preservation

Sufficient-support grouping is explicit in the native representation. In particular, the native encodings of C04 and C05 must remain distinguishable before any reference outcome is consulted.

### A5 — challenge locality

The frozen counterevidence event removes/revokes exactly the designated primitive warrant. It does not directly mark descendants invalid or preserved.

### A6 — native dependency consequence

Any descendant contraction or survival used later must arise from the candidate realizer's own existing operations/state semantics after the translated challenge, not from adapter-side closure.

### A7 — independent preservation

Independent standings/routes remain available only because their translated native support remains effective, not because the adapter labels them `preserved`.

### A8 — alternative-route non-aliasing

The candidate must be capable of representing and operationally retaining the difference between one conjunctive route and two alternative routes. Merely storing both structures in opaque metadata while native behavior ignores the distinction is insufficient.

### A9 — replacement firewall

C08 counterevidence alone cannot constitute the successor standing. The independent successor event must be separately translated and required for re-entry.

### A10 — decoder purity

`D_r` reads only candidate-native state/output/receipts/certificates produced through the frozen adapter path. It may rename or project native statuses; it may not recompute `F_LCC` semantics.

### A11 — oracle noninterference

Neither adapter imports, reads, hashes, embeds, or branches on the reference evaluator, its mechanically generated results, or a derivative expected-output artifact.

### A12 — opaque-label equivariance

Admission must survive the registered type-preserving opaque identity permutations. No semantic choice may depend on canonical names such as `s_g`, `s_h`, `w_a`, or case IDs.

### A13 — no coordinate measurement

Admission records no `V_F`, `C_F`, `B_F`, timing, opcode, memory, or comparative coordinate result.

### A14 — no semantic invention

If passing A1-A13 requires the adapter to implement a semantic operation absent from the frozen candidate surface, admission fails rather than extending the candidate.

## 7. Terminal rule

For each candidate:

\[
\boxed{
A_{\mathrm{trans}}^{RG}(r)=PASS
\iff
A1\land\cdots\land A14
}
\]

Otherwise:

\[
\boxed{
A_{\mathrm{trans}}^{RG}(r)=FAIL
\Rightarrow
\texttt{FUNCTION_EQUIVALENCE_NOT_CONSTITUTED}
}
\]

A failure is a translation/admission result only. It is not a negative `V_F` result and does not license repair under the same assay identifier.

## 8. Preregistration gate

The RG-001 preregistration may be frozen only if **both** independently constituted adapters pass this admission contract:

\[
\boxed{
A_{\mathrm{trans}}^{RG}(\mathrm{SSI\!\mbox{-}CALC})=PASS
\land
A_{\mathrm{trans}}^{RG}(\mathrm{Nano})=PASS
}
\]

Only then may RG-001 freeze the later sequence:

\[
A_{\mathrm{trans}}
\rightarrow V_F
\rightarrow \mathbf C_F
\rightarrow \mathcal B_F
\rightarrow \mathbf{STOP},
\qquad A_F=\mathrm{NA}.
\]

If either admission fails, the RG-001 preregistration is not opened and no `V_F`, `C_F`, or `B_F` execution occurs.

## 9. Claim ceiling at this layer

A successful admission means only:

> A frozen transport pair was constituted without obvious semantic invention and passed the registered translation/noninterference gates for the frozen case geometry.

It does **not** establish that the realizer satisfies `F_LCC`; that is reserved for the later preregistered `V_F` stage.

> **Constitute the object first; admit the realizers second.**
