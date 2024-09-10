#!/usr/bin/python3
# Comprehension

"""
>>>> List Comprehension
        It is an easier and more readable way to create a list.
>>>>
>>>>
>>>>
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example 1
my_list = [n * n for n in nums]
print(my_list)
# Same using the map + lambda
my_list = map(lambda n: n * n, nums)
print(my_list)

# Example 2
my_list = [n for n in nums if n % 2 == 0]
print(my_list)
# Same using the filter + lambda.
my_list = list(filter(lambda n: n % 2 == 0, nums))
print(my_list)

# Example 3
my_list = [(letter, num) for letter in "abcd" for num in range(4)]
print(my_list)

# Example 4
# Dictionary comprehension
name = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
my_dict = {name: hero for name, hero in zip(name, heros) if name != "Peter"}
print(my_dict)

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 6, 8, 7, 9, 9]

# Example 5
# Set comprehension.
my_set = {n for n in nums}
print(my_set)


# Generator expression
# I want to yield 'n*n' for each 'n' in nums.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gen_func(nums):
    for n in nums:
        yield n * n


my_gen = gen_func(nums)
print(list(my_gen))

# Same can be implemented using the below line of code.
my_gen = (n * n for n in nums)
for i in my_gen:
    print(i)
