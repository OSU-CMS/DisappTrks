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


#### List of cuts first ####

cutMuonVeto = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    # alias = cms.string("Muon Veto")
    )
cutElecVeto = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    # alias = cms.string("Electron Veto")
    )
cutDeadEcal = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isMatchedDeadEcal == 0"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("deadEcal Veto")
    )
cutCrackVeto = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Crack Veto")
    )

#Standard PreSelection Cuts with the Trigger, Jet pT, and MET cuts applied
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






#### List of channels #####


NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.string("tracks"),
            cutString = cms.string("pt > -1"),
            numberRequired = cms.string(">= 0"),
            ),    
        ),
)




#Standard Preselection Cuts, with no trigger.  
PreSelectionIsoTrkOnly = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$p_T$ > 20 GeV")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|eta|$ < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|d_{0}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|d_{z}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("numValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Valid Hits > 4")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingMiddle == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Middle Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingInner == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Inner Hits = 0")
        ),
#    cms.PSet (
#        inputCollection = cms.string("tracks"),
#        cutString = cms.string("isIso == 1"),
#        numberRequired = cms.string(">= 1"),
#        alias = cms.string("Track Isolation")

        #),
    )   
)  # end PreSelectionIsoTrkOnly


#Standard Preselection Cuts, with no trigger.  
PreSelectionIsoTrkOnlyNoDz = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$p_T$ > 20 GeV")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|eta|$ < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.02"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|d_{0}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("numValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Valid Hits > 4")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingMiddle == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Middle Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingInner == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Inner Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Track Isolation")
        ),
    )   
)  # end PreSelectionIsoTrkOnly


#Standard Preselection Cuts, with no trigger.  
PreSelectionIsoTrkOnlyNoD0 = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$p_T$ > 20 GeV")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|eta|$ < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) < 0.02"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|d_{z}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("numValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Valid Hits > 4")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingMiddle == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Middle Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingInner == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Inner Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Track Isolation")
        ),
    )   
)  # end PreSelectionIsoTrkOnly



#Standard Preselection Cuts, with no trigger.  
PreSelectionIsoTrkOnlyDzSide = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$p_T$ > 20 GeV")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|eta|$ < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.02"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|d_{0}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) > 0.05 && fabs(dZwrtPV) < 0.15"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|d_{z}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("numValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Valid Hits > 4")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingMiddle == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Middle Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingInner == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Inner Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Track Isolation")
        ),
    )   
)  # end PreSelectionIsoTrkOnlyDzSide




#Standard Preselection Cuts, with no trigger.  
PreSelectionIsoTrkOnlyD0Side = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$p_T$ > 20 GeV")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|eta|$ < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) > 0.1 && fabs(d0wrtPV) < 0.3"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|d_{z}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) < 0.02"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("$|d_{0}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("numValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Valid Hits > 4")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingMiddle == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Middle Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("nHitsMissingInner == 0"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Missing Inner Hits = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        #        alias = cms.string("Track Isolation")
        ),
    )   
)  # end PreSelectionIsoTrkOnlyD0Side






#Standard Preselection Cuts, with no trigger, and no inner/middle hit requirements.  
PreSelectionIsoTrkOnlyNoHitCut = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        # alias = cms.string("$p_T$ > 20 GeV")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        # alias = cms.string("$|eta|$ < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        # alias = cms.string("$|d_{0}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        # alias = cms.string("$|d_{z}|$ < 0.02 cm")
        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("numValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        # alias = cms.string("Valid Hits > 4")
        ),    
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        # alias = cms.string("Track Isolation")
        ),
    )   
)  # end PreSelectionIsoTrkOnlyNoHitCut

cutTrkIso = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isIso == 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Track Isolation")
    )
PreSelectionIsoOrig = cms.PSet(
    name = cms.string("PreSelectionIsoOrig"),
    cuts = copy.deepcopy(PreSelectionIsoTrkOnly.cuts),
    )
PreSelectionIsoOrig.cuts.append(cutTrkIso)



cutNTrksRp5 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nTracksRp5 == 1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("nTracksRp5 = 1")
    )
