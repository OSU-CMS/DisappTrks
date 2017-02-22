#!/usr/bin/env python

import sys
import os
import re
from ROOT import TFile,TKey,TIter

################################################################################
# Recursive function for copying all keys from input file to output file, while
# removing "NoElectronMuonFiducialCuts" from any directory names
################################################################################
def copyAllKeys (fin, key, cwd, cwdOut, fout):
  className = key.GetClassName ()
  name = key.GetName ()
  obj = None

  if "TDirectory" in className:
    obj = fin.GetDirectory (cwd + "/" + name)
    nextIter = TIter (obj.GetListOfKeys ())
    key = nextIter ()
    nameOut = re.sub (r"NoElectronMuonFiducialCuts", r"", name)
    cwdOut = nameOut if not cwdOut else (cwdOut + "/" + nameOut)
    cwd = name if not cwd else (cwd + "/" + name)
    fout.mkdir (cwdOut)
    while key:
      copyAllKeys (fin, key, cwd, cwdOut, fout)
      key = nextIter ()
  else:
    obj = fin.Get (cwd + "/" + name)
    fout.cd (cwdOut)
    obj.Write (name)
################################################################################

################################################################################
# Get and test command line arguments
################################################################################
argc = len (sys.argv)
if argc < 3:
  print "Usage: " + sys.argv[0] + " INPUT_FILE OUTPUT_FILE"
  sys.exit (1)
inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

if not os.path.isfile (inputFileName):
  print "\"" + inputFileName + "\" does not exist!"
  sys.exit (1)
if os.path.isfile (outputFileName):
  print "\"" + outputFileName + "\" already exists!"
  sys.exit (1)
################################################################################

################################################################################
# Copy all keys from input file to output file
################################################################################
fin = TFile.Open (inputFileName)
fout = TFile.Open (outputFileName, "recreate")
nextIter = TIter (fin.GetListOfKeys ())
key = nextIter ()
cwd = ""
while key:
  copyAllKeys (fin, key, cwd, cwd, fout)
  key = nextIter ()
fin.Close ()
fout.Close ()
################################################################################
