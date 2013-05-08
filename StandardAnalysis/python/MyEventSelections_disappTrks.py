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





#### List of channels #####
NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    cuts = cms.VPSet (),
    )
NoCuts.cuts.append(cutNoCuts)


## Preselection ##

PreSelection = cms.PSet(
    name = cms.string("PreSelection"),
    cuts = cms.VPSet (),
    )
PreSelection.cuts.append(cutTrackPt)
PreSelection.cuts.append(cutTrackEta)
PreSelection.cuts.append(cutTrackd0)
PreSelection.cuts.append(cutTrackdz)
PreSelection.cuts.append(cutTrackNumValidHits)
PreSelection.cuts.append(cutMissingMiddleHits)
PreSelection.cuts.append(cutMissingInnerHits)
PreSelection.cuts.append(cutTrkIso)
PreSelection.cuts.append(cutMuonVeto)
PreSelection.cuts.append(cutElecVeto)
PreSelection.cuts.append(cutDeadEcal)
PreSelection.cuts.append(cutCrackVeto)

PreSelectionWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnly = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (),
    )
PreSelectionIsoTrkOnly.cuts.append(cutTrackPt)
PreSelectionIsoTrkOnly.cuts.append(cutTrackEta)
PreSelectionIsoTrkOnly.cuts.append(cutTrackd0)
PreSelectionIsoTrkOnly.cuts.append(cutTrackdz)
PreSelectionIsoTrkOnly.cuts.append(cutTrackNumValidHits)
PreSelectionIsoTrkOnly.cuts.append(cutMissingMiddleHits)
PreSelectionIsoTrkOnly.cuts.append(cutMissingInnerHits)
PreSelectionIsoTrkOnly.cuts.append(cutTrkIso)

PreSelectionIsoTrkOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnly.cuts),
    )
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyNoDz = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDz"),
    cuts = cms.VPSet (),
    )
PreSelectionIsoTrkOnlyNoDz.cuts.append(cutTrackPt)
PreSelectionIsoTrkOnlyNoDz.cuts.append(cutTrackEta)
PreSelectionIsoTrkOnlyNoDz.cuts.append(cutTrackd0)
PreSelectionIsoTrkOnlyNoDz.cuts.append(cutTrackNumValidHits)
PreSelectionIsoTrkOnlyNoDz.cuts.append(cutMissingMiddleHits)
PreSelectionIsoTrkOnlyNoDz.cuts.append(cutMissingInnerHits)
PreSelectionIsoTrkOnlyNoDz.cuts.append(cutTrkIso)

PreSelectionIsoTrkOnlyNoDzWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDzWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoDz.cuts),
    )
PreSelectionIsoTrkOnlyNoDzWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoDzWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyNoD0 = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDz"),
    cuts = cms.VPSet (),
    )
PreSelectionIsoTrkOnlyNoD0.cuts.append(cutTrackPt)
PreSelectionIsoTrkOnlyNoD0.cuts.append(cutTrackEta)
PreSelectionIsoTrkOnlyNoD0.cuts.append(cutTrackdz)
PreSelectionIsoTrkOnlyNoD0.cuts.append(cutTrackNumValidHits)
PreSelectionIsoTrkOnlyNoD0.cuts.append(cutMissingMiddleHits)
PreSelectionIsoTrkOnlyNoD0.cuts.append(cutMissingInnerHits)
PreSelectionIsoTrkOnlyNoD0.cuts.append(cutTrkIso)

PreSelectionIsoTrkOnlyNoD0WithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoD0WithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoD0.cuts),
    )
PreSelectionIsoTrkOnlyNoD0WithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoD0WithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionMuonVetoOnly = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnly"),
    cuts = cms.VPSet (),
    )
PreSelectionMuonVetoOnly.cuts.append(cutTrackPt)
PreSelectionMuonVetoOnly.cuts.append(cutTrackEta)
PreSelectionMuonVetoOnly.cuts.append(cutTrackd0)
PreSelectionMuonVetoOnly.cuts.append(cutTrackdz)
PreSelectionMuonVetoOnly.cuts.append(cutTrackNumValidHits)
PreSelectionMuonVetoOnly.cuts.append(cutMissingMiddleHits)
PreSelectionMuonVetoOnly.cuts.append(cutMissingInnerHits)
PreSelectionMuonVetoOnly.cuts.append(cutTrkIso)
PreSelectionMuonVetoOnly.cuts.append(cutMuonVeto)

PreSelectionMuonVetoOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionMuonVetoOnly.cuts),
    )
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionElectronVetoOnly = cms.PSet(
    name = cms.string("PreSelectionElectronVetoOnly"),
    cuts = cms.VPSet (),
    )
