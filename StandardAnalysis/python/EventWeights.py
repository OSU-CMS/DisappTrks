import FWCore.ParameterSet.Config as cms
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

electronRecoPayload = "electronReco2015"
electronIDPayload = "electronID2015Tight"
muonTriggerPayload = "muonTrigger2015IsoMu20_OR_IsoTkMu20"
muonIDPayload = "muonID2015Tight"
muonIsoPayload = "muonIso2015Tight"

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# EventWeights applied: 2016"
    electronRecoPayload = "electronReco2016"
    electronIDPayload = "electronID2016Tight"
    muonTriggerPayload = "muonTrigger2016IsoMu24_OR_IsoTkMu24"
    muonIDPayload = "muonID2016Tight"
    muonIsoPayload = "muonIso2016Tight"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# EventWeights applied: 2017 (really 2016, should be updated!)"
    electronRecoPayload = "electronReco2016"
    electronIDPayload = "electronID2016Tight"
    muonTriggerPayload = "muonTrigger2016IsoMu24_OR_IsoTkMu24"
    muonIDPayload = "muonID2016Tight"
    muonIsoPayload = "muonIso2016Tight"
else:
    print "# EventWeights applied: 2015"

# weights including electron scale factors (only for selections requiring electrons)
weightsWithEleSF = copy.deepcopy(weights)
weightsWithEleSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(electronRecoPayload)
    )
)
weightsWithEleSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(electronIDPayload)
    )
)

# weights including muon scale factors (only for selections requiring muons)
weightsWithMuonSF = copy.deepcopy(weights)
weightsWithMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(muonTriggerPayload)
    )
)
weightsWithMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(muonIDPayload)
    )
)
weightsWithMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(muonIsoPayload)
    )
)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    weightsWithMuonSF.append(
        cms.PSet (
            inputCollections = cms.vstring("eventvariables"),
            inputVariable = cms.string("muonTracking2016")
        )
    )

# weights including both electron and muon scale factors (only for selections requiring both electrons and muons)
weightsWithEleMuonSF = copy.deepcopy(weightsWithMuonSF)
weightsWithEleMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(electronRecoPayload)
    )
)
weightsWithEleMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string(electronIDPayload)
    )
)

# weights including ISR scale factor fluctuations
weightsFluctuateISR = copy.deepcopy(weights)
for w in weightsFluctuateISR:
    if w.inputVariable == cms.string("isrWeight"):
        w.fluctuations = cms.vstring("isrWeightUp", "isrWeightDown")

# weights including trigger scale factor fluctuations
weightsFluctuateTrigger = cms.VPSet (
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
        inputVariable = cms.string("grandOrWeight"),
        fluctuations = cms.vstring("grandOrWeightMCUp", "grandOrWeightMCDown", "grandOrWeightDataUp", "grandOrWeightDataDown")
    ),
)

# weights including pileup weight fluctuations
weightsFluctuatePileup = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("lifetimeWeight")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor"),
        fluctuations = cms.vstring("puScalingFactorUp", "puScalingFactorDown")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("grandOrWeight")
    ),
)
