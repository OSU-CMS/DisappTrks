import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.Triggers import *
from DisappTrks.StandardAnalysis.METFilters import *
from DisappTrks.TriggerAnalysis.AllTriggers import *
from OSUT3Analysis.Configuration.cutUtilities import *
from DisappTrks.StandardAnalysis.protoConfig_cfg import UseCandidateTracks
from OSUT3Analysis.AnaTools.osuAnalysis_cfi import dataFormat
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
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    cutMet.cutString = cms.string("noMuPt > 120")
    print("# MetNoMu > 120 GeV")
else:
    print("# MetNoMu > 100 GeV")

cutVetoMetPhiHEM1516 = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("phi < -1.6 || phi > -0.6"),
    numberRequired = cms.string(">= 1"),
)

cutVetoJetsHEM1516 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("jetInHEM1516 == 0"),
    numberRequired = cms.string(">= 1"),
)

cutVetoJetMap2022 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("jetVeto2022 == 1"),
    numberRequired = cms.string(">= 1"),
)

cutDummyMet = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("noMuPt > -1"),
    numberRequired = cms.string(">= 1"),
)
cutLowMet = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt < 60"),
    numberRequired = cms.string(">= 1"),
)
cutMet275 = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("pt > 275"),
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
cutMetPassecalBadCalibFilterUpdate = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("passecalBadCalibFilterUpdate"),
    numberRequired = cms.string(">= 1"),
)
# This was used for Run 2 and is different for Run 3; changing the name here to not have to
# change this cut in every selection that uses it
# cutMetFilters = cms.PSet(
#     inputCollection = cms.vstring("mets"),
#     cutString = cms.string("badPFMuonFilter && badChargedCandidateFilter && passecalBadCalibFilterUpdate"),
#     numberRequired = cms.string(">= 1"),
# )
cutMetFilters = cms.PSet(
    inputCollection = cms.vstring("mets"),
    cutString = cms.string("passecalBadCalibFilterUpdate"),
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
cutVetoL1PrefiringJets = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("!hasPrefiredJets"),
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
    alias = cms.string("veto pairs of jets with #Delta#phi > 2.5"),
)
cutLeadingJetMetPhi = cms.PSet(
    inputCollection = cms.vstring("eventvariables", "mets"),
    cutString = cms.string("fabs( dPhi (met.noMuPhi, eventvariable.phiJetLeading) ) > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta#phi(E_{T}^{miss},jet) > 0.5"),
)
cutLeadingJetMetPhiInvert = cms.PSet(
    inputCollection = cms.vstring("eventvariables", "mets"),
    cutString = cms.string("fabs( dPhi (met.noMuPhi, eventvariable.phiJetLeading) ) < 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta#phi(E_{T}^{miss},jet) < 0.5"),
)
cutLeadingJetTauMetMinusOnePhi = cms.PSet(
    inputCollection = cms.vstring("eventvariables", "taus"),
    cutString = cms.string("fabs( dPhi (tau.metNoMuMinusOnePhi, eventvariable.phiJetLeading) ) > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta#phi(E_{T}^{miss},jet) > 0.5"),
)
cutLeadingJetTauMetMinusOnePhiInvert = cms.PSet(
    inputCollection = cms.vstring("eventvariables", "taus"),
    cutString = cms.string("fabs( dPhi (tau.metNoMuMinusOnePhi, eventvariable.phiJetLeading) ) < 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta#phi(E_{T}^{miss},jet) < 0.5"),
)
cutSubleadingJetMetPhi = cms.PSet(
    inputCollection = cms.vstring("eventvariables", "mets"),
    cutString = cms.string("fabs( dPhi (met.noMuPhi, eventvariable.phiJetSubleading) ) > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta#phi(E_{T}^{miss},jet) > 0.5"),
)
cutJetMetPhi = cms.PSet(
    inputCollection = cms.vstring("eventvariables", "mets"),
    cutString = cms.string("fabs( dPhi (met.noMuPhi, eventvariable.phiJetLeading) ) > 0.5 && fabs( dPhi (met.noMuPhi, eventvariable.phiJetSubleading) ) > 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("#Delta#phi(E_{T}^{miss},jet) > 0.5"),
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
# https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVRun2017
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    cutJetTightLepVeto.cutString = cms.string("\
    ((\
    neutralHadronEnergyFraction<0.90 && \
    neutralEmEnergyFraction<0.90 && \
    (chargedMultiplicity + neutralMultiplicity)>1 && \
    muonEnergyFraction<0.8) && \
    ((abs(eta)<=2.4 && chargedHadronEnergyFraction>0 && chargedMultiplicity>0 && chargedEmEnergyFraction<0.80) || \
    abs(eta)>2.4) && \
    abs(eta)<=2.7) \
    || (neutralEmEnergyFraction>0.02 && neutralEmEnergyFraction<0.99 && neutralMultiplicity>2 && abs(eta)<=3.0 && abs(eta)>2.7) \
    || (neutralEmEnergyFraction<0.90 && neutralHadronEnergyFraction>0.02 && neutralMultiplicity>10 && abs(eta)>3.0)")
    print('# Using 2017 reqs for Jet TightLepVeto')

# https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVRun2018
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    cutJetTightLepVeto.cutString = cms.string("\
    (\
    (abs(eta) <= 2.6 && neutralHadronEnergyFraction<0.90 && neutralEmEnergyFraction<0.90 && (chargedMultiplicity + neutralMultiplicity)>1 && muonEnergyFraction<0.8 && chargedHadronEnergyFraction>0 && chargedMultiplicity>0 && chargedEmEnergyFraction<0.80) || \
    (abs(eta) > 2.6 && abs(eta) <= 2.7 && neutralHadronEnergyFraction<0.90 && neutralEmEnergyFraction<0.99 && muonEnergyFraction<0.8 && chargedMultiplicity>0 && chargedEmEnergyFraction<0.8) || \
    (abs(eta) > 2.7 && abs(eta) <= 3.0 && neutralEmEnergyFraction>0.02 && neutralEmEnergyFraction<0.99 && neutralMultiplicity>2) || \
    (abs(eta) > 3.0 && neutralEmEnergyFraction<0.90 && neutralHadronEnergyFraction>0.2 && neutralMultiplicity>10)\
    )")
    print('# Using 2018 reqs for Jet TightLepVeto')

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    cutJetTightLepVeto.cutString = cms.string("\
    (\
    (abs(eta) <= 2.6 && neutralHadronEnergyFraction<0.99 && neutralEmEnergyFraction<0.90 && (chargedMultiplicity + neutralMultiplicity)>1 && muonEnergyFraction<0.8 && chargedHadronEnergyFraction>0.01 && chargedMultiplicity>0 && chargedEmEnergyFraction<0.80) || \
    (abs(eta) > 2.6 && abs(eta) <= 2.7 && neutralHadronEnergyFraction<0.90 && neutralEmEnergyFraction<0.99 && muonEnergyFraction<0.8 && chargedMultiplicity>0 && chargedEmEnergyFraction<0.8) || \
    (abs(eta) > 2.7 && abs(eta) <= 3.0 && neutralEmEnergyFraction<0.99 && neutralHadronEnergyFraction<0.99 && neutralMultiplicity>1) || \
    (abs(eta) > 3.0 && neutralEmEnergyFraction<0.4 && neutralMultiplicity>10)\
    )")
    print('# Using 2022 reqs for Jet TightLepVeto https://twiki.cern.ch/twiki/bin/view/CMS/JetID13p6TeV')

#############
# pair of jets pt > 30
# HT > 250 GeV
#############

cutJetPairSmearedPt30 = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("smearedPt > 30"),
    numberRequired = cms.string(">= 2"),
)
cutJetPairEta = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("fabs ( eta ) < 2.4"),
    numberRequired = cms.string(">= 2"),
)
cutJetPairTightLepVeto = copy.deepcopy(cutJetTightLepVeto)
cutJetPairTightLepVeto.numberRequired = cms.string(">= 2")
cutJetPairTightLepVeto.alias = cms.string(">= 2 jets passing TightLepVeto ID")

