#!/usr/bin/env python

# Usage
# Takes token for Slack and use it against a demo environment

# Imports
import requests
import os
from pprint import pprint
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable self-signed complaints because I'm not importing the cert as trusted
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Token assignment
token = os.environ["SLACK_TOKEN"]
print("My token is {}".format(token))

# URL of demo Slack
url = "https://slack.com/api/channels.list"

# Headers for API request
# Upper or lower case "authorization" "Authorization" works the same
# Slack requires the token format to be "Bearer token" and not just "token"
headers = {"authorization": f"Bearer {token}"}

# Make GET call using token in GET method
response = requests.get(url, headers=headers)

print("")
pprint(response.json())

# Above worked, but what about passing the token in the URL?
url = f"https://slack.com/api/channels.list?token={token}"

# Let's try this again with another GET request which does not include headers
response = requests.get(url)

# Pretty print response of URL method
pprint(response.json())

# Let's try a put operation...
data = {"token": token, "name": "student-29-channel"}
url = "https://slack.com/api/channels.create"

print("")
print("I am now trying to create a channel known as student29channel")
response = requests.put(url, data)
print(response.json())
print("")

# Huzzah I created a channel on the test API slack
