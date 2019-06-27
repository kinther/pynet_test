#!/usr/bin/env python

# Usage parses file for specific data using regex search

import re

with open('show_int_fa4.txt') as f:
    output = f.read()

patterns = {
    'Input': r'(\d+) packets input, (\d+) bytes',
    'Output': r'(\d+) packets output, (\d+) bytes',
}

for k, v in patterns.items():
    match = re.search(v, output)
    if match:
        print('\n{}:'.format(k))
        print('Packets: {}'.format(match.group(1)))
        print('Bytes: {}'.format(match.group(2)))



