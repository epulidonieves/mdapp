import mdapp


def test_convert_value_to_bool():
    assert mdapp.value_to_bool(3)
    assert not mdapp.value_to_bool(None)
