#!/usr/bin/env python

# Usage
# Runs command remotely on multiple devices concurrently

# Imports
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor, wait

# Create dictionary with login information for netmiko
devices = [{"host": "cisco3.lasthop.io",
            "username": "pyclass",
            "password": "88newclass",
            "device_type": "cisco_ios",
           },
           {"host": "cisco4.lasthop.io",
            "username": "pyclass",
            "password": "88newclass",
            "device_type": "cisco_ios",
           },
           {"host": "arista1.lasthop.io",
            "username": "pyclass",
            "password": "88newclass",
            "device_type": "arista_eos",
           },
           {"host": "arista2.lasthop.io",
            "username": "pyclass",
            "password": "88newclass",
            "device_type": "arista_eos",
           },
          ]


# Define command to be sent
cmd = "show ip arp"


# Define netmiko connection function
def send_command(devices, cmd):
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command(cmd)
    net_connect.disconnect()
    return output


# Define main function
def main():
    with ThreadPoolExecutor(max_workers=8) as pool:
        procs = []
        for dev in devices:
            procs.append(pool.submit(send_command, dev, "show ip arp"))
        wait(procs)
        for proc in procs:
            print("")
            print(proc.result())
            print("")

# Call main function
if __name__ == "__main__":
    main()