PreSelectionIsoNTrk = cms.PSet(
    name = cms.string("PreSelectionIsoNTrk"),
    cuts = copy.deepcopy(PreSelectionIsoTrkOnly.cuts),
    )
PreSelectionIsoNTrk.cuts.append(cutNTrksRp5)
##deptrkrp5 is sumpT, plot and look at it to determine cut
## cutdepTrkRp5 = cms.PSet (
##         inputCollection = cms.string("tracks"),
##             cutString = cms.string("depTrkRp5 == 1"),
##             numberRequired = cms.string(">= 1"),
##             alias = cms.string("depTrkRp5 = 1")
##             )
## PreSelectionIsoNTrk = cms.PSet (
##         name = cms.string("PreSelectionIsoNTrk")
##             cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoHitCut.cuts)
##             )
## PreSelectionIsoOrig.cuts.append(cutNTrksRp5)
   


PreSelectionMuonVetoOnly = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnly"),
    cuts = copy.deepcopy(PreSelectionIsoTrkOnly.cuts),
    )
PreSelectionMuonVetoOnly.cuts.append(cutMuonVeto)

PreSelection = cms.PSet(  
    name = cms.string("PreSelection"), 
    cuts = copy.deepcopy(PreSelectionMuonVetoOnly.cuts),  
    )
PreSelection.cuts.append(cutElecVeto)  
PreSelection.cuts.append(cutDeadEcal)  
PreSelection.cuts.append(cutCrackVeto)  


PreSelNoTrig = cms.PSet(
    name = cms.string("PreSelNoTrig"),
    cuts = copy.deepcopy(PreSelection.cuts),
)


PreSelNoTrigNoDz = cms.PSet(  
    name = cms.string("PreSelNoTrigNoDz"), 
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoDz.cuts),  
    )
PreSelNoTrigNoDz.cuts.append(cutMuonVeto)  
PreSelNoTrigNoDz.cuts.append(cutElecVeto)  
PreSelNoTrigNoDz.cuts.append(cutDeadEcal)  
PreSelNoTrigNoDz.cuts.append(cutCrackVeto)  


PreSelNoTrigNoD0 = cms.PSet(  
    name = cms.string("PreSelNoTrigNoD0"), 
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoD0.cuts),  
    )
PreSelNoTrigNoD0.cuts.append(cutMuonVeto)  
PreSelNoTrigNoD0.cuts.append(cutElecVeto)  
PreSelNoTrigNoD0.cuts.append(cutDeadEcal)  
PreSelNoTrigNoD0.cuts.append(cutCrackVeto)  



cutJetPt = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("jet $p_{T}$ > 110 GeV")
    )

triggersStandard = cms.vstring(
    "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
    "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
    "HLT_MET120_HBHENoiseCleaned_v"
    )

PreSelectionWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionWithTrigJetMet"),
    triggers = triggersStandard, 
    cuts  = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionWithTrigJetMet.cuts.insert(0,cutJetPt)  
PreSelectionWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyWithTrigJetMet"),
    triggers = triggersStandard,
    cuts  = copy.deepcopy(PreSelectionIsoTrkOnly.cuts),
    )
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)  
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionMuonVetoOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyWithTrigJetMet"),
    triggers = triggersStandard,
    cuts  = copy.deepcopy(PreSelectionMuonVetoOnly.cuts),
    )
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)  
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

# Channels for processing AOD files
PreSelectionIsoTrkOnlyWithTrigJetMetNoHitCut = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyWithTrigJetMetNoHitCut"),
    triggers = triggersStandard, 
    cuts  = copy.deepcopy(PreSelectionIsoTrkOnlyNoHitCut.cuts),
    )
PreSelectionIsoTrkOnlyWithTrigJetMetNoHitCut.cuts.insert(0,cutJetPt)  
PreSelectionIsoTrkOnlyWithTrigJetMetNoHitCut.cuts.insert(0,cutMET)

PreSelectionMuonVetoOnlyWithTrigJetMetNoHitCut = copy.deepcopy(PreSelectionIsoTrkOnlyWithTrigJetMetNoHitCut)
PreSelectionMuonVetoOnlyWithTrigJetMetNoHitCut.name = cms.string("PreSelectionMuonVetoOnlyWithTrigJetMetNoHitCut")
PreSelectionMuonVetoOnlyWithTrigJetMetNoHitCut.cuts.append(cutMuonVeto)

