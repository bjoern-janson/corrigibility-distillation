# RIL-002 apparatus

Family-transfer apparatus for the frozen 24-member `RIL_002_FAMILY.json`.

The representation pair and core search/update/instrumentation code are inherited by exact blob identity from the RIL-001 implementation freeze. New code only verifies/enumerates the frozen family, constructs the same FS007 datasets with a truth-table target, dispatches inherited arm execution, and adjudicates member/family records.

Do not run family opcode or memory comparisons before the implementation freeze and pre-execution audit.
