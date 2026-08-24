from rg_001 import MEMORY_BYTES, build_r0, build_r1, reference_parity12


def test_substrate_shape_only():
    assert len(build_r0().memory) == MEMORY_BYTES == 64
    assert len(build_r1().memory) == MEMORY_BYTES == 64


def test_reference_boundary_values_only():
    assert reference_parity12(0) == 0
    assert reference_parity12(1) == 1
    assert reference_parity12(4095) == 0
