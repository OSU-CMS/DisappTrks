import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions
from DisappTrks.BackgroundEstimation.ElectronTagProbeSelections import *  # Get the composite cut definitions
from DisappTrks.BackgroundEstimation.MuonTagProbeSelections import *  # Get the composite cut definitions

################################################################################
## Tau tag skim
################################################################################
TauTagSkim = cms.PSet(
    name = cms.string("TauTagSkim"),
    triggers = triggersSingleTau,
    metFilters = metFilters,
    cuts = cms.VPSet (),
)
# See SMP-12-023 for example of W->mu nu selection
tagTauCuts = [
    cutMetFilters,
    cutTauPt50,
    cutTauEta21,
    cutTauTightID,
    cutTauTightPFIso,
]
addCuts(TauTagSkim.cuts, tagTauCuts)

##################################################
## Cannot go lower than 50 GeV because of trigger
##################################################
TauTagPt50 = copy.deepcopy(TauTagSkim)
TauTagPt50.name = cms.string("TauTagPt50")
cutsToAdd = [
    cutTauArbitration,
]
cutsToAdd += jetCuts
cutsToAdd += [
    cutTrkPt50,
    cutTrkTauDR0p1,
    cutTrkMatchRecoTau,
]
cutsToAdd += isoTrkCuts
addCuts(TauTagPt50.cuts, cutsToAdd)
removeCuts(TauTagPt50.cuts, [cutTrkJetDeltaPhi])

TauTagPt50NoTrig = copy.deepcopy(TauTagPt50)
TauTagPt50NoTrig.name = cms.string("TauTagPt50NoTrig")
TauTagPt50NoTrig.triggers = cms.vstring()

TauTagPt50MetTrig = copy.deepcopy(TauTagPt50)
TauTagPt50MetTrig.name = cms.string("TauTagPt50MetTrig")
TauTagPt50MetTrig.triggers = triggersMet

TauTagPt50MetCut = copy.deepcopy(TauTagPt50)
TauTagPt50MetCut.name = cms.string("TauTagPt50MetCut")
addCuts(TauTagPt50MetCut.cuts, [cutTauMetMinusOne])

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
TauTagPt55 = copy.deepcopy(TauTagPt50)
TauTagPt55.name = cms.string("TauTagPt55")
addSingleCut(TauTagPt55.cuts, cutTrkPt55, cutTrkPt50)
removeCuts(TauTagPt55.cuts, [cutTrkPt50])

TauTagPt55NoTrig = copy.deepcopy(TauTagPt55)
TauTagPt55NoTrig.name = cms.string("TauTagPt55NoTrig")
TauTagPt55NoTrig.triggers = cms.vstring()

TauTagPt55MetTrig = copy.deepcopy(TauTagPt55)
TauTagPt55MetTrig.name = cms.string("TauTagPt55MetTrig")
TauTagPt55MetTrig.triggers = triggersMet

TauTagPt55MetCut = copy.deepcopy(TauTagPt55)
TauTagPt55MetCut.name = cms.string("TauTagPt55MetCut")
addCuts(TauTagPt55MetCut.cuts, [cutTauMetMinusOne])

TauTagPt55NoJetCuts = copy.deepcopy(TauTagPt55)
TauTagPt55NoJetCuts.name = cms.string("TauTagPt55NoJetCuts")
cutsToRemove = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutLeadingJetMetPhi,
]
removeCuts(TauTagPt55NoJetCuts.cuts, cutsToRemove)

TauTagPt55NoJetCutsMetTrig = copy.deepcopy(TauTagPt55NoJetCuts)
TauTagPt55NoJetCutsMetTrig.name = cms.string("TauTagPt55NoJetCutsMetTrig")
TauTagPt55NoJetCutsMetTrig.triggers = triggersMet

################################################################################
## Tau tag and probe sample
################################################################################
# after invariant mass cut of 10 GeV
    #cutMuTrkDeltaPhi,
    #cutMuTrkMETBalance,
# after muon arbitration
    #cutLowMet,
    #cutNJetsLE2,

