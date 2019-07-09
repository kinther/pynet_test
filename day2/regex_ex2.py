#!/usr/bin/env python

# Imports
import re
from pprint import pprint

# Create data structures
dict = {
}

mac_dict = {
    "ports": "",
    "vlan": "",
    "type":"",
}

ports = []

# Open file and assign to variable
with open("show_mac_multicast.txt") as f:
    output = f.read()

# Define regex patterns to search for
pattern = r"^\s+(\d+)\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(.*)$"

# Parse data for match groups
for line in output.splitlines():
    match = re.search(pattern, line)

# Split ports along delineator and paste into list format
ports = match.group(4).split(",")

# Assign matches to dictionary values
mac_dict["vlan"] = match.group(1)
mac_dict["type"] = match.group(3)
mac_dict["ports"] = match.group(4)

dict[match.group(2)] = mac_dict

# Print data out pretty like
pprint(dict)