cutHTJets250 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("HTJets > 250"),
    numberRequired = cms.string(">= 1"),
)

##################################################
## tracks
##################################################
cutTrkDummy = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string(">= 0"),
)
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
cutTrkPt25 = cms.PSet(  # LOWER PT CUT FOR SKIMMING
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1"),
)
cutTrkPt20 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 2.1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEta15 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs ( eta ) < 1.5"),
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
cutTrkInvestigate2017Ineff = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("eta > 0.35 && eta < 1.42 && phi > 2.8"),
    numberRequired = cms.string(">= 1"),
)
cutTrkInvestigate2018Ineff = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("eta > 0.2 && eta < 1.42 && phi > 0.4 && phi < 0.8"),
    numberRequired = cms.string(">= 1"),
)
cutTrkTOBCrack = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("!inTOBCrack"),
    numberRequired = cms.string(">= 1"),
)
cutTrk2017LowEfficiencyRegion = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("phi < 2.7 || eta < 0 || eta > 1.42"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Veto low efficiency 2017 eta-phi region"),
)
cutTrk2018LowEfficiencyRegion = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("phi < 0.4 || eta < 0 || eta > 1.42 || phi > 0.8"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Veto low efficiency 2018 eta-phi region"),
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
cutTrkIsHighPurity = cms.PSet( # to be used in signal MC trigger efficiency
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("isHighPurityTrack"),
    numberRequired = cms.string(">= 1"),
)

cutDeepSets = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("")
)
# cutTrkEtaEcalCrackVeto = cms.PSet(  # TRACK ETA:  NOT IN ECAL CRACKS:  UPDATE CRACK BOUNDARIES
#     inputCollection = cms.vstring("tracks"),
#     cutString = cms.string("fabs ( eta ) "),
#     numberRequired = cms.string(">= 1"),
# )

