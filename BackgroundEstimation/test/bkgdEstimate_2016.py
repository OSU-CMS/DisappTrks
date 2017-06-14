#!/usr/bin/env python

import math, os, sys
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate
from DisappTrks.BackgroundEstimation.fakeEstimateTest import FakeTrackBkgdEstimate
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors

gROOT.SetBatch () # I am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

background = "all"
if len (sys.argv) > 1:
    background = sys.argv[1]
background = background.upper ()

# '' will gives you Dataset_2016.root for the whole year
#runPeriods = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
runPeriods = ['BC', 'DEFGH', '']

nEstFake = []
nEstElectron = []
nEstMuon = []
nEstTau = []

for runPeriod in runPeriods:

    if background == "FAKE" or background == "ALL":

        print "********************************************************************************"
        print "performing fake track background estimate in search region (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("fakeTrackBkgdEstimate_2016" + runPeriod + ".root", "recreate")

        fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
        fakeTrackBkgdEstimate.addTFile (fout)
        fakeTrackBkgdEstimate.addTCanvas (canvas)
        fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
        fakeTrackBkgdEstimate.addChannel  ("Basic3hits",      "DisTrkSelectionNoD0CutNHits3",  "MET_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")
        fakeTrackBkgdEstimate.addChannel  ("DisTrkInvertD0",  "DisTrkSelectionSidebandD0Cut",  "MET_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackSystematic_d0Sideband_new_v2")

        print "********************************************************************************"

        nEstFake.append( fakeTrackBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

        print "********************************************************************************"
        print "performing fake track background estimate in ZtoMuMu (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("zToMuMuEstimate_2016" + runPeriod + ".root", "recreate")

        zToMuMuEstimate = FakeTrackBkgdEstimate ()
        zToMuMuEstimate.addTFile (fout)
        zToMuMuEstimate.addTCanvas (canvas)
        zToMuMuEstimate.addLuminosityInInvPb (lumi["SingleMuon_2016" + runPeriod])
        zToMuMuEstimate.addChannel  ("Basic3hits",      "ZtoMuMuDisTrkNoD0CutNHits3",  "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        zToMuMuEstimate.addChannel  ("DisTrkInvertD0",  "ZtoMuMuDisTrkSidebandD0Cut",  "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/fakeTrackBackground_d0Sideband_new")
        zToMuMuEstimate.addChannel  ("Basic",           "BasicSelection",              "MET_2016"       +  runPeriod,  dirs['Andrew']+"2016_final_prompt/basicSelection_new")
        zToMuMuEstimate.addChannel  ("ZtoLL",           "ZtoMuMu",                     "SingleMu_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/zToMuMu_new")

        print "********************************************************************************"

        zToMuMuEstimate.printNest ()

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    if background == "ELECTRON" or background == "LEPTON" or background == "ALL":

        print "********************************************************************************"
        print "performing electron background estimate in search region (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("electronBkgdEstimate_2016" + runPeriod + ".root", "recreate")

        electronBkgdEstimate = LeptonBkgdEstimate ("electron")
        electronBkgdEstimate.addTFile (fout)
        electronBkgdEstimate.addTCanvas (canvas)
        electronBkgdEstimate.addPrescaleFactor (lumi["MET_2016" + runPeriod] / lumi["SingleElectron_2016" + runPeriod])

        # RAW/RECO missing for 1/5 events in C, 1/9 in E, and 2/4 events in F for ZtoEleDisTrk passing events
        electronTagProbeEffectiveLumi = lumi["SingleElectron_2016" + runPeriod]
        if "C" in runPeriod or runPeriod == "":
            electronTagProbeEffectiveLumi -= (1./5.) * lumi["SingleElectron_2016C"]
        if "E" in runPeriod or runPeriod == "":
            electronTagProbeEffectiveLumi -= (1./9.) * lumi["SingleElectron_2016E"]
        if "F" in runPeriod or runPeriod == "":
            electronTagProbeEffectiveLumi -= (2./4.) * lumi["SingleElectron_2016F"]
        electronBkgdEstimate.addTagProbePassScaleFactor (lumi["SingleElectron_2016" + runPeriod] / electronTagProbeEffectiveLumi)

        electronBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
        electronBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleElectron_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        electronBkgdEstimate.addPlotLabel ("SingleElectron 2016" + runPeriod)
        electronBkgdEstimate.addChannel  ("TagProbe",        "ZtoEleProbeTrkWithZCuts",  "SingleEle_2016"         +  runPeriod,  dirs['Andrew']+"2016_final_prompt/electronBackground_new")
        electronBkgdEstimate.addChannel  ("TagProbePass",    "ZtoEleDisTrk",             "SingleEle_rereco_2016"  +  runPeriod,  dirs['Andrew']+"2016_final_prompt/electronBackground_new")
        electronBkgdEstimate.addChannel  ("TagPt35",         "ElectronTagPt55",          "SingleEle_2016"         +  runPeriod,  dirs['Andrew']+"2016_final_prompt/electronBackground_new")
        electronBkgdEstimate.addChannel  ("TagPt35MetTrig",  "ElectronTagPt55MetTrig",   "SingleEle_2016"         +  runPeriod,  dirs['Andrew']+"2016_final_prompt/electronBackground_metTrig_new")

        print "********************************************************************************"

        nEstElectron.append( electronBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

    if background == "MUON" or background == "LEPTON" or background == "ALL":

        if runPeriod == "D":
            nEstMuon.append( (0.0, 0.0) )
        else:

            print "********************************************************************************"
            print "performing muon background estimate in search region (2016", runPeriod, ")"
            print "--------------------------------------------------------------------------------"

            fout = TFile.Open ("muonBkgdEstimate_2016" + runPeriod + ".root", "recreate")

            muonBkgdEstimate = LeptonBkgdEstimate ("muon")
            muonBkgdEstimate.addTFile (fout)
            muonBkgdEstimate.addTCanvas (canvas)
            muonBkgdEstimate.addPrescaleFactor (lumi["MET_2016" + runPeriod] / lumi["SingleMuon_2016" + runPeriod])

            # RAW/RECO missing for SingleMuon_2016D passing ZtoMuDisTrk events
            if "D" in runPeriod or runPeriod == "":
              muonBkgdEstimate.addTagProbePassScaleFactor (lumi["SingleMuon_2016" + runPeriod] / (lumi["SingleMuon_2016" + runPeriod] - lumi["SingleMuon_2016D"]))

            muonBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
            muonBkgdEstimate.addLuminosityLabel (str (round (lumi["SingleMuon_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
            muonBkgdEstimate.addPlotLabel ("SingleMuon 2016" + runPeriod)
            muonBkgdEstimate.addMetCut (100.0)
            muonBkgdEstimate.addChannel  ("TagProbe",        "ZtoMuProbeTrkWithZCuts",  "SingleMu_2016"  +  runPeriod,              dirs['Brian']+"2016_final/muonBackground")
            muonBkgdEstimate.addChannel  ("TagProbePass",    "ZtoMuDisTrk",             "SingleMu_2016"  +  runPeriod + "_rereco",  dirs['Brian']+"2016_final/muonBackground")
            muonBkgdEstimate.addChannel  ("TagPt35",         "MuonTagPt55",             "SingleMu_2016"  +  runPeriod,              dirs['Brian']+"2016_final/muonBackground")
            #muonBkgdEstimate.addChannel  ("TagPt35MetTrig",  "MuonTagPt55MetTrig",      "SingleMu_2016"  +  runPeriod,              dirs['Brian']+"2016_final/muonBackground")
            muonBkgdEstimate.addChannel  ("TrigEffDenom",    "MuonTagPt55",             "SingleMu_2016"  +  runPeriod,              dirs['Brian']+"2016_final/muonBackground")
            muonBkgdEstimate.addChannel  ("TrigEffNumer",    "MuonTagPt55MetTrig",      "SingleMu_2016"  +  runPeriod,              dirs['Brian']+"2016_final/muonBackground")

            print "********************************************************************************"

            nEstMuon.append( muonBkgdEstimate.printNest () )

            print "********************************************************************************"

            fout.Close ()

            print "\n\n"

    if background == "TAU" or background == "LEPTON" or background == "ALL":

        print "********************************************************************************"
        print "performing tau background estimate in search region (2016", runPeriod, ")"
        print "--------------------------------------------------------------------------------"

        fout = TFile.Open ("tauBkgdEstimate_2016" + runPeriod + ".root", "recreate")

        tauBkgdEstimate = LeptonBkgdEstimate ("tau")
        tauBkgdEstimate.addTFile (fout)
        tauBkgdEstimate.addTCanvas (canvas)
        tauBkgdEstimate.addPrescaleFactor (lumi["MET_2016" + runPeriod] / lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016" + runPeriod])

        # RAW/RECO missing for SingleMuon_2016D passing ZtoTauToMuDisTrk events
        if runPeriod == "D":
            tauBkgdEstimate.addTagProbePassScaleFactor ( 0.0 )
        elif "D" in runPeriod or runPeriod == "":
          tauBkgdEstimate.addTagProbePassScaleFactor (lumi["SingleMuon_2016" + runPeriod] / (lumi["SingleMuon_2016" + runPeriod] - lumi["SingleMuon_2016D"]))

        # RAW/RECO missing for SingleElectron_2016F passing ZtoTauToEleDisTrk events
        # Also for the 1/10 events in SingleElectron_2016H-v3 (9/10 in v2 are available but not v3!)
        if runPeriod == "F":
            tauBkgdEstimate.addTagProbePass1ScaleFactor ( 0.0 )
        else:
            tauToEleTagProbeEffectiveLumi = lumi["SingleElectron_2016" + runPeriod]
            if "F" in runPeriod or runPeriod == "":
                tauToEleTagProbeEffectiveLumi -= lumi["SingleElectron_2016F"]
            if "H" in runPeriod or runPeriod == "":
                tauToEleTagProbeEffectiveLumi -= (1./9.) * lumi["SingleElectron_2016H"]

            tauBkgdEstimate.addTagProbePass1ScaleFactor ( lumi["SingleElectron_2016" + runPeriod] / tauToEleTagProbeEffectiveLumi )

        tauBkgdEstimate.addLuminosityInInvPb (lumi["MET_2016" + runPeriod])
        tauBkgdEstimate.addLuminosityLabel (str (round (lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016" + runPeriod] / 1000.0, 2)) + " fb^{-1} (13 TeV)")
        tauBkgdEstimate.addPlotLabel ("Tau 2016" + runPeriod)
        tauBkgdEstimate.addMetCut (100.0)
        tauBkgdEstimate.addRebinFactor (4)
        tauBkgdEstimate.addChannel  ("TagProbe",        "ZtoTauToMuProbeTrkWithZCuts",   "SingleMu_2016"   +  runPeriod,              dirs['Brian']+"2016_final/muonBackground")
        tauBkgdEstimate.addChannel  ("TagProbePass",    "ZtoTauToMuDisTrk",              "SingleMu_2016"   +  runPeriod + "_rereco",  dirs['Brian']+"2016_final/muonBackground")
        tauBkgdEstimate.addChannel  ("TagProbe1",       "ZtoTauToEleProbeTrkWithZCuts",  "SingleEle_2016"  +  runPeriod,              dirs['Brian']+"2016_final/electronBackground")
        tauBkgdEstimate.addChannel  ("TagProbePass1",   "ZtoTauToEleDisTrk",             "SingleEle_2016"  +  runPeriod + "_rereco",  dirs['Brian']+"2016_final/electronBackground")
        tauBkgdEstimate.addChannel  ("TagPt35",         "TauTagPt55",                    "Tau_2016"        +  runPeriod,              dirs['Brian']+"2016_final/tauBackground")
        #tauBkgdEstimate.addChannel  ("TagPt35MetTrig",  "TauTagPt55MetTrig",             "Tau_2016"        +  runPeriod,              dirs['Brian']+"2016_final/tauBackground")
        tauBkgdEstimate.addChannel  ("TrigEffDenom",    "ElectronTagPt55",               "SingleEle_2016"  +  runPeriod,              dirs['Brian']+"2016_final/electronBackground")
        tauBkgdEstimate.addChannel  ("TrigEffNumer",    "ElectronTagPt55MetTrig",        "SingleEle_2016"  +  runPeriod,              dirs['Brian']+"2016_final/electronBackground")

        print "********************************************************************************"

        nEstTau.append ( tauBkgdEstimate.printNest () )

        print "********************************************************************************"

        fout.Close ()

        print "\n\n"

# print sums
if background == "ALL":
    for iRunPeriod in range(0,len(runPeriods)):
        print "********************************************************************************"
        nLeptons = nEstElectron[iRunPeriod][0] + nEstMuon[iRunPeriod][0] + nEstTau[iRunPeriod][0]
        nLeptonsError = math.hypot (math.hypot (nEstElectron[iRunPeriod][1], nEstMuon[iRunPeriod][1]), nEstTau[iRunPeriod][1])
        nTotal = nLeptons + nEstFake[iRunPeriod][0]
        nTotalError = math.hypot(nLeptonsError, nEstFake[iRunPeriod][1])
        print "Total background from leptons (2016", runPeriods[iRunPeriod], "): ", nLeptons, " +/- ", nLeptonsError
        print "Total background from fake tracks (2016",runPeriods[iRunPeriod], "): ", nEstFake[iRunPeriod][0], " +/- ", nEstFake[iRunPeriod][1]
        print "********************************************************************************"
        print "Total background (2016", runPeriods[iRunPeriod], "): ", nTotal, " +/- ", nTotalError
        print "********************************************************************************"
        print "\n\n"

    x = array ("d"); ex = array ("d")
    electron   =  array  ("d");  muon   =  array  ("d");  tau   =  array  ("d");  fake   =  array  ("d")
    eElectron  =  array  ("d");  eMuon  =  array  ("d");  eTau  =  array  ("d");  eFake  =  array  ("d")

    #runPeriodsToPlot = ["B", "C", "D", "E", "F", "G", "H"]
    runPeriodsToPlot = ["BC", "DEFGH"]
    i = 0.0

    for runPeriod in runPeriodsToPlot:
        x.append (i); ex.append (0.0); i += 1.0

        electron.append  (nEstElectron[runPeriods.index  (runPeriod)][0]  /  lumi["MET_2016"  +  runPeriod])
        muon.append      (nEstMuon[runPeriods.index      (runPeriod)][0]  /  lumi["MET_2016"  +  runPeriod])
        tau.append       (nEstTau[runPeriods.index       (runPeriod)][0]  /  lumi["MET_2016"  +  runPeriod])
        fake.append      (nEstFake[runPeriods.index      (runPeriod)][0]  /  lumi["MET_2016"  +  runPeriod])

        eElectron.append  (nEstElectron[runPeriods.index  (runPeriod)][1]  /  lumi["MET_2016"  +  runPeriod])
        eMuon.append      (nEstMuon[runPeriods.index      (runPeriod)][1]  /  lumi["MET_2016"  +  runPeriod])
        eTau.append       (nEstTau[runPeriods.index       (runPeriod)][1]  /  lumi["MET_2016"  +  runPeriod])
        eFake.append      (nEstFake[runPeriods.index      (runPeriod)][1]  /  lumi["MET_2016"  +  runPeriod])

    gElectron  =  TGraphErrors  (len  (x),  x,  electron,  ex,  eElectron)
    gMuon      =  TGraphErrors  (len  (x),  x,  muon,      ex,  eMuon)
    gTau       =  TGraphErrors  (len  (x),  x,  tau,       ex,  eTau)
    gFake      =  TGraphErrors  (len  (x),  x,  fake,      ex,  eFake)

    fout = TFile.Open ("backgroundCrossSections_2016.root", "recreate")
    fout.cd ()
    gElectron.Write ("electron")
    gMuon.Write ("muon")
    gTau.Write ("tau")
    gFake.Write ("fake")
    fout.Close ()
