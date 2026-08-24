# Roadmap — Representation, Resource Boundaries, and Effective Repertoire

Status: **CONJECTURAL ROADMAP — NOT PART OF THE FROZEN RIL-001 SCIENTIFIC CONTRACT**

RIL-001 has now supplied one bounded positive single-function witness. Nothing in this document is thereby promoted to universal theory.

## 1. Current empirical foothold

RIL-001 established, under its exact frozen scope:

```text
same corrective transformation
same exhaustive algorithm
same scope and authority
R0_AST -> R1_SEM8
C_op: 9,825,003 -> 4,094,613
Lambda_F^op = 2.399494897320
peak memory: 206,757 -> 206,757 bytes
```

This earns **RIL-1 for one bounded assay only**.

It does not by itself establish that one representation gives leverage across a family, on unseen transformations, near resource boundaries, or on constrained hardware.

## 2. Candidate affordance object

Provisional notation:

\[
\mathcal A(R)=(\Omega_R,\tau_R,c_R,\mathcal C_R),
\]

where `Omega_R` denotes transformations available under `R`, `tau_R` their semantic/type signatures, `c_R` realization cost, and `C_R` constraints on legal transformation space.

This remains a research convenience, not an earned ontology.

## 3. Resource-bounded effective repertoire

Candidate object:

\[
\Omega_{\mathrm{eff}}(R;B)=\{\omega:\tau_R(\omega)\text{ is valid and }c_R(\omega)\le B\}.
\]

Conjecture:

> **Changing representation may enlarge the practically reachable typed transformation repertoire of a fixed substrate by moving useful transformations below a resource boundary.**

This says nothing about changing formal computability or creating new physical primitives.

## 4. RIL ladder

### RIL-1 — single-function leverage

**Status: one bounded positive witness (`RIL-001`).**

The result is local to one FS007 correction and one representation pair.

### RIL-2 — family leverage

**Status: NOT OPENED.**

Future question: freeze one representation choice and test a prospectively specified family of already-valid transformations, requiring preservation for every member and counting any representation construction cost.

A positive family result would still not establish held-out generality.

### RIL-3 — held-out transformation leverage

**Status: NOT OPENED.**

Choose or learn the representation from `F_train`, freeze it, then test disjoint `F_test`:

```text
F_train intersection F_test = empty
```

This is the first rung at which “representation-induced generality” could begin to acquire prospective evidence.

### RIL-4 — resource-boundary amplification

**Status: NOT OPENED.**

Explicitly manipulate budget `B` and test the predicted region:

```text
c_R0(omega) > B >= c_R1(omega)
```

The claim would concern effective-capability consequence near a budget boundary, not merely a cost ratio on abundant hardware.

### RIL-5 — broad effective generality on constrained substrate

**Status: NOT OPENED.**

Maximal conjecture:

> A useful representation may place a surprisingly broad class of typed transformations below the practical resource boundary of a constrained substrate.

This remains far beyond current evidence.

## 5. Representation payback horizon

Representation discovery/learning is not free. Candidate total-cost object:

\[
C_{\mathrm{total}}(R,n)=C_{\mathrm{learn}}(R)+\sum_{i=1}^{n}c_R(F_i).
\]

Candidate payback horizon:

\[
n^*=\min\{n:C_{\mathrm{total}}(R_1,n)<C_{\mathrm{total}}(R_0,n)\}.
\]

RIL-001 does not estimate this quantity because both coordinate systems were already present in the frozen parent library and the assay measured only its preregistered representation-view construction boundary.

## 6. Failure taxonomy to preserve

```text
distinction failure
    required states collapse under R

typing failure
    required transformations cannot legally compose

leverage failure
    transformation remains valid but realization cost is unfavorable
```

These are not claimed to be exhaustive or one proven theory.

Motivating exemplars remain evidentially separate:

```text
SRE       formal quotient-operation constraints
CGP-001   prospective semantic/interface typing failure
FS007     bounded representation-generator repair
RIL-001   bounded representation-induced leverage witness
Quake     external engineering analogy only
```

## 7. Escalation discipline

```text
RIL-001 positive != family leverage
family leverage != held-out leverage
held-out leverage != resource-boundary amplification
resource-boundary amplification != broad generality
```

Every rung requires its own frozen scope, preservation predicate, resource accounting, leakage firewall, and null.

## Working maxim

> **Observed capability may be the subset of a substrate's valid transformation repertoire that its current representation places below its operative resource boundary.**

After RIL-001 this remains a conjecture with one microscopic empirical foothold—not a theory.
