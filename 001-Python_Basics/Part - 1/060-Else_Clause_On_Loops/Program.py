#!/usr/bin/python3
# Else Clause On Loops

"""
>>>>
>>>>
>>>>
>>>>
"""

my_list = [1, 2, 3, 4, 5]

# Else will not be executed if break statement is executed in the for loop.
# If break does not hit in the for loop, then the else block wil be executed.
# Similar for the while loop.
for i in my_list:
    print(i)

    if i == 3:
        break
else:
    print("No break statement in for loop.")
