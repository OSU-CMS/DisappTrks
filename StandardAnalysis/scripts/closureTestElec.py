#!/usr/bin/env python
import os
import sys

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1, TH1D 
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

# sample = "WJetsToLNu" 
# sample = "TTJets" 
sample = "DYJetsToLL_50" 
#condor_dir = "ElecBkgdClosureTestWjets"
condor_dir = "ElecBkgdClosureTestWjets_V2"

nElectronTagPt35 = getYield(sample, condor_dir, "ElectronTagPt35CutFlowPlotter")
print "nElectronTagPt35 = ", nElectronTagPt35

nElectronTagPt35NoTrig = getYield(sample, condor_dir, "ElectronTagPt35NoTrigCutFlowPlotter")
print "nElectronTagPt35NoTrig = ", nElectronTagPt35NoTrig

effElecTrig = nElectronTagPt35[0] / nElectronTagPt35NoTrig[0] 
print "Efficiency of single electron trigger after offline selection: ", effElecTrig 

HeaderLabel = TPaveLabel(0.5, 0.5, 0.9, 0.7,"","NDC")
HeaderLabel.SetTextFont(42)
HeaderLabel.SetTextSize(0.3) 
HeaderLabel.SetBorderSize(0)
HeaderLabel.SetFillColor(0)
HeaderLabel.SetFillStyle(0)

# hist = "Electron Plots/electronMetMinusOnePt"
hist = "Met Plots/metNoMu"
hMetCtrl         = getHist(sample, condor_dir, "ElectronTagPt35Plotter",        hist)
hMetTrig         = getHist(sample, condor_dir, "ElectronTagPt35MetTrigPlotter", hist) 
hMetBack         = getHist(sample, condor_dir, "CandTrkIdElecPt35Plotter",      hist) 
hMetCandTrkNoMet = getHist(sample, condor_dir, "CandTrkIdElecPt35NoMetPlotter",      hist) 
if sample == "WJetsToLNu":
    hMetBack     = getHist("WJetsToLNu_HT", condor_dir, "CandTrkIdElecPt35Plotter",      hist) 

# hMetTrigEff = TGraphAsymmErrors(hMetTrig, hMetCtrl)
print "hMetCtrl.NbinsX() = ", hMetCtrl.GetNbinsX() 
print "hMetTrig.NbinsX() = ", hMetTrig.GetNbinsX() 
print "hMetCtrl.GetTitle() = ", hMetCtrl.GetTitle()  
hMetTrigEff = ratioHistogram(hMetTrig, hMetCtrl, False, True)
hMetTrigEff.GetYaxis().SetTitle("E_{T}^{miss} efficiency:  trigger and offline")  
hMetTrigEff.GetXaxis().SetTitle("E_{T}^{miss} excluding muons [GeV]")  
c = TCanvas("can")
setHistStyle(hMetCtrl)
hMetCtrl.Draw()
HeaderLabel.Draw()  
c.SaveAs("hMetCtrl.pdf")  
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
HeaderLabel.SetLabel("Use for P(pass E_{T}^{miss})")  
HeaderLabel.Draw()  
c.SaveAs("hMetTrigEffPlusOffline.pdf")  


hMetNoElecCtrl = getHist(sample, condor_dir, "ElectronTagPt35Plotter", "Electron Plots/electronMetNoMuMinusOnePt")  
hMetNoElecEst  = hMetNoElecCtrl.Clone()  

setHistStyle(hMetNoElecCtrl)
hMetNoElecCtrl.Draw()
HeaderLabel.SetLabel("Use for N_{ctrl}")  
HeaderLabel.Draw()  
c.SaveAs("hMetNoElecCtrl.pdf")  



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

