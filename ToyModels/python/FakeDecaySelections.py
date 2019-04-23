import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

###########################################################
###   Cuts for FakeDecay selection
###########################################################

cutTrkDZLoose = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackDZWRTPV + " ) < 5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |dz| < 10"),
)

cutTrkD0Loose = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackD0WRTPV + " ) < 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |d0| < 2"),
)

#cutDecayIn

cutGenTrkPt45to55 = cms.PSet(
    inputCollection = cms.vstring("genParticlePlusGeant"),
    cutString = cms.string("pt > 45 && pt < 55"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with 45 GeV < p_{T} < 55 GeV"),
)
