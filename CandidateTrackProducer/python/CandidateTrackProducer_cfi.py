import FWCore.ParameterSet.Config as cms
import os
import copy

# The following are needed for the calculation of associated calorimeter energy
from Configuration.StandardSequences.GeometryRecoDB_cff import *
from Configuration.StandardSequences.MagneticField_38T_cff import *

candidateTrackProducer = cms.EDFilter ("CandidateTrackProducer",
  tracks             =  cms.InputTag  ("generalTracks",                  ""),
  rhoTag             =  cms.InputTag  ("fixedGridRhoFastjetAll"),
  rhoCaloTag         =  cms.InputTag  ("fixedGridRhoFastjetAllCalo"),
  rhoCentralCaloTag  =  cms.InputTag  ("fixedGridRhoFastjetCentralCalo"),
  EBRecHits          =  cms.InputTag  ("reducedEcalRecHitsEB"),
  EERecHits          =  cms.InputTag  ("reducedEcalRecHitsEE"),
  HBHERecHits        =  cms.InputTag  ("reducedHcalRecHits", "hbhereco"),
  dEdxDataPixel      =  cms.InputTag  ("dedxPixelHarmonic2"),
  dEdxDataStrip      =  cms.InputTag  ("dedxHarmonic2"),
  candMinPt          =  cms.double(10),
  usedEdx            =  cms.bool(True), # turn off for FastSim
)

class Collections:
  pass

collections = Collections ()

collections.MiniAOD = cms.PSet (
  beamspots        = cms.InputTag ("offlineBeamSpot",                ""),
  conversions      = cms.InputTag ("reducedEgamma",                  "reducedConversions",  ""),
  electrons        = cms.InputTag ("slimmedElectrons",               ""),
  mets             = cms.InputTag ("slimmedMETs",                    ""),
  pfCandidates     = cms.InputTag ("packedPFCandidates",             ""),
  muons            = cms.InputTag ("slimmedMuons",                   ""),
  rho              = cms.InputTag ("fixedGridRhoFastjetAll",         "",                    ""),
  taus             = cms.InputTag ("slimmedTaus",                    ""),
  triggers         = cms.InputTag ("TriggerResults",                 "",                    "HLT"),
  vertices         = cms.InputTag ("offlineSlimmedPrimaryVertices",  ""),
  trigobjs         = cms.InputTag ('slimmedPatTrigger'),
)

electronIdName = "cutBasedElectronID-Spring15-25ns-V1-standalone-tight"
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0"):
  electronIdName = "cutBasedElectronID-Summer16-80X-V1-tight"
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4"):
  electronIdName = "cutBasedElectronID-Fall17-94X-V1-tight"
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2"):
  electronIdName = "cutBasedElectronID-Fall17-94X-V2-tight"

