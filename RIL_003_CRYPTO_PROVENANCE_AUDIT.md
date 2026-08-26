# RIL-003 — Beacon Cryptographic Provenance Audit

Status: **PASS — CRYPTO_PROVENANCE_PASS / TARGET DERIVATION NOT PERFORMED / EXECUTION NOT AUTHORIZED**

This audit closes only the external source-authenticity gate for the already-frozen RIL-003 NIST Beacon custody package. It does **not** derive `F_test`, rank targets, create `RIL_003_TARGET_MANIFEST.json`, or execute any RIL-003 member.

## 1. Frozen custody inputs

Pulse custody artifact:

```text
experiments/ril_003/custody/NIST_BEACON_2_CHAIN_2_PULSE_1918805.json
Git blob: 36758cffd2418f9050643de86f7c13a9022503f8
custody commit: fe87e15d75d4386b80aeccdc30f2ed185f69b9ba
```

Certificate custody artifact:

```text
experiments/ril_003/custody/NIST_BEACON_CERT_528943a555f5f8ca54423be6dfb95925a35c7b552046420e7d7cd072058a14d6536ad3a8e9754b6582f164a90b0cd86a65d659f5426a2659a947595d1c816c8c.pem
Git blob: 299611f535e795eae65b324af2f4d6cfb18113fb
custody commit: 473a1b8a31a5bdbc3a061f64ed5fd0e230a6e0d7
```

Frozen pulse identity:

```text
version        = 2.0
cipherSuite    = 0
chainIndex     = 2
pulseIndex     = 1918805
timeStamp      = 2026-08-26T12:00:00.000Z
statusCode     = 0
certificateId = 528943a555f5f8ca54423be6dfb95925a35c7b552046420e7d7cd072058a14d6536ad3a8e9754b6582f164a90b0cd86a65d659f5426a2659a947595d1c816c8c
outputValue    = 4F95053399C7661D912F51A9A52F8FA65EF0570D917D5E8C8CA0E9804D553B9C777B4E27C35276A2AA97DA8F4B9BD1CDB790E6EA397314991F6EAE6A0BD5BA35
```

## 2. Certificate parse and identity binding

The frozen PEM parses as an X.509 certificate with:

```text
Subject:
CN=engine.beacon.nist.gov,
O=National Institute of Standards and Technology,
L=Gaithersburg,
ST=Maryland,
C=US

Issuer:
CN=DigiCert Global G2 TLS RSA SHA256 2020 CA1,
O=DigiCert Inc,
C=US

RSA public key size: 4096 bits
Validity: 2025-08-28T00:00:00Z through 2026-09-04T23:59:59Z
SAN: engine.beacon.nist.gov
KeyUsage: digitalSignature=true
```

DER fingerprints:

```text
SHA-256 = 67e1c70f0654421f589f3c908480f6edbadc3521e2798b2b4718dfb4f3c77288
SHA-512 = 528943a555f5f8ca54423be6dfb95925a35c7b552046420e7d7cd072058a14d6536ad3a8e9754b6582f164a90b0cd86a65d659f5426a2659a947595d1c816c8c
```

Therefore:

```text
SHA512(DER certificate) == pulse.certificateId
```

Result:

```text
CERTIFICATE_ID_BINDING = PASS
```

## 3. CA chain verification

The leaf certificate signature verifies under:

```text
DigiCert Global G2 TLS RSA SHA256 2020 CA1
SHA-256 fingerprint:
c8025f9fc65fdfc95b3ca8cc7867b9a587b5277973957917463fc813d0b625a9
```

That intermediate fingerprint agrees with DigiCert's published certificate listing. The intermediate signature verifies under the locally trusted:

```text
DigiCert Global Root G2
SHA-256 fingerprint:
cb3ccbb76031e5e0138f8dd39a23f9de47ffc35e43c1144cea27d46a5ab1cb5f
```

At `2026-08-26T12:00:00Z`, leaf, intermediate, and root are all inside their validity intervals.

Result:

```text
CERTIFICATE_CHAIN = PASS
```

