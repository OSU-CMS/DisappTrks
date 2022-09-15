#!/usr/bin/env python3

import os
import subprocess
import sys

if len(sys.argv) < 2:
    sys.exit(187)

fileName = sys.argv[1]

if not subprocess.call('edmFileUtil ' + fileName, shell = True) == 0:
	print 'Input file: ' + fileName + ' is not an EDM file, or does not exist!'
	sys.exit(187)

if fileName.startswith('/store/'):
	fileName = subprocess.check_output(['edmFileUtil', '-d', fileName]).strip()

from DataFormats.FWLite import Events
events = Events(fileName)
for event in events:
    if event.eventAuxiliary().isRealData():
        sys.exit(1)
    else:
        sys.exit(0)

sys.exit(187)
