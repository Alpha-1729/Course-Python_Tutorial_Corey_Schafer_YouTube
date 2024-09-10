#!/usr/bin/python3
# If Dunder Name Equals Dunder Main

"""
>>>> 
>>>>
>>>>
>>>>
"""
import employee

print("First module name: {}".format(__name__))


def main():
    pass


# Checks if this file is directly run by python or is imported.
if __name__ == "__main__":
    print("Run directly")
    main()
else:
    print("Run from import")
