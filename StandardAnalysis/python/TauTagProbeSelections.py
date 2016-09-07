import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions
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
ZtoTauIsoTrk = copy.deepcopy(MuonTagSkim)
ZtoTauIsoTrk.name = cms.string("ZtoTauIsoTrk")

muTrkCuts = [
    cutMuTrkInvMass10,
]
addCuts(ZtoTauIsoTrk.cuts, [cutMuonMT])
addCuts(ZtoTauIsoTrk.cuts, [cutMuonArbitration])
addCuts(ZtoTauIsoTrk.cuts, [cutTrkPt30])
addCuts(ZtoTauIsoTrk.cuts, isoTrkCuts)
addCuts(ZtoTauIsoTrk.cuts, muTrkCuts)
cutsToRemove = [
    cutTrkPt55,
    cutTrkJetDeltaPhi,
]
removeCuts(ZtoTauIsoTrk.cuts, cutsToRemove)

ZtoTauProbeTrk = copy.deepcopy(ZtoTauIsoTrk)
ZtoTauProbeTrk.name = cms.string("ZtoTauProbeTrk")

cutsToAdd = [
    cutTrkElecVeto,
    cutTrkMuonVeto,
]
addCuts(ZtoTauProbeTrk.cuts, cutsToAdd)
addCuts(ZtoTauProbeTrk.cuts, [cutTrkArbitration])

ZtoTauProbeTrkWithZCuts = copy.deepcopy(ZtoTauProbeTrk)
ZtoTauProbeTrkWithZCuts.name = cms.string("ZtoTauProbeTrkWithZCuts")
cutsToAdd = [
    cutMuTrkInvMass40To75,
    cutMuTrkOS,
]
addCuts(ZtoTauProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoTauDisTrk = copy.deepcopy(ZtoTauProbeTrkWithZCuts)
ZtoTauDisTrk.name = cms.string("ZtoTauDisTrk")
cutsToAdd = [
    cutTrkTauHadVeto,
    cutTrkEcalo,
]
addCuts(ZtoTauDisTrk.cuts, cutsToAdd)