ZtoTauToMuProbeTrkWithZCuts = copy.deepcopy(MuonTagSkim)
ZtoTauToMuProbeTrkWithZCuts.name = cms.string("ZtoTauToMuProbeTrkWithZCuts")
addSingleCut(ZtoTauToMuProbeTrkWithZCuts.cuts, cutMuonMatchToTrigObj, cutMuonPt)
cutsToAdd = [
    cutMuonLowMT,
    cutMuonArbitration,
    cutTrkPt30,
]
cutsToAdd += isoTrkCuts
cutsToAdd += [
    cutMuTrkInvMass10,
    cutTrkElecVeto,
    cutTrkMuonVeto,
    cutTrkArbitration,
    cutMuTrkInvMass40To75,
    cutMuTrkOS,
]
addCuts(ZtoTauToMuProbeTrkWithZCuts.cuts, cutsToAdd)
removeCuts(ZtoTauToMuProbeTrkWithZCuts.cuts, [cutTrkJetDeltaPhi])

ZtoTauToMuProbeTrk = copy.deepcopy (ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrk.name = cms.string ("ZtoTauToMuProbeTrk")
removeCuts (ZtoTauToMuProbeTrk.cuts, [cutMuonArbitration, cutMuTrkInvMass10, cutTrkArbitration, cutMuTrkInvMass40To75, cutMuTrkOS])

ZtoTauToMuProbeTrkWithoutD0Cut = copy.deepcopy (ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithoutD0Cut.name = cms.string ("ZtoTauToMuProbeTrkWithoutD0Cut")
removeCuts (ZtoTauToMuProbeTrkWithoutD0Cut.cuts, [cutTrkD0])

ZtoTauToMuDisTrk = copy.deepcopy(ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuDisTrk.name = cms.string("ZtoTauToMuDisTrk")
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkNMissOut, cutMuTrkOS)
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkEcalo, cutMuTrkOS)
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkJetDeltaPhi, cutMuTrkOS)
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkTauHadVeto, cutMuTrkOS)

