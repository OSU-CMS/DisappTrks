import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.invMass import *
from OSUT3Analysis.Configuration.cutUtilities import *

##############################
##### Constants          #####
##############################

mZPDG = 91.1876  # Z mass from http://pdglive.lbl.gov/DataBlock.action?node=S044M

##############################
##### List of triggers   #####
##############################

triggersMet = cms.vstring(
    "HLT_MET75_IsoTrk50_v", # trigger designed for disappearing tracks

    # monojet triggers in the data, unprescaled for all of 2015, see EXO-15-003 PAS / AN2015_072_v8 Table 6
    "HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v",   # 74X MC
    "HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v",   # 2015D 76X ReReco Part 1
    "HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v",                # 2015D 76X ReReco Part 2  && RunIIFall15MiniAODv2_76X MC

    "HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v",
    "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v",
    "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v",

    "HLT_PFMET170_BeamHaloCleaned_v",
    "HLT_PFMET170_HBHECleaned_v",
    "HLT_PFMET170_JetIdCleaned_v",
    "HLT_PFMET170_NoiseCleaned_v",
    "HLT_PFMET170_NotCleaned_v",
)

triggersSingleMu = cms.vstring( # recommended here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Trigger
    "HLT_IsoMu20_v",    # yes available in bkgd MC
    "HLT_IsoTkMu20_v",  # yes available in bkgd MC
)

triggersSingleMu2016 = cms.vstring( # recommended here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Trigger
    "HLT_IsoMu22_v",    # yes available in bkgd MC
    "HLT_IsoTkMu22_v",  # yes available in bkgd MC
)

triggersSingleEle = cms.vstring(
    "HLT_Ele22_eta2p1_WPLoose_Gsf_v", # available in the data
    "HLT_Ele22_eta2p1_WP75_Gsf_v",    # available in the bkgd MC
    "HLT_Ele25_eta2p1_WPLoose_Gsf_v"  # available in the 2016 data
)

triggersSingleTau = cms.vstring(
    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v", # prescaled in data
)

##########################
##### List of cuts   #####
##########################

##### List of valid input collections #####
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters

##################################################
## primaryvertexs
##################################################
cutGoodPV = cms.PSet (
    inputCollection = cms.vstring("primaryvertexs"),
    cutString = cms.string("isValid > 0 && ndof >= 4 && fabs (z) < 24.0 && sqrt (x * x + y * y) < 2.0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 good primary vertices"),
)

##################################################
## mets
##################################################
cutMet = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("noMuPt > 100"),
    numberRequired = cms.string(">= 1"),
)
cutLowMet = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt < 60"),
    numberRequired = cms.string(">= 1"),
)

##################################################
## track-met pairs
##################################################
cutMuonMT = cms.PSet(
    inputCollection = cms.vstring("muons", "mets"),
    cutString = cms.string("transMass (muon, met) < 40"),
    numberRequired = cms.string(">= 1"),
)
cutElectronMT = cms.PSet(
    inputCollection = cms.vstring("electrons", "mets"),
    cutString = cms.string("transMass (electron, met) < 40"),
    numberRequired = cms.string(">= 1"),
)

##################################################
## jets
##################################################
cutJetPt = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 110"),
    numberRequired = cms.string(">= 1"),
)
cutJetEta = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("fabs ( eta ) < 2.4"),
    numberRequired = cms.string(">= 1"),
)
cutJetChgHad = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("chargedHadronEnergyFraction > 0.2"),
    numberRequired = cms.string(">= 1"),
)
cutJetChgEm = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("chargedEmEnergyFraction < 0.5"),
    numberRequired = cms.string(">= 1"),
)
cutJetNeuHad = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("neutralHadronEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
)
cutJetNeuEm = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("neutralEmEnergyFraction < 0.7"),
    numberRequired = cms.string(">= 1"),
)
cutNJets = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nJets <= 2"),
    numberRequired = cms.string(">= 1"),
)
cutDijetDeltaPhiMax = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("dijetMaxDeltaPhi < 2.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("veto pairs of jets with #Delta#Phi > 2.5"),
)
cutJetMetPhi = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("deltaPhiMetJetLeading > 0.5 && deltaPhiMetJetSubleading > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta#Phi(E_{T}^{miss},jet) > 0.5"),
)
cutJetTightLepVeto = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("\
    ((\
    neutralHadronEnergyFraction<0.90 && \
    neutralEmEnergyFraction<0.90 && \
    (chargedMultiplicity + neutralMultiplicity)>1 && \
    muonEnergyFraction<0.8) && \
    ((abs(eta)<=2.4 && chargedHadronEnergyFraction>0 && chargedMultiplicity>0 && chargedEmEnergyFraction<0.90) || \
    abs(eta)>2.4) && \
    abs(eta)<=3.0) \
    || (neutralEmEnergyFraction<0.90 && neutralMultiplicity>10 && abs(eta)>3.0)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 jet passing TightLepVeto ID"),
)

