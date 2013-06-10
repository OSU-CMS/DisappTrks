
import FWCore.ParameterSet.Config as cms
import copy
from DisappTrksT3ANTemp.StandardAnalysis.MyCuts_disappTrks import *  # Put all the individual cuts in this file 

##################################################
##### Set up the event selections (channels) #####
##################################################

WToMu = cms.PSet(
    name = cms.string("WToMu"),
    triggers = triggersSingleMu,
#    triggers = triggersJetMet,
    cuts = cms.VPSet(
         cutMET,
         cutJetPt,
         cutEvtFilterScraping,
         cutVtxGood,
         cutMuonEta,
         cutMuonPt20,
         cutMuonTightID,
         cutMuonPFIso,
         cutMuonD0,
         cutMuonOneOnly,
         cutMET40,
         )
    )

ZtoMuMu = cms.PSet(
    # Get this example from http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/OSUT3Analysis/AnaTools/python/MyEventSelections.py?revision=1.2&view=markup  
    name = cms.string("ZtoMuMu"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
         cutMuonPairPt20,
         cutMuonPairEta,
         cutMuonPairTightID,
         cutMuonPairPFIso,
         cutMuonPairD0,
         cutMuonPairDZ,
         cutElecVeto,
         cutMuMuChargeProduct,
         cutMuMuInvMass,
         cutMuTrkDeltaR,
         )
    )   

WtoMuNuTrackFullPreSel = cms.PSet(
    name = cms.string("WtoMuNuTrackFullPreSel"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutMuonPt20,
         cutMuonEta,
         cutMuonTightID,
         cutMuonPFIso,
         cutMuonD0,
         cutMuonDZ,
         cutMuonValidHits,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissIn,
         cutTrkHitMissMid,
         cutTrkIso,
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         cutMuonOneOnly,
         cutMuTrkDeltaR,
         )
    )


PreSelMuonMatchTrigMuonV1 = cms.PSet(
    name = cms.string("PreSelMuonMatchTrigMuonV1"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutMET,
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutMuonOneOnly,
        cutMuonPt25,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutElecVetoPt10,   
        cutMET30,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkNHits,
        cutMuonTrkDRSame,
    )
)

PreSelMuonMatchTrigMuonV2 = cms.PSet(
    name = cms.string("PreSelMuonMatchTrigMuonV2"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutMuonOneOnly,
        cutMuonPt25,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutElecVetoPt10,   
        cutMET30,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkNHits,
        cutMuonTrkDRSame,
    )
)


PreSelMuonMatchTrigMuonV2NoJetCut = cms.PSet(
    name = cms.string("PreSelMuonMatchTrigMuonV2"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutMuonOneOnly,
        cutMuonPt25,
        cutMuonEta,
        cutMuonTightID,
        cutMuonDetIso,
        cutMuonD0,
        cutElecVetoPt10,   
        cutMET30,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkNHits,
        cutMuonTrkDRSame,
    )
)

PreSelMuonMatchTrigMuonV3 = cms.PSet(
    name = cms.string("PreSelMuonMatchTrigMuonV3"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutMuonOneOnly,
        cutMuonPt25,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutElecVetoPt10,   
        cutMET30,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkNHits,
        cutMuonTrkDRSame,
    )
)

PreSelMuonMatchTrigMuonV4 = cms.PSet(
    name = cms.string("PreSelMuonMatchTrigMuonV4"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutMuonOneOnly,
        cutMuonPt25,
        cutMuonEta2p1,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutElecVetoPt10,   
        cutMET30,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkNHits,
        cutMuonTrkDRSame,
    )
)



WToMuSimple = cms.PSet(
    name = cms.string("WToMuSimple"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutEvtFilterScraping,
         cutVtxGood,
         cutMuonOneOnly,
         cutMuonPt25,
         cutMuonEta,
         cutMuonTightID,
         cutMuonPFIso,
         cutMuonD0,
         cutElecVetoPt10,   
         cutMET30,
         cutJetPt30N0,
         cutJetEta2p4N0,
         cutJetIDLooseN0,
         )
    )


