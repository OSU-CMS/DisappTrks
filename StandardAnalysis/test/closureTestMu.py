#!/usr/bin/env python

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
muonBkgdClosureTest.addChannel  ("TagPt35",             "MuonTagPt35",         "WJetsToLNu",  "withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest.addChannel  ("TagPt35NoTrig",       "MuonTagPt35NoTrig",   "WJetsToLNu",  "withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest.addChannel  ("TagPt35MetTrig",      "MuonTagPt35MetTrig",  "WJetsToLNu",  "withFiducialCuts/muonBkgdClosureTest")
#muonBkgdClosureTest.addChannel  ("TagPt35MetCut",       "MuonTagPt35MetCut",   "WJetsToLNu",  "withFiducialCuts/muonBkgdClosureTest")
muonBkgdClosureTest.addChannel  ("CandTrkIdPt35",       "CandTrkIdMuPt35",       "WJetsToLNu_HT",  "withFiducialCuts/muonBkgdClosureTest_LHS")
muonBkgdClosureTest.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdMuPt35NoMet",  "WJetsToLNu",  "withFiducialCuts/muonBkgdClosureTest_LHS")
muonBkgdClosureTest.printSingleLeptonTriggerEff ()

print "********************************************************************************"

muonBkgdClosureTest.printNest ()

print "--------------------------------------------------------------------------------"

muonBkgdClosureTest.printNback ()

print "********************************************************************************"

fout.Close ()
