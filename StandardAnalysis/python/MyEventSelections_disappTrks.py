import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.MyCuts_disappTrks import *  # Put all the individual cuts in this file 
################################################
##### List of cut VPSets                   #####
################################################


cutsMET = cms.VPSet (
        cutMET,
)

cutsJets = cms.VPSet (
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
)

cutsTrkPtEta = cms.VPSet (
    cutTrkPt,
    cutTrkEta,
    )

cutsTrkQuality = cms.VPSet (
    cutTrkD0,
    cutTrkDZ,
    cutTrkNHits,
    cutTrkHitMissMid,
    cutTrkHitMissIn,
    )

cutsTrkIso = cms.VPSet (
    cutTrkRelIsoRp3,  
    cutTrkJetDeltaR,
    )

cutsTrkVetoRegions = cms.VPSet (
    cutTrkDeadEcalVeto,
    cutTrkCrackVeto,
    cutTrkWheel0GapVeto, 
    cutTrkEtaMuonPk, 
    cutTrkBadCSCVeto, 
    )

cutsTrkLeptonVeto = cms.VPSet (
    cutTauLooseHadronicVeto,  
    cutElecLooseIDVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto, 
    )

cutsTrkPresel = \
  cutsTrkPtEta + \
  cutsTrkVetoRegions + \
  cutsTrkQuality + \
  cutsTrkIso + \
  cutsTrkLeptonVeto 

cutsTrkPreselNoLepVeto = \
  cutsTrkPtEta + \
  cutsTrkVetoRegions + \
  cutsTrkQuality + \
  cutsTrkIso 

cutsPresel = \
  cutsMET + \
  cutsJets + \
  cutsTrkPresel 

cutsSigReg = cms.VPSet (
    cutMaxCalo10, 
    cutTrkHitMissOut,
    )

cutsTagMuon = cms.VPSet (
    # See SMP-12-023 for example of W->mu nu selection  
    cutMuonPt25,
    cutMuonEta,
    cutMuonTightID,
    cutMuonPFIso,
    cutMuonD0,
    cutMuonDZ,
    cutMuonValidHits,
    )

cutsMuTrkZPeak = cms.VPSet (
    cutMuTrkInvMass80To100,
    cutMuTrkChgOpp,
    ) 
    

################################################
##### List of  event selections (channels) #####
################################################

NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    cuts = cms.VPSet (
       cutNoCuts,
       ),
    )

