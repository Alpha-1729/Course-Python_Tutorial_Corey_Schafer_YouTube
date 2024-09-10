#!/usr/bin/python3
# Setup Python Development Environment In Atom

"""
>>>> Installing packages in Atom.
        Open Atom -> Preferences -> Install (Packages/Theme)
        After installing a package, click on the settings to change the default behavior of package.
        All the keyboard should be displayed under the settings page.
>>>> Popular atom packages.
        script (Package) 
            Run code in Atom.
            Ctrl + I to run the current script.
        predawn-syntax (Theme)
            After installing the theme.
            Click on the themes on the left side and select the default syntax theme.
        autocomplete-python
        file-icons
        minimap
        python-autopep8
            pip install autopep8
            Check "Format On Save" option in settings.
        linter-flake8
            pip install flake8
         
>>>> Other editor settings.
        Check the "Scroll Past End".
        Set "Tab Length" to 4.
        Disable "autocomplete-plus" and "autocomplete-snippets" packages in the atom.
            This section is under the Packages in the left side nav.

>>>> Setting different build system for python.
        Adding a profile.
            Open command palette using Ctrl + Shift + P.
            Select "Script: Run Options"
                Command: /usr/bin/python2.7
            Click on Save as profile.
                Enter the profile name.
        Running with added profile.
            Open command palette and select "Script: Run With Profile" option.
            Select the option and run.
            You can also set keyboard shortcut for each profile.
"""
