#!/usr/bin/env python

# Usage
# Creates a function which is imported into the shell
# This library is in another directory, forcing the
# student to test how to adjust their environmental
# paths

# Define function to be called
def awesome():
    print("You have done it!")
    print("Awesome job!")

# Modified .bashrc file and added lines
# export PYTHONPATH:$HOME/pynet_test
# source .bashrc
# then was able to call the library from a different
# directory
