#!/usr/bin/env python

# Usage
# Passes in three inputs and returns the sum of the three outputs

my_list = [100, 200, 300]
my_dict = {'x': 100, 'y': 200, 'z': 300}
bad_list = ['100', '200', '300']
bad_dict = {'x': '100', 'y': '200', 'z': '300'}


def func_ex1(x, y, z=20):
    return x + y + z

print()
sum = func_ex1(10, 20, 30)
print('Calling positional arguments sum: {}'.format(sum))

print()
default = func_ex1(10, 20)
print('Calling position arguments with default value for z: {}'.format(default))

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

print()
list_args = func_ex1(*my_list)
print('Calling list in *args format: {}'.format(list_args))

print()
dict_kwargs = func_ex1(**my_dict)
print('Calling dict in **kwargs format: {}'.format(dict_kwargs))

print()
print('If we try to pass a list or dictionary with string args')
print('we end up getting concatenated strings.')
bad_list_args = func_ex1(*bad_list)
bad_dict_args = func_ex1(**bad_dict)
print('For example here is a list: {}'.format(bad_list_args))
print()
print('Another example using a dictionary: {}'.format(bad_dict_args))
