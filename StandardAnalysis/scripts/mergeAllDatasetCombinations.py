#!/usr/bin/env python

import sys, glob, re, itertools, subprocess, shutil

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

for year in combinations:
  for r in range (2, len (combinations[year])):
    for combination in itertools.combinations (combinations[year], r):
      joinedCombination = "".join (combination)
      if joinedCombination not in alphabet:
        continue
      arguments = datasetPrefix + "_" + year + joinedCombination + ".root"
      for i in range (0, r):
        arguments += " " + datasetPrefix + "_" + year + combination[i] + ".root"
      subprocess.call ("hadd -f " + arguments, shell = True)
  shutil.copy (datasetPrefix + "_" + year + "".join (combinations[year]) + ".root", datasetPrefix + "_" + year + ".root")
