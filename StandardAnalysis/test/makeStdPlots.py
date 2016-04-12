#!/usr/bin/python

# Create single pdf with 
# Usage:
# makeStdPlots.py MYCONDORDIR


import os  
import sys 

if len(sys.argv) < 2:
    print "ERROR:  Must specify name of condor directory as argument."
    exit(0)  

condorDir = "condor/" + sys.argv[1]  

plotDirs = os.listdir(condorDir + "/stacked_histograms_pdfs/") 

for plotDir in plotDirs:  
    if "Plotter" in plotDir and not "CutFlow" in plotDir:
        finalPlotDir = os.path.join(condorDir, "stacked_histograms_pdfs", plotDir) 

plotsList = [
    "Met_Plots/metPt.pdf", 
    "Jet_Plots/jetPt.pdf", 
    "Jet_Plots/jetEta.pdf", 
    "Eventvariable_Plots/dijetMaxDeltaPhi.pdf", 
    "Eventvariable_Plots/deltaPhiMetJetLeading.pdf", 
    "Eventvariable_Plots/deltaPhiMetJetSubleading.pdf", 
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

output = "mergedStd.pdf"  

os.chdir(finalPlotDir) 
print "Moving to directory: ", finalPlotDir

cmd = "mergePdf.py " + output + " "
for plot in plotsList:
    cmd += plot + " " 
print "Executing command: " + cmd
os.system(cmd)

os.system("mv " + output + " ../../") 
print "Finished writing plot to ", os.path.join(condorDir, output) 


