import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *
from DisappTrks.BackgroundEstimation.ZtoMuMuSelections import *

def createHitsVariations (ch, chName):
    globals ().update (createChannelVariations (ch, chName, None, cutTrkNLayersVariations))
    globals ().update (createChannelVariations (ch, chName, cutTrkNValidHitsSignal, cutTrkNValidHitsVariations))
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        replaceSingleCut (globals ()[chName + 'NHits3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)
        replaceSingleCut (globals ()[chName + 'NLayers3'].cuts, cutTrkNValidPixelHits[3], cutTrkNValidPixelHitsSignal)

################################################################################
################################################################################
# IMPORTANT!
# This is actaully the central value selection for MC since you need to smear the jets
################################################################################
################################################################################
disTrkSelectionSmearedJets = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJets.name = cms.string("disTrkSelectionSmearedJets")
replaceSingleCut (disTrkSelectionSmearedJets.cuts, cutJetJERSmearedPt, cutJetPt)
################################################################################
################################################################################

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

createHitsVariations(disTrkSelection,         "disTrkSelection")
createHitsVariations(disTrkSelectionJECUp,    "disTrkSelectionJECUp")
createHitsVariations(disTrkSelectionJECDown,  "disTrkSelectionJECDown")

################################################################################
## JER signal systematic
################################################################################

disTrkSelectionSmearedJetsNoElectronMuonFiducialCuts = copy.deepcopy(disTrkSelectionSmearedJets)
disTrkSelectionSmearedJetsNoElectronMuonFiducialCuts.name = cms.string("disTrkSelectionSmearedJetsNoElectronMuonFiducialCuts")
removeCuts (disTrkSelectionSmearedJetsNoElectronMuonFiducialCuts.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

disTrkSelectionSmearedJetsUp = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsUp.name = cms.string("disTrkSelectionSmearedJetsUp")
replaceSingleCut (disTrkSelectionSmearedJetsUp.cuts, cutJetJERSmearedPtUp, cutJetPt)

disTrkSelectionSmearedJetsDown = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsDown.name = cms.string("disTrkSelectionSmearedJetsDown")
replaceSingleCut (disTrkSelectionSmearedJetsDown.cuts, cutJetJERSmearedPtDown, cutJetPt)

disTrkSelectionSmearedJetsJECUp = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsJECUp.name = cms.string("disTrkSelectionSmearedJetsJECUp")
replaceSingleCut (disTrkSelectionSmearedJetsJECUp.cuts, cutJetJERSmearedPtJECUp, cutJetPt)

disTrkSelectionSmearedJetsJECDown = copy.deepcopy(disTrkSelection)
disTrkSelectionSmearedJetsJECDown.name = cms.string("disTrkSelectionSmearedJetsJECDown")
replaceSingleCut (disTrkSelectionSmearedJetsJECDown.cuts, cutJetJERSmearedPtJECDown, cutJetPt)

disTrkSelectionSmearedJetsL1PrefiringTest = copy.deepcopy(disTrkSelectionSmearedJets)
disTrkSelectionSmearedJetsL1PrefiringTest.name = cms.string("disTrkSelectionSmearedJetsL1PrefiringTest")
addSingleCut(disTrkSelectionSmearedJetsL1PrefiringTest.cuts, cutVetoL1PrefiringJets, cutLeadingJetMetPhi)

createHitsVariations(disTrkSelectionSmearedJets,        "disTrkSelectionSmearedJets")
createHitsVariations(disTrkSelectionSmearedJetsUp,      "disTrkSelectionSmearedJetsUp")
createHitsVariations(disTrkSelectionSmearedJetsDown,    "disTrkSelectionSmearedJetsDown")
createHitsVariations(disTrkSelectionSmearedJetsJECUp,   "disTrkSelectionSmearedJetsJECUp")
createHitsVariations(disTrkSelectionSmearedJetsJECDown, "disTrkSelectionSmearedJetsJECDown")
createHitsVariations(disTrkSelectionSmearedJetsL1PrefiringTest, "disTrkSelectionSmearedJetsL1PrefiringTest")

################################################################################
## MET signal systematic
################################################################################

disTrkNoMet = copy.deepcopy(disTrkSelection)
disTrkNoMet.name = cms.string("DisTrkNoMet")
removeCuts(disTrkNoMet.cuts, [cutMet])

disTrkNoMetSmearedJets = copy.deepcopy(disTrkSelectionSmearedJets)
disTrkNoMetSmearedJets.name = cms.string("DisTrkNoMetSmearedJets")
removeCuts(disTrkNoMetSmearedJets.cuts, [cutMet])

createHitsVariations(disTrkNoMet,             "disTrkNoMet")
createHitsVariations(disTrkNoMetSmearedJets,  "disTrkNoMetSmearedJets")

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

#######################################################################
# Test channel comparing to MT2 analysis cuts. 
# Requested by Yuri 4-08-19
#######################################################################
disTrkSelectionSmearedJetsCompareMT2 = copy.deepcopy(disTrkSelectionSmearedJets)
disTrkSelectionSmearedJetsCompareMT2.name = cms.string("disTrkSelectionSmearedJetsCompareMT2")
addSingleCut(disTrkSelectionSmearedJetsCompareMT2.cuts, cutJetPairPt30, cutJetJERSmearedPt)
addSingleCut(disTrkSelectionSmearedJetsCompareMT2.cuts, cutJetPairEta, cutJetEta)
addSingleCut(disTrkSelectionSmearedJetsCompareMT2.cuts, cutJetPairTightLepVeto, cutJetTightLepVeto)
addCuts(disTrkSelectionSmearedJetsCompareMT2.cuts, [cutHT250])

createHitsVariations(disTrkSelectionSmearedJetsCompareMT2, "disTrkSelectionSmearedJetsCompareMT2")

#######################################################################
# Number of missing outer hits channels
#######################################################################

createHitsVariations(disTrkNoNMissOut,        "disTrkNoNMissOut")


