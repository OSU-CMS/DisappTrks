import FWCore.ParameterSet.Config as cms
import copy
from DisappTrksT3ANTemp.StandardAnalysis.MyCuts_disappTrks import *  # Put all the individual cuts in this file 
################################################
##### List of  event selections (channels) #####
################################################


NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    cuts = cms.VPSet (
       cutNoCuts,
       ),
    )

TriggerJetMet = cms.PSet(
    name = cms.string("TriggerJetMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
    ),
    )

TriggerMet = cms.PSet(
    name = cms.string("TriggerMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         ),
    )

Trigger = cms.PSet(
    name = cms.string("Trigger"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
    cutNoCuts,
    ),
    )

TriggerJetMetDebug = cms.PSet(
    name = cms.string("TriggerJetMetDebug"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,  
        cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
        ),
    )

TriggerJetMetDebug2 = cms.PSet(
    name = cms.string("TriggerJetMetDebug2"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,  
        cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
        cutElecLooseIDVeto,  # cut on secondary jets collection so that BNTree includes all jets  
        ),
    )

TriggerJetMetDebug3 = cms.PSet(
    name = cms.string("TriggerJetMetDebug3"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,  
        cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
        cutMuonLooseIDVeto,  # cut on secondary jets collection so that BNTree includes all jets  
        ),
    )

## Preselection ##
PreSelection = cms.PSet(
    name = cms.string("PreSelection"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        ),
    )


## Preselection invert muon veto ##
PreSelInvMuonVeto = cms.PSet(
    name = cms.string("PreSelInvMuonVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutElecLooseIDVeto,
        cutMuonLooseIDVetoInv,
        cutTauLooseHadronicVeto,
        ),
    )


PreSelNoTauVeto = cms.PSet(
    name = cms.string("PreSelNoTauVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )


PreSelNoLepVeto = cms.PSet(
    name = cms.string("PreSelNoLepVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutTauLooseHadronicVeto,
        ),
    )

## Preselection invert elec veto##
PreSelectionInvElecVeto = cms.PSet(
    name = cms.string("PreSelectionInvElecVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutElecLooseIDVetoInv,
        cutMuonLooseIDVeto,
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
        ),
    )

## Preselection invert tau veto ##
PreSelectionInvTauVeto = cms.PSet(
    name = cms.string("PreSelectionInvTauVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVetoInv,
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
        ),
    )

PreSelElecVetoEnd = cms.PSet(
    name = cms.string("PreSelElecVetoEnd"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
        #        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        ),
    )

PreSelMuonVetoEnd = cms.PSet(
    name = cms.string("PreSelMuonVetoEnd"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutTauLooseHadronicVeto,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )

PreSelTauVetoEnd = cms.PSet(
    name = cms.string("PreSelTauVetoEnd"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        ),
    )

PreSelElecVetoEndInv = cms.PSet(
    name = cms.string("PreSelElecVetoEndInv"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        ),
    )

PreSelMuonVetoEndInv = cms.PSet(
    name = cms.string("PreSelMuonVetoEndInv"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutTauLooseHadronicVeto,
        cutElecLooseIDVeto,
        cutMuonLooseIDVetoInv,
        cutSecMuonLooseIDVetoInv,
        ),
    )

PreSelTauVetoEndInv = cms.PSet(
    name = cms.string("PreSelTauVetoEndInv"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTauLooseHadronicVetoInv,
        ),
    )



ZtoMuTrk = cms.PSet(
    name = cms.string("ZtoMuTrk"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutMuonDZ,
        cutMuonValidHits,
        cutMuonPlusMet220, 
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        ),
    )

## Ctrl sample for muons ##
ZtoMuTrkInvMuonVeto = cms.PSet(
    name = cms.string("ZtoMuTrkInvMuonVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutMuonDZ,
        cutMuonValidHits,
        cutMuonPlusMet220, 
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
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
        cutElecLooseIDVeto,
        cutMuonLooseIDVetoInv,
        cutTauLooseHadronicVeto,
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        ),
    )


PreSelectionMuonVetoOnly = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnly"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
       cutMET,
       cutSecJetPt,
       cutSecJetEta2p4,
       cutSecJetNoiseChgHad,
       cutSecJetNoiseChgEM,
       cutSecJetNoiseNeuHad,
       cutSecJetNoiseNeuEM,
       cutSubLeadingJetID,
       cutElecLooseIDVeto,
       cutMuonLooseIDVeto,
       ),
    )



PreSelectionMuonLooseID = cms.PSet(
    name = cms.string("PreSelectionMuonLooseID"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
       cutMET,
       cutSecJetPt,
       cutSecJetEta2p4,
       cutSecJetNoiseChgHad,
       cutSecJetNoiseChgEM,
       cutSecJetNoiseNeuHad,
       cutSecJetNoiseNeuEM,
       cutSubLeadingJetID,
       cutElecLooseIDVeto,
       cutMuonLooseID,
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
       cutJetJetDPhi,
       ),
    )

## Ctrl sample for electrons ##
PreSelectionElec = cms.PSet(
    name = cms.string("PreSelectionElec"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
       cutMET,
       cutSecJetPt,
       cutSecJetEta2p4,            
       cutSecJetNoiseChgHad,
       cutSecJetNoiseChgEM,
       cutSecJetNoiseNeuHad,
       cutSecJetNoiseNeuEM,
       cutSubLeadingJetID,
       cutJetJetDPhi,
       cutMuonLooseIDVeto,
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
       cutElecMva,
       cutElecTrkDRSame,
       ),
    )

## Ctrl sample for muons ##
PreSelectionMuon = cms.PSet(
    name = cms.string("PreSelectionMuon"),
    #    triggers = triggersJetMet,
    cuts = cms.VPSet (
        #       cutMET,
        #       cutSecJetPt,
       cutSecJetEta2p4,            
       cutSecJetNoiseChgHad,
       cutSecJetNoiseChgEM,
       cutSecJetNoiseNeuHad,
       cutSecJetNoiseNeuEM,
       cutSubLeadingJetID,
       cutJetJetDPhi,
       cutElecLooseIDVeto,
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
       cutMuonTightID,
       cutMuonTrkDRSame,
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




PreSelectionPTrkJetDeltaR = cms.PSet(
    name = cms.string("PreSelectionPTrkJetDeltaR"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         cutSecJetPt,
         cutSecJetEta2p4,
         cutSecJetNoiseChgHad,
         cutSecJetNoiseChgEM,
         cutSecJetNoiseNeuHad,
         cutSecJetNoiseNeuEM,
         cutSubLeadingJetID,
         cutElecLooseIDVeto,
         cutMuonLooseIDVeto,
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
         cutTrkJetDeltaR
         ),
    )


PreSelectionWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
## PreSelectionWithTrigJetMet.cuts.insert(0,cutJetPt)
## PreSelectionWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionDeadEcalMatch = cms.PSet(
        name = cms.string("PreSelectionDeadEcalMatch"),
        cuts = cms.VPSet (
           cutTrkPt,
           cutTrkEta,
           cutTrkD0,
           cutTrkDZ,
           cutTrkNHits,
           cutTrkHitMissMid,
           cutTrkHitMissIn,
           cutTrkIso,
           cutMuonVeto,
           cutElecVeto,
           cutTrkDeadEcalMatch,
           cutTrkCrackVeto,
           ),
        )

PreSelectionDeadEcalMatchWithTrigJetMet = cms.PSet(
        name = cms.string("PreSelectionDeadEcalMatchWithTrigJetMet"),
        triggers = triggersJetMet,
        cuts = copy.deepcopy(PreSelectionDeadEcalMatch.cuts),
        )
PreSelectionDeadEcalMatchWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionDeadEcalMatchWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnly = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkIso,
         ),
    )

PreSelectionIsoTrkOnlyWithNoiseClean = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyWithNoiseClean"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutEvtFilterScraping,
         cutVtxGood,
         cutMET,
         cutJetPt,
         cutJetEta,
         cutJetNoiseChgHad,
         cutJetNoiseNeuEM,
         cutJetNoiseNeuHad,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkIso,
         cutTrkSumPtLT,
         ),
    )

