#!/usr/bin/python3
# Pipenv Easily Manage Packages And Virtual Environments

"""
>>>> Pipenv is a new way to combine package management with virtual environments.
        It combines the features of pip and virtual env.
>>>> Installing pipenv
        pip install pipenv
>>>> Creating a virtual environment and install a package.
        pipenv will automatically create an environment if there is no environment.

        pipenv install requests

>>>> PipFile
        It is a file that describes our environment and how we can build it back from scratch.
        It is similar to requirements.txt
>>>> PipFile.lock
        This file contain the exact information about the current environment.
        It contain the versions of the packages installed.
        This file can be used to create the same environment in the future.
>>>> Activating an environment.
        pipenv shell
>>>> Deactivating an environment.
        exit
>>>> Run python shell without activating the current environment.
        pipenv run python
>>>> Run a script in the current environment without activating the environment.
        pipenv run python main.py
>>>> Install dependencies from requirement.txt using pipenv.
        pipenv install -r requirements.txt
>>>> Generate requirements.txt file from pipenv.
        pipenv lock -r
>>>>  Install packages in only dev environments.
        pipenv install pytest --dev
        Please refer the changes added in the PipFile.lock file.
>>>> Remove installed packages.
        pipenv uninstall requests
>>>> Create new virtual environment for different version of python.
        pipenv --python 3.6

        If virtual environment already existed
        Old will be deleted and new one will be created.
>>>> Remove current environment and create new one from the PipFile.
        Removing the current virtual environment.
            pipenv --rm
        Create new environment from PipFile.
            pipenv install
>>>>  To know the path of the virtual environment.
        pipenv --venv
>>>> Check know security vulnerabilities for any of the installed packages.
        pipenv check

        If you want to change any of the package version.
        Change the version number in the PipFile and run the below command.
            pipenv install
>>>> pipenv graph
        Will display a dependency graph showing your packages and the dependencies for each of these.
            pipenv graph
>>>> Update the PipFile.lock with the current dependencies which has been tested.
        pipenv lock
>>>> Install and environment from PipFile.lock to match the exact requirements.
        pipfile install --ignore-pipfile
>>>> Creating an environment variables for the current environment.
        Create a .env file in the project.
        And environment variables in that file.
        Then activate the environment using the command.
            pipenv shell
        Then access that environment variables.
>>>>
>>>>
>>>>
>>>> 
>>>>
"""
 