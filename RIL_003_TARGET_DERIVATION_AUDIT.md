# RIL-003 — Target Derivation Audit

Status: **PASS — DERIVATION_AUDIT_PASS / TARGET MANIFEST NOT FROZEN / EXECUTION NOT AUTHORIZED**

This audit independently reconstructs the RIL-003 target derivation from the frozen preregistration/implementation inputs and the already-authenticated NIST Beacon pulse. It does **not** create `RIL_003_TARGET_MANIFEST.json`, execute any member, compute preservation, or compute `Lambda`.

## 1. Frozen derivation contract

Preregistration commit:

```text
c5acae018aec09afc9ceece152bb9cdc7a39e112
created: 2026-08-24T16:59:36Z
```

Implementation freeze:

```text
f54d9e1a4d8ef35404824d2172ace173af387a96
created: 2026-08-24T17:12:38Z
```

Both precede the frozen Beacon target time:

```text
2026-08-26T12:00:00.000Z
```

The preregistration freezes:

```text
all-three-essential count = 218
prior exact exclusions    = 25
eligible count            = 193
sample size               = 24
target ID                 = TT_XX (uppercase two-digit hex)
rank domain               = b"RIL-003|TARGET-RANK|"
rank expression           = SHA256(domain + beacon_output_bytes + b"|" + target_id_ascii)
sort                      = digest ascending, then target ID ascending
take                      = first 24
```

Frozen prior exclusions:

```text
TT_17
TT_1B TT_1D TT_27 TT_2E TT_35 TT_3A
TT_47 TT_4E TT_53 TT_5C TT_72 TT_74
TT_8B TT_8D TT_A3 TT_AC TT_B1 TT_B8
TT_C5 TT_CA TT_D1 TT_D8 TT_E2 TT_E4
```

## 2. Frozen authenticated entropy input

The already-custodied and cryptographically authenticated Beacon pulse is:

```text
chainIndex = 2
pulseIndex = 1918805
timeStamp  = 2026-08-26T12:00:00.000Z
```

Frozen 64-byte `outputValue`:

```text
4F95053399C7661D912F51A9A52F8FA65EF0570D917D5E8C8CA0E9804D553B9C777B4E27C35276A2AA97DA8F4B9BD1CDB790E6EA397314991F6EAE6A0BD5BA35
```

Crypto provenance was closed separately in `RIL_003_CRYPTO_PROVENANCE_AUDIT.md`. This audit does not reopen that gate.

## 3. Independent audit method

The audit was implemented independently from the frozen `select_targets()` routine. The frozen helper was not invoked to produce the audit result.

Procedure:

1. Enumerate all 256 8-bit Boolean truth tables.
2. For each table, test x/y/z essentiality directly by comparing inputs differing in exactly one coordinate.
3. Retain tables for which all three coordinates are essential.
4. Remove exactly the frozen 25 prior target values.
5. Encode each survivor as uppercase ASCII `TT_XX`.
6. Decode the frozen Beacon `outputValue` to exactly 64 bytes.
7. Compute the SHA-256 rank digest independently for all 193 survivors.
8. Sort the complete 193-member set by `(digest bytes, target ID)`.
9. Inspect the first 25 positions, not only the provisionally selected 24.
10. Independently construct the ordered 24-row family object and compute its canonical SHA-256 using sorted JSON keys and separators `(',', ':')`, matching the frozen family-integrity representation.

## 4. Eligibility audit

Observed:

```text
all-three-essential tables          = 218
frozen exclusions                   = 25
unique exclusions                   = 25
excluded tables that are essential  = 25
eligible universe                   = 193
```

Checks:

```text
218 expected == 218 observed        PASS
25 expected  == 25 observed         PASS
all exclusions in Ess3              PASS
no excluded value admitted          PASS
no non-essential value admitted     PASS
193 expected == 193 observed        PASS
```

Result:

```text
ELIGIBILITY_AUDIT = PASS
```

## 5. Digest and determinism audit

Frozen ranking expression:

```text
SHA256(
  b"RIL-003|TARGET-RANK|"
  + beacon_output_bytes
  + b"|"
  + target_id_ascii
)
```

