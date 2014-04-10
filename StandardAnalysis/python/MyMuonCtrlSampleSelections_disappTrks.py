
import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.MyCuts_disappTrks import *  # Put all the individual cuts in this file 
from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *  # Get the composite cut definitions  

##################################################
##### Set up the event selections (channels) #####
##################################################


SingleMuTrigTrkPreselNoMuonVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("SingleMuTrigTrkPreselNoMuonVetoMet"),
    triggers = triggersSingleMu,
    cuts = cutsPresel, 
    )
for i in xrange(len(SingleMuTrigTrkPreselNoMuonVetoMet.cuts) - 1, -1, -1):
    if SingleMuTrigTrkPreselNoMuonVetoMet.cuts[i].cutString == cutMuonLooseIDVeto.cutString \
    or SingleMuTrigTrkPreselNoMuonVetoMet.cuts[i].cutString == cutSecMuonLooseIDVeto.cutString \
    or SingleMuTrigTrkPreselNoMuonVetoMet.cuts[i].cutString == cutSecJetPt.cutString: 
        del SingleMuTrigTrkPreselNoMuonVetoMet.cuts[i]
for i in xrange(len(SingleMuTrigTrkPreselNoMuonVetoMet.cuts) - 1, -1, -1):
    if SingleMuTrigTrkPreselNoMuonVetoMet.cuts[i].cutString == cutSubLeadingJetID.cutString:  
        idx = i
SingleMuTrigTrkPreselNoMuonVetoMet.cuts.insert(idx, cutSecJetLeadingPt)  

MonojetTrigTrkPreselNoMuonVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("MonojetTrigTrkPreselNoMuonVetoMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(SingleMuTrigTrkPreselNoMuonVetoMet.cuts)
    )
Jet80TrigTrkPreselNoMuonVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("Jet80TrigTrkPreselNoMuonVetoMet"),
    triggers = cms.vstring("HLT_PFJet80_v"),
    cuts = copy.deepcopy(SingleMuTrigTrkPreselNoMuonVetoMet.cuts)
    )
Monojet80Met95TrigTrkPreselNoMuonVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("Monojet80Met95TrigTrkPreselNoMuonVetoMet"),
    triggers = cms.vstring("HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v"),
    cuts = copy.deepcopy(SingleMuTrigTrkPreselNoMuonVetoMet.cuts)
    )
Met120TrigTrkPreselNoMuonVetoMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("Met120TrigTrkPreselNoMuonVetoMet"),
    triggers = cms.vstring("HLT_MET120_HBHENoiseCleaned_v"),
    cuts = copy.deepcopy(SingleMuTrigTrkPreselNoMuonVetoMet.cuts)
    )

                


SingleMuTrigTrkPreselNoMuonVetoJet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("SingleMuTrigTrkPreselNoMuonVetoJet"),
    triggers = triggersSingleMu,
    cuts = copy.deepcopy(cutsPresel),
    )
for i in xrange(len(SingleMuTrigTrkPreselNoMuonVetoJet.cuts) - 1, -1, -1):
    if SingleMuTrigTrkPreselNoMuonVetoJet.cuts[i].cutString == cutElecLooseIDVeto.cutString or SingleMuTrigTrkPreselNoMuonVetoJet.cuts[i].cutString == cutMET.cutString:
        del SingleMuTrigTrkPreselNoMuonVetoJet.cuts[i]
MonojetTrigTrkPreselNoMuonVetoJet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("MonojetTrigTrkPreselNoMuonVetoJet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(SingleMuTrigTrkPreselNoMuonVetoJet.cuts)
    )
Jet80TrigTrkPreselNoMuonVetoJet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("Jet80TrigTrkPreselNoMuonVetoJet"),
    triggers = triggersJet80,
    cuts = copy.deepcopy(SingleMuTrigTrkPreselNoMuonVetoJet.cuts)
    )

                


SingleMuTrigLeadJet = cms.PSet(
    name = cms.string("SingleMuTrigLeadJet"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
      cutJetEta2p6Filter,
      cutJetNoiseNeuHad95Filter,
      cutJetLeadingPt,
      ),
    )

