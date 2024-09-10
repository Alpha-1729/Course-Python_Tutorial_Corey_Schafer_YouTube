#!/usr/bin/python3
# Hiding Password And Secret Keys In Environment Variables Linux And Mac

"""
>>>> Adding environment variables in linux.
        nano .bash_profile
        export DB_USER="my_db_user"
        export DB_PASS="my_db_pass"
        Close the file.
>>>>
>>>>
>>>>
"""

import os

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASS")

print(db_user)
print(db_password)