DebugCuts = cms.PSet(
    name = cms.string("DebugCuts"),
    cuts = cms.VPSet (
       cms.PSet(
          inputCollection = cms.string("tracks"),
          cutString = cms.string("isMatchedBadCSC == 1"),
          numberRequired = cms.string(">= 1"),
          ),
       )
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

TriggerMetNoMu = cms.PSet(
    name = cms.string("TriggerMetNoMu"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMETNoMu,
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

FullSelection = cms.PSet(
    name = cms.string("FullSelection"),
    triggers = triggersJetMet,
    cuts =
    cutsPresel +
    cutsSigReg, 
    )


PreSelection = cms.PSet(
    name = cms.string("PreSelection"),
    triggers = triggersJetMet,
    cuts = cutsPresel, 
    )

FullSelectionIdMuon = cms.PSet(
    name = cms.string("FullSelectionIdMuon"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cms.VPSet ( cutTrkMuonId ) + 
    cutsTrkPresel + 
    cutsSigReg
    )



FullSelectionMuPreveto = cms.PSet(
    name = cms.string("FullSelectionMuPreveto"),
    triggers = triggersJetMet,
    cuts = 
    cms.VPSet ( cutMETNoMu ) + 
    cutsJets + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet ( cutTauLooseHadronicVeto, cutElecLooseIDVeto ) +  
    cutsSigReg, 
    )



StudyMuVeto = cms.PSet(
    name = cms.string("StudyMuVeto"),
#    triggers = triggersJetMet,
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
##         cutTrkMuonId,
##         cutMuonLooseIDVeto,
##         cutMET, 
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt50,
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
        cutTauLooseHadronicVeto,
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )

StudyMuVeto2 = cms.PSet(
    name = cms.string("StudyMuVeto2"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutTrkMuonId,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt50,
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
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVeto,
        cutMET, 
        ),
    )

PreSelInvMuonVeto = cms.PSet(
    name = cms.string("PreSelInvMuonVeto"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto, 
      cutMuonLooseIDVetoInv
      ), 
    )

PreSelNoTauVeto = cms.PSet(
    name = cms.string("PreSelNoTauVeto"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutElecLooseIDVeto,
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto
      ), 
    )

PreSelNoLepVeto = cms.PSet(
    name = cms.string("PreSelNoLepVeto"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto, 
    )

PreSelInvElecVeto = cms.PSet(
    name = cms.string("PreSelectionInvElecVeto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
for cut in PreSelInvElecVeto.cuts:
    if cut.cutString == cutElecLooseIDVeto.cutString:
        cut.cutString = cutElecLooseIDVetoInv.cutString


PreSelInvTauVeto = cms.PSet(
    name = cms.string("PreSelectionInvTauVeto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
for cut in PreSelInvTauVeto.cuts:
    if cut.cutString == cutTauLooseHadronicVeto.cutString:
        cut.cutString = cutTauLooseHadronicVetoInv.cutString


PreSelElecVetoEnd = cms.PSet(
    name = cms.string("PreSelElecVetoEnd"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutTauLooseHadronicVeto, 
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto, 
      cutElecLooseIDVeto,
      ), 
    )

PreSelMuonVetoEnd = cms.PSet(
    name = cms.string("PreSelMuonVetoEnd"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts), 
    )

PreSelTauVetoEnd = cms.PSet(
    name = cms.string("PreSelTauVetoEnd"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto, 
      cutElecLooseIDVeto,
      cutTauLooseHadronicVeto, 
      ), 
    )  

PreSelElecVetoEndInv = cms.PSet(
    name = cms.string("PreSelElecVetoEndInv"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelElecVetoEnd.cuts), 
    )
for cut in PreSelElecVetoEndInv.cuts:
    if cut.cutString == cutElecLooseIDVeto.cutString:
        cut.cutString = cutElecLooseIDVetoInv.cutString
                

PreSelMuonVetoEndInv = cms.PSet(
    name = cms.string("PreSelMuonVetoEndInv"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelInvMuonVeto.cuts),  
    )

PreSelTauVetoEndInv = cms.PSet(
    name = cms.string("PreSelTauVetoEndInv"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelTauVetoEnd.cuts),  
    )
for cut in PreSelTauVetoEndInv.cuts:
    if cut.cutString == cutTauLooseHadronicVeto.cutString:
        cut.cutString = cutTauLooseHadronicVetoInv.cutString  


ZtoMuTrk = cms.PSet(
    name = cms.string("ZtoMuTrk"),
    triggers = triggersJetMet,
    cuts =
    cutsTagMuon +
    cms.VPSet (cutMuonPlusMet220) +
    cutsJets + 
    cutsTrkPresel + 
    cms.VPSet (
      cutMuTrkDeltaR,
      cutMuTrkInvMass,
      )
    )


ZtoMuTrkMuIdNoTrigMet = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdNoTrigMet"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
#        cutMET,
#        cutMETNoMu,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutMuonDZ,
        cutMuonValidHits,
#        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        cutTrkPt,
        cutTrkEta,
#       cutTrkEtaBarrel,
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
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )

ZtoMuTrkMuIdNoVeto = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdNoVeto"),
#    triggers = triggersJetMetOrSingleMu, 
#    triggers = triggersJetMet,
     triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon + 
#    cms.VPSet ( cutTrkMuonId ) + 
    cutsTrkPresel + 
    cms.VPSet (
      cutMaxCalo10,
#      cutTrkHitMissOut,
      ) + 
    cutsMuTrkZPeak
    )


ZtoMuTrkMuId = cms.PSet(
    name = cms.string("ZtoMuTrkMuId"),
#    triggers = triggersJetMetOrSingleMu, 
#    triggers = triggersJetMet,
     triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon +
    cutsTrkPresel +
    cms.VPSet (
      cutMaxCalo10,
      #      cutTrkHitMissOut,
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto,
      ) + 
    cutsMuTrkZPeak
    )



ZtoMuTrkMuIdHiStats = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdHiStats"),
#    triggers = triggersJetMetOrSingleMu, 
     triggers = triggersJetMet,
#    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
#       cutMETNoMu,
       cutMET,
#       cutMuonChgNeg,
#       cutMuonChgPos,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutMuonDZ,
        cutMuonValidHits,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
#       cutTrkMuonId, 
        cutTrkPt50,
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
        cutTauLooseHadronicVeto,
        cutTrkWheel0GapVeto,
        cutTrkEtaMuonPk,
        cutMaxCalo10, 
#        cutMuTrkInvMass,
        cutMuTrkInvMass80To100, 
        cutMuTrkChgOpp, 
        cutMuTrkDeltaR,
        cutTrkHitMissOut,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )

ZtoMuTrkMuIdInvHits = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdInvHits"),
#    triggers = triggersJetMetOrSingleMu, 
     triggers = triggersJetMet,
#    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
        cutMET,
#       cutMETNoMu,
#       cutMuonChgNeg,
#       cutMuonChgPos,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonD0,
        cutMuonDZ,
        cutMuonValidHits,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        cutMuTrkChgOpp, 
        cutTrkPt50,
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
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTrkWheel0GapVeto,
        cutTrkEtaMuonPk,
        cutMaxCalo10, 
        cutTrkHitMissOutInv,
        ),
    )

## ZtoMuTrkMuId = copy.deepcopy(ZtoMuTrkMuIdNoVeto)  
## ZtoMuTrkMuId.name = "ZtoMuTrkMuId"  
## ZtoMuTrkMuId.cuts.append(cutMuonLooseIDVeto)
## ZtoMuTrkMuId.cuts.append(cutSecMuonLooseIDVeto)


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
#       cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVetoInv,
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        ),
    )


FakeTrackSel = cms.PSet(
    name = cms.string("FakeTrackSel"),
#    triggers = triggersJetMetOrSingleMu, 
#    triggers = triggersJetMet,
#    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
##         cutMETNoMu,
##         cutMET,
#       cutMuonChgNeg,
#       cutMuonChgPos,
##         cutMuonPt20,
##         cutMuonEta,
##         cutMuonTightID,
##         cutMuonPFIso,
##         cutMuonD0,
##         cutMuonDZ,
##         cutMuonValidHits,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkNotGenMatched,
        cutTrkPt50,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
#       cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkWheel0GapVeto,
        cutTrkEtaMuonPk,
        cutMaxCalo10, 
        cutTrkHitMissOut,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
##         cutMETNoMu,
##         cutMET,
        ),
    )


FullSelectionInvD0 = cms.PSet(
    name = cms.string("FullSelectionInvD0"),
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
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0Loose = cms.PSet(
    name = cms.string("FullSelectionInvD0Loose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET100,
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
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZ = cms.PSet(
    name = cms.string("FullSelectionInvDZ"),
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
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZLoose = cms.PSet(
    name = cms.string("FullSelectionInvDZLoose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET100,
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
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvNHits = cms.PSet(
    name = cms.string("FullSelectionInvNHits"),
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
        cutTrkNHits4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvNHitsLoose = cms.PSet(
    name = cms.string("FullSelectionInvNHitsLoose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET100,
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
        cutTrkNHits4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvNMissMid"),
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
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvNMissMidLoose = cms.PSet(
    name = cms.string("FullSelectionInvNMissMidLoose"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET100,
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
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvNoneLoose = cms.PSet(
    name = cms.string("FullSelectionInvNoneLoose"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET100,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
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
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvDZ = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZ"),
    triggers = triggersJetMet,
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
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvNHits = cms.PSet(
    name = cms.string("FullSelectionInvD0InvNHits"),
    triggers = triggersJetMet,
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
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHitsInv,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvNMissMid"),
    triggers = triggersJetMet,
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
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZInvNHits = cms.PSet(
    name = cms.string("FullSelectionInvDZInvNHits"),
    triggers = triggersJetMet,
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
        cutTrkDZInv,
        cutTrkNHitsInv,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvDZInvNMissMid"),
    triggers = triggersJetMet,
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
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvNHitsInvNMissMid"),
    triggers = triggersJetMet,
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
        cutTrkNHitsInv,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)

FullSelectionInvD0InvDZInvNHits = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZInvNHits"),
    triggers = triggersJetMet,
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
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHitsInv,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvD0InvDZInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZInvNMissMid"),
    triggers = triggersJetMet,
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
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvNHitsInvNMissMid"),
    triggers = triggersJetMet,
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
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHitsInv,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvDZInvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvDZInvNHitsInvNMissMid"),
    triggers = triggersJetMet,
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
        cutTrkDZInv,
        cutTrkNHitsInv,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvDZInvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZInvNHitsInvNMissMid"),
    triggers = triggersJetMet,
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
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHitsInv,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionFakeTrk = cms.PSet(
    name = cms.string("FullSelectionFakeTrk"),
    triggers = triggersJetMet,
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
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
        cutTrkNotGenMatched,  
    )
)



MuTrigNoCuts = cms.PSet(
    name = cms.string("MuTrigNoCuts"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
       cutNoCuts,
       )
    )

FakeTrkMuTrig = cms.PSet(
    name = cms.string("FakeTrkMuTrig"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
#        cutMET,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
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
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
        cutTrkNotGenMatched,  
    )
)


FullSelectionNoTrkCuts = cms.PSet(
    name = cms.string("FullSelectionNoTrkCuts"),
    triggers = triggersJetMet,
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
    )
)


FakeTrkTestCorr = cms.PSet(
    name = cms.string("FakeTrkTestCorr"),
    triggers = triggersJetMet,
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
#        cutTrkD0,
#        cutTrkDZ,
#        cutTrkNHits,
#        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FakeTrkTestCorrLoose = cms.PSet(
    name = cms.string("FakeTrkTestCorrLoose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
#        cutTrkD0,
#        cutTrkDZ,
#        cutTrkNHits,
#        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionFakeTrkCtrlInv = cms.PSet(
    name = cms.string("FullSelectionFakeTrkCtrlInv"),
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
#       cutTrkD0Inv,
        cutTrkDZ,
#       cutTrkDZInv,
#       cutTrkNHits,
        cutTrkNHits4,
#        cutTrkHitMissMid,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionFakeTrkCtrlNom = cms.PSet(
    name = cms.string("FullSelectionFakeTrkCtrlNom"),
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
#       cutTrkD0Inv,
        cutTrkDZ,
#       cutTrkDZInv,
#       cutTrkNHits,
        cutTrkNHits4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
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


PreSelIdMuonNoVeto = cms.PSet(
    name = cms.string("PreSelIdMuonNoVeto"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET,
##         cutMETNoMu,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkMuonId, 
#       cutMET,
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
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMaxCalo10, 
##         cutTrkHitMissOut,
    )
)

PreSelIdMuon = copy.deepcopy(PreSelIdMuonNoVeto)
PreSelIdMuon.name = "PreSelIdMuon"
PreSelIdMuon.cuts.append(cutMuonLooseIDVeto)
PreSelIdMuon.cuts.append(cutSecMuonLooseIDVeto)  

PreSelIdMuonInvHits = cms.PSet(
    name = cms.string("PreSelIdMuonInvHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
#        cutMETNoMu,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
#       cutTrkMuonId, 
#       cutTrkPt,
        cutTrkPt50,
        cutTrkEta,
#       cutTrkEtaBarrel,
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
        cutTauLooseHadronicVeto,  
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMaxCalo10, 
        cutTrkHitMissOutInv,
    )
)

SimpleIdMuon = cms.PSet(
    name = cms.string("SimpleIdMuon"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutTrkMuonId, 
#        cutTrkPt,
        cutTrkPt50,
#       cutTrkPt75,
        cutTrkEta,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        )
    )


PreSelIdMuonNoMetJetNoVeto = cms.PSet(
    name = cms.string("PreSelIdMuonNoMetJetNoVeto"),
    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
##         cutMET,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutTrkPt,
        cutTrkEta,
#       cutTrkEtaBarrel,
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
        cutTauLooseHadronicVeto,    
    )
)

PreSelIdMuonNoMetJet = copy.deepcopy(PreSelIdMuonNoMetJetNoVeto)  
PreSelIdMuonNoMetJet.name = "PreSelIdMuonNoMetJet"  
PreSelIdMuonNoMetJet.cuts.append(cutMuonLooseIDVeto)  
PreSelIdMuonNoMetJet.cuts.append(cutSecMuonLooseIDVeto)  



SigRegIdMuon = cms.PSet(
    name = cms.string("SigRegIdMuon"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutTrkMuonId, 
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
        cutTauLooseHadronicVeto,    
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkHitMissOut,
        cutMaxCaloPUCorr,
##         cutMuonLooseIDVeto,
##         cutSecMuonLooseIDVeto,
    )
)


PreSelPMissInvVetoIdMuon = cms.PSet(
    name = cms.string("PreSelPMissInvVetoIdMuon"),
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
        cutTrkMuonId, 
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
        cutTauLooseHadronicVeto,    
        cutTrkHitMissOut,
        cutMaxCaloPUCorr,
        cutMuonLooseIDVetoInv,
    )
)

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

PreSelWithMaxCalo = cms.PSet(
    name = cms.string("PreSelWithMaxCalo"),
    cuts = copy.deepcopy(PreSelection.cuts),
)
PreSelWithMaxCalo.cuts.append(cutMaxCaloTight) 
#PreSelWithMaxCalo.cuts.append(cutMaxMissOut)  # for data only


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


SigRegNominal = cms.PSet(
    name = cms.string("SigRegNominal"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegNominal.cuts.append(cutMaxCalo10) 
SigRegNominal.cuts.append(cutTrkWheel0GapVeto) 
SigRegNominal.cuts.append(cutTrkEtaMuonPk)  

SigRegWithMaxCaloPUCorr = cms.PSet(
    name = cms.string("SigRegWithMaxCaloPUCorr"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloPUCorr.cuts.append(cutMaxCalo10)

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


