#!/usr/bin/env python3

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from ROOT import gROOT, TFile, TGraphAsymmErrors

gROOT.SetBatch () # I am Groot.

#if len (sys.argv) < 2:
#    print("Usage: " + os.path.basename (sys.argv[0]) + " NLAYERS")
#    sys.exit (1)
#nLayers = sys.argv[1]
#if int (nLayers) > 5:
#    nLayers += "plus"

dirs = getUser()

debug=True

runPeriods = ['EFG']
year = '2022'
mode = 'zToMuMu'
nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]

stdout = sys.stdout
if not debug:
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

  maxFluctuationDown = 0.0
  maxFluctuationUp = 0.0

  nominal = 0.

  fout = TFile (f"fakeTrackEstimateVsD0_{mode}_{year}{runPeriod}.root", "RECREATE")
  
  for nLayer in nLayersWords:

    print("---------------------------------------")
    print(f"Working on layer {nLayer}")
    print("---------------------------------------")

    g0 = TGraphAsymmErrors (N)
    g1 = TGraphAsymmErrors (N)

    for i in range (0, N):
      minD0 = A + i * D

      sys.stdout = stdout
      print("minimum |d0|: " + str (minD0) + " cm")
      print("maximum |d0|: " + str (minD0+0.05) + " cm")

      if not debug:
        sys.stdout = nullout

      fdummy = TFile.Open("fakeTrackBkgdEstimate_dummy.root", "recreate")
      txtFile = "fakeTrackBkgdEstimate_dummy.txt"
      f = open(txtFile, 'w+')
      fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
      fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi[f"MET_{year}{runPeriod}"])
      fakeTrackBkgdEstimate.addMinD0 (minD0)
      fakeTrackBkgdEstimate.addMaxD0 (minD0+0.05)        
      fakeTrackBkgdEstimate.addTFile (fdummy)
      fakeTrackBkgdEstimate.addTxtFile(txtFile)
      
      if mode=='zToMuMu':
        fakeTrackBkgdEstimate.addChannel("Basic3hits",     "ZtoMuMuDisTrkNoD0CutNLayers4",       f"Muon_{year}" + runPeriod, dirs['Matt'] + f"merged_data/Muon_{year}{runPeriod}")
        fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0", "ZtoMuMuDisTrkNoD0Cut" + nLayer, f"Muon_{year}" + runPeriod, dirs['Matt'] + f"merged_data/Muon_{year}{runPeriod}")
        fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelection",                     f"MET_{year}"      + runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_{year}{runPeriod}_basicSelection")
        fakeTrackBkgdEstimate.addChannel("ZtoLL",          "ZtoMuMu",                            f"Muon_{year}" + runPeriod, dirs['Mike'] + f"abyss/Muon_run3/Muon_{year}{runPeriod}_ZtoMuMu")
      
      else:
        fakeTrackBkgdEstimate.addChannel("Basic3hits",     "ZtoEEDisTrkNoD0CutNLayers4",       f"EGamma_{year}" + runPeriod, dirs['Mike']   + f"abyss/EGamma_run3/EGamma_{year}{runPeriod}_ZtoEEDisTrkNoD0CutNLayer/")
        fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0", "ZtoEEDisTrkNoD0Cut" + nLayer, f"EGamma_{year}" + runPeriod, dirs['Mike']   + f"abyss/EGamma_run3/EGamma_{year}{runPeriod}_ZtoEEDisTrkNoD0CutNLayer")
        fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelection",                   f"MET_{year}"    + runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_{year}{runPeriod}_basicSelection")
        fakeTrackBkgdEstimate.addChannel("ZtoLL",          "ZtoEE",                            f"EGamma_{year}" + runPeriod, dirs['Mike']   + f"abyss/EGamma_run3/EGamma_{year}{runPeriod}_ZtoEE")
      
      nEst, pFake = fakeTrackBkgdEstimate.printNest ()

      print("nest", nEst, type(nEst))

      if nEst.centralValue() != 0:
        g0.SetPoint (i, minD0, nEst.centralValue ())
        g1.SetPoint (i, minD0, pFake.centralValue ())
        g0.SetPointError (i, D / 2.0, D / 2.0, min (nEst.minUncertainty (), nEst.centralValue ()), nEst.maxUncertainty ())
        g1.SetPointError (i, D / 2.0, D / 2.0, min (pFake.minUncertainty (), pFake.centralValue ()), pFake.maxUncertainty ())

      if i == 0:
        nominal = nEst.centralValue ()
      else:
        if nEst.centralValue () < nominal:
          maxFluctuationDown = max (maxFluctuationDown, nominal - nEst.centralValue ())
        else:
          maxFluctuationUp = max (maxFluctuationUp, nEst.centralValue () - nominal)

    sys.stdout = stdout
    #print ("["+ year + runPeriod + "] systematic uncertainty: - " + str (maxFluctuationDown) + " + " + str (maxFluctuationUp) + " (- " + str ((maxFluctuationDown / nominal) * 100.0) + " + " + str ((maxFluctuationUp / nominal) * 100.0) + ")%")
    #if not debug:
    #  sys.stdout = nullout

    fout.cd ()
    print("writing g0")
    g0.Write (f"est_{mode}_{year}{runPeriod}_{nLayer}")
    g1.Write(f"pFake_{mode}_{year}{runPeriod}_{nLayer}")
  
  fout.Close ()
