#!/usr/bin/env python

# Usage
# Checks version information on two lab devices

# Imports
import netmiko
from getpass import getpass

# Lab device variables

cisco3 = {
    'device_type': 'cisco_ios',
    'host':   'cisco3.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
}

srx2 = {
    'device_type': 'juniper_junos',
    'host':   'srx2.lasthop.io',
    'username': 'pyclass',
    'password': getpass(),
}

# Define global variables

cisco_connect = netmiko.ConnectHandler(**cisco3)
juniper_connect = netmiko.ConnectHandler(**srx2)

# Print out prompt from each device

print(cisco_connect.find_prompt())
print(juniper_connect.find_prompt())

# Gather show version output

cver = cisco_connect.send_command("show version")
jver = juniper_connect.send_command("show version")

# Gather running config output

crun = cisco_connect.send_command("show run")
jrun = juniper_connect.send_command("show configuration")

# Write running config to file

with open("cisco_run_conf.txt", "w+") as f:
    f.write(crun)

with open("juniper_run_conf.txt", "w+") as f:
    f.write(jrun)
