import FWCore.ParameterSet.Config as cms
import copy

###########################################################
##### Set up the event selections (channels) #####
###########################################################

##### List of valid input collections #####   
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters


# Define cuts first  

## # FIXME:  Need to figure out why no events seem to pass these triggers.  
triggersSingleElec = cms.vstring(
     # Choose triggers by going to http://j2eeps.cern.ch/cms-project-confdb-hltdev/browser/
     # Select online/2012/8e33/v2.1.
     # Take all the single electron triggers than are unprescaled and do not have extra strange requirements.
##      "HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_PFMET20_v",
##      "HLT_Ele24_WP80_CentralPFJet35_CentralPFJet25_v",
##      "HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_CentralPFJet30_v",
##      "HLT_Ele24_WP80_PFJet30_PFJet25_Deta3_v",
##      "HLT_Ele25_CaloIdVT_CaloIsoT_TrkIdT_TrkIsoT_CentralPFNoPUJet30_BTagIPIter_v",
##      "HLT_Ele27_WP80_CentralPFJet80_v",
##      "HLT_Ele27_WP80_PFMET_MT50_v",
##     "HLT_Ele27_WP80_WCandPt80_v",
     "HLT_Ele27_WP80_v",
     )
triggersJetMet = cms.vstring(
    "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
    "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
    "HLT_MET120_HBHENoiseCleaned_v"
    )


cutEvtFilterScraping = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("FilterOutScraping > 0"),
    numberRequired = cms.string(">= 1"),
    )


cutVtxGood = cms.PSet (
    inputCollection = cms.string("primaryvertexs"),
    cutString = cms.string("isGood > 0"),
    numberRequired = cms.string(">= 1"),
    )


cutMET40 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    )
cutMET = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 220"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("MET > 220 Gev")
    )


cutJetPt = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("jet pT > 110 GeV")
    )


cut2ElecPt = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2"),
    )
cutElecPt = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("electron pt > 20 GeV")
    )
cutElecPt40 = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    )
cut2ElecEta = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 2"),
    #alias =cms.string("$|\eta|$ < 2.1")
    )
cutElecEta = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("$|\eta|$ < 2.1")
    )
cut2ElecD0 = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
    numberRequired = cms.string(">= 2"),
    #alias =cms.string("$|d_{0}|$ < 0.05 cm")
    )
cutElecD0 = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("$|d_{0}|$ < 0.05 cm")
    )
cut2ElecDZ = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedDZ) < 0.01"),
    numberRequired = cms.string(">= 2"),
    #alias =cms.string("$|d_{z}|$ < 0.05 cm")
    )
cutElecDZ = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedDZ) < 0.01"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("$|d_{z}|$ < 0.05 cm")
    )
cut2ElecNHits = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 2"),
    #alias =cms.string("Valid Hits > 4")
    )
cutElecNHits = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("Valid Hits > 4")
    )
cutElecMva = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("mvaNonTrigV0 > 0.9"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("(e) mvaNonTrigV0 > 0.9")
    )
cutElecPFIso = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("relPFrhoIso < 0.1"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("(e) Electron Iso  < 0.1")
    )
cutElecTightID = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("tightID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutElecVetoOneMax =   cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 1"),  # Require no more than one electron in event (since one elec is already selected).  
    #alias = cms.string("Electrons = 1")
    )
cutElecVetoAll =   cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),  # Require no electron in event.  
    #alias = cms.string("Electrons = 0")
    )


cutTrkPt = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("(t) pt > 20 GeV")
    )
cutTrkEta = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("(t) $|\eta|$ < 2.1")
    )
cutTrkD0 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) < 0.01"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("(t) $|d_{0}|$ < 0.01 cm")
    )
cutTrkDZ = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(dZwrtPV) < 0.01"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("(t) $|d_{z}|$ < 0.01 cm")
    )
cutTrkNHits = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    #alias =cms.string("(t) Valid Hits > 4")
    ) 
cutTrkHitMissMid = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingMiddle == 0"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("Missing Middle Hits = 0")
    )
cutTrkHitMissIn = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingInner == 0"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("Missing Inner Hits = 0")
    )  
cutTrkIso = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isIso == 1"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("Track Isolation")
    )
cutTrkDeadEcalVeto =  cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isMatchedDeadEcal == 0"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("deadEcal Veto")
    )
cutTrkCrackVeto = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("Crack Veto")
    )   


cutMuonVeto = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    #alias = cms.string("Muons = 0")
    )


cutElecElecMass = cms.PSet (
    inputCollection = cms.string("electron-electron pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("40 < InvMass(e+e) < 160")
    )


cutElecTrkDR = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR > 0.15"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("deltaRETrack > 0.15")
    )
cutElecTrkInvMass = cms.PSet(
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("40 < InvMass(e+t) < 160")
    )




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



