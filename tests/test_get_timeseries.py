from pysdmx import get_timeseries

def test_get_timeseries_v2():
    timeseries=get_timeseries('ECB',id='EXR.A.USD.EUR.SP00.A')
    print(timeseries)
    timeseries=get_timeseries('ECB',id='EXR.Q.USD.EUR.SP00.A')
    print(timeseries)
    #timeseries=get_timeseries('ECB',id='EXR.B.USD.EUR.SP00.A')
    #print(timeseries)
    timeseries=get_timeseries('ECB',id='EXR.D.USD.EUR.SP00.A')
    print(timeseries)
    # timeseries=get_timeseries('ECB',id='EXR.S.USD.EUR.SP00.A')
    # print(timeseries)
    # timeseries=get_timeseries('ECB',id='EXR.E.USD.EUR.SP00.A')
    # print(timeseries)
    # timeseries=get_timeseries('ECB',id='EXR.W.USD.EUR.SP00.A')
    # print(timeseries)
    timeseries=get_timeseries('ECB',id='EXR.H.USD.EUR.SP00.A')
    print(timeseries)
    timeseries=get_timeseries('ECB',id='EXR.M.USD.EUR.SP00.A')
    print(timeseries)
    assert isinstance(timeseries, list)

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