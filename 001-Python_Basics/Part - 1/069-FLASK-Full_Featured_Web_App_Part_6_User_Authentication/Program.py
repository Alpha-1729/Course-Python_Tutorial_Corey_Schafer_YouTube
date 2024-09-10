#!/usr/bin/python3
# Full Featured Web App Part 6 User Authentication

"""
>>>> bcrypt is a hashing algorithm to encrypt the passwords.
        There is also an extension for flask.
        pip install flask-bcrypt
>>>> flask library for login related stuffs.
        pip install flask-login
>>>>
>>>>
"""
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Generate password hash in byte.
bcrypt.generate_password_hash("testing")

# Generate password hash in string.
# Everytime new password will be generated.
bcrypt.generate_password_hash("testing").decode("utf-8")

# We have to use the check_password_hash method to check whether the current password and the previously stored hash are same.
hashed_pw = bcrypt.generate_password_hash("testing").decode("utf-8")

# This will return True.
bcrypt.check_password_hash(hashed_pw, "testing")
