from pysdmx.sdmx_client import get_providers

def test_get_providers():
    assert isinstance(get_providers(), dict)
