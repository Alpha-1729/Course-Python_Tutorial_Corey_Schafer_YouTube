#!/usr/bin/python3
# How To Set The Path And Switch Between Different Versions Executables Windows

"""
>>>> Location of the pip directory.
        It is inside the scripts directory in the python folder.
>>>> If we have python2 and python3 in our machine.
        And if the path of the python2 is above the path of the python3 in the environment variable.
        When we type python in the command prompt, it will open the python2 and viceversa.
>>>> Getting all the path in the environment variable in command prompt.
        echo %path %
>>>> Show location of the libraries installed with pip.
        pip show django

        Also while installing a package using pip:
            It shows the location where it installs the package.
"""

# Getting the executable location of the current python version.
import sys
print(sys.version)
print(sys.executable)