PreSelectionWithTrigJetMetNoHitCut = copy.deepcopy(PreSelectionMuonVetoOnlyWithTrigJetMetNoHitCut)
PreSelectionWithTrigJetMetNoHitCut.name = cms.string("PreSelectionWithTrigJetMetNoHitCut")
PreSelectionWithTrigJetMetNoHitCut.cuts.append(cutElecVeto)   
PreSelectionWithTrigJetMetNoHitCut.cuts.append(cutDeadEcal)   
PreSelectionWithTrigJetMetNoHitCut.cuts.append(cutCrackVeto)  



#Channels for cut on PDG Id
##GenElec
cutCharginoId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 1000024"),  
    numberRequired = cms.string(">= 1"),  
    #    # alias = cms.string("GenMatch to chargino")
    )
cutElectronId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 11"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("GenElec")
    )
cutPionId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 211"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("GenPion")
    )
cutNotGenMatched = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 0"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("No Gen Match")
    )




PreSelectionCharginoId = cms.PSet(
    name = cms.string("PreSelectionCharginoId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionCharginoId.cuts.append(cutCharginoId)

PreSelectionElectronId = cms.PSet(
    name = cms.string("PreSelectionElectronId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionElectronId.cuts.append(cutElectronId)

PreSelectionPionId = cms.PSet(
    name = cms.string("PreSelectionPionId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPionId.cuts.append(cutPionId)

PreSelectionNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionNotGenMatched"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionNotGenMatched.cuts.append(cutNotGenMatched)


cutLightMesonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 15"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)  
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("GenMatch to light meson")
    )
cutKMesonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 16"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)  
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("GenMatch to K meson")
    )
cutLightBaryonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 19"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)  
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("GenMatch to light baryon")
    )
cutKBaryonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 20"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)  
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("GenMatch to K baryon")
    )





#Cuts that define the signal region after the PreSelection with Trig, Jet, and MET
cutMaxCaloByP = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5ByP < 0.1"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$E_{iso}$/p < 0.1")
    )
cutMaxCaloByPLoose = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5ByP < 0.5"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$E_{iso}$/p < 0.5")
    )
cutMaxCaloTight = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5 < 10"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$E_{iso}$ < 10 GeV")
    )
cutMaxCaloLoose = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5 < 30"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$E_{iso}$ < 30 GeV")
    )
cutMaxCaloPUCorr = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5RhoCorr < 20"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$E_{iso}^{PU-corr}$ < 20 GeV")
    )
cutNMissingOuterHits = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter >= 3"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Missing Outer Hits > 2")
    )
cutNMissingOuterHitsCtrlReg = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter == 0"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Missing Outer Hits = 0")
    )


##NMissingHits + Eiso
#Cuts that define the control region after the PreSelection with Trig, Jet, and MET
CtrlRegWithTrigJetMet = copy.deepcopy(PreSelectionWithTrigJetMet)
CtrlRegWithTrigJetMet.name = cms.string("CtrlRegWithTrigJetMet")
CtrlRegWithTrigJetMet.cuts.append(cutNMissingOuterHitsCtrlReg)  

SigRegWithMaxCaloByPLoose = copy.deepcopy(PreSelection)
SigRegWithMaxCaloByPLoose.name = cms.string("SigRegWithMaxCaloByPLoose")
SigRegWithMaxCaloByPLoose.cuts.append(cutNMissingOuterHits)
SigRegWithMaxCaloByPLoose.cuts.append(cutMaxCaloByPLoose)

SigRegWithMaxCaloByP = copy.deepcopy(PreSelection)
SigRegWithMaxCaloByP.name = cms.string("SigRegWithMaxCaloByP")
SigRegWithMaxCaloByP.cuts.append(cutNMissingOuterHits)
SigRegWithMaxCaloByP.cuts.append(cutMaxCaloByP)

SigRegWithMaxCalo = copy.deepcopy(PreSelection)
SigRegWithMaxCalo.name = cms.string("SigRegWithMaxCalo")
SigRegWithMaxCalo.cuts.append(cutNMissingOuterHits)  
SigRegWithMaxCalo.cuts.append(cutMaxCaloTight)  

