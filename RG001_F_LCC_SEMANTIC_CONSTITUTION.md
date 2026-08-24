# F_LCC Semantic Constitution v0.1

**Object:** `F_LCC_SEMANTIC_CONSTITUTION_V0.1`  
**Lane:** `RG-001`  
**Status:** `FROZEN_SEMANTIC_CONSTITUTION`  
**Realizers admitted:** `NO`

## 1. Scientific role

This artifact constitutes the realizer-neutral function later tested by RG-001.

It does not establish that SSI-CALC, OpenCore Nano, or any other system realizes the function.

\[
\boxed{
F_{\mathrm{LCC}}\text{ constituted}
\not\Rightarrow
F_{\mathrm{LCC}}\text{ realized}
}
\]

The governing rule is:

> **Adapt the realizer to \(F\). Never adapt \(F\) to the realizer.**

## 2. State and support structure

A case contains a finite set of standings

\[
S=\{s_1,\ldots,s_n\}
\]

and a finite set of externally constituted primitive warrants

\[
W=\{w_1,\ldots,w_m\}.
\]

Each standing \(s\in S\) has an externally supplied family of sufficient support sets

\[
\boxed{
\mathcal Q(s)\subseteq \mathcal P(S\cup W).
}
\]

Each \(q\in\mathcal Q(s)\) is one sufficient route for the standing.

The complete support structure is

\[
\boxed{
\rho=\{\mathcal Q(s):s\in S\}.
}
\]

For RG-001 v0.1, \(\rho\) is finite and acyclic.

The realizer does not infer, discover, repair, or redefine \(\rho\).

## 3. Sufficient support, not binary dependency

A binary statement such as \(H\prec G\) is insufficient when alternative warrants exist.

For example,

\[
\mathcal Q(H)=\{\{G\},\{w_{\mathrm{alt}}\}\}.
\]

Here \(G\) is a genuine support route for \(H\), but invalidating \(G\) does not invalidate \(H\) while \(w_{\mathrm{alt}}\) remains active.

Therefore:

\[
\boxed{
\text{structural dependency}
\neq
\text{effective contraction}.
}
\]

The frozen support hypergraph, not either realizer, determines the expected consequence.

## 4. Validity semantics

Let \(W_t^+\subseteq W\) be the active primitive warrants at phase \(t\).

A primitive warrant \(w\) is available iff \(w\in W_t^+\).

A standing is valid iff at least one sufficient support set is fully available:

\[
\boxed{
Valid_\rho(s,t)
\iff
\exists q\in\mathcal Q(s):
\forall x\in q,\ Available_\rho(x,t).
}
\]

where

\[
Available_\rho(x,t)=
\begin{cases}
x\in W_t^+,&x\in W,\\
Valid_\rho(x,t),&x\in S.
\end{cases}
\]

Thus validity is mechanically determined by \((\rho,W_t^+)\).

## 5. Challenge constitution

Each canonical LCC case designates a challenged standing \(G\in S\) and one specific active primitive warrant \(w_G\in W\).

The counterevidence event is externally constituted as:

\[
E^-:w_G\rightarrow\texttt{INVALID}.
\]

Operationally,

\[
\boxed{
W_1^+=W_0^+\setminus\{w_G\}.
}
\]

The event changes no other primitive warrant, does not change \(\rho\), and does not itself create positive support for a replacement.

Canonical RG-001 cases require:

\[
Valid_\rho(G,0)=1
\qquad\text{and}\qquad
Valid_\rho(G,1)=0.
\]

## 6. Corrective consequence classes

After the challenge, validity is recomputed under unchanged \(\rho\).

### LCC-1 — implicated contraction

The challenged standing loses effective standing:

\[
G:\texttt{VALID}\rightarrow\texttt{DIRECTLY\_INVALIDATED}.
\]

### LCC-2 — dependency-selective contraction

For \(H\neq G\),

\[
Valid_\rho(H,0)=1
\land
Valid_\rho(H,1)=0
\]

implies:

\[
H:\texttt{VALID}\rightarrow\texttt{DEPENDENCY\_DEFERRED}.
\]

Contraction occurs only when every sufficient support route has become unavailable.

### LCC-3 — independent preservation

For \(U\),

