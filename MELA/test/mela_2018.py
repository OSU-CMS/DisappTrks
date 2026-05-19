#!/usr/bin/env python3

import math, os, sys
from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.MELA.mela import LikelihoodEstimator
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.integrated_luminosity import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch()

dirs = getUser()
canvas = TCanvas("c1", "c1", 800, 800)
setCanvasStyle(canvas)

nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]
if len(sys.argv) > 2:
    nLayersWords = [sys.argv[2]]

variables = [
        'track_p',
        'track_matchedIsolatedTrack.dEdxPixel',
        'track_jet_trackJetDR',
        'track_met_trackMetPhi',
]

for nLayersWord in nLayersWords:

        print "********************************************************************************"
        print "constructing signal PDFs in sample: AMSB_chargino_700GeV_100cm_94X -- (", nLayersWord, ")"
        print "--------------------------------------------------------------------------------"

        estimator = LikelihoodEstimator(nLayersWord)
        estimator.addSignal('AMSB_chargino_700GeV_100cm_102X', 'disTrkSelectionSmearedJets' + nLayersWord, dirs['Kai'] + '2018/signalAcceptance_full_dEdx', 700, 100)

        estimator.addData  ('observation', 'MET_2018ABCD_obs',   'DisTrkSelection' + nLayersWord, dirs['Kai'] + '2018/miniUnblind')
        estimator.addData  ('fake',        'SingleMu_2018ABCD', 'ZtoMuMuDisTrkNoD0Cut' + nLayersWord, dirs['Kai'] + '2018/fake_dEdx')

        estimator.setPrintObservedTracks(True)

        estimator.constructSignalPdfs()
        estimator.constructDataPdf('observation')
        estimator.constructDataPdf('fake')
