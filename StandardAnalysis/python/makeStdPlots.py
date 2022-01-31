#!/usr/bin/python

# Make standard plots desired for most selections.
# Assumes that the pdf's of the individual plots have been saved as pdf's in the current directory.
# Usage:
# makeStdPlots.py condorDir
# condorDir is the directory in condor/ where the merged plot should be stored

import os
import sys

if len(sys.argv) < 2:
    print("Error:  Must specify as argument the condor directory")
    exit(0)

command = "gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile="
condorDir = sys.argv[1]
command += "condor/" + condorDir + "/merged.pdf "
plots = [
    "genMatchedPromptFinalStateIsMatched.pdf",
    "genMatchedPromptFinalStatePdgIdNoHadrons.pdf",
    "genMatchedDirectPromptTauDecayProductFinalStateIsMatched.pdf",
    "genMatchedDirectPromptTauDecayProductFinalStatePdgIdNoHadrons.pdf",
    "metPt.pdf",
    "jetPt.pdf",
    "trackPt.pdf",
    "trackEta.pdf",
    "trackIsolation.pdf",
    "trackNumValidHits.pdf",
    "trackNHitsMissingOuter.pdf",
    "trackCaloTot_RhoCorr.pdf"
]

for plot in plots:
    command += plot + " "

print("Executing: ", command)
os.system(command)