Observed across the complete 193-member eligible universe:

```text
rank digests computed = 193
unique rank digests   = 193
rank digest collisions = 0
```

Canonical SHA-256 of the complete independently sorted 193-row ranking object:

```text
62e73097a15d5bd0415fb782e12bb006ea320190686ffc3a38124db613874150
```

Result:

```text
DETERMINISM_AUDIT = PASS
```

## 6. Complete selection-boundary audit

The independently reconstructed first 25 positions are:

| rank | target | truth table | rank digest |
|---:|---|---|---|
| 1 | `TT_B0` | `10110000` | `0156e481784f85240f19d50b55c93801ac66c8907010bf4236dcae98c482f9cc` |
| 2 | `TT_B3` | `10110011` | `0258822b8790cb6fc99943ab9cb1e65e67f66da6fb8791b8b72043d4f928e8a1` |
| 3 | `TT_63` | `01100011` | `035cf8f13e5b60c3d37f813345e448e8e4f49b71f64066f18f1c2e8717988cc7` |
| 4 | `TT_7C` | `01111100` | `0411596886049814e2e85db553575f230ec43269de3b8311614db36cecd13c46` |
| 5 | `TT_13` | `00010011` | `08c7090b176d73e776192e4b634b5d7b79d7f013131e9458567925724dad0524` |
| 6 | `TT_E7` | `11100111` | `0d3eaa45e427699e4f924915f17cb49fd30cceadc59a206ced84ca414a1a2c2e` |
| 7 | `TT_EC` | `11101100` | `0db45d673a090e66bc702ecee96b860f208205e0cd8fbb3b1e953d7cb7cfb495` |
| 8 | `TT_9F` | `10011111` | `10f5caf8a24837a15041f99a0654413c619fd451a3c95df0f5ea007e473f9515` |
| 9 | `TT_F8` | `11111000` | `1205ebe67e53f345ee6c3bd68a198b5988e9b2f097f3a1668b9662af7fb43315` |
| 10 | `TT_52` | `01010010` | `15211e4f2ea3a189ea3d566ebde013979f2a9be52d57e981e1f7a45490c3f389` |
| 11 | `TT_C9` | `11001001` | `1530071385a4c77e7d15772b7e83c9d33b59634fc1fc13abddc61e40ede7edaf` |
| 12 | `TT_86` | `10000110` | `16091d3b32e5a8abba9dd0ad9448bc45659c9137da3f260977fb64d3014ff746` |
| 13 | `TT_FD` | `11111101` | `17b6ef3c6b6e2547a03680b9875fd792e601da5c7b62d2a11e4d4e59d0148b73` |
| 14 | `TT_87` | `10000111` | `18c557e10ab77ea185994bd05c1a92c2b6755da1738921548af51af5f6e1acd5` |
| 15 | `TT_BD` | `10111101` | `18ffa54028d969c6b44a0b609407e6201cab56803ea1068a2c8349e9ba7f9182` |
| 16 | `TT_FE` | `11111110` | `1aa25a2c0cc9e5d137320ad53be863976b860c02efcc769f104de255ee746fd7` |
| 17 | `TT_57` | `01010111` | `1b51a34e441b22483bc9cf0628b02ff4eefb0c3de18bc9cb249e9fbfd23bff32` |
| 18 | `TT_1F` | `00011111` | `1bef14cb9b8abca327ac3b4855d1e7671d218f1df37fa6d45fe627ad18d38e53` |
| 19 | `TT_62` | `01100010` | `1bfccc6fc002e0993a289d207f0ae153dcf8ed1cd4dbdc739b9daef904d3e7ce` |
| 20 | `TT_06` | `00000110` | `1d056ed917d1684b5fbb430aac9c507bedc32bf6eb39daa96e74c90cc3d592b0` |
| 21 | `TT_2D` | `00101101` | `1ecf77c7ee40a4b4ad3c95e1bee755fcc88b366bd0dc5b2f271fc61996ea94a9` |
| 22 | `TT_6A` | `01101010` | `1f19aa6f80cce278369e7f13961f134f22a984fd6ef0d94a4b83763454df7031` |
| 23 | `TT_8A` | `10001010` | `1f8a921d58f1e8b94ba756face1714071efc0ccc9a7f29244307f1ebbacdba28` |
| 24 | `TT_E8` | `11101000` | `22ae50f1af050bf2c5b3c94bb84f0c6de004be2751157e5f1b88946970f7a39a` |
| 25 | `TT_39` | `00111001` | `231bba57333955b25b136eedb307c7e1ed6b382841726ee211fc05fea61a691d` |

