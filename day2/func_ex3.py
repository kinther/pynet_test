#!/usr/bin/env python

# Usage
# Takes file input and returns it in string format
# Opens file and returns only a specific substring

def func1(filename):
    with open(filename, 'r') as f:
        f = f.read()
        return f

def func2():
    with open('show_version.txt', 'r') as f:
        f = f.read().splitlines()
        for line in f:
            if 'CISCO881-SEC-K9' in line:
                serial = line.split()
                return serial[2]

print()
print(func1('show_version.txt'))

print()
print(func2())
