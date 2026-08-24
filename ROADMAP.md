# Roadmap — Representation, Transfer, Resource Boundaries, and Effective Repertoire

Status: **CONJECTURAL ROADMAP; ONLY RIL-1 HAS A POSITIVE RESULT AND RIL-2 NOW HAS A FROZEN FAMILY**

Nothing here rewrites the frozen corpus, CGP-001, RIL-001, or the RIL-002 family.

## Current ladder

```text
RIL-1  one-function existence witness                 POSITIVE / CLOSED
RIL-2  family transfer                                FAMILY FROZEN / UNEXECUTED
RIL-3  provenance-separated held-out generalization   NOT OPENED
RIL-4  resource-boundary amplification                NOT OPENED
RIL-5  broad effective generality                     NOT OPENED
```

## RIL-1 — earned

RIL-001 established one bounded existence witness:

\[
\exists(F,D,R_0,R_1): P=1 \land C_{R_1}^{op}(F)<C_{R_0}^{op}(F).
\]

The frozen AST→SEM8 representation change reduced counted work by 58.325% for one exact FS007 correction with equal preregistered peak memory.

This does not imply transfer.

## RIL-2 — frozen transfer family

RIL-002 now asks whether the **same** frozen representation pair transfers leverage across a complete bounded family.

The family was frozen prospectively under:

```text
K1  f in frozen M1/FANOUT semantics
K2  f not in frozen M0/READ_ONCE semantics
K3  x,y,z all essential
K4  exclude RIL-001 target 0x17
```

This yields exactly 24 targets.

Every member has:

```text
M0 exact ceiling = 0.875
M1 exact ceiling = 1.000
```

The primary future object is the full leverage profile:

\[
\boldsymbol{\Lambda}=(\Lambda_1,\ldots,\Lambda_{24}),
\]

plus member-level preservation and memory results.

A family-wide result may show transfer across this family. It cannot show provenance-separated generality because SEM8 was originally selected with knowledge of the FS007 structure.

## RIL-3 — provenance-separated generalization

RIL-3 is a genuinely stronger experiment.

A future design must freeze a representation-selection procedure:

\[
R_1=g(\mathcal I_{select})
\]

before revealing the held-out transformation information.

The relevant firewall is stronger than different function names:

\[
\mathcal I_{select}(R_1)\cap \mathcal I_{test}=\varnothing.
\]

Only prospective leverage on the held-out side could begin to earn the phrase **representation-induced generality**.

RIL-3 is not opened by a positive RIL-002 result automatically.

## RIL-4 — resource-boundary amplification

Candidate object:

\[
\Omega_{eff}(R;B)=
\{\omega:\tau_R(\omega)\text{ valid and }c_R(\omega)\le B\}.
\]

The conjecture is that a representation's behavioral consequence is largest near a resource boundary:

```text
c_R0(omega) > B >= c_R1(omega)
```

This requires explicit budget manipulation. It cannot be inferred from RIL-001 or RIL-002 running on an unconstrained machine.

## RIL-5 — broad effective generality

Maximal conjecture:

> A useful representation may place a surprisingly broad class of typed transformations below the practical resource boundary of a constrained substrate.

This remains far beyond current evidence.

## Candidate affordance notation

The provisional object remains:

\[
\mathcal A(R)=
(\Omega_R,\tau_R,c_R,\mathcal C_R).
\]

This is a research convenience, not an earned ontology.

## Representation payback horizon

Representation construction/learning is not free:

\[
C_{total}(R,n)=C_{learn}(R)+\sum_{i=1}^{n}c_R(F_i).
\]

Candidate payback horizon:

\[
n^*=\min\{n:C_{total}(R_1,n)<C_{total}(R_0,n)\}.
\]

This becomes relevant only when a later study actually includes representation acquisition or learning cost.

## Escalation discipline

```text
RIL-1 positive != RIL-2 family transfer
RIL-2 transfer != RIL-3 held-out generality
RIL-3 generality != RIL-4 resource-boundary amplification
RIL-4 amplification != RIL-5 broad effective generality
```

Each rung requires its own prospective scope, preservation predicate, resource accounting, null, and stop condition.

## Working maxim

> **Observed capability may be the subset of a substrate's valid transformation repertoire that its current representation places below its operative resource boundary.**

For now, that remains a conjecture with one positive existence witness and one frozen transfer family.
