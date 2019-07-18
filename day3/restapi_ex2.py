#!/usr/bin/env python

# Usagee
# Parse API output into JSON format and print it

# Imports
from pprint import pprint
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable self-signed complaints because I'm not importing the cert as trusted
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Assign variables from ENVIRONMENT
token = os.environ["NETBOX_TOKEN"]
token = "Token {}".format(token)

# Assign variables for API interaction
url = "https://netbox.lasthop.io/api/dcim/devices"
http_headers = {"accept": "application/json; version=2.4;","authorization": token}

# Try to connect to remove API
response = requests.get(url, headers=http_headers, verify=False)

# Try to print response
pprint(response.json())
