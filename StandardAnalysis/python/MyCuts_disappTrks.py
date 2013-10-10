import FWCore.ParameterSet.Config as cms
import copy

##############################
##### List of triggers   #####
##############################

triggersJetMet = cms.vstring(
    "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
    "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
    "HLT_MET120_HBHENoiseCleaned_v",
    )
# Choose triggers by going to http://j2eeps.cern.ch/cms-project-confdb-hltdev/browser
# Select online/2012/8e33/v2.1.
# Take all the single electron triggers than are unprescaled and do not have extra strange requirements.  
triggersSingleMu = cms.vstring(
    "HLT_IsoMu24_eta2p1_v",  
    #    "HLT_IsoMu24_v",  # Not available in 2012A  
    )

triggersJetMetOrSingleMu = copy.deepcopy(triggersJetMet)  
triggersJetMetOrSingleMu.extend(["HLT_IsoMu24_eta2p1_v"])  


triggersSingleElec = cms.vstring(
    "HLT_Ele27_WP80_v",
    )
triggersDoubleMu = cms.vstring(
    "HLT_DoubleMu11_Acoplanarity03_v",
    "HLT_DoubleMu14_Mass8_PFMET40_v",
    "HLT_DoubleMu14_Mass8_PFMET50_v",
    "HLT_DoubleMu3_4_Dimuon5_Bs_Central_v",
    "HLT_DoubleMu3p5_4_Dimuon5_Bs_Central_v",
    "HLT_DoubleMu3p5_LowMassNonResonant_Displaced_v",
    "HLT_DoubleMu3p5_LowMass_Displaced_v",
    "HLT_DoubleMu4_Acoplanarity03_v",
    "HLT_DoubleMu4_Dimuon7_Bs_Forward_v",
    "HLT_DoubleMu4_JpsiTk_Displaced_v",
    "HLT_DoubleMu4_Jpsi_Displaced_v",
    "HLT_DoubleMu5_Ele8_CaloIdT_TrkIdVL_v",
    "HLT_DoubleMu5_IsoMu5_v",
    "HLT_DoubleMu8_Ele8_CaloIdT_TrkIdVL_v",
    )
##########################
##### List of cuts   #####
##########################

##### List of valid input collections #####
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters 

######################
#-- Cuts on  Event --#
######################
cutEvtFilterScraping = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("FilterOutScraping > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutEvtCSCHaloTight = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("CSCTightHaloId == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutEvtCSCHaloLoose = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("CSCLooseHaloId == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutEvtHBHENoiseFilter = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("HBHENoiseFilter == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutEvtHcalNoiseFilter = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("hcalnoiseTight == 1"),
    numberRequired = cms.string(">= 1"),
    )
################################
#-- Cuts on Primary Vertexes --#
################################
cutVtxGood = cms.PSet (
    inputCollection = cms.string("primaryvertexs"),
    cutString = cms.string("isGood > 0"),
    numberRequired = cms.string(">= 1"),
    )
###################
#-- Cuts on MET --#
###################
cutMET = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 220"),
    numberRequired = cms.string(">= 1"),
    )
cutMETNoMu = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("metNoMu > 220"),
    numberRequired = cms.string(">= 1"),
    )
cutMETNoElec = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("metNoElec > 220"),
    numberRequired = cms.string(">= 1"),
    )
cutMET20 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutMET30 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutMET40 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    )
cutMET50 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    )
cutMET75 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 1"),
    )
cutMET90 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 90"),
    numberRequired = cms.string(">= 1"),
    )
cutMET100 = cms.PSet(
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1"),
    )
cutMET200 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 200"),
    numberRequired = cms.string(">= 1"),
    )
####################
#-- Cuts on Jets --#
####################
cutSubLeadingJetID = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("disappTrkSubLeadingJetID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutBTagVeto = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("btagCombinedSecVertex > 0.679"),
    numberRequired = cms.string("= 0"),
    )
cutJetPt = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt20 = cms.PSet(
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt30N0 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 0"),
    )
