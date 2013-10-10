import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.MyCuts_disappTrks import *  # Put all the individual cuts in this file 

##################################################
##### Set up the event selections (channels) #####
##################################################
SingleElecTrig = cms.PSet(
    name = cms.string("SingleElecTrig"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet(
      cutNoCuts,
      )
    ) 

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




## Bkgd estimate ctrl sample ##
ZtoETrk = cms.PSet(
    name = cms.string("ZtoETrk"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet (
        cutElecPt,     
        cutElecEta,    
        cutElecD0,     
        #        cutElecDZ,     
        cutElecMva, 
        cutElecPFIso, 
        cutElecNHits,
        #        cutElecPlusMet220, 
#        cutElecPlusMet220, 
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutElecTrkDR, 
        cutElecTrkInvMass,
       ),
    )




## Bkgd estimate ctrl sample ##
ZtoETrk_MetTrig = cms.PSet(
    name = cms.string("ZtoETrk_MetTrig"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutElecPt,
        cutElecEta,
        cutElecD0,
        #        cutElecDZ,
        cutElecMva,
        cutElecPFIso,
        cutElecNHits,
        #        cutElecPlusMet220,
        cutElecPlusMet110,
        cutSecJetPt,
        cutSecJetEta2p4,
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutElecLooseIDOnlyOne,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,
        cutTrkJetDeltaR,
        cutElecTrkDR,
        cutElecTrkInvMass,
        ),
    )



## Bkgd estimate ctrl sample ##
ZtoETrkEId = cms.PSet(
    name = cms.string("ZtoETrkEId"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet (
        cutElecPt,     
        cutElecEta,    
        cutElecD0,     
        #        cutElecDZ,     
        cutElecMva, 
        cutElecPFIso, 
        cutElecNHits,
        #        cutElecPlusMet220, 
#        cutElecPlusMet220, 
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutElecLooseIDVetoInv,
        cutElecTrkDR, 
        cutElecTrkInvMass,
       ),
    )

## Bkgd estimate ctrl sample ##
ZtoETrkEVeto = cms.PSet(
    name = cms.string("ZtoETrkEVeto"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet (
        cutElecPt,     
        cutElecEta,    
        cutElecD0,     
        #        cutElecDZ,     
        cutElecMva, 
        cutElecPFIso, 
        cutElecNHits,
        #        cutElecPlusMet220, 
#        cutElecPlusMet220, 
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutElecLooseIDVeto,
        cutElecTrkDR, 
        cutElecTrkInvMass,
       ),
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
        cutElecVetoOneMax, 
        cutElecPt30,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutMuonVetoPt10,   
        cutMET30,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkNHits,
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
        cutElecVetoOneMax, 
        cutElecPt30,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutMuonVetoPt10,   
        cutMET30,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkNHits,
        cutElecTrkDRSame,
    )
)

PreSelElecMatchTrigElecV2NJet1         = copy.deepcopy(PreSelElecMatchTrigElecV2)
PreSelElecMatchTrigElecV2NJet2         = copy.deepcopy(PreSelElecMatchTrigElecV2)
PreSelElecMatchTrigElecV2NJet3         = copy.deepcopy(PreSelElecMatchTrigElecV2)
PreSelElecMatchTrigElecV2NJet4         = copy.deepcopy(PreSelElecMatchTrigElecV2)
PreSelElecMatchTrigElecV2NJet1BTagVeto = copy.deepcopy(PreSelElecMatchTrigElecV2)
PreSelElecMatchTrigElecV2NJet2BTagVeto = copy.deepcopy(PreSelElecMatchTrigElecV2)
PreSelElecMatchTrigElecV2NJet3BTagVeto = copy.deepcopy(PreSelElecMatchTrigElecV2)
PreSelElecMatchTrigElecV2NJet4BTagVeto = copy.deepcopy(PreSelElecMatchTrigElecV2)

PreSelElecMatchTrigElecV2NJet1.name         = "PreSelElecMatchTrigElecV2NJet1" 
PreSelElecMatchTrigElecV2NJet2.name         = "PreSelElecMatchTrigElecV2NJet2" 
PreSelElecMatchTrigElecV2NJet3.name         = "PreSelElecMatchTrigElecV2NJet3" 
PreSelElecMatchTrigElecV2NJet4.name         = "PreSelElecMatchTrigElecV2NJet4" 
PreSelElecMatchTrigElecV2NJet1BTagVeto.name = "PreSelElecMatchTrigElecV2NJet1BTagVeto" 
PreSelElecMatchTrigElecV2NJet2BTagVeto.name = "PreSelElecMatchTrigElecV2NJet2BTagVeto" 
PreSelElecMatchTrigElecV2NJet3BTagVeto.name = "PreSelElecMatchTrigElecV2NJet3BTagVeto"  
PreSelElecMatchTrigElecV2NJet4BTagVeto.name = "PreSelElecMatchTrigElecV2NJet4BTagVeto"  

PreSelElecMatchTrigElecV2NJet1BTagVeto.cuts.append(cutSecJetBTagVeto)  
PreSelElecMatchTrigElecV2NJet2BTagVeto.cuts.append(cutSecJetBTagVeto)  
PreSelElecMatchTrigElecV2NJet3BTagVeto.cuts.append(cutSecJetBTagVeto)  
PreSelElecMatchTrigElecV2NJet4BTagVeto.cuts.append(cutSecJetBTagVeto)  

PreSelElecMatchTrigElecV2NJet1BTagVeto.cuts.insert(2,cutJetPt30NJet1) 
PreSelElecMatchTrigElecV2NJet2BTagVeto.cuts.insert(2,cutJetPt30NJet2) 
PreSelElecMatchTrigElecV2NJet3BTagVeto.cuts.insert(2,cutJetPt30NJet3) 
PreSelElecMatchTrigElecV2NJet4BTagVeto.cuts.insert(2,cutJetPt30NJet4) 
PreSelElecMatchTrigElecV2NJet1.        cuts.insert(2,cutJetPt30NJet1) 
PreSelElecMatchTrigElecV2NJet2.        cuts.insert(2,cutJetPt30NJet2) 
PreSelElecMatchTrigElecV2NJet3.        cuts.insert(2,cutJetPt30NJet3) 
PreSelElecMatchTrigElecV2NJet4.        cuts.insert(2,cutJetPt30NJet4) 

PreSelElecMatchTrigElecV2NJet1BTagVeto.cuts.insert(2,cutJetEta2p4) 
PreSelElecMatchTrigElecV2NJet2BTagVeto.cuts.insert(2,cutJetEta2p4) 
PreSelElecMatchTrigElecV2NJet3BTagVeto.cuts.insert(2,cutJetEta2p4) 
PreSelElecMatchTrigElecV2NJet4BTagVeto.cuts.insert(2,cutJetEta2p4) 
PreSelElecMatchTrigElecV2NJet1.        cuts.insert(2,cutJetEta2p4) 
PreSelElecMatchTrigElecV2NJet2.        cuts.insert(2,cutJetEta2p4) 
PreSelElecMatchTrigElecV2NJet3.        cuts.insert(2,cutJetEta2p4) 
PreSelElecMatchTrigElecV2NJet4.        cuts.insert(2,cutJetEta2p4) 




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
        cutElecVetoOneMax, 
        cutElecPt30,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutMuonVetoPt10,   
        cutMET30,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkNHits,
        cutBTagVeto,
        cutElecTrkDRSame,
    )
)

PreSelElecMatchTrigElecV4 = cms.PSet(
    name = cms.string("PreSelElecMatchTrigElecV4"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutElecVetoOneMax, 
        cutElecPt30,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutMuonVetoPt10,   
        cutMET30,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkNHits,
        cutBTagVeto,
        cutElecTrkDRSame,
    )
)


WToENuSimple = cms.PSet(
    name = cms.string("WToENuSimple"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutElecVetoOneMax, 
        cutElecPt30,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        cutElecPFIso,  
        cutElecNHits,  
        cutMuonVetoPt10,   
        cutMET30,
        ## cutJetPt30N0,
        ## cutJetEta2p4N0,
        ## cutJetIDLooseN0,
        )
    )