cutTrkDeepSets = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("deepSetsElectronScore > 0.5"),
    numberRequired = cms.string('>= 1'),
)

cutTrkFakeNN = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fakeTrackScore > 0.5"),
    numberRequired = cms.string('>= 1'),
)

########################################
##### track number of valid hits   #####
########################################

cutTrkNValidPixelHits = {
    x : cms.PSet (
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("hitPattern_.numberOfValidPixelHits >= " + str(x)),
            numberRequired = cms.string(">= 1"),
        ) 
    for x in range(1, 10)
}

cutTrkNValidHits = {
    x : cms.PSet (
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("hitPattern_.numberOfValidHits >= " + str(x)),
            numberRequired = cms.string(">= 1"),
        )
    for x in range(1, 10)
}

cutTrkNValidHitsExclusive = {
    x : cms.PSet (
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("hitPattern_.numberOfValidHits == " + str(x)),
            numberRequired = cms.string(">= 1"),
        )
    for x in range(1, 10)
}

cutTrkNLayers = {
    x : cms.PSet (
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("hitPattern_.trackerLayersWithMeasurement >= " + str(x)),
            numberRequired = cms.string(">= 1"),
        )
    for x in range(1, 10)
}

cutTrkNLayersExclusive = {
    x : cms.PSet (
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("hitPattern_.trackerLayersWithMeasurement == " + str(x)),
            numberRequired = cms.string(">= 1"),
        )
    for x in range(1, 10)
}

cutTrkNValidPixelHitsSignal = cutTrkNValidPixelHits[3]
cutTrkNValidHitsSignal = cutTrkNValidHits[7]
cutTrkNValidHitsVariations = {"NHits" + str(x) : cutTrkNValidHitsExclusive[x] for x in range(3, 7)}
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    cutTrkNValidPixelHitsSignal = cutTrkNValidPixelHits[4]
    cutTrkNValidHitsSignal = cutTrkNValidHits[4]
    cutTrkNValidHitsVariations.update({"NHits7plus" : cutTrkNValidHits[7]})
    print("# Hits requirement: 4/4")
else:
    print("# Hits requirement: 3/7")

