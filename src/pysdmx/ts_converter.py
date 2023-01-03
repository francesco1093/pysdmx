from collections import namedtuple
import pandas as pd
from .JVM_Setup import Utils

#This function is used to convert an input list of SDMX dimensions into a list of Dimension namedtuples, containing the dimension id and full identifier. The dimension id can be used to query dimension codes via the function get_codes

def convert_dim_list(dl):
    """Converts the list of SDMX dimensions to a Python list. 
    
    This function is used to convert an input list of SDMX dimensions into a list of Dimension namedtuples, containing the dimension id and full identifier. The dimension id can be used to query dimension codes via the function get_codes
    """
    dimensions_list = dl.toArray()
    Dimension = namedtuple("Dimension", "id full_identifier")
    dimensions_namedtuples = [Dimension(d.getId(), d.getCodeList().getFullIdentifier()) for d in dimensions_list]
    return dimensions_namedtuples

def convert_hashtable(ht):
    return {key: ht.get(key) for key in ht.keySet()} 

def convert_timeseries_list(tsl):
    timeseries_list = tsl.toArray()
    return list(map(convert_single_timeseries, timeseries_list))

def convert_timeseries_dataframe(table):
    attrs = dict()
    attrs['IS_NUMERIC'] = table.isNumeric()
    time = table.getTimeStamps()
    values = table.getObservations()
    if attrs['IS_NUMERIC']:
        observations = values
    else:
        #untested TODO
        observations = [o.toString() for o in values]

    meta_names = table.getMetadataNames()
    meta_list = [table.getMetadata(name) for name in meta_names]
    meta_names = ['OBS_VALUE', 'TIME_PERIOD'] + meta_names
    meta_list = [observations, time] + meta_list
    result = pd.DataFrame([list(i) for i in zip(*meta_list)], columns=meta_names)

    #handling errors
    error_objects = None
    if table.isErrorFlag():
        error_objects = table.getErrorObjects()
        attrs['ERROR_OBJECTS'] = error_objects
        raise Warning('The results contain errors. Please check the ERROR_OBJECTS attribute')
    return result, attrs
    
def convert_single_timeseries(jpts, plain = False):
    freq = jpts.getFrequency()
    print(freq)
    time_slots = jpts.timeSlotsArray
    print(time_slots)
    print()

    if jpts.isNumeric():
        observations = Utils.toDoubleArray(jpts)
    else:
        #untested TODO
        observations = [o.toString() for o in jpts.getObservations()]

    num_obs = len(observations)
    num_times = len(time_slots)

    attrs = dict()
    if num_obs > 0 and num_obs == num_times:
        if freq is None:
            print(jpts.getName(), ": frequency is NULL. Irregular timeseries defined")	 
        result = make_SDMXTS(freq, time_slots, observations, plain)

        #set attributes missing!! TODO
        #attrs <- attributes(result)
        
        attrs.update({a: jpts.getObsLevelAttributes(a).toArray() for a in jpts.getObsLevelAttributesNames().toArray()})
        attrs.update({a.getKey() : a.getValue() for a in jpts.getDimensionsMap().entrySet().toArray()})
        attrs.update({a.getKey() : a.getValue() for a in jpts.getAttributesMap().entrySet().toArray()})
        attrs["ID"] = jpts.getName()
        attrs['IS_NUMERIC'] = jpts.isNumeric()

        #check errors
        err_flag = attrs["IS_ERROR"] = jpts.isErrorFlag()
        if err_flag:
            attrs["ERROR_MSG"] = jpts.getErrorMessage()
            print('The time series ', jpts.getName(), ' contains errors. Please check the ERROR_MSG attribute')

        result.name = jpts.getName()
        result.attrs.update(attrs)

    else:
        print("Warning building timeseries '", jpts.getName(), "': number of observations and time slots equal to zero, or not matching: ", num_obs, " ", num_times, "\n")
    return result

def zoo(values, order_by):
    return values

# currently not validating timeseries frequency as it is done in zoo
def make_SDMXTS(freq, times, values, enforce_format = None):
    if len(values) > 0:
        if not enforce_format:
            tmp_ts = pd.Series(values, index=pd.to_datetime(times))

        elif enforce_format == 'plain':
            # format will always be: yyyy-mm-ddThh:mm:ss
            return
            '''
            if freq is None:
                tmp_ts = zoo(values, order_by = "Date(times)")

            else:
                if freq == 'M':
                    tmp_ts = zoo(values, order_by = "yearmon(Date(times)),frequency=12")
                elif(freq == 'Q'):
                    tmp_ts = zoo(values, order_by = "yearqtr(Date(times)),frequency=4")
                else:
                    tmp_ts = zoo(values, order_by = "Date(times)")
            '''
        else:
            #do we need distinct cases? do we need to set freq
            if freq == 'A':
                # we expect a string year ('1984')
                tmp_ts = pd.Series(values, index=pd.to_datetime(times, format='%Y'))
                tmp_ts.index.freq = pd.infer_freq(tmp_ts.index)
                assert tmp_ts.index.freq == 'AS-JAN'
            elif freq == 'M':
                # we expect '1984-02'
                #times = sub(pattern='M', replacement='-', times) # OECD only '1984-M2'
                tmp_ts = pd.Series(values, index=pd.to_datetime(times, format='%Y-%m'))
            elif freq == 'Q':
                # we expect '1984-Q2' TODO
                tmp_ts = pd.Series(values, index=pd.to_datetime(times))
            elif freq == 'D' or freq == 'B':
                # we expect '1984-03-27'
                tmp_ts = pd.Series(values, index=pd.to_datetime(times, format='%Y-%m-%d'))
            
            
            else:
                # nothing we can forecast
                tmp_ts = pd.Series(values, index=pd.to_datetime(times))

    else:
        tmp_ts = pd.Series()

    return tmp_ts