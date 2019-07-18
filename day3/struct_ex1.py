#!/usr/bin/env python

# Usage
# Tests out parsing json

# Imports
import json
from pprint import pprint

# Open file
with open("struct_data1.json", "r") as f:
    file = json.load(f)

# Print the file as a test
pprint(file)
print("")

# Print the type and length of each entry
print(type(file))
print(len(file))

# Assign list position 0 to a variable
list0 = file[0]

# Print type and length of list0
print(type(list0))
print(len(list0))

# Create dictionary to hold data we care about
parsed_data = {}

# Iterate over file and parse data into dictionary
for list in file:
    if list["protocol"] is not "L":
        route = list["network"]
        nexthop = list["nexthop_if"]
        nextip = list["nexthop_ip"]
        parsed_data[route] = {"nexthop_interface": nexthop,
                              "nexthop_ip": nextip,
                             }
    else:
        pass

# Print out the new data structure
pprint(parsed_data)
