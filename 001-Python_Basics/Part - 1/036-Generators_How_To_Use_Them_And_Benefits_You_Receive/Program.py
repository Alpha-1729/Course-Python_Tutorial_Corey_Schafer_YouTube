#!/usr/bin/python3
# Generators How To Use Them And Benefits You Receive

"""
>>>> Generators.
		Generators don't hold the entire result in memory, it yields one result at a time.
>>>> Getting the memory usage in python.
		Reference Link: https://pypi.org/project/memory-profiler/
>>>> A script has been added to compare the difference between the list and generators.
        Refer Program_2.py
>>>>
"""


def square_num_list(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


def square_num_generators(nums):
    for i in nums:
        yield (i * i)


# Using list.
my_nums = square_num_list([1, 2, 3, 4, 5])
print(my_nums)

# Using generators.
my_nums = square_num_generators([1, 2, 3, 4, 5])

# Print the first value using generators.
print(next(my_nums))
# Print the remaining values using generators.
for num in my_nums:
    print(num)

# Generators using list comprehension.
my_nums = (x * x for x in [1, 2, 3, 4, 5])

# Converting generators to list.
print(list(my_nums))

# This will print nothing.
# Since all the values in the generators have been used.
# Check the above code, which converts the generators to list.
for num in my_nums:
    print(num)
