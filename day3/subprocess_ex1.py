#!/usr/bin/env python

# Usage
# Tests subprocess and popen

# Imports
import subprocess
from pprint import pprint

# Create function for sending argument
def check_fs():
    command = ["df", "-h"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = process.communicate()
    (std_out, std_err) = [x.decode("utf-8") for x in (std_out, std_err)]
    return std_out

# Create function to parse output and return list
def parse_data(input):
    list = []
    for line in input.splitlines():
        if "Size" in line:
            pass
        else:
            dict = {}
            line = line.split()
            dict["filesystem"] = line[0]
            dict["usage"] = line[4]
            list.append(dict)
    return list

# Create main function
def main():
    output = check_fs()
    data = parse_data(output)
    pprint(data)

# Call main function
if __name__ == "__main__":
    main()
