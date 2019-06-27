#!/usr/bin/env python

class Device:
    def __init__(self,ip_addr,username,password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

    def display_info(self):
        print('IP address: {}'.format(self.ip_addr))
        print('Username: {}'.format(self.username))
        print('Password: {}'.format(self.password))

dev1 = Device(ip_addr='192.168.1.100',username='admin',password='admin')
dev2 = Device(ip_addr='172.16.1.100',username='cisco',password='cisco')
dev3 = Device(ip_addr='10.10.1.100',username='arista',password='arista')
dev4 = Device(ip_addr='8.8.8.8',username='googleadmin',password='googlepassword')

print()
print('Network device list')
print('---------------------------------\n')
print('Device 1:')
print(dev1.display_info())
print('Device 2:')
print(dev2.display_info())
print('Device 3:')
print(dev3.display_info())
print('Device 4:')
print(dev4.display_info())