PreSelectionWithNoiseClean = cms.PSet(
    name = cms.string("PreSelectionWithNoiseClean"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutEvtFilterScraping,
         cutVtxGood,
         cutMET,
         cutJetPt,
         cutJetEta,
         cutJetNoiseChgHad,
         cutJetNoiseNeuEM,
         cutJetNoiseNeuHad,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkIso,
         cutTrkSumPtLT,
         cutMuonVeto,
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         ),
    )

PreSelectionIsoTrkOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnly.cuts),
    )
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnlyElecMatch = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyElecMatch"),
    triggers = triggersJetMet,
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
        #        cutElecTightID,  
        cutElecPFIso,  
        cutElecNHits,  
        cutElecVetoOneMax, 
        cutMuonVetoPt10,   
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        #        cutTrkDZ,
        cutTrkNHits,
        ## cutTrkHitMissMid,
        ## cutTrkHitMissIn,
        ## cutTrkIso,
        ## cutTrkSumPtLT,
        cutElecTrkDRSame,
    )
)


PreSelectionIsoTrkOnlyMuonMatch = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyMuonMatch"),
    triggers = triggersJetMet,
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
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonDetIso,
        cutMuonD0,
        cutMuonOneOnly,
        cutElecVetoPt10,   
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        #        cutTrkDZ,
        cutTrkNHits,
        ## cutTrkHitMissMid,
        ## cutTrkHitMissIn,
        #        cutTrkIso,
        #        cutTrkSumPtLT,
        cutMuonTrkDRSame,
    )
)


