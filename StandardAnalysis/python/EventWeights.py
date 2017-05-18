import FWCore.ParameterSet.Config as cms
import copy

# N.B.: All of these event variable producers should check if an event is real data or MC, and in the case of real data just stores 1.0
#       So it should be safe to include these for data channels.

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
        inputVariable = cms.string("metLegWeight")
    ),
)

# weights including electron scale factors (only for selections requiring electrons)
weightsWithEleSF = copy.deepcopy(weights)
weightsWithEleSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("electronScalingFactor")
    )
)

# weights including muon scale factors (only for selections requiring muons)
weightsWithMuonSF = copy.deepcopy(weights)
weightsWithMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonScalingFactor")
    )
)

# weights including both electron and muon scale factors (only for selections requiring both electrons and muons)
weightsWithEleMuonSF = copy.deepcopy(weightsWithEleSF)
weightsWithEleMuonSF.append(
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("muonScalingFactor")
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
        inputVariable = cms.string("metLegWeight"),
        fluctuations = cms.vstring("metLegWeightMCUp", "metLegWeightMCDown", "metLegWeightDataUp", "metLegWeightDataDown")
    ),
)
