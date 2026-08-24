# RIL-003 apparatus

This directory implements the frozen RIL-003 preregistration **without revealing targets**.

Before `2026-08-26T12:00:00.000Z`, only static/pre-reveal audit and environment-manifest operations are scientifically legal. The apparatus contains no Beacon network client. Later target reveal requires an externally captured NIST Beacon 2.0 pulse package; `reveal-targets` enforces the frozen wall-clock boundary and deterministically materializes the preregistered 24-target manifest.

The AST/SEM8 predictors, shared corrective algorithm, and opcode/memory instrumentation are inherited from the exact frozen RIL-001 implementation blobs. No representation adaptation is permitted.
