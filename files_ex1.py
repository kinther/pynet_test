#!/usr/bin/env python

with open('inputfile', 'r') as f:
    for line in f:
        print(line)
    f.close()

with open('outputfile', 'w') as ff:
    ff.write('This is a test of the emergency broadcast system.\n')
    ff.close()

with open('outputfile', 'a+') as fff:
    fff.write('This is only a test.\n')
    fff.close()
