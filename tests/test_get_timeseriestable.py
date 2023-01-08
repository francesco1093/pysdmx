from pysdmx import get_timeseries_table
import pandas as pd

def test_get_timeseries_table():
    assert isinstance(get_timeseries_table('ECB',id='EXR.A.USD.EUR.SP00.A'), pd.DataFrame)