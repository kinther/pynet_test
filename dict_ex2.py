router = {
    "addr" : "192.168.1.100",
    "user" : "admin",
    "pass" : "admin",
    "vendor" : "cisco",
    "model" : "9372TX"
    }

for key,value in router.items():
    print("The {} field has an entry of {}.".format(key,value))

print("Password being updated...")

router["password"] = "admin123"

print("Adding secret to dictionary...")

router["secret"] = "cisco123"

print("Checking device_type key...")

try:
    router.get(device_type)
except:
    print("cisco_ios")
