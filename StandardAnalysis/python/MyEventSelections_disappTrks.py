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
 ## Trigger + Jet + Met ##
triggersJetMet = cms.vstring(
    "HLT_MonoCentralPFJet80_PFMETnoMu95_NHEF0p95_v",
    "HLT_MonoCentralPFJet80_PFMETnoMu105_NHEF0p95_v",
    "HLT_MET120_HBHENoiseCleaned_v"
    )
triggersSingleMu = cms.vstring(
    "HLT_IsoMu24_v",
    )


cutVtxGood = cms.PSet (
    inputCollection = cms.string("primaryvertexs"),
    cutString = cms.string("isGood > 0"),
    numberRequired = cms.string(">= 1"),
    )

cutEvtFilterScraping = cms.PSet (
    inputCollection = cms.string("events"),
    cutString = cms.string("FilterOutScraping > 0"),
    numberRequired = cms.string(">= 1"),
    )


cutMuonEta = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.5"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonPt20 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonTightID = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightID > 0"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonDetIso = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("detIso < 0.05"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonD0 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("abs(correctedD0) < 0.02"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonOneOnly = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 1"),  
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

# FIXME:  Need to remove duplicate cuts listed below.  
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


cutElecElecMass = cms.PSet (
    inputCollection = cms.string("electron-electron pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("40 < InvMass(e+e) < 160")
    )


cutElecTrkDRSame = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
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



cutMET = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 220"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("MET > 220 Gev")
    )
cutMET40 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 40"),
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




cutJetPt = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
    )


 ##  Preselection Cuts ##
cutTrackPt = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$p_{T}$ > 20 GeV")
    )
cutTrackEta = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$|eta|$ < 2.1 ")
    )
cutTrackd0 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) < 0.01"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$|d_{0}|$ < 0.01 cm ")
    )

cutTrackdz = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(dZwrtPV) < 0.01"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$|d_{z}|$ < 0.01 cm ")
    )
cutTrackNumValidHits = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("numValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Valid Hits > 4 ")
    )
cutMissingMiddleHits = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingMiddle == 0"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Missing Middle Hits = 0 ")
    )
cutMissingInnerHits = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingInner == 0"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Missing Inner Hits = 0 ")
    )
cutTrkIso = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isIso == 1"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Track Isolation")
    )

cutMuonVeto = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    # alias = cms.string("Muon Veto")
    )
cutMuonVetoPt10 = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string("= 0"),
    # alias = cms.string("Muon Veto")
    )
cutElecVeto = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    # alias = cms.string("Electron Veto")
    )
cutElecVetoPt10 = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > 10"),
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

## Signal Region (Loose and Tight) ##
cutSumPtGreaterThan = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("depTrkRp5MinusPt > 7"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Missing Outer Hits > 2")
    )
cutSumPtLessThan = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("depTrkRp5MinusPt <= 7"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Missing Outer Hits > 2")
    )
cutNMissingOuterHits = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter >= 3"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Missing Outer Hits > 2")
    )

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
cutMaxCaloPUCorrBlind = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("caloTotDeltaRp5RhoCorr > 20"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$E_{iso}^{PU-corr}$ < 20 GeV")
    )
## Control Region ##
cutNMissingOuterHitsCtrlReg = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("nHitsMissingOuter == 0"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Missing Outer Hits = 0")
    )
## PDG Id ##
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

cutNoCuts = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
    )
cutd0Side = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) > 0.1 && fabs(d0wrtPV) < 0.3"),
    numberRequired = cms.string(">= 1"),
    )
cutdzSide = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(dZwrtPV) > 0.05 && fabs(dZwrtPV) < 0.15"),
    numberRequired = cms.string(">= 1"),
    )

