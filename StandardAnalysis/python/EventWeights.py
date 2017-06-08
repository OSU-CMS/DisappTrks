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
)

is80X = os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_")

# weights including electron scale factors (only for selections requiring electrons)
weightsWithEleSF = copy.deepcopy(weights)
weightsWithEleSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronReco2015") if not is80X else cms.string("electronReco2016")
    )
)
weightsWithEleSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronID2015Tight") if not is80X else cms.string("electronID2016Tight")
    )
)

# weights including muon scale factors (only for selections requiring muons)
weightsWithMuonSF = copy.deepcopy(weights)
weightsWithMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonTrigger2015IsoMu20_OR_IsoTkMu20") if not is80X else cms.string("muonTrigger2016IsoMu24_OR_IsoTkMu24")
    )
)
weightsWithMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonID2015Tight") if not is80X else cms.string("muonID2016Tight")
    )
)
weightsWithMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonIso2015Tight") if not is80X else cms.string("muonIso2016Tight")
    )
)
if is80X:
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
        inputVariable = cms.string("electronReco2015") if not is80X else cms.string("electronReco2016")
    )
)
weightsWithEleMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronID2015Tight") if not is80X else cms.string("electronID2016Tight")
    )
)

# weights including ISR reweighting (only for signal systematic)
weightsISR = copy.deepcopy(weights)
weightsISR.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("isrWeight")
    )
)

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
