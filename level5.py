#!/usr/bin/python

# level5.py

# peakhell sounds like pickle
# Read the sourecode of the webpage
# Find "banner.p" and download this file

import pickle

f = open('banner.p', 'r')
for line in pickle.load(f):
    print ''.join([element[0] * element[1] for element in line])
