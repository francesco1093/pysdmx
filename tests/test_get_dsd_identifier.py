from pysdmx import get_dsd_identifier

def test_get_dsd_identifier():
    assert isinstance(get_dsd_identifier('ECB', 'EXR'), str)