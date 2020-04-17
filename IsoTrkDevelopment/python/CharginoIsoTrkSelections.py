import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

################################################################################
## Muon Gun skim
################################################################################

charginoMatchedCut = [
    cutCharginoMatched,
]

CharginoMatchedSkim = cms.PSet(
    name = cms.string("CharginoMatchedSkim"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (),
)

addCuts(CharginoMatchedSkim.cuts, charginoMatchedCut)