PreSelectionIsoTrkOnlyNoMuonMatch = copy.deepcopy(PreSelectionIsoTrkOnlyWithTrigJetMet)
PreSelectionIsoTrkOnlyNoMuonMatch.name = "PreSelectionIsoTrkOnlyNoMuonMatch"
PreSelectionIsoTrkOnlyNoMuonMatch.cuts.append(cutMuonTrkDRSameNone)
PreSelectionIsoTrkOnlyNoMuonMatch.cuts.append(cutMuonVeto)

PreSelectionIsoTrkOnlyNoElecMatch = copy.deepcopy(PreSelectionIsoTrkOnlyWithTrigJetMet)
PreSelectionIsoTrkOnlyNoElecMatch.name = "PreSelectionIsoTrkOnlyNoElecMatch"
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutTrkDeadEcalVeto)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutTrkCrackVeto)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutElecTrkDRSameNone)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutElecVeto)




PreSelectionIsoTrkOnlyNoDz = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDz"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )

PreSelectionIsoTrkOnlyNoDzWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDzWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoDz.cuts),
    )
PreSelectionIsoTrkOnlyNoDzWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoDzWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyNoD0 = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDz"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )

PreSelectionIsoTrkOnlyNoD0WithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoD0WithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoD0.cuts),
    )
PreSelectionIsoTrkOnlyNoD0WithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoD0WithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionMuonVetoOnly = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnly"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       cutMuonVeto,
       ),
    )

PreSelectionMuonVetoOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionMuonVetoOnly.cuts),
    )
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionElectronVetoOnly = cms.PSet(
    name = cms.string("PreSelectionElectronVetoOnly"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       cutMuonVeto,
       cutElecVeto,
       ),
    )

PreSelectionElectronVetoOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionElectronVetoOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionElectronVetoOnly.cuts),
    )
PreSelectionElectronVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionElectronVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionDeadEcalVetoOnly = cms.PSet(
        name = cms.string("PreSelectionDeadEcalVetoOnly"),
        cuts = cms.VPSet (
           cutTrkPt,
           cutTrkEta,
           cutTrkD0,
           cutTrkDZ,
           cutTrkNHits,
           cutTrkHitMissMid,
           cutTrkHitMissIn,
           cutTrkIso,
           cutMuonVeto,
           cutElecVeto,
           cutTrkDeadEcalVeto,
           ),
        )

PreSelectionDeadEcalVetoOnlyWithTrigJetMet = cms.PSet(
        name = cms.string("PreSelectionDeadEcalVetoOnlyWithTrigJetMet"),
            triggers = triggersJetMet,
            cuts = copy.deepcopy(PreSelectionDeadEcalVetoOnly.cuts),
            )
PreSelectionDeadEcalVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionDeadEcalVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionDeadEcalMatchOnly = cms.PSet(
            name = cms.string("PreSelectionDeadEcalMatchOnly"),
            cuts = cms.VPSet (
               cutTrkPt,
               cutTrkEta,
               cutTrkD0,
               cutTrkDZ,
               cutTrkNHits,
               cutTrkHitMissMid,
               cutTrkHitMissIn,
               cutTrkIso,
               cutMuonVeto,
               cutElecVeto,
               cutTrkDeadEcalMatch,
               ),
            )

PreSelectionDeadEcalMatchOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionDeadEcalMatchOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionDeadEcalMatchOnly.cuts),
    )
PreSelectionDeadEcalMatchOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionDeadEcalMatchOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnlyDzSide = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyDzSide"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZSide,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyDzSideWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyDzSide.cuts),
    )
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyD0Side = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyD0Side"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0Side,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )
PreSelectionIsoTrkOnlyD0SideWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyD0SideWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyD0Side.cuts),
    )
