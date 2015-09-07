import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.StandardAnalysis.MyCuts_disappTrks import * # Put all the individual cuts in this file 


##########################################################################
##### Preselection #####
##########################################################################

preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = cms.vstring("HLT_MET75_IsoTrk50"), 
    cuts = cms.VPSet (
        # EVENT HAS GOOD PV
        cms.PSet (
            inputCollection = cms.vstring("primaryvertexs"),
            cutString = cms.string("isValid > 0 && ndof >= 4"),
            numberRequired = cms.string(">= 1")
        ),
        # ELECTRON ETA CUT
        cms.PSet (
            inputCollection = cms.vstring("electrons"),
            cutString = cms.string("abs(eta) < 2.5"),
            numberRequired = cms.string(">= 1")
        ),
    )
)
