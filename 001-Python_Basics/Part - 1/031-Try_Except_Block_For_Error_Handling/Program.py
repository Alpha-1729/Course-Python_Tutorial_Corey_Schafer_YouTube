#!/usr/bin/python3
# Try Except Block For Error Handling

"""
>>>>
>>>>
>>>>
>>>>
"""

# Simple try except.
# Catch all exception.
try:
    open('test_1.txt', 'r')
except Exception:
    print("Sorry. This file doesn't exist")


# File not found exception.
try:
    x = 4 / 0;
except FileNotFoundError:
    print("Sorry. This file doesn't exist")
except Exception as e:
    print(f'Error: {e}')

# Else block.
# This block will run if try block doesn't raise and error.
try:
    f = open('test.txt', 'r')
except FileNotFoundError:
    print("Sorry. This file doesn't exist")
except Exception as e:
    print(f'Error: {e}')
else:
    print(f.read())
    f.close()
          
# Finally block.
# This block always work.
try:
    f = open('test.txt', 'r')
except FileNotFoundError:
    print("Sorry. This file doesn't exist")
except Exception as e:
    print(f'Error: {e}')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')

# Raising exception manually.
raise Exception('File Content missing')