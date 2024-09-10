#!/usr/bin/python3
# Class Methods And Static Methods

"""
>>>> Static Method.
        Method that don't access the instance or the class.
>>>>
>>>>
>>>>
"""
import datetime


class Employee:
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
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


emp_1 = Employee("Corey", "Schafer", 5000)
emp_2 = Employee("Test", "User", 6000)

# Calling the class method using the class.
# This is the preferred way.
Employee.set_raise_amount(1.05)

# Calling the class method using the instance.
# This is not the best way, Don't use it.
# emp_1.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Example 2
# For using class method.
emp_str_1 = "John-Doe-70000"
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

# Example 3
# Static method.
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
