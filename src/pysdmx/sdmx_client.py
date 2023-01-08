from typing import Dict
from .JVM_Setup import SdmxClientHandler, Helper
from .ts_converter import convert_hashtable, convert_dim_list, convert_timeseries_list, convert_timeseries_dataframe

def get_providers():
    """Extract the list of available Data Providers. 
    
    This function is used to query the list of currently available data providers.

    Parameters
    ----------

    Returns
    -------
    Dict[str, str]
        dict-like object where keys are words and values are counts.

    Examples
    --------
    >>> get_providers()
    """
    providers = SdmxClientHandler.getProviders()
    return convert_hashtable(providers)

def add_provider(name, endpoint, needsCredentials=False, needsURLEncoding=False, supportsCompression=True, description=''):
    """Add new provider. 
    
    Configure a new data provider (only SDMX 2.1 REST providers are supported). This function can be used to configure a new (SDMX 2.1 compliant, REST based) data provider.
    
    Parameters
    ----------
    name : str
        the name of the provider
    endpoint: str
     the URL where the provider resides
    needsCredentials : bool 
        set this to TRUE if the user needs to authenticate to query the provider
    supportsCompression : bool 
        set this to TRUE if the provider is able to handle compression
    description : str
        a brief text description of the provider
    """
    SdmxClientHandler.addProvider(name, endpoint, needsCredentials, needsURLEncoding, supportsCompression, description)


def get_dsd_identifier(provider, dataflow):
    """Extracts the dsd identifier of a DataFlow. 
    
    This function is used to retrieve the name of the keyfamily of the input dataflow.
    
    Parameters
    ----------
    provider : str
        Name of the provider.
    dataflow : str
        Identifier of the dataflow.

    Returns
    -------
    str
        name of the keyfamily of the input dataflow.

    Examples
    --------
    >>> id = get_dsd_identifier('ECB','EXR')
    """
    dsd = SdmxClientHandler.getDSDIdentifier(provider, dataflow)
    return dsd.toString()

def get_flows(provider, pattern = ''):
    """Extract the list of DataFlows of a provider. 
    
    This function is used to query the list of dataflows of the provider. A matching pattern can be provided, if needed. 
    
    Parameters
    ----------
    provider : str
        Name of the provider.
    pattern : str
        Pattern to match against the dataflow id or description. If a pattern is not provided, all dataflows are returned.
    Returns
    -------
    Dict[str, str]
        dict-like object where keys are codes and values are descriptions.

    Examples
    --------
    >>> ## get all flows from ECB
    >>> flows = get_flows('ECB')
    >>> ## get all flows that contain the 'EXR
    >>> flows = get_flows('ECB','*EXR*')
    """
    flows = SdmxClientHandler.getFlows(provider, pattern)
    return convert_hashtable(flows)

def get_dimensions(provider, dataflow):
    """Extract the dimensions of a DataFlow. 
    
    This function is used to retrieve the list of dimensions of the input dataflow
     
    Parameters
    ----------
    provider : str
        Name of the provider.
    dataflow : str
        Identifier of the dataflow.

    Returns
    -------
    Dict[str, str]
        dict-like object where keys are dimension ids and values are their descriptions.

    Examples
    --------
    >>> dims = get_dimensions('ECB','EXR')
    """
    dimensions = SdmxClientHandler.getDimensions(provider, dataflow)
    return convert_dim_list(dimensions)

def get_codes(provider, dataflow, dimension):
    """Extract the codes relative to a specific dimension. 
    
    This function is used to retrieve the list of codes of the input dimension
     
    Parameters
    ----------
    provider : str
        Name of the provider.
    dataflow : str
        Identifier of the dataflow.
    dimension : str
        Identifier of the dimension.

    Returns
    -------
    Dict[str, str]
        dict-like object where keys are code ids and values are their descriptions.

    Examples
    --------
    >>> codes = get_codes('ECB','EXR','FREQ')
    """
    codes = SdmxClientHandler.getCodes(provider, dataflow, dimension)
    codes_dict = convert_hashtable(codes)
    return codes_dict

