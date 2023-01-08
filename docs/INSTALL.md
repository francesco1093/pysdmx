# Installation

## Windows

This package is based on the Pyjnius library. Pyjnius requires Java to be installed and Pyjnius needs to be able to access the jvm.dll file to start the JVM. In particular, you need to satisfy the following requirements:

- As Pyjnius uses CPython, the C++ build tools need to be installed (download link here: https://visualstudio.microsoft.com/downloads/)
- The Python requirements need to be installed. It is recommended to install a python virtual environment using the provided ``requirements.txt`` file (which includes cython and pyjnius)
- The ``JAVA_HOME`` environment variable needs to be set and point to the Java installation directory (the current version has been developed for Java 8, please notify any incompatibilities with other versions). The ``JAVA_HOME/bin`` directory needs to be added to PATH

### Troubleshooting
**Unable to create jni env, no jvm dll found.**

The issue might be due to the missing installation of C++ build tools (can be downloaded here: https://visualstudio.microsoft.com/downloads/), as when running python import autoclass the package needs to import a .pyd file which requires the build tools

## MacOS

TODO