SigRegWithMaxCaloLoose = copy.deepcopy(PreSelection)
SigRegWithMaxCaloLoose.name = cms.string("SigRegWithMaxCaloLoose")
SigRegWithMaxCaloLoose.cuts.append(cutNMissingOuterHits)
SigRegWithMaxCaloLoose.cuts.append(cutMaxCaloLoose)

# Use the PU corrected by default
SigRegWithMaxCaloPUCorr = copy.deepcopy(PreSelection)
SigRegWithMaxCaloPUCorr.name = cms.string("SigRegWithMaxCaloPUCorr")
SigRegWithMaxCaloPUCorr.cuts.append(cutNMissingOuterHits)  
SigRegWithMaxCaloPUCorr.cuts.append(cutMaxCaloPUCorr)  

SigRegWithTrigJetMet = copy.deepcopy(PreSelectionWithTrigJetMet)
SigRegWithTrigJetMet.name = cms.string("SigRegWithTrigJetMet")
SigRegWithTrigJetMet.cuts.append(cutNMissingOuterHits)
SigRegWithTrigJetMet.cuts.append(cutMaxCaloLoose)

# Use the PU corrected by default
SigRegWithTrigJetMetPUCorr = copy.deepcopy(PreSelectionWithTrigJetMet)
SigRegWithTrigJetMetPUCorr.name = cms.string("SigRegWithTrigJetMetPUCorr")
SigRegWithTrigJetMetPUCorr.cuts.append(cutNMissingOuterHits)
SigRegWithTrigJetMetPUCorr.cuts.append(cutMaxCaloPUCorr)  

#Cuts that define the fit region after the PreSelection with Trig, Jet, and MET
SigRegWithTrigJetMetCaloByP = copy.deepcopy(PreSelectionWithTrigJetMet)
SigRegWithTrigJetMetCaloByP.name = cms.string("SigRegWithTrigJetMetCaloByP")
SigRegWithTrigJetMetCaloByP.cuts.append(cutNMissingOuterHits)
SigRegWithTrigJetMetCaloByP.cuts.append(cutMaxCaloByPLoose)



PreSelectionPMissingDzSide = cms.PSet(  
    name = cms.string("PreSelectionPMissingDzSide"), 
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyDzSide.cuts),  
    )
PreSelectionPMissingDzSide.cuts.append(cutMuonVeto)
PreSelectionPMissingDzSide.cuts.append(cutElecVeto)  
PreSelectionPMissingDzSide.cuts.append(cutDeadEcal)  
PreSelectionPMissingDzSide.cuts.append(cutCrackVeto)  
PreSelectionPMissingDzSide.cuts.append(cutNMissingOuterHits)

PreSelectionPMissingD0Side = cms.PSet(  
    name = cms.string("PreSelectionPMissingD0Side"), 
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyD0Side.cuts),  
    )
PreSelectionPMissingD0Side.cuts.append(cutMuonVeto)
PreSelectionPMissingD0Side.cuts.append(cutElecVeto)  
PreSelectionPMissingD0Side.cuts.append(cutDeadEcal)  
PreSelectionPMissingD0Side.cuts.append(cutCrackVeto)  
PreSelectionPMissingD0Side.cuts.append(cutNMissingOuterHits)




#PreSelection + Eiso/p
PreSelectionPEiso = copy.deepcopy(PreSelection)
PreSelectionPEiso.name = cms.string("PreSelectionPEiso")
PreSelectionPEiso.cuts.append(cutMaxCaloByP)

#Cuts that define the control region after the PreSelection with Trig, Jet, and MET
CtrlReg = copy.deepcopy(PreSelection)
CtrlReg.name = cms.string("CtrlReg")
CtrlReg.cuts.append(cutNMissingOuterHitsCtrlReg)




#PreSelection + NHitsMissing  
PreSelNoTrigPMissingNotGenMatched = copy.deepcopy(PreSelNoTrig)  
PreSelNoTrigPMissingNotGenMatched.name = cms.string("PreSelNoTrigPMissingNotGenMatched")  
PreSelNoTrigPMissingNotGenMatched.cuts.append(cutNMissingOuterHits)  
PreSelNoTrigPMissingNotGenMatched.cuts.append(cutNotGenMatched)  