MonojetTrigLeadJet  = cms.PSet(
    name = cms.string("MonojetTrigLeadJet"),
    triggers = triggersJetMet, 
    cuts = cms.VPSet (
      cutJetEta2p6Filter,
      cutJetNoiseNeuHad95Filter,
      cutJetLeadingPt,
      ),
    )



WToMuNu = cms.PSet(
    name = cms.string("WToMuNu"),
    triggers = triggersSingleMu,
#    triggers = triggersJetMet,
    cuts = cms.VPSet(
##          cutMET,
##          cutJetPt,
         cutEvtFilterScraping,
         cutVtxGood,
         cutMuonEta,
         cutMuonPt25,
         cutMuonTightID,
         cutMuonPFIso,
         cutMuonOneOnly,
         cutMET40,
         cutMuonTrkDRSame, 
         )
    )


## Ctrl sample for muons ##
ZtoMuTrkNoJetMet = cms.PSet(
    name = cms.string("ZtoMuTrkNoJetMet"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
         # See SMP-12-023 for example of W->mu nu selection
         cutMuonPt20,
         cutMuonEta,
         cutMuonTightID,
         cutMuonPFIso,
    #     cutMuonPlusMet220,
     #    cutSecJetPt,
     #    cutSecJetEta2p4,
     #    cutSecJetNoiseChgHad,
     #    cutSecJetNoiseChgEM,
     #    cutSecJetNoiseNeuHad,
     #    cutSecJetNoiseNeuEM,
     #    cutSubLeadingJetID,
     #    cutJetJetDPhi,
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
#         cutMuonLooseIDOnlyOne,
         #        cutSecMuonLooseIDOnlyOne,  # Leave this out for now
#         cutMuonLooseIDVeto,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )

ZtoMuTrkNoJetMetInv = cms.PSet(
    name = cms.string("ZtoMuTrkNoJetMetInv"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
         # See SMP-12-023 for example of W->mu nu selection
         cutMuonPt20,
         cutMuonEta,
         cutMuonTightID,
         cutMuonPFIso,
         #     cutMuonPlusMet220,
         #    cutSecJetPt,
         #    cutSecJetEta2p4,
         #    cutSecJetNoiseChgHad,
         #    cutSecJetNoiseChgEM,
         #    cutSecJetNoiseNeuHad,
         #    cutSecJetNoiseNeuEM,
         #    cutSubLeadingJetID,
         #    cutJetJetDPhi,
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
         #cutMuonLooseIDOnlyOne,
         cutTauLooseHadronicVeto,
         cutMuonLooseIDVetoInv,
         cutMuTrkDeltaR,
         cutMuTrkInvMass,
         ),
    )


SigRegMuTrigMuId = cms.PSet(
    name = cms.string("SigRegMuTrigMuId"),
    triggers = triggersSingleMu, 
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
      cutSubLeadingJetID,
      cutJetJetDPhi,
      cutElecLooseIDVeto,
##       cutMuonLooseIDVeto,
##       cutSecMuonLooseIDVeto,
      cutTauLooseHadronicVeto,
      cutTrkHitMissOut,
      cutMaxCaloPUCorr,
      ),
    )


MuTrigMuId = cms.PSet(
    name = cms.string("MuTrigMuId"),
    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
      cutTrkMuonId,
      cutTrkPt,
      cutTrkEta,
      cutTrkHitMissOut,
      ),
    )




ZtoMuMu = cms.PSet(
    # Get this example from http://cmssw.cvs.cern.ch/cgi-bin/cmssw.cgi/UserCode/OSUT3Analysis/AnaTools/python/MyEventSelections.py?revision=1.2&view=markup  
    name = cms.string("ZtoMuMu"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
         cutMuonPairPt25,
         cutMuonPairEta,
         cutMuonPairTightID,
         cutMuonPairPFIso,
         cutMuonPairD0,
         cutMuonPairDZ,
#         cutElecVeto,
         cutMuMuChargeProduct,
         cutMuMuInvMass,
#         cutMuTrkDeltaRSame,  # apply this so that selected tracks are associated with muons  
         )
    )   


ZtoMuMuFakeTrk = cms.PSet(
    name = cms.string("ZtoMuMuFakeTrk"),
    triggers = triggersSingleMu,
    cuts = copy.deepcopy(ZtoMuMu.cuts),
    )