##################################################
## tracks
##################################################
cutTrkPt55 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 55"),
    numberRequired = cms.string(">= 1"),
)
cutTrkPt50 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
)
cutTrkPt35 = cms.PSet(  # LOWER PT CUT FOR SYSTEMATICS STUDIES
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 35"),
    numberRequired = cms.string(">= 1"),
)
cutTrkPt30 = cms.PSet(  # LOWER PT CUT FOR SYSTEMATICS STUDIES
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 2.1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEcalGapVeto = cms.PSet(  # BARREL-ENDCAP GAP VETO
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 1.42 || fabs ( eta ) > 1.65"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEtaMuonIneff1 = cms.PSet(        # TRACK ETA:  MUON INEFFICIENCY REGION 1
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 0.15 || fabs ( eta ) > 0.35"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEtaMuonIneff2 = cms.PSet(        # TRACK ETA:  MUON INEFFICIENCY REGION 2
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 1.55 || fabs ( eta ) > 1.85"),
    numberRequired = cms.string(">= 1"),
)
cutTrkTOBCrack = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("!inTOBCrack"),
    numberRequired = cms.string(">= 1"),
)
cutTrkFiducialElectron = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("isFiducialElectronTrack"),
    numberRequired = cms.string(">= 1"),
)
cutTrkFiducialMuon = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("isFiducialMuonTrack"),
    numberRequired = cms.string(">= 1"),
)
cutTrkFiducialECAL = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("isFiducialECALTrack"),
    numberRequired = cms.string(">= 1"),
)
# cutTrkEtaEcalCrackVeto = cms.PSet(  # TRACK ETA:  NOT IN ECAL CRACKS:  UPDATE CRACK BOUNDARIES
#     inputCollection = cms.vstring("tracks"),
#     cutString = cms.string("fabs ( eta ) "),
#     numberRequired = cms.string(">= 1"),
# )
cutTrkNValidPixelHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitPattern_.numberOfValidPixelHits >= 1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNValidHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("numberOfValidHits >= 7"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNValidHits3 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("numberOfValidHits == 3"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNValidHits4 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("numberOfValidHits == 4"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNValidHitsLE4 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("numberOfValidHits <= 4"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNValidHits5 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("numberOfValidHits == 5"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNValidHits6 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("numberOfValidHits == 6"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissIn = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingInnerHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissMid = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingMiddleHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkIso = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string(" ( trackIsoNoPUDRp3 / pt ) < 0.05"),
    numberRequired = cms.string(">= 1"),
)
cutTrkGsfTrkVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dRToMatchedGsfTrack > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkElecVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestElectron > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkTightElecVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestTightElectron > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkVetoElecVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestVetoElectron > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMuonVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestMuon > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkTightMuonVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestTightMuon > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkLooseMuonVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestLooseMuon > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkTauVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestTau > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkTauHadVeto = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestTauHad > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkTauHadVetoInv = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestTauHad < 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkJetDeltaPhi = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dRMinJet > 0.5"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEcalo = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("caloNewNoPUDRp5CentralCalo < 10"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissOut = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingOuterHits >= 3"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissOut4 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingOuterHits >= 4"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEcaloInv = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("caloNewNoPUDRp5CentralCalo > 10"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEcaloInv50 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("caloNewNoPUDRp5CentralCalo > 50"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissOutInv = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingOuterHits <= 2"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchGenNone = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("genMatchedParticle.promptFinalState.isNull"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchedGen = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("genMatchedParticle.promptFinalState.isNonnull"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchGenElec = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.bestMatchPdgId) == 11"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchGenMuon = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.bestMatchPdgId) == 13"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchGenTau = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.bestMatchPdgId) == 15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchFake = cms.PSet(
    # not matched to tau, electron, or muon
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("\
    genMatchedParticle.directPromptTauDecayProductFinalState.isNull && \
    genMatchedParticle.directHardProcessTauDecayProductFinalState.isNull && \
    abs ( genMatchedParticle.promptFinalState.pdgId ) != 11 && \
    abs ( genMatchedParticle.promptFinalState.pdgId ) != 13"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchGenPhoton = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs ( genMatchedParticle.promptFinalState.pdgId ) == 22"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchNoElecNoMuon = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs ( genMatchedParticle.promptFinalState.pdgId ) != 11 && abs ( genMatchedParticle.promptFinalState.pdgId ) != 13"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNoMuonDRMatch = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deltaRToClosestMuon > 0.8"),
    numberRequired = cms.string(">= 1"),
)
cutTrkArbitration = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 1"),
    arbitration = cms.string("random"),
    alias = cms.string("pick random track"),
)
cutTrkD0 = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackD0WRTPV + " ) < 0.02"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |d0| < 0.02"),
)
cutTrkDZ = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackDZWRTPV + " ) < 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |dz| < 0.5"),
)
cutTrkD0BS = cms.PSet(
    inputCollection = cms.vstring("tracks", "beamspots"),
    cutString = cms.string("fabs ( " + trackD0WRTBeamspot + " ) < 0.02"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |d0| < 0.02"),
)
cutTrkLargeD0 = cms.PSet(
    inputCollection = cms.vstring("tracks", "beamspots"),
    cutString = cms.string(trackD0WRTBeamspot + " > 0.1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |d0| > 0.1"),
)
cutTrkSmallD0 = cms.PSet(
    inputCollection = cms.vstring("tracks", "beamspots"),
    cutString = cms.string(trackD0WRTBeamspot + " < 0.1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |d0| < 0.1"),
)
cutTrkMatchMC = cms.PSet(
    inputCollection = cms.vstring("tracks", "mcparticles"),
    cutString = cms.string("deltaR ( track , mcparticle ) < 0.2"),
    numberRequired = cms.string(">= 1"),
)


##################################################
## mcparticles
##################################################
cutMCPt = cms.PSet(
    inputCollection = cms.vstring("mcparticles"),
    cutString = cms.string("pt > 40"),
    numberRequired = cms.string(">= 1"),
)
cutMCIdElec = cms.PSet(
    inputCollection = cms.vstring("mcparticles"),
    cutString = cms.string("abs ( pdgId ) == 11"),
    numberRequired = cms.string(">= 1"),
)
cutMCPt30 = cms.PSet(
    inputCollection = cms.vstring("mcparticles"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
)


##################################################
## muons
##################################################
cutMuonPt20 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
)
cutMuonPt25 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1"),
)
cutMuonPt35 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 35"),
    numberRequired = cms.string(">= 1"),
)
cutMuonEta21 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
)
cutMuonTightID = cms.PSet (  # Recommended by https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Tight_Muon
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isTightMuonWRTVtx > 0"),
    numberRequired = cms.string(">= 1"),
)
cutMuonLoosePFIso = cms.PSet (  # Recommended by https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("(pfIsolationR04_.sumChargedHadronPt + max (0.0, pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5 * pfIsolationR04_.sumPUPt)) / pt < 0.25"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 muons with #Delta#beta-corrected rel. iso. < 0.25"),
)
cutMuonTightPFIso = cms.PSet (  # Recommended by https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("(pfIsolationR04_.sumChargedHadronPt + max (0.0, pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5 * pfIsolationR04_.sumPUPt)) / pt < 0.15"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 muons with #Delta#beta-corrected rel. iso. < 0.15"),
)
cutMuonPairPt20 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string("== 2"),
)
cutMuonPairPt25 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string("== 2"),
)
cutMuonPairEta21 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string("== 2"),
)
cutMuonPairTightID = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isTightMuonWRTVtx > 0"),
    numberRequired = cms.string("== 2"),
)
cutMuonPairTightPFIso = cms.PSet (  # Recommended by https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
    inputCollection = cms.vstring("muons"),
    cutString = cutMuonTightPFIso.cutString,
    numberRequired = cms.string("== 2"),
    alias = cms.string("== 2 muons with #Delta#beta-corrected rel. iso. < 0.15"),
)
cutMuonArbitration = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 1"),
    arbitration = cms.string("random"),
    alias = cms.string("pick random muon"),
)
cutMuonMetMinusOne = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("metNoMuMinusOnePt > 100"),
    numberRequired = cms.string(">= 1"),
)

