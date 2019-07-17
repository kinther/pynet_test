#!/usr/bin/env python

# Usage
# Tests using a YAML file as a device entry
# for netmiko logins

# Imports
from netmiko import ConnectHandler
import yaml
from getpass import getpass

# Open YAML file as device
def yaml_file(input):
    with open(input) as f:
        return yaml.load(f)

# Connect to device with Netmiko
def net_connect():
    devices = yaml_file("some_device.yml")
    password = getpass()
    for a_device in devices:
        device_name = a_device.pop("device_name")
        print("Connecting to {}...".format(device_name))
        a_device["password"] = password
        net_conn = ConnectHandler(**a_device)
        print(net_conn.send_command("show arp"))
        net_conn.disconnect()
    print()

net_connect()
