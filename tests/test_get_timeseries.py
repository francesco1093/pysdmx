from pysdmx.sdmx_client import get_timeseries
import pandas as pd

def test_get_timeseries_v2():
    # SDMX V2
    ## get single time series:
    timeseries=get_timeseries('ECB',id='EXR.H.USD.EUR.SP00.A')
    print(timeseries)
    # print(timeseries[0])
    print(timeseries[0].index)
    # #timeseries[0].index.freq = 'D'
    # print(timeseries[0].index.freq)
    # print(pd.infer_freq(timeseries[0].index))
    # timeseries[0].index.freq = pd.infer_freq(timeseries[0].index)
    # print(timeseries[0].index)
    # #print(timeseries[0].attrs)
    # print('Name ', timeseries[0].name)
    assert isinstance(timeseries, list)

    #print(attrs)
    #assert isinstance(attrs, dict)
    ## get monthly and annual frequency: 
    #my_ts=get_timeseries('ECB',id='EXR.A+M.USD.EUR.SP00.A')
    ## get all available frequencies: 
    #my_ts=get_timeseries('ECB',id='EXR..USD.EUR.SP00.A')

print(test_get_timeseries_v2())

'''
# SDMX V3

## get single time series: 
my_ts=get_timeseries('ECB', dataflow='EXR', id='A.USD.EUR.SP00.A')
## get monthly and annual frequency: 
my_ts=get_timeseries('ECB', dataflow='EXR', id='A+M.USD.EUR.SP00.A')
## get all available frequencies: 
my_ts=get_timeseries('ECB', dataflow='EXR', id='.USD.EUR.SP00.A')

#or

## get single time series: EXR.A.USD.EUR.SP00.A
my_ts=get_timeseries('ECB', dataflow='EXR', filter='c[FREQ]=A&c[CURRENCY]=USD&c[CURRENCY_DENOM]=EUR&c[EXR_TYPE]=SP00&c[EXR_SUFFIX]=A')
## get monthly and annual frequency: 
my_ts=get_timeseries('ECB', dataflow='EXR', filter='c[FREQ]=A,M&c[CURRENCY]=USD&c[CURRENCY_DENOM]=EUR&c[EXR_TYPE]=SP00&c[EXR_SUFFIX]=A')
## get all available frequencies: 
my_ts=get_timeseries('ECB', dataflow='EXR', filter='c[CURRENCY]=USD&c[CURRENCY_DENOM]=EUR&c[EXR_TYPE]=SP00&c[EXR_SUFFIX]=A')
'''