#!/usr/bin/env python

# Usage
# Pulls GET information from a URL

# Imports
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

# Ignore insecure warings for sites with self-signed certificates
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

url = "https://netbox.lasthop.io/api/"
http_headers = {"accept": "application/json; version=2.4;"}
response = requests.get(url, headers=http_headers, verify=False)

# Print out information on the URL we got

print(dir(response))

pprint(response.json())
pprint(response.text)
pprint(response.status_code)
pprint(response.ok)
