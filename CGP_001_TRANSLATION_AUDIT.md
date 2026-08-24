# CGP-001 Translation Audit

Status: **FROZEN FIRST AUDIT — `A_trans = FAIL`**

Scientific stage:

```text
PREREGISTERED
-> APPARATUS FROZEN
-> TRANSLATION AUDIT
-> STOP
```

No CGP arm was executed. No outcome-bearing result directory, `CGP_001_RESULT.md`, or `CGP_001_AUDIT.md` was created.

## 1. Frozen lineage audited

Preregistration anchor:

```text
669a94aac6c07484323dde3b0fb64df5b9ec4bca
```

Apparatus anchor:

```text
50f817ce584a18a68237340fe05ede34602b874a
```

The apparatus anchor is a direct child of the preregistration anchor and changes exactly the six preregistered apparatus files.

| Apparatus file | SHA-256 |
|---|---|
| `experiments/cgp_001/cgp_001.py` | `ec4034d3f1142b0d2e556d28277574bbbec61d7a2d98ee12b94fbb609c4f772a` |
| `experiments/cgp_001/opcode_runner.py` | `43da3c30582cfd0cce154df0e9c471a987216a92c5da73d0da0b548662dfd768` |
| `experiments/cgp_001/test_translation.py` | `898f9f86c00e325f833a834e8a409acb53519f0e325446f214eac82392439058` |
| `experiments/cgp_001/contracts/translation_contract.json` | `360993ea973c14266516120c343c38c5d2087b40e992ccab1355d5229da875da` |
| `experiments/cgp_001/contracts/evaluation_contract.json` | `9e491a6827100d86ee261cb162d38741cd672a726d369f8aef64f4ce9b6559d5` |
| `experiments/cgp_001/fixtures/translation_fixtures.json` | `696efde534f12a754315458ef80ed7869394c69e4348407fe6a7a620d7df1991` |

Frozen parents inspected read-only:

```text
Negative-Space Search
307c24576ebea951be04d187c61e7428f4f0e184

Future Sufficiency
2f4ca824e02b89df0c23d64de312c4f93a4c8a41
```

This audit was performed after the apparatus existed and before any CGP arm execution. The auditor did not author the interrupted Codex implementation.

## 2. Audit rule

The preregistered rule is noncompensatory:

```text
all ten criteria PASS -> A_trans = PASS
any criterion FAIL    -> A_trans = FAIL
```

Missing evidence or semantic ambiguity fails closed.

`A_trans` is prerequisite evidence only. A pass would not itself support `H_CG`.

## 3. Criterion table

| # | Frozen criterion | Verdict | Evidence |
|---:|---|---|---|
| 1 | Identical source multisets map byte-identically after canonical serialization. | `PASS` | `translate_examples` validates then sorts only by `(local_values, hidden, raw_id)` and emits deterministic frozen literals / input-derived values. The frozen fixture suite includes source-order permutations and canonical JSON comparison. No mutable translator state exists. |
| 2 | Every translated value derives only from declared input or an explicitly frozen literal with its documented role. | `PASS` | `_validate_record` reads only `bits`, `task.args`, `hidden`, and `raw_id`; `translate_examples` derives the three local bits and emits only the preregistered constants/index-derived fields. |
| 3 | No family, target-function object, future result, adequacy label, M1 result, value, or persistence state is read. | `PASS` | The translator signature is `translate_examples(examples)` only. The implementation has no condition/family/cost/horizon/M0/M1/held-out/persistence argument or lookup in the translator path. `hidden` is an allowed released input field; criterion 8 separately audits whether its semantic role survives the mapping. |
| 4 | The adapter cannot mutate or authorize FS state. | `PASS` | Translation constructs fresh NSS `LanguageEpisode` values and has no reference to an FS learner/generator. `nss_allocate` constructs a fresh NSS policy and returns a record; it does not write FS repair/adoption state. |
| 5 | Output role remains search allocation. | `PASS` | The translator itself emits episodes, not adequacy/adoption. The coupling reads only NSS resource output to produce `INVOKE/SKIP`; repair scoring, value, mutation, and persistence remain outside the translator path. Criterion 9 separately audits whether that resource projection is semantically legitimate. |
| 6 | Exact 78-expression NSS signature equivalence equals full-M0 equivalence on all eight local Boolean patterns. | `PASS` | FS M0 contains the atom programs `x`, `y`, and `z`, so equality under every M0 program implies equality of `(x,y,z)`, and equal tuples trivially agree under all M0 programs. The translation maps each bit to `(0,0)` versus `(0,1)`; NSS's frozen single relation `pair_i_close` therefore distinguishes `0` from `1` on each coordinate. Hence complete NSS-signature equality iff local-tuple equality iff full-M0 equivalence. The apparatus also freezes an exhaustive 8-pattern checker. |
| 7 | Exact `BoundaryGatedGenericSynthesizer` makes every per-signature expansion decision. | `PASS` | The frozen NSS parent groups by `current_language_signature`, marks a collision iff a signature has more than one `resolving_probe`, and `BoundaryGatedGenericSynthesizer` expands only such signatures. `nss_allocate` instantiates that exact class fresh and derives its count only after `policy.fit`; the adapter does not compute collisions. |
| 8 | `hidden -> resolving_probe` is only an injective rename of a released FS scoring label into the NSS resolved-class slot; semantic non-equivalence is `FAIL`. | **`FAIL`** | FS `Example.hidden` is the target/scoring output: `make_probe_examples` sets `hidden = target(values, family)`, and `score_program` judges a program by equality to `example.hidden`. NSS `resolving_probe` is not an output class; it records which probe resolves an episode/case, is collected as `matched_resolving_probes`, and is emitted as `selected_probe` / compared to a `true_resolving_probe`. Renaming `0/1` to `fs_output_0/fs_output_1` is injective lexically but changes semantic type from **target output** to **resolving probe identity**. Under the frozen rule, that is constitutive semantic non-equivalence, not a faithful rename. |
| 9 | `expanded_signature_count > 0 -> one FS M1 opportunity` is only a resource-unit conversion, not a new adequacy decision. | **`FAIL`** | In NSS v0.7, an expanded signature is a specific collision class on which the parent immediately runs its own generic predicate synthesis to distinguish resolving probes. `expanded_signature_count` therefore counts **per-signature NSS synthesis events**. FS007 M1 is instead one global search over a different construction language whose possible consequence is a persistent generator change. Mapping existential NSS expansion to a global FS M1 opportunity changes both the search object and scope. The parent does not supply this bridge. Calling it a mere unit conversion would grant the adapter a constitutive cross-mechanism allocation rule that the frozen parent did not demonstrate. Ambiguity is `FAIL` by preregistration. |
| 10 | Malformed, hash-mismatched, stale-instance, and unmapped cases fail closed. | `PASS` | The pure translator rejects empty/malformed records, duplicate IDs, non-Boolean bits/labels, malformed task indices, and wrong bit length. `verify_apparatus` checks exact parent commit IDs, file SHA-256s, imports, counts, and signature equivalence before translation. `nss_allocate` creates a fresh `BoundaryGatedGenericSynthesizer` per call, so a stale caller-supplied policy cannot enter the gate. No fallback allocation exists on verifier/translation exceptions. |

