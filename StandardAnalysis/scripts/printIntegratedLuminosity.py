#!/usr/bin/env python

from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
import sys, os

def printValidKeys ():
    for x in sorted (lumi.keys ()):
        print "  " + x
        if isinstance (lumi[x], dict):
            for y in sorted (lumi[x].keys ()):
                print "    " + y

if len (sys.argv) < 2:
    print "Usage: " + os.path.basename (sys.argv[0]) + " KEY SUB_KEY"
    print ""
    print "Valid values for KEY and SUB_KEY are the following:"
    printValidKeys ()
    sys.exit (1)

if sys.argv[1] not in lumi or (len (sys.argv) > 2 and sys.argv[2] not in lumi[sys.argv[1]]) or (len (sys.argv) < 3 and isinstance (lumi[sys.argv[1]], dict)):
    print "Invalid KEY or SUB_KEY. Valid values are the following:"
    printValidKeys ()
    sys.exit (1)

print "integrated luminosity for",
if len (sys.argv) < 3:
    print sys.argv[1] + ": " + str (lumi[sys.argv[1]]) + "/pb"
else:
    print sys.argv[2] + " (" + sys.argv[1] + "): " + str (lumi[sys.argv[1]][sys.argv[2]]) + "/pb"
