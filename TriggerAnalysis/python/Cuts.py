import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.invMass import *
from OSUT3Analysis.Configuration.cutUtilities import *

##############################
##### List of triggers   #####
##############################

triggersSingleMu = cms.vstring( # recommended here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Trigger
    "HLT_IsoMu20_v",    # yes available in bkgd MC
    "HLT_IsoTkMu20_v",  # yes available in bkgd MC
)

triggersSingleMu2016 = cms.vstring( # recommended here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Trigger
    "HLT_IsoMu22_v",    # yes available in bkgd MC
    "HLT_IsoTkMu22_v",  # yes available in bkgd MC
)

passesMainTrigger = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("passesMainTrigger > 0"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("HLT_MET75_IsoTrk50_v")
)

##############################################################################
## Require leading jet to be central
##############################################################################

cutLeadJetCentral = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("fabs(etaJetLeading) <= 2.4"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Require leading jet to be central")
)

##############################################################################
## Good track
##############################################################################

cutTrkEta = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("fabs(eta) < 2.5"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNormalizedChi2 = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("normalizedChi2 < 10.0"),
    numberRequired = cms.string(">= 1"),
)
cutTrkD0 = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackD0WRTPV + " ) < 0.2"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |d0| < 0.2 cm"),
)
cutTrkDZ = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    cutString = cms.string("fabs ( " + trackDZWRTPV + " ) < 0.5"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 tracks with |dz| < 0.5"),
)
cutTrkNValidPixelHits = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitPattern_.numberOfValidPixelHits >= 1"),
    numberRequired = cms.string(">= 1"),
)
cutTrkNLayersWMeasurement = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    cutString = cms.string("hitPattern_.trackerLayersWithMeasurement >= 6"),
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
    cutString = cms.string(" ( trackIsoNoPUDRp3 / pt ) < 0.01"),
    numberRequired = cms.string(">= 1"),
)
cutTrkMatchHLTTrack = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("trackMatchToHLTTrack > 0"),
    numberRequired = cms.string(">= 1"),
)
#durp -- deltaR match to charginos

##############################################################################
## Good muon
##############################################################################

cutMuonEta21 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
)
cutMuonPt25 = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("pt > 25"),
    numberRequired = cms.string(">= 1"),
)
cutMuonTightID = cms.PSet (  # Recommended by https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Tight_Muon
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("isTightMuonWRTVtx > 0"),
    numberRequired = cms.string(">= 1"),
)
cutMuonNMissIn = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("innerTrack.missingInnerHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutMuonNMissMid = cms.PSet (
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("innerTrack.missingMiddleHits == 0"),
    numberRequired = cms.string(">= 1"),
)
cutMuonTightPFIso = cms.PSet (  # Recommended by https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Isolation
    inputCollection = cms.vstring("muons"),
    cutString = cms.string("(pfIsolationR04_.sumChargedHadronPt + max (0.0, pfIsolationR04_.sumNeutralHadronEt + pfIsolationR04_.sumPhotonEt - 0.5 * pfIsolationR04_.sumPUPt)) / pt < 0.15"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string(">= 1 muons with #Delta#beta-corrected rel. iso. < 0.15"),
)
cutMuonMatchHLTTrack = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    cutString = cms.string("muonMatchToHLTTrack > 0"),
    numberRequired = cms.string(">= 1"),
)
