# RD-001 Calibration Seed v2

**Status:** `BEACON CAPTURED / CAL SEED DERIVED / MANIFEST LOCALLY MATERIALIZED / SCIENTIFIC ARM COMPARISON NOT RUN`

Preregistration commit:

`bb0a85182a59a498568fa2905a49802af35b56b4`

V2 implementation freeze:

`7d5fb20d73f47dab4d6dae72ad3ad16ad6443ea7`

Frozen v2 source SHA-256:

`08cc82e528b400617c72e768811748b936315e3195c0658e374d3262799c95e2`

Selected drand round:

`6405789`

Captured randomness:

`24ee3fa7b7832d19d911e6cd510bba5e6a8e98977d72dd011a1412dac894a470`

Frozen derivation:

`SHA256(raw32(randomness) || raw20(prereg_commit) || UTF8("RD001/CAL"))`

Derived calibration seed:

`1ee66660adc596f5d0104e3310f4dedb3602b4f5379eda13011c5519a3a17b6f`

The frozen v2 generator was then invoked locally as:

```text
python rd001_v2_frozen.py generate \
  --seed 1ee66660adc596f5d0104e3310f4dedb3602b4f5379eda13011c5519a3a17b6f \
  --role CAL \
  --count 24 \
  --out RD001_CALIBRATION_MANIFEST_V2.json
```

Local materialization diagnostics before any scientific arm comparison:

```text
manifest_sha256 = 01f0211272291ad9c553a5cd7ff31128f981cd0e5892a97dc18484549b562d86
role            = CAL
count           = 24
unique_layouts  = 24
n counts        = {7:9, 8:7, 9:8}
k counts        = {3:12, 4:9, 5:3}
|J| counts      = {1:10, 2:14}
max candidate   = 23
```

No calibration cost comparison, leverage statistic, or scientific verdict was computed before this seed/materialization record.

The complete manifest must be committed and audited before the `calibrate` command is legally opened.