def get_timeseries(provider, id ='', start ='', end ='', dataflow ='', filter =''):
    """Extract a list of time series. 
    
    This function is used to extract a list of time series identified by the parameters provided in input.     
    
    Parameters
    ----------
    provider : str
        Name of the provider
    id : str
        Timeseries key
    start: str
        Start time - optional
    end: str
        End time - optional
    dataflow : str
        Identifier of the dataflow - optional
    filter : str
        Filter to be applied - optional

    Returns
    -------
    list
        A list of time series identified by the parameters provided in input.
    Dict[str, str]
        A dictionary containing time series attributes

    Examples
    --------
    >>> SDMX V2
    >>> ## get single time series:
    >>> my_ts=get_timeseries('ECB',id='EXR.A.USD.EUR.SP00.A')
    >>> ## get monthly and annual frequency: 
    >>> my_ts=get_timeseries('ECB',id='EXR.A+M.USD.EUR.SP00.A')
    >>> ## get all available frequencies: 
    >>> my_ts=get_timeseries('ECB',id='EXR..USD.EUR.SP00.A')
    >>> 
    >>> # SDMX V3
    >>> 
    >>> ## get single time series: 
    >>> my_ts=get_timeseries('ECB', dataflow='EXR', id='A.USD.EUR.SP00.A')
    >>> ## get monthly and annual frequency: 
    >>> my_ts=get_timeseries('ECB', dataflow='EXR', id='A+M.USD.EUR.SP00.A')
    >>> ## get all available frequencies: 
    >>> my_ts=get_timeseries('ECB', dataflow='EXR', id='.USD.EUR.SP00.A')
    >>> 
    >>> #or
    >>> 
    >>> ## get single time series: EXR.A.USD.EUR.SP00.A
    >>> my_ts=get_timeseries('ECB', dataflow='EXR', filter='c[FREQ]=A&c[CURRENCY]=USD&c[CURRENCY_DENOM]=EUR&c[EXR_TYPE]=SP00&c[EXR_SUFFIX]=A')
    >>> ## get monthly and annual frequency: 
    >>> my_ts=get_timeseries('ECB', dataflow='EXR', filter='c[FREQ]=A,M&c[CURRENCY]=USD&c[CURRENCY_DENOM]=EUR&c[EXR_TYPE]=SP00&c[EXR_SUFFIX]=A')
    >>> ## get all available frequencies: 
    >>> my_ts=get_timeseries('ECB', dataflow='EXR', filter='c[CURRENCY]=USD&c[CURRENCY_DENOM]=EUR&c[EXR_TYPE]=SP00&c[EXR_SUFFIX]=A')
    """
    ts = SdmxClientHandler.getTimeSeries(provider, dataflow, id, filter, start, end, False, None, False)
    return convert_timeseries_list(ts)

