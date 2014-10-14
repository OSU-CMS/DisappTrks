#!/usr/bin/env python

# Script to average several efficiency histograms, produced with makeEfficiencyPlots.py --noTGraph
#
# Example usage:
# getAvgEffPlots.py -i condor/condor_2014_07_26_ModelIndepFullSel/eff_histograms100cmRebin10.root -o condor/condor_2014_07_26_ModelIndepFullSel/eff_histogramsAvg.root -n stopDecayVxyZoom 

import sys
import math
import os 
from optparse import OptionParser
from ROOT import gROOT, TFile, gDirectory, TH1F, TCanvas, TPad, TIter, TPaveLabel, TGraphErrors  



parser = OptionParser()
parser.add_option("-i", "--infile", dest="infile",
                  help="input root file")
parser.add_option("--infile2", dest="infile2",
                  help="second input root file")
parser.add_option("-o", "--outfile", dest="outfile",
                  help="output root file")
parser.add_option("-n", "--canName", dest="canName",
                  help="canvas name")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                  help="verbose output")

(arguments, args) = parser.parse_args()

gROOT.SetBatch()  # Do not open TCanvas 

def getAvgHist(infile): 
    global outRootFile

    inputFile = TFile(infile, "READ")
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
                havg.SetDirectory(0)  
                havg.Reset()
                hwts.Reset()
                # Define average efficiency as weighted arithmetic mean:
                # (See http://en.wikipedia.org/wiki/Weighted_arithmetic_mean) 
                # <eff> = (1/N) * Sum_i (eff_i   / sigma_i^2)
                # <err> = sqrt(1/N)
                # weight_i = 1 / sigma_i^2
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
        havg.SetBinError  (i, math.sqrt(        1.0 / hwts.GetBinContent(i)))
        if arguments.verbose:
            print "Bin ", i, ": range: (", havg.GetBinLowEdge(i), ", ", havg.GetBinLowEdge(i+1), "): value=", havg.GetBinContent(i), ", error=", havg.GetBinError(i)  

    outRootFile.cd()  
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
        #        print "Debug:  setting max to 0.8"  
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
#    outputPdf += "/" + canNew.GetName() + ".pdf"    
    outputPdf += "/" + havg.GetName() + "_avgEff.pdf"    
    canNew.SaveAs(outputPdf)  
    canNew.Write()
    print "Saving pdf: ", outputPdf  
    inputFile.Close()

    return havg
# End getAvgHist(infile)  


def makeGraphAvg(havg, gravg):
    inputFile = TFile(arguments.infile, "READ")    
    can = inputFile.Get(arguments.canName).Clone()
    canNew = TCanvas("canNewGraph", "canNewGraph", can.GetWw(), can.GetWh())
    canNew.SetBottomMargin(can.GetBottomMargin())
    canNew.SetLeftMargin  (can.GetLeftMargin())
    newtitle = havg.GetYaxis().GetTitle() 
    newtitle = newtitle[:newtitle.rfind("(")]  # Exclude bin width from title  
    havg.GetYaxis().SetTitle(newtitle)  
    havg.SetMinimum(0)  
    havg.Draw("AXIS")
    gravg.SetMarkerStyle(21) 
    gravg.SetLineWidth(2)
    gravg.Draw("SAME P0")  
    outRootFile.cd()
    canNew.Write()
    outputPdf = arguments.outfile[:arguments.outfile.rfind("/")]
    outputPdf += "/" + havg.GetName() + "_avgEffGraph.pdf"    
    canNew.SaveAs(outputPdf)
    print "Saved pdf: ", outputPdf 
# End def makeGraphAvg(havg, gravg) 

def combineTwoAvgHists(havg, havg2):
    # Define average efficiency as weighted arithmetic mean:
    # (See http://en.wikipedia.org/wiki/Weighted_arithmetic_mean)
    # <eff> = (1/N) * Sum_i (eff_i   / sigma_i^2)
    # <err> = sqrt(1/N)
    # weight_i = 1 / sigma_i^2
    # normalization: N = Sum_i (1 / sigma_i^2)   
    # Calculate a simple average:
    # <eff> = (eff1 + eff2) / 2
    # <err> = sqrt(1/N)
    # normalization: N = Sum_i (1 / sigma_i^2)
    for i in range(1, havg.GetNbinsX()+1):
        eff1 =  havg.GetBinContent(i)
        err1 =  havg.GetBinError  (i)
        eff2 = havg2.GetBinContent(i)
        err2 = havg2.GetBinError  (i)
        N = (1.0 / pow(err1, 2)) + (1.0 / pow(err2, 2))
        effAvg = (eff1 + eff2) / 2
        errAvg = math.sqrt(1.0 / N)
        havg.SetBinContent(i, effAvg)
        havg.SetBinError  (i, errAvg)          
    return havg

outRootFile = TFile(arguments.outfile, "RECREATE")
havg = getAvgHist(arguments.infile)
if arguments.infile2:
    havg2 = getAvgHist(arguments.infile2)
    havg = combineTwoAvgHists(havg, havg2)  



