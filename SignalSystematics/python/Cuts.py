import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.invMass import *
from OSUT3Analysis.Configuration.cutUtilities import *

from DisappTrks.StandardAnalysis.Cuts import *

##############################
##### List of triggers   #####
##############################

triggersDoubleMu = cms.vstring( # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2#2015_Data_and_MC
    "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v",
    "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v",
)

triggersDoubleMu2016 = cms.vstring( # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideMuonIdRun2#2016_Data
    "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v",
    "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v",
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
## jets
##################################################
cutJetPt30 = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pt > 30"),
    numberRequired = cms.string(">= 1"),
)
cutJetEta25 = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("fabs ( eta ) < 2.5"),
    numberRequired = cms.string(">= 1"),
)
cutJetLooseID = cms.PSet(
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("\
    (abs(eta) > 3.0 && neutralEmEnergyFraction<0.90 && neutralMultiplicity>10) || \
    (abs(eta) > 2.7 && abs(eta) <= 3.0 && neutralEmEnergyFraction<0.90 && neutralMultiplicity>2) || \
    (abs(eta) > 2.4 && abs(eta) <= 2.7 && neutralHadronEnergyFraction<0.99 && neutralEmEnergyFraction<0.99 && (chargedMultiplicity + neutralMultiplicity)>1) || \
    (abs(eta) <= 2.4 && neutralHadronEnergyFraction<0.99 && neutralEmEnergyFraction<0.99 && (chargedMultiplicity + neutralMultiplicity)>1 && chargedHadronEnergyFraction>0 && chargedMultiplicity>0 && chargedEmEnergyFraction<0.99)"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 jet passing Loose ID"),
)
cutJetVetoCSVv2M = cms.PSet( # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation76X
    inputCollection = cms.vstring("jets"),
    cutString = cms.string("pfCombinedInclusiveSecondaryVertexV2BJetTags > 0.800"),
    numberRequired = cms.string("== 0"),
    alias = cms.string("reject events with a CSVv2M tagged jet"),
)

##################################################
## muons
##################################################
cutMuonPairEta24 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("fabs(eta) < 2.4"),
    numberRequired = cms.string("== 2"),
)
cutMuonPairLoosePFIso = cms.PSet (  # Recommended by https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
    inputCollection = cms.vstring("muons"),
    cutString = cutMuonLoosePFIso.cutString,
    numberRequired = cms.string("== 2"),
    alias = cms.string("== 2 muons with #Delta#beta-corrected rel. iso. < 0.25"),
)
cutMuonPairVetoThirdMuon = cms.PSet(
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 10"),
    numberRequired = cms.string("< 3"),
    alias = cms.string("reject events with third muon with p_{T} > 10 GeV"),
)