cutTrkNValidHitsLE = {
    x : cms.PSet (
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("hitPattern_.numberOfValidHits <= " + str(x)),
            numberRequired = cms.string(">= 1"),
        )
    for x in range(2, 10)
}

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

#####################################################
##### track number of layers with measurement   #####
#####################################################

cutTrkNLayersExclusive = {
    x : cms.PSet (
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("hitPattern_.trackerLayersWithMeasurement == " + str(x)),
            numberRequired = cms.string(">= 1"),
        )
    for x in range(3, 7)
}

cutTrkAtMostNLayers = {
    x : cms.PSet (
        inputCollection = cms.vstring("tracks"),
        cutString = cms.string("hitPattern_.trackerLayersWithMeasurement <= " + str(x)),
        numberRequired = cms.string(">= 1"),
    )
    for x in range(3, 7)
}

cutTrkNLayers = {
    x : cms.PSet (
        inputCollection = cms.vstring("tracks"),
        cutString = cms.string("hitPattern_.trackerLayersWithMeasurement >= " + str(x)),
        numberRequired = cms.string(">= 1"),
    )
    for x in range(3, 7)
}

cutTrkNLayersVariations = {
    "NLayers3"     : cutTrkNLayersExclusive[3],
    "NLayers4"     : cutTrkNLayersExclusive[4],
    "NLayers5"     : cutTrkNLayersExclusive[5],
    "NLayers6plus" : cutTrkNLayers[6],
}

#####################################################

cutTrkNMissIn = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingInnerHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNoInvalidInnerHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("numberOfTotallyOffOrBadInnerHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissMid = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitDrop_missingMiddleHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNMissMidNoDrop = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("missingMiddleHits == 0"),
    numberRequired = cms.string(">= 1"),
) 
cutTrkNoInvalidMiddleHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("numberOfTotallyOffOrBadMiddleHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkAllowedThreeLayerHitPattern = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("isAllowedThreeLayerHitPattern"),
    numberRequired = cms.string(">= 1"),
)
cutTrkFourLayersAnyHitQuality = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("expectedIncludeInactivePixelHits == 4"),
    numberRequired = cms.string(">= 1"),
)
cutTrkIso = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string(" ( trackIsoNoPUDRp3 / pt ) < 0.05"),
    numberRequired = cms.string(">= 1"),
)
if not UseCandidateTracks:
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
        # This cut does something very similar to the old trackIsoNoPUDRp3. pfIsolationDR03_.chargedHadronIso sums the pT of all PF charged pions that are compatible to the PV in a DR 0.3 cone around an IsolatedTrack. The 0.05 requirement is the same as the one in the HLT_MET105_IsoTrk50 path. In this way, the track isolation is still PU independent, which makes the efficiency of the cut higher.
        cutTrkIso.cutString = cms.string (" (pfIsolationDR03_.chargedHadronIso / pt) < 0.05")

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
cutTrkJetDeltaPhiInvert = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("dRMinJet < 0.5"),
    numberRequired = cms.string(">= 1"),
)
cutTrkEcalo = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("caloNewNoPUDRp5CentralCalo < 10"),
    numberRequired = cms.string(">= 1"),
)
# If using MiniAOD only processing, the ecalo cut has to be changed to the CMSSW standard
if dataFormat == 'MINI_AOD_ONLY_2022_CUSTOM':
    cutTrkEcalo.cutString = cms.string ("(matchedCaloJetEmEnergy + matchedCaloJetHadEnergy) < 10")

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
cutTrkNMissOutNoDrop = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("bestTrackMissingOuterHits >= 3"),
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
# If using MiniAOD only processing, the ecalo cut has to be changed to the CMSSW standard
if dataFormat == 'MINI_AOD_ONLY_2022_CUSTOM':
    cutTrkEcaloInv.cutString = cms.string ("(matchedCaloJetEmEnergy + matchedCaloJetHadEnergy) > 10")