ZtoMuMuFakeTrk.cuts = ZtoMuMuFakeTrk.cuts + cutsTrkPresel + cutsSigReg 

ZtoMuMuFakeTrkPreSel = cms.PSet(
    name = cms.string("ZtoMuMuFakeTrkPreSel"),
    triggers = triggersSingleMu,
    cuts = copy.deepcopy(ZtoMuMu.cuts),
    )
ZtoMuMuFakeTrkPreSel.cuts = ZtoMuMuFakeTrkPreSel.cuts + cutsTrkPresel 

ZtoMuMuFakeTrkPreSelCtrlPt30 = cms.PSet(
    name = cms.string("ZtoMuMuFakeTrkPreSelCtrlPt30"),
    triggers = triggersSingleMu,
    cuts = copy.deepcopy(ZtoMuMu.cuts) + copy.deepcopy(cutsTrkPresel), 
    )
#ZtoMuMuFakeTrkPreSelCtrlPt30.cuts = ZtoMuMuFakeTrkPreSelCtrlPt30.cuts + copy.deepcopy(cutsTrkPresel)  
for i in xrange(len(ZtoMuMuFakeTrkPreSelCtrlPt30.cuts) - 1, -1, -1):
    if ZtoMuMuFakeTrkPreSelCtrlPt30.cuts[i].cutString == cutTrkPt.cutString:
        ZtoMuMuFakeTrkPreSelCtrlPt30.cuts[i].cutString = cutTrkPt30.cutString
                
ZtoMuMuFakeTrkPreSelCtrlNMiss = cms.PSet(
    name = cms.string("ZtoMuMuFakeTrkPreSelCtrlNMiss"),
    triggers = triggersSingleMu,
    cuts = copy.deepcopy(ZtoMuMu.cuts),
    )
ZtoMuMuFakeTrkPreSelCtrlNMiss.cuts = ZtoMuMuFakeTrkPreSelCtrlNMiss.cuts + cutsTrkPreselCtrlNMiss  

ZtoMuMuFakeTrkPreSelCtrlEcalo = cms.PSet(
    name = cms.string("ZtoMuMuFakeTrkPreSelCtrlEcalo"),
    triggers = triggersSingleMu,
    cuts = copy.deepcopy(ZtoMuMu.cuts),
    )
ZtoMuMuFakeTrkPreSelCtrlEcalo.cuts = ZtoMuMuFakeTrkPreSelCtrlEcalo.cuts + cutsTrkPreselCtrlEcalo  

ZtoMuMuFakeTrkNHits4 = cms.PSet(
    name = cms.string("ZtoMuMuFakeTrkNHits4"),
    triggers = triggersSingleMu,
    cuts = copy.deepcopy(ZtoMuMuFakeTrk.cuts), 
    )
for i in xrange(len(ZtoMuMuFakeTrkNHits4.cuts) - 1, -1, -1):
    if ZtoMuMuFakeTrkNHits4.cuts[i].cutString == cutTrkNHits.cutString:
        ZtoMuMuFakeTrkNHits4.cuts[i].cutString = cutTrkNHits4.cutString  

ZtoMuMuFakeTrkNHits4NoEcalo = copy.deepcopy(ZtoMuMuFakeTrkNHits4) 
ZtoMuMuFakeTrkNHits4NoEcalo.name = cms.string("ZtoMuMuFakeTrkNHits4NoEcalo")  
for i in xrange(len(ZtoMuMuFakeTrkNHits4NoEcalo.cuts) - 1, -1, -1):  
    if ZtoMuMuFakeTrkNHits4NoEcalo.cuts[i].cutString == cutMaxCalo10.cutString:  
        del ZtoMuMuFakeTrkNHits4NoEcalo.cuts[i]



WtoMuNuTrackFullPreSel = cms.PSet(
    name = cms.string("WtoMuNuTrackFullPreSel"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet(
         cutMuonPt20,
         cutMuonEta,
         cutMuonTightID,
         cutMuonPFIso,
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
         cutElecVetoPt10,   
#         cutMET30,
##          cutJetPt30Filter,
##          cutJetEta2p4Filter,
##          cutJetIDLooseFilter,
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
        cutElecVetoPt10,   
        cutMET30,
    )
)

