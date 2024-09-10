#!/usr/bin/python3
# Import Modules And Exploring The Standard Library

"""
>>>> To make the module name shorter we can use alias for module name.
        import my_module as mm
        import numpy as np
>>>> Importing essential things from module.
        from my_module import find_index as fi, test
>>>> To import everything from a module.
        from my_module import *
>>>> How to import a module that is not in a current working directory.
        1. Manually add the directory which contains to the sys.path.
            sys.path.append("directory in which the module is located")
            Add this line in the script before importing the module.
        2. Add the module path in the environment variable.
            How to add the module directory to the environment variable in mac.
                sudo nano ~/.bash_profile
                Add this line to the end of the file.
                    export PYTHONPATH="directory name of the module"
                Save the file.
                source ~/.bash_profile (Or restart the terminal)
            How to add the module directory to the environment variable in Windows.
                Open the environment variable in Windows.
                Click on New button under the user variable.
                    Variable name: PYTHONPATH
                    Variable value: directory name of the module.
            All the advanced text editor like eclipse, sublime-text, pycharm can have their own environment variable. Just google them for different text-editor.
>>>> os module give access to underlying operating system.

"""

import my_module
import sys
import random
import math
import datetime
import calendar
import os

courses = ["History", "Math", "Physics", "Biology"]

index = my_module.find_index(courses, "Math")
print(index)

# Get the list of path from which the python import other modules.
# When we import a module, it checks multiple location and locations that it checks is within a list called sys.path.
# This is the list of directories on the machine, where python look for modules, when we run an import, and it look in the same order in the list.
# Order is like this.
# 1. It checks the directory containing the current script.
# 2. Then checks in the directories added in the python path environment variable.
# 3. Then checks in the standard libraries path.
# 4. Then it checks in the site-package directories, Which contains the third party packages.
print(sys.path)

# Getting random value from a list.
random_course = random.choice(courses)
print(random_course)

# Convert degree into radians.
rads = math.radians(90)
print(rads)

# Find sign value of a radian value.
print(math.sin(math.radians(90)))

# Getting today's date.
today = datetime.date.today()
print(today)

# Check for a leap year.
print(calendar.isleap(2024))

# Print current working directory.
print(os.getcwd())

# Getting the directory of a particular standard library using the dunder file attribute.
print(os.__file__)
