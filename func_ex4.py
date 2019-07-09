#!/usr/bin/env python

# Usage
# Takes file input and returns it in string format
# Finds specific data points and enters them into a dictionary

# Import needed modules
import pprint

# Define global variables
device_info = {
    'Vendor': '',
    'Model Number': '',
    'Version': '',
    'Serial number': '',
    'Uptime': '',
}

# Define global functions

def readfile(filename):
    with open(filename, 'r') as f:
        f = f.read()
        return f

def findvendor(input):
    for line in input.splitlines():
        if 'Cisco' in line:
            device_info['Vendor'] = 'Cisco'
            break
        elif 'Juniper' in line:
            device_info['Vendor'] = 'Juniper'
            break
        elif 'Arista' in line:
            device_info['Vendor'] = 'Arista'
            break
        else:
            device_info['Vendor'] = 'Unknown'

def findmodel(input):
    for line in input.splitlines():
        if 'processor' in line:
            model = line.split()
            device_info['Model Number'] = model[1]
            break
        else:
            device_info['Model Number'] = 'Unknown'

def findversion(input):
    for line in input.splitlines():
        if 'Software' in line:
            version = line.split()
            device_info['Version'] = version[7]
            break
        else:
            device_info['Version'] = 'Unknown'

def findserial(input):
    for line in input.splitlines():
        if 'CISCO881-SEC-K9' in line:
            serial = line.split()
            device_info['Serial number'] = serial[2]
            break
        else:
            device_info['Serial number'] = 'Unknown'

def finduptime(input):
    for line in input.splitlines():
        if 'uptime' in line:
            time = line.split()
            weeks = (time[3] + ' ' + time[4])
            days = (time[5] + ' ' + time[6])
            hours = (time[7] + ' ' + time[8])
            minutes = (time[9] + ' ' + time[10])
            device_info['Uptime'] = (weeks + ' ' + days + ' ' +
                                     hours + ' ' + minutes)
            break
        else:
            device_info['Uptime'] = 'Unknown'

# Open file to for later parsing

file = readfile('show_version.txt')

# Call functions and input data into dictionary

findvendor(file)
findmodel(file)
findversion(file)
findserial(file)
finduptime(file)

pprint.pprint(device_info)
