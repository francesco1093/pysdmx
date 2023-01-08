from pysdmx import get_dimensions

def test_get_dimensions():
    assert isinstance(get_dimensions('ECB','EXR'), list)