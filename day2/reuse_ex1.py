#!/usr/bin/env python

# Usage
# Demonstrates how to use __name__ and main()
# Demonstrates ability to create sample code which can be
# imported later, but is not run immediately like main()

def func1():
    print("I am function 1.")

def func2():
    print("I am function 2.")

def func3():
    print("I am funcion 3.")

def main():
    print("I am the main function.")

if __name__ == "__main__":
    main()
