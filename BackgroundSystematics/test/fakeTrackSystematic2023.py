#!/usr/bin/env python3

import math, os, sys
from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.BackgroundEstimation.bkgdEstimate import LeptonBkgdEstimate, FakeTrackBkgdEstimate, prettyPrintTotals, gaussian
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile, TGraphErrors, TF1
from scipy.optimize import minimize
import numpy as np

gROOT.SetBatch() # I am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)

triggerEfficiencyFlat = True
closureTest = False

background = "FAKE"
if len(sys.argv) > 1:
    background = sys.argv[1]
background = background.upper()

nLayersWords = ["NLayers4"]#, "NLayers5", "NLayers6plus"]
#nLayersWords = ['']
combineLayers = True
if len(sys.argv) > 2:
    nLayersWords = [sys.argv[2]]
    combineLayers = False

runPeriods = ['D']

nEstFake = {}
nEstElectron = {}
nEstMuon = {}
nEstTau = {}

nLeptons = {}
nTotal = {}

# ARC EXO-19-010: use one large sideband for fake estimate
#fakeSidebands = [(x * 0.05, (x + 1) * 0.05) for x in range(1, 10)]
fakeSidebands = [(0.05, 0.5)] 

applyHEMveto = False

stdout = sys.stdout
nullout = open("/dev/null", "w")

def getMinimumEstimate(pars):
    par0, par1, par2 = pars
    modFit = TF1 ("gaussian", gaussian,  -1.0, 1.0, 3)
    modFit.SetParameter(0, par0)
    modFit.SetParameter(1, par1)
    modFit.SetParameter(2, par2)

    nest, pfake = fakeTrackBkgdEstimate.printNest(setFit=modFit, verbose=False)
    nest = nest._centralValue
    return nest

def getMaximumEstimate(pars):
    return -1 * getMinimumEstimate(pars)



