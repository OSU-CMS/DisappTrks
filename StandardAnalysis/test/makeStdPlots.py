#!/usr/bin/python

# Create single pdf with
# Usage:
# makeStdPlots.py MYCONDORDIR


import os
import sys

if len(sys.argv) < 2:
    print("ERROR:  Must specify name of condor directory as argument.")
    exit(0)

condorDir = "condor/" + sys.argv[1]

pwd = os.getcwd()

plotDirs = os.listdir(condorDir + "/stacked_histograms_pdfs/")

outputNames = []
finalPlotDirs = []

for plotDir in plotDirs:
    if "Plotter" in plotDir and not "CutFlow" in plotDir:
        outputNames.append(plotDir + "_mergedStd.pdf")
        finalPlotDirs.append(os.path.join(condorDir, "stacked_histograms_pdfs", plotDir))

plotsList = [
    "Met_Plots/metPt.pdf",
    "Jet_Plots/jetPt.pdf",
    "Jet_Plots/jetEta.pdf",
    "Eventvariable_Plots/dijetMaxDeltaPhi.pdf",
    "Met-eventvariable_Plots/deltaPhiMetJetLeading.pdf",
    "Met-eventvariable_Plots/deltaPhiMetJetSubleading.pdf",
    "Track_Plots/trackPt.pdf",
    "Track_Plots/trackEta.pdf",
    "Track_Plots/trackNumValidHits.pdf",
    "Track_Plots/trackNHitsMissingInner.pdf",
    "Track_Plots/trackNHitsMissingMiddle.pdf",
    "Track_Plots/trackIsolation.pdf",
    "Track-eventvariable_Plots/trackd0WRTPV_Zoom.pdf",
    "Track-eventvariable_Plots/trackdzWRTPV_Zoom.pdf",
    "Track_Plots/trackDRMinJet.pdf",
    "Track_Plots/trackDeltaRToClosestElectron.pdf",
    "Track_Plots/trackDeltaRToClosestMuon.pdf",
    "Track_Plots/trackDeltaRToClosestTauHad.pdf",
    "Track_Plots/trackNHitsMissingOuter.pdf",
    "Track_Plots/trackCaloNew_RhoCorr.pdf",
]

for i in range(0, len(finalPlotDirs)):

    print("\n\nMoving to directory: ", finalPlotDirs[i])
    os.chdir(pwd)
    os.chdir(finalPlotDirs[i])

    cmd = "mergePdf.py " + outputNames[i] + " "
    for plot in plotsList:
        cmd += plot + " "
    print("Executing command: " + cmd)
    os.system(cmd)

    os.system("mv " + outputNames[i] + " ../../")
    print("Finished writing plot to ", os.path.join(condorDir, outputNames[i]))


