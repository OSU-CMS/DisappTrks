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

# sample = "TTJets"
# condor_dir = dirs['Wells']+"ElecBkgdClosureTestWjets"
# elecBkgdClosureTest.addChannel  ("TagPt35",             "ElectronTagPt35",        sample, condor_dir)
# elecBkgdClosureTest.addChannel  ("TagPt35NoTrig",       "ElectronTagPt35NoTrig",  sample, condor_dir)   
# elecBkgdClosureTest.addChannel  ("TagPt35MetTrig",      "ElectronTagPt35MetTrig", sample, condor_dir)
# elecBkgdClosureTest.addChannel  ("CandTrkIdPt35",       "CandTrkIdElecPt35",      sample, condor_dir)
# elecBkgdClosureTest.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdElecPt35NoMet", sample, condor_dir)

# sample = "WJetsToLNu"
# condor_dir = dirs['Wells']+"ElecBkgdClosureTestWjets"
# elecBkgdClosureTest.addChannel  ("TagPt35",             "ElectronTagPt35",        sample, condor_dir)
# elecBkgdClosureTest.addChannel  ("TagPt35NoTrig",       "ElectronTagPt35NoTrig",  sample, condor_dir)   
# elecBkgdClosureTest.addChannel  ("TagPt35MetTrig",      "ElectronTagPt35MetTrig", sample, condor_dir)
# elecBkgdClosureTest.addChannel  ("CandTrkIdPt35",       "CandTrkIdElecPt35",      sample+"_HT", condor_dir)
# elecBkgdClosureTest.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdElecPt35NoMet", sample, condor_dir)

sample = "DYJetsToLL_50"
condor_dir = dirs['Wells']+"ElecBkgdClosureTestWjets_V2" 
elecBkgdClosureTest.addChannel  ("TagPt35",             "ElectronTagPt35",         sample, condor_dir)
elecBkgdClosureTest.addChannel  ("TagPt35NoTrig",       "ElectronTagPt35NoTrig",   sample, condor_dir)   
elecBkgdClosureTest.addChannel  ("TagPt35MetTrig",      "ElectronTagPt35MetTrig",  sample, condor_dir)
elecBkgdClosureTest.addChannel  ("CandTrkIdPt35",       "CandTrkIdElecPt35",       sample, condor_dir)
elecBkgdClosureTest.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdElecPt35NoMet",  sample, condor_dir)
elecBkgdClosureTest.addChannel  ("TagProbe",            "ZtoEleProbeTrkWithZCuts", sample, "electronTagProbe") 
elecBkgdClosureTest.addChannel  ("TagProbePass",        "ZtoEleDisTrk",            sample, "electronTagProbe") 



elecBkgdClosureTest.printSingleLeptonTriggerEff ()

print "********************************************************************************"

elecBkgdClosureTest.printNest ()

print "--------------------------------------------------------------------------------"

elecBkgdClosureTest.printNback ()

print "********************************************************************************"

elecBkgdClosureTest.printLepVetoEffTagProbe ()

print "********************************************************************************"

fout.Close ()
