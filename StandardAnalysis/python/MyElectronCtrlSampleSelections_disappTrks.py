import FWCore.ParameterSet.Config as cms
import copy
from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *  # Put all the individual cuts in this file 

###########################################################
##### Set up the event selections (channels) #####
###########################################################



# Define channels 
ZtoEE = cms.PSet(
     name = cms.string("ZtoEE"),
     triggers = triggersSingleElec, 
     cuts = cms.VPSet(
         cut2ElecPt,     
         cut2ElecEta,    
         cut2ElecD0,     
         cut2ElecDZ,     
         cut2ElecNHits,  
         cutMuonVeto,   
         cutElecElecMass,        
         )
    ) 


ZtoETrack = cms.PSet(
    name = cms.string("ZtoETrack"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet(
        cutElecPt,     
        cutElecEta,    
        cutElecD0,     
        cutElecDZ,     
        cutElecMva, 
        cutElecPFIso, 
        cutElecNHits,  
        cutTrkPt, 
        cutTrkEta, 
        cutTrkD0, 
        cutTrkDZ, 
        cutTrkNHits, 
        ## cutTrkHitMissMid,
        ## cutTrkHitMissIn, 
        cutTrkIso, 
        cutMuonVeto,   
        cutElecTrkDR, 
        ##      cutElecElecMass,        
        )
    )


ZtoETrackPreSel = copy.deepcopy(ZtoETrack)
ZtoETrackPreSel.name = cms.string("ZtoETrackPreSel")  
ZtoETrackPreSel.cuts.append(cutElecTrkInvMass)


ZtoETrackFullPreSel = cms.PSet(
    name = cms.string("ZtoETrackFullPreSel"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet(
        cutElecPt,     
        cutElecEta,    
        cutElecD0,     
        cutElecDZ,     
        cutElecMva, 
        cutElecPFIso, 
        cutElecNHits,  
        cutElecVetoOneMax,
        cutTrkPt, 
        cutTrkEta, 
        cutTrkD0, 
        cutTrkDZ, 
        cutTrkNHits, 
        cutTrkIso, 
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutMuonVeto,   
        cutElecTrkDR, 
        cutElecTrkInvMass, 
        )
    )


WtoENuTrigElec = cms.PSet(
    name = cms.string("WtoENuTrigElec"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet(
        cutEvtFilterScraping,
        cutVtxGood, 
        cutElecPt40,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        #        cutElecTightID,  
        cutElecPFIso,  
        cutElecNHits,  
        cutElecVetoOneMax, 
        cutMuonVeto,   
        cutMET40,
        )
    )


WtoENuTrigMET = copy.deepcopy(WtoENuTrigElec)
WtoENuTrigMET.name = cms.string("WtoENuTrigMET")
WtoENuTrigMET.triggers = triggersJetMet
WtoENuTrigMET.cuts.insert(0,cutJetPt)
WtoENuTrigMET.cuts.insert(0,cutMET)


WtoENuTrkSel = cms.PSet(
    name = cms.string("WtoENuTrkSel"),
    triggers = triggersJetMet, 
    cuts = cms.VPSet(
        cutJetPt, 
        cutMET, 
        cutEvtFilterScraping,
        cutVtxGood, 
        cutElecPt40,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutElecVetoOneMax, 
        cutMuonVeto,   
        cutTrkPt, 
        cutTrkEta, 
        cutTrkD0, 
        cutTrkDZ, 
        cutTrkNHits, 
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkIso, 
        ## cutTrkDeadEcalVeto,
        ## cutTrkCrackVeto,
        cutElecTrkDRSame, 
        )
    )


PreSelElecMatchTrigElecV1 = cms.PSet(
    name = cms.string("PreSelElecMatchTrigElecV1"),
    triggers = triggersSingleElec, 
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
        cutElecPt20,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutElecVetoOneMax, 
        cutMuonVetoPt10,   
        cutTrackPt,
        cutTrackEta,
        cutTrackd0,
        cutTrackNumValidHits,
        cutElecTrkDRSame,
    )
)

PreSelElecMatchTrigElecV2 = cms.PSet(
    name = cms.string("PreSelElecMatchTrigElecV2"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutElecPt20,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutElecVetoOneMax, 
        cutMuonVetoPt10,   
        cutTrackPt,
        cutTrackEta,
        cutTrackd0,
        cutTrackNumValidHits,
        cutElecTrkDRSame,
    )
)

PreSelElecMatchTrigElecV3 = cms.PSet(
    name = cms.string("PreSelElecMatchTrigElecV3"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutElecPt20,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutElecVetoOneMax, 
        cutMuonVetoPt10,   
        cutTrackPt,
        cutTrackEta,
        cutTrackd0,
        cutTrackNumValidHits,
        cutElecTrkDRSame,
    )
)

PreSelElecMatchTrigElecV4 = cms.PSet(
    name = cms.string("PreSelElecMatchTrigElecV4"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutElecPt20,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutElecVetoOneMax, 
        cutMuonVetoPt10,   
        cutTrackPt,
        cutTrackEta,
        cutTrackd0,
        cutTrackNumValidHits,
        cutElecTrkDRSame,
    )
)