PreSelMuonMatchTrigMuonV2NJet1         = copy.deepcopy(PreSelMuonMatchTrigMuonV2)
PreSelMuonMatchTrigMuonV2NJet2         = copy.deepcopy(PreSelMuonMatchTrigMuonV2)
PreSelMuonMatchTrigMuonV2NJet3         = copy.deepcopy(PreSelMuonMatchTrigMuonV2)
PreSelMuonMatchTrigMuonV2NJet4         = copy.deepcopy(PreSelMuonMatchTrigMuonV2)
PreSelMuonMatchTrigMuonV2NJet1BTagVeto = copy.deepcopy(PreSelMuonMatchTrigMuonV2)
PreSelMuonMatchTrigMuonV2NJet2BTagVeto = copy.deepcopy(PreSelMuonMatchTrigMuonV2)
PreSelMuonMatchTrigMuonV2NJet3BTagVeto = copy.deepcopy(PreSelMuonMatchTrigMuonV2)
PreSelMuonMatchTrigMuonV2NJet4BTagVeto = copy.deepcopy(PreSelMuonMatchTrigMuonV2)

PreSelMuonMatchTrigMuonV2NJet1.name         = "PreSelMuonMatchTrigMuonV2NJet1" 
PreSelMuonMatchTrigMuonV2NJet2.name         = "PreSelMuonMatchTrigMuonV2NJet2" 
PreSelMuonMatchTrigMuonV2NJet3.name         = "PreSelMuonMatchTrigMuonV2NJet3" 
PreSelMuonMatchTrigMuonV2NJet4.name         = "PreSelMuonMatchTrigMuonV2NJet4" 
PreSelMuonMatchTrigMuonV2NJet1BTagVeto.name = "PreSelMuonMatchTrigMuonV2NJet1BTagVeto" 
PreSelMuonMatchTrigMuonV2NJet2BTagVeto.name = "PreSelMuonMatchTrigMuonV2NJet2BTagVeto" 
PreSelMuonMatchTrigMuonV2NJet3BTagVeto.name = "PreSelMuonMatchTrigMuonV2NJet3BTagVeto"  
PreSelMuonMatchTrigMuonV2NJet4BTagVeto.name = "PreSelMuonMatchTrigMuonV2NJet4BTagVeto"  

PreSelMuonMatchTrigMuonV2NJet1BTagVeto.cuts.append(cutSecJetBTagVeto)  
PreSelMuonMatchTrigMuonV2NJet2BTagVeto.cuts.append(cutSecJetBTagVeto)  
PreSelMuonMatchTrigMuonV2NJet3BTagVeto.cuts.append(cutSecJetBTagVeto)  
PreSelMuonMatchTrigMuonV2NJet4BTagVeto.cuts.append(cutSecJetBTagVeto)  

PreSelMuonMatchTrigMuonV2NJet1BTagVeto.cuts.insert(2,cutJetPt30NJet1) 
PreSelMuonMatchTrigMuonV2NJet2BTagVeto.cuts.insert(2,cutJetPt30NJet2) 
PreSelMuonMatchTrigMuonV2NJet3BTagVeto.cuts.insert(2,cutJetPt30NJet3) 
PreSelMuonMatchTrigMuonV2NJet4BTagVeto.cuts.insert(2,cutJetPt30NJet4) 
PreSelMuonMatchTrigMuonV2NJet1.        cuts.insert(2,cutJetPt30NJet1) 
PreSelMuonMatchTrigMuonV2NJet2.        cuts.insert(2,cutJetPt30NJet2) 
PreSelMuonMatchTrigMuonV2NJet3.        cuts.insert(2,cutJetPt30NJet3) 
PreSelMuonMatchTrigMuonV2NJet4.        cuts.insert(2,cutJetPt30NJet4) 

PreSelMuonMatchTrigMuonV2NJet1BTagVeto.cuts.insert(2,cutJetEta2p4) 
PreSelMuonMatchTrigMuonV2NJet2BTagVeto.cuts.insert(2,cutJetEta2p4) 
PreSelMuonMatchTrigMuonV2NJet3BTagVeto.cuts.insert(2,cutJetEta2p4) 
PreSelMuonMatchTrigMuonV2NJet4BTagVeto.cuts.insert(2,cutJetEta2p4) 
PreSelMuonMatchTrigMuonV2NJet1.        cuts.insert(2,cutJetEta2p4) 
PreSelMuonMatchTrigMuonV2NJet2.        cuts.insert(2,cutJetEta2p4) 
PreSelMuonMatchTrigMuonV2NJet3.        cuts.insert(2,cutJetEta2p4) 
PreSelMuonMatchTrigMuonV2NJet4.        cuts.insert(2,cutJetEta2p4) 




DebugMuon = cms.PSet(
    name = cms.string("PreSelMuonMatchTrigMuonV4"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
        cutMuonOneOnly,
        cutMuonPt25,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutElecVetoPt10,   
        cutMET30,
    )
)

