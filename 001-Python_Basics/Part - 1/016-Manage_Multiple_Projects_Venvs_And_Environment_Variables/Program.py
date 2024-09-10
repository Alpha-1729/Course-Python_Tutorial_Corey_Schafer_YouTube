#!/usr/bin/python3
# Manage Multiple Projects Venvs And Environment Variables

"""
>>>> How to create yaml file (That can be used to build the same environment from scratch)
        conda env export > environment.yaml
>>>> Recreate environment from the yaml file.
        conda env create -f environment.yaml
>>>> Environment variables.
        Environment variables allows us to access sensitive data without putting it directly in our projects code.
>>>> Managing environment variables for different virtual environments.
        If we use the global environment variable for this purpose, there should be a problem of overriding variable in the global environments.
        To separate this out conda environment comes with some useful scripts, that we can create.
			To create these scrips we need to put them in specific location.
        Find environment location using the below command.
			conda env list.
			navigate to a specific environment directory.
        Create two directories to set and unset environment variables when the environment is activated or deactivated.
			mkdir -p etc/conda/activate.d
            touch /etc/conda/activate.d/env_vars.sh
            mkdir -p etc/conda/deactivate.d
            touch /etc/conda/deactivate.d/env_vars.sh
            
            Add environment variables to activate.d/env_vars.sh
				#!/bin/sh
				export DATABASE_URL="database_url"
			Add content in deactivate.d/env_vars.sh
				#!/bin/sh
                unset DATABASE_URL
            
            Check the status of the environment variable after activating the environment.
				echo $DATABASE_URL
            Check the status of the environment variable after deactivating the environment.
				echo $DATABASE_URL
>>>> How to activate a environment which contains a environment.yaml when we switch to that directory.
		The tools like autoenv and direnv can do theses thing.
        
        How to create own function in bash to do this.
			All the code is available in the Resource folder.
            Paste the code in the ~/.bash_profile.
			# Original
            	Reference Link: https://github.com/chdoig/conda-auto-env/blob/master/conda_auto_env.sh
			# Updated
				Reference Link: https://github.com/CoreyMSchafer/code_snippets/blob/master/conda_auto_env.sh
                
        How to do this.
			We need to create a bash function that check for the virtual environment and activates if it finds.
            Then we need to set one environment variable called PROMPTCOMMAND that will run this custom function before each bash prompt.
"""