cutJetPt30 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt50 = cms.PSet(
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt75 = cms.PSet(
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 1"),
    )
cutJetPt100 = cms.PSet(
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 100"),
    numberRequired = cms.string(">= 1"),
    )
cutJetEta = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 1"),
    )
cutJetEta2p4 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 1"),
    )
cutJetEta2p8 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.8"),
    numberRequired = cms.string(">= 1"),
    )
cutJetVetoDPhiMet = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(dPhiMet) < 1.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),  
    )
cutJetEta2p4N0 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 0"),
    )
cutJetIDLooseN0 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("jetIDLoose > 0"),
    numberRequired = cms.string(">= 0"),
    )
cutJetPt30NJet1 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 1"),
    )
cutJetPt30NJet2 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30c"),
    numberRequired = cms.string("== 2"),
    )
cutJetPt30NJet3 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 3"),
    )
cutJetPt30NJet4 = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 4"),
    )
cutNJets = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2"),
    )
cutJetNoiseChgHad = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("chargedHadronEnergyFraction > 0.2"),
    numberRequired = cms.string(">= 1"),
    )
cutJetNoiseChgEM  = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("chargedEmEnergyFraction < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutJetNoiseNeuEM = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("neutralEmEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )
cutJetNoiseNeuHad = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("neutralHadronEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )
##############################
#-- Cuts on Secondary Jets --#
##############################
cutLeadingJetID = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("disappTrkLeadingJetID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetBTagVeto = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("btagCombinedSecVertex > 0.679"),
    numberRequired = cms.string("= 0"),
    )
cutSecJetPt = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetPt90 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 90"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetEta2p4 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetEta2p8 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("fabs(eta) < 2.8"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseChgHad = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("chargedHadronEnergyFraction > 0.2"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseChgEM  = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("chargedEmEnergyFraction < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseNeuEM = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("neutralEmEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseNeuHad = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("neutralHadronEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetPt30NJet1 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 1"),
    )
cutSecJetPt30NJet2 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 2"),
    )
cutSecJetPt30NJet3 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string("== 3"),
    )
cutSecJetPt30NJet4 = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 4"),
    )
cutSecJetBTagVeto = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("btagCombinedSecVertex > 0.679"),
    numberRequired = cms.string("= 0"),
    )
cutSecJetNoiseChgHad = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("chargedHadronEnergyFraction > 0.2"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseNeuEM = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("neutralEmEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseChgEM = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("chargedEmEnergyFraction < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutSecJetNoiseNeuHad = cms.PSet (
    inputCollection = cms.string("secondary jets"),
    cutString = cms.string("neutralHadronEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
    )

#############################
#-- Cuts on Jet-Jet Pairs --#
#############################
cutJetJetDPhi = cms.PSet (
    inputCollection = cms.string("jet-jet pairs"),
    cutString = cms.string("deltaPhi > 2.5"),
    numberRequired = cms.string("= 0"),
    isVeto = cms.bool(True),
    )
######################
#-- Cuts on Tracks --#
######################
cutTrkPt = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt20 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt10 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt50 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPt75 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 75"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPtError = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("ptErrorByPt < 0.2"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEta = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEtaBarrel = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 0.8"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkWheel0GapVeto = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 0.15 | fabs(eta) > 0.35"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEtaMuonPk = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.55 | fabs(eta) > 1.85"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkEtaAtlas = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 0.63 && fabs(eta) > 0.1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkD0 = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) < 0.02"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkDZ = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("fabs(dZwrtPV) < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNHits = cms.PSet(
    inputCollection= cms.string("tracks"),
    cutString = cms.string("numValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissMid = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingMiddle == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissIn = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingInner == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissInDebug = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingInner >= 1"),
    numberRequired = cms.string("= 0"),
    #    isVeto = cms.bool(True),  
    )
cutTrkIso = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isIso == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkRelIsoRp3 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("trkRelIsoRp3 < 0.05"), 
    numberRequired = cms.string(">= 1"),
    )
cutTrkRelIsoRp3Debug = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("trkRelIsoRp3 > 0.05"), 
    numberRequired = cms.string("= 0"),
    isVeto = cms.bool(True),  
    )