# If using MiniAOD only processing, the ecalo cut has to be changed to the CMSSW standard
if dataFormat == 'MINI_AOD_ONLY_2022_CUSTOM':
    cutTrkEcaloInv50.cutString = cms.string ("(matchedCaloJetEmEnergy + matchedCaloJetHadEnergy) > 50")

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
cutTrkMatchChargino = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.promptOrTauDecayPdgId) == 1000024"), # N.B. "promptOrTauDecay" changed to "promptOrTauDecay"
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchCharginoByMother = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.promptOrTauDecay.motherRef.pdgId) == 1000024 && abs (genMatchedParticle.promptOrTauDecayPdgId) == 1000022"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchGenElec = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.promptOrTauDecayPdgId) == 11"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchGenMuon = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.promptOrTauDecayPdgId) == 13"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchGenTau = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.promptOrTauDecayPdgId) == 15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchReal = cms.PSet(
    # matched to a charged lepton
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.promptOrTauDecayPdgId) == 11 || abs (genMatchedParticle.promptOrTauDecayPdgId) == 13 || abs (genMatchedParticle.promptOrTauDecayPdgId) == 15"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchFake = cms.PSet(
    # not matched to any genParticle
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("abs (genMatchedParticle.promptOrTauDecayPdgId) == 0"),
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
cutTrkLargeIsoDiffPos = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("((pfIsolationDR03_.chargedHadronIso + pfIsolationDR03_.puChargedHadronIso) / pt)-(matchedCandidateTrack.trackIsoNoPUDRp3 / matchedCandidateTrack.pt) > 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("large difference in Isolation, candidateTrack << isolatedtrack"),
)
cutTrkLargeIsoDiffNeg = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("((pfIsolationDR03_.chargedHadronIso + pfIsolationDR03_.puChargedHadronIso) / pt)-(matchedCandidateTrack.trackIsoNoPUDRp3 / matchedCandidateTrack.pt) < 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("large difference in Isolation, candidateTrack >> isolatedtrack"),
)
cutTrkD0 = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackD0WRTPV + " ) < 0.02"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |d0| < 0.02"),
)
cutTrkSidebandD0 = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackD0WRTPV + " ) >= 0.02 && fabs ( " + trackD0WRTPV + " ) < 0.1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with 0.02 <= |d0| < 0.1"),
)
cutTrkInvertD0 = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackD0WRTPV + " ) >= 0.02"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |d0| >= 0.02"),
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

if not UseCandidateTracks:
    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
        cutTrkD0.inputCollection = cms.vstring("tracks")
        cutTrkD0.cutString = cms.string("fabs (dxy) < 0.02")

        cutTrkSidebandD0.inputCollection = cms.vstring("tracks")
        cutTrkSidebandD0.cutString = cms.string("fabs (dxy) >= 0.02 && fabs (dxy) < 0.1")

        cutTrkInvertD0.inputCollection = cms.vstring("tracks")
        cutTrkInvertD0.cutString = cms.string("fabs (dxy) >= 0.02")

        cutTrkDZ.inputCollection = cms.vstring("tracks")
        cutTrkDZ.cutString = cms.string("fabs (dz) < 0.5")

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
# reject charginos getting to the muon detector
cutCharginoDecayLength3m = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("decayLength_1000024_0 >= 3000.0"),
    numberRequired = cms.string("== 0"),
)

##################################################
## muons
##################################################

cutMuonMatchToTrigObj = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("match_HLT_IsoMu20_v || match_HLT_IsoTkMu20_v"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 muons firing trigger"),
)

cutMuonPt = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 22"),
    numberRequired = cms.string(">= 1"),
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print("# Muon PT cut: >26 GeV (2016)")
    cutMuonMatchToTrigObj.cutString = cms.string ("match_HLT_IsoMu24_v || match_HLT_IsoTkMu24_v")
    cutMuonPt.cutString = cms.string("pt > 26")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print("# Muon PT cut: >29 GeV (2017)")
    cutMuonMatchToTrigObj.cutString = cms.string ("match_HLT_IsoMu27_v") 
    cutMuonPt.cutString = cms.string("pt > 29")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print("# Muon PT cut: >26 GeV (2018)")
    cutMuonMatchToTrigObj.cutString = cms.string ("match_HLT_IsoMu24_v") 
    cutMuonPt.cutString = cms.string("pt > 26")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    print("# Muon PT cut: >26 GeV (2022) FIXME")
    cutMuonMatchToTrigObj.cutString = cms.string ("match_HLT_IsoMu24_v")
    cutMuonPt.cutString = cms.string("pt > 26")