cutElecEta = cms.PSet (
    inputCollection = cms.string("electrons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
cutMuonEta = cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )

cutElecTrkDRSame = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
cutElecTrkDRSameNone = cms.PSet (
    inputCollection = cms.string("electron-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string("= 0"),
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


#### Cuts from monojet analysis, AN-2012-421 #####
cutMET200 = cms.PSet (
    inputCollection = cms.string("mets"),
    cutString = cms.string("pt > 200"),
    numberRequired = cms.string(">= 1"),
    )

cutJetEta = cms.PSet (
    inputCollection = cms.string("jets"),
    #    cutString = cms.string("fabs(eta) < 2.0"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )

cutNJets = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 2"),
    )

cutJetJetDPhi = cms.PSet (
    inputCollection = cms.string("jet-jet pairs"),
    cutString = cms.string("deltaPhi > 2"),
    numberRequired = cms.string("= 0"),
    )

cutJetNoiseChgHad = cms.PSet (
    inputCollection = cms.string("jets"),
    cutString = cms.string("chargedHadronEnergyFraction > 0.2"),
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


cutTauVeto = cms.PSet (
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),
    )



#### List of channels #####
NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    cuts = cms.VPSet (
       cutNoCuts,
       ),
    )

## Preselection ##

PreSelection = cms.PSet(
    name = cms.string("PreSelection"),
    cuts = cms.VPSet (
       cutTrackPt,
       cutTrackEta,
       cutTrackd0,
       cutTrackdz,
       cutTrackNumValidHits,
       cutMissingMiddleHits,
       cutMissingInnerHits,
       cutTrkIso,
       cutMuonVeto,
       cutElecVeto,
       cutDeadEcal,
       cutCrackVeto,
       ),
    )

PreSelectionWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnly = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
         cutTrackPt,
         cutTrackEta,
         cutTrackd0,
         cutTrackdz,
         cutTrackNumValidHits,
         cutMissingMiddleHits,
         cutMissingInnerHits,
         cutTrkIso,
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
        cutTrackPt,
        cutTrackEta,
        cutTrackd0,
        #        cutTrackdz,
        cutTrackNumValidHits,
        ## cutMissingMiddleHits,
        ## cutMissingInnerHits,
        ## cutTrkIso,
        ## cutSumPtLessThan,
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
        cutTrackPt,
        cutTrackEta,
        cutTrackd0,
        #        cutTrackdz,
        cutTrackNumValidHits,
        ## cutMissingMiddleHits,
        ## cutMissingInnerHits,
        #        cutTrkIso,
        #        cutSumPtLessThan,
        cutMuonTrkDRSame,
    )
)


PreSelectionIsoTrkOnlyNoMuonMatch = copy.deepcopy(PreSelectionIsoTrkOnlyWithTrigJetMet)
PreSelectionIsoTrkOnlyNoMuonMatch.name = "PreSelectionIsoTrkOnlyNoMuonMatch"
PreSelectionIsoTrkOnlyNoMuonMatch.cuts.append(cutMuonTrkDRSameNone)
PreSelectionIsoTrkOnlyNoMuonMatch.cuts.append(cutMuonVeto)

PreSelectionIsoTrkOnlyNoElecMatch = copy.deepcopy(PreSelectionIsoTrkOnlyWithTrigJetMet)
PreSelectionIsoTrkOnlyNoElecMatch.name = "PreSelectionIsoTrkOnlyNoElecMatch"
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutDeadEcal)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutCrackVeto)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutElecTrkDRSameNone)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutElecVeto)




