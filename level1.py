#!/usr/bin/python

# level1.py
import string

hintStr = '''g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj.'''

print "The hint is: "
print hintStr.translate(string.maketrans(string.lowercase,
                        string.lowercase[2:] + string.lowercase[:2]))

solutionStr = "map"

print "\nThe solution is: "
print solutionStr.translate(string.maketrans(string.lowercase,
                            string.lowercase[2:] + string.lowercase[:2]))
