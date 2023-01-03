# Installation

## Windows 
- Requires JAVA to be installed and the environment variable JAVA_HOME to be set

### Troubleshooting
On Python >= 3.8:
- Unable to create jni env, no jvm dll found.

The issue might be due to the missing installation of C++ build tools (can be downloaded here: https://visualstudio.microsoft.com/downloads/), as when running python import autoclass the package needs to import a .pyd file which requires the build tools

## MacOS

TODO

