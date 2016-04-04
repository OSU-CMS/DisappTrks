import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions
from DisappTrks.StandardAnalysis.MuonTagProbeSelections import *  # Get the composite cut definitions

##################################################
## Tau tag and probe sample
##################################################
ZtoTauProbeTrk = copy.deepcopy(MuonTagSkim)
ZtoTauProbeTrk.name = cms.string("ZtoTauProbeTrk")
addCuts(ZtoTauProbeTrk.cuts, [cutMuonMT])
addCuts(ZtoTauProbeTrk.cuts, [cutMuonArbitration])
addCuts(ZtoTauProbeTrk.cuts, [cutTrkPt30])
addCuts(ZtoTauProbeTrk.cuts, disTrkCuts)
addCuts(ZtoTauProbeTrk.cuts, muTrkCuts)
addCuts(ZtoTauProbeTrk.cuts, [cutTrkArbitration])
cutsToRemove = [
    cutTrkPt,
    cutTrkEcalo,
    cutTrkNMissOut, 
    cutTrkJetDeltaPhi,  
    cutTrkTauHadVeto,
]
removeCuts(ZtoTauProbeTrk.cuts, cutsToRemove)

ZtoTauProbeTrkTauId = copy.deepcopy(ZtoTauProbeTrk) 
ZtoTauProbeTrkTauId.name = cms.string("ZtoTauProbeTrkTauId")
cutToAdd = cutTrkTauHadVetoInv
previousExistingCut = cutTrkMuonVeto
addSingleCut(ZtoTauProbeTrkTauId.cuts, cutToAdd, previousExistingCut)  

ZtoTauProbeTrkWithZCuts = copy.deepcopy(ZtoTauProbeTrk)
ZtoTauProbeTrkWithZCuts.name = cms.string("ZtoTauProbeTrkWithZCuts")
cutsToAdd = [
    cutMuTrkInvMass40To75, 
    cutMuTrkOS,
]
addCuts(ZtoTauProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoTauDisTrk = copy.deepcopy(ZtoTauProbeTrkWithZCuts)
ZtoTauDisTrk.name = cms.string("ZtoTauDisTrk")
cutToAdd = cutTrkTauHadVeto  
previousExistingCut = cutTrkMuonVeto
addSingleCut(ZtoTauDisTrk.cuts, cutToAdd, previousExistingCut)  


ZtoTauProbeTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoTauProbeTrk)
ZtoTauProbeTrkNoMissingOuterHitsCut.name = cms.string("ZtoTauProbeTrkNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoTauProbeTrkNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut = copy.deepcopy(ZtoTauProbeTrkWithZCuts)
ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut.name = cms.string("ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoTauProbeTrkWithZCutsNoMissingOuterHitsCut.cuts, cutsToRemove)

ZtoTauDisTrkNoMissingOuterHitsCut = copy.deepcopy(ZtoTauDisTrk)
ZtoTauDisTrkNoMissingOuterHitsCut.name = cms.string("ZtoTauDisTrkNoMissingOuterHitsCut")
cutsToRemove = [
    cutTrkNMissOut, # removed due to mismodelling in the MC
]
removeCuts(ZtoTauDisTrkNoMissingOuterHitsCut.cuts, cutsToRemove)
