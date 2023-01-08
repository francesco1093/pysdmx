from pysdmx import get_codes, get_dimensions, get_dsd_identifier, get_flows, get_providers, get_timeseries
import matplotlib.pyplot as plt

#https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html

def print_list(ls):
    for l in ls:
        print(l)

def print_dict(d):
    for k, v in d.items():
        print(k, ': ', v)


#print(get_timeseries('WITS', dataflow='DF_WITS_Tariff_TRAINS', id='.840.000.020110.reported'))

print_dict(get_providers())
provider = input("\nChoose provider : ")

#addProvider('TEST', "http://sdw-wsrest.ecb.europa.eu/service", F)

#getProviders()
#input("\nType  <Return>\t to continue : ")

print_dict(get_flows(provider))
dataflow = input("\nChoose dataflow : ")

print(get_dsd_identifier(provider, dataflow))
input("\nPress enter : ")

def select_over(dim):
    print('Dimension: ', dim)
    codes = get_codes(provider, dataflow, dim.id)
    print_dict(codes)
    selection = None
    while selection not in codes.keys() or selection is None:
        selection = input(f'Insert <{dim.full_identifier}>: ')
        print(selection)
    return selection, (dim.id, codes[selection])

final_selection = [select_over(dim) for dim in get_dimensions(provider, dataflow)]

id = '.'.join([a for a, _ in final_selection])
sels = '\n'.join([a + ': ' + b for _, (a, b) in final_selection])
print(id)
print(sels)
input("\nType  <Return>\t to continue : ")

ans=get_timeseries(provider, dataflow=dataflow, id=id)
ts = ans[0].timeseries
print(ts)

plt.plot(range(len(ts)), ts)
plt.xticks(range(len(ts)), ts.index, size='small', rotation=45)
plt.show()

""" print(get_flows('EUROSTAT'))
input("\nType  <Return>\t to continue : ")

print(get_dimensions('EUROSTAT', 'prc_hicp_midx'))
input("\nType  <Return>\t to continue : ")

ans=get_timeseries('EUROSTAT', 'prc_hicp_midx/..CP00.EU+DE+FR')
print(ans)
#plot(ans[[1]], main=names(ans)[[1]])

#sdmxHelp() """



#print(get_dsd_identifier('ECB','EXR'))
#print(get_flows('ECB', '*EXR*'))
#print(get_dimensions('ECB','EXR'))
#print(get_providers())
#print(get_codes('ECB', 'EXR', 'FREQ'))
#print(get_timeseries('ECB', dataflow='EXR', id='A.USD.EUR.SP00.A'))
#print(get_providers())
#print(get_flows('WITS', '*Devlo*'))
#print(get_dimensions('WITS','WBG_WITS,DF_WITS_TradeStats_Development,1.0'))
#print(get_codes('ECB','EXR', 'FREQ'))
#print(get_timeseries('WITS', dataflow='WBG_WITS,DF_WITS_TradeStats_Development,1.0'))
#print(get_timeseries_table('ECB', dataflow='EXR', id='A.USD.EUR.SP00.A'))
# flows = SdmxClientHandler.getFlows('ECB', '')
# print(flows.keySet().toArray())
# print(flows.values().toArray())
#print(get_timeseries_revisions('ECB', id='EXR.A.USD.EUR.SP00.A', updated_after='2023', include_history=False))