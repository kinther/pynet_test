#!/usr/env/python

ip_addr = input("Please enter an IPv4 address: ")

ip_addr = ip_addr.split(".")

print("{:<12}".format(ip_addr[0]))
print("{:<12}".format(ip_addr[1]))
print("{:<12}".format(ip_addr[2]))
print("{:<12}".format(ip_addr[3]))