## 4. Decisive semantic failure — criterion 8

The two parent fields are differently typed.

Future Sufficiency uses:

```text
Example.hidden
= target-function output / supervised scoring label
```

The exact scoring relation is:

```text
program.evaluate_local(local_values(example)) == example.hidden
```

Negative-Space Search uses:

```text
LanguageEpisode.resolving_probe
= identity of the probe that resolves the case
```

and the parent decision surface preserves that role through:

```text
matched_resolving_probes
selected_probe
true_resolving_probe
```

Therefore:

```text
FS target output label
!=
NSS resolving-probe identity
```

The mapping:

```text
0 -> fs_output_0
1 -> fs_output_1
```

preserves cardinality and equality structure, but not semantic role.

CGP-001 explicitly required semantic equivalence, not merely an isomorphic two-class encoding.

So criterion 8 fails.

## 5. Independent bridge failure — criterion 9

The frozen NSS mechanism's allocation unit is a **current-language signature**.

For each signature:

```text
collision = len(distinct resolving_probe labels) > 1
collision -> expand this signature
```

When it expands, NSS runs its own generic predicate synthesis inside that collision group.

The proposed CGP projection instead says:

```text
any expanded NSS signature
-> invoke one global FS M1/fan-out search
```

But FS M1 is not the same resource unit:

- it searches a different program language;
- it is global over the FS repair condition rather than local to one NSS signature;
- its output may enable a persistent generator mutation after FS value gating;
- no frozen NSS output denotes this global repair-search opportunity.

Thus the projection is not merely:

```text
N NSS search units -> 1 equivalent FS search unit
```

It introduces a new cross-mechanism bridge rule:

```text
existence of an NSS-local collision
-> license evaluation of a global FS generator repair
```

That bridge is exactly what CGP-001 was supposed to test, so it cannot be smuggled into the adapter as a constitutive conversion.

Criterion 9 therefore independently fails.

## 6. Why no primary execution follows

The preregistered terminal rule is exact:

```text
A_trans = FAIL
-> CGP-001 = NOT EVALUABLE
-> STOP
```

This is not:

```text
H_CG = false
```

and it is not evidence that an NSS/FS corridor cannot exist.

The narrower result is:

> The specific CGP-001 transformation could not be constituted as a faithful coupling of the frozen parent mechanisms. Its adapter changed the semantic type of the NSS collision label and introduced a new scope-changing bridge from per-signature NSS expansion to global FS repair search.

No B-code is assigned because the preregistration forbids boundary localization when `A_trans=FAIL`.

## 7. Terminal status

```text
A_trans                    = FAIL
failed_criteria            = [8, 9]
CGP_001                     = NOT EVALUABLE
CGP arm execution           = NOT AUTHORIZED
L0/L1/L2/L3 scoring         = NOT REACHED
H_CG                        = NOT TESTED BY CGP-001
old corpus lane             = CLOSED / UNCHANGED
next repair under CGP-001   = FORBIDDEN
```

No adapter repair, semantic remapping, scope remapping, new gate, new cost rule, or outcome-bearing run may be added to CGP-001.

Any scientifically meaningful attempt to repair the cross-repository relation must be a new prospective object, e.g. `CGP-002`, with this null preserved.

## Final rule

**The corridor was not yet constituted faithfully enough to test the snowflake prediction. Stop before execution.**
