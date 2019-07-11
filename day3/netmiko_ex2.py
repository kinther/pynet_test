#!/usr/bin/env python

# Usage
# Logs in and updates logging configuration

# Imports
import netmiko
from getpass import getpass

# Prompt user for password
passwd = getpass("Please input the password: ")

# Lab device variables

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": passwd,
}

# Define handler function

net_connect = netmiko.ConnectHandler(**nxos1)

# Define configuration line to send
conf_t = ["logging console 3"]

# Send command to device
net_connect.send_config_set(conf_t)

# Write to memory
net_connect.send_command("write mem")
