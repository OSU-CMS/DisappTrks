import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions
from DisappTrks.BackgroundEstimation.FakeDecaySelection import *
################################################################################
## Muon Gun skim
################################################################################

isoTrkCutsLoose = [
    cutTrkEta,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkTOBCrack,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
    cutTrkFiducialECAL,
    cutTrkNValidPixelHits3,
    cutTrkNValidHits,
    cutTrkNMissIn,
    cutTrkNMissMid,
    cutTrkIso,
    cutTrkD0Loose,
    cutTrkDZLoose,
    cutTrkJetDeltaPhi,
]


MuonGunSkim = cms.PSet(
    name = cms.string("MuonGunSkim"),
    triggers = cms.vstring(),
    metFilters = metFilters,
    cuts = cms.VPSet (),
)

# See SMP-12-023 for example of W->mu nu selection
GunMuonCuts = [
    cutDummyMet,
    cutTrkDummy,
    cutTrkMatchChargino,
    cutTrkPt30,
    cutTrkElecVeto,
    cutTrkTauHadVeto,
    cutTrkEcalo,
    cutTrkArbitration,
    cutTrkNValidHits,
#    cutMuonPt, # this will be >22 for 76X and >26 for 80X
]
GunMuonCuts += isoTrkCutsLoose
addCuts(MuonGunSkim.cuts, GunMuonCuts)

MuonGunSkim_Pt45to55 = copy.deepcopy(MuonGunSkim)
cutsToAdd = [
    cutGenTrkPt45to55,
]
addCuts(MuonGunSkim_Pt45to55.cuts, cutsToAdd)
