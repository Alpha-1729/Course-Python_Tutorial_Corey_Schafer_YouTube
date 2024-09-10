#!/usr/bin/python3
# Lists Tuples And Sets

"""
>>>> List are mutable and tuple are immutable.
        We cannot modify the tuples.
>>>> List are reference type in python.
        If we assign one list to another list, both the list will point to same list.
        Changing the one value in one list will also affect the other list also.
>>>> Sets
        Sets are values that are unordered and also have no duplicate.
>>>>
"""

# Lists
courses = ["History", "Math", "Physics", "Chemistry"]
print(courses)

# Find the length of the list.
print(len(courses))

# Accessing first item in the list.
print(courses[0])

# Accessing last item in the list using negative index.
print(courses[-1])

# Getting the sub list using slicing.
print(courses[0:2])

# List Method.

# Add an item to end of the list.
courses.append('Art')
print(courses)

# Insert an item at a specific position in the list.
courses.insert(1, 'Biology')
print(courses)

# Add a list into another list.
courses_2 = ['Zoology', 'Geology']
courses.extend(courses_2)
print(courses)

# Remove an item from list.
courses.remove('Geology')

# Remove the last item from the list and get the last value.
removed_value = courses.pop()
print(removed_value)
print(courses)

# Reversing the list.
courses.reverse()
print(courses)

# Sorting the list in ascending order.
# These sorting are done inplace.
courses.sort()
print(courses)

# Sort the list in the descending order.
# These sorting are done inplace.
courses.sort(reverse=True)
print(courses)

# Get the sorted version of a list.
sorted_courses = sorted(courses)
print(sorted_courses)

# Min and Max.
nums = [1, 5, 2, 4, 3]
print(min(nums))
print(max(nums))
print(sum(nums))

# Find the index of an item in the list.
# -1 is returned, if the item is not in the list.
print(courses.index('Physics'))

# Check the existence of a value in the list.
print('Art' in courses)

# Print all values in the list.
for item in courses:
    print(item)

# Getting the index and value in the list.
for index, course in enumerate(courses):
    print(index, course)

# Getting the index and value in the list with another start value for the index.
for index, course in enumerate(courses, start=100):
    print(index, course)

# Convert the list into string with comma-separated values.
courses_str = ', '.join(courses)
print(courses_str)

# Generate list by splitting the string.
new_list = courses_str.split(", ")
print(new_list)

# Tuples
# Creating a tuples.
tuple_1 = ('History', 'Math', 'Physics', 'Biology')
print(tuple_1)

# Sets
cs_courses = {'History', 'Math', 'Math', 'Physics', 'Chemistry'}
# Order of the items will not be constant always.
print(cs_courses)

# Membership test in sets.
# Sets are optimized for this.
print("Math" in cs_courses)

# Find the intersection between two sets.
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))

# Find the difference between two sets.
print(cs_courses.difference(art_courses))

# Find the union of two sets.
print(cs_courses.union(art_courses))

# Creating empty list, tuple and sets.
# Creating empty list.
empty_list = []
empty_list = list() 

# Creating empty tuple
empty_tuple= ()
empty_tuple = tuple()

# Creating empty set.
empty_set = {}  # This is not right, It is for creating an empty dictionary
empty_set = set()

