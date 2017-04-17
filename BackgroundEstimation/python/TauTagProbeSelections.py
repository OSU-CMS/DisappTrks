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

ZtoTauToMuDisTrk = copy.deepcopy(ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuDisTrk.name = cms.string("ZtoTauToMuDisTrk")
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkNMissOut, cutMuTrkOS)
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkEcalo, cutMuTrkOS)
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkJetDeltaPhi, cutMuTrkOS)
addSingleCut(ZtoTauToMuDisTrk.cuts, cutTrkTauHadVeto, cutMuTrkOS)

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

ZtoTauToEleDisTrk = copy.deepcopy(ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleDisTrk.name = cms.string("ZtoTauToEleDisTrk")
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkNMissOut, cutEleTrkOS)
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkEcalo, cutEleTrkOS)
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkJetDeltaPhi, cutEleTrkOS)
addSingleCut(ZtoTauToEleDisTrk.cuts, cutTrkTauHadVeto, cutEleTrkOS)

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

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