PreSelectionPMissing = copy.deepcopy(PreSelection)
PreSelectionPMissing.name = cms.string("PreSelectionPMissing")
PreSelectionPMissing.cuts.append(cutNMissingOuterHits)

PreSelectionPMissingPionId = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingPionId.name = cms.string("PreSelectionPMissingPionId")
PreSelectionPMissingPionId.cuts.append(cutPionId)

PreSelectionPMissingElectronId = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingElectronId.name = cms.string("PreSelectionPMissingElectronId")
PreSelectionPMissingElectronId.cuts.append(cutElectronId)

PreSelectionPMissingNotGenMatched = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingNotGenMatched.name = cms.string("PreSelectionPMissingNotGenMatched")
PreSelectionPMissingNotGenMatched.cuts.append(cutNotGenMatched)


PreSelectionPMissingLtMesonId = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingLtMesonId.name = cms.string("PreSelectionPMissingLtMesonId")
PreSelectionPMissingLtMesonId.cuts.append(cutLightMesonId)  

PreSelectionPMissingKMesonId = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingKMesonId.name = cms.string("PreSelectionPMissingKMesonId")
PreSelectionPMissingKMesonId.cuts.append(cutKMesonId)  

PreSelectionPMissingLtBaryonId = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingLtBaryonId.name = cms.string("PreSelectionPMissingLtBaryonId")
PreSelectionPMissingLtBaryonId.cuts.append(cutLightBaryonId)  

PreSelectionPMissingKBaryonId = copy.deepcopy(PreSelectionPMissing)
PreSelectionPMissingKBaryonId.name = cms.string("PreSelectionPMissingKBaryonId")
PreSelectionPMissingKBaryonId.cuts.append(cutKBaryonId)  



#Divided up into Pt Slices
PreSelectionPt20 = cms.PSet(
    name = cms.string("PreSelectionPt20"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )
cutPt20 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 20 & pt < 50"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("20 GeV < pT < 50 GeV ")
    )
PreSelectionPt20.cuts.append(cutPt20)

PreSelectionPt50 = cms.PSet(
    name = cms.string("PreSelectionPt50"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )
cutPt50 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 50 & pt < 75"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("50 GeV < pT < 75 GeV ")
    )
PreSelectionPt50.cuts.append(cutPt50)

PreSelectionPt75 = cms.PSet(
    name = cms.string("PreSelectionPt75"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )
cutPt75 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 75 & pt < 100"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("75 GeV < pT < 100 GeV ")
    )
PreSelectionPt75.cuts.append(cutPt75)

PreSelectionPt100 = cms.PSet(
    name = cms.string("PreSelectionPt100"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )
cutPt100 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 100 & pt < 125"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("100 GeV < pT < 125 GeV ")
    )
PreSelectionPt100.cuts.append(cutPt100)

PreSelectionPt125 = cms.PSet(
    name = cms.string("PreSelectionPt125"),
    cuts  = copy.deepcopy(PreSelection.cuts),
    )
cutPt125 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 125"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("125 GeV < pT ")
    )
PreSelectionPt125.cuts.append(cutPt125)



PreSelNoTrigNoDzNotGenMatched = cms.PSet(  
    name = cms.string("PreSelNoTrigNoDzNotGenMatched"), 
    cuts = copy.deepcopy(PreSelNoTrigNoDz.cuts),  
    )
PreSelNoTrigNoDzNotGenMatched.cuts.append(cutNMissingOuterHits)  
PreSelNoTrigNoDzNotGenMatched.cuts.append(cutNotGenMatched)  
PreSelNoTrigNoD0NotGenMatched = cms.PSet(  
    name = cms.string("PreSelNoTrigNoD0NotGenMatched"), 
    cuts = copy.deepcopy(PreSelNoTrigNoD0.cuts),  
    )
PreSelNoTrigNoD0NotGenMatched.cuts.append(cutNMissingOuterHits)  
PreSelNoTrigNoD0NotGenMatched.cuts.append(cutNotGenMatched)  

