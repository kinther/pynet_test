#!/usr/bin/env python

# Usage
# Creates a dictionary of ARP mappings and prints it

# Imports
from pprint import pprint

# Create data structures
ip_dict = {}
mac_dict = {}

# Open file and assign to variable
with open("show_arp.txt") as f:
    output = f.read()

# Parse output
for line in output.splitlines():
    if "Protocol" in line:
        pass
    else:
        _, ip_addr, _, mac_addr, _, _ = line.split()
        ip_dict[ip_addr] = mac_addr
        mac_dict[mac_addr] = ip_addr

# Print output pretty like
print("IP to MAC mappings:")
print("--------------------------------")
pprint(ip_dict)
print("\n\n")
print("MAC to IP mappings:")
print("--------------------------------")
pprint(mac_dict)
