ip_addr = input("Please enter an IPv4 address: ")

print("Splitting the address into a list...")

ip_addr = ip_addr.split('.')

print("The address now looks like...")

print(ip_addr)

print("Converting the last octet to a 0...")

ip_addr[3] = 0

print("The address now looks like...")

print(ip_addr)

print("Now we will print the decimal and binary version of each octet...")

print(ip_addr[0])
print(bin(int(ip_addr[0])))
print(ip_addr[1])
print(bin(int(ip_addr[1])))
print(ip_addr[2])
print(bin(int(ip_addr[2])))
print(ip_addr[3])
print(bin(int(ip_addr[3])))
