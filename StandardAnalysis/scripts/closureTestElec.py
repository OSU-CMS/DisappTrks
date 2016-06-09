#!/usr/bin/env python
import os
import sys

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1, TH1D 
from histUtils import * 
sys.path.append(os.environ['CMSSW_BASE'] + "/src/OSUT3Analysis/Configuration/scripts/")
#from makeEfficiencyPlots import ratioHistogram 

from OSUT3Analysis.Configuration.histogramUtilities import * 
from DisappTrks.StandardAnalysis.tdrstyle import *
setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)  

def setHistStyle(h):
    h.SetLineColor(1)
    h.SetLineWidth(1)
    h.SetMarkerColor(1)
    h.SetMarkerStyle(20)
    h.SetMarkerSize(1.0)

sample = "WJetsToLNu" 
condor_dir = "ElecBkgdClosureTestWjets"

nElectronTagPt35 = getYield(sample, condor_dir, "ElectronTagPt35CutFlowPlotter")
print "nElectronTagPt35 = ", nElectronTagPt35

nElectronTagPt35NoTrig = getYield(sample, condor_dir, "ElectronTagPt35NoTrigCutFlowPlotter")
print "nElectronTagPt35NoTrig = ", nElectronTagPt35NoTrig

effElecTrig = nElectronTagPt35[0] / nElectronTagPt35NoTrig[0] 
print "Efficiency of single electron trigger after offline selection: ", effElecTrig 

# hist = "Electron Plots/electronMetMinusOnePt"
hist = "Met Plots/metNoMu"
hMetCtrl         = getHist(sample, condor_dir, "ElectronTagPt35Plotter",        hist)
hMetTrig         = getHist(sample, condor_dir, "ElectronTagPt35MetTrigPlotter", hist) 
hMetBack         = getHist(sample, condor_dir, "CandTrkIdElecPt35Plotter",      hist) 
hMetCandTrkNoMet = getHist(sample, condor_dir, "CandTrkIdElecPt35NoMetPlotter",      hist) 
# hMetTrigEff = TGraphAsymmErrors(hMetTrig, hMetCtrl)
print "hMetCtrl.NbinsX() = ", hMetCtrl.GetNbinsX() 
print "hMetTrig.NbinsX() = ", hMetTrig.GetNbinsX() 
print "hMetCtrl.GetTitle() = ", hMetCtrl.GetTitle()  
hMetTrigEff = ratioHistogram(hMetTrig, hMetCtrl, False, True)
hMetTrigEff.GetYaxis().SetTitle("E_{T}^{miss} efficiency:  trigger and offline")  
hMetTrigEff.GetXaxis().SetTitle("E_{T}^{miss} excluding muons [GeV]")  
c = TCanvas("can")
setHistStyle(hMetTrigEff)
hMetTrigEff.Draw()
c.SaveAs("hMetTrigEff.pdf")  
# for i in range(hMetTrigEff.GetNbinsX() - 15, hMetTrigEff.GetNbinsX()+1):
#     print "Bin: ", i, ": low edge = ", hMetTrigEff.GetXaxis().GetBinLowEdge(i), ", content = ", hMetTrigEff.GetBinContent(i), ", error = ", hMetTrigEff.GetBinError(i)

print "hNCtrl.GetEntries() = ", hMetCtrl.GetEntries()  
print "hNCtrl.GetMean() = ",    hMetCtrl.GetMean()  

# Now apply the Met > 100 GeV offline requirement
for i in range(1, hMetTrigEff.GetNbinsX()+1):
    if hMetTrigEff.GetXaxis().GetBinCenter(i) < 100:
        hMetTrigEff.SetBinContent(i, 0.0) 
        hMetTrigEff.SetBinError(i, 0.0) 
hMetTrigEff.Draw()
print "marker style: ", hMetTrigEff.GetMarkerStyle()
print "marker size: ", hMetTrigEff.GetMarkerSize()
print "line width: ", hMetTrigEff.GetLineWidth()
print "title size: ", hMetTrigEff.GetMarkerSize()
c.SaveAs("hMetTrigEffPlusOffline.pdf")  

hMetNoElecCtrl = getHist(sample, condor_dir, "ElectronTagPt35Plotter", "Electron Plots/electronMetMinusOnePt")  
hMetNoElecEst  = hMetNoElecCtrl.Clone()  


chan =  "ElectronTagPt35Plotter"
hist =  "Met Plots/metNoMu"  
# include under and overflow 
nCtrl     = getHistIntegral(sample, condor_dir, "ElectronTagPt35Plotter",        hist,  -1, 550)  
nPassVeto = getHistIntegral(sample, condor_dir, "CandTrkIdElecPt35NoMetPlotter", hist,  -1, 550) 
nPassVetoFracErr = nPassVeto[1] / nPassVeto[0] 
PPassLepVeto = nPassVeto[0] / nCtrl[0]  
PPassLepVetoErr = nPassVetoFracErr * PPassLepVeto

print "nCtrl = ", nCtrl
print "nPassVeto = ", nPassVeto
print "nPassVetoFracErr = ", nPassVetoFracErr
print "PPassLepVeto = ", PPassLepVeto, " +- ", PPassLepVetoErr  

for i in range(1, hMetNoElecEst.GetNbinsX()+1):
    x = hMetNoElecEst.GetXaxis().GetBinCenter(i)  
    metEff = hMetTrigEff.GetBinContent(hMetTrigEff.FindBin(x))  
    est = hMetNoElecCtrl.GetBinContent(i) * PPassLepVeto * metEff
    estFracErr1 = hMetNoElecCtrl.GetBinError(i) / hMetNoElecCtrl.GetBinContent(i)
    estFracErr2 = PPassLepVetoErr / PPassLepVeto 
    estFracErr3 = hMetTrigEff.GetBinError(hMetTrigEff.FindBin(x)) / metEff if metEff else 0.0  
    estFracErr = math.sqrt(pow(estFracErr1, 2) + pow(estFracErr2, 2) + pow(estFracErr3, 2)) 
    estErr = estFracErr * est
    hMetNoElecEst.SetBinContent(i, est)
    hMetNoElecEst.SetBinError  (i, estErr)

setHistStyle(hMetNoElecEst) 
hMetNoElecEst.Draw("pe")
c.SaveAs("hMetNoElecEst.pdf") 
setHistStyle(hMetBack) 
hMetBack.Draw()
c.SaveAs("hMetBack.pdf") 


estError  = Double(0.0)  
backError = Double(0.0)  
xloBin = 0 # include underflow
xhiBin = hMetNoElecEst.GetNbinsX()  # exclude overflow
est = hMetNoElecEst.IntegralAndError(xloBin, xhiBin, estError) 
print "Estimate:  hMetNoElecEst.Integral() = ", est, " +- ", estError 

xhiBin = hMetBack.GetNbinsX()  # exclude overflow
back = hMetBack.IntegralAndError(xloBin, xhiBin, backError) 
print "Observed:  NBack = hMetBack.Integral() = ", back, " +- ", backError  

print "Done."



