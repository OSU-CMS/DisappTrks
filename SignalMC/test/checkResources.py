#!/usr/bin/python

# This script makes plots of the resource usage of condor jobs.
# It was designed for CMSSW simulation jobs, but could be adapted for other 
# types of jobs, as long as the information is included in the stdout 
# or stderr files.  
#
# For CMSSW jobs, to get the memory usage, add the following to the config file:
process.SimpleMemoryCheck = cms.Service("SimpleMemoryCheck")  
# See for reference:  https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideEDMTimingAndMemory  


import os
from ROOT import gROOT, TGraphErrors, TCanvas, TH1F, TStyle, gStyle, TColor 

gROOT.SetBatch() # Do not open TCanvas
gStyle.SetOptStat(0)

def getUsage(cmd, step, y, yerr):
    fullcmd = cmd[0] + step + cmd[1]   # cmd is list of 2 strings 
    print "fullcmd = ", fullcmd  
    usage = os.popen(fullcmd).read().split("\n")
    usage = sorted(usage)  
    idxMedian = int(len(usage) / 2)
    idx16     = int(0.16 * len(usage)) 
    idx84     = int(0.84 * len(usage)) 
    usageMedian = float(usage[idxMedian])
    usage16     = float(usage[idx16])
    usage84     = float(usage[idx84])  
    usageErr = ((usage84 - usageMedian) + (usageMedian - usage16)) / 2 
    if "Time" in fullcmd:
        print "Time ",
    else:
        print "Memory ", 
    print "usage for ", step, ":  ", usageMedian, " +- ", usageErr
    y.append(usageMedian)
    yerr.append(usageErr)  

condorDir = "AMSB_chargino500GeV_ctau100cm_" # excluding 

labels = ["step1b", "step1c", "step2"]
n = len(labels)  
y    = [] 
yerr = [] 
cmdMem = ["grep 'Peak virtual size' condor/AMSB_chargino500GeV_ctau100cm_", 
          "/condor_*.err | awk '{print $5}'"]  
# Print out will be of the form:
# MemoryReport> Peak virtual size 1228.38 Mbytes  
h = TH1F("h", "Memory usage;;Peak virtual memory (MB)", n, 0, n)
for i in range(n):
    getUsage(cmdMem, labels[i],  y, yerr) 
    h.SetBinContent(i+1, y   [i])
    h.SetBinError  (i+1, yerr[i])
    h.GetXaxis().SetBinLabel(i+1, labels[i])  
h.SetMinimum(0)
h.SetMarkerStyle(21)  
h.SetLineColor(1)  
can = TCanvas()
h.Draw("pe")
can.SaveAs("usageMem.pdf")  



labels = ["step1", "step1b", "step1c", "step2"]
n = len(labels)  
y    = [] 
yerr = [] 
cmdTime = ["grep -A 5 'Time report complete' condor/AMSB_chargino500GeV_ctau100cm_", 
           "/condor_*.err | grep 'Avg event' | awk '{print $5}'"]  
# Print outs will be of the form:
# TimeReport> Time report complete in 1476.87 seconds
#  Time Summary: 
#  - Min event:   6.90868
#  - Max event:   44.1434
#  - Avg event:   14.7687
#  - Total job:   1476.87
h = TH1F("h", "Processing time;;Average processing time per event (seconds)", n, 0, n)
for i in range(n):
    getUsage(cmdTime, labels[i],  y, yerr) 
    h.SetBinContent(i+1, y   [i])
    h.SetBinError  (i+1, yerr[i])
    h.GetXaxis().SetBinLabel(i+1, labels[i])  
h.SetMinimum(0)
h.SetMarkerStyle(21)  
h.SetLineColor(1)  
can = TCanvas()
h.Draw("pe")
can.SaveAs("usageTime.pdf")  


print "done"