######################################
## Make tables
######################################
def getAvgOfBins(havg, gravg, lo, hi, option):
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

    # Define average efficiency as weighted arithmetic mean:
    # (See http://en.wikipedia.org/wiki/Weighted_arithmetic_mean)
    # <eff> = (1/N) * Sum_i (eff_i   / sigma_i^2)
    # <err> = sqrt(1/N)
    # weight_i = 1 / sigma_i^2
    # normalization: N = Sum_i (1 / sigma_i^2)
    effSum = 0
    errSum = 0
    N = 0
    if arguments.verbose:
        print "Debug:  for lo=", lo, ", hi=", hi, ", lobin=", lobin, ", hibin=", hibin
    isZeroBin = False
    for i in range(lobin, hibin+1):
        if havg.GetBinContent(i) < 1.e-5:
            isZeroBin = True
        effSum += havg.GetBinContent(i) / math.pow(havg.GetBinError(i), 2)
        errSum += havg.GetBinError  (i) / math.pow(havg.GetBinError(i), 2)
        N      +=                   1.0 / math.pow(havg.GetBinError(i), 2)
        if arguments.verbose:
            print "Debug:  adding bin ", i
    if isZeroBin:
        effSum = 0  # Set sum to 0 if any of bins is zero (so that first bin of DisappTrk efficiency is 0)  
    effAvg = effSum / N if N else 0  
    errAvg = math.sqrt(1.0 / N) if N else 0

    if errAvg > 10:  # protect against very large errors
        errAvg = 0.0
        
    line = ""
    if option == "max":
        line += "   $>" + str(lo) + "$ & " 
    elif option == "min":
        line += "   $<" + str(hi) + "$ & " 
    else:
        line += str(lo) + "--" + str(hi) + "  & " 
    line += "{:0.1f}".format(100*effAvg) + " $\pm$ " + "{:0.1f}".format(100*errAvg) + " \\\\  \n"
    if arguments.verbose:
        print "Debug: line = ", line

    n = gravg.GetN() 
    center    = (hi + lo) / 2
    halfwidth = (hi - lo) / 2 
    gravg.SetPoint     (n,    center, effAvg)
    gravg.SetPointError(n, halfwidth, errAvg)
    if arguments.verbose: 
        print "Setting point ", n, " center = ", center, ", effAvg = ", effAvg  
    return line 
# End def getAvgOfBins(havg, lo, hi, option):





hline = "\\hline \n"
if arguments.canName == "stopDecayVxyZoom":
    header  = "% Table produced with ../scripts/getAvgEffPlots.py -i " + arguments.infile + " --infile2 " + arguments.infile2 + " -o " + arguments.outfile + " -n " + arguments.canName + " \n"
    header += "% Full list of arguments: " + str(sys.argv) + " \n"  
    outputFile = "tables/modelIndepDisTrk.tex"
    fout = open (outputFile, "w")
    
    content = header
    content += "\\begin{tabular}{lc}\n"
    content += hline
    content += hline
    content += "$L_{xy}$ [cm]    &  Disappearing track efficiency (\\%) \\\\ \n"  
    content += hline
    gravg = TGraphErrors()
    content += getAvgOfBins(havg, gravg,   0,  30, "min")
    content += getAvgOfBins(havg, gravg,  30,  40, "")
    content += getAvgOfBins(havg, gravg,  40,  50, "")
    content += getAvgOfBins(havg, gravg,  50,  70, "")
    content += getAvgOfBins(havg, gravg,  70,  80, "")
    content += getAvgOfBins(havg, gravg,  80,  90, "")
    content += getAvgOfBins(havg, gravg,  90, 110, "")
    content += getAvgOfBins(havg, gravg, 110, 150, "max")
    content += hline
    content += hline
    content += "\\end{tabular}\n"
    fout.write(content)
    fout.close()
    os.system("cat " + outputFile)
    makeGraphAvg(havg, gravg)
    print "Finished writing " + outputFile + "\n\n\n"

elif arguments.canName == "totalMcparticleStatus3SusyIdPt":
    header  = "% Table produced with ../scripts/getAvgEffPlots.py -i " + arguments.infile + " -o " + arguments.outfile + " -n " + arguments.canName + " \n"
    header += "% Full list of arguments: " + str(sys.argv) + " \n"  
    outputFile = "tables/modelIndepBasic.tex"
    fout = open (outputFile, "w")    
    content = header
    content += "\\begin{tabular}{lc}\n"
    content += hline
    content += hline
    content += "$\\pt(\\tilde{\\chi}\\tilde{\\chi})$ [GeV]    &  Basic selection efficiency (\\%) \\\\  \n"
    content += hline
    gravg = TGraphErrors()  
    content += getAvgOfBins(havg, gravg,   0, 100, "min")
    content += getAvgOfBins(havg, gravg, 100, 125, "")
    content += getAvgOfBins(havg, gravg, 125, 150, "")
    content += getAvgOfBins(havg, gravg, 150, 175, "")
    content += getAvgOfBins(havg, gravg, 175, 200, "")
    content += getAvgOfBins(havg, gravg, 200, 225, "")
    content += getAvgOfBins(havg, gravg, 225, 500, "max")
    content += hline
    content += hline
    content += "\\end{tabular}\n"
    fout.write(content)
    fout.close()
    os.system("cat " + outputFile)
    makeGraphAvg(havg, gravg)  
    print "Finished writing " + outputFile + "\n\n\n"


outRootFile.Close()



print "Finished writing average efficiency histogram " + arguments.canName + " to " + arguments.outfile 
            
            
                                
