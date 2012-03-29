#/usr/bin/python

# level2.py
import urllib

url = r"http://www.pythonchallenge.com/pc/def/ocr.html"

chars = urllib.urlopen(url).readlines()
start = chars.index('find rare characters in the mess below:\n') + 1

print filter(lambda x: x.isalpha(), ''.join(chars[start: -1]))