else:
    print("# Muon PT cut: >22 GeV (2015)")

cutMuonPt35 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 35"),
    numberRequired = cms.string(">= 1"),
)
cutMuonPt55 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 55"),
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

cutMuonVeryTightPFIso= cms.PSet (  # Recommended by https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("(pfIsolationR04_.sumChargedHadronPt + max (0.0, pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5 * pfIsolationR04_.sumPUPt)) / pt < 0.1"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 muons with #Delta#beta-corrected rel. iso. < 0.1"),
)

cutMuonPairPt = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 22"),
    numberRequired = cms.string("== 2"),
)

# already printed info message above
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    cutMuonPairPt.cutString = cms.string("pt > 26")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    cutMuonPairPt.cutString = cms.string("pt > 29")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    cutMuonPairPt.cutString = cms.string("pt > 26")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
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
cutMuonPairNMissIn = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("missingInnerHitsFromTrackerLayersWithoutMeasurements == 0"),
    numberRequired = cms.string(">= 2"),
)
cutMuonPairNMissMid = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("missingMiddleHitsFromTrackerLayersWithoutMeasurements == 0"),
    numberRequired = cms.string(">= 2"),
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
## electron-electron pairs
##################################################
cutEEChargeProduct = cms.PSet(
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("electron.charge * electron.charge < 0"),
    numberRequired = cms.string(">= 1"),
)
cutEEInvMassZLo = cms.PSet(
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("invMass ( electron , electron ) > " + str(mZPDG - 10)),
    numberRequired = cms.string(">= 1"),
)
cutEEInvMassZHi = cms.PSet(
    inputCollection = cms.vstring("electrons", "electrons"),
    cutString = cms.string("invMass ( electron , electron ) < " + str(mZPDG + 10)),
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
cutMuTrkMatch = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string("deltaR ( muon , track ) < 0.15"),
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
cutMuTrkSS = cms.PSet(
    inputCollection = cms.vstring("muons", "tracks"),
    cutString = cms.string("muon.charge * track.charge > 0"),
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
    cutString = cms.string(invMassWithElectron ("electron") + " > " + str(mZPDG - 10) + " && " + invMassWithElectron ("electron") + " < " + str(mZPDG + 10)),
    numberRequired = cms.string(">= 1"),
    alias = cms.string (">= 1 electron-track pairs with " + str(mZPDG - 10) + " < invMass(electron,track) < " + str(mZPDG + 10)),
)
cutEleTrkInvMass40To75 = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks"),
    cutString = cms.string(invMassWithElectron ("electron") + " > " + str(mZPDG - 50) + " && " + invMassWithElectron ("electron") + " < " + str(mZPDG - 15)),
    numberRequired = cms.string(">= 1"),
    alias = cms.string (">= 1 electron-track pairs with " + str(mZPDG - 50) + " < invMass(electron,track) < " + str(mZPDG - 15)),
)
cutEleTrkOS = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks"),
    cutString = cms.string("electron.charge * track.charge < 0"),
    numberRequired = cms.string(">= 1"),
)
cutEleTrkSS = cms.PSet(
    inputCollection = cms.vstring("electrons", "tracks"),
    cutString = cms.string("electron.charge * track.charge > 0"),
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

cutElectronMatchToTrigObj = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("match_HLT_Ele22_eta2p1_WPLoose_Gsf_v"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons firing trigger"),
)

cutElectronPt = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1"),
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print("# Electron PT cut: >25 GeV (2016)")
    cutElectronMatchToTrigObj.cutString = cms.string ("match_HLT_Ele25_eta2p1_WPTight_Gsf_v")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print("# Electron PT cut: >35 GeV (2017)")
    cutElectronPt.cutString = cms.string("pt > 35")
    cutElectronMatchToTrigObj.cutString = cms.string("match_HLT_Ele35_WPTight_Gsf_v")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print("# Electron PT cut: >32 GeV (2018)")
    cutElectronPt.cutString = cms.string("pt > 32")
    cutElectronMatchToTrigObj.cutString = cms.string("match_HLT_Ele32_WPTight_Gsf_v")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    print("# Electron PT cut: >32 GeV (2022) FIXME")
    cutElectronPt.cutString = cms.string("pt > 32")
    cutElectronMatchToTrigObj.cutString = cms.string("match_HLT_Ele32_WPTight_Gsf_v")
else:
    print("# Electron PT cut: >25 GeV (2015)")

# this should be the final printout for what we're switching based on CMSSW_VERSION
print("########################################################################")

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
cutElectronPt55 = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 55"),
    numberRequired = cms.string(">= 1"),
)
cutElectronEta21 = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
)
cutElectronEta24 = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string(">= 1"),
)
cutElectronTightID = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("passesTightID_noIsolation_LegacySpring15 > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with isTightElectronWRTVtx (Legacy Spring15) > 0"),
)
cutElectronTightPFIso = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("((fabs (superCluster.eta) <= 1.479) && (((pfIso_.sumChargedHadronPt + max (0.0, pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho * AEff)) / pt) < 0.0591)) \
                         || ((fabs (superCluster.eta) >  1.479) && (((pfIso_.sumChargedHadronPt + max (0.0, pfIso_.sumNeutralHadronEt + pfIso_.sumPhotonEt - rho * AEff)) / pt) < 0.0759))"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with tight #rho-corrected rel. iso."),
)
cutElectronVIDTightID = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("passesVID_tightID"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with passesVID_tightID (ID + iso)"),
)
cutElectronD02017 = cms.PSet (
    inputCollection = cms.vstring("electrons", "eventvariables"),
    cutString = cms.string("((fabs (electron.superCluster.eta) <= 1.479) && (fabs (" + electronD0WRTPV + ") < 0.05)) \
                         || ((fabs (electron.superCluster.eta) >  1.479) && (fabs (" + electronD0WRTPV + ") < 0.10))"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with |d0| < 0.05, 0.10 (EB, EE)"),
)
cutElectronDZ2017 = cms.PSet (
    inputCollection = cms.vstring("electrons", "eventvariables"),
    cutString = cms.string("((fabs (electron.superCluster.eta) <= 1.479) && (fabs (" + electronDZWRTPV + ") < 0.10)) \
                         || ((fabs (electron.superCluster.eta) >  1.479) && (fabs (" + electronDZWRTPV + ") < 0.20))"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 electrons with |dz| < 0.10, 0.20 (EB, EE)"),
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

cutElectronPairPt = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string("== 2"),
)
# Reminder -- this could (and probably should?) change to 35/25 in 2017 and 32/25 in 2018. But possibly 25/25 is fine with trigger issues...not terribly important?

cutElectronPairEta21 = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string("== 2"),
)
cutElectronPairTightID = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("passesTightID_noIsolation_LegacySpring15 > 0"),
    numberRequired = cms.string("== 2"),
)
cutElectronPairTightPFIso = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cutElectronTightPFIso.cutString,
    numberRequired = cms.string("== 2"),
    alias = cms.string("== 2 electrons with tight #rho-corrected rel. iso."),
)
cutElectronPairVIDTightID = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("passesVID_tightID"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string(">= 2 electrons with passesVID_tightID (ID + iso)"),
)
cutElectronPairD02017 = cms.PSet (
    inputCollection = cms.vstring("electrons", "eventvariables"),
    cutString = cms.string("((fabs (electron.superCluster.eta) <= 1.479) && (fabs (" + electronD0WRTPV + ") < 0.05)) \
                         || ((fabs (electron.superCluster.eta) >  1.479) && (fabs (" + electronD0WRTPV + ") < 0.10))"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string(">= 2 electrons with |d0| < 0.05, 0.10 (EB, EE)"),
)
cutElectronPairDZ2017 = cms.PSet (
    inputCollection = cms.vstring("electrons", "eventvariables"),
    cutString = cms.string("((fabs (electron.superCluster.eta) <= 1.479) && (fabs (" + electronDZWRTPV + ") < 0.10)) \
                         || ((fabs (electron.superCluster.eta) >  1.479) && (fabs (" + electronDZWRTPV + ") < 0.20))"),
    numberRequired = cms.string(">= 2"),
    alias = cms.string(">= 2 electrons with |dz| < 0.10, 0.20 (EB, EE)"),
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
cutTauTightMVAIso = cms.PSet (
    inputCollection = cms.vstring("taus"),
    cutString = cms.string("passesTightMVAIsolation"),
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

############################################################################
## Cuts used in the trigger efficiency measurement
## Produced only with variableProducers.append('EventTriggerVarProducer')
############################################################################

firesTrigger = {}
for trig in triggerFiltersMet:
    firesTrigger[trig] = cms.PSet(
        inputCollection = cms.vstring("eventvariables"),
        cutString = cms.string("fires_" + trig + " > 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string(trig),
    )

firesFilter = {}
for trig in triggerFiltersMet:
    for filt in triggerFiltersMet[trig]:
        if not filt in firesFilter:
            firesFilter[filt] = cms.PSet(
                inputCollection = cms.vstring("eventvariables"),
                cutString = cms.string("fires_" + filt + " > 0"),
                numberRequired = cms.string(">= 1"),
                alias = cms.string(filt),
            )

cutHltMet105 = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("hltMet > 105"),
    numberRequired = cms.string(">= 1"),
)

firesGrandOrTrigger = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("passesGrandOrTrigger > 0"),
    numberRequired = cms.string(">= 1"),
    # Apparently if you alias a cut to end in trigger (contain it?) it prints out the "triggers = " string again?
    #alias = cms.string("passes OR of all signal triggers"),
)

firesGrandOrTriggerWithoutIsoTrk = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("passesGrandOrTriggerWithoutIsoTrk > 0"),
    numberRequired = cms.string(">= 1"),
)

cutLeadJetCentral = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    # -999 means there are no jets, and for trigger efficiencies we want to allow the case where there are zero jets
    cutString = cms.string("fabs(etaJetLeading) <= 2.4 || etaJetLeading < -998.9"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Require leading jet to be central (if any jets)")
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
    cutString = cms.string("missingInnerHitsFromTrackerLayersWithoutMeasurements == 0"),
    numberRequired = cms.string(">= 1"),
)
cutMuonNMissMid = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("missingMiddleHitsFromTrackerLayersWithoutMeasurements == 0"),
    numberRequired = cms.string(">= 1"),
)
cutElectronNMissIn = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("missingInnerHitsFromTrackerLayersWithoutMeasurements == 0"),
    numberRequired = cms.string(">= 1"),
)
cutElectronNMissMid = cms.PSet (
    inputCollection = cms.vstring("electrons"),
    cutString = cms.string("missingMiddleHitsFromTrackerLayersWithoutMeasurements == 0"),
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

#######################################################
## testing CandidateTrack versus pat::IsolatedTrack
#######################################################

# fabs because if there is no matched candidate track, this will be INVALID_VALUE
cutTrkMatchedCandidateTrack = cms.PSet(
    inputCollection = cms.vstring("tracks"),
        cutString = cms.string("fabs(dRToMatchedCandidateTrack) < 0.15"),
        numberRequired = cms.string(">= 1"),
)

###########################################################
###   Cuts for FakeDecay selection
###########################################################

cutTrkDZLoose = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackDZWRTPV + " ) < 5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |dz| < 10"),
)

cutTrkD0Loose = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackD0WRTPV + " ) < 2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |d0| < 2"),
)

#cutDecayIn

cutGenTrkPt45to55 = cms.PSet(
    inputCollection = cms.vstring("genParticlePlusGeant"),
    cutString = cms.string("pt > 45 && pt < 55"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with 45 GeV < p_{T} < 55 GeV"),
)
