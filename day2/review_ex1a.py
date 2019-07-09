#!/usr/bin/env python

# Usage
# Creates a dictionary of dictionaries similar to
# regex_ex2.py
# using a simpler method of splitting lines

# Imports
from pprint import pprint

# Create data structures
dict = {}

# Open file and assign to variable
with open("show_ip_int_brief.txt") as f:
    output = f.read()

# Loop over file output, adding data to dictionaries
for line in output.splitlines():
    if "Interface" in line:
        pass
    else:
        interface, ip_address, _, _, line_protocol, line_status = line.split()
        dict[interface] = {"ip_address": ip_address,
                           "line_protocol": line_protocol,
                           "line_status": line_status,
                          }

# Print dictionary pretty like
pprint(dict)