##################################################
## muon-muon pairs
##################################################
cutMuMuChargeProduct = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("muon.charge * muon.charge < 0"),
    numberRequired = cms.string(">= 1"),
)
cutMuMuInvMassZLo = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass ( muon , muon ) > " + str(mZPDG - 10)),
    numberRequired = cms.string(">= 1"),
)
cutMuMuInvMassZHi = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    cutString = cms.string("invMass ( muon , muon ) < " + str(mZPDG + 10)),
    numberRequired = cms.string(">= 1"),
)

##################################################
## muon-track pairs
##################################################
cutMuTrkDeltaR = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string("deltaR ( muon , track ) > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMuDR0p1 = cms.PSet(
    inputCollection = cms.vstring("tracks", "muons"),
    cutString = cms.string("deltaR (track, muon) < 0.1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchRecoMu = cms.PSet(
    inputCollection = cms.vstring("tracks", "muons"),
    cutString = cms.string("muon.pt > -1"),
    numberRequired = cms.string(">= 1"),
    arbitration = cms.string("-deltaR ( track, muon)"),
    alias = cms.string("match track to muon"),
)
cutMuTrkInvMass10 = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string(invMassWithMuon ("muon") + " > 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string (">= 1 muon-track pairs with invMass(muon,track) > 10"),
)
cutMuTrkInvMass80To100 = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string(invMassWithMuon ("muon") + " > " + str(mZPDG - 10) + " && " + invMassWithMuon ("muon") + " < " + str(mZPDG + 10)),
    numberRequired = cms.string(">= 1"),
    alias = cms.string (">= 1 muon-track pairs with " + str(mZPDG - 10) + " < invMass(muon,track) < " + str(mZPDG + 10)),
)
cutMuTrkInvMass40To75 = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string(invMassWithMuon ("muon") + " > " + str(mZPDG - 50) + " && " + invMassWithMuon ("muon") + " < " + str(mZPDG - 15)),
    numberRequired = cms.string(">= 1"),
    alias = cms.string (">= 1 muon-track pairs with " + str(mZPDG - 50) + " < invMass(muon,track) < " + str(mZPDG - 15)),
)
cutMuTrkOS = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string("muon.charge * track.charge < 0"),
    numberRequired = cms.string(">= 1"),
)
cutMuTrkDeltaPhi = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string("fabs (deltaPhi (muon, track)) > 2.5"),
    numberRequired = cms.string(">= 1"),
)
cutMuTrkMETBalance = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks", "mets"),
    cutString = cms.string("hypot (muon.px + met.px + track.px, muon.py + met.py + track.py) < 45.0"),
    numberRequired = cms.string(">= 1"),
)

