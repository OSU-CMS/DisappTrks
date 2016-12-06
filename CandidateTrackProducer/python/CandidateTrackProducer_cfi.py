import FWCore.ParameterSet.Config as cms

# The following are needed for the calculation of associated calorimeter energy
from Configuration.StandardSequences.GeometryRecoDB_cff import *
from Configuration.StandardSequences.MagneticField_38T_cff import *

candidateTrackProducer = cms.EDFilter ("CandidateTrackProducer",
  tracks             =  cms.InputTag  ("generalTracks",                  ""),
  electrons          =  cms.InputTag  ("slimmedElectrons",               ""),
  muons              =  cms.InputTag  ("slimmedMuons",                   ""),
  taus               =  cms.InputTag  ("slimmedTaus",                    ""),
  beamspot           =  cms.InputTag  ("offlineBeamSpot",                ""),
  vertices           =  cms.InputTag  ("offlineSlimmedPrimaryVertices",  ""),
  conversions        =  cms.InputTag  ("reducedEgamma",                  "reducedConversions"),
  rhoTag             =  cms.InputTag  ("fixedGridRhoFastjetAll"),
  rhoCaloTag         =  cms.InputTag  ("fixedGridRhoFastjetAllCalo"),
  rhoCentralCaloTag  =  cms.InputTag  ("fixedGridRhoFastjetCentralCalo"),
  EBRecHits          =  cms.InputTag  ("reducedEcalRecHitsEB"),
  EERecHits          =  cms.InputTag  ("reducedEcalRecHitsEE"),
  HBHERecHits        =  cms.InputTag  ("reducedHcalRecHits", "hbhereco"),
  candMinPt          =  cms.double(10),
)

class Collections:
  pass

collections = Collections ()

collections.MiniAOD = cms.PSet (
  beamspots    =  cms.InputTag  ("offlineBeamSpot",                ""),
  conversions  =  cms.InputTag  ("reducedEgamma",                  "reducedConversions",  ""),
  electrons    =  cms.InputTag  ("slimmedElectrons",               ""),
  mets         =  cms.InputTag  ("slimmedMETs",                    ""),
  muons        =  cms.InputTag  ("slimmedMuons",                   ""),
  rho          =  cms.InputTag  ("fixedGridRhoFastjetAll",         "",                    ""),
  taus         =  cms.InputTag  ("slimmedTaus",                    ""),
  triggers     =  cms.InputTag  ("TriggerResults",                 "",                    "HLT"),
  vertices     =  cms.InputTag  ("offlineSlimmedPrimaryVertices",  ""),
)

metSkimFilter = cms.EDFilter ("METSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  triggerNames =  cms.vstring (
    # trigger developed for disappearing tracks
    "HLT_MET75_IsoTrk50_v",

    # all other MET triggers that remained unprescaled for 2016
    "HLT_MET200_v",
    "HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned_v",
    "HLT_PFMET120_PFMHT120_IDTight_v",
    "HLT_PFMET170_HBHECleaned_v",
    "HLT_PFMET300_v",
    "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v",
  ),
)

electronSkimFilter = cms.EDFilter ("ElectronSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  triggerNames =  cms.vstring (
    # all single electron triggers that remained unprescaled for 2016
    "HLT_Ele25_eta2p1_WPTight_Gsf_v",
    "HLT_Ele27_WPTight_Gsf_v",
  ),
)

muonSkimFilter = cms.EDFilter ("MuonSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  triggerNames =  cms.vstring (
    "HLT_IsoMu20_v",
    "HLT_IsoMu22_v",
    "HLT_IsoTkMu20_v",
    "HLT_IsoTkMu22_v",
  ),
)

tauSkimFilter = cms.EDFilter ("TauSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  triggerNames =  cms.vstring (
    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v",
  ),
)
