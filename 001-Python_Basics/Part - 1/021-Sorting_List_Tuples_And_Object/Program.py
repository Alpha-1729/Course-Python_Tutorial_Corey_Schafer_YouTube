#!/usr/bin/python3
# Sorting List Tuples And Object

"""
>>>>
>>>>
>>>>
>>>>
"""
from operator import attrgetter

# Sorting list.
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# Returning a new sorted list in ascending order.
s_li = sorted(li)
print(s_li)

# Return a new sorted list in descending order.
s_li = sorted(li, reverse=True)
print(s_li)

# Sort inplace in ascending order.
li.sort()
print(li)

# Sort inplace in descending order.
li.sort(reverse=True)
print(li)

# Sorting Tuple.
# Tuple does't have a sort method like list.
# We have to use the sorted function.
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print(s_tup)

# Sorting the dictionary by keys.
di = {"name": "Corey", "job": "Programming", "age": "None", "os": "Mac"}
s_di = sorted(di)
print(s_di)

# Sort the list based on a custom function.
# Sort based on the absolute value of the element.
li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)


# Sorting objects.
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "{},{},${}".format(self.name, self.age, self.salary)


e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employees, key=e_sort, reverse=True)
print(s_employees)

# Sort using the lambda function.
s_employees = sorted(employees, key=lambda e: e.name)
print(s_employees)


# Sort using the attrgetter function.
s_employees = sorted(employees, key=attrgetter("name"))
print(s_employees)
