import FWCore.ParameterSet.Config as cms
import copy
from DisappTrksT3ANTemp.StandardAnalysis.MyCuts_disappTrks import *  # Put all the individual cuts in this file 
##################################################
##### Set up the event selections (channels) #####
##################################################

ZtoTauTau = cms.PSet(
    name = cms.string("ZtoTauTau"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
         cutTauPairPt,
         cutTauPairEta,
         cutTauPairValidHits,
         cutTauPairNumProng,
         cutTauPairNumSigGamma,
         cutTauPairNumSigNeutral,
         cutTauPairNumPi0,
         cutTauPairInvMass,
         ),
    )
ZtoMuTau = cms.PSet(
    name = cms.string("ZtoMuTau"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
         cutTauPt,
         cutTauEta,
         cutTauOneProng,
         cutTauNumSigGamma,
         cutTauNumSigNeutral,
         cutTauNumSigPi0,
         cutTauAgainstElectron,
         cutTauAgainstMuonTight,
         cutTauValidHits,
         cutMuonEta,
         cutMuonPt20,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         ),
    )
ZtoTauTrack = cms.PSet(
    name = cms.string("ZtoTauTrack"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # tau cuts
         cutTauPt,
         cutTauEta,
         cutTauAgainstElectron,
         cutTauAgainstMuonTight,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutTauTrkDeltaR,
         cutMuTrkDeltaR,
         cutTauTrkDeltaR,
         cutMuTauCharge,
         cutMuTauInvMass,
         ),
    )

ZtoTauTrackForElec = cms.PSet(
    name = cms.string("ZtoTauTrackForElec"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # tau cuts
         cutTauPt,
         cutTauEta,
         cutTauForElectron,
         cutTauAgainstMuonTight,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutTauTrkDeltaR,
         cutMuTrkDeltaR,
         cutTauTrkDeltaR,
         cutMuTauCharge,
         cutMuTauInvMass,
         ),
    )


ZtoTauTrackOneProng = cms.PSet(
    name = cms.string("ZtoTauTrackOneProng"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         #tau cuts
         cutTauPt,
         cutTauEta,
         cutTauAgainstElectron,
         cutTauAgainstMuonTight,
         cutTauOneProng,
         #track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutTauTrkDeltaR,
         cutMuTrkDeltaR,
         cutTauTrkDeltaR,
         cutMuTauCharge,
         cutMuTauInvMass,
         ),
    )

ZtoTauTrackThreeProng = cms.PSet(
    name = cms.string("ZtoTauTrackThreeProng"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # tau cuts
         cutTauPt,
         cutTauEta,
         cutTauAgainstElectron,
         cutTauAgainstMuonTight,
         cutTauThreeProng,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutTauTrkDeltaR,
         cutMuTrkDeltaR,
         cutTauTrkDeltaR,
         cutMuTauCharge,
         cutMuTauInvMass,
         ),
    )



ZtoTauTrackMuonMed = cms.PSet(
    name = cms.string("ZtoTauTrackMuonMed"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # tau cuts
         cutTauPt,
         cutTauEta,
         cutTauAgainstElectron,
         cutTauAgainstMuonMed,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutTauTrkDeltaR,
         cutMuTrkDeltaR,
         cutTauTrkDeltaR,
         cutMuTauCharge,
         cutMuTauInvMass,
         ),
    )



ZtoTauTrackDiMuonVeto = cms.PSet(
    name = cms.string("ZtoTauTrackDiMuonVeto"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         #muon cuts
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutMuonOneOnly,
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # tau cuts
         cutTauPt,
         cutTauEta,
         cutTauAgainstElectron,
         cutTauAgainstMuonTight,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutTauTrkDeltaR,
         cutMuTrkVeto,
         cutMuTrkDeltaR,
         cutTauTrkDeltaR,
         cutMuTauCharge,
         cutMuTauInvMass,
         ),
    )

ZtoTauTrackDecayMode = cms.PSet(
    name = cms.string("ZtoTauTrackDecayMode"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         #muon cuts
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         cutMuonOneOnly,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # tau cuts
         cutTauPt,
         cutTauEta,
         cutTauDecayModeFinding,
         cutTauAgainstElectron,
         cutTauAgainstMuonTight,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutTauTrkDeltaR,
         cutMuTrkDeltaR,
         cutTauTrkDeltaR,
         cutMuTauCharge,
         cutMuTauInvMass,
         ),
    )


