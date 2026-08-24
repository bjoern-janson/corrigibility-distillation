# RD-001 — Learner / Oracle Target Compatibility Audit

**Status:** `LEARNER FREEZE BLOCKED / TARGET-CLASS MISMATCH / Q_TRAIN UNOPENED / NO LEARNER DESIGNED`

**Experiment:** `RD-001`  
**Preregistration:** `bb0a85182a59a498568fa2905a49802af35b56b4`  
**Frozen v2 implementation:** `7d5fb20d73f47dab4d6dae72ad3ad16ad6443ea7`  
**Frozen calibration result:** `d2df78ada3642cd33a543360cb5218bda7892e30`  
**RIL-003:** `UNTOUCHED / FROZEN PRE-REVEAL`

This audit was opened **before any RD-001 training beacon was consumed, before `Q_train` was materialized, and before any learner architecture or acquisition source code was frozen**.

Its purpose is to test whether the newly proposed minimal learner is actually aimed at the same representational object measured by the successful `R_STAR` calibration.

---

## 1. Proposed learner question

The proposed minimal learner would search a finite hypothesis class of descriptor-coordinate projections and identity-retention choices, asking:

> **Which distinctions can safely disappear while preserving every operation in the frozen future operation signature?**

A candidate descriptor subset would be:

\[
K\subseteq\{0,1,2,3\}
\]

with a fixed learner-acquired canonicalization schema frozen before held-out test realization.

This is intentionally much weaker than an arbitrary learned program.

---

## 2. Frozen `R_L` output language is global

The preregistration allows `R_L` to emit only a candidate token-classification / canonicalization schema, including:

1. one partition of the finite descriptor alphabet `\{0,1\}^4` into learned token classes;
2. identity-retention choices within learned classes;
3. deterministic class labels;
4. deterministic canonicalization using those frozen classes.

The frozen `R_L` artifact may not contain test-instance-specific state tables, graph-specific test data, action recommendations, or post-test representation repair.

Therefore the scientific `R_L` object is one **prospectively frozen global descriptor partition / canonicalization rule** applied to fresh instances.

---

## 3. Frozen `R_STAR` is instance-adaptive

The implemented generator does **not** use one family-wide relevant descriptor subset.

The frozen implementation contract states:

> `For each generated instance the hidden structural signature chooses |J| in {1,2}; J uniformly ...`

For each instance, `R_STAR` receives that evaluator-only instance-specific `J` and uses the exact projection onto that `J` to construct its token classes.

Thus:

\[
\boxed{
R_\star(X_i)=R_{J_i}(X_i)
}
\]

with `J_i` allowed to vary across instances.

By contrast, the proposed fixed-coordinate learner would produce:

\[
\boxed{
R_L(X_i)=R_K(X_i)
}
\]

with one frozen `K` (or, more generally, one frozen global descriptor partition) for all fresh instances.

Therefore:

\[
\boxed{
R_\star\text{ and }R_L\text{ do not currently inhabit the same adaptation class.}
}
\]

---

## 4. Calibration confirms that `J` actually varies

The frozen 24-instance calibration result already shows variation in the oracle coordinate set.

Examples from the raw result:

```text
instance 0: J = {0,1}
instance 1: J = {0,3}
instance 2: J = {3}
instance 4: J = {1,2}
```

These four examples alone cover every descriptor coordinate `0,1,2,3` as future-relevant on at least one frozen calibration instance.

This matters because the positive calibration:

```text
sum C_fresh(R0)     = 2,093,094
sum C_fresh(R_STAR) = 1,134,901
aggregate leverage  = 1.844296550976693
24 / 24 fresh-cost wins
```

was obtained by allowing the oracle representation to use the **correct instance-specific `J_i` on each instance**.

The calibration therefore establishes:

\[
\boxed{
\text{instance-specific future-preserving representational leverage exists.}
}
\]

It does **not** yet establish:

\[
\boxed{
\text{one reusable global descriptor partition exists that recovers that leverage.}
}
\]

---

## 5. Consequence for the proposed fixed-`K` learner

