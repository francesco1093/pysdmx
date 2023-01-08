try:
    import jnius_config
    jnius_config.set_classpath('inst/java/SDMX.jar')
except:
    pass

from jnius import autoclass
CLIENT_HANDLER = 'it.bancaditalia.oss.sdmx.client.SdmxClientHandler'
SdmxClientHandler = autoclass(CLIENT_HANDLER)

UTILS_HANDLER = "it.bancaditalia.oss.sdmx.util.Utils"
Utils = autoclass(UTILS_HANDLER)

HELPER = "it.bancaditalia.oss.sdmx.helper.SDMXHelper"
Helper = autoclass(HELPER)