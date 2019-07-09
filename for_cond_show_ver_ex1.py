#!/usr/bin/env python

serial = ''

with open('show_version.txt', 'r') as f:
    for line in f:
        if 'CISCO881-SEC-K9' in line:
           split = line.split()
           serial = split[2]

print(serial) 
