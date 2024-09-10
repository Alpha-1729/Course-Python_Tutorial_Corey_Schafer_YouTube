#!/usr/bin/python3
# Context Managers Efficiently Managing Resources

"""
>>>> Context managers allow us to properly manage resources.
>>>> Use of context managers.
        To properly close the file after use.
        Connect and close databases automatically.
        We could acquire and release locks.
>>>> In this video, we will be focusing on writing our own context managers to handle custom resources.
        By using a class.
        By a function by a decorator.
            using contextlib module.
>>>> __enter__ and __exit__ methods ar going to setup and tear down of the context manager.
"""
import os
from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
    f = None
    try:
        f = open(filename, mode)
        yield f
    finally:
        if f is not None:
            f.close()


# This is used to change directory to another location and get back to previous directory after use.
@contextmanager
def change_dir(destination):
    cwd = os.getcwd()
    try:
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # The extra parameter are there for if we throw an exception.
    # We can use those to access that information.
    def __exit__(self, exec_type, exc_val, traceback):
        self.file.close()


# Context manager using class.
with OpenFile("test.txt", "w") as f:
    f.write("Testing")

print(f.closed)

# Context manager using function and decorator.
with open_file("test.txt", "r") as s:
    # s.write("Good morning")
    s.read()
print(s.closed)


with change_dir("Sample_Dir_One"):
    print(os.listdir())

with change_dir("Sample_Dir_Two"):
    print(os.listdir())
