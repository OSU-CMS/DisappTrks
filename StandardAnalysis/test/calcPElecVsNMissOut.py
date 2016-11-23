#!/usr/bin/env python

# Calculate the electron veto probability, for different cuts on number of missing outer hits.  

from OSUT3Analysis.Configuration.histogramUtilities import * 
from DisappTrks.StandardAnalysis.utilities import * 
dirs = getUser() 

def getEff(num, numerr, den, denerr):
    eff    = num / den if den else 0
    efferr = numerr / den if den else 0  
    if numerr < 0.001: # very close to 0
        efferr = 1.139 / den 
        # use 1.139 = 68% CL upper limit on observation of 0, 
        # assuming lumi weight of 1.0 (not correct for MC!)  
        # taken from https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp#L101 
    return eff, efferr 

def printValues(sample, condorDir, condorDirDen, channel, channelDen, hist, lo, hi):
    num, numerr = getHistIntegral (sample, condorDir,    channel,    hist, lo, hi)
    den, denerr = getHistIntegral (sample, condorDirDen, channelDen, hist, lo, hi)  
    eff, efferr = getEff(num, numerr, den, denerr) 
    print "Eff for sample", sample, " for NMissOut in range: [", lo, ",", hi, "]: ", eff, "+-", efferr  


sample = "allBkgd"
condorDir = dirs['Wells']+"ZtoEleDisTrk" 
channel = "ZtoEleDisTrkPlotter" 
condorDirDen = dirs['Wells']+"ZtoEleProbeTrkWithZCuts" 
channelDen   = "ZtoEleProbeTrkWithZCutsPlotter" 
hist = "Track Plots/trackNHitsMissingOuter"
lo = 0
hi = 2
printValues(sample, condorDir, condorDirDen, channel, channelDen, hist, lo, hi)
lo = 3
hi = 15
printValues(sample, condorDir, condorDirDen, channel, channelDen, hist, lo, hi)

sample = "SingleEle_2015D"  
lo = 0
hi = 2
printValues(sample, condorDir, condorDirDen, channel, channelDen, hist, lo, hi)
lo = 3
hi = 15
printValues(sample, condorDir, condorDirDen, channel, channelDen, hist, lo, hi)

