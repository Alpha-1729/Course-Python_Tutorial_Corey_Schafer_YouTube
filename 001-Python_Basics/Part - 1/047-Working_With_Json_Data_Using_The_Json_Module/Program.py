#!/usr/bin/python3
# Working With Json Data Using The Json Module

"""
>>>> JSON
        JavaScript Object Notation
>>>> Refer the screenshot attached.
        How the string value get converted to python will be shown in the screenshot.
>>>>
>>>>
"""

import json

people_string = """
{
    "people" : [
        {
            "name" : "John Smith",
            "phone" : "615-555-7164",
            "emails" : ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license" : false
        },
        {
            "name" : "John Doe",
            "phone" : "560-555-5153",
            "emails" : null,
            "has_license" : true
        }
    ]
}
"""

# Convert json string to a dictionary.
data = json.loads(people_string)
print(data)
print(type(data))

# Accessing the information in the json string.
for person in data["people"]:
    print(person["name"])

    # Delete data from the dict.
    # This is for editing the data and write back to a file.
    del person["phone"]


# Converting data dictionary back to json string.
# indent = 4 will indentation to the data in the dict.
# sort_keys = True will sort the keys in the dict.
new_string = json.dumps(data, indent=4, sort_keys=True)
print(new_string)

# Reading json from a file.
with open("people.json", "r") as f:
    data = json.load(f)
print(data)

# Dumping json to file.
with open("people_new.json", "w") as f:
    json.dump(data, f, indent=2)