PreSelectionIsoTrkOnlyD0SideWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyD0SideWithTrigJetMet.cuts.insert(0,cutMET)


PreSelIdMuon = cms.PSet(
    name = cms.string("PreSelIdMuon"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelIdMuon.cuts.append(cutTrkMuonId)

PreSelInvVetoIdMuon = cms.PSet(
    name = cms.string("PreSelInvVetoIdMuon"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelInvMuonVeto.cuts),
    )
PreSelInvVetoIdMuon.cuts.append(cutTrkMuonId)


PreSelectionPMissing = cms.PSet(
    name = cms.string("PreSelectionPMissing"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPMissing.cuts.append(cutTrkHitMissOut)

PreSelNoTauVetoPMissing = cms.PSet(
    name = cms.string("PreSelNoTauVetoPMissing"),
    cuts = copy.deepcopy(PreSelNoTauVeto.cuts),
    )
PreSelNoTauVetoPMissing.cuts.append(cutTrkHitMissOut)


PreSelectionPMissingWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPMissingWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPMissingBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPSumPtLessThan = cms.PSet(
    name = cms.string("PreSelectionPSumPtLessThan"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPSumPtLessThan.cuts.append(cutTrkSumPtLT)

PreSelectionPSumPtLessThanWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPSumPtLessThanWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPSumPtLessThan.cuts),
    )
PreSelectionPSumPtLessThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPSumPtLessThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPSumPtLessThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPSumPtLessThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPSumPtLessThanWithTrigJetMet.cuts),
    )
PreSelectionPSumPtLessThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPSumPtGreaterThan = cms.PSet(
    name = cms.string("PreSelectionPSumPtGreaterThan"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPSumPtGreaterThan.cuts.append(cutTrkSumPtGT)

PreSelectionPSumPtGreaterThanWithTrigJetMet = cms.PSet(
            name = cms.string("PreSelectionPSumPtGreaterThanWithTrigJetMet"),
            triggers = triggersJetMet,
            cuts = copy.deepcopy(PreSelectionPSumPtGreaterThan.cuts),
            )
PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPSumPtGreaterThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPSumPtGreaterThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts),
    )
PreSelectionPSumPtGreaterThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPMissingSumPtGreaterThan = cms.PSet(
        name = cms.string("PreSelectionPMissingSumPtGreaterThan"),
        cuts = copy.deepcopy(PreSelectionPMissing.cuts),
        )
PreSelectionPMissingSumPtGreaterThan.cuts.append(cutTrkSumPtGT)


PreSelectionPMissingSumPtGreaterThanWithTrigJetMet = cms.PSet(
        name = cms.string("PreSelectionPMissingSumGreaterThanWithTrigJetMet"),
            triggers = triggersJetMet,
            cuts = copy.deepcopy(PreSelectionPMissingSumPtGreaterThan.cuts),
            )
PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPMissingSumPtGreaterThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingSumGreaterThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts),
    )
PreSelectionPMissingSumPtGreaterThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPMissingSumPtLessThan = cms.PSet(
    name = cms.string("PreSelectionPMissingSumPtLessThan"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingSumPtLessThan.cuts.append(cutTrkSumPtLT)

PreSelectionPMissingSumPtLessThanWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingSumLessThanWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingSumPtLessThan.cuts),
    )
PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPMissingSumPtLessThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingSumLessThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts),
    )
PreSelectionPMissingSumPtLessThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPMissingDzSide = cms.PSet(
    name = cms.string("PreSelectionPMissingDzSide"),
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyDzSide.cuts),
    )
PreSelectionPMissingDzSide.cuts.append(cutMuonVeto)
PreSelectionPMissingDzSide.cuts.append(cutElecVeto)
PreSelectionPMissingDzSide.cuts.append(cutTrkDeadEcalVeto)
PreSelectionPMissingDzSide.cuts.append(cutTrkCrackVeto)
PreSelectionPMissingDzSide.cuts.append(cutTrkHitMissOut)

PreSelectionPMissingD0Side = cms.PSet(
    name = cms.string("PreSelectionPMissingD0Side"),
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyD0Side.cuts),
    )
PreSelectionPMissingD0Side.cuts.append(cutMuonVeto)
PreSelectionPMissingD0Side.cuts.append(cutElecVeto)
PreSelectionPMissingD0Side.cuts.append(cutTrkDeadEcalVeto)
PreSelectionPMissingD0Side.cuts.append(cutTrkCrackVeto)
PreSelectionPMissingD0Side.cuts.append(cutTrkHitMissOut)


