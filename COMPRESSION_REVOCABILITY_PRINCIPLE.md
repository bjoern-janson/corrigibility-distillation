# Compression / Revocability Principle

**Status:** `PROGRAM-LEVEL METHODOLOGICAL PRINCIPLE / NOT A NEW MECHANISM / NOT A NEW EXPERIMENT`  
**Scope:** retrospective synthesis over the existing corrigibility / realization lineage  
**Parent program head:** `794ce9b6c7a3ef9d0c83cdbe859d6aaadeb955b5`  
**RIL-003:** `UNTOUCHED / FROZEN PRE-REVEAL`

## 1. Core distinction

\[
\boxed{
\textbf{Compression buys cheap execution. Corrigibility preserves the right to revoke what was compressed.}
}
\]

This preserves the non-equivalence

\[
\boxed{\text{optimization}\neq\text{continued validity}.}
\]

A representation or compiled rule may preserve the operational benefit of an earlier discovery while failing to preserve the derivation, validity conditions, or provenance that originally justified trusting it.

A useful decomposition is:

\[
\boxed{
D=\text{discovery},\quad
E=\text{execution},\quad
V=\text{validity},\quad
P=\text{provenance}.
}
\]

The program should not assume

\[
\boxed{E\text{ preserved}\Rightarrow D,V,P\text{ preserved}.}
\]

In many systems, cheap execution can survive while much of the epistemic structure that licensed the execution is lost.

## 2. Stable and drifting validity domains

The principle separates two regimes.

### Stable validity domain

When the validity conditions are constituted and effectively invariant over the intended domain:

\[
\boxed{\text{validate}\rightarrow\text{compress}\rightarrow\text{exploit repeatedly}.}
\]

No general requirement follows that every execution must re-derive the original justification.

The bounded methodological statement is:

\[
\boxed{
\textbf{Compressed structure is trustworthy relative to a constituted domain of validity.}
}
\]

### Drifting / revisable validity domain

When the validity conditions can cease to hold, continued use of the compressed structure requires more than prior success.

The required condition is:

\[
\boxed{
\textbf{When invalidation is possible, invalidating evidence must retain a causal route to the decision that relies on the compressed structure.}
}
\]

Equivalently:

\[
\boxed{
\text{compressed decision}
+
\text{reachable invalidation path}
}
\]

rather than

\[
\text{compressed decision}
+
\text{permanent trust}.
\]

The path may support detection, reopening, replacement, withdrawal of authority, or another admissible form of revocation. This artifact does not prescribe one universal mechanism.

## 3. Correction regimes

The distinction also separates two forms of correction.

### Constituted-target refinement

The target and the error relation are already fully specified. Correction reduces approximation error against that fixed target.

### Warrant-revisable correction

The target, model, representation, authority, or warrant may itself become invalid. The scientific problem is not merely to reduce residual error but to preserve a valid path by which changed evidence can alter what is trusted or acted upon.

Therefore:

\[
\boxed{
\textbf{constituted-target refinement}
\neq
\textbf{warrant-revisable correction}.
}
\]

## 4. Relation to existing program results

This principle is a synthesis of already-separated results, not evidence that the underlying mechanisms are identical.

### RIL

RIL-001/002 establish a bounded positive result of the form

\[
F\text{ fixed and constituted}
\quad+\quad
R_0\rightarrow R_1
\quad\Rightarrow\quad
C_1<C_0.
\]

This demonstrates that once function validity is constituted, representation can materially change realization cost.

### Signature-Relative Equivalence

SRE establishes that preservation/equivalence is relative to the future operation signature that must remain supported. This is directly relevant to the phrase "domain of validity": validity is not an untyped universal property.

### Cerebro / SSI / OpenCore

These lines repeatedly separate stored history, certificates, evidence, admission, authority, and causal effect. The present principle does not collapse those objects. It uses them as examples of why preserving an operational conclusion need not preserve the conditions under which that conclusion remains licensed.

### Admissibility Failure Atlas

The 54-repository atlas found that mature failures frequently occur before or at semantic, provenance, identifiability, or causal-path constitution. The present principle adds a downstream consequence:

> Even after a useful conclusion has been compressed into a cheap rule, continued trust is not automatically licensed when the rule's validity conditions are capable of changing.

## 5. Relation to the intervening-transformation principle

The program-level methodological law already established is:

\[
\boxed{
\textbf{Every consequential claim depends on an intervening transformation whose admissibility must be earned independently.}
}
\]

The compression/revocability principle applies after some of those transformations have succeeded.

A useful ordering is:

\[
\boxed{
\text{constitute validity}
\rightarrow
\text{compress / optimize execution}
\rightarrow
\text{preserve invalidation reachability when validity can drift}.
}
\]

This prevents two opposite errors:

1. refusing useful compression merely because the full discovery history is not replayed on every execution; and
2. treating a historically successful compressed rule as permanently authoritative after the conditions that licensed it may have changed.

## 6. Plain-language compression

\[
\boxed{
\textbf{Having a cheap rule is not the same as having a permanently valid rule.}
}
\]

and:

\[
\boxed{
\textbf{If the reasons for trusting a rule can cease to hold, invalidation must still be able to reach the rule.}
}
\]

The shortest program compression remains:

\[
\boxed{
\textbf{Compression buys cheap execution. Corrigibility preserves the right to revoke what was compressed.}
}
\]

## 7. Claim ceiling

This artifact does **not** establish:

- a universal theorem about compression;
- that all compressed knowledge requires full provenance at execution time;
- that all domains drift;
- that every system requires a single explicit "revocation module";
- that RIL, SRE, SSI, Cerebro, OpenCore, the atlas, or historical optimization examples instantiate one common mechanism;
- a new architecture, primitive, or experiment;
- any modification to RIL-003 or its preregistered reveal boundary.

It freezes only a program-level methodological principle:

> Compression and validity are distinct. When validity can change, a system that continues to rely on compressed structure must preserve an admissible causal route by which invalidating evidence can alter, reopen, replace, or revoke the decision rule that depends on it.
