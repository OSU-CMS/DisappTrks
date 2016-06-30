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
    cutTrkPt,
    cutTrkTauDR0p1,
    cutTrkMatchRecoTau,
    cutTrkEta,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
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
cutsToAdd = [
#    cutTrkEcalo,
#    cutTrkNMissOut,
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
    cutTrkPt,
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
]
addCuts(ZtoTauDisTrk.cuts, cutsToAdd)

ZtoTauDisTrkWithECaloCut = copy.deepcopy(ZtoTauDisTrk)
ZtoTauDisTrkWithECaloCut.name = cms.string("ZtoTauDisTrkWithECaloCut")
cutsToAdd = [
    cutTrkEcalo,
]
addCuts(ZtoTauDisTrkWithECaloCut.cuts, cutsToAdd)