Selection-boundary check:

```text
rank(24) target = TT_E8
rank(24) digest = 22ae50f1af050bf2c5b3c94bb84f0c6de004be2751157e5f1b88946970f7a39a

rank(25) target = TT_39
rank(25) digest = 231bba57333955b25b136eedb307c7e1ed6b382841726ee211fc05fea61a691d

rank(24) digest < rank(25) digest
```

Therefore the provisionally derived 24 are exactly the first 24 of the complete 193-way ranking.

Result:

```text
ORDERING_AUDIT = PASS
```

## 7. Ordered family integrity

Audited ordered family:

```text
TT_B0 TT_B3 TT_63 TT_7C TT_13 TT_E7 TT_EC TT_9F
TT_F8 TT_52 TT_C9 TT_86 TT_FD TT_87 TT_BD TT_FE
TT_57 TT_1F TT_62 TT_06 TT_2D TT_6A TT_8A TT_E8
```

Canonical ordered-family SHA-256, using rows of:

```text
member_id
truth_table
hex
rank_digest
```

with JSON `sort_keys=True` and separators `(',', ':')`:

```text
170c074e77fa6cb079be3a51ed3db65aa16b29b616b722bfc0df3055e80e8865
```

The independently reconstructed ordered family matches the previously provisional `F_test` target-for-target, truth-table-for-truth-table, digest-for-digest, and order-for-order.

Result:

```text
FAMILY_INTEGRITY_AUDIT = PASS
```

## 8. Temporal/provenance audit

The target-generation contract and exact prior exclusion set were frozen on 2026-08-24, before the Beacon target time on 2026-08-26.

The derivation used only:

```text
pre-reveal frozen Q_test / exclusion / ranking contract
+ independently authenticated frozen Beacon outputValue
```

It did not use:

```text
member preservation outcomes
member costs
member Lambda values
post-reveal representation changes
post-reveal target-specific search/filter criteria
scientific member results
```

At audit completion there is still no member execution result and `Lambda` remains undefined.

Result:

```text
TEMPORAL_PROVENANCE_AUDIT = PASS
```

## 9. Terminal audit state

```text
ELIGIBILITY_AUDIT         = PASS
DETERMINISM_AUDIT         = PASS
ORDERING_AUDIT            = PASS
FAMILY_INTEGRITY_AUDIT    = PASS
TEMPORAL_PROVENANCE_AUDIT = PASS

DERIVATION_AUDIT          = PASS
```

Therefore:

```text
F_test = DERIVED AND AUDITED
```

with exact ordered family:

```text
(TT_B0, TT_B3, TT_63, TT_7C, TT_13, TT_E7,
 TT_EC, TT_9F, TT_F8, TT_52, TT_C9, TT_86,
 TT_FD, TT_87, TT_BD, TT_FE, TT_57, TT_1F,
 TT_62, TT_06, TT_2D, TT_6A, TT_8A, TT_E8)
```

## 10. Authority ceiling / mandatory stop

This audit earns only the deterministic target-construction result.

It does **not** earn or instantiate:

```text
RIL_003_TARGET_MANIFEST.json
member execution
A_fixed_i
P_i
Lambda_i
family leverage
representation-induced transfer
```

Current state:

```text
CRYPTO_PROVENANCE_PASS = EARNED
F_test                  = DERIVED
DERIVATION_AUDIT        = PASS
TARGET MANIFEST         = ABSENT
MEMBER EXECUTION        = NOT RUN
Lambda                  = UNDEFINED
```

Next legal operation is a separate target-manifest freeze/commit. Member execution must not occur in the same operation.

**STOP.**
