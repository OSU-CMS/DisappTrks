import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

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
    cutTrkNValidPixelHitsSignal,
    cutTrkNValidHitsSignal,
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
    cutTrkMatchChargino,
    cutTrkPt30,
    cutTrkElecVeto,
    cutTrkTauHadVeto,
    cutTrkEcalo,
    cutTrkArbitration,
    cutTrkNValidHitsSignal,
#    cutMuonPt, # this will be >22 for 76X and >26 for 80X
]
GunMuonCuts += isoTrkCutsLoose
addCuts(MuonGunSkim.cuts, GunMuonCuts)

MuonGunSkimPt45to55 = copy.deepcopy(MuonGunSkim)
MuonGunSkimPt45to55.name = cms.string("MuonGunSkimPt45to55")
addCuts(MuonGunSkimPt45to55.cuts, [cutGenTrkPt45to55])