\[
Valid_\rho(U,0)=Valid_\rho(U,1)=1
\]

implies:

\[
U:\texttt{VALID}\rightarrow\texttt{PRESERVED}.
\]

This includes structurally unrelated standings and standings retaining an alternative sufficient support route.

The operative challenge-relative independence relation is therefore:

\[
\boxed{
Independent_\rho(U;w_G)
\iff
Valid_\rho(U,0)=Valid_\rho(U,1)=1.
}
\]

## 7. Replacement firewall

A case may designate a candidate successor \(G'\in S\).

The counterevidence event \(E^-\) contains no positive warrant for \(G'\).

For canonical replacement-firewall cases:

\[
Valid_\rho(G',0)=0
\]

and

\[
Valid_\rho(G',1)=0.
\]

Therefore:

\[
\boxed{
\operatorname{REFUTE}(G)
\not\Rightarrow
\operatorname{AUTHORIZE}(G').
}
\]

This is LCC-4.

## 8. Independent successor re-entry

A distinct event \(E^+_{G'}\) may later activate a separately constituted primitive successor warrant \(w_{G'}\):

\[
W_2^+
=
W_1^+\cup\{w_{G'}\}.
\]

If this completes a sufficient support set for \(G'\), then:

\[
Valid_\rho(G',2)=1.
\]

Thus LCC-5 is:

\[
\boxed{
\text{independent successor evidence can re-enter}.
}
\]

This prevents permanent refusal from masquerading as corrigible authority discipline.

## 9. Frozen function

A canonical case is

\[
X=
(S,W,\rho,W_0^+,G,w_G,G',E^-,E^+_{G'})
\]

with optional replacement fields where not applicable.

Define:

\[
X_0=Closure_\rho(W_0^+),
\]

\[
X_1=Closure_\rho(W_0^+\setminus\{w_G\}),
\]

and, when successor evidence is supplied,

\[
X_2=
Closure_\rho
\left(
(W_0^+\setminus\{w_G\})\cup\{w_{G'}\}
\right).
\]

Then:

\[
\boxed{
F_{\mathrm{LCC}}(X)=(X_0,X_1,X_2)
}
\]

subject to:

\[
\boxed{
\begin{aligned}
LCC_1&:\text{ implicated contraction}\\
LCC_2&:\text{ dependency-selective contraction}\\
LCC_3&:\text{ independent preservation}\\
LCC_4&:\text{ no replacement authority from refutation}\\
LCC_5&:\text{ independent successor evidence can re-enter}.
\end{aligned}
}
\]

## 10. Realizer-neutral schema constraints

The semantic case representation may contain:

```text
case_id
standings
primitive_warrants
support_sets
initial_active_warrants
challenge
replacement
```

It must not contain:

```text
SSI rule names
Nano licenses
Nano receipts
receipt-parent hints
realizer-native expected statuses
adapter hints
failure-locus hints
preferred realizer encoding
```

Expected consequences are derived by an independent closure evaluator from the frozen support semantics; they are not hand-authored into the scientific case family.

## 11. Well-formedness

A canonical RG-001 case must satisfy:

```text
finite support structure
acyclic standing-to-standing support
all referenced nodes declared
nonempty sufficient support sets
challenged warrant active at phase 0
challenged standing valid at phase 0
challenged standing invalid at phase 1
challenge changes exactly the designated primitive warrant
rho unchanged across phases
counterevidence creates no successor warrant
successor evidence distinct from counterevidence
expected phase states mechanically reconstructible from the reference evaluator
```

## 12. Explicit non-claims

This constitution does not establish:

```text
SSI-CALC realizes F_LCC
OpenCore Nano realizes F_LCC
cross-realizer functional equivalence
adapter admissibility
cost separation
boundary separation
autonomy
dependency discovery
general realization geometry
completeness of Gamma_F
```

In particular:

\[
\boxed{
\rho\text{ is apparatus-supplied semantic structure.}
}
\]

RG-001 does not test autonomous discovery of dependency or warrant structure.

## 13. Next legal object

The next scientific artifact is:

```text
RG001_CASE_FAMILY
```

It must be finite, realizer-blind, permutation-tested, and evaluated only by the independent closure semantics defined here.

SSI-CALC and Nano remain outside the assay until that family and its reference audit are frozen.
