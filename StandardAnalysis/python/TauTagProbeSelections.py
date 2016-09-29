import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions
from DisappTrks.StandardAnalysis.ElectronTagProbeSelections import *  # Get the composite cut definitions
from DisappTrks.StandardAnalysis.MuonTagProbeSelections import *  # Get the composite cut definitions

################################################################################
## Tau tag skim
################################################################################
TauTagSkim = cms.PSet(
    name = cms.string("TauTagSkim"),
    triggers = triggersSingleTau,
    cuts = cms.VPSet (),
)
# See SMP-12-023 for example of W->mu nu selection
tagTauCuts = [
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
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutTrkPt50,
    cutTrkTauDR0p1,
    cutTrkMatchRecoTau,
    cutTrkEta,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkTOBCrack,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
    cutTrkFiducialECAL,
    cutTrkNValidHits,
    cutTrkNMissIn,
    cutTrkNMissMid,
    cutTrkIso,
    cutTrkD0,
    cutTrkDZ,
]
addCuts(TauTagPt50.cuts, cutsToAdd)

TauTagPt50NoTrig = copy.deepcopy(TauTagPt50)
TauTagPt50NoTrig.name = cms.string("TauTagPt50NoTrig")
TauTagPt50NoTrig.triggers = cms.vstring() 

TauTagPt50MetTrig = copy.deepcopy(TauTagPt50)
TauTagPt50MetTrig.name = cms.string("TauTagPt50MetTrig")
TauTagPt50MetTrig.triggers = triggersMet 

TauTagPt50MetCut = copy.deepcopy(TauTagPt50)
TauTagPt50MetCut.name = cms.string("TauTagPt50MetCut")
cutsToAdd = [ 
    cutTauMetMinusOne, 
]
addCuts(TauTagPt50MetCut.cuts, cutsToAdd)  

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
TauTagPt55 = copy.deepcopy(TauTagPt50)
TauTagPt55.name = cms.string("TauTagPt55")
addSingleCut(TauTagPt55.cuts, cutTrkPt55, cutTrkPt50)
cutsToAdd = [
    cutTrkEcalo,
    cutTrkNMissOut,
    #cutTrkNMissOutInv
]
addCuts(TauTagPt55.cuts, cutsToAdd)
cutsToRemove = [
    cutTrkPt50,
]
removeCuts(TauTagPt55.cuts, cutsToRemove)

TauTagPt55NoTrig = copy.deepcopy(TauTagPt55)
TauTagPt55NoTrig.name = cms.string("TauTagPt55NoTrig")
TauTagPt55NoTrig.triggers = cms.vstring() 

TauTagPt55MetTrig = copy.deepcopy(TauTagPt55)
TauTagPt55MetTrig.name = cms.string("TauTagPt55MetTrig")
TauTagPt55MetTrig.triggers = triggersMet 

TauTagPt55MetCut = copy.deepcopy(TauTagPt55)
TauTagPt55MetCut.name = cms.string("TauTagPt55MetCut")
cutsToAdd = [ 
    cutTauMetMinusOne, 
]
addCuts(TauTagPt55MetCut.cuts, cutsToAdd)  

################################################################################
## Tau tag and probe sample
################################################################################
ZtoTauToMuIsoTrk = copy.deepcopy(MuonTagSkim)
ZtoTauToMuIsoTrk.name = cms.string("ZtoTauToMuIsoTrk")

muTrkCuts = [
    cutMuTrkInvMass10,
    cutMuTrkDeltaPhi,
    cutMuTrkMETBalance,
]
addCuts(ZtoTauToMuIsoTrk.cuts, [cutMuonMT])
addCuts(ZtoTauToMuIsoTrk.cuts, [cutMuonArbitration])
addCuts(ZtoTauToMuIsoTrk.cuts, [cutLowMet])
addCuts(ZtoTauToMuIsoTrk.cuts, [cutNJets])
addCuts(ZtoTauToMuIsoTrk.cuts, [cutTrkPt30])
addCuts(ZtoTauToMuIsoTrk.cuts, isoTrkCuts)
addCuts(ZtoTauToMuIsoTrk.cuts, muTrkCuts)
cutsToRemove = [
    cutTrkPt55,
    cutTrkJetDeltaPhi,
]
removeCuts(ZtoTauToMuIsoTrk.cuts, cutsToRemove)

