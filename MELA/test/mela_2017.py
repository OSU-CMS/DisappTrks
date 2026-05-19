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
	print "constructing signal PDFs in sample: AMSB_chargino_900GeV_100cm_94X -- (", nLayersWord, ")"
	print "--------------------------------------------------------------------------------"

	estimator = LikelihoodEstimator(nLayersWord)
	estimator.addSignal('AMSB_chargino_700GeV_100cm_94X', 'disTrkSelectionSmearedJets' + nLayersWord, dirs['Brian'] + '2017/signalAcceptance_full_v9', 700, 100)
	
	estimator.addData  ('observation', 'observation_v2',   'DisTrkSelection' + nLayersWord, dirs['Brian'] + '2017/signalAcceptance_hitInfo_v8')
	#estimator.addData  ('fake',        'SingleMu_2017',	'ZtoMuMuDisTrkNoD0Cut'       + nLayersWord, dirs['Brian'] + '2017/fake_dedx', useTrees = True)

	estimator.setPrintObservedTracks(True)

	estimator.constructSignalPdfs()
	estimator.constructDataPdf('observation')
	#estimator.constructDataPdf('fake')
