#!/usr/bin/python3
# Variable Scope Understanding The Legb Rule And Global Nonlocal Statement

"""
>>>> Variable Scope.
        This is what determines where our variable can be accessed from within the program, and what values variables hold in different context.
>>>> LEGB (Common abbreviation to understand the scoping rule in python)
        Python checks the variables in these order.
        Local, Enclosing, Global, Built-in
>>>> You can create a global variable from a function, and you can use that variable outside the function.
>>>> Getting the list of builtin function and variables.
        import builtins
        print(dir(builtins))
>>>> Enclosing Scope:
        Enclosing scope has to do with the nested function.
        See the example mentioned in the below code.
"""

x = "global x"


# Pointing to a global variable in the function.
def test():
    global x
    x = "local x"
    print(x)


test()
print(x)


# Example to demonstrate the enclosing scope.
def outer():
    x = "outer x"

    def inner():
        # Here it first check x in the local scope.
        # Then it checks x in the enclosing function.
        print(x)

    inner()


outer()


# Non local statement.
def non_outer():
    x = "outer x"

    def non_inner():
        # This is used to update the x in the enclosing scope.
        nonlocal x
        x = "inner x"
        print(x)

    non_inner()
    print(x)


non_outer()
