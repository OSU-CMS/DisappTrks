#!/usr/bin/env python3

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from ROOT import gROOT, TFile, TGraphAsymmErrors

gROOT.SetBatch () # I am Groot.

if len (sys.argv) < 2:
    print("Usage: " + os.path.basename (sys.argv[0]) + " NLAYERS")
    sys.exit (1)
nLayers = sys.argv[1]
#if int (nLayers) > 5:
#    nLayers += "plus"

dirs = getUser()

runPeriods = ['AB']

stdout = sys.stdout
nullout = open ("/dev/null", "w")
sys.stdout = nullout

N = 9
A = 0.05
B = 0.5
D = (B - A) / N

try:
  os.unlink ("fakeTrackEstimateVsD0.root")
except OSError:
  pass

for runPeriod in runPeriods:

    g0 = TGraphAsymmErrors (N)

    maxFluctuationDown = 0.0
    maxFluctuationUp = 0.0

    nominal = 0.0

    for i in range (0, N):
        minD0 = A + i * D

        sys.stdout = stdout
        print("minimum |d0|: " + str (minD0) + " cm")
        print("maximum |d0|: " + str (minD0+0.05) + " cm")

        sys.stdout = nullout

        fout = TFile.Open("fakeTrackBkgdEstimate_zToMuMu_2018" + runPeriod + "_" + nLayers + "Test.root", "recreate")
        txtFile = "fakeTrackBkgdEstimate_zToMuMu_2018" + runPeriod + "_" + nLayers + 'Test.txt'
        f = open(txtFile, 'w+')
        fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
        fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2018" + runPeriod])
        fakeTrackBkgdEstimate.addMinD0 (minD0)
        fakeTrackBkgdEstimate.addMaxD0 (minD0+0.05)        
        fakeTrackBkgdEstimate.addTFile (fout)
        fakeTrackBkgdEstimate.addTxtFile(txtFile)

        #fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "ZtoMuMuDisTrkNoD0Cut3Layers",          "SingleMu_2017"  +  runPeriod,  dirs['Andrew']+"2017/fakeTrackBackground")
        #fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",  "ZtoMuMuDisTrkNoD0CutNLayers"+nLayers,  "SingleMu_2017"  +  runPeriod,  dirs['Andrew']+"2017/fakeTrackBackground_noD0")
        #fakeTrackBkgdEstimate.addChannel  ("Basic",           "BasicSelection",                       "MET_2017"       +  runPeriod,  dirs['Andrew']+"2017/basicSelection")
        #fakeTrackBkgdEstimate.addChannel  ("ZtoLL",           "ZtoMuMu",                              "SingleMu_2017"  +  runPeriod,  dirs['Andrew']+"2017/zToMuMu")
        fakeTrackBkgdEstimate.addChannel("Basic3hits",     "ZtoMuMuDisTrkNoD0CutNLayers4",       "SingleMu_2018" + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/fakeBackground")
        fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0", "ZtoMuMuDisTrkNoD0Cut" + nLayers, "SingleMu_2018" + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/fakeBackground")
        fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelection",                     "MET_2018"      + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/basicSelection_v2")
        fakeTrackBkgdEstimate.addChannel("ZtoLL",          "ZtoMuMu",                            "SingleMu_2018" + runPeriod, dirs['Mike'] + "bfrancisStore/2018/fromLPC/zToMuMu")

        nEst = fakeTrackBkgdEstimate.printNest ()[0]


        print("debugging!!!!")

        print("nest", nEst, type(nEst))

        g0.SetPoint (i, minD0, nEst.centralValue ())
        g0.SetPointError (i, D / 2.0, D / 2.0, min (nEst.maxUncertainty (), nEst.centralValue ()), nEst.maxUncertainty ())

        if i == 0:
          nominal = nEst.centralValue ()
        else:
          if nEst.centralValue () < nominal:
            maxFluctuationDown = max (maxFluctuationDown, nominal - nEst.centralValue ())
          else:
            maxFluctuationUp = max (maxFluctuationUp, nEst.centralValue () - nominal)

    sys.stdout = stdout
    print ("[2017" + runPeriod + "] systematic uncertainty: - " + str (maxFluctuationDown) + " + " + str (maxFluctuationUp) + " (- " + str ((maxFluctuationDown / nominal) * 100.0) + " + " + str ((maxFluctuationUp / nominal) * 100.0) + ")%")
    sys.stdout = nullout

    fout = TFile ("fakeTrackEstimateVsD0.root", "update")
    fout.cd ()
    g0.Write ("est_ZtoMuMu_2017" + runPeriod)
    fout.Close ()
