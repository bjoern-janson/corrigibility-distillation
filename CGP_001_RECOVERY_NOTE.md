# CGP-001 Recovery and Public-Integration Note

Status: **PROVENANCE NOTE — DOES NOT CHANGE THE CGP-001 SCIENTIFIC RESULT**

## 1. Why this note exists

CGP-001 was interrupted when the Codex execution session exhausted its usage allowance after the preregistration had already been pushed to GitHub but while the experimental apparatus still existed only in the local working copy.

The user supplied that interrupted working copy as `work.zip`.

The recovery process preserved the existing preregistration and reconstructed the local Git state rather than restarting CGP-001 or rewriting its scientific contract.

## 2. Recovered local lineage

The recovered local repository contained this lineage:

```text
669a94aac6c07484323dde3b0fb64df5b9ec4bca
    Freeze CGP-001 preregistration

50f817ce584a18a68237340fe05ede34602b874a
    Freeze CGP-001 apparatus

b5ee054628926de3509b7a6d7f50918dec319372
    Freeze CGP-001 translation audit
```

The apparatus commit was a direct child of the preregistration commit. The audit was performed on that frozen apparatus before any primary CGP arm execution.

## 3. Exact recovered apparatus

The six apparatus files and SHA-256 hashes are:

| File | SHA-256 |
|---|---|
| `experiments/cgp_001/cgp_001.py` | `ec4034d3f1142b0d2e556d28277574bbbec61d7a2d98ee12b94fbb609c4f772a` |
| `experiments/cgp_001/opcode_runner.py` | `43da3c30582cfd0cce154df0e9c471a987216a92c5da73d0da0b548662dfd768` |
| `experiments/cgp_001/test_translation.py` | `898f9f86c00e325f833a834e8a409acb53519f0e325446f214eac82392439058` |
| `experiments/cgp_001/contracts/translation_contract.json` | `360993ea973c14266516120c343c38c5d2087b40e992ccab1355d5229da875da` |
| `experiments/cgp_001/contracts/evaluation_contract.json` | `9e491a6827100d86ee261cb162d38741cd672a726d369f8aef64f4ce9b6559d5` |
| `experiments/cgp_001/fixtures/translation_fixtures.json` | `696efde534f12a754315458ef80ed7869394c69e4348407fe6a7a620d7df1991` |

The frozen translation audit has SHA-256:

```text
2ed0364b9ca20c5254d142cef646bbbe4febc6b2a16a8a5297e932342f00bef4
```

## 4. Why the public commit order differs

While the recovered local CGP history was being preserved and audited, the public `main` branch still ended at the preregistration commit. The later RIL-001 preregistration was then frozen on public `main`.

Therefore the public branch did not initially contain the recovered CGP apparatus/audit even though those artifacts existed and CGP-001 had already reached its terminal local scientific state.

The later repository-reconciliation commit imports the **exact recovered blobs** and this provenance note into the public branch. It does not pretend that the integration commit was the original apparatus freeze time.

Scientific temporal order remains:

```text
CGP preregistration
-> local apparatus freeze
-> independent translation audit
-> A_trans FAIL
-> STOP, no primary execution
-> later public integration of recovered artifacts
```

The public Git topology is therefore an integration history, while the hashes above preserve the recovered scientific artifact identity.

## 5. Terminal result is unchanged

```text
A_trans              FAIL
failed criteria      8, 9
CGP-001               NOT EVALUABLE
H_CG                  NOT TESTED
primary arms          NOT RUN
```

No adapter repair or post-hoc CGP-001 execution is authorized by this recovery.
