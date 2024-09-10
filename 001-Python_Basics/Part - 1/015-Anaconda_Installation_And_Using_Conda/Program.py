#!/usr/bin/python3
# Anaconda Installation And Using Conda

"""
>>>> Anaconda
        It is a data science platform that comes with python distribution, package manager (conda), and other libraries preinstalled.
        Anaconda have another version called "Miniconda" which contains only python and conda.
            You have to install individual packages you want.
>>>> Conda
        conda can be also used to install non python packages.
>>>> Getting the documentation for conda.
        conda --help
>>>> List all packages using conda
        conda list
>>>> Install package using conda.
        conda install package_name
>>>> Create virtual environment using conda.
        conda create --name my_app flak sqlalchemy
        You have to pass at least one starting package name.
        Activating environment on windows.
            activate my_app
        Activating environment on Linux/Mac.
            source activate my_app
        Deactivating environment on Windows.
            deactivate
        Deactivating environment on Linux/Mac.
            source deactivate.
>>>> Create environment using different version of python.
        conda create --name my_name27 python=2.7 flask sqlalchemy
>>>> View all the environment created using conda command.
        conda env list
        "*" represent the activated environment.
>>>> Remove an environment using conda command.
        After the name, specify the package name to remove, or you can add --all to remove everything.
        conda remove --name my_app27 --all
>>>> Open jupyter notebook after installing anaconda.
        jupyter notebook
"""
