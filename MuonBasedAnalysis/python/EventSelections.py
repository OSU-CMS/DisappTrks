import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.BackgroundEstimation.EventSelections import *

isoTrkSelection = copy.deepcopy(MuonTagSkim)
isoTrkSelection.name = cms.string("IsoTrkSelection")
addCuts(isoTrkSelection.cuts, [cutTrkPt55] + isoTrkCuts)

candTrkSelection = copy.deepcopy(isoTrkSelection)
candTrkSelection.name = cms.string("CandTrkSelection")
addCuts(candTrkSelection.cuts, leptonVetoes)

disTrkSelection = copy.deepcopy(candTrkSelection)
disTrkSelection.name = cms.string("DisTrkSelection")
addCuts(disTrkSelection.cuts, cutsToAdd)
