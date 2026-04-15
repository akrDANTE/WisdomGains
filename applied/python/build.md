# Building in python
Building in context of python means preparing python package or module that is converted into standard distributable format for the target platform. Python can use C/C++ code, so the binaries are created at the build time. The output of building a python project is a wheel file and a tar file. Wheel file contains all the necessary metadata required for configuring and installing the project like dependencies, compiled binaries of C/C++ and the python source code. tar file is the tarball of the source code, it is like a backup in case there is no suitable wheel file for a specific platform the pip falls back to build from this source code and install. 

# Build Systems in python
These are the tools used to build the wheels and tarfiles and are specified in the pyproject.toml files.
- Setup tools
- hatchling

# Distribution
This is the process of building executable which does not require users to install python. In the process of creating distributable exe we bundle the interpreter, dependecies and source code into one executable.
- Tool: PyInstaller