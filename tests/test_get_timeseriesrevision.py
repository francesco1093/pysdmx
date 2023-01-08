from pysdmx import get_timeseries_revisions
import pandas as pd

def test_get_timeseries_revisions():
    assert isinstance(get_timeseries_revisions('ECB',id='EXR.A.USD.EUR.SP00.A'), pd.DataFrame)