import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

##################################################
## Electron tag skim
##################################################
ElectronTagSkim = cms.PSet(
    name = cms.string("ElectronTagSkim"),
    triggers = triggersSingleEle,
    metFilters = metFilters,
    cuts = cms.VPSet (),
)
tagElectronCuts = [
    cutMetFilters,
    cutElectronPt, # pt>25 for 2015-6, >35 for 2017
    cutElectronEta21,
    cutElectronTightID,
    cutElectronTightPFIso,
]
addCuts(ElectronTagSkim.cuts, tagElectronCuts)

# In 2017 there is no eta2p1 trigger, but tracks require |eta|<2.1 so keep this cut
#if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_2_"):
#    addSingleCut(ElectronTagSkim.cuts, cutElectronEta24, cutElectronEta21)
#    removeCuts(ElectronTagSkim.cuts, [cutElectronEta21])

##################################################
## Higher pt to be closer to candidate track selection
##################################################
ElectronTagPt35 = copy.deepcopy(ElectronTagSkim)
ElectronTagPt35.name = cms.string("ElectronTagPt35")
addSingleCut(ElectronTagPt35.cuts, cutElectronPt35, cutElectronPt)
removeCuts(ElectronTagPt35.cuts, [cutElectronPt])
cutsToAdd = [
    cutElectronArbitration,
]
cutsToAdd += jetCuts
cutsToAdd += [
    cutTrkPt35,
    cutTrkElecDR0p1,
    cutTrkMatchRecoElec,
]
cutsToAdd += isoTrkCuts
addCuts(ElectronTagPt35.cuts, cutsToAdd)

ElectronTagPt35NoTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35NoTrig.name = cms.string("ElectronTagPt35NoTrig")
ElectronTagPt35NoTrig.triggers = cms.vstring()

ElectronTagPt35MetTrig = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetTrig.name = cms.string("ElectronTagPt35MetTrig")
ElectronTagPt35MetTrig.triggers = triggersMet

ElectronTagPt35MetCut = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35MetCut.name = cms.string("ElectronTagPt35MetCut")
addCuts(ElectronTagPt35MetCut.cuts, [cutElectronMetMinusOne])

ElectronTagPt35NoJetCuts = copy.deepcopy(ElectronTagPt35)
ElectronTagPt35NoJetCuts.name = cms.string("ElectronTagPt35NoJetCuts")
cutsToRemove = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutLeadingJetMetPhi,
]
removeCuts(ElectronTagPt35NoJetCuts.cuts, cutsToRemove)

ElectronTagPt35NoJetCutsMetTrig = copy.deepcopy(ElectronTagPt35NoJetCuts)
ElectronTagPt35NoJetCutsMetTrig.name = cms.string("ElectronTagPt35NoJetCutsMetTrig")
ElectronTagPt35NoJetCutsMetTrig.triggers = triggersMet

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
ElectronTagPt55 = copy.deepcopy(ElectronTagPt35)
ElectronTagPt55.name = cms.string("ElectronTagPt55")
addSingleCut(ElectronTagPt55.cuts, cutTrkPt55, cutTrkPt35)
removeCuts(ElectronTagPt55.cuts, [cutTrkPt35])

ElectronTagPt55NoTrig = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55NoTrig.name = cms.string("ElectronTagPt55NoTrig")
ElectronTagPt55NoTrig.triggers = cms.vstring()

ElectronTagPt55MetTrig = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55MetTrig.name = cms.string("ElectronTagPt55MetTrig")
ElectronTagPt55MetTrig.triggers = triggersMet

ElectronTagPt55MetCut = copy.deepcopy(ElectronTagPt55)
ElectronTagPt55MetCut.name = cms.string("ElectronTagPt55MetCut")
addCuts(ElectronTagPt55MetCut.cuts, [cutElectronMetMinusOne])

################################################################################
## Electron tag and probe sample
################################################################################
ZtoEleProbeTrkWithZCuts = copy.deepcopy(ElectronTagSkim)
ZtoEleProbeTrkWithZCuts.name = cms.string("ZtoEleProbeTrkWithZCuts")
cutsToAdd = [
    cutElectronArbitration,
    cutTrkPt30,
]
cutsToAdd += isoTrkCuts
cutsToAdd += [
    cutEleTrkInvMass10,
    cutTrkMuonVeto,
    cutTrkTauHadVeto,
    cutTrkArbitration,
    cutEleTrkInvMass80To100,
    cutEleTrkOS,
]
addCuts(ZtoEleProbeTrkWithZCuts.cuts, cutsToAdd)

ZtoEleProbeTrkBeforeArbitration = copy.deepcopy (ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkBeforeArbitration.name = cms.string ("ZtoEleProbeTrkBeforeArbitration")
removeCuts (ZtoEleProbeTrkBeforeArbitration.cuts, [cutTrkArbitration, cutEleTrkInvMass80To100, cutEleTrkOS])

ZtoEleProbeTrkWithoutD0Cut = copy.deepcopy (ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithoutD0Cut.name = cms.string ("ZtoEleProbeTrkWithoutD0Cut")
removeCuts (ZtoEleProbeTrkWithoutD0Cut.cuts, [cutTrkD0])

ElectronFiducialCalcBefore = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ElectronFiducialCalcBefore.name = cms.string("ElectronFiducialCalcBefore")
removeCuts(ElectronFiducialCalcBefore.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

ElectronFiducialCalcAfter = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ElectronFiducialCalcAfter.name = cms.string("ElectronFiducialCalcAfter")
addSingleCut(ElectronFiducialCalcAfter.cuts, cutTrkVetoElecVeto, cutEleTrkOS)
removeCuts(ElectronFiducialCalcAfter.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

ZtoEleDisTrk = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleDisTrk.name = cms.string("ZtoEleDisTrk")
addSingleCut(ZtoEleDisTrk.cuts, cutTrkNMissOut, cutEleTrkOS)
addSingleCut(ZtoEleDisTrk.cuts, cutTrkEcalo,    cutEleTrkOS)
addSingleCut(ZtoEleDisTrk.cuts, cutTrkElecVeto, cutEleTrkOS)

ZtoEleDisTrkNoNMissOutCut = copy.deepcopy(ZtoEleDisTrk)
ZtoEleDisTrkNoNMissOutCut.name = cms.string("ZtoEleDisTrkNoNMissOutCut")
removeCuts (ZtoEleDisTrkNoNMissOutCut.cuts, [cutTrkNMissOut])

ElectronTagPt55NoValidHitsCut = copy.deepcopy (ElectronTagPt55)
ElectronTagPt55NoValidHitsCut.name = cms.string ("ElectronTagPt55NoValidHitsCut")
removeCuts (ElectronTagPt55NoValidHitsCut.cuts, [cutTrkNValidHits])

ElectronTagPt55MetTrigNoValidHitsCut = copy.deepcopy (ElectronTagPt55MetTrig)
ElectronTagPt55MetTrigNoValidHitsCut.name = cms.string ("ElectronTagPt55MetTrigNoValidHitsCut")
removeCuts (ElectronTagPt55MetTrigNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoEleProbeTrkWithZCutsNoValidHitsCut = copy.deepcopy(ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithZCutsNoValidHitsCut.name = cms.string("ZtoEleProbeTrkWithZCutsNoValidHitsCut")
removeCuts(ZtoEleProbeTrkWithZCutsNoValidHitsCut.cuts, [cutTrkNValidHits])

ZtoEleDisTrkNoValidHitsCut = copy.deepcopy(ZtoEleDisTrk)
ZtoEleDisTrkNoValidHitsCut.name = cms.string("ZtoEleDisTrkNoValidHitsCut")
removeCuts(ZtoEleDisTrkNoValidHitsCut.cuts, [cutTrkNValidHits])

################################################################################
## Channels with reduced numbers of hits
################################################################################
ElectronTagPt55NHits3 = copy.deepcopy (ElectronTagPt55)
ElectronTagPt55NHits3.name = cms.string ("ElectronTagPt55NHits3")
addSingleCut (ElectronTagPt55NHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ElectronTagPt55NHits3.cuts, [cutTrkNValidHits])

ElectronTagPt55NHits4 = copy.deepcopy (ElectronTagPt55)
ElectronTagPt55NHits4.name = cms.string ("ElectronTagPt55NHits4")
addSingleCut (ElectronTagPt55NHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ElectronTagPt55NHits4.cuts, [cutTrkNValidHits])

ElectronTagPt55NHits5 = copy.deepcopy (ElectronTagPt55)
ElectronTagPt55NHits5.name = cms.string ("ElectronTagPt55NHits5")
addSingleCut (ElectronTagPt55NHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ElectronTagPt55NHits5.cuts, [cutTrkNValidHits])

ElectronTagPt55NHits6 = copy.deepcopy (ElectronTagPt55)
ElectronTagPt55NHits6.name = cms.string ("ElectronTagPt55NHits6")
addSingleCut (ElectronTagPt55NHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ElectronTagPt55NHits6.cuts, [cutTrkNValidHits])

ElectronTagPt55MetTrigNHits3 = copy.deepcopy (ElectronTagPt55MetTrig)
ElectronTagPt55MetTrigNHits3.name = cms.string ("ElectronTagPt55MetTrigNHits3")
addSingleCut (ElectronTagPt55MetTrigNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ElectronTagPt55MetTrigNHits3.cuts, [cutTrkNValidHits])

ElectronTagPt55MetTrigNHits4 = copy.deepcopy (ElectronTagPt55MetTrig)
ElectronTagPt55MetTrigNHits4.name = cms.string ("ElectronTagPt55MetTrigNHits4")
addSingleCut (ElectronTagPt55MetTrigNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ElectronTagPt55MetTrigNHits4.cuts, [cutTrkNValidHits])

ElectronTagPt55MetTrigNHits5 = copy.deepcopy (ElectronTagPt55MetTrig)
ElectronTagPt55MetTrigNHits5.name = cms.string ("ElectronTagPt55MetTrigNHits5")
addSingleCut (ElectronTagPt55MetTrigNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ElectronTagPt55MetTrigNHits5.cuts, [cutTrkNValidHits])

ElectronTagPt55MetTrigNHits6 = copy.deepcopy (ElectronTagPt55MetTrig)
ElectronTagPt55MetTrigNHits6.name = cms.string ("ElectronTagPt55MetTrigNHits6")
addSingleCut (ElectronTagPt55MetTrigNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ElectronTagPt55MetTrigNHits6.cuts, [cutTrkNValidHits])

ZtoEleProbeTrkWithZCutsNHits3 = copy.deepcopy (ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithZCutsNHits3.name = cms.string ("ZtoEleProbeTrkWithZCutsNHits3")
addSingleCut (ZtoEleProbeTrkWithZCutsNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ZtoEleProbeTrkWithZCutsNHits3.cuts, [cutTrkNValidHits])

ZtoEleProbeTrkWithZCutsNHits4 = copy.deepcopy (ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithZCutsNHits4.name = cms.string ("ZtoEleProbeTrkWithZCutsNHits4")
addSingleCut (ZtoEleProbeTrkWithZCutsNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ZtoEleProbeTrkWithZCutsNHits4.cuts, [cutTrkNValidHits])

ZtoEleProbeTrkWithZCutsNHits5 = copy.deepcopy (ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithZCutsNHits5.name = cms.string ("ZtoEleProbeTrkWithZCutsNHits5")
addSingleCut (ZtoEleProbeTrkWithZCutsNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ZtoEleProbeTrkWithZCutsNHits5.cuts, [cutTrkNValidHits])

ZtoEleProbeTrkWithZCutsNHits6 = copy.deepcopy (ZtoEleProbeTrkWithZCuts)
ZtoEleProbeTrkWithZCutsNHits6.name = cms.string ("ZtoEleProbeTrkWithZCutsNHits6")
addSingleCut (ZtoEleProbeTrkWithZCutsNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ZtoEleProbeTrkWithZCutsNHits6.cuts, [cutTrkNValidHits])

ZtoEleDisTrkNHits3 = copy.deepcopy (ZtoEleDisTrk)
ZtoEleDisTrkNHits3.name = cms.string ("ZtoEleDisTrkNHits3")
addSingleCut (ZtoEleDisTrkNHits3.cuts, cutTrkNValidHits3, cutTrkNValidHits)
removeCuts (ZtoEleDisTrkNHits3.cuts, [cutTrkNValidHits])

ZtoEleDisTrkNHits4 = copy.deepcopy (ZtoEleDisTrk)
ZtoEleDisTrkNHits4.name = cms.string ("ZtoEleDisTrkNHits4")
addSingleCut (ZtoEleDisTrkNHits4.cuts, cutTrkNValidHits4, cutTrkNValidHits)
removeCuts (ZtoEleDisTrkNHits4.cuts, [cutTrkNValidHits])

ZtoEleDisTrkNHits5 = copy.deepcopy (ZtoEleDisTrk)
ZtoEleDisTrkNHits5.name = cms.string ("ZtoEleDisTrkNHits5")
addSingleCut (ZtoEleDisTrkNHits5.cuts, cutTrkNValidHits5, cutTrkNValidHits)
removeCuts (ZtoEleDisTrkNHits5.cuts, [cutTrkNValidHits])

ZtoEleDisTrkNHits6 = copy.deepcopy (ZtoEleDisTrk)
ZtoEleDisTrkNHits6.name = cms.string ("ZtoEleDisTrkNHits6")
addSingleCut (ZtoEleDisTrkNHits6.cuts, cutTrkNValidHits6, cutTrkNValidHits)
removeCuts (ZtoEleDisTrkNHits6.cuts, [cutTrkNValidHits])

# create copies of all above selections with the fiducial electron/muon cuts removed
for selection in list (locals ()):
    if not hasattr (locals ()[selection], "name") or not hasattr (locals ()[selection], "triggers") or not hasattr (locals ()[selection], "cuts"):
        continue
    locals ()[selection + "NoElectronMuonFiducialCuts"] = copy.deepcopy (locals ()[selection])
    locals ()[selection + "NoElectronMuonFiducialCuts"].name = cms.string (locals ()[selection].name.value () + "NoElectronMuonFiducialCuts")
    removeCuts (locals ()[selection + "NoElectronMuonFiducialCuts"].cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])