cutTrkDeadEcalVeto =  cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isMatchedDeadEcal == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkCrackVeto = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkDeadEcalMatch = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isMatchedDeadEcal == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkSumPtGT = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("depTrkRp5MinusPt > 7"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkSumPtLT = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("depTrkRp5MinusPt <= 7"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissOut = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter >= 3"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxMissOut = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter <= 2"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloByP = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5ByP < 0.1"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloByPLoose = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5ByP < 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloTight = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5 < 5"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCalo10 = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5RhoCorr < 10"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloLoose = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5 < 30"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloPUCorr = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5RhoCorr < 20"),
    numberRequired = cms.string(">= 1"),
    )
cutMaxCaloPUCorrBlind = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5RhoCorr > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkHitMissOutCtrlReg = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkCharginoId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 1000024"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkElectronId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 11"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkMuonId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 13"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkTauId = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 15"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkPionId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 211"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkNotGenMatched = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedPdgId) == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkLightMesonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 15"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)
    numberRequired = cms.string(">= 1"),
    )
cutTrkKMesonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 16"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)
    numberRequired = cms.string(">= 1"),
    )
cutTrkLightBaryonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 19"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)
    numberRequired = cms.string(">= 1"),
    )
cutTrkKBaryonId =cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(genMatchedId) == 20"),
    #  for bin indices, see OSUAnalysis::getPdgIdBinValue(int pdgId)
    numberRequired = cms.string(">= 1"),
    )
cutNoCuts = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    )
cutTrkD0Side = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) > 0.1 && fabs(d0wrtPV) < 0.3"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkDZSide = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(dZwrtPV) > 0.05 && fabs(dZwrtPV) < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutTrkJetDeltaR = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinSubLeadJet > 0.5"),
    numberRequired = cms.string(">= 1"),
    )


###############################
#-- Cuts on Track-Jet pairs --#
###############################

