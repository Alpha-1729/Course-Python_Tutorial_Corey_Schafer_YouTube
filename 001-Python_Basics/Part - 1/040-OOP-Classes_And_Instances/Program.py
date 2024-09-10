#!/usr/bin/python3
# Classes And Instances

"""
>>>> Why classes.
		Helps to logically group our data and functions in a way that's easy to reuse and also easy to build upon if we need.
        
        Data -> Attributes.
        Methods -> Functions associated with a class.
>>>> Class and Instances
		Class is a blueprint for creating instances.
        Each thing we create using class will be an instance of that class.
>>>> Instance variable.
		Instance variable contain data that is unique to each instance(object).
>>>>
"""


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def full_name(self):
        return f"{self.first} {self.last}"


# Create instance variable manually.
# Without declaring attributes in the class.
# emp_1 = Employee()
# emp_2 = Employee()
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 5000
# print(emp_1.email)

# Instances of the class.
emp_1 = Employee("Corey", "Schafer", 5000)
emp_2 = Employee("Test", "User", 6000)

print(emp_2.email)
print(emp_2.full_name())

# Here emp_2 is passed as self.
# This is the background working of the above line.
print(Employee.full_name(emp_2))
