import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.MuonTagProbeSelections import *

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
]
addCuts(ZtoMuMuISRStudy.cuts, cutsToAdd)

ZtoMuMuISRStudy2016 = copy.deepcopy(ZtoMuMuISRStudy)
ZtoMuMuISRStudy2016.name = cms.string("ZtoMuMuISRStudy2016")
ZtoMuMuISRStudy2016.triggers = triggersSingleMu2016

####################################################################################################
# Drop MET requirement, jet pt requirement of only 30
####################################################################################################
ZtoMuMuISRStudyJet30 = copy.deepcopy(ZtoMuMu)
ZtoMuMuISRStudyJet30.name = cms.string("ZtoMuMuISRStudyJet30")
cutsToAdd = [
    cutJetPt30,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
]
addCuts(ZtoMuMuISRStudyJet30.cuts, cutsToAdd)

ZtoMuMuISRStudy2016Jet30 = copy.deepcopy(ZtoMuMuISRStudyJet30)
ZtoMuMuISRStudy2016Jet30.name = cms.string("ZtoMuMuISRStudy2016Jet30")
ZtoMuMuISRStudy2016Jet30.triggers = triggersSingleMu2016