PreSelectionElectronVetoOnly.cuts.append(cutTrackPt)
PreSelectionElectronVetoOnly.cuts.append(cutTrackEta)
PreSelectionElectronVetoOnly.cuts.append(cutTrackd0)
PreSelectionElectronVetoOnly.cuts.append(cutTrackdz)
PreSelectionElectronVetoOnly.cuts.append(cutTrackNumValidHits)
PreSelectionElectronVetoOnly.cuts.append(cutMissingMiddleHits)
PreSelectionElectronVetoOnly.cuts.append(cutMissingInnerHits)
PreSelectionElectronVetoOnly.cuts.append(cutTrkIso)
PreSelectionElectronVetoOnly.cuts.append(cutMuonVeto)
PreSelectionElectronVetoOnly.cuts.append(cutElecVeto)

PreSelectionElectronVetoOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionElectronVetoOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionElectronVetoOnly.cuts),
    )
PreSelectionElectronVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionElectronVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnlyDzSide = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyDzSide"),
    cuts = cms.VPSet (),
    )
PreSelectionIsoTrkOnlyDzSide.cuts.append(cutTrackPt)
PreSelectionIsoTrkOnlyDzSide.cuts.append(cutTrackEta)
PreSelectionIsoTrkOnlyDzSide.cuts.append(cutTrackd0)
PreSelectionIsoTrkOnlyDzSide.cuts.append(cutdzSide)
PreSelectionIsoTrkOnlyDzSide.cuts.append(cutTrackNumValidHits)
PreSelectionIsoTrkOnlyDzSide.cuts.append(cutMissingMiddleHits)
PreSelectionIsoTrkOnlyDzSide.cuts.append(cutMissingInnerHits)
PreSelectionIsoTrkOnlyDzSide.cuts.append(cutTrkIso)

PreSelectionIsoTrkOnlyDzSideWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyDzSideWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyDzSide.cuts),
    )
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyD0Side = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyD0Side"),
    cuts = cms.VPSet (),
    )
PreSelectionIsoTrkOnlyD0Side.cuts.append(cutTrackPt)
PreSelectionIsoTrkOnlyD0Side.cuts.append(cutTrackEta)
PreSelectionIsoTrkOnlyD0Side.cuts.append(cutd0Side)
PreSelectionIsoTrkOnlyD0Side.cuts.append(cutTrackdz)
PreSelectionIsoTrkOnlyD0Side.cuts.append(cutTrackNumValidHits)
PreSelectionIsoTrkOnlyD0Side.cuts.append(cutMissingMiddleHits)
PreSelectionIsoTrkOnlyD0Side.cuts.append(cutMissingInnerHits)
PreSelectionIsoTrkOnlyD0Side.cuts.append(cutTrkIso)

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
PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)


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
PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)

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
PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)

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
    cuts = cms.VPSet (),
    )
PreSelectionNoHitCut.cuts.append(cutTrackPt)
PreSelectionNoHitCut.cuts.append(cutTrackEta)
PreSelectionNoHitCut.cuts.append(cutTrackd0)
PreSelectionNoHitCut.cuts.append(cutTrackdz)
PreSelectionNoHitCut.cuts.append(cutTrackNumValidHits)
PreSelectionNoHitCut.cuts.append(cutTrkIso)
PreSelectionNoHitCut.cuts.append(cutMuonVeto)
PreSelectionNoHitCut.cuts.append(cutElecVeto)
PreSelectionNoHitCut.cuts.append(cutDeadEcal)
PreSelectionNoHitCut.cuts.append(cutCrackVeto)

PreSelectionNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionNoHitCut.cuts),
    )
PreSelectionWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyNoHitCut = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoHitCut"),
    cuts = cms.VPSet (),
    )
PreSelectionIsoTrkOnlyNoHitCut.cuts.append(cutTrackPt)
PreSelectionIsoTrkOnlyNoHitCut.cuts.append(cutTrackEta)
PreSelectionIsoTrkOnlyNoHitCut.cuts.append(cutTrackd0)
PreSelectionIsoTrkOnlyNoHitCut.cuts.append(cutTrackdz)
PreSelectionIsoTrkOnlyNoHitCut.cuts.append(cutTrackNumValidHits)
PreSelectionIsoTrkOnlyNoHitCut.cuts.append(cutTrkIso)

PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoHitCut.cuts),
    )
PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionMuonVetoOnlyNoHitCut = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyNoHitCut"),
    cuts = cms.VPSet (),
    )
PreSelectionMuonVetoOnlyNoHitCut.cuts.append(cutTrackPt)
PreSelectionMuonVetoOnlyNoHitCut.cuts.append(cutTrackEta)
PreSelectionMuonVetoOnlyNoHitCut.cuts.append(cutTrackd0)
PreSelectionMuonVetoOnlyNoHitCut.cuts.append(cutTrackdz)
PreSelectionMuonVetoOnlyNoHitCut.cuts.append(cutTrackNumValidHits)
PreSelectionMuonVetoOnlyNoHitCut.cuts.append(cutTrkIso)
PreSelectionMuonVetoOnlyNoHitCut.cuts.append(cutMuonVeto)

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