No independent OCSP/CRL revocation-status query was performed in this audit. The PASS here is the cryptographic chain/identity result required to bind the pulse signing key to the CA-issued NIST certificate.

## 4. Signature serialization discrepancy and implemented format

The draft NISTIR 8213 byte-serialization text describes 8-byte length prefixes for non-integer fields and an 8-byte `external.statusCode`. Applied literally to this pulse, that draft serialization produces an 863-byte preimage and does **not** verify the live pulse signature or reproduce `outputValue`.

The live Beacon 2.0 implementation instead uses the field order from the reference but with:

```text
string / hex-field length prefix = uint32 big-endian (4 bytes)
external.statusCode              = uint32 big-endian (4 bytes)
chainIndex / pulseIndex          = uint64 big-endian (8 bytes)
all other integer fields         = uint32 big-endian (4 bytes)
```

Using the exact frozen pulse fields in their emitted order gives:

```text
signature-input byte length = 807
SHA-512(signature-input) =
ebdaec331afb310e7e1e4ad9b7556f43fae6ffe21790d90893fc2baa9ff793bff92676dd86db9171ddf57a1fdb29e967919e98d3776b12e697fee4c7d4d56b18
```

This format is independently documented by a public Beacon 2.0 verification implementation and is mechanically selected here by the stronger test: it verifies the frozen pulse's RSA signature under the certificate-bound public key and reproduces the pulse output exactly.

## 5. RSA pulse-signature verification

For `cipherSuite = 0`, verify the 512-byte `signatureValue` using:

```text
RSA-4096
PKCS#1 v1.5
SHA-512
public key = frozen certificate public key
message    = exact 807-byte implemented signature input
```

Result:

```text
RSA_SIGNATURE = PASS
```

This establishes that the frozen pulse fields were signed by the private key corresponding to the certificate whose DER SHA-512 equals the signed `certificateId` field.

## 6. Output-value binding

Compute:

```text
SHA512(signature_input || signatureValue)
```

Observed:

```text
4F95053399C7661D912F51A9A52F8FA65EF0570D917D5E8C8CA0E9804D553B9C777B4E27C35276A2AA97DA8F4B9BD1CDB790E6EA397314991F6EAE6A0BD5BA35
```

This is exactly the frozen pulse `outputValue`.

Result:

```text
OUTPUT_VALUE_BINDING = PASS
```

## 7. External authority references

NIST CSRC documents that Beacon 2.0 pulses are timestamped and signed, that the certificate for each pulse is exposed through the certificate API, and that cipher suite 0 uses SHA-512 with RSA PKCS#1 v1.5.

Reference:

```text
https://csrc.nist.gov/projects/interoperable-randomness-beacons/beacon-20
https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8213-draft.pdf
```

DigiCert publishes the intermediate certificate identity/fingerprint used above:

```text
https://knowledge.digicert.com/general-information/digicert-trusted-root-authority-certificates
```

## 8. Verdict

```text
raw Beacon package custody           PASS
boundary timestamp                   PASS
certificate custody                  PASS
certificateId -> certificate binding PASS
certificate chain                    PASS
RSA pulse signature                  PASS
outputValue binding                  PASS

CRYPTO_PROVENANCE_PASS               PASS
```

Therefore the external source-authenticity gate required before target derivation is closed positively for the frozen pulse:

```text
chain 2 / pulse 1918805 / 2026-08-26T12:00:00.000Z
```

The next legal RIL-003 transition is now:

```text
CRYPTO_PROVENANCE_PASS
-> derive F_test exactly once using the already-frozen generator
-> freeze RIL_003_TARGET_MANIFEST.json
-> audit deterministic derivation
-> commit manifest
-> STOP
```

This audit performs none of those downstream operations.

## Terminal state

```text
RIL-003 crypto provenance = PASS
F_test                    = NOT DERIVED
TARGET MANIFEST           = ABSENT
member preservation       = NOT RUN
member cost execution     = NOT RUN
Lambda vector             = DOES NOT EXIST
```
