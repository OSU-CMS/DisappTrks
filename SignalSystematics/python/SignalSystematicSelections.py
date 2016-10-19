import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.SignalSystematics.Cuts import *
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

################################################################################
## ISR signal systematic
################################################################################
# doesn't use puJetId
ZtoMuMuISRStudy = cms.PSet(
    name = cms.string("ZtoMuMuISRStudy"),
    triggers = triggersDoubleMu,
    cuts = cms.VPSet(
        cutMuonPairPt20,
        cutMuonPairEta24,
        cutMuonPairTightID,
        cutMuonPairLoosePFIso,
        cutMuMuChargeProduct,
        cutMuMuInvMassZLo,
        cutMuMuInvMassZHi,
        cutMuonPairVetoThirdMuon,
        cutJetPt30,
        cutJetEta25,
        cutJetLooseID,
    )
)

ZtoMuMuISRStudy2016 = copy.deepcopy(ZtoMuMuISRStudy)
ZtoMuMuISRStudy2016.name = cms.string("ZtoMuMuISRStudy2016")
ZtoMuMuISRStudy2016.triggers = triggersDoubleMu2016

# Veto bjets (doesn't reweight in MC yet)

ZtoMuMuISRStudyVetoBjets = copy.deepcopy(ZtoMuMuISRStudy)
ZtoMuMuISRStudyVetoBjets.name = cms.string("ZtoMuMuISRStudyVetoBjets")
addCuts(ZtoMuMuISRStudyVetoBjets.cuts, [cutJetVetoCSVv2M])

ZtoMuMuISRStudy2016VetoBjets = copy.deepcopy(ZtoMuMuISRStudy2016)
ZtoMuMuISRStudy2016VetoBjets.name = cms.string("ZtoMuMuISRStudy2016VetoBjets")
addCuts(ZtoMuMuISRStudy2016VetoBjets.cuts, [cutJetVetoCSVv2M])

# Jet |eta| < 2.4, goodPV, no btagging
ZtoMuMuISRStudyMoreSimilar = cms.PSet(
    name = cms.string("ZtoMuMuISRStudyMoreSimiliar"),
    triggers = triggersDoubleMu,
    cuts = cms.VPSet(
        cutGoodPV,
        cutMuonPairPt20,
        cutMuonPairEta24,
        cutMuonPairTightID,
        cutMuonPairLoosePFIso,
        cutMuMuChargeProduct,
        cutMuMuInvMassZLo,
        cutMuMuInvMassZHi,
        cutMuonPairVetoThirdMuon,
        cutJetPt30,
        cutJetEta,
        cutJetTightLepVeto,
    )
)

ZtoMuMuISRStudyMoreSimilar2016 = copy.deepcopy(ZtoMuMuISRStudyMoreSimilar)
ZtoMuMuISRStudyMoreSimilar2016.name = cms.string("ZtoMuMuISRStudyMoreSimilar2016")
ZtoMuMuISRStudyMoreSimilar2016.triggers = triggersDoubleMu2016
