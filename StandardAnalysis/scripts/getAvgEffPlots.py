#!/usr/bin/env python

# Script to average several efficiency histograms, produced with makeEfficiencyPlots.py --noTGraph
#
# Example usage:
# getAvgEffPlots.py -i condor/condor_2014_07_26_ModelIndepFullSel/eff_histograms100cmRebin10.root -o condor/condor_2014_07_26_ModelIndepFullSel/eff_histogramsAvg.root -n stopDecayVxyZoom 

import sys
import math  
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-i", "--infile", dest="infile",
                                    help="input root file")
parser.add_option("-o", "--outfile", dest="outfile",
                                    help="output root file")
parser.add_option("-n", "--canName", dest="canName",
                                    help="canvas name")

(arguments, args) = parser.parse_args()

from ROOT import gROOT, TFile, gDirectory, TH1F, TCanvas, TPad, TIter, TPaveLabel  

gROOT.SetBatch()  # Do not open TCanvas 

inputFile = TFile(arguments.infile, "READ")
canOrig = inputFile.Get(arguments.canName).Clone()
can     = inputFile.Get(arguments.canName).Clone()
if not can:
    print "Could not find TCanvas " + can + " in " + inputFile

isFirstHist = True
for obj in can.GetListOfPrimitives():  
    print "Reading: ", obj.GetName()
    if obj.InheritsFrom("TH1"):
        if isFirstHist:
            isFirstHist = False
            havg = obj.Clone()
            hwts = obj.Clone()
            havg.Reset()
            hwts.Reset()
            # Define average efficiency as weighted sum:
            # <eff> = N * Sum_i (eff_i   / sigma_i^2)
            # <err> = N * Sum_i (sigma_i / sigma_i^2)            
            # normalization: N = Sum_i (1 / sigma_i^2)  
        for i in range(1,obj.GetNbinsX()+1):
            eff = obj.GetBinContent(i)
            err = obj.GetBinError(i)
            #            print "Debug:  bin ", i, ": eff=", eff, ", err=", err  
            # If error is 0, then reset to be very large value, so that it does not contribute much to the sum
            if err == 0:
                err = 9.E9
            hwts.SetBinContent(i, hwts.GetBinContent(i) + 1.0 / math.pow(err,2))
            havg.SetBinContent(i, havg.GetBinContent(i) + eff / math.pow(err,2))
            havg.SetBinError  (i, havg.GetBinError  (i) + err / math.pow(err,2))
        print "Found TH1: ", obj.GetName()
        print "yield: ", obj.GetBinContent(2), " +- ", obj.GetBinError(2)

# After looping over all hists, calculate average
for i in range(1,havg.GetNbinsX()+1):
    havg.SetBinContent(i, havg.GetBinContent(i) / hwts.GetBinContent(i))  
    havg.SetBinError  (i, havg.GetBinError  (i) / hwts.GetBinContent(i))  
    print "Bin ", i, ": range: (", havg.GetBinLowEdge(i), ", ", havg.GetBinLowEdge(i+1), "): value=", havg.GetBinContent(i), ", error=", havg.GetBinError(i)  

outputFile = TFile(arguments.outfile, "RECREATE")
canOrig.SetName(canOrig.GetName() + "_orig")  
canOrig.Write()  
can.cd()
can.Clear("D")
canNew = TCanvas("canNew", "canNew", can.GetWw(), can.GetWh())
canNew.SetBottomMargin(can.GetBottomMargin())
canNew.SetLeftMargin  (can.GetLeftMargin())
havg.SetMaximum(1.1)
if arguments.canName == "totalMcparticleStatus3SusyIdPt":
    havg.GetXaxis().SetTitle(havg.GetXaxis().GetTitle().replace("#sum", ""))  
if arguments.canName == "stopDecayVxyZoom":
    print "Debug:  setting max to 0.8"  
    havg.SetMaximum(0.8)
havg.GetYaxis().SetTitleOffset(1.4)  
havg.GetXaxis().SetTitleOffset(1.4)  
havg.GetXaxis().SetNdivisions(509) 
havg.Draw("P, E")

#LumiLabel = TPaveLabel(0.7063758,0.8321678,0.9765101,0.9318182,"CMS","NDC")
#LumiLabel = TPaveLabel(0.1641611,0.80,0.4463087,0.90,"CMS","NDC")
LumiLabel = TPaveLabel(0.1858108,0.7904412,0.5084459,0.8897059,"CMS","NDC")
LumiLabel.SetTextFont(62)
LumiLabel.SetTextAlign(12)
LumiLabel.SetBorderSize(0)
LumiLabel.SetFillColor(0)
LumiLabel.SetFillStyle(0)
LumiLabel.Draw()

#HeaderLabel = TPaveLabel(0.03187919, 0.9440559, 0.9110738, 0.9947552,"19.5 fb^{-1} (8 TeV)","NDC") # from makePlots.py
HeaderLabel = TPaveLabel(0.02702703,0.9117647,0.9070946,0.9632353,"19.5 fb^{-1} (8 TeV)","NDC") # from makePlots.py
HeaderLabel.SetTextAlign(32)
HeaderLabel.SetBorderSize(0)
HeaderLabel.SetFillColor(0)
HeaderLabel.SetFillStyle(0)
HeaderLabel.SetTextFont(42);
HeaderLabel.Draw()

outputPdf = arguments.outfile[:arguments.outfile.rfind("/")]
outputPdf += "/" + can.GetName() + ".pdf"    
canNew.SaveAs(outputPdf)  
canNew.Write()
outputFile.Close()
inputFile.Close()

print "Finished writing average efficiency histogram " + arguments.canName + " to " + arguments.outfile + " and to " + outputPdf  
            
            
                                
