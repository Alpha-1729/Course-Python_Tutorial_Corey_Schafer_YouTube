#!/usr/bin/python3
# Functions

"""
>>>> DRY (Dont't Repeat Yourself)
>>>> docstring.
        A Python docstring is a string used to document a Python module, class, function or method.
>>>>
>>>>
"""


# Creating a empty function.
def test_func():
    pass


def hello_func():
    return "Hello Function!"


def add(num_1, num_2):
    return num_1 + num_2


# Function with a default parameter
def greeting_func(greeting, name="You"):
    return "{}, {}".format(greeting, name)


# Function that accepts multiple arguments and keyword arguments.
# args and kwargs.
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# This will return None, as the function does not return anything.
print(test_func())

# Function that return a string.
print(hello_func().upper())

# Function with parameter.
print(add(100, 200))

# Calling a function with a default parameter.
print(greeting_func("Morning"))
print(greeting_func("Evening", "Sam"))

 # args and kwargs.
student_info("Math", "Chemistry", name="Peter", age=33)
# OR
courses = ["Math", "Chemistry"]
info = {"name": "John", "age": 33}
student_info(*courses, **info)

# Checking the leap year function.
print(is_leap(2024))
