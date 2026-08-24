# RG-002 apparatus

Instrumentation-repair assay for RG-001. It inherits the exact frozen RG-001 `PARITY12`, `LOOP12`, `LUT6`, 64-byte substrate, and 512-fault robustness contract.

The sole scientific-apparatus change is corrected CPython opcode tracing: target frames enable opcode events on both `call` and `line` events.

RG-002 is not an independent replication and has no interaction with RIL-003.
