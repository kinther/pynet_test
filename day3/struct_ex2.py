#!/usr/bin/env python

# Usage
# Function parses Slack API for list of channels
# Function sends a message to "random" channel

# Imports
import requests
import os
from pprint import pprint

# Variables
token = os.environ["SLACK_TOKEN"]
url = f"https://slack.com/api/channels.list?token={token}"

# Function to parse channels list
def get_list():
    response = requests.get(url)
    channels = response.json()["channels"]
    for list in channels:
        if "random" in list["name"]:
            print("My channel name is {}".format(list["name"]))
            print("My channel id is {}".format(list["id"]))

# Call the function and see if we find the right channel
get_list()

# Updating variables for posting a message to Slack channel
message = "Patrick wuz here"
data = {"token": token, "channel": "CET1DP0KU", "text": message}
url = "https://slack.com/api/chat.postMessage"

# New function for posting chat messages
def post_msg():
    response = requests.put(url, data)
    success = response.json()["message"]
    print("My timestamp is {}".format(success["ts"]))
    print("My username is {}".format(success["username"]))


# Post it!
post_msg()
