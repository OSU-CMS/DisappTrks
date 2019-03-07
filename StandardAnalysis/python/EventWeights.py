import FWCore.ParameterSet.Config as cms
import copy
import os

from DisappTrks.StandardAnalysis.LeptonScaleFactors import *

# default event weights (for selections without electrons/muons required)
weights = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("lifetimeWeight")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("grandOrWeight")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("isrWeight")
    ),
)

# weights with lepton SFs when using lepton selections
weightsWithEleSF = copy.deepcopy(weights)
weightsWithMuonSF = copy.deepcopy(weights)
weightsWithEleMuonSF = copy.deepcopy(weights)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_"):
    weightsWithEleSF.extend(electronScaleFactors2015)
    weightsWithMuonSF.extend(muonScaleFactors2015)
    weightsWithEleMuonSF.extend(electronScaleFactors2015)
    weightsWithEleMuonSF.extend(muonScaleFactors2015)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    weightsWithEleSF.extend(electronScaleFactors2016)
    weightsWithMuonSF.extend(muonScaleFactors2016)
    weightsWithEleMuonSF.extend(electronScaleFactors2016)
    weightsWithEleMuonSF.extend(muonScaleFactors2016)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    weightsWithEleSF.extend(electronScaleFactors2017)
    weightsWithMuonSF.extend(muonScaleFactors2017)
    weightsWithEleMuonSF.extend(electronScaleFactors2017)
    weightsWithEleMuonSF.extend(muonScaleFactors2017)
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    weightsWithEleSF.extend(electronScaleFactors2018)
    weightsWithMuonSF.extend(muonScaleFactors2018)
    weightsWithEleMuonSF.extend(electronScaleFactors2018)
    weightsWithEleMuonSF.extend(muonScaleFactors2018)

# weights including ISR scale factor fluctuations
weightsFluctuateISR = copy.deepcopy(weights)
for w in weightsFluctuateISR:
    if w.inputVariable == cms.string("isrWeight"):
        w.fluctuations = cms.vstring("isrWeightUp", "isrWeightDown")

# weights including trigger scale factor fluctuations
weightsFluctuateTrigger = copy.deepcopy(weights)
for w in weightsFluctuateTrigger:
    if w.inputVariable == cms.string("grandOrWeight"):
        w.fluctuations = cms.vstring("grandOrWeightMCUp", "grandOrWeightMCDown", "grandOrWeightDataUp", "grandOrWeightDataDown")

# weights including pileup weight fluctuations
weightsFluctuatePileup = copy.deepcopy(weights)
for w in weightsFluctuatePileup:
    if w.inputVariable == cms.string("puScalingFactor"):
        w.fluctuations = cms.vstring("puScalingFactorUp", "puScalingFactorDown")
