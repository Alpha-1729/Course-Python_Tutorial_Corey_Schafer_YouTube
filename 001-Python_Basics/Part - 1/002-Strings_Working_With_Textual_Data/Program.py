#!/usr/bin/python3
# Strings Working With Textual Data

"""
>>>> Always separate long variable name using underscore.
>>>> Escape single and double quote in string.
        Use double quote if string contain only single quotes.
        Use single quote if string contain only double quote.
        If string contain both single and double quotes:
            Use triple quotes. (Can use single or double quotes)
            Use escape character \' or \" to escape single and double quote respectively.
>>>> Function and Methods.
        Methods are function that belongs to an object.
>>>>
"""

message_1 = "Hello World"
message_2 = "Hello World"

print(message_1) 
print(message_2)

# Print the length of the string.
print("The length of the string is", len(message_1))

# Print the first character of the string.
print("The first character:", message_1[0])

# Getting the first part of the string.
# This is called string slicing in python.
# First index is inclusive and last index is exclusive.
print("The first part of the string:", message_1[0:5])
print("The first part of the string:", message_1[:5])

# Getting the last part of the word.
print("The last part of the string:", message_1[6:])

# String methods.

# Convert to lower case.
print(message_1.lower())

# Convert to upper case.
print(message_1.upper())

# Count the number of occurrence of a character of substring in a string.
print(message_1.count('o'))
print(message_1.count('Hello'))

# Find the index of a substring in a string.
# It will return -1, if the substring is not found in the string.
print(message_1.find('World'))

# Replace substring in a string.
# This will not update the original string, It will return a new string.
# In order to update the original string, assign this to the original string.
print(message_1.replace("World", "Universe"))

# String concatenation.
greeting = 'Hello'
name = 'Michael'

# Using + operator
message = greeting + ', ' + name + '. Welcome!'
print(message)

# Using string formatter.
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# Using f strings.
# Works on python 3.6 and above.
# String methods will also work inside the f strings.
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# Getting all the string method names.
# All of these will work.
print(dir(str))
# print(dir(""))
# print(dir(message))

# To get the detailed information of all string method.
# print(help(str))

# Get detailed information of a specific string method.
print(help(str.lower))

