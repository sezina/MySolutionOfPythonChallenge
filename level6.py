#!/usr/bin/env python

# level6.py

# The hint means that change 'channel.html' to 'channel.zip'
# you will need download the zipfile

from re import compile
from zipfile import ZipFile

findNum = compile(r'\d+$').findall
myzip = ZipFile('channel.zip')

zipDataCollector = []
filename = '90052.txt'
while True:
    zipInfo = myzip.getinfo(filename)
    f = myzip.open(filename)
    data = findNum(f.read())
    f.close()
    zipDataCollector.append(zipInfo.comment)
    if data:
        filename = '%s.txt' % data[0]
    else:
        break

print ''.join(zipDataCollector)

# Run this script, apply the answer to the url.
# You may get a new hint.
# Do as the hint recomment. You will get the final answer.
