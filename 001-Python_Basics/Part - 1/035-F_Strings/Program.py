#!/usr/bin/python3
# F Strings

"""
>>>> F string only work on python3.6 and above.
>>>>
>>>>
>>>>
"""
from datetime import datetime

# Example 1
first_name = "Corey"
last_name = "Schafer"

sentence = f"My name is {first_name.upper()} {last_name}"
print(sentence)

# Example 2
person = {"name": "John", "age": 23}
sentence = f"My name is {person['name']} and I am {person['age']} years old"
print(sentence)

# Example 3
for n in range(1, 11):
    # Zero padding for 3 digit.
    sentence = f"The value is {n:03}"
    print(sentence)

# Example 4
pi = 3.14159265

# Round off to 4 decimal place.
sentence = f"Pi is equal to {pi:.4f}"
print(sentence)

# Example 5
birthday = datetime(1990, 1, 1)
sentence = f"Jenn has a birthday on {birthday:%B %d, %Y}"
print(sentence)
