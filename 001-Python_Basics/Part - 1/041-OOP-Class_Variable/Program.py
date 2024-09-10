#!/usr/bin/python3
# Class Variable

"""
>>>> Class variables.
        Variables that are shared among all instances of a class.
        Class variable will be same for each instance.
>>>>
>>>>
>>>>
"""


class Employee:
    # This is a class variable.
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        # Both of this will work.

        # This will provide ability to allow any subclass to override that constant, if they wanted.
        self.pay = int(self.pay * self.raise_amount)

        # self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee("Corey", "Schafer", 5000)
emp_2 = Employee("Test", "User", 6000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# raise_amount is class variable.
# It can be accessed using the class and the instance of the class.
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# Print the namespace of the instance and class.
# To see where the raise_amount belong.
print(emp_1.__dict__)
print(Employee.__dict__)

# If we update the raise_amount for a particular instance, the value of the the instance will only change.
# All other instance will have the default value.
emp_1.raise_amount = 1.05
print(emp_1.__dict__)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)

print(emp_1.num_of_emps)
print(emp_2.num_of_emps)
print(Employee.num_of_emps)