for i in range(1, hMetNoElecEst.GetNbinsX()+1):
    x = hMetNoElecEst.GetXaxis().GetBinCenter(i)  
    metEff = hMetTrigEff.GetBinContent(hMetTrigEff.FindBin(x))  
    est = hMetNoElecCtrl.GetBinContent(i) * PPassLepVeto * metEff 
    estFracErr1 = hMetNoElecCtrl.GetBinError(i) / hMetNoElecCtrl.GetBinContent(i) if hMetNoElecCtrl.GetBinContent(i) else 0.0 
    estFracErr2 = hMetTrigEff.GetBinError(hMetTrigEff.FindBin(x)) / metEff if metEff else 0.0  
    estFracErr = math.sqrt(pow(estFracErr1, 2) + pow(estFracErr2, 2)) 
    estErr = estFracErr * est
    hMetNoElecEst.SetBinContent(i, est)
    hMetNoElecEst.SetBinError  (i, estErr)

setHistStyle(hMetNoElecEst) 
hMetNoElecEst.Draw("pe")
HeaderLabel.SetLabel("Use for N_{est}")  
HeaderLabel.Draw()  
c.SaveAs("hMetNoElecEst.pdf") 
setHistStyle(hMetBack) 
hMetBack.Draw()
HeaderLabel.SetLabel("Use for N_{back}")  
HeaderLabel.Draw()  
c.SaveAs("hMetBack.pdf") 

print "**************************************************"
print "**************************************************"
print "**************************************************"
print "Closure test for electron background estimate"
print "Condor directory: ", condor_dir
print "sample = ", sample 
estErrUnCorr  = Double(0.0)  
backError = Double(0.0)  
ctrlError = Double(0.0)  
xloBin = 0 # include underflow
xhiBin = hMetBack.GetNbinsX()  # exclude overflow
back = hMetBack.IntegralAndError(xloBin, xhiBin, backError) 

ctrl = hMetCtrl.IntegralAndError(xloBin, xhiBin, ctrlError) 
print "N_ctrl = ", ctrl, " +- ", ctrlError 

print "P(pass electron veto) = ", PPassLepVeto, " +- ", PPassLepVetoErr  
PPassLepVetoFracErr = PPassLepVetoErr / PPassLepVeto 

est = hMetNoElecEst.IntegralAndError(xloBin, xhiBin, estErrUnCorr) 
estErr = est * math.sqrt(pow(estErrUnCorr / est, 2) + pow(PPassLepVetoFracErr, 2)) 
# Uncertainty from lepton veto is correlated across all bins, 
# so add it in quadrature with the errors that are not correlated from bin to bin.  


# probability to pass Met trigger and offline criteria, after passing lepton veto
PPassMet    = est / (ctrl * PPassLepVeto) 
PPassMetErr = PPassMet * PPassLepVetoFracErr

print "P(pass Met trigger & offline after passing electron veto) = ", PPassMet, " +- ", PPassMetErr  
print "N_est = ", est, " +- ", estErr

print "N_back = ", back, " +- ", backError  


print "**************************************************"
print "**************************************************"
print "**************************************************"
print "Check lepton veto probability in tag and probe sample."  
sampleTNP = "DYJetsToLL_50"
condor_dirTNP = "electronTagProbe"
print "Condor directory: ", condor_dirTNP
print "sample = ", sampleTNP

(nProbe, nProbeErr) = getYield(sampleTNP, condor_dirTNP, "ZtoEleProbeTrkWithZCutsCutFlowPlotter")
(nPass,  nPassErr)  = getYield(sampleTNP, condor_dirTNP, "ZtoEleDisTrkCutFlowPlotter")

PPassLepVetoTNP = nPass / nProbe
PPassLepVetoTNPErr = PPassLepVetoTNP * (nPassErr / nPass)  # Error on efficiency is dominated by the error on the numerator

print "P(pass electron veto) from single lepton sample = ", PPassLepVeto, " +- ", PPassLepVetoErr  
print "P(pass electron veto) from tag and probe sample = ", PPassLepVetoTNP, " +- ", PPassLepVetoTNPErr  

print "Done."



