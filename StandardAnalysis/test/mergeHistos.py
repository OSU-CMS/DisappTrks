import os
import sys
from os.path import exists

inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_Pythia100_100_candidateTracksNoSkimming/"
inpFile = "histos_100_Pythia100.txt"
outFile = "hist_merged_100_Pythia100.root"

if exists(outFile): os.system("rm " + outFile)

os.system("ls " + inpPath + "*.root > " + inpFile)

# Using readlines()
file1 = open(inpFile, 'r')
Lines = file1.readlines()
  
histos = ''

# Strips the newline character
for line in Lines:
    histos += line.strip()+' '

os.system("hadd -k -j 8 " + outFile + " " + histos)