##################################################
## electron-track pairs
##################################################
cutEleTrkDeltaR = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks"),
    cutString = cms.string("deltaR ( electron , track ) > 0.15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkElecDR0p1 = cms.PSet(
    inputCollection = cms.vstring("tracks", "electrons"),
    cutString = cms.string("deltaR (track, electron) < 0.1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchRecoElec = cms.PSet(
    inputCollection = cms.vstring("tracks", "electrons"),
    cutString = cms.string("electron.pt > -1"),
    numberRequired = cms.string(">= 1"),
    arbitration = cms.string("-deltaR ( track, electron)"),
    alias = cms.string("match track to electron"),
)
cutEleTrkInvMass10 = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks"),
    cutString = cms.string(invMassWithElectron ("electron") + " > 10"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string (">= 1 electron-track pairs with invMass(electron,track) > 10"),
)
cutEleTrkInvMass80To100 = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks"),
    cutString = cms.string(invMassWithMuon ("electron") + " > " + str(mZPDG - 10) + " && " + invMassWithMuon ("electron") + " < " + str(mZPDG + 10)),
    numberRequired = cms.string(">= 1"),
    alias = cms.string (">= 1 electron-track pairs with " + str(mZPDG - 10) + " < invMass(electron,track) < " + str(mZPDG + 10)),
)
cutEleTrkInvMass40To75 = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks"),
    cutString = cms.string(invMassWithMuon ("electron") + " > " + str(mZPDG - 50) + " && " + invMassWithMuon ("electron") + " < " + str(mZPDG - 15)),
    numberRequired = cms.string(">= 1"),
    alias = cms.string (">= 1 electron-track pairs with " + str(mZPDG - 50) + " < invMass(electron,track) < " + str(mZPDG - 15)),
)
cutEleTrkOS = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks"),
    cutString = cms.string("electron.charge * track.charge < 0"),
    numberRequired = cms.string(">= 1"),
)
cutEleTrkDeltaPhi = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks"),
    cutString = cms.string("fabs (deltaPhi (electron, track)) > 2.5"),
    numberRequired = cms.string(">= 1"),
)
cutEleTrkMETBalance = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks", "mets"),
    cutString = cms.string("hypot (electron.px + met.px + track.px, electron.py + met.py + track.py) < 45.0"),
    numberRequired = cms.string(">= 1"),
)

