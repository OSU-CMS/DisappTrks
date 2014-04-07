#!/usr/bin/env python

# Makes a plot of two eta histograms produced by running decayAnalyzer_cfg.py

# Sample usage:
# $ makeEtaPlot.py -i histoDecayCharginoPartGun.root -o myEtaPlot.pdf  

from optparse import OptionParser


from ROOT import TFile, TH1F, TCanvas, TF1, TPaveLabel, TStyle, gROOT  
import ROOT  


parser = OptionParser()
parser.add_option("-i", "--infile", dest="infile",
                                    help="input root file")
parser.add_option("-o", "--outfile", dest="outfile",
                  help="output pdf name (optional)")
parser.add_option("--nobatch", action="store_true", dest="nobatch", default=False,
                  help="do not run in batch mode")   
(arguments, args) = parser.parse_args()

if not arguments.nobatch: 
    ROOT.gROOT.SetBatch(True)  # To prevent pop-up of canvas  


inputFile = TFile(arguments.infile, "READ")
histEtaSel   = inputFile.Get("demo/hGenEtaSel").Clone()
histEtaFound = inputFile.Get("demo/hGenEtaFoundVtx").Clone()
if not histEtaSel or not histEtaFound:
    print "Could not find required hists in " + inputFile
    
ROOT.gStyle.SetOptStat(1111111)
can = TCanvas()  
histEtaSel.Draw()
histEtaFound.SetLineColor(kRed)
histEtaFound.Draw("same")  


BgMCLegend = TLegend()
BgMCLegend.AddEntry(histEtaSel,  "#chi^{#pm} generated", "LEP")
BgMCLegend.AddEntry(histEtaFound,"#chi^{#pm} with found vertex","LEP")
BgMCLegend.SetBorderSize(0)
BgMCLegend.SetFillColor(0)
BgMCLegend.SetFillStyle(0)


outfileRoot = arguments.outfile.replace(".pdf", ".root")  
outputFile = TFile(outfileRoot, "RECREATE")



histEtaSel.Write()
histEtaFound.Write()
can.Write()

outputFile.Close() 
can.SaveAs(arguments.outfile)
print "Saved plot in " + arguments.outfile + " and " + outfileRoot  

print "Finished makeEtaPlot.py"  







