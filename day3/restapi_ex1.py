#!/usr/bin/env python

# Usage
# Opens a REST API and performs a GET

# Imports
import requests
from urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

# Variables
http_headers = {"accept": "application/json; version=2.4;"}
url = "https://netbox.lasthop.io/api"

# Disable self-signed certificate complaints
requests.urllib3.disable_warnings(InsecureRequestWarning)

# Try to open remote site
response = requests.get(url, http_headers, verify=False)

# Print out data types from response
pprint(dir(response))

# Print out whether the response was OK or not
print("Was the response from the server ok? - {}".format(response.ok))

# Print out the status code from the HTTP GET
print("Status code from the HTTP GET was {}.".format(response.status_code))

# Print out the URL we queried with HTTP GET
print("The url we queried was {}.".format(response.url))

# Print out any text that was called
print("Text from the HTTP GET was {}.".format(response.text))

# Print out the json data format pretty like
print("Json format:")
pprint(response.json())
