#!/usr/bin/python3
# Csv Module Read Parse And Write Csv Files

"""
>>>> CSV
        Comma Separated Values
>>>> Delimiter
        What separate values in the CSV.
>>>>
>>>>
"""


import csv

# Reading a csv file.
with open("test.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skipping the heading.
    # next(csv_reader)

    # newline='' to avoid printing an extra newline.
    with open("test_copy.csv", "w", newline="") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")

        for line in csv_reader:
            csv_writer.writerow(line)

# Reading the csv using the dictionary reader method.
with open("test.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")

    for line in csv_reader:
        print(line)
        print(line["email"])

# Writing the csv using the Dictionary writer.
with open("test.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")

    # newline='' to avoid printing an extra newline.
    with open("test_copy.csv", "w", newline="") as new_file:
        field_names = ["first_name", "last_name", "email"]

        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter="\t")

        # Writing the heading.
        # This step is optional.
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)


# Writing the csv using the Dictionary writer.
# Writing only some columns. (first_name, last_name)
with open("test.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")

    # newline='' to avoid printing an extra newline.
    with open("test_copy.csv", "w", newline="") as new_file:
        field_names = ["first_name", "last_name"]

        csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter="\t")

        # Writing the heading.
        # This step is optional.
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)