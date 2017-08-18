import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.BackgroundEstimation.MuonTagProbeSelections import *

class MuonBasedAnalysis:
    pass
muonBasedAnalysis = MuonBasedAnalysis ()

muonBasedAnalysis.isoTrkSelection = copy.deepcopy(MuonTagSkim)
muonBasedAnalysis.isoTrkSelection.name = cms.string("IsoTrkSelection")
addCuts(muonBasedAnalysis.isoTrkSelection.cuts, [cutTrkPt55] + isoTrkCuts)

muonBasedAnalysis.candTrkSelection = copy.deepcopy(muonBasedAnalysis.isoTrkSelection)
muonBasedAnalysis.candTrkSelection.name = cms.string("CandTrkSelection")
addCuts(muonBasedAnalysis.candTrkSelection.cuts, leptonVetoes)

muonBasedAnalysis.disTrkSelection = copy.deepcopy(muonBasedAnalysis.candTrkSelection)
muonBasedAnalysis.disTrkSelection.name = cms.string("DisTrkSelection")
addCuts(muonBasedAnalysis.disTrkSelection.cuts, cutsToAdd)
