#!/usr/bin/env python

# Fits an exponential function to a histogram in a specified file.
# Reports the fitted parameters and prints the plot.  

# Sample usage:
# $ doExpoFit.py -b 10 -i condor/condor_2014_03_02_TestCTauRewt2/AMSB_mGrav100K_150.0cm.root -n OSUAnalysis/NoCuts/stopCtau --lo 10 

from optparse import OptionParser


from ROOT import TFile, TH1F, TCanvas, TF1, TPaveLabel, TStyle, gROOT  
import ROOT  


parser = OptionParser()
parser.add_option("-i", "--infile", dest="infile",
                                    help="input root file")
parser.add_option("-n", "--histName", dest="histName",
                                    help="histogram name")
parser.add_option("-b", "--rebin", dest="rebinFactor",
                  help="Rebin the histogram")  
parser.add_option("-o", "--outfile", dest="outfile",
                  help="output pdf name (optional)")
parser.add_option("--lo", dest="lo",
                  help="Lo limit of fit range")  
parser.add_option("--hi", dest="hi",
                  help="Hi limit of fit range")  
parser.add_option("--nobatch", action="store_true", dest="nobatch", default=False,
                  help="do not run in batch mode")   
(arguments, args) = parser.parse_args()

if not arguments.nobatch: 
    ROOT.gROOT.SetBatch(True)  # To prevent pop-up of canvas  


inputFile = TFile(arguments.infile, "READ")
hist = inputFile.Get(arguments.histName).Clone()
if not hist:
    print "Could not find TH1 " + arguments.histName + " in " + inputFile
    
if arguments.rebinFactor:
    hist.Rebin(int(arguments.rebinFactor))

ROOT.gStyle.SetOptStat(1111111)
ROOT.gStyle.SetOptFit(1111)
lo = hist.GetBinLowEdge(1)  
hi = hist.GetBinLowEdge(hist.GetNbinsX()+1)
if arguments.lo:  
    lo = float(arguments.lo)  
if arguments.hi:  
    hi = float(arguments.hi)  
print "lo = " + str(lo)  
myfunc = TF1("myfunc", "expo", lo, hi)  
can = TCanvas()  
hist.Fit("myfunc", "R")   # Fit in range  
hist.Draw("pe")   
can.SetLogy(1)  

print "Fit function:  exp([0]+[1]*x) in range (" + str(lo) + "," + str(hi) + ")"  
print "Fitted parameters:  [0] = " + str(myfunc.GetParameter(0))
print "Fitted parameters:  [1] = " + str(myfunc.GetParameter(1))

ctau      =  -1.0 /  myfunc.GetParameter(1)
ctauErrHi = (-1.0 / (myfunc.GetParameter(1) + myfunc.GetParError(1))) - ctau
ctauErrLo = (-1.0 / (myfunc.GetParameter(1) - myfunc.GetParError(1))) - ctau

print "Fitted parameters:  ctau = -1./[1] = " + str(ctau) + "; ctau error =  + " + str(ctauErrHi) + " - " + str(ctauErrLo)    

histName = arguments.histName
histName = histName[histName.rfind('/')+1:]  # strip off anything before the last '/'   
outfileRoot = arguments.infile.replace(".root", "_" + histName + "Fit.root") 
outputFile = TFile(outfileRoot, "RECREATE")

FitText = "Fitted <c#tau> = " \
+ str.format('{0:.1f}', ctau) + "^{+" \
+ str.format('{0:.1f}', ctauErrHi) + "}_{" \
+ str.format('{0:.1f}', ctauErrLo) + "}"  
#, #chi^{2}/NDF = " \
#+ str.format('{0:.1f}', myfunc.GetChisquare()) + "/" + str(myfunc.GetNDF())  
FitLabel = TPaveLabel(0.2, 0.8, 0.6, 0.9, FitText,"NDC")
FitLabel.SetBorderSize(0)
FitLabel.SetFillColor(0)
FitLabel.SetFillStyle(0)
FitLabel.Draw()  

hist.Write()
can.Write()

outputFile.Close() 
outfilePdf = outfileRoot.replace(".root", ".pdf")  
can.SaveAs(outfilePdf)
print "Saved plot in " + outfilePdf + " and " + outfileRoot  

print "Finished doExpoFit.py"  







