#!/usr/bin/env python

import math
from DisappTrks.StandardAnalysis.closureTest import LeptonBkgdClosureTest
from ROOT import TCanvas, TFile

print "********************************************************************************"

fout = TFile.Open ("muonBkgdClosureTest.root", "recreate")
canvas = TCanvas("c1", "c1",800,800)
canvas.SetHighLightColor(2)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetBorderSize(2)
canvas.SetTickx(1)
canvas.SetTicky(1)
canvas.SetLeftMargin(0.128141)
canvas.SetRightMargin(0.0414573)
canvas.SetBottomMargin(0.0971503)
canvas.SetTopMargin(0.0712435)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)

muonBkgdClosureTest = LeptonBkgdClosureTest ("muon")
muonBkgdClosureTest.addTFile (fout)
muonBkgdClosureTest.addTCanvas (canvas)
muonBkgdClosureTest.addMetCut (100.0)
muonBkgdClosureTest.addChannel  ("TagPt35",             "MuonTagPt35",         "TTJets",  "withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest.addChannel  ("TagPt35NoTrig",       "MuonTagPt35NoTrig",   "TTJets",  "withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest.addChannel  ("TagPt35MetTrig",      "MuonTagPt35MetTrig",  "TTJets",  "withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest.addChannel  ("TagPt35MetCut",       "MuonTagPt35MetCut",   "TTJets",  "withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest.addChannel  ("CandTrkIdPt35",       "CandTrkIdMuPt35",       "TTJets",  "withFiducialCuts/muonBkgdClosureTest_LHS")
muonBkgdClosureTest.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdMuPt35NoMet",  "TTJets",  "withFiducialCuts/muonBkgdClosureTest_LHS_LHS")
muonBkgdClosureTest.printSingleLeptonTriggerEff ()

print "********************************************************************************"

(nEst, nEstError) = muonBkgdClosureTest.printNest ()

print "--------------------------------------------------------------------------------"

(nBack, nBackError) = muonBkgdClosureTest.printNback ()
print "|N_est - N_back| = " + str (abs (nEst - nBack) / math.hypot (nEstError, nBackError)) + " sigma"

print "********************************************************************************"

fout.Close ()