#####################
#-- Cuts on Muons --#
#####################
cutMuonChgPos = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("charge == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonChgNeg = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("charge == -1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonEta = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonEta2p5 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.5"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonEta2p1 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonPt20 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonPt25 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonTightID = cms.PSet (  # recommended by https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Tight_Muon 
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonLooseID = cms.PSet (  
    inputCollection = cms.string("muons"),
    cutString = cms.string("looseID > 0"),
    numberRequired = cms.string(">= 1"),
    )
## cutMuonLooseIDVeto = cms.PSet (  
##     inputCollection = cms.string("muons"),
##     cutString = cms.string("looseID > 0"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
## cutMuonLooseIDVeto = cms.PSet (  
##     inputCollection = cms.string("muon-track pairs"),
##     cutString = cms.string("deltaRLooseID < 0.15"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
cutMuonLooseIDVeto = cms.PSet (  
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinMuonLooseId > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonLooseIDVetoInv = cms.PSet (  
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinMuonLooseId < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
## cutMuonLooseIDVetoInv = cms.PSet ( 
##     inputCollection = cms.string("muons"),
##     cutString = cms.string("looseID > 0"),
##     numberRequired = cms.string(">= 1"),
##     )
cutMuonLooseIDOnlyOne = cms.PSet (  
    inputCollection = cms.string("muons"),
    cutString = cms.string("looseID > 0"),
    numberRequired = cms.string("= 1"),
    )
cutSecMuonLooseIDVeto = cms.PSet (  
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinSecMuonLooseIdGlobal > 0.15"), 
    numberRequired = cms.string(">= 1"),
    )
## cutSecMuonLooseIDVeto = cms.PSet (  
##     inputCollection = cms.string("secondary muon-track pairs"),
##     cutString = cms.string("deltaRGlobalMuon < 0.15"), 
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
## cutSecMuonLooseIDVeto = cms.PSet (  
##     inputCollection = cms.string("secondary muons"),
##     cutString = cms.string("isGlobalMuon  > 0"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
cutSecMuonLooseIDVetoInv = cms.PSet (  
    inputCollection = cms.string("secondary muons"),
    cutString = cms.string("isGlobalMuon  > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutSecMuonLooseIDOnlyOne = cms.PSet (  
    inputCollection = cms.string("secondary muons"),
    cutString = cms.string("looseID > 0"),
    numberRequired = cms.string("= 1"),
    )
cutMuonDetIso = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("detIso < 0.05"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonPFIso = cms.PSet (  # recommended by https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Muon_Isolation_AN1
    inputCollection = cms.string("muons"),
    cutString = cms.string("relPFdBetaIso < 0.12"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonD0 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonDZ = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedDZ) < 0.02"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonValidHits = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonOneOnly = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 1"),
    )
cutMuonMetMT = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("metMT < 40"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonVeto = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    )
cutMuonVetoPt10 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string("= 0"),
    )
cutMuonPlusMet220 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("ptPlusMet > 220"),
    numberRequired = cms.string(">= 1"),
    )
###############################
#-- Cuts on Muon-Muon Pairs --#
###############################
cutMuonPairPt20 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairEta = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.5"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairTightID = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightID > 0"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairDetIso = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("detIso < 0.05"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairPFIso = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("relPFdBetaIso < 0.12"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairD0 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairDZ = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedDZ) < 0.02"),
    numberRequired = cms.string(">= 2"),
    )
cutMuonPairValidHits = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 2"),
    )
cutMuMuInvMass = cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )
cutMuMuChargeProduct = cms.PSet (
    inputCollection = cms.string("muon-muon pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    )
################################
#-- Cuts on Muon-Track Pairs --#
################################
cutMuTrkChgOpp = cms.PSet (
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonTrkDRSame = cms.PSet (
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonTrkDRSameNone = cms.PSet (
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string("= 0"),
    )
cutMuTrkDeltaR = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkDeltaRp5 = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR > 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkInvMass = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkInvMassTight = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 185"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTrkVeto = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("invMass < 80 | invMass > 100"),
    numberRequired = cms.string(">= 1"),
    )
##############################
#-- Cuts on Muon-Tau Pairs --#
##############################
cutMuTauInvMass = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTauCharge = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuTauDeltaR = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
#########################
#-- Cuts on Electrons --#
#########################
cutElecPt = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPt40 = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPt30 = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPt20 = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutElecEta = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutElecD0 = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedD0Vertex) < 0.02"),
    numberRequired = cms.string(">= 1"),
    )
cutElecDZ = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedDZ) < 0.01"),
    numberRequired = cms.string(">= 1"),
    )
cutElecNHits = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    )
cutElecMva = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA
    inputCollection= cms.string("electrons"),
    cutString = cms.string("mvaTrig_HtoWWto2l2nu == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPFIso = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    inputCollection= cms.string("electrons"),
    cutString = cms.string("relPFrhoIso < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPassConvVeto = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    inputCollection= cms.string("electrons"),
    cutString = cms.string("passConvVeto == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutElecLostHits = cms.PSet(  # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    inputCollection= cms.string("electrons"),
    cutString = cms.string("numberOfLostHits == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTightID = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("tightID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutElecLooseIDVeto = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinElecLooseMvaId > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
## cutElecLooseIDVeto = cms.PSet (
##     inputCollection = cms.string("electron-track pairs"),
##     cutString = cms.string("deltaRLooseMvaId < 0.15"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
cutElecLooseIDOnlyOne = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("mvaNonTrigV0 > 0"),
    numberRequired = cms.string("= 1"),
    )
cutElecLooseIDVetoInv = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinElecLooseMvaId < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
## cutElecLooseIDVetoInv = cms.PSet (
##     inputCollection = cms.string("electrons"),
##     cutString = cms.string("mvaNonTrigV0 > 0"),
##     numberRequired = cms.string(">= 1"),
##     )
cutElecVetoOneMax =   cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 1"),  
    )
cutElecVeto = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    )
cutElecVetoPt10 = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string("= 0"),
    )
