#!/usr/bin/python3
# Conditionals And Booleans

"""
>>>> Python does not have switch case.
        Because the if elif and else is clean in python.
>>>>
>>>>
>>>>
"""


language = "Python"

if language == "Python":
    print("Language is Python")
elif language == "Java":
    print("Language is Java")
else:
    print("Language is not Python")

user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
    print("Admin Page")
elif not logged_in:
    print("Please Log In")
elif user == "Admin" or logged_in:
    print("Credential validated.")


# Object Identity (is)
# Tests if two object have the same id.
# Checks whether they are the same object in memory.
list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

# These both list point to the same memory address.
print(id(list_a), id(list_b))

# Both of the statement are same.
print(list_a is list_b)
print(id(list_a) == id(list_b))

# This checks whether the values are equal.
print(list_a == list_c)

# These are the values where python evaluates to False.
# All other values will be evaluates to True.
# False
# None
# Zero of any numeric type (0, 0.0, 0i + 0j etc.)
# Any empty sequence. For example, '', (), []
# Any empty mapping. For example, {}.

condition = False
if condition:
    print("Evaluated to True")
else:
    print("Evaluates to False")