def get_timeseries_table(provider, id='', start='', end='', dataflow='', filter=''):
    """Extract a list of time series as Pandas DataFrame
 
    This function is used to extract a list of time series identified by the parameters provided in input, and return a Pandas DataFrame as result

    Parameters
    ----------
    provider : str
        Name of the provider
    id : str
        Timeseries key
    start: str
        Start time - optional
    end: str
        End time - optional
    dataflow : str
        Identifier of the dataflow - optional
    filter : str
        Filter to be applied - optional

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame of time series identified by the parameters provided in input
    Dict[str, str]
        A dictionary containing time series attributes

    Examples
    --------
    >>> SDMX V2
    >>> ## get single time series:
    >>> my_ts=get_timeseries_table('ECB',id='EXR.A.USD.EUR.SP00.A')
    >>> ## get monthly and annual frequency: 
    >>> my_ts=get_timeseries_table('ECB',id='EXR.A+M.USD.EUR.SP00.A')
    >>> ## get all available frequencies: 
    >>> my_ts=get_timeseries_table('ECB',id='EXR..USD.EUR.SP00.A')
    >>> 
    >>> # SDMX V3
    >>> 
    >>> ## get single time series: 
    >>> my_ts=get_timeseries_table('ECB', dataflow='EXR', id='A.USD.EUR.SP00.A')
    >>> ## get monthly and annual frequency: 
    >>> my_ts=get_timeseries_table('ECB', dataflow='EXR', id='A+M.USD.EUR.SP00.A')
    >>> ## get all available frequencies: 
    >>> my_ts=get_timeseries_table('ECB', dataflow='EXR', id='.USD.EUR.SP00.A')
    >>> 
    >>> #or
    >>> 
    >>> ## get single time series: EXR.A.USD.EUR.SP00.A
    >>> my_ts=get_timeseries_table('ECB', dataflow='EXR', filter='c[FREQ]=A&c[CURRENCY]=USD&c[CURRENCY_DENOM]=EUR&c[EXR_TYPE]=SP00&c[EXR_SUFFIX]=A')
    >>> ## get monthly and annual frequency: 
    >>> my_ts=get_timeseries_table('ECB', dataflow='EXR', filter='c[FREQ]=A,M&c[CURRENCY]=USD&c[CURRENCY_DENOM]=EUR&c[EXR_TYPE]=SP00&c[EXR_SUFFIX]=A')
    >>> ## get all available frequencies: 
    >>> my_ts=get_timeseries_table('ECB', dataflow='EXR', filter='c[CURRENCY]=USD&c[CURRENCY_DENOM]=EUR&c[EXR_TYPE]=SP00&c[EXR_SUFFIX]=A')
    """    
    tst = SdmxClientHandler.getTimeSeriesTable(provider, dataflow, id, filter, start, end, False, None, False)
    return convert_timeseries_dataframe(tst)

def get_timeseries_revisions(provider, id='', start='', end='', updated_after='', include_history=True):
    """Extract time series updates
    
    This function is used to extract time series starting from a specific update time and with history of revisions. This function works as get_timeseries_table but the query can be narrowed to getting only observations that were updated after a specific point in time, and eventually it returns the revision history of the matching time series. The result is packed into a pandas DataFrame

    
    Parameters
    ----------
    provider : str
        Name of the provider
    id : str
        Timeseries key
    start: str
        Start time - optional
    end: str
        End time - optional
    updated_after : str
        Used to select only records modified after a certain date (format 'YYYY-MM-DD') - optional
    include_history : bool
        If true the full list of revisions will be returned - optional

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame of time series identified by the parameters provided in input
    Dict[str, str]
        A dictionary containing time series attributes

    Examples
    --------
    >>> # get single time series with history: 
    >>> my_ts=get_timeseries_revisions('ECB','EXR.A.USD.EUR.SP00.A', includeHistory=TRUE)
    >>> # get single time series (only observations updated after january 1st 2015): 
    >>> my_ts=get_timeseries_revisions('ECB','EXR.A.USD.EUR.SP00.A', updatedAfter='2015', includeHistory=F)
    >>> # get single time series (full revision history starting from january 1st 2015): 
    >>> my_ts=get_timeseries_revisions('ECB','EXR.A.USD.EUR.SP00.A', updatedAfter='2015', includeHistory=TRUE)
    """
    tst = SdmxClientHandler.getTimeSeriesTable(provider, None, id, None, start, end, False, updated_after, include_history)
    return convert_timeseries_dataframe(tst)

import shutil
import subprocess
import os
def sdmx_help(internalJVM=True):
  # fix for #41 on OS X
    if internalJVM:
        Helper.start()
    else:
        JAVA = shutil.which('java')
        print(JAVA)
        if len(JAVA) > 0 and len(JAVA[1]) > 0:
             javaExe = JAVA
             print('JVM detected: ', javaExe)
             print(os.getcwd())
             os.chdir('inst/java/')
             print(os.getcwd())
             subprocess.run([javaExe, ' -jar', 'SDMX.jar', 'it.bancaditalia.oss.sdmx.helper.SDMXHelper'])
            
        else:
            print('Could not detect external JVM.')
        

