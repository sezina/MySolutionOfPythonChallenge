#!/usr/bin/python

# level4.py
import urllib
from string import split
import re

urlPrefix = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
url = urlPrefix + '12345'

for i in range(400):
    urlData = urllib.urlopen(url).read()
    if ".html" in urlData:
        print urlData
        break
    urlPostfix = split(urlData, ' ')[-1]
    url = urlPrefix + urlPostfix
