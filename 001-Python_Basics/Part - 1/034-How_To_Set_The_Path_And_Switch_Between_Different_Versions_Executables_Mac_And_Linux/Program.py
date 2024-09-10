#!/usr/bin/python3
# How To Set The Path And Switch Between Different Versions Executables Mac And Linux

"""
>>>> Getting the location of the python.
        which python3
        which python

        OR

        type python3
        type python
>>>> Getting the environment path in linux/mac.
        echo $PATH
>>>> Adding path variable in linux.
        nano .bash_profile

        Add this line at the end of the file.
            PATH="usr/bin:${PATH}"
            export PATH
>>>> Adding alias in linux.
        nano .bash_profile

        Add this line at the end of the file.
            alias python=python3
            alias pip=pip3
"""

# Getting the location of the current python executable.
import sys

print(sys.version)
print(sys.executable)