## Preselection (AOD)
PreSelectionNoHitCut = cms.PSet(
    name = cms.string("PreSelectionNoHitCut"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkIso,
       cutMuonVeto,
       cutElecVeto,
       cutTrkDeadEcalVeto,
       cutTrkCrackVeto,
       ),
    )
PreSelectionNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionNoHitCut.cuts),
    )
PreSelectionNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyNoHitCut = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoHitCut"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkIso,
       ),
    )

PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoHitCut.cuts),
    )
PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionMuonVetoOnlyNoHitCut = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyNoHitCut"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkIso,
       cutMuonVeto,
       ),
    )
PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionMuonVetoOnlyNoHitCut.cuts),
    )
PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)



## Gen Matched Channels ##

PreSelectionCharginoId = cms.PSet(
    name = cms.string("PreSelectionCharginoId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionCharginoId.cuts.append(cutTrkCharginoId)


PreSelectionElectronId = cms.PSet(
    name = cms.string("PreSelectionElectronId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionElectronId.cuts.append(cutTrkElectronId)

PreSelMuonId = cms.PSet(
    name = cms.string("PreSelMuonId"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelMuonId.cuts.append(cutTrkMuonId)

PreSelectionElectronIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionElectronIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
PreSelectionElectronIdWithTrigJetMet.cuts.append(cutTrkElectronId)


PreSelectionPionId = cms.PSet(
    name = cms.string("PreSelectionPionId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPionId.cuts.append(cutTrkPionId)

PreSelectionPionIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPionIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
PreSelectionPionIdWithTrigJetMet.cuts.append(cutTrkPionId)


PreSelectionNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionNotGenMatched"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionNotGenMatched.cuts.append(cutTrkNotGenMatched)


PreSelectionPMissingElectronId = cms.PSet(
    name = cms.string("PreSelectionPMissingElectronId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingElectronId.cuts.append(cutTrkElectronId)


PreSelectionPMissingElectronIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPMissingElectronIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingElectronIdWithTrigJetMet.cuts.append(cutTrkElectronId)


PreSelectionPMissingPionId = cms.PSet(
    name = cms.string("PreSelectionPMissingPionId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingPionId.cuts.append(cutTrkPionId)

PreSelectionPMissingPionIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPMissingPionIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingPionIdWithTrigJetMet.cuts.append(cutTrkPionId)


PreSelectionPMissingNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionPMissingNotGenMatched"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingNotGenMatched.cuts.append(cutTrkNotGenMatched)


PreSelectionPMissingLtMesonId = cms.PSet(
    name = cms.string("PreSelectionPMissingLtMesonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingLtMesonId.cuts.append(cutTrkLightMesonId)


PreSelectionPMissingKMesonId = cms.PSet(
    name = cms.string("PreSelectionPMissingKMesonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingKMesonId.cuts.append(cutTrkKMesonId)


PreSelectionPMissingLtBaryonId = cms.PSet(
    name = cms.string("PreSelectionPMissingLtBaryonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingLtBaryonId.cuts.append(cutTrkLightBaryonId)


PreSelectionPMissingKBaryonId = cms.PSet(
    name = cms.string("PreSelectionPMissingKBaryonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingKBaryonId.cuts.append(cutTrkKBaryonId)


## Signal Region Channels ##

SigRegWithMaxCaloByPLoose = cms.PSet(
    name = cms.string("SigRegWithMaxCaloByPLoose"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloByPLoose.cuts.append(cutMaxCaloByPLoose)


SigRegWithMaxCaloByPLooseWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloByPLooseWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloByPLooseWithTrigJetMet.cuts.append(cutMaxCaloByPLoose)


SigRegWithMaxCaloByP = cms.PSet(
    name = cms.string("SigRegWithMaxCaloByP"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloByP.cuts.append(cutMaxCaloByP)


SigRegWithMaxCalo = cms.PSet(
    name = cms.string("SigRegWithMaxCalo"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
)
SigRegWithMaxCalo.cuts.append(cutMaxCaloTight)


SigRegWithMaxCaloLoose = cms.PSet(
    name = cms.string("SigRegWithMaxCaloLoose"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloLoose.cuts.append(cutMaxCaloLoose)


SigRegWithMaxCaloLooseWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloLooseWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloLooseWithTrigJetMet.cuts.append(cutMaxCaloLoose)


SigRegWithMaxCaloPUCorr = cms.PSet(
    name = cms.string("SigRegWithMaxCaloPUCorr"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloPUCorr.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrNoiseCleaned = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloPUCorrNoiseCleaned"),
    cuts = copy.deepcopy(PreSelectionWithNoiseClean.cuts),
    )
SigRegWithMaxCaloPUCorrNoiseCleaned.cuts.append(cutTrkSumPtLT)
SigRegWithMaxCaloPUCorrNoiseCleaned.cuts.append(cutTrkHitMissOut)
SigRegWithMaxCaloPUCorrNoiseCleaned.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrAndSumPtLessThan = cms.PSet(
    name = cms.string("SigRegWithMaxCaloPUCorrAndSumPtLessThan"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloPUCorrAndSumPtLessThan.cuts.append(cutTrkSumPtLT)
SigRegWithMaxCaloPUCorrAndSumPtLessThan.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloPUCorrWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloPUCorrWithTrigJetMet.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloPUCorAndSumPtLessThanWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet.cuts.append(cutTrkSumPtLT)
SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet.cuts.append(cutMaxCaloPUCorr)


## Control Region Channels ##
CtrlReg = cms.PSet(
    name = cms.string("CtrlReg"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
CtrlReg.cuts.append(cutTrkHitMissOutCtrlReg)


CtrlRegWithTrigJetMet = cms.PSet(
    name = cms.string("CtrlRegWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
CtrlRegWithTrigJetMet.cuts.append(cutTrkHitMissOutCtrlReg)


JetFirst = cms.PSet(
    name = cms.string("JetFirst"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutJetPt,
        cutMET,
        )
    )

MetFirst = cms.PSet(
    name = cms.string("MetFirst"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        )
    )

TrigTestTighterMet = cms.PSet(
    name = cms.string("TrigTestTighterMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.string("mets"),
            cutString = cms.string("pt > 250"),
            numberRequired = cms.string(">= 1"),
            ),
        cutJetPt,
        )
    )

TrigTestTighterJet = cms.PSet(
    name = cms.string("TrigTestTighterJet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cms.PSet (
            inputCollection = cms.string("jets"),
            cutString = cms.string("pt > 180"),
            numberRequired = cms.string(">= 1"),
            ),
        )
    )


JetOnly = cms.PSet(
    name = cms.string("JetOnly"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
       ),
    )

JetOnlyNoClean = cms.PSet(
    name = cms.string("JetOnlyNoClean"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        cutJetEta,
       ),
    )


# Monojet selection #  
MonoJet = cms.PSet(
    name = cms.string("MonoJet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET200,
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
#        cutJetPt,
#        cutJetEta2p4,
#        cutJetNoiseChgHad,
#        cutJetNoiseChgEM,
#        cutJetNoiseNeuEM,
#        cutJetNoiseChgEM,
#        cutLeadingJetID,
        cutSubLeadingJetID,
        cutNJets,
        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
#        cutTrkIso,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
#        cutSecJetNoiseChgHad,
#        cutSecJetNoiseChgEM,
#        cutSecJetNoiseNeuHad,
#        cutSecJetNoiseNeuEM,
#        cutSecJetPt,
#        cutSecJetEta2p4,
#        cutNJets,
#        cutJetJetDPhi,
#        cutMuonVeto,
#        cutElecVeto,
#        cutTauVeto,
       ),
    )

# Modified Monojet selection #  
MonoJetNoNJetVeto = cms.PSet(
    name = cms.string("MonoJetNoNJetVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
#        cutNJets,
        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
#        cutTrkIso,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
       ),
    )

# Modified Monojet selection #  
MonoJetNoSubjetCuts = cms.PSet(
    name = cms.string("MonoJetNoSubjetCuts"),  
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
#        cutNJets,
#        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
#        cutTrkIso,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
       ),
    )


AtlasDisappTrk = cms.PSet(
    # Copy cuts from arXiv:1210.2852v1, JHEP 01 (2013) 131 
    name = cms.string("AtlasDisappTrk"),
    # Do not apply a trigger  
    cuts = cms.VPSet (
        cutMET90,
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSecJetEta2p8,
        cutSecJetPt90,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutJetPt50,
        cutJetEta2p8,
        cutJetVetoDPhiMet,
        cutTrkPt10,
        cutTrkEtaAtlas,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkPtError,
        cutTrkIso,
       ),
    )


