# Roadmap — Representation, Resource Boundaries, and Effective Repertoire

Status: **CONJECTURAL ROADMAP — NOT PART OF THE FROZEN RIL-001 SCIENTIFIC CONTRACT**

This document records the larger rabbit hole without leaking it into RIL-001. Nothing here changes `RIL_001_PREREGISTRATION.md`, the frozen corpus results, or CGP-001.

## 1. Candidate affordance object

A representation may be described provisionally by:

\[
\mathcal A(R)=(\Omega_R,\tau_R,c_R,\mathcal C_R),
\]

where:

- `Omega_R` — transformations available under `R`;
- `tau_R` — semantic/type signatures of those transformations;
- `c_R(omega)` — resource cost of realizing `omega`;
- `C_R` — constraints defining the legal transformation region.

This notation is a research convenience, not an earned ontology.

## 2. Resource-bounded effective repertoire

For fixed substrate and resource budget `B`, define the candidate object:

\[
\Omega_{\mathrm{eff}}(R;B)
=
\{\omega:\tau_R(\omega)\text{ is valid and }c_R(\omega)\le B\}.
\]

The disciplined conjecture is:

> **Changing representation may enlarge the practically reachable typed transformation repertoire of a fixed substrate by moving useful transformations below a resource boundary.**

This does **not** mean representation changes formal computability or creates new physical primitives.

A useful distinction is:

```text
C_raw   physical compute / memory / primitive substrate resources
C_repr  transformations exposed or supported by a representation
C_eff   transformations that are valid and realizable within the operative budget
```

The research target is `C_eff`, not magical creation of `C_raw`.

## 3. RIL ladder

### RIL-1 — single-function leverage

Question:

```text
Can one already-earned transformation become cheaper under R1 than R0
while preserving F, D, Omega_req, authority, and algorithm?
```

This is the only rung currently preregistered: `RIL-001`.

### RIL-2 — family leverage

Freeze one representation and test whether its leverage survives across a preregistered family of already-valid transformations.

A positive result would require preservation for every family member. It would not yet establish generality.

### RIL-3 — held-out transformation leverage

Choose/learn the representation using `F_train`, freeze it, then test disjoint `F_test`.

```text
F_train intersection F_test = empty
```

The interesting signal is prospective cost reduction on held-out transformations without semantic or authority drift.

This is the first rung where the phrase **representation-induced generality** could begin to earn evidence.

### RIL-4 — resource-boundary amplification

For fixed representation `R` and budget `B`:

```text
omega is practically reachable iff c_R(omega) <= B
```

The conjecture is that representational improvements have the largest *effective-capability consequence* when tasks lie near the resource boundary:

```text
c_R0(omega) > B >= c_R1(omega)
```

With abundant resources, both representations may succeed and the same leverage ratio may have little behavioral consequence.

A future assay should therefore manipulate the resource budget explicitly rather than infer boundary effects from one powerful machine.

### RIL-5 — broad effective generality on constrained substrate

The maximal conjecture is:

> **A sufficiently useful representation may place a surprisingly broad class of typed transformations below the practical resource boundary of an otherwise constrained substrate.**

This is intentionally far beyond current evidence.

## 4. Representation payback horizon

Representation construction/learning is not free.

For repeated transformations:

\[
C_{\mathrm{total}}(R,n)
=
C_{\mathrm{learn}}(R)
+
\sum_{i=1}^{n}c_R(F_i).
\]

Define the candidate payback horizon:

\[
n^*
=
\min\left\{
 n:
 C_{\mathrm{total}}(R_1,n)
 <
 C_{\mathrm{total}}(R_0,n)
\right\}.
\]

This separates:

```text
cheap execution after expensive representation discovery
```

from:

```text
genuine total-resource advantage over a reuse horizon.
```

A future learning study could treat representation repair as an investment that changes the cost landscape of later transformations.

## 5. Failure taxonomy to preserve

The broader conjecture currently distinguishes at least three failure modes:

```text
distinction failure
    required states collapse under R

typing failure
    required transformations cannot compose under the semantic signatures

leverage failure
    the required transformation remains valid but is too expensive under R
```

These are not claimed to be exhaustive or manifestations of one proven theory.

Examples that motivated the distinction remain evidentially separate:

```text
SRE       formal distinction / quotient-operation constraints
CGP-001   prospective semantic typing failure in an attempted interface
FS007     bounded evidence/value-conditioned representation-generator repair
Quake     external engineering analogy for representation-induced computational leverage
```

Do not convert analogy into evidence.

## 6. What would count as real escalation

The ladder may advance only through new prospective evidence:

```text
RIL-1 positive
!= family leverage

family leverage
!= held-out leverage

held-out leverage
!= resource-boundary amplification

resource-boundary amplification
!= broad generality
```

Every rung needs its own frozen scope, preservation predicate, resource accounting, and null.

## Working maxim

> **Observed capability may be the subset of a substrate's valid transformation repertoire that its current representation places below its operative resource boundary.**

For now, that is a conjecture with a ladder—not a theory.
