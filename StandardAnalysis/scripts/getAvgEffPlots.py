#!/usr/bin/env python

# Script to average several efficiency histograms, produced with makeEfficiencyPlots.py --noTGraph
#
# Example usage:
# getAvgEffPlots.py -i condor/condor_2014_07_26_ModelIndepFullSel/eff_histograms100cmRebin10.root -o condor/condor_2014_07_26_ModelIndepFullSel/eff_histogramsAvg.root -n stopDecayVxyZoom 

import sys
import math
import os 
from optparse import OptionParser
from ROOT import gROOT, TFile, gDirectory, TH1F, TCanvas, TPad, TIter, TPaveLabel  



parser = OptionParser()
parser.add_option("-i", "--infile", dest="infile",
                                    help="input root file")
parser.add_option("-o", "--outfile", dest="outfile",
                                    help="output root file")
parser.add_option("-n", "--canName", dest="canName",
                                    help="canvas name")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                  help="verbose output")

(arguments, args) = parser.parse_args()

gROOT.SetBatch()  # Do not open TCanvas 

inputFile = TFile(arguments.infile, "READ")
canOrig = inputFile.Get(arguments.canName).Clone()
can     = inputFile.Get(arguments.canName).Clone()
if not can:
    print "Could not find TCanvas " + can + " in " + inputFile

isFirstHist = True
for obj in can.GetListOfPrimitives():  
    if arguments.verbose:
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
            if arguments.verbose:
                print "Debug:  bin ", i, ": eff=", eff, ", err=", err  
            # If error is 0, then reset to be very large value, so that it does not contribute much to the sum
            if err == 0:
                err = 9.E9
            hwts.SetBinContent(i, hwts.GetBinContent(i) + 1.0 / math.pow(err,2))
            havg.SetBinContent(i, havg.GetBinContent(i) + eff / math.pow(err,2))
            havg.SetBinError  (i, havg.GetBinError  (i) + err / math.pow(err,2))
        if arguments.verbose:
            print "Found TH1: ", obj.GetName()
            print "yield: ", obj.GetBinContent(2), " +- ", obj.GetBinError(2)

# After looping over all hists, calculate average
for i in range(1,havg.GetNbinsX()+1):
    havg.SetBinContent(i, havg.GetBinContent(i) / hwts.GetBinContent(i))  
    havg.SetBinError  (i, havg.GetBinError  (i) / hwts.GetBinContent(i))
    if arguments.verbose:
        print "Bin ", i, ": range: (", havg.GetBinLowEdge(i), ", ", havg.GetBinLowEdge(i+1), "): value=", havg.GetBinContent(i), ", error=", havg.GetBinError(i)  

outRootFile = TFile(arguments.outfile, "RECREATE")
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

######################################
## Make tables
######################################
def getAvgOfBins(havg, lo, hi, option):
    # Calculate the average of several bins, and return a string corresponding to the line that should go in the table.  

    # First get bin range
    lobin = havg.GetNbinsX()+1 
    hibin = -1
    for i in range(1, havg.GetNbinsX()+1):
        midbin = havg.GetBinCenter(i)
        if midbin > lo and i < lobin:
            lobin = i
        if midbin < hi and i > hibin:
            hibin = i

    # Loop over bin range, and average the bin values
    # Define average efficiency as weighted sum:
    # <eff> = N * Sum_i (eff_i / sigma_i^2)
    # <err> = N * Sum_i (sigma_i / sigma_i^2)
    # normalization: N = Sum_i (1 / sigma_i^2)
    effSum = 0
    N = 0
    if arguments.verbose:
        print "Debug:  for lo=", lo, ", hi=", hi, ", lobin=", lobin, ", hibin=", hibin
    isZeroBin = False
    for i in range(lobin, hibin+1):
        if havg.GetBinContent(i) < 1.e-5:
            isZeroBin = True
        effSum += havg.GetBinContent(i) / math.pow(havg.GetBinError(i), 2)
        N      +=                   1.0 / math.pow(havg.GetBinError(i), 2)
        if arguments.verbose:
            print "Debug:  adding bin ", i
    if isZeroBin:
        effSum = 0  # Set sum to 0 if any of bins is zero (so that first bin of DisappTrk efficiency is 0)  
    effAvg = effSum / N if N else 0  
    line = ""
    if option == "max":
        line += "   $>" + str(lo) + "$ & " 
    elif option == "min":
        line += "   $<" + str(hi) + "$ & " 
    else:
        line += str(lo) + "--" + str(hi) + "  & " 
    line += "{:0.0f}".format(100*effAvg) + " \\\\  \n"
    if arguments.verbose:
        print "Debug: line = ", line 
    return line 

