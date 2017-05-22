#!/usr/bin/env python

import subprocess
import sys
import re
import numpy
import socket
import os

from ROOT import TFile, TH1D, TH2D

coresPerNode = {
  0: 8,
  1: 8,
  2: 8,
  3: 8,
  4: 16,
  5: 16,
  6: 16,
  7: 16,
  8: 16,
  9: 24,
  10: 24,
  11: 24,
  12: 24,
  13: 24,
  14: 24,
  15: 24,
  16: 24,
  17: 24,
  18: 24,
  19: 8,
  20: 8,
  21: 8,
  22: 8,
  23: 8,
  24: 8,
  25: 8,
  26: 8,
  27: 8,
  28: 8,
  29: 8,
}

if len (sys.argv) < 2:
  print "Usage: " + os.path.basename (sys.argv[0]) + " CONDOR_DIR [OUTPUT_FILE]"
  sys.exit (1)
condorDir = sys.argv[1]
outputFile = "eventTimes.root"
if len (sys.argv) > 2:
  outputFile = sys.argv[2]

nBins = 200

cpuTimePerEvent = []
realTimePerEvent = []
node = []

################################################################################
# Extract times from output files
################################################################################
print "extracting times from output files..."
command = ["find", condorDir, "-type", "f", "-regex", ".*\/condor_[^/]*\.err$"]
stdErrFiles = subprocess.check_output (command).split ()
for stdErrFile in stdErrFiles:
  isFinished = False
  f = open (stdErrFile, "r")
  for line in f:
    if not re.match (r".*CPU time.*", line) and not re.match (r".*real time.*", line):
      continue
    isFinished = True
    timePerEvent = float (re.sub (r".*\(([^ ]*) seconds per event\)$", r"\1", line))
    if re.match (r".*CPU time.*", line):
      cpuTimePerEvent.append (timePerEvent)
    if re.match (r".*real time.*", line):
      realTimePerEvent.append (timePerEvent)
  f.close ()

  if not isFinished:
    continue

  logFile = re.sub (r"(.*)\.err$", r"\1.log", stdErrFile)
  f = open (logFile, "r")
  for line in reversed (f.readlines ()):
    if not re.match (r".*Job executing on host.*", line):
      continue
    ipAddress = re.sub (r".*Job executing on host: <([^:]*):.*>$", r"\1", line)
    hostName = socket.gethostbyaddr (ipAddress)[0]
    hostNumber = int (re.sub (r"compute-0-(.*)\.local", r"\1", hostName))
    node.append (hostNumber)
    break
  f.close ()
################################################################################

################################################################################
# Fill histograms with times
################################################################################
print "filling histograms with times..."
cpuTime = []
realTime = []
cpuTime.append (TH1D ("cpuTime10p0", ";CPU time per event [s/evt];number of jobs", nBins, 0.0, 10.0))
cpuTime.append (TH1D ("cpuTime1p0", ";CPU time per event [s/evt];number of jobs", nBins, 0.0, 1.0))
cpuTime.append (TH1D ("cpuTime0p1", ";CPU time per event [s/evt];number of jobs", nBins, 0.0, 0.1))
cpuTime.append (TH1D ("cpuTime0p01", ";CPU time per event [s/evt];number of jobs", nBins, 0.0, 0.01))
cpuTime.append (TH1D ("cpuTime0p001", ";CPU time per event [s/evt];number of jobs", nBins, 0.0, 0.001))
cpuTime.append (TH1D ("cpuTime0p0001", ";CPU time per event [s/evt];number of jobs", nBins, 0.0, 0.0001))
cpuTime.append (TH1D ("cpuTime0p00001", ";CPU time per event [s/evt];number of jobs", nBins, 0.0, 0.00001))
cpuTime.append (TH1D ("cpuTime_log", ";CPU time per event [s/evt];number of jobs", nBins, numpy.logspace (-5, 1, nBins + 1)))
cpuTimeVsNode = TH2D ("cpuTimeVsNode", ";;CPU time per event [s/evt];number of jobs/core", 30, -0.5, 29.5, nBins, numpy.logspace (-5, 1, nBins + 1))
realTime.append (TH1D ("realTime10p0", ";real time per event [s/evt];number of jobs", nBins, 0.0, 10.0))
realTime.append (TH1D ("realTime1p0", ";real time per event [s/evt];number of jobs", nBins, 0.0, 1.0))
realTime.append (TH1D ("realTime0p1", ";real time per event [s/evt];number of jobs", nBins, 0.0, 0.1))
realTime.append (TH1D ("realTime0p01", ";real time per event [s/evt];number of jobs", nBins, 0.0, 0.01))
realTime.append (TH1D ("realTime0p001", ";real time per event [s/evt];number of jobs", nBins, 0.0, 0.001))
realTime.append (TH1D ("realTime0p0001", ";real time per event [s/evt];number of jobs", nBins, 0.0, 0.0001))
realTime.append (TH1D ("realTime0p00001", ";real time per event [s/evt];number of jobs", nBins, 0.0, 0.00001))
realTime.append (TH1D ("realTime_log", ";real time per event [s/evt];number of jobs", nBins, numpy.logspace (-5, 1, nBins + 1)))
realTimeVsNode = TH2D ("realTimeVsNode", ";;real time per event [s/evt];number of jobs/core", 30, -0.5, 29.5, nBins, numpy.logspace (-5, 1, nBins + 1))

for i in range (1, cpuTimeVsNode.GetNbinsX () + 1):
  cpuTimeVsNode.GetXaxis ().SetBinLabel (i, "compute-0-" + str (i - 1))
for i in range (1, realTimeVsNode.GetNbinsX () + 1):
  realTimeVsNode.GetXaxis ().SetBinLabel (i, "compute-0-" + str (i - 1))

i = 0
for time in cpuTimePerEvent:
  for hist in cpuTime:
    hist.Fill (time)
  cpuTimeVsNode.Fill (node[i], time, 1.0 / coresPerNode[node[i]])
  i += 1
i = 0
for time in realTimePerEvent:
  for hist in realTime:
    hist.Fill (time)
  realTimeVsNode.Fill (node[i], time, 1.0 / coresPerNode[node[i]])
  i += 1
################################################################################

################################################################################
# Write the histograms to a file
################################################################################
f = TFile.Open (outputFile, "recreate")
for hist in cpuTime:
  hist.Write ()
cpuTimeVsNode.Write ()
for hist in realTime:
  hist.Write ()
realTimeVsNode.Write ()
f.Close ()
print "wrote times to " + outputFile
################################################################################