ZtoTauToMuProbeTrk = copy.deepcopy(ZtoTauToMuIsoTrk)
ZtoTauToMuProbeTrk.name = cms.string("ZtoTauToMuProbeTrk")

cutsToAdd = [
    cutTrkElecVeto,
    cutTrkMuonVeto,
]
addCuts(ZtoTauToMuProbeTrk.cuts, cutsToAdd)
addCuts(ZtoTauToMuProbeTrk.cuts, [cutTrkArbitration])

ZtoTauToMuProbeTrkWithZCuts = copy.deepcopy(ZtoTauToMuProbeTrk)
ZtoTauToMuProbeTrkWithZCuts.name = cms.string("ZtoTauToMuProbeTrkWithZCuts")
cutsToAdd = [
    cutMuTrkInvMass40To75,
    cutMuTrkOS,
]
addCuts(ZtoTauToMuProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoTauToMuDisTrk = copy.deepcopy(ZtoTauToMuProbeTrkWithZCuts)
ZtoTauToMuDisTrk.name = cms.string("ZtoTauToMuDisTrk")
cutsToAdd = [
    cutTrkTauHadVeto,
    cutTrkEcalo,
]
addCuts(ZtoTauToMuDisTrk.cuts, cutsToAdd)

################################################################################

ZtoTauToEleIsoTrk = copy.deepcopy(ElectronTagSkim)
ZtoTauToEleIsoTrk.name = cms.string("ZtoTauToEleIsoTrk")

eleTrkCuts = [
    cutEleTrkInvMass10,
    cutEleTrkDeltaPhi,
    cutEleTrkMETBalance,
]
addCuts(ZtoTauToEleIsoTrk.cuts, [cutElectronMT])
addCuts(ZtoTauToEleIsoTrk.cuts, [cutElectronArbitration])
addCuts(ZtoTauToEleIsoTrk.cuts, [cutLowMet])
addCuts(ZtoTauToEleIsoTrk.cuts, [cutNJets])
addCuts(ZtoTauToEleIsoTrk.cuts, [cutTrkPt30])
addCuts(ZtoTauToEleIsoTrk.cuts, isoTrkCuts)
addCuts(ZtoTauToEleIsoTrk.cuts, eleTrkCuts)
cutsToRemove = [
    cutTrkPt55,
    cutTrkJetDeltaPhi,
]
removeCuts(ZtoTauToEleIsoTrk.cuts, cutsToRemove)

ZtoTauToEleProbeTrk = copy.deepcopy(ZtoTauToEleIsoTrk)
ZtoTauToEleProbeTrk.name = cms.string("ZtoTauToEleProbeTrk")

cutsToAdd = [
    cutTrkElecVeto,
    cutTrkMuonVeto,
]
addCuts(ZtoTauToEleProbeTrk.cuts, cutsToAdd)
addCuts(ZtoTauToEleProbeTrk.cuts, [cutTrkArbitration])

ZtoTauToEleProbeTrkWithZCuts = copy.deepcopy(ZtoTauToEleProbeTrk)
ZtoTauToEleProbeTrkWithZCuts.name = cms.string("ZtoTauToEleProbeTrkWithZCuts")
cutsToAdd = [
    cutEleTrkInvMass40To75,
    cutEleTrkOS,
]
addCuts(ZtoTauToEleProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoTauToEleDisTrk = copy.deepcopy(ZtoTauToEleProbeTrkWithZCuts)
ZtoTauToEleDisTrk.name = cms.string("ZtoTauToEleDisTrk")
cutsToAdd = [
    cutTrkTauHadVeto,
    cutTrkEcalo,
]
addCuts(ZtoTauToEleDisTrk.cuts, cutsToAdd)
