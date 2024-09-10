#!/usr/bin/python3
# Property Decorators Getters Setters And Deleters

"""
>>>> Property Decorator.
        This allows us to give our class attributes getter and setter and a deleter functionality.
        Property decorator allows us to define a method, but we can access it like an attribute.
>>>>
>>>>
>>>>
"""


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print("Name Deleted!")
        self.first = None
        self.last = None


emp_1 = Employee("Corey", "Schafer", 50000)

emp_1.full_name = "Lam Sonal"

print(emp_1.first)
print(emp_1.email)
print(emp_1.full_name)

# Deleting a attribute.
del emp_1.full_name
