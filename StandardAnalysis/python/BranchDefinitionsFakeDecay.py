import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.utilities import *
from OSUT3Analysis.Configuration.pdgIdBins import *
from OSUT3Analysis.Configuration.cutUtilities import *
##############################################
##### Set up the branches for flat trees #####
##############################################

##############################################################################################

FakeDecayBranches = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    branches = cms.VPSet (
        cms.PSet (
            name = cms.string("DeltaAngle_overall"),
            inputVariables = cms.vstring("DeltaAngle"),
        ),
        cms.PSet (
            name = cms.string("Pprime_overall"),
            inputVariables = cms.vstring("GenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("DeltaAngle_missouter"),
            inputVariables = cms.vstring("MissOuterDeltaAngle"),
        ),
        cms.PSet (
            name = cms.string("Pprime_missouter"),
            inputVariables = cms.vstring("MissOuterGenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("DeltaAngle_distrk"),
            inputVariables = cms.vstring("DisTrkDeltaAngle"),
        ),
        cms.PSet (
            name = cms.string("Pprime_distrk"),
            inputVariables = cms.vstring("DisTrkGenTrkMu"),
        ),
    )
)