ZtoTauToMuDisTrkNoNMissOutCut = copy.deepcopy(ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkNoNMissOutCut.name = cms.string("ZtoTauToMuDisTrkNoNMissOutCut")
removeCuts (ZtoTauToMuDisTrkNoNMissOutCut.cuts, [cutTrkNMissOut])

TauTagPt55NoValidHitsCut = copy.deepcopy (TauTagPt55)
TauTagPt55NoValidHitsCut.name = cms.string ("TauTagPt55NoValidHitsCut")
removeCuts (TauTagPt55NoValidHitsCut.cuts, [cutTrkNValidHits])

TauTagPt55MetTrigNoValidHitsCut = copy.deepcopy (TauTagPt55MetTrig)
TauTagPt55MetTrigNoValidHitsCut.name = cms.string ("TauTagPt55MetTrigNoValidHitsCut")
removeCuts (TauTagPt55MetTrigNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoTauToMuProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoTauToMuDisTrkNoValidHitsCut = copy.deepcopy(ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkNoValidHitsCut.name = cms.string("ZtoTauToMuDisTrkNoValidHitsCut")
removeCuts(ZtoTauToMuDisTrkNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoTauToMuProbeTrkWithZCutsBetterPurity = copy.deepcopy(ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithZCutsBetterPurity.name = cms.string("ZtoTauToMuProbeTrkWithZCutsBetterPurity")
addSingleCut(ZtoTauToMuProbeTrkWithZCutsBetterPurity.cuts, cutMuTrkMETBalance, cutMuTrkInvMass10)
addSingleCut(ZtoTauToMuProbeTrkWithZCutsBetterPurity.cuts, cutMuTrkDeltaPhi, cutMuTrkInvMass10)
addSingleCut(ZtoTauToMuProbeTrkWithZCutsBetterPurity.cuts, cutNJetsLE2, cutMuonArbitration)
addSingleCut(ZtoTauToMuProbeTrkWithZCutsBetterPurity.cuts, cutLowMet, cutMuonArbitration)

ZtoTauToMuDisTrkBetterPurity = copy.deepcopy(ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkBetterPurity.name = cms.string("ZtoTauToMuDisTrkBetterPurity")
addSingleCut(ZtoTauToMuDisTrkBetterPurity.cuts, cutMuTrkMETBalance, cutMuTrkInvMass10)
addSingleCut(ZtoTauToMuDisTrkBetterPurity.cuts, cutMuTrkDeltaPhi, cutMuTrkInvMass10)
addSingleCut(ZtoTauToMuDisTrkBetterPurity.cuts, cutNJetsLE2, cutMuonArbitration)
addSingleCut(ZtoTauToMuDisTrkBetterPurity.cuts, cutLowMet, cutMuonArbitration)

################################################################################

ZtoTauToEleProbeTrkWithZCuts = copy.deepcopy(ElectronTagSkim)
ZtoTauToEleProbeTrkWithZCuts.name = cms.string("ZtoTauToEleProbeTrkWithZCuts")
addSingleCut(ZtoTauToEleProbeTrkWithZCuts.cuts, cutElectronMatchToTrigObj, cutElectronPt)
cutsToAdd = [
    cutElectronLowMT,
    cutElectronArbitration,
    cutTrkPt30,
]
cutsToAdd += isoTrkCuts
cutsToAdd += [
    cutEleTrkInvMass10,
    cutTrkElecVeto,
    cutTrkMuonVeto,
    cutTrkArbitration,
    cutEleTrkInvMass40To75,
    cutEleTrkOS,
]
addCuts(ZtoTauToEleProbeTrkWithZCuts.cuts, cutsToAdd)
removeCuts(ZtoTauToEleProbeTrkWithZCuts.cuts, [cutTrkJetDeltaPhi])

ZtoTauToEleProbeTrk = copy.deepcopy (ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrk.name = cms.string ("ZtoTauToEleProbeTrk")
removeCuts (ZtoTauToEleProbeTrk.cuts, [cutElectronArbitration, cutEleTrkInvMass10, cutTrkArbitration, cutEleTrkInvMass40To75, cutEleTrkOS])

ZtoTauToEleProbeTrkWithoutD0Cut = copy.deepcopy (ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithoutD0Cut.name = cms.string ("ZtoTauToEleProbeTrkWithoutD0Cut")
removeCuts (ZtoTauToEleProbeTrkWithoutD0Cut.cuts, [cutTrkD0])

ZtoTauToEleDisTrk = copy.deepcopy(ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleDisTrk.name = cms.string("ZtoTauToEleDisTrk")
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkNMissOut, cutEleTrkOS)
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkEcalo, cutEleTrkOS)
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkJetDeltaPhi, cutEleTrkOS)
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkTauHadVeto, cutEleTrkOS)

ZtoTauToEleDisTrkNoNMissOutCut = copy.deepcopy(ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkNoNMissOutCut.name = cms.string("ZtoTauToEleDisTrkNoNMissOutCut")
removeCuts (ZtoTauToEleDisTrkNoNMissOutCut.cuts, [cutTrkNMissOut])

ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoTauToEleProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoTauToEleDisTrkNoValidHitsCut = copy.deepcopy(ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkNoValidHitsCut.name = cms.string("ZtoTauToEleDisTrkNoValidHitsCut")
removeCuts(ZtoTauToEleDisTrkNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoTauToEleProbeTrkWithZCutsBetterPurity = copy.deepcopy(ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithZCutsBetterPurity.name = cms.string("ZtoTauToEleProbeTrkWithZCutsBetterPurity")
addSingleCut(ZtoTauToEleProbeTrkWithZCutsBetterPurity.cuts, cutEleTrkMETBalance, cutEleTrkInvMass10)
addSingleCut(ZtoTauToEleProbeTrkWithZCutsBetterPurity.cuts, cutEleTrkDeltaPhi, cutEleTrkInvMass10)
addSingleCut(ZtoTauToEleProbeTrkWithZCutsBetterPurity.cuts, cutNJetsLE2, cutElectronArbitration)
addSingleCut(ZtoTauToEleProbeTrkWithZCutsBetterPurity.cuts, cutLowMet, cutElectronArbitration)

ZtoTauToEleDisTrkBetterPurity = copy.deepcopy(ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkBetterPurity.name = cms.string("ZtoTauToEleDisTrkBetterPurity")
addSingleCut(ZtoTauToEleDisTrkBetterPurity.cuts, cutEleTrkMETBalance, cutEleTrkInvMass10)
addSingleCut(ZtoTauToEleDisTrkBetterPurity.cuts, cutEleTrkDeltaPhi, cutEleTrkInvMass10)
addSingleCut(ZtoTauToEleDisTrkBetterPurity.cuts, cutNJetsLE2, cutElectronArbitration)
addSingleCut(ZtoTauToEleDisTrkBetterPurity.cuts, cutLowMet, cutElectronArbitration)

################################################################################
## Channels with reduced numbers of hits
################################################################################
TauTagPt55NHits3 = copy.deepcopy (TauTagPt55)
TauTagPt55NHits3.name = cms.string ("TauTagPt55NHits3")
addSingleCut (TauTagPt55NHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (TauTagPt55NHits3.cuts, [cutTrkNValidHits])

TauTagPt55NHits4 = copy.deepcopy (TauTagPt55)
TauTagPt55NHits4.name = cms.string ("TauTagPt55NHits4")
addSingleCut (TauTagPt55NHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (TauTagPt55NHits4.cuts, [cutTrkNValidHits])

TauTagPt55NHits5 = copy.deepcopy (TauTagPt55)
TauTagPt55NHits5.name = cms.string ("TauTagPt55NHits5")
addSingleCut (TauTagPt55NHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (TauTagPt55NHits5.cuts, [cutTrkNValidHits])

TauTagPt55NHits6 = copy.deepcopy (TauTagPt55)
TauTagPt55NHits6.name = cms.string ("TauTagPt55NHits6")
addSingleCut (TauTagPt55NHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (TauTagPt55NHits6.cuts, [cutTrkNValidHits])

TauTagPt55MetTrigNHits3 = copy.deepcopy (TauTagPt55MetTrig)
TauTagPt55MetTrigNHits3.name = cms.string ("TauTagPt55MetTrigNHits3")
addSingleCut (TauTagPt55MetTrigNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (TauTagPt55MetTrigNHits3.cuts, [cutTrkNValidHits])

TauTagPt55MetTrigNHits4 = copy.deepcopy (TauTagPt55MetTrig)
TauTagPt55MetTrigNHits4.name = cms.string ("TauTagPt55MetTrigNHits4")
addSingleCut (TauTagPt55MetTrigNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (TauTagPt55MetTrigNHits4.cuts, [cutTrkNValidHits])

TauTagPt55MetTrigNHits5 = copy.deepcopy (TauTagPt55MetTrig)
TauTagPt55MetTrigNHits5.name = cms.string ("TauTagPt55MetTrigNHits5")
addSingleCut (TauTagPt55MetTrigNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (TauTagPt55MetTrigNHits5.cuts, [cutTrkNValidHits])

TauTagPt55MetTrigNHits6 = copy.deepcopy (TauTagPt55MetTrig)
TauTagPt55MetTrigNHits6.name = cms.string ("TauTagPt55MetTrigNHits6")
addSingleCut (TauTagPt55MetTrigNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (TauTagPt55MetTrigNHits6.cuts, [cutTrkNValidHits])

ZtoTauToMuProbeTrkWithZCutsNHits3 = copy.deepcopy (ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithZCutsNHits3.name = cms.string ("ZtoTauToMuProbeTrkWithZCutsNHits3")
addSingleCut (ZtoTauToMuProbeTrkWithZCutsNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ZtoTauToMuProbeTrkWithZCutsNHits3.cuts, [cutTrkNValidHits])

ZtoTauToMuProbeTrkWithZCutsNHits4 = copy.deepcopy (ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithZCutsNHits4.name = cms.string ("ZtoTauToMuProbeTrkWithZCutsNHits4")
addSingleCut (ZtoTauToMuProbeTrkWithZCutsNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ZtoTauToMuProbeTrkWithZCutsNHits4.cuts, [cutTrkNValidHits])

ZtoTauToMuProbeTrkWithZCutsNHits5 = copy.deepcopy (ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithZCutsNHits5.name = cms.string ("ZtoTauToMuProbeTrkWithZCutsNHits5")
addSingleCut (ZtoTauToMuProbeTrkWithZCutsNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ZtoTauToMuProbeTrkWithZCutsNHits5.cuts, [cutTrkNValidHits])

ZtoTauToMuProbeTrkWithZCutsNHits6 = copy.deepcopy (ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuProbeTrkWithZCutsNHits6.name = cms.string ("ZtoTauToMuProbeTrkWithZCutsNHits6")
addSingleCut (ZtoTauToMuProbeTrkWithZCutsNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ZtoTauToMuProbeTrkWithZCutsNHits6.cuts, [cutTrkNValidHits])

ZtoTauToEleProbeTrkWithZCutsNHits3 = copy.deepcopy (ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithZCutsNHits3.name = cms.string ("ZtoTauToEleProbeTrkWithZCutsNHits3")
addSingleCut (ZtoTauToEleProbeTrkWithZCutsNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ZtoTauToEleProbeTrkWithZCutsNHits3.cuts, [cutTrkNValidHits])

ZtoTauToEleProbeTrkWithZCutsNHits4 = copy.deepcopy (ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithZCutsNHits4.name = cms.string ("ZtoTauToEleProbeTrkWithZCutsNHits4")
addSingleCut (ZtoTauToEleProbeTrkWithZCutsNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ZtoTauToEleProbeTrkWithZCutsNHits4.cuts, [cutTrkNValidHits])

ZtoTauToEleProbeTrkWithZCutsNHits5 = copy.deepcopy (ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithZCutsNHits5.name = cms.string ("ZtoTauToEleProbeTrkWithZCutsNHits5")
addSingleCut (ZtoTauToEleProbeTrkWithZCutsNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ZtoTauToEleProbeTrkWithZCutsNHits5.cuts, [cutTrkNValidHits])

ZtoTauToEleProbeTrkWithZCutsNHits6 = copy.deepcopy (ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleProbeTrkWithZCutsNHits6.name = cms.string ("ZtoTauToEleProbeTrkWithZCutsNHits6")
addSingleCut (ZtoTauToEleProbeTrkWithZCutsNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ZtoTauToEleProbeTrkWithZCutsNHits6.cuts, [cutTrkNValidHits])

ZtoTauToMuDisTrkNHits3 = copy.deepcopy (ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkNHits3.name = cms.string ("ZtoTauToMuDisTrkNHits3")
addSingleCut (ZtoTauToMuDisTrkNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ZtoTauToMuDisTrkNHits3.cuts, [cutTrkNValidHits])

ZtoTauToMuDisTrkNHits4 = copy.deepcopy (ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkNHits4.name = cms.string ("ZtoTauToMuDisTrkNHits4")
addSingleCut (ZtoTauToMuDisTrkNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ZtoTauToMuDisTrkNHits4.cuts, [cutTrkNValidHits])

ZtoTauToMuDisTrkNHits5 = copy.deepcopy (ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkNHits5.name = cms.string ("ZtoTauToMuDisTrkNHits5")
addSingleCut (ZtoTauToMuDisTrkNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ZtoTauToMuDisTrkNHits5.cuts, [cutTrkNValidHits])

ZtoTauToMuDisTrkNHits6 = copy.deepcopy (ZtoTauToMuDisTrk)
ZtoTauToMuDisTrkNHits6.name = cms.string ("ZtoTauToMuDisTrkNHits6")
addSingleCut (ZtoTauToMuDisTrkNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ZtoTauToMuDisTrkNHits6.cuts, [cutTrkNValidHits])

ZtoTauToEleDisTrkNHits3 = copy.deepcopy (ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkNHits3.name = cms.string ("ZtoTauToEleDisTrkNHits3")
addSingleCut (ZtoTauToEleDisTrkNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ZtoTauToEleDisTrkNHits3.cuts, [cutTrkNValidHits])

ZtoTauToEleDisTrkNHits4 = copy.deepcopy (ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkNHits4.name = cms.string ("ZtoTauToEleDisTrkNHits4")
addSingleCut (ZtoTauToEleDisTrkNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ZtoTauToEleDisTrkNHits4.cuts, [cutTrkNValidHits])

ZtoTauToEleDisTrkNHits5 = copy.deepcopy (ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkNHits5.name = cms.string ("ZtoTauToEleDisTrkNHits5")
addSingleCut (ZtoTauToEleDisTrkNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ZtoTauToEleDisTrkNHits5.cuts, [cutTrkNValidHits])

ZtoTauToEleDisTrkNHits6 = copy.deepcopy (ZtoTauToEleDisTrk)
ZtoTauToEleDisTrkNHits6.name = cms.string ("ZtoTauToEleDisTrkNHits6")
addSingleCut (ZtoTauToEleDisTrkNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ZtoTauToEleDisTrkNHits6.cuts, [cutTrkNValidHits])

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
