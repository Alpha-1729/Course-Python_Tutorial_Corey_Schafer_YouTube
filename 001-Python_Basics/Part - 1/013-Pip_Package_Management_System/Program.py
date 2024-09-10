#!/usr/bin/python3
# Pip Package Management System

"""
>>>> Getting the documentation for pip.
        pip help
>>>> Getting the information about specific command.
        pip help install
>>>> Search for a package name.
        pip search Pympler
>>>> Install package.
        pip instal Pympler.
>>>> Get the list of installed packages.
        pip list
>>>> Uninstall a package.
        pip uninstall Pympler
>>>> Check the current version of the package is latest or not.
        pip list --outdated (or -o)
>>>> Upgrade a specific package.
        pip install -U package_name
>>>> Generate the requirement.txt file.
        pip freeze > requirements.txt
>>>> Install from requirement file.
        pip install -r requirements.txt
>>>> Upgrading multiple outdate packages.
        pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U
"""
