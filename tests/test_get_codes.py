from pysdmx import get_codes

def test_get_codes():
    assert isinstance(get_codes('ECB','EXR','FREQ'), dict)