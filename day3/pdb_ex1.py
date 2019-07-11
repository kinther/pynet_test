#!/usr/bin/env python

# Usage
# Passes in three inputs and returns the sum of the three outputs

def func_ex1(x, y, z=20):
    return x + y + z

print()
sum = func_ex1(10, 20, 30)
print('Calling positional arguments sum: {}'.format(sum))

print()
default = func_ex1(10, 20)
print('Calling position arguments with default value for z: {}'.format(default))

import pdb
pdb.set_trace()

print()
named = func_ex1(x=10, y=20)
print('Calling named arguments with default value for z: {}'.format(named))

print()
mixed = func_ex1(10, y=20, z=35)
print('Calling mixed arguments: {}'.format(mixed))

print()
strings = func_ex1('hello', 'goodbye', 'farewell')
print('Calling string arguments: {}'.format(strings))

print()
lists = func_ex1(x=["5"], y=["10"], z=["15"])
print('Calling lists arguments: {}'.format(lists))