##################################################
## electrons
##################################################
cutElectronPt24 = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 24"),
    numberRequired = cms.string(">= 1"),
)
cutElectronPt25 = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1"),
)
cutElectronPt35 = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 35"),
    numberRequired = cms.string(">= 1"),
)
cutElectronPt50 = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
)
cutElectronEta21 = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
)
cutElectronTightID = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("passesTightID_noIsolation > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with isTightElectronWRTVtx > 0"),
)
cutElectronTightPFIso = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("((fabs (superCluster.eta) <= 1.479) && (((pfIso_.sumChargedHadronPt + max (0.0, pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho * AEff)) / pt) < 0.0591)) \
                         || ((fabs (superCluster.eta) >  1.479) && (((pfIso_.sumChargedHadronPt + max (0.0, pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho * AEff)) / pt) < 0.0759))"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with tight #rho-corrected rel. iso."),
)
cutElectronArbitration = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 1"),
    arbitration = cms.string("random"),
    alias = cms.string("pick random electron"),
)
cutElectronMetMinusOne = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("metMinusOnePt > 100"),
    numberRequired = cms.string(">= 1"),
)

##################################################
## taus
##################################################
cutTauPt50 = cms.PSet (
    inputCollection = cms.vstring("taus"),
    cutString = cms.string("pt > 50"),
    numberRequired = cms.string(">= 1"),
)
cutTauEta21 = cms.PSet (
    inputCollection = cms.vstring("taus"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
)
cutTauTightID = cms.PSet (
    inputCollection = cms.vstring("taus"),
    cutString = cms.string("passesDecayModeReconstruction && passesLightFlavorRejection"),
    numberRequired = cms.string(">= 1"),
)
cutTauTightPFIso = cms.PSet (
    inputCollection = cms.vstring("taus"),
    cutString = cms.string("passesTightCombinedIsolation"),
    numberRequired = cms.string(">= 1"),
)
cutTauArbitration = cms.PSet(
    inputCollection = cms.vstring("taus"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 1"),
    arbitration = cms.string("random"),
    alias = cms.string("pick random tau"),
)
cutTrkTauDR0p1 = cms.PSet(
    inputCollection = cms.vstring("tracks", "taus"),
    cutString = cms.string("deltaR (track, tau) < 0.1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchRecoTau = cms.PSet(
    inputCollection = cms.vstring("tracks", "taus"),
    cutString = cms.string("tau.pt > -1"),
    numberRequired = cms.string(">= 1"),
    arbitration = cms.string("-deltaR ( track, tau)"),
    alias = cms.string("match track to tau"),
)
cutTauMetMinusOne = cms.PSet (
    inputCollection = cms.vstring("taus"),
    cutString = cms.string("metNoMuMinusOnePt > 100"),
    numberRequired = cms.string(">= 1"),
)
