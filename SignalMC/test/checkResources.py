#!/usr/bin/python
import os

#import numpy as np
#import matplotlib.pyplot as plt
from ROOT import gROOT, TGraphErrors, TCanvas, TH1F, TStyle, gStyle, TColor 

gROOT.SetBatch() # Do not open TCanvas
gStyle.SetOptStat(0)

def getMemoryUsage(step, y, yerr):
#    print "Checking memory usage..."
    #os.system('grep "Peak virtual size" condor/AMSB_chargino500GeV_ctau100cm_step2/condor_0.err >! ') 
    cmd = "grep 'Peak virtual size' condor/AMSB_chargino500GeV_ctau100cm_" + step + "/condor_*.err | awk '{print $5}'"
    #mem = os.popen(cmd).read().split("\n")[4] 
    mem = os.popen(cmd).read().split("\n")
    mem = sorted(mem)  
#    print "mem = "
    idxMedian = int(len(mem) / 2)
    idx16     = int(0.16 * len(mem)) 
    idx84     = int(0.84 * len(mem)) 
    memMedian = float(mem[idxMedian])
    mem16     = float(mem[idx16])
    mem84     = float(mem[idx84])  
    memErr = ((mem84 - memMedian) + (memMedian - mem16)) / 2 
#    print mem
    print "len(mem) = ", str(len(mem) )  
    print "cmd = ", cmd  
    print "indices: median: ", idxMedian, ", idx16=", idx16, "idx84=", idx84  
#    print "Memory usage for ", step, ":  median=", memMedian, ", 68% interval=[", mem16, " - ", mem84, "]"  
    print "Memory usage for ", step, ":  ", memMedian, " +- ", memErr
    print "float(memMedian) = ", float(memMedian) 
    y.append(memMedian)
    yerr.append(memErr)  

#getMemoryUsage("step1")
n = 3
x    = [1.0, 2.0, 3.0] 
y    = [] 
yerr = [] 
labels = ["step1b", "step1c", "step2"]
# getMemoryUsage(labels[0], y, yerr) 
# getMemoryUsage(labels[1], y, yerr) 
# getMemoryUsage(labels[2],  y, yerr) 
#x = range(1,n+1)
xerr = [1] * n

print "Debug: x = ", x
print "Debug: y = ", y 
print "Debug: xerr = ", xerr 
print "Debug: yerr = ", yerr 

#gr = TGraphErrors()
h = TH1F("h", "Memory usage;;Peak virtual memory (MB)", n, 0, n)
for i in range(n):
    # gr.SetPoint(i, i, y[i])
    # gr.SetPointError(i, 0.5, yerr[i])
    getMemoryUsage(labels[i],  y, yerr) 
    h.SetBinContent(i+1, y   [i])
    h.SetBinError  (i+1, yerr[i])
    h.GetXaxis().SetBinLabel(i+1, labels[i])  

h.SetMinimum(0)
h.SetMarkerStyle(21)  
h.SetLineColor(0)  
can = TCanvas()

#gr.Draw()
h.Draw("pe")

can.SaveAs("plot1.pdf")  

# # example data
# x = np.arange(1, 4, 1)
# #y = np.exp(-x)

# plt.errorbar(x, y, xerr, yerr)
# #plt.show()
# plt.savefig('plot1.png')

print "done"









