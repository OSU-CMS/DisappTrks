import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
import copy
import os

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

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    if osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] != "data"):
        weights.append (
            cms.PSet (
                inputCollections = cms.vstring("eventvariables"),
                inputVariable = cms.string("L1ECALPrefiringWeight")
            )
        )

#####################################################################
# Lepton scale factors. N.B. these are weights you're applying,
# LeptonScaleFactors.py control which eventvariables are produced.
#####################################################################

electronRecoPayload = ""
electronIDPayload = ""
muonTriggerPayload = ""
muonIDPayload = ""
muonIsoPayload = ""

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print("# EventWeights applied: 2016")
    electronRecoPayload = "electronReco2016"
    electronIDPayload = "electronID2016Tight"
    muonTriggerPayload = "muonTrigger2016IsoMu24_OR_IsoTkMu24"
    muonIDPayload = "muonID2016Tight"
    muonIsoPayload = "muonIso2016Tight"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print("# EventWeights applied: 2017")
    # no reco payload for 2017 V1
    electronIDPayload = "electronID2017Tight"
    muonTriggerPayload = "muonTrigger2017IsoMu27"
    muonIDPayload = "muonID2017Tight"
    muonIsoPayload = "muonIso2017TightTightID"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print("# EventWeights applied: 2018")
    electronRecoPayload = "electronReco2018"
    electronIDPayload = "electronID2018Tight"
    # the average of "before HLT update" to "after", weighted by the lumi before/after the change
    muonTriggerPayload = "muonTrigger2018IsoMu24LumiWeightedAveABCD"
    muonIDPayload = "muonID2018Tight"
    muonIsoPayload = "muonIso2018TightTightID"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    print("# EventWeights applied: 2022")
    electronRecoPayload = "electronReco2022EFG"
    electronIDPayload = "electronID2022EFGTight"
    muonTriggerPayload = "muonTrigger2022EFGIsoMu24"
    muonIDPayload = "muonID2022EFGTight"
    muonIsoPayload = "muonIso2022EFGTightTightID"
else:
    print("# EventWeights applied: 2015")
    electronRecoPayload = "electronReco2015"
    electronIDPayload = "electronID2015Tight"
    muonTriggerPayload = "muonTrigger2015IsoMu20_OR_IsoTkMu20"
    muonIDPayload = "muonID2015Tight"
    muonIsoPayload = "muonIso2015Tight"

# weights including electron scale factors (only for selections requiring electrons)
weightsWithEleSF = copy.deepcopy(weights)
if electronRecoPayload != "":
    weightsWithEleSF.append(
        cms.PSet(
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronRecoPayload)
        )
    )
if electronIDPayload != "":
    weightsWithEleSF.append(
        cms.PSet(
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronIDPayload)
        )
    )

# weights including muon scale factors (only for selections requiring muons)
weightsWithMuonSF = copy.deepcopy(weights)
if muonTriggerPayload != "":
    weightsWithMuonSF.append(
        cms.PSet(
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonTriggerPayload)
        )
    )
if muonIDPayload != "":
    weightsWithMuonSF.append(
        cms.PSet(
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonIDPayload)
        )
    )
if muonIsoPayload != "":
    weightsWithMuonSF.append(
        cms.PSet(
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(muonIsoPayload)
        )
    )

# weights including both electron and muon scale factors (only for selections requiring both electrons and muons)
weightsWithEleMuonSF = copy.deepcopy(weightsWithMuonSF)
if electronRecoPayload != "":
    weightsWithEleMuonSF.append(
        cms.PSet(
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronRecoPayload)
        )
    )
if electronIDPayload != "":
    weightsWithEleMuonSF.append(
        cms.PSet(
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string(electronIDPayload)
        )
    )

#####################################################################
# Systematic fluctuations of the standard weights.
# We don't use lepton selections in the systematics, 
# so these aren't made
#####################################################################

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

# weights including L1ECALPrefiring weight fluctuations
weightsFluctuateL1ECALPrefiring = copy.deepcopy(weights)
for w in weightsFluctuateL1ECALPrefiring:
    if w.inputVariable == cms.string("L1ECALPrefiringWeight"):
        w.fluctuations = cms.vstring("L1ECALPrefiringWeightUp", "L1ECALPrefiringWeightDown")

#####################################################################
# Simple set of weights for ToyModels
#####################################################################

weightsPileupOnly = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
)
