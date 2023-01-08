# Python Interface to SDMX Web Services
The Python Interface to SDMX Web Services provides functions to retrieve data and metadata from providers that disseminate data by means of SDMX web services. SDMX (Statistical Data and Metadata eXchange) is a standard that has been developed with the aim of simplifying the exchange of statistical information. More about the SDMX standard and the SDMX Web Services can be found at: <https://sdmx.org>.

This package is a Python interface to the Java library available at: https://github.com/amattioc/SDMX/

## Documentation
Documentation is based on ``sphinx`` and can be generated via 

```
cd docs
make html
```

## Demo
A sample usage of the package can be found in the ``demo/`` folder.
- ``sample_output.py`` provides an sample output of the main functions 
- ``interactive.ipynb`` provides an interactive query script where user can provide query inputs

## Tests
Tests (still WIP) can be run using ``pytest tests/``
