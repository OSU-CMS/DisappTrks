#!/usr/bin/env python

import sys, glob, re, itertools, subprocess, shutil, copy

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if len (sys.argv) < 2:
  print "Usage: " + sys.argv[0] + " DATASET_PREFIX"
  sys.exit (1)
datasetPrefix = sys.argv[1]

existingFiles = glob.glob (datasetPrefix + "_?????.root")
combinations = {}
for existingFile in existingFiles:
  year = re.sub (r"^.*_([0-9]*)([A-Z]*)\.root$", r"\1", existingFile)
  era = re.sub (r"^.*_([0-9]*)([A-Z]*)\.root$", r"\2", existingFile)
  if year not in combinations:
    combinations[year] = [era]
  else:
    combinations[year].append (era)

for year in combinations:
  combinations[year] = sorted (list (set (combinations[year])))

commands = {}
for year in combinations:
  for r in range (2, len (combinations[year]) + 1):
    for combination in itertools.combinations (combinations[year], r):
      joinedCombination = "".join (combination)
      if joinedCombination not in alphabet:
        continue
      outputFile = datasetPrefix + "_" + year + joinedCombination + ".root"
      arguments = copy.deepcopy (outputFile)
      for i in range (0, r):
        arguments += " " + datasetPrefix + "_" + year + combination[i] + ".root"
      commands[outputFile] = "hadd -f -k " + arguments

i = 0
for outputFile in sorted (commands.keys ()):
  print "================================================================================"
  print "Merging combination " + str (i + 1) + "/" + str (len (commands)) + ": \"" + outputFile + "\"..."
  print "--------------------------------------------------------------------------------"
  subprocess.call (commands[outputFile], shell = True)
  i += 1
  print "================================================================================\n"

for year in combinations:
  shutil.copy (datasetPrefix + "_" + year + "".join (combinations[year]) + ".root", datasetPrefix + "_" + year + ".root")
