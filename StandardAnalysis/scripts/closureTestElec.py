#!/usr/bin/env python
import os
import sys

#sys.path.append(os.environ['CMSSW_BASE'] + "/src/DisappTrks/StandardAnalysis/scripts/")
#from makeANTables import getYield
#import makeANTables as tables 

from ROOT import TFile, TH1, TH1D  
from histUtils import * 


sample = "WJetsToLNu" 
condor_dir = "ElecBkgdClosureTestWjets"

nElectronTagPt35 = getYield(sample, condor_dir, "ElectronTagPt35CutFlowPlotter")
print "nElectronTagPt35 = ", nElectronTagPt35

nElectronTagPt35NoTrig = getYield(sample, condor_dir, "ElectronTagPt35NoTrigCutFlowPlotter")
print "nElectronTagPt35NoTrig = ", nElectronTagPt35NoTrig

effElecTrig = nElectronTagPt35[0] / nElectronTagPt35NoTrig[0] 
print "Efficiency of single electron trigger after offline selection: ", effElecTrig 

hMetMinusOneNCtrl = getHist(sample, condor_dir, "ElectronTagPt35Plotter", "Electron Plots/electronMetMinusOnePt")  

print "hNCtrl.GetEntries() = ", hMetMinusOneNCtrl.GetEntries()  
print "hNCtrl.GetMean() = ", hMetMinusOneNCtrl.GetMean()  

print "Done."



