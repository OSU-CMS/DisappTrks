#!/usr/bin/env python

import math
from DisappTrks.BackgroundEstimation.FiducialMapCalculator import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors
import os

gROOT.SetBatch ()

dirs = getUser()
canvas = TCanvas("c1", "c1", 800, 800)

# Will use Dataset_runPeriod.root
runPeriods = ['2015']
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    runPeriods = ['2016']
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    runPeriods = ['2017B', '2017C', '2017D', '2017E', '2017F']
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    runPeriods = ['2018A', '2018B', '2018C', '2018D']

for runPeriod in runPeriods:

    condorDirectory = dirs['Brian'] + "2015/eleHotSpots"
    datasetName = "SingleEle"
    if '2016' in runPeriod:
        condorDirectory = dirs['Brian'] + "2016_final/eleHotSpots"
    if '2017' in runPeriod:
        condorDirectory = dirs['Brian'] + "2017/fromLPC/eleHotSpots"
    if '2018' in runPeriod:
        condorDirectory = dirs['Kai'] + "2018/elecHotSpots"
        datasetName = "EGamma"
        
    if not '2018' in runPeriod or runPeriod == '2018B':

        print "********************************************************************************"
        print "Calculating electron fiducial map in search region", runPeriod
        print "--------------------------------------------------------------------------------"
    
        fout = TFile.Open("newElectronFiducialMap_" + runPeriod + ".root", "recreate")
    
        electronMap = FiducialMapCalculator()
        #electronMap.setVerboseComparison(True)
        electronMap.addTFile(fout)
        electronMap.addTCanvas(canvas)
        electronMap.addLuminosityInInvPb(lumi[datasetName + "_" + runPeriod])
        electronMap.addChannel("Denominator", "ElectronFiducialCalcBefore", datasetName + "_" + runPeriod, condorDirectory)
        electronMap.addChannel("Numerator",   "ElectronFiducialCalcAfter",  datasetName + "_" + runPeriod, condorDirectory)
        electronMap.CalculateFiducialMap()
        electronMap.MakePlots()

        print "********************************************************************************"
        print "Compared to the existing map:"
        print "********************************************************************************"
        electronMap.CompareFiducialMap()
        print "********************************************************************************"
        print "\n\n"
        
        fout.Close()

    condorDirectory = dirs['Brian'] + "2015/muonHotSpots"
    if '2016' in runPeriod:
        condorDirectory = dirs['Brian'] + "2016_final/muonHotSpots"
    if '2017' in runPeriod:
        condorDirectory = dirs['Brian'] + "2017/muonHotSpots"
    if '2018' in runPeriod:
        condorDirectory = dirs['Brian'] + "2018/muonHotSpots"

    if not '2018' in runPeriod or runPeriod == '2018B' or runPeriod == '2018C':       

        print "********************************************************************************"
        print "Calculating muon fiducial map in search region", runPeriod
        print "--------------------------------------------------------------------------------"
    
        fout = TFile.Open("newMuonFiducialMap_" + runPeriod + ".root", "recreate")
    
        muonMap = FiducialMapCalculator()
        #muonMap.setVerboseComparison(True)
        muonMap.addTFile(fout)
        muonMap.addTCanvas(canvas)
        muonMap.addLuminosityInInvPb(lumi["SingleMuon_" + runPeriod])
        muonMap.addChannel("Denominator", "MuonFiducialCalcBefore", "SingleMu_" + runPeriod, condorDirectory)
        muonMap.addChannel("Numerator",   "MuonFiducialCalcAfter",  "SingleMu_" + runPeriod, condorDirectory)
        muonMap.CalculateFiducialMap()
        muonMap.MakePlots()
    
        print "********************************************************************************"
        print "Compared to the existing map:"
        print "********************************************************************************"
        muonMap.CompareFiducialMap()
        print "********************************************************************************"
        print "\n\n"
    
        fout.Close()
