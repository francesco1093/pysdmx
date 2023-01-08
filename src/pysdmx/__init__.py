# read version from installed package
from importlib.metadata import version
__version__ = version("pysdmx")

from .sdmx_client import (get_codes, 
get_dimensions, 
get_dsd_identifier, 
get_flows,
get_providers,
get_timeseries,
get_timeseries_revisions,
get_timeseries_table
)