import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *
from DisappTrks.BackgroundEstimation.ZtoMuMuSelections import *

################################################################################
## ISR signal systematic
################################################################################

ZtoMuMuISRStudy = copy.deepcopy(ZtoMuMu)
ZtoMuMuISRStudy.name = cms.string("ZtoMuMuISRStudy")
cutsToAdd = [
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutLeadingJetMetPhi,
]
addCuts(ZtoMuMuISRStudy.cuts, cutsToAdd)

# Drop MET requirement, jet pt requirement of only 30
ZtoMuMuISRStudyJet30 = copy.deepcopy(ZtoMuMu)
ZtoMuMuISRStudyJet30.name = cms.string("ZtoMuMuISRStudyJet30")
cutsToAdd = [
    cutJetPt30,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutLeadingJetMetPhi,
]
addCuts(ZtoMuMuISRStudyJet30.cuts, cutsToAdd)

################################################################################
## JEC signal systematic
################################################################################

disTrkSelectionJECUp = copy.deepcopy(disTrkSelection)
disTrkSelectionJECUp.name = cms.string("disTrkSelectionJECUp")
removeCuts(disTrkSelectionJECUp.cuts, [cutJetPt])
addCuts(disTrkSelectionJECUp.cuts, [cutJetPtJECUp])

disTrkSelectionJECDown = copy.deepcopy(disTrkSelection)
disTrkSelectionJECDown.name = cms.string("disTrkSelectionJECDown")
removeCuts(disTrkSelectionJECDown.cuts, [cutJetPt])
addCuts(disTrkSelectionJECDown.cuts, [cutJetPtJECDown])

################################################################################
## JER signal systematic
################################################################################

disTrkSelectionSmearedJets = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJets.name = cms.string("disTrkSelectionSmearedJets")
removeCuts(disTrkSelectionSmearedJets.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJets.cuts, [cutJetJERSmearedPt])

disTrkSelectionSmearedJetsNoElectronMuonFiducialCuts = copy.deepcopy(disTrkSelectionSmearedJets)
disTrkSelectionSmearedJetsNoElectronMuonFiducialCuts.name = cms.string("disTrkSelectionSmearedJetsNoElectronMuonFiducialCuts")
removeCuts (disTrkSelectionSmearedJetsNoElectronMuonFiducialCuts.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

disTrkSelectionSmearedJetsUp = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsUp.name = cms.string("disTrkSelectionSmearedJetsUp")
removeCuts(disTrkSelectionSmearedJetsUp.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJetsUp.cuts, [cutJetJERSmearedPtUp])

disTrkSelectionSmearedJetsDown = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsDown.name = cms.string("disTrkSelectionSmearedJetsDown")
removeCuts(disTrkSelectionSmearedJetsDown.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJetsDown.cuts, [cutJetJERSmearedPtDown])

disTrkSelectionSmearedJetsJECUp = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsJECUp.name = cms.string("disTrkSelectionSmearedJetsJECUp")
removeCuts(disTrkSelectionSmearedJetsJECUp.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJetsJECUp.cuts, [cutJetJERSmearedPtJECUp])

disTrkSelectionSmearedJetsJECDown = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsJECDown.name = cms.string("disTrkSelectionSmearedJetsJECDown")
removeCuts(disTrkSelectionSmearedJetsJECDown.cuts, [cutJetPt])
addCuts(disTrkSelectionSmearedJetsJECDown.cuts, [cutJetJERSmearedPtJECDown])

################################################################################
## MET signal systematic
################################################################################

disTrkNoMet = copy.deepcopy(disTrkSelection)
disTrkNoMet.name = cms.string("DisTrkNoMet")
removeCuts(disTrkNoMet.cuts, [cutMet])

disTrkNoMetSmearedJets = copy.deepcopy(disTrkSelectionSmearedJets)
disTrkNoMetSmearedJets.name = cms.string("DisTrkNoMetSmearedJets")
removeCuts(disTrkNoMetSmearedJets.cuts, [cutMet])

##########################################################################
#2017 Trig Efficiency Tests
##########################################################################

#metTrigTemp = copy.deepcopy(disTrkSelection)
#metTrigTemp.name = cms.string("metTrigTemp")
#metTrigTemp.triggers = cms.vstring()
#removeCuts (metTrigTemp.cuts, [cutMet])

metTrigNoTriggers = copy.deepcopy(disTrkNoMet)
metTrigNoTriggers.name = cms.string("metTrigNoTriggers")
metTrigNoTriggers.triggers = cms.vstring()

metTrigNoTriggersNoRandom = copy.deepcopy(metTrigNoTriggers)
metTrigNoTriggersNoRandom.name = cms.string("metTrigNoTriggersNoRandom")
removeCuts(metTrigNoTriggersNoRandom.cuts, [cutTrkNMissOut,cutTrkNMissMid])
addCuts(metTrigNoTriggersNoRandom.cuts, [cutTrkNMissOutNoDrop,cutTrkNMissMidNoDrop])

metTrig01 = copy.deepcopy(disTrkNoMet)
metTrig01.name = cms.string("metTrig01")
metTrig01.triggers = cms.vstring('HLT_MET105_IsoTrk50_v')
removeCuts(metTrig01.cuts, [cutTrkNMissOut,cutTrkNMissMid])
addCuts(metTrig01.cuts, [cutTrkNMissOutNoDrop,cutTrkNMissMidNoDrop])

metTrig02 = copy.deepcopy(metTrig01)
metTrig02.name = cms.string("metTrig02")
metTrig02.triggers.append('HLT_PFMET140_PFMHT140_IDTight_v')

metTrig03 = copy.deepcopy(metTrig02)
metTrig03.name = cms.string("metTrig03")
metTrig03.triggers.append('HLT_PFMET250_HBHECleaned_v')

metTrig04 = copy.deepcopy(metTrig03)
metTrig04.name = cms.string("metTrig04")
metTrig04.triggers.append('HLT_PFMET300_HBHECleaned_v')

metTrig05 = copy.deepcopy(metTrig04)
metTrig05.name = cms.string("metTrig05")
metTrig05.triggers.append('HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v')

metTrig06 = copy.deepcopy(metTrig05)
metTrig06.name = cms.string("metTrig06")
metTrig06.triggers.append('HLT_PFMETTypeOne140_PFMHT140_IDTight_v')

metTrig07 = copy.deepcopy(metTrig06)
metTrig07.name = cms.string("metTrig07")
metTrig07.triggers.append('HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v')

metTrig08 = copy.deepcopy(metTrig07)
metTrig08.name = cms.string("metTrig08")
metTrig08.triggers.append('HLT_PFMET120_PFMHT120_IDTight_v')

metTrig09 = copy.deepcopy(metTrig08)
metTrig09.name = cms.string("metTrig09")
metTrig09.triggers.append('HLT_PFMET130_PFMHT130_IDTight_v')

metTrig10 = copy.deepcopy(metTrig09)
metTrig10.name = cms.string("metTrig10")
metTrig10.triggers.append('HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v')

metTrig11 = copy.deepcopy(metTrig10)
metTrig11.name = cms.string("metTrig11")
metTrig11.triggers.append('HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v')

metTrig12 = copy.deepcopy(metTrig11)
metTrig12.name = cms.string("metTrig12")
metTrig12.triggers.append('HLT_PFMETTypeOne120_PFMHT120_IDTight_v')

metTrig13 = copy.deepcopy(metTrig12)
metTrig13.name = cms.string("metTrig13")
metTrig13.triggers.append('HLT_PFMETTypeOne130_PFMHT130_IDTight_v')