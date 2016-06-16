#!/usr/bin/env python

from DisappTrks.StandardAnalysis.closureTest import *  
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile
import os 


dirs = getUser() 

print "********************************************************************************"

fout = TFile.Open ("elecBkgdClosureTest.root", "recreate")
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

elecBkgdClosureTest = LeptonBkgdClosureTest ("electron")
elecBkgdClosureTest.addTFile (fout)
elecBkgdClosureTest.addTCanvas (canvas)
elecBkgdClosureTest.addMetCut (100.0)

sample = "TTJets"
condor_dir = dirs['Wells']+"ElecBkgdClosureTestWjets"
elecBkgdClosureTest.addChannel  ("TagPt35",             "ElectronTagPt35",           sample, condor_dir)
#elecBkgdClosureTest.addChannel  ("TagPt35NoTrig",       "MuonTagPt35NoTrig",     sample, condor_dir)   
elecBkgdClosureTest.addChannel  ("TagPt35MetTrig",      "ElectronTagPt35MetTrig",    sample, condor_dir)
#elecBkgdClosureTest.addChannel  ("TagPt35MetCut",       "MuonTagPt35MetCut",     sample, condor_dir)
elecBkgdClosureTest.addChannel  ("CandTrkIdPt35",       "CandTrkIdElecPt35",       sample, condor_dir)
elecBkgdClosureTest.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdElecPt35NoMet",  sample, condor_dir)
elecBkgdClosureTest.printSingleLeptonTriggerEff ()

print "********************************************************************************"

elecBkgdClosureTest.printNest ()

print "--------------------------------------------------------------------------------"

elecBkgdClosureTest.printNback ()

print "********************************************************************************"

fout.Close ()
