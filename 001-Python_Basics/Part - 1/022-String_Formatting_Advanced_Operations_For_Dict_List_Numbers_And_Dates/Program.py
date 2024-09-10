#!/usr/bin/python3
# String Formatting Advanced Operations For Dict List Numbers And Dates

"""
>>>>
>>>>
>>>>
>>>>
"""
import datetime

person = {"name": "Jenn", "age": 14}

# String formatting using the string concatenation.
sentence = (
    "My name is " + person["name"] + " and I am " + str(person["age"]) + " years old."
)
print(sentence)

# Using format option.
sentence = "My name is {} and I am {} years old.".format(person["name"], person["age"])
print(sentence)

# Using format option with numbering
sentence = "My name is {0} and I am {1} years old.".format(
    person["name"], person["age"]
)
print(sentence)

# Using format option with numbering and reduce code.
# Directly accessing the property within curly braces.
sentence = "My name is {0[name]} and I am {0[age]} years old.".format(person)
print(sentence)

# Using format option with numbering from list.
# Directly accessing the property within curly braces.
l = ["Jenn", 23]
sentence = "My name is {0[0]} and I am {0[1]} years old.".format(l)
print(sentence)


# Format option with object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Jack", 33)

sentence = "My name is {0.name} and I am {0.age} years old.".format(p)
print(sentence)

# Using format with keyword arguments.
sentence = "My name is {name} and I am {age} years old.".format(name="Jenn", age=32)
print(sentence)

# Using format with dictionary unpacking.
sentence = "My name is {name} and I am {age} years old.".format(**person)
print(sentence)

# Using format with number with zero padding.
for i in range(1, 11):
    sentence = "The value is {:03}".format(i)
    print(sentence)

# Using format with decimal places.
# Round of the number while formatting.
pi = 3.14159265
sentence = "Pi is equal to {:.2f}".format(pi)
print(sentence)

# Using format with numbers.
# Use comma separation for large number and adding the decimal places.
sentence = "1MB is equal to {:,.2f}".format(1000**2)
print(sentence)

# Format option with dates
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# March 01, 2016
sentence = "{:%B %d, %Y}".format(my_date)
print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.
sentence = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(
    my_date
)
print(sentence)
