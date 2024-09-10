#!/usr/bin/python3
# Dictionaries Working With Key Value Pair

"""
>>>>
>>>>
>>>>
>>>>
"""

# Creating a dictionary.
student = {'name': 'John', 'age': 25, 'courses': ['Maths', 'Physics']}
print(student)

# Access value from dictionary using key.
# Accessing a invalid key will give KeyError.
print(student['name'])

# Accessing value from dictionary using get method.
# This will return None if key is not present in dictionary.
print(student.get('phone'))
print(student.get('phone', 'Not Found'))  # Passing a default value if key is not found.

# Adding a new key-value pair to dictionary.
# If key already exist, it will overwrite the existing value.
student['phone'] = '555-555-555'

# Update multiple values in the dictionary.
student.update({'name': 'sam', 'age': 33, 'phone': '111-111-1111'})
print(student)

# Delete a key-value from dictionary.
del student['age']
print(student)

# Delete key using pop method and return the value.
phone = student.pop('phone')
print(phone)

# Print the length of the dictionary.
print(len(student))

# Getting all the keys in the dictionary.
print(student.keys())

# Getting all the values in the dictionary.
print(student.values())

# Print all the keys and value in the dictionary.
print(student.items())

# Looping through keys and value in the dictionary.
for key, value in student.items():
    print(key, value)