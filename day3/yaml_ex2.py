#!/usr/bin/env python

# Usage
# Creates a YAML file

# Imports
import yaml

# Load yaml file
with open("yaml_ex2_struct.yml", "r") as f:
    file = yaml.load(f)

print(file)

# Load a second yaml file
with open("yaml_ex2_struct2.yml", "r") as f:
    file = yaml.load(f)

print(file)