ZtoMuTrackMet20 = cms.PSet(
    name = cms.string("ZtoMuTrackMet20"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutMET20,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )

ZtoMuTrackMet50 = cms.PSet(
    name = cms.string("ZtoMuTrackMet50"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutMET50,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )
ZtoMuTrackMet75 = cms.PSet(
    name = cms.string("ZtoMuTrackMet75"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutMET75,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )

ZtoMuTrackMet100 = cms.PSet(
    name = cms.string("ZtoMuTrackMet100"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutMET100,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )

ZtoMuTrackJet20 = cms.PSet(
    name = cms.string("ZtoMuTrackJet20"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutJetPt20,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         
         ),
    )

ZtoMuTrackJet50 = cms.PSet(
    name = cms.string("ZtoMuTrackJet50"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutJetPt50,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )
ZtoMuTrackJet75 = cms.PSet(
    name = cms.string("ZtoMuTrackJet75"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutJetPt75,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )

ZtoMuTrackJet100 = cms.PSet(
    name = cms.string("ZtoMuTrackJet100"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutJetPt100,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )

ZtoMuTrackJetMet20 = cms.PSet(
    name = cms.string("ZtoMuTrackJetMet20"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutMET20,
         cutJetPt20,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         
         ),
    )

ZtoMuTrackJetMet50 = cms.PSet(
    name = cms.string("ZtoMuTrackJetMet50"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutMET50,
         cutJetPt50,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         
         ),
    )

ZtoMuTrackJetMet100 = cms.PSet(
    name = cms.string("ZtoMuTrackJetMet100"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutMET100,
         cutJetPt100,
         #muon cuts
         cutMuonOneOnly,
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         #electron vetos
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )

ZtoTauTrackNoSumPt = cms.PSet(
    name = cms.string("ZtoTauTrackNoSumPt"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         #muon cuts
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         # electron and extra muon veto
         cutMuonOneOnly,
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # tau cuts
         cutTauPt,
         cutTauEta,
         cutTauAgainstElectron,
         cutTauAgainstMuonTight,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         #cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutTauTrkDeltaR,
         cutMuTrkDeltaR,
         cutTauTrkDeltaR,
         cutMuTauCharge,
         cutMuTauInvMass,
         ),
    )

ZtoTauTrackTauIso = cms.PSet(
    name = cms.string("ZtoTauTrackTauIso"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         #muon cuts
         cutMuonPt20,
         cutMuonEta,
         cutMuonValidHits,
         cutMuonTightID,
         cutMuonPFIso,
         # electron and extra muon veto
         cutMuonOneOnly,
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         # tau cuts
         cutTauPt,
         cutTauPtLeadingTrack,
         cutTauEta,
         cutTauLooseIso,
         cutTauAgainstElectron,
         cutTauAgainstMuonTight,
         cutTauValidHits,
         # track cuts
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         # cuts on pairs of objects
         cutMuonMetMT,
         cutTauTrkDeltaR,
         cutMuTrkDeltaR,
         cutTauTrkDeltaR,
         cutMuTauCharge,
         cutMuTauInvMass,
         ),
    )



#WToTauNu selection taken from http://cms.cern.ch/iCMS/jsp/db_notes/showNoteDetails.jsp?noteID=CMS%20AN-2011/019
WToTauNu = cms.PSet(
    name = cms.string("WToTauNu"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         cutJetPt,
         cutTauPt,
         cutTauPtLeadingTrack,
         cutTauEta,
         cutTauLooseIso,
         cutTauAgainstElectron,
         cutTauAgainstMuonTight,
         cutTauValidHits,
         cutElecVeto,
         cutMuonVeto
         )
    )

WToTauNuPTrack = cms.PSet(
    name = cms.string("WToTauNuPTrack"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         cutJetPt,
         #cutTauPt,
         #cutTauPtLeadingTrack,
         #cutTauEta,
         #cutTauLooseIso,
         #cutTauAgainstElectron,
         #cutTauAgainstMuonTight,
         #cutTauValidHits,
         cutElecVeto,
         cutMuonVeto,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         cutTauTrkDeltaR,
         )
    )

WToTauNuPTrackNoJetMet = cms.PSet(
    name = cms.string("WToTauNuPTrackNoJetMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#         cutMET,
#         cutJetPt,
#         cutTauPt,
#         cutTauPtLeadingTrack,
#         cutTauEta,
#         cutTauLooseIso,
#         cutTauAgainstElectron,
#         cutTauAgainstMuonTight,
#         cutTauValidHits,
         cutElecVeto,
         cutMuonVeto,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkIso,
         cutTrkSumPtLT,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         cutTauTrkDeltaR,
         )
    )




