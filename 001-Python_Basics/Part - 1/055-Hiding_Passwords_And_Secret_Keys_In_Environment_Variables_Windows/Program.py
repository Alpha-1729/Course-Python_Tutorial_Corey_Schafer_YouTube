#!/usr/bin/python3
# Hiding Passwords And Secret Keys In Environment Variables Windows

"""
>>>> Adding environment variables in windows.
        ControlPanel -> System and Security -> System -> Advanced system settings.
        Click on Environment Variables.
        Add the variable name and variable value.
>>>>
>>>>
>>>>
"""
import os

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")

print(db_user)
print(db_password)
