#!/usr/bin/env python

# Imports
import re
from pprint import pprint

# Create dictionary to hold data
dict = {
    "address": "",
    "vlan": "",
    "type": "",
    "ports": "",
}

# Open file and assign to variable
with open("show_mac_multicast.txt") as f:
    output = f.read()

# Define regex patterns to search for
patterns = "^\s+(\d+)\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(.*)$"

# Parse data for match groups and assign to dictionary values