metSkimFilter = cms.EDFilter ("METSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  pfCandidates =  collections.MiniAOD.pfCandidates,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  ptCut        =  cms.double (100),
  etaCut       =  cms.double (-1),
  eleVIDid     =  cms.string (electronIdName),
  d0Cuts       = cms.vdouble (-1, -1),
  dZCuts       = cms.vdouble (-1, -1),
  triggerNames =  cms.vstring (
    # trigger developed for disappearing tracks
    "HLT_MET75_IsoTrk50_v",
    "HLT_MET90_IsoTrk50_v",

    # all other MET triggers that remained unprescaled for 2015
    "HLT_MET250_v",
    "HLT_PFMET120_PFMHT120_IDTight_v",
    "HLT_PFMET170_HBHECleaned_v",
    "HLT_PFMET170_JetIdCleaned_v",
    "HLT_PFMET170_NoiseCleaned_v",
    "HLT_PFMET170_v",
    "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v",

    # these two are missing ~10/pb in 2015, but they're close enough
    "HLT_PFMET90_PFMHT90_IDTight_v",
    "HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v",

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
  pfCandidates =  collections.MiniAOD.pfCandidates,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  etaCut       =  cms.double(2.1),
  ptCut        =  cms.double (25),
  eleVIDid     =  cms.string (electronIdName),
  d0Cuts       = cms.vdouble (0.0111, 0.0351),
  dZCuts       = cms.vdouble (0.0466, 0.417),
  triggerNames =  cms.vstring (
    # all single electron triggers that remained unprescaled for 2015
    "HLT_Ele32_eta2p1_WPTight_Gsf_v",

    # these two are missing ~10/pb in 2015, but they're close enough
    "HLT_Ele22_eta2p1_WPLoose_Gsf_v",
    "HLT_Ele22_eta2p1_WPTight_Gsf_v",
    "HLT_Ele23_WPLoose_Gsf_v",

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
  pfCandidates =  collections.MiniAOD.pfCandidates,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  etaCut       =  cms.double(2.1),
  ptCut        =  cms.double (22),
  eleVIDid     =  cms.string (electronIdName),
  d0Cuts       = cms.vdouble (-1, -1),
  dZCuts       = cms.vdouble (-1, -1),
  triggerNames =  cms.vstring ("HLT_IsoMu20_v", "HLT_IsoTkMu20_v"),
)

tauSkimFilter = cms.EDFilter ("TauSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  pfCandidates =  collections.MiniAOD.pfCandidates,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  etaCut       =  cms.double(2.1),
  ptCut        =  cms.double (50),
  eleVIDid     =  cms.string (electronIdName),
  d0Cuts       = cms.vdouble (-1, -1),
  dZCuts       = cms.vdouble (-1, -1),
  triggerNames =  cms.vstring ("HLT_LooseIsoPFTau50_Trk30_eta2p1_v"),
)

electronTagProbeFilter = cms.EDFilter ("ElectronTagProbeFilter",
  triggers         = collections.MiniAOD.triggers,
  triggerObjects   = collections.MiniAOD.trigobjs,
  vertices         = collections.MiniAOD.vertices,
  met              = collections.MiniAOD.mets,
  electrons        = collections.MiniAOD.electrons,
  muons            = collections.MiniAOD.muons,
  tracks           = cms.InputTag ("generalTracks"),
  triggerNames     = cms.vstring (),
  dataTakingPeriod = cms.string(""),
)

muonTagProbeFilter = copy.deepcopy(electronTagProbeFilter)
tauToElectronTagProbeFilter = copy.deepcopy(electronTagProbeFilter)
tauToMuonTagProbeFilter = copy.deepcopy(electronTagProbeFilter)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0"):
  muonSkimFilter.ptCut = cms.double(26)
  muonSkimFilter.triggerNames =  cms.vstring ("HLT_IsoMu24_v", "HLT_IsoTkMu24_v")
  electronSkimFilter.d0Cuts = cms.vdouble(0.05, 0.10)
  electronSkimFilter.dZCuts = cms.vdouble(0.10, 0.20)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4"):
  metSkimFilter.ptCut = cms.double(120)
  electronSkimFilter.ptCut = cms.double(35)
  muonSkimFilter.ptCut = cms.double(29)

  electronSkimFilter.d0Cuts = cms.vdouble(0.05, 0.10)
  electronSkimFilter.dZCuts = cms.vdouble(0.10, 0.20)

  metSkimFilter.triggerNames = cms.vstring (
    "HLT_MET105_IsoTrk50_v",
    "HLT_MET120_IsoTrk50_v",

    # all other MET triggers that remained unprescaled for 2017
    'HLT_PFMET120_PFMHT120_IDTight_v',
    'HLT_PFMET130_PFMHT130_IDTight_v',
    'HLT_PFMET140_PFMHT140_IDTight_v',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
    
    # available starting 2017C
    'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
    'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
    'HLT_PFMET120_PFMHT120_IDTight_HFCleaned_v', # not available in MC
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_HFCleaned_v', # not available in MC
    'HLT_PFMET250_HBHECleaned_v',
    'HLT_PFMET300_HBHECleaned_v',
  )
  electronSkimFilter.triggerNames = cms.vstring ("HLT_Ele35_WPTight_Gsf_v")
  muonSkimFilter.triggerNames = cms.vstring ("HLT_IsoMu27_v")
  tauSkimFilter.triggerNames = cms.vstring ("HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v")

  electronTagProbeFilter.triggerNames = cms.vstring ("HLT_Ele35_WPTight_Gsf_v")
  tauToElectronTagProbeFilter.triggerNames = cms.vstring ("HLT_Ele35_WPTight_Gsf_v")
  muonTagProbeFilter.triggerNames = cms.vstring ("HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v")
  tauToMuonTagProbeFilter.triggerNames = cms.vstring ("HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v")

  electronTagProbeFilter.dataTakingPeriod = cms.string ("2017")
  tauToElectronTagProbeFilter.dataTakingPeriod = cms.string ("2017")
  muonTagProbeFilter.dataTakingPeriod = cms.string ("2017")
  tauToMuonTagProbeFilter.dataTakingPeriod = cms.string ("2017")

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2"):
  metSkimFilter.ptCut = cms.double(120)
  electronSkimFilter.ptCut = cms.double(32)
  muonSkimFilter.ptCut = cms.double(26)

  electronSkimFilter.d0Cuts = cms.vdouble(0.05, 0.10)
  electronSkimFilter.dZCuts = cms.vdouble(0.10, 0.20)

  metSkimFilter.triggerNames = cms.vstring (
    "HLT_MET105_IsoTrk50_v",
    "HLT_MET120_IsoTrk50_v",

    "HLT_PFMET120_PFMHT120_IDTight_v",
    "HLT_PFMET130_PFMHT130_IDTight_v",
    "HLT_PFMET140_PFMHT140_IDTight_v",
    "HLT_PFMETTypeOne140_PFMHT140_IDTight_v",
    "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v",
    "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v",
    "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v",
    "HLT_PFMET250_HBHECleaned_v",
    "HLT_PFMET300_HBHECleaned_v",
    "HLT_PFMET200_HBHE_BeamHaloCleaned_v",
    "HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v",
  )
  electronSkimFilter.triggerNames = cms.vstring ("HLT_Ele32_WPTight_Gsf_v")
  muonSkimFilter.triggerNames = cms.vstring ("HLT_IsoMu24_v")
  tauSkimFilter.triggerNames = cms.vstring ("HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v")

  electronTagProbeFilter.triggerNames = cms.vstring ("HLT_Ele32_WPTight_Gsf_v")
  tauToElectronTagProbeFilter.triggerNames = cms.vstring ("HLT_Ele32_WPTight_Gsf_v")
  muonTagProbeFilter.triggerNames = cms.vstring ("HLT_IsoMu24_v"),
  tauToMuonTagProbeFilter.triggerNames = cms.vstring ("HLT_IsoMu24_v")

  electronTagProbeFilter.dataTakingPeriod = cms.string ("2018")
  tauToElectronTagProbeFilter.dataTakingPeriod = cms.string ("2018")
  muonTagProbeFilter.dataTakingPeriod = cms.string ("2018")
  tauToMuonTagProbeFilter.dataTakingPeriod = cms.string ("2018")
