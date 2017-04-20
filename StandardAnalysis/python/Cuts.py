import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.Triggers import *
from DisappTrks.StandardAnalysis.METFilters import *
from OSUT3Analysis.Configuration.cutUtilities import *
import os

##############################
##### Constants          #####
##############################

mZPDG = 91.1876  # Z mass from http://pdglive.lbl.gov/DataBlock.action?node=S044M

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

cutNumPV14to18 = cms.PSet (
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("numPVReco >= 14 && numPVReco <= 18"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("14-18 good primary vertices"),
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
cutMetBadPFMuonFilter = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("badPFMuonFilter"),
    numberRequired = cms.string(">= 1"),
)
cutMetBadChargedCandidateFilter = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("badChargedCandidateFilter"),
    numberRequired = cms.string(">= 1"),
)
cutMetFilters = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("badPFMuonFilter && badChargedCandidateFilter"),
    numberRequired = cms.string(">= 1"),
)

##################################################
## track-met pairs
##################################################
cutMuonLowMT = cms.PSet(
    inputCollection = cms.vstring("muons", "mets"),
    cutString = cms.string("transMass (muon, met) < 40"),
    numberRequired = cms.string(">= 1"),
)
cutElectronLowMT = cms.PSet(
    inputCollection = cms.vstring("electrons", "mets"),
    cutString = cms.string("transMass (electron, met) < 40"),
    numberRequired = cms.string(">= 1"),
)

cutMuonHighMT = cms.PSet(
    inputCollection = cms.vstring("muons", "mets"),
    cutString = cms.string("transMass (muon, met) > 40"),
    numberRequired = cms.string(">= 1"),
)
cutElectronHighMT = cms.PSet(
    inputCollection = cms.vstring("electrons", "mets"),
    cutString = cms.string("transMass (electron, met) > 40"),
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
cutJetPt55 = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 55"),
    numberRequired = cms.string(">= 1"),
)
cutJetPtJECUp = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt * (1 + jecUncertainty) > 110"),
    numberRequired = cms.string(">= 1"),
)
cutJetPtJECDown = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt * (1 - jecUncertainty) > 110"),
    numberRequired = cms.string(">= 1"),
)
cutJetJERSmearedPt = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("smearedPt > 110"),
    numberRequired = cms.string(">= 1"),
)
cutJetJERSmearedPtJECUp = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("smearedPt * (1 + jecUncertainty) > 110"),
    numberRequired = cms.string(">= 1"),
)
cutJetJERSmearedPtJECDown = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("smearedPt * (1 - jecUncertainty) > 110"),
    numberRequired = cms.string(">= 1"),
)
cutJetJERSmearedPtUp = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("smearedPtUp > 110"),
    numberRequired = cms.string(">= 1"),
)
cutJetJERSmearedPtDown = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("smearedPtDown > 110"),
    numberRequired = cms.string(">= 1"),
)
cutJetPt30 = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
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
cutNJetsEQ1 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nJets == 1"),
    numberRequired = cms.string(">= 1"),
)
cutNJetsLE2 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nJets <= 2"),
    numberRequired = cms.string(">= 1"),
)
cutNJetsGE1 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("nJets >= 1"),
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
cutTrkNValidPixelHits3 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitPattern_.numberOfValidPixelHits >= 3"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNValidPixelEndcapHits2 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitPattern_.numberOfValidPixelBarrelHits == 2"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNValidPixelBarrelHits3 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitPattern_.numberOfValidPixelBarrelHits == 3"),
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
    cutString = cms.string("hitDrop_missingMiddleHits == 0"),
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
cutTrkNMissOut0 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits >= 0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissOut1 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits >= 1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissOut2 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits >= 2"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissOut = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits >= 3"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissOut4 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits >= 4"),
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
    cutString = cms.string("hitAndTOBDrop_bestTrackMissingOuterHits <= 2"),
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
    cutString = cms.string("abs (genMatchedParticle.bestMatchPdgId) == 0"),
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
cutMCCharginoChargino = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("isCharginoChargino"),
    numberRequired = cms.string(">= 1"),
)
cutMCCharginoNeutralino = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("isCharginoNeutralino"),
    numberRequired = cms.string(">= 1"),
)


##################################################
## muons
##################################################

cutMuonPt = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 22"),
    numberRequired = cms.string(">= 1"),
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Switching muon pt cut to >26 GeV since we are in " + os.environ["CMSSW_VERSION"] + "..."
    cutMuonPt.cutString = cms.string("pt > 26")
else:
    print "# Using muon pt cut of >22 GeV since we are in " + os.environ["CMSSW_VERSION"] + "..."

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

cutMuonPairPt = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 22"),
    numberRequired = cms.string("== 2"),
)

# already printed info message above
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    cutMuonPairPt.cutString = cms.string("pt > 26")

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
cutMuonExactlyOne = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
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
## muon-jet pairs
##################################################
cutMuonPairJetDeltaRVeto = cms.PSet(
    inputCollection = cms.vstring("muons", "jets"),
    cutString = cms.string("deltaR(muon, jet) < 0.5"),
    numberRequired = cms.string("== 0"),
    isVeto = cms.bool(True),
    alias = cms.string("muon near jet veto")
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
cutElectronExactlyOne = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 1"),
)
cutElectronExactlyZero = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("== 0"),
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

##################################################
## Cuts used in the trigger efficiency measurement
## Produced only with variableProducers.append('EventTriggerVarProducer')
##################################################

passesMainTrigger = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("passesMainTrigger > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("HLT_MET75_IsoTrk50_v")
)
passesHigherMetTrigger = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("passesHigherMetTrigger > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("HLT_MET90_IsoTrk50_v")
)
passesHLTMet75 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("passesHLTMet75 > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("hltMET75")
)
passesHLTMet90 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("passesHLTMet90 > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("hltMET90")
)

cutLeadJetCentral = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs(etaJetLeading) <= 2.4"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Require leading jet to be central")
)

cutTrkEta25 = cms.PSet( # Cut for trigger efficiency measurement
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs(eta) < 2.5"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNormalizedChi2 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("normalizedChi2 < 10.0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNLayersWMeasurement = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitPattern_.trackerLayersWithMeasurement >= 6"),
    numberRequired = cms.string(">= 1"),
)
cutTrkIsoTight = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string(" ( trackIsoNoPUDRp3 / pt ) < 0.01"),
    numberRequired = cms.string(">= 1"),
)
cutLeadTrkMatchHLTTrack = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("leadTrackMatchToHLTTrack > 0"),
    numberRequired = cms.string(">= 1"),
)
cutAnyTrkMatchHLTTrack = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("anyTrackMatchToHLTTrack > 0"),
    numberRequired = cms.string(">= 1"),
)
# to add -- deltaR match to charginos for MC

cutMuonNMissIn = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("missingInnerHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutMuonNMissMid = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("missingMiddleHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutLeadMuonMatchHLTTrack = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("leadMuonMatchToHLTTrack > 0"),
    numberRequired = cms.string(">= 1"),
)
cutAnyMuonMatchHLTTrack = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("anyMuonMatchToHLTTrack > 0"),
    numberRequired = cms.string(">= 1"),
)