Under the frozen generator support, any descriptor coordinate may become behaviorally relevant on a future instance because gated native transitions may depend on any bit `j in {0,1,2,3}`.

Therefore a fixed candidate `K` that permanently omits bit `j` cannot be claimed family-uniformly future-preserving merely because that bit was irrelevant on some other instance.

The problem is structural:

\[
\boxed{
J_i\text{ varies by instance}
\quad\land\quad
K\text{ is frozen globally}.
}
\]

A globally conservative coordinate projection can retain all four descriptor bits:

\[
K=\{0,1,2,3\}.
\]

Such a representation may still remove native identity where exact descriptor classes permit it, but it cannot in general reproduce the per-instance irrelevant-bit deletion used by `R_STAR`.

Whether that residual global compression yields any useful fresh-instance leverage has **not been measured** and is not inferred here.

---

## 6. Why the learner specification is not frozen

The intended next scientific question had been phrased as:

> **Can intelligence discover the same search-saving geometry that an oracle can supply?**

Under the frozen RD-001 objects, that wording is not yet licensed because the oracle is allowed an instance-specific structural input `J_i` that the preregistered learner output class cannot express as an instance-conditioned representation.

Freezing the proposed learner now and treating `R_STAR` as its recoverable structural ceiling would silently conflate:

\[
\boxed{
\text{instance-adaptive oracle coordinates}
\neq
\text{one globally frozen reusable coordinate system}.
}
\]

That would violate the program's own admission discipline.

Accordingly:

```text
MINIMAL LEARNER SPECIFICATION = NOT FROZEN
Q_TRAIN BEACON                = NOT CONSUMED
Q_TRAIN                       = NOT MATERIALIZED
R_L SOURCE                    = NONE
R_L ACQUISITION               = NOT RUN
TEST SEED                     = UNAVAILABLE BY DESIGN
```

---

## 7. What the positive calibration still earns

The RD-001 oracle calibration remains valid and unchanged.

It establishes, under the exact frozen 24-instance calibration:

\[
\boxed{
\text{future-preserving structural compression can reduce exhaustive fresh-instance search work.}
}
\]

The present audit narrows only the interpretation of `R_STAR` as a target for the future learner.

The calibration is evidence that useful coordinates exist **instance by instance**.

It is not yet evidence that the preregistered global learner language contains a reusable representation capable of recovering the same coordinate choices across changing `J_i`.

---

## 8. Scientifically distinct continuations

No continuation is opened by this audit.

Three continuations would answer different questions:

### A. Continue RD-001 exactly as preregistered

Keep one global learned descriptor partition.

Then the scientific question becomes:

> Can a single prospectively frozen global representation find any cross-instance leverage under a family whose relevant descriptor coordinates vary per instance?

`R_STAR` remains an instance-specific calibration control, **not** a directly recoverable learner ceiling.

### B. New experiment with a family-wide latent coordinate set

Freeze one hidden `J` for an entire train/test family before instance generation.

Then a learner could genuinely attempt to recover reusable coordinates from training dynamics.

This changes the task generator and therefore requires a **new experiment identifier and fresh preregistration/calibration**. It may not rewrite RD-001.

### C. New experiment with instance-conditioned representation inference

Allow a frozen learner to acquire a rule that, on each fresh instance, infers which descriptor distinctions matter from permitted instance structure/dynamics before BFS.

All such fresh-instance inference must be charged to `C_instantiate` and must not solve the planning task itself.

This changes the frozen `R_L` output/use class and therefore also requires a **new experiment identifier and fresh preregistration**.

---

## 9. Audit verdict

\[
\boxed{
\texttt{LEARNER_TARGET_CLASS_MISMATCH / TRAINING_NOT_OPENED}
}
\]

The first positive RD-001 calibration answered:

> **Do useful instance-specific coordinates exist?**

Yes.

Before asking whether the learner can discover them, the experiment must first ensure that the learner is actually allowed to represent the same kind of object.

The governing lesson is:

\[
\boxed{
\textbf{A demonstrated oracle advantage is not automatically a learnable target.}
}
\]

No learner, training suite, or held-out test lane is opened by this audit.
