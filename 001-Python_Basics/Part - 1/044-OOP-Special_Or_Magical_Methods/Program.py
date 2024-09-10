#!/usr/bin/python3
# Special Or Magical Methods

"""
>>>> Special methods
        These methods allow us to emulate some built-in behavior within python and it's also how we implement operator overloading.
        These special methods are surrounded by double underscore.
        __ is also called dunder.
        __init__ -> is called dunder init.
>>>> __repr__
        It is meant to be an unambiguous representation of the object and should be used for debugging and logging and things like that.
        It is really meant to be seen by other developer.
>>>> __str__
        It is meant to be more of a readable representation of an object.

        If __str__ is not present, it will call the __repr__ by default.
>>>>
"""


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Generate a string to regenerate this employee.
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "Employee", 60000)

print(emp_1)

print(repr(emp_1))
print(emp_1.__repr__())

print(str(emp_1))
print(emp_1.__str__())

# dunder add for integer.
print(1 + 2)
print(int.__add__(1, 2))

# dunder add for string.
print('a' + 'b')
print(str.__add__('a', 'b'))
