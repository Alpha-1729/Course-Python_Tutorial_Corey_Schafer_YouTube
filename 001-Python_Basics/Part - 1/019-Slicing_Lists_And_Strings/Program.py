#!/usr/bin/python3
# Slicing Lists And Strings

"""
>>>> Slicing
        It is a way to extract certain elements from the list or strings. 
>>>>
>>>>
>>>>
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing the list.
# Last index in exclusive.
print(my_list[0:6])
print(my_list[-7:-2])
print(my_list[5:])
print(my_list[:-2])
print(my_list[:])

# Skipping some elements using slicing.
# [start:end:step]
print(my_list[2:-1:2])
# Printing in reverse order.
print(my_list[-1:2:-2])

# Reversing a list.
print(my_list[::-1])
