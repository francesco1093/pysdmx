from pysdmx import get_flows

def test_get_flows():
    assert isinstance(get_flows('ECB'), dict)