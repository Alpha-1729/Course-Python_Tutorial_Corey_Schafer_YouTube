#!/usr/bin/python3
# Working With Numeric Data Integers And Floats

"""
>>>> Arithmetic Operators:
        # Addition:         3 + 2
        # Subtraction:      3 - 2
        # Multiplication:   3 * 2
        # Division:         3 / 2
        # Floor Division:   3 // 2
        # Exponent:         3 ** 2
        # Modulus:          3 % 2
>>>> Comparison Operators:
        # Equal:            3 == 2
        # Not Equal:        3 != 2
        # Greater Than:     3 > 2
        # Less Than:        3 < 2
        # Greater or Equal: 3 >= 2
        # Less or Equal:    3 <= 2
        # Object Identity:  is 
                We are checking whether two values have same id.
                Or whether they are the same object in memory.

>>>>
>>>>
"""

num = 3
print(type(num))  # Print type of an object.

PI = 3.14
print(type(PI))

# Floor division.
# Result will be an integer.
print(3 // 2)

# Shorthand for incrementing number.
number = 4
number += 1
print(number)

# Get the absolute value of a number.
print(abs(-100))

# Rounding the number.
print(round(3.14))  # Round to nearest integer.
print(round(1000.33424524, 4))  # Round the result to 4 decimal digits.

# Comparing two numbers.
print(3 == 4)
print(3 < 4)

# Casting to integer
print(int('101') + int('102'))