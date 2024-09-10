#!/usr/bin/python3
# Setup A Python Development Environment In Sublime Text

"""
>>>> Install sublime text.
>>>> How to run the python script in sublime using the automatic build system.
        Open Tools -> Build. (Use keyboard shortcut Ctrl + B)
>>>> Installing package control in sublime.
        Open Command Palette.
            Tools -> Command Palette (Use shortcut Ctrl + Shift + P)
        Search "Install Package Control" and click on it.
        Open command palette after installing the package control and search for install package and select it.

        Install predawn (color scheme)
        Install Material Theme (color scheme)
>>>> Use the sublime settings file uploaded in the instructor github page.
        Copy the file content to clipboard.
        Sublime text -> Preference -> Settings.
        Paste the copied content in the "Preferences.sublime-settings - User".
        Restart the sublime text to apply the changes.
        You can also read the comment mentioned in the Default settings.
>>>> Color Scheme and Color Theme
        Color scheme change the color of the font.
        Color theme change the entire look of the text-editor.
>>>> Other sublime text packages.
        Bracket Highlighter.
            It helps you keep track of where certain brackets begin and ends.
        Sidebar Enhancements.
				It provide lot of options for right click on the left sidebar.
        Anaconda
			Provide python linting and auto formatting.
			Anaconda.sublime-settings is available in the instructor's github repo.
			Update the settings in the Preferences -> Package Settings -> Anaconda -> Settings - User.
			Restart the sublime-text.
>>>> All the package specific settings are available in Preferences -> Package Settings.
>>>> Create different python build system for running different version of python.
        All the build system files are available in the instructor github repo.
			Python2.7.sublime.build
			Python3.5.sublime.build
        Creating python2.7 build system
			Open Tools -> Build System - > New Build System.
            Copy and paste the content from the Python2.7.sublime.build file in the repo.
            Save as Python2.7.sublime.build

        Creating python3.5 build system
			Open Tools -> Build System - > New Build System.
            Copy and paste the content from the Python3.5.sublime.build file in the repo.
            Save as Python3.5.sublime.build
        
        Select the build system while running the python file.
>>>> Removing packages from sublime text.
		Open command palette and search remove packages.
        Select the package you want to uninstall.

"""
