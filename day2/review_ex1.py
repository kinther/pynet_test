#!/usr/bin/env python

# Usage
# Creates a dictionary of dictionaries similar to
# regex_ex2.py
# while this kind of works, it doesn't capture the IP
# on one of the lines correctly

# Imports
from pprint import pprint
import re

# Create data structures
dict = {}
port_dict = {}

# Open file and assign to variable
with open("show_ip_int_brief.txt") as f:
    output = f.read()

# Create pattern for parsing data
pattern = r"^(.+\d+)\s+(\w+|\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(\w+)\s+(unset|NVRAM)\s+(\w+)\s+(\w+).*$"

# Loop over file output, adding data to dictionaries
for line in output.splitlines():
    try:
        match = re.search(pattern, line)
        port_dict["ip_address"] = match.group(2)
        port_dict["line_protocol"] = match.group(5)
        port_dict["line_status"] = match.group(6)
        dict[match.group(1)] = port_dict
    except:
        pass

# Print dictionary pretty like
pprint(dict)
