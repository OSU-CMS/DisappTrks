import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *  # Get the composite cut definitions

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

SingleElecTrigLeadJet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("SingleElecTrigLeadJet"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet(
##       cutJetEta2p6Filter,
##       cutJetNoiseNeuHad95Filter, 
      cutJetLeadingPt,   
      )
    ) 

Monojet80Met95TrigLeadJet = cms.PSet(  # Use for Monojet trigger efficiency (run on skims that have passed SingleElec trigger)  
    name = cms.string("Monojet80Met95TrigLeadJet"),
#    triggers = triggersJetMet,  
    triggers = cms.vstring("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v"),   
    cuts = cms.VPSet(
##       cutJetEta2p6Filter,
##       cutJetNoiseNeuHad95Filter, 
      cutJetLeadingPt,   
# Testing:
##       cms.PSet (
##         inputCollection = cms.string("jets"),
##         cutString = cms.string("pt < 50"),
##         numberRequired = cms.string(">= 1"),
##         ), 
      )
    ) 

Jet80TrigLeadJet = cms.PSet(  # Use for Monojet trigger efficiency (run on skims that have passed SingleElec trigger)  
    name = cms.string("Jet80TrigLeadJet"),
    triggers = triggersJet80, 
    cuts = cms.VPSet(
      cutJetEta5Filter,
      cutJetLeadingPt,   
      )
    ) 



SingleElecTrigTrkPreselNoElecVeto = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("SingleElecTrigTrkPreselNoElecVeto"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet(
      cutJetEta2p6Filter,
      cutJetNoiseNeuHad95Filter, 
      cutJetLeadingPt,
      ) + cutsTrkPresel, 
    ) 
for i in xrange(len(SingleElecTrigTrkPreselNoElecVeto.cuts) - 1, -1, -1):
    if SingleElecTrigTrkPreselNoElecVeto.cuts[i].cutString == cutElecLooseIDVeto.cutString:
        del SingleElecTrigTrkPreselNoElecVeto.cuts[i]
                
MonojetTrigTrkPreselNoElecVeto = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("MonojetTrigTrkPreselNoElecVeto"),
    triggers = triggersJetMet, 
    cuts = copy.deepcopy(SingleElecTrigTrkPreselNoElecVeto.cuts)
    ) 

SingleElecTrigTrkPreselNoElecVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("SingleElecTrigTrkPreselNoElecVetoMet"),
    triggers = triggersSingleElec, 
##     cuts = cms.VPSet(
##       cutJetEta2p6Filter,
##       cutJetNoiseNeuHad95Filter, 
##       cutJetLeadingPt,
##       cutMET,
##       ) + cutsTrkPresel, 
    cuts = cutsPresel,
    ) 
for i in xrange(len(SingleElecTrigTrkPreselNoElecVetoMet.cuts) - 1, -1, -1):
    if SingleElecTrigTrkPreselNoElecVetoMet.cuts[i].cutString == cutElecLooseIDVeto.cutString \
    or SingleElecTrigTrkPreselNoElecVetoMet.cuts[i].cutString == cutSecJetPt.cutString:
        del SingleElecTrigTrkPreselNoElecVetoMet.cuts[i]
for i in xrange(len(SingleElecTrigTrkPreselNoElecVetoMet.cuts) - 1, -1, -1):
    if SingleElecTrigTrkPreselNoElecVetoMet.cuts[i].cutString == cutSubLeadingJetID.cutString:
        idx = i
SingleElecTrigTrkPreselNoElecVetoMet.cuts.insert(idx, cutSecJetLeadingPt)
                
MonojetTrigTrkPreselNoElecVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("MonojetTrigTrkPreselNoElecVetoMet"),
    triggers = triggersJetMet, 
    cuts = copy.deepcopy(SingleElecTrigTrkPreselNoElecVetoMet.cuts)
    ) 
Jet80TrigTrkPreselNoElecVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("Jet80TrigTrkPreselNoElecVetoMet"),
    triggers = cms.vstring("HLT_PFJet80_v"), 
    cuts = copy.deepcopy(SingleElecTrigTrkPreselNoElecVetoMet.cuts)
    ) 
Monojet80Met95TrigTrkPreselNoElecVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("Monojet80Met95TrigTrkPreselNoElecVetoMet"),
    triggers = cms.vstring("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v"), 
    cuts = copy.deepcopy(SingleElecTrigTrkPreselNoElecVetoMet.cuts)
    ) 
Met120TrigTrkPreselNoElecVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("Met120TrigTrkPreselNoElecVetoMet"),
    triggers = cms.vstring("HLT_MET120_HBHENoiseCleaned_v"), 
    cuts = copy.deepcopy(SingleElecTrigTrkPreselNoElecVetoMet.cuts)
    ) 



SingleElecTrigTrkPreselNoElecVetoJet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("SingleElecTrigTrkPreselNoElecVetoJet"),
    triggers = triggersSingleElec, 
    cuts = copy.deepcopy(cutsPresel), 
    ) 
for i in xrange(len(SingleElecTrigTrkPreselNoElecVetoJet.cuts) - 1, -1, -1):  
    if SingleElecTrigTrkPreselNoElecVetoJet.cuts[i].cutString == cutElecLooseIDVeto.cutString \
    or SingleElecTrigTrkPreselNoElecVetoJet.cuts[i].cutString == cutMET.cutString:
        del SingleElecTrigTrkPreselNoElecVetoJet.cuts[i]
MonojetTrigTrkPreselNoElecVetoJet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("MonojetTrigTrkPreselNoElecVetoJet"),
    triggers = triggersJetMet, 
    cuts = copy.deepcopy(SingleElecTrigTrkPreselNoElecVetoJet.cuts)  
    ) 
Jet80TrigTrkPreselNoElecVetoJet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("Jet80TrigTrkPreselNoElecVetoJet"),
    triggers = triggersJet80, 
    cuts = copy.deepcopy(SingleElecTrigTrkPreselNoElecVetoJet.cuts)  
    ) 


ZtoEE = cms.PSet(
     name = cms.string("ZtoEE"),
     triggers = triggersSingleElec, 
     cuts = cms.VPSet(
         cut2ElecPt,     
         cut2ElecEta,    
         cut2ElecMva,    
         cut2ElecPFIso,
         cut2ElecD0,     
         cut2ElecDZ,     
         cut2ElecPassConvVeto,
         cut2ElecLostHits,
         cutElecElecChargeProduct,
         cutElecElecMass,        
         )
     ) 


## Bkgd estimate ctrl sample ##
ZtoETrk = cms.PSet(
    name = cms.string("ZtoETrk"),
    triggers = triggersSingleElec, 
    cuts = cms.VPSet (
    # Follow the recommended electron Triggering MVA criteria from:  https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
        cutElecPt,     
        cutElecEta,    
        cutElecMva, 
        cutElecPFIso, 
        cutElecLostHits,
        cutElecPassConvVeto, 
        cutMETNoElec, 
        cutSecJetPt,
        cutSecJetEta2p4,
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkElectronId,  
        cutElecTrkDR, 
        cutElecTrkInvMass,
        cutElecTrkChgOpp,
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
        cutTrkWheel0GapVeto,
        cutTrkEtaMuonPk,
        cutTrkHitMissOut,
        cutMaxCalo10,
        cutElecLooseIDVeto,
       ),
    )




## Try different trigger  ##  
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
ZtoETrkEIdOld = cms.PSet(
    name = cms.string("ZtoETrkEIdOld"),
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
        ## cutJetPt30Filter,
        ## cutJetEta2p4Filter,
        ## cutJetIDLooseFilter,
        )
    )


