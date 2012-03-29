#!/usr/bin/python

#level3.py
import urllib
import re

url = r"http://www.pythonchallenge.com/pc/def/equality.html"
webData = urllib.urlopen(url).readlines()
startIndex = webData.index('<!--\n') + 1
patternStr = '(?:^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?:[^A-Z]|$)'
targetPattern = re.compile(patternStr)

print ''.join(re.findall(targetPattern, ''.join(webData[startIndex:-1])))
