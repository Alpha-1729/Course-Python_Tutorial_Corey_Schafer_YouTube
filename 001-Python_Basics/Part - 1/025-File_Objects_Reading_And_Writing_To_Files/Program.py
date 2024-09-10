#!/usr/bin/python3
# File Objects Reading And Writing To Files

"""
>>>> Writing to files.
        We cannot write to a file which is in read mode.
>>>>
>>>>
>>>>
"""

# Opening a file
f = open("test.txt", "r")
print(f.name)
print(f.mode)
# print(f.read())
f.close()


# Open file using context manager.
# It automatically close the file after use.
with open("test.txt", "r") as f:
    # Read the full file.
    # f_content = f.read()

    # Read the each line as a list.
    # f_content = f.readlines()

    # Read a single line.
    # Run this multiple times to read all line.
    f_content = f.readline()
    print(f_content, end="")
    f_content = f.readline()
    print(f_content, end="")


# How to read a large file.
with open("test.txt", "r") as f:
    # Read one line at a time.
    for line in f:
        print(line, end="")
    print()

# Reading a large file by small chunk.
print()
with open("test.txt", "r") as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end="")
        f_contents = f.read(size_to_read)

# Getting the current read location of the file.
print()
with open("test.txt", "r") as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    # Print the start of the next read location.
    print(f.tell())

# Move the read location to any other position.
print()
with open("test.txt", "r") as f:
    size_to_read = 10

    f_content = f.read(size_to_read)
    print(f_content)

    # Read from the start again.
    # Move the cursor to the beginning of the file.
    f.seek(0)

    f_content = f.read(size_to_read)
    print(f_content)


# Simply creating a file without any contents.
with open("test2.txt", "w") as f:
    pass

# Writing to a file.
with open("test2.txt", "w") as f:
    f.write("Test")

# Copy one file to another.
with open("test.txt", "r") as rf:
    with open("test_copy.txt", "w") as wf:
        for line in rf:
            wf.write(line)

# Create copy of a image file.
# Always ready images like file in binary mode.
with open("dog.jpg", "rb") as rf:
    with open("dog_copy.jpg", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


# Check whether the file is closed or not.
print(f.closed)
