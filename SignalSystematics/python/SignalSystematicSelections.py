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