cutElecPlusMet220 = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("ptPlusMet > 220"),
    numberRequired = cms.string(">= 1"),
    )
cutElecPlusMet110 = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("ptPlusMet > 110"),
    numberRequired = cms.string(">= 1"),
    )

#######################################
#-- Cuts on Electron-Electron Pairs --#
#######################################
cut2ElecPt = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecEta = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecD0 = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedD0Vertex) < 0.01"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecDZ = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("fabs(correctedDZ) < 0.01"),
    numberRequired = cms.string(">= 2"),
    )
cut2ElecNHits = cms.PSet(
    inputCollection= cms.string("electrons"),
    cutString = cms.string("tkNumValidHits > 4"),
    numberRequired = cms.string(">= 2"),
    )
cutElecElecMass = cms.PSet (
    inputCollection = cms.string("electron-electron pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )
####################################
#-- Cuts on Electron-Track Pairs --#
####################################
cutElecTrkDRSame = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTrkDR = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTrkDRp5 = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR > 0.5"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTrkInvMass = cms.PSet(
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTrkDRSameNone = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string("= 0"),
    )
cutElecTrkChgOpp = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    )

####################
#-- Cuts on Taus --#
####################
cutTauPt = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
    )
cutTauPtLeadingTrack = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("leadingTrackPt > 15"),
    numberRequired = cms.string(">= 1"),
    )
cutTauEta = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string(" fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauOneProng = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numProngs == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauThreeProng = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numProngs == 3"),
    numberRequired = cms.string(">= 1"),
    )
cutTauNumSigGamma = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalGammas == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTauNumSigNeutral = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalNeutrals == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTauNumSigPi0 = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalPiZeros == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTauAgainstElectron = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstElectronTight == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauForElectron = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstElectronTight == 0"),
    numberRequired = cms.string(">= 1"),
    )
cutTauAgainstMuonTight = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstMuonTight == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauAgainstMuonMed = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstMuonMedium == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauValidHits = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("leadingTrackValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    )
cutTauLooseIso = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSbyVLooseCombinedIsolationDeltaBetaCorr == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauDecayModeFinding = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSdecayModeFinding == 1"),
    numberRequired = cms.string(">= 1"),
    )
cutTauVeto = cms.PSet (
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    )
cutTauLooseHadronicVeto = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("deltaRMinTauLooseHadronicId > 0.15"),
    numberRequired = cms.string(">= 1"),
    )
## cutTauLooseHadronicVeto = cms.PSet (
##     inputCollection = cms.string("tau-track pairs"),
##     cutString = cms.string("deltaRLooseHadronicID < 0.15"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
## cutTauLooseHadronicVeto = cms.PSet (
##     inputCollection = cms.string("taus"),
##     cutString = cms.string("looseHadronicID > 0"),
##     numberRequired = cms.string("= 0"),
##     isVeto = cms.bool(True),  
##     )
cutTauLooseHadronicVetoInv = cms.PSet (
    inputCollection = cms.string("taus"),
    cutString = cms.string("looseHadronicID > 0"),
    numberRequired = cms.string(">= 1"),
    )
#############################
#-- Cuts on Tau-Tau Pairs --#
#############################
cutTauPairPt = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairEta = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairValidHits = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("leadingTrackValidHits > 4"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairNumProng = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numProngs == 1"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairNumSigGamma = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalGammas == 0"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairNumSigNeutral = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalNeutrals == 0"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairNumPi0 = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalPiZeros == 0"),
    numberRequired = cms.string(">= 2"),
    )
cutTauPairInvMass = cms.PSet(
    inputCollection = cms.string("tau-cutTau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )
##############################
#-- Cuts on Tau-Track Pairs--#
##############################
cutTauTrkDeltaR = cms.PSet(
    inputCollection = cms.string("tau-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
