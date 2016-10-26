import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.SignalSystematics.Cuts import *
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

################################################################################
## ISR signal systematic
################################################################################

ZtoMuMuISRStudy = cms.PSet(
    name = cms.string("ZtoMuMuISRStudy"),
    triggers = triggersDoubleMu,
    cuts = cms.VPSet(
        cutMet, # > 100

        # >=1 jets
        cutGoodPV, # has PV
        cutJetPt, # > 110
        cutJetEta, # < 2.4
        cutJetTightLepVeto, # tight ID
        cutDijetDeltaPhiMax, # deltaPhi(jets)

        # >=2 muons
        cutMuonPairPt20,  # track pt > 55
        cutMuonPairEta21, # track abs(eta) < 2.1
        cutMuonPairTightID,
        cutMuMuChargeProduct,
        cutMuMuInvMassZLo,
        cutMuMuInvMassZHi,
        cutMuonPairVetoThirdMuon,
        cutMuonPairJetDeltaRVeto,
    )
)

ZtoMuMuISRStudy2016 = copy.deepcopy(ZtoMuMuISRStudy)
ZtoMuMuISRStudy2016.name = cms.string("ZtoMuMuISRStudy2016")
ZtoMuMuISRStudy2016.triggers = triggersDoubleMu2016

# Drop MET requirement
ZtoMuMuISRStudyNoMet = copy.deepcopy(ZtoMuMuISRStudy)
ZtoMuMuISRStudyNoMet.name = cms.string("ZtoMuMuISRStudyNoMet")
removeCuts(ZtoMuMuISRStudyNoMet.cuts, [cutMet])

ZtoMuMuISRStudy2016NoMet = copy.deepcopy(ZtoMuMuISRStudy2016)
ZtoMuMuISRStudy2016NoMet.name = cms.string("ZtoMuMuISRStudy2016NoMet")
removeCuts(ZtoMuMuISRStudy2016NoMet.cuts, [cutMet])

# Drop MET requirement, jet pt requirement of only 30
ZtoMuMuISRStudyNoMetJet30 = cms.PSet(
    name = cms.string("ZtoMuMuISRStudyNoMetJet30"),
    triggers = triggersDoubleMu,
    cuts = cms.VPSet(
        # >=1 jets
        cutGoodPV, # has PV
        cutJetPt30, # > 30
        cutJetEta, # < 2.4
        cutJetTightLepVeto, # tight ID
        cutDijetDeltaPhiMax, # deltaPhi(jets)

        # >=2 muons
        cutMuonPairPt20,  # track pt > 55
        cutMuonPairEta21, # track abs(eta) < 2.1
        cutMuonPairTightID,
        cutMuMuChargeProduct,
        cutMuMuInvMassZLo,
        cutMuMuInvMassZHi,
        cutMuonPairVetoThirdMuon,
        cutMuonPairJetDeltaRVeto,
    )
)

ZtoMuMuISRStudy2016NoMetJet30 = copy.deepcopy(ZtoMuMuISRStudyNoMetJet30)
ZtoMuMuISRStudy2016NoMetJet30.name = cms.string("ZtoMuMuISRStudy2016NoMetJet30")
ZtoMuMuISRStudy2016NoMetJet30.triggers = triggersDoubleMu2016