for runPeriod in runPeriods:

    if background == "FAKE" or background == "ALL":

        for nLayersWord in nLayersWords:

            print("********************************************************************************")
            print("performing fake track background estimate in search region(2023", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("fakeTrackSystematic_zToMuMu_2023" + runPeriod + "_" + nLayersWord + ".root", "recreate")
            txtFile = "fakeTrackSystematic_zToMuMu_2023" + runPeriod + "_" + nLayersWord + '.txt'
            f = open(txtFile, 'w+')
            f.close()
            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
            fakeTrackBkgdEstimate.addTFile (fout)
            fakeTrackBkgdEstimate.addTxtFile(txtFile)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2023" + runPeriod])
            fakeTrackBkgdEstimate.addChannel("Basic3hits",     "ZtoMuMuDisTrkNoD0CutNLayers4",       "Muon_2023" + runPeriod, dirs['Mike'] + f"abyss/Muon_run3/Muon_2023{runPeriod}_ZtoMuMuDisTrkNoD0Cut/")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0", "ZtoMuMuDisTrkNoD0Cut" + nLayersWord, "Muon_2023" + runPeriod, dirs['Mike'] + f"abyss/Muon_run3/Muon_2023{runPeriod}_ZtoMuMuDisTrkNoD0Cut/")
            fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelection",                     "MET_2023"      + runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_2023{runPeriod}_basicSelection")
            fakeTrackBkgdEstimate.addChannel("ZtoLL",          "ZtoMuMu",                            "Muon_2023" + runPeriod, dirs['Mike'] + f"abyss/Muon_run3/Muon_2023{runPeriod}_ZtoMuMu")

            print("********************************************************************************")
            print("Baseline sideband result ({:.2f}, {:.2f}) cm: ".format(fakeSidebands[0][0], fakeSidebands[0][1]))
            fakeTrackBkgdEstimate.addMinD0 (fakeSidebands[0][0])
            fakeTrackBkgdEstimate.addMaxD0 (fakeSidebands[0][1])
            fakeTrackBkgdEstimate.addRebinFactor(5)
            fit = fakeTrackBkgdEstimate.printTransferFactor(returnFit=True)
            print("fit values:")
            for i in range(fit.GetNpar()):
                print(f"Parameter {i}: {fit.GetParameter(i)} +- {fit.GetParError(i)}")
            nestNominal, pfakeNominal = fakeTrackBkgdEstimate.printNest ()
            fout.Close ()

            print("********************************************************************************")
            print("VARYING THE FIT PARAMETERS")

            par0Nominal = fit.GetParameter(0)
            par1Nominal = fit.GetParameter(1)
            par2Nominal = fit.GetParameter(2)

            bounds = [(fit.GetParameter(0)-fit.GetParError(0), fit.GetParameter(0)+fit.GetParError(0)),
                        (fit.GetParameter(1)-fit.GetParError(1), fit.GetParameter(1)+fit.GetParError(1)),
                        (fit.GetParameter(2)-fit.GetParError(2), fit.GetParameter(2)+fit.GetParError(2))
            ]

            print("Bounds", bounds)

            maxEstimate = minimize(getMaximumEstimate, [par0Nominal, par1Nominal, par2Nominal], bounds=bounds)
            minEstimate = minimize(getMinimumEstimate, [par0Nominal, par1Nominal, par2Nominal], bounds=bounds)

            print(f"Maximum Value for nEst: {-1*maxEstimate.fun} at {maxEstimate.x}")
            print(f"Minimum Value for nEst: {minEstimate.fun} at {minEstimate.x}")

            maxError = abs(nestNominal._centralValue - (-1*maxEstimate.fun)) / nestNominal._centralValue
            minError = abs(nestNominal._centralValue - (minEstimate.fun)) / nestNominal._centralValue
            print("Uncertainties", maxError, minError)
            maximumUncertainty = maxError if maxError > minError else minError

            print(f"Maximum Error on nEst (ZtoMuMu): {round(maximumUncertainty, 4)}")



            print("********************************************************************************")
            print("performing fake track background estimate with Z->ee selection in search region(2023", runPeriod, "--", nLayersWord, ")")
            print("--------------------------------------------------------------------------------")

            fout = TFile.Open("fakeTrackSystematic_zToEE_2023" + runPeriod + "_" + nLayersWord + ".root", "recreate")
            txtFile = "fakeTrackSystematic_zToEE_2023" + runPeriod + "_" + nLayersWord + '.txt'
            f = open(txtFile, 'w+')
            f.close()
            fakeTrackBkgdEstimate = FakeTrackBkgdEstimate ()
            fakeTrackBkgdEstimate.addTFile (fout)
            fakeTrackBkgdEstimate.addTxtFile(txtFile)
            fakeTrackBkgdEstimate.addLuminosityInInvPb (lumi["MET_2023" + runPeriod])

            fakeTrackBkgdEstimate.addChannel("Basic3hits",     "ZtoEEDisTrkNoD0CutNLayers4",       "EGamma_2023" + runPeriod, dirs['Mike']   + f"abyss/EGamma_run3/")
            fakeTrackBkgdEstimate.addChannel("DisTrkInvertD0", "ZtoEEDisTrkNoD0Cut" + nLayersWord, "EGamma_2023" + runPeriod, dirs['Mike']   + f"abyss/EGamma_run3/")
            if closureTest:
                fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelectionInvertJetMetPhiCut",                   "MET_2023"    + runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_2023{runPeriod}_basicSelectionInvertJetMetPhiCut/")
            else:
                fakeTrackBkgdEstimate.addChannel("Basic",          "BasicSelection",                   "MET_2023"    + runPeriod, dirs['Mike'] + f"abyss/MET_run3/MET_2023{runPeriod}_basicSelection")

            fakeTrackBkgdEstimate.addChannel("ZtoLL",          "ZtoEE",                            "EGamma_2023" + runPeriod, dirs['Mike']   + dirs['Mike']   + f"abyss/EGamma_run3/")

            print("********************************************************************************")
            print("Baseline sideband result ({:.2f}, {:.2f}) cm: ".format(fakeSidebands[0][0], fakeSidebands[0][1]))
            fakeTrackBkgdEstimate.addMinD0 (fakeSidebands[0][0])
            fakeTrackBkgdEstimate.addMaxD0 (fakeSidebands[0][1])
            fakeTrackBkgdEstimate.addRebinFactor(5)
            fit = fakeTrackBkgdEstimate.printTransferFactor(returnFit=True)
            print("fit values:")
            for i in range(fit.GetNpar()):
                print(f"Parameter {i}: {fit.GetParameter(i)} +- {fit.GetParError(i)}")
            nestNominal, pfakeNominal = fakeTrackBkgdEstimate.printNest ()
            fout.Close ()
            print("********************************************************************************")
            print("VARYING THE FIT PARAMETERS")

            par0Nominal = fit.GetParameter(0)
            par1Nominal = fit.GetParameter(1)
            par2Nominal = fit.GetParameter(2)

            bounds = [(fit.GetParameter(0)-fit.GetParError(0), fit.GetParameter(0)+fit.GetParError(0)),
                        (fit.GetParameter(1)-fit.GetParError(1), fit.GetParameter(1)+fit.GetParError(1)),
                        (fit.GetParameter(2)-fit.GetParError(2), fit.GetParameter(2)+fit.GetParError(2))
            ]

            print("Bounds", bounds)

            maxEstimate = minimize(getMaximumEstimate, [par0Nominal, par1Nominal, par2Nominal], bounds=bounds)
            minEstimate = minimize(getMinimumEstimate, [par0Nominal, par1Nominal, par2Nominal], bounds=bounds)

            print(f"Maximum Value for nEst: {-1*maxEstimate.fun} at {maxEstimate.x}")
            print(f"Minimum Value for nEst: {minEstimate.fun} at {minEstimate.x}")

            maxError = abs(nestNominal._centralValue - (-1*maxEstimate.fun)) / nestNominal._centralValue
            minError = abs(nestNominal._centralValue - (minEstimate.fun)) / nestNominal._centralValue
            print("Uncertainties", maxError, minError)
            maximumUncertainty = maxError if maxError > minError else minError

            print(f"Maximum Error on nEst (ZtoEE): {round(maximumUncertainty, 4)}")


