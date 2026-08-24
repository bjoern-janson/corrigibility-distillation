from instrument_v2 import OpcodeCounterV2


def one_line(): return 1


def test_one_line_trace_activation():
    c = OpcodeCounterV2((one_line.__code__,))
    _, n = c.run(one_line)
    assert n > 0