PreSelectionIsoTrkOnlyNoDz = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDz"),
    cuts = cms.VPSet (
       cutTrackPt,
       cutTrackEta,
       cutTrackd0,
       cutTrackNumValidHits,
       cutMissingMiddleHits,
       cutMissingInnerHits,
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
       cutTrackPt,
       cutTrackEta,
       cutTrackdz,
       cutTrackNumValidHits,
       cutMissingMiddleHits,
       cutMissingInnerHits,
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
       cutTrackPt,
       cutTrackEta,
       cutTrackd0,
       cutTrackdz,
       cutTrackNumValidHits,
       cutMissingMiddleHits,
       cutMissingInnerHits,
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
       cutTrackPt,
       cutTrackEta,
       cutTrackd0,
       cutTrackdz,
       cutTrackNumValidHits,
       cutMissingMiddleHits,
       cutMissingInnerHits,
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

PreSelectionIsoTrkOnlyDzSide = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyDzSide"),
    cuts = cms.VPSet (
       cutTrackPt,
       cutTrackEta,
       cutTrackd0,
       cutdzSide,
       cutTrackNumValidHits,
       cutMissingMiddleHits,
       cutMissingInnerHits,
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
       cutTrackPt,
       cutTrackEta,
       cutd0Side,
       cutTrackdz,
       cutTrackNumValidHits,
       cutMissingMiddleHits,
       cutMissingInnerHits,
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


PreSelectionPMissing = cms.PSet(
    name = cms.string("PreSelectionPMissing"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPMissing.cuts.append(cutNMissingOuterHits)

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
PreSelectionPSumPtLessThan.cuts.append(cutSumPtLessThan)

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
PreSelectionPSumPtGreaterThan.cuts.append(cutSumPtGreaterThan)

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
PreSelectionPMissingSumPtGreaterThan.cuts.append(cutSumPtGreaterThan)


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
PreSelectionPMissingSumPtLessThan.cuts.append(cutSumPtLessThan)

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


## Preselection (AOD)
PreSelectionNoHitCut = cms.PSet(
    name = cms.string("PreSelectionNoHitCut"),
    cuts = cms.VPSet (
       cutTrackPt,
       cutTrackEta,
       cutTrackd0,
       cutTrackdz,
       cutTrackNumValidHits,
       cutTrkIso,
       cutMuonVeto,
       cutElecVeto,
       cutDeadEcal,
       cutCrackVeto,
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
       cutTrackPt,
       cutTrackEta,
       cutTrackd0,
       cutTrackdz,
       cutTrackNumValidHits,
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
       cutTrackPt,
       cutTrackEta,
       cutTrackd0,
       cutTrackdz,
       cutTrackNumValidHits,
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
PreSelectionCharginoId.cuts.append(cutCharginoId)


PreSelectionElectronId = cms.PSet(
    name = cms.string("PreSelectionElectronId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionElectronId.cuts.append(cutElectronId)

PreSelectionElectronIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionElectronIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
PreSelectionElectronIdWithTrigJetMet.cuts.append(cutElectronId)


PreSelectionPionId = cms.PSet(
    name = cms.string("PreSelectionPionId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPionId.cuts.append(cutPionId)

PreSelectionPionIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPionIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
PreSelectionPionIdWithTrigJetMet.cuts.append(cutPionId)


PreSelectionNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionNotGenMatched"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionNotGenMatched.cuts.append(cutNotGenMatched)


PreSelectionPMissingElectronId = cms.PSet(
    name = cms.string("PreSelectionPMissingElectronId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingElectronId.cuts.append(cutElectronId)


PreSelectionPMissingElectronIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPMissingElectronIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingElectronIdWithTrigJetMet.cuts.append(cutElectronId)


PreSelectionPMissingPionId = cms.PSet(
    name = cms.string("PreSelectionPMissingPionId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingPionId.cuts.append(cutPionId)

PreSelectionPMissingPionIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPMissingPionIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingPionIdWithTrigJetMet.cuts.append(cutPionId)


PreSelectionPMissingNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionPMissingNotGenMatched"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingNotGenMatched.cuts.append(cutNotGenMatched)


PreSelectionPMissingLtMesonId = cms.PSet(
    name = cms.string("PreSelectionPMissingLtMesonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingLtMesonId.cuts.append(cutLightMesonId)


PreSelectionPMissingKMesonId = cms.PSet(
    name = cms.string("PreSelectionPMissingKMesonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingKMesonId.cuts.append(cutKMesonId)


PreSelectionPMissingLtBaryonId = cms.PSet(
    name = cms.string("PreSelectionPMissingLtBaryonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingLtBaryonId.cuts.append(cutLightBaryonId)


PreSelectionPMissingKBaryonId = cms.PSet(
    name = cms.string("PreSelectionPMissingKBaryonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingKBaryonId.cuts.append(cutKBaryonId)


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

SigRegWithMaxCaloPUCorrAndSumPtLessThan = cms.PSet(
    name = cms.string("SigRegWithMaxCaloPUCorrAndSumPtLessThan"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloPUCorrAndSumPtLessThan.cuts.append(cutSumPtLessThan)
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
SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet.cuts.append(cutSumPtLessThan)
SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet.cuts.append(cutMaxCaloPUCorr)


## Control Region Channels ##
CtrlReg = cms.PSet(
    name = cms.string("CtrlReg"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
CtrlReg.cuts.append(cutNMissingOuterHitsCtrlReg)


CtrlRegWithTrigJetMet = cms.PSet(
    name = cms.string("CtrlRegWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
CtrlRegWithTrigJetMet.cuts.append(cutNMissingOuterHitsCtrlReg)


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
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutJetJetDPhi,
        cutMuonVeto,
        cutElecVeto,
        cutTauVeto,
       ),
    )


MonoJetNoDijetCut = cms.PSet(
    name = cms.string("MonoJetNoDijetCut"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutMuonVeto,
        cutElecVeto,
        cutTauVeto,
       ),
    )