hline = "\\hline \n"
header = "% Table produced with ../scripts/getAvgEffPlots.py -i " + arguments.infile + " -o " + arguments.outfile + " -n " + arguments.canName + " \n"  
if arguments.canName == "stopDecayVxyZoom":
    outputFile = "tables/modelIndepDisTrk.tex"
    fout = open (outputFile, "w")
    
    content = header
    content += "\\begin{tabular}{lc}\n"
    content += hline
    content += hline
    content += "$L_{xy}$ [cm]    &  disappearing track efficiency (\\%) \\\\ \n"  
    content += hline
    content += getAvgOfBins(havg,   0,  30, "min")
    content += getAvgOfBins(havg,  30,  40, "")
    content += getAvgOfBins(havg,  40,  50, "")
    content += getAvgOfBins(havg,  50,  70, "")
    content += getAvgOfBins(havg,  70,  80, "")
    content += getAvgOfBins(havg,  80,  90, "")
    content += getAvgOfBins(havg,  90, 110, "")
    content += getAvgOfBins(havg, 110, 150, "max")
    content += hline
    content += hline
    content += "\\end{tabular}\n"
    fout.write(content)
    fout.close()
    os.system("cat " + outputFile)
    print "Finished writing " + outputFile + "\n\n\n"

## $L_{xy}$ [cm]    &  Disappearing Track efficiency (\%) \\
## \hline
## % ~/workdirTemplateDisTrk]$ getAvgEffPlots.py -i condor/condor_2014_07_26_ModelIndepFullSel/eff_histograms100cmRebin10.root -o condor/condor_2014_07_26_ModelIndepFullSel/eff_histogramsAvg.root -n stopDecayVxyZoom
## $<30$   &  0  \\
## 30--40  & 25  \\
## 40--50  & 43  \\
## 50--70  & 51  \\
## 70--80  & 45  \\
## 80--90  & 25  \\
## 90--110 &  3  \\
## $>110$  &  0  \\


elif arguments.canName == "totalMcparticleStatus3SusyIdPt":
    outputFile = "tables/modelIndepBasic.tex"
    fout = open (outputFile, "w")    
    content = header
    content += "\\begin{tabular}{lc}\n"
    content += hline
    content += hline
    content += "$\\pt(\\chi\\chi)$ [GeV]    &  basic selection efficiency (\\%) \\\\  \n"
    content += hline
    content += getAvgOfBins(havg,   0, 100, "min")
    content += getAvgOfBins(havg, 100, 125, "")
    content += getAvgOfBins(havg, 125, 150, "")
    content += getAvgOfBins(havg, 150, 175, "")
    content += getAvgOfBins(havg, 175, 200, "")
    content += getAvgOfBins(havg, 200, 225, "")
    content += getAvgOfBins(havg, 225, 500, "max")
    content += hline
    content += hline
    content += "\\end{tabular}\n"
    fout.write(content)
    fout.close()
    os.system("cat " + outputFile)
    print "Finished writing " + outputFile + "\n\n\n"



outputPdf = arguments.outfile[:arguments.outfile.rfind("/")]
outputPdf += "/" + can.GetName() + ".pdf"    
canNew.SaveAs(outputPdf)  
canNew.Write()
outRootFile.Close()
inputFile.Close()



print "Finished writing average efficiency histogram " + arguments.canName + " to " + arguments.outfile + " and to " + outputPdf  
            
            
                                
