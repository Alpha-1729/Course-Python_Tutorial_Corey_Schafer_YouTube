#!/usr/bin/python3
# Os Module

"""
>>>> OS module
        It allows us to interact with the underlying operating system.
>>>>
>>>>
>>>>
"""

import os
from datetime import datetime

# Get current working directory.
print(os.getcwd())

# Changing directory.
# os.chdir("/Users/coreyschafer/Desktop")

# List files and folders in the current directory.
print(os.listdir())

# List files and folders in a specific folder.
print(os.listdir("/"))

# Creating Directories.

# Creating inner level directories.
# os.makedirs("/Users/coreyschafer/help/test/nothing")

# To create only top level directories.
# os.mkdir("Test")

# Deleting directories.

# Removing the top level directories.
# os.rmdir("Test")

# Removing the intermediate directories.
# os.removedirs("/Users/coreyschafer/help/test")

# Rename a file.
# os.rename("test.txt", "demo.txt")

# Print information about a file.
file_name = "Program.py"
print(os.stat(file_name))

# Get the file size in bytes.
print(os.stat(file_name).st_size)

# Get the last modification time of the file. (This will be in timestamp)
modification_time = os.stat(file_name).st_mtime

# Convert the timestamp into actual datetime.
print(datetime.fromtimestamp(modification_time))

# If we want to traverse the entire directory tree.
# os.walk() is a generator, that yields a tuple of three values.
# For each directories, it will give the directory path, directories within that path, and files within that path.

'''
for dirpath, dirnames, filenames in os.walk("/Users/coreyschafer/Desktop/"):
	print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()
'''

# Get all the environment variables.
# print(os.environ)

# Getting a single environment variable.
# Get the home directory of the user.
home_dir = os.environ.get('HOME')
print(home_dir)

# Joining file path. 
print(os.path.join(home_dir, 'test.txt'))

# Grab the file name from the full path.
print(os.path.basename('/temp/test.txt'))

# Grab the dir name from the full path of a file.
print(os.path.dirname('/test/temp/test.txt'))

# Getting the directory name and the file name.
print(os.path.split('/test/temp/test.txt'))

# Check the existence of a file path.
print(os.path.exists('/test/temp/test.txt'))

# Check whether the file path is a file or a directory.
# It actually check the existence of this file or directory.
# If the file path doesn't exist, it will return False for isfile and isdir methods.
print(os.path.isfile('/test/temp/test.txt'))
print(os.path.isdir('/test/temp/test.txt'))

# Split the file root and extension.
print(os.path.splitext('/test/temp/test.txt'))

# Get the list of all method in os.path.
print(dir(os.path))