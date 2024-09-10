#!/usr/bin/python3
# Setup Python Development Environment In Eclipse

"""
>>>> Download and install eclipse installer from their official website.
        Select the Eclipse Platform option and click on install.
>>>> Open eclipse and go to workbench.

>>>> Install PyDev plugin.
        Click on help -> Install New Software
            Work with: All Available Sites
            Filter: Market
            Select Marketplace client and click on Next.
            Restart the eclipse.
        Click on help -> Eclipse Marketplace.
            Install PyDev plugin.
            Restart.
>>>> Creating a python project in Eclipse.
        File -> New -> Project -> Select PyDev Project.
        Add project name.
        Select default python interpreter.

        Create a PyDev module in the project.
            Right click on the project, New -> PyDev Module
            Add package name.
            Add module name. (Don't add .py extension)
            Select the appropriate template.
                Select <Empty> as default.
                    It will add the CreatedOn and author name at the top.
                    It will create the __init__.py file in the package folder.
>>>> Change the preference.
        Open Eclipse -> Preferences.
        Change Theme.
            General -> Appearance -> Theme
        Change Font.
            General -> Appearance -> Colors and Fonts -> Basic -> Text Font.
                Select the font and click on apply.
        Change PyDev Code Formatter.
            PyDev - > Editor -> Code Style -> Code Formatter.
                Check "Use autopep8 for code formatting".
                Click on apply.
            PyDev -> Editor -> Save Actions.
                Check "Auto-format editor contents before saving"

"""
