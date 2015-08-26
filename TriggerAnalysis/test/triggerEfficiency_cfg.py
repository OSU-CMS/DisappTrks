import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import OSUT3Analysis.AnaTools.MuonIDSelections as muonID
import math
import os
import numpy

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('OSUAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)
process.source = cms.Source ("PoolSource",
    #fileNames = cms.untracked.vstring ('root://cmsxrootd.fnal.gov///store/mc/RunIISpring15DR74/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/50000/689003ED-18FE-E411-9EE9-F04DA23BBCCA.root')
    fileNames = cms.untracked.vstring ('root://cmsxrootd.fnal.gov///store/mc/RunIISpring15DR74/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/80000/FC8BEFF2-DFFB-E411-9369-002590D0AFC4.root')
)

###########################################################
##### Set up the analyzer #####
###########################################################

class Collections:
  pass

collections = Collections ()

collections.BEAN = cms.PSet (
  bxlumis         =  cms.InputTag  ('BNproducer',  'BXlumi'),
  electrons       =  cms.InputTag  ('BNproducer',  'selectedPatElectronsLoosePFlow'),
  events          =  cms.InputTag  ('BNproducer',  ''),
  genjets         =  cms.InputTag  ('BNproducer',  'ak5GenJets'),
  jets            =  cms.InputTag  ('BNproducer',  'selectedPatJetsPFlow'),
  mcparticles     =  cms.InputTag  ('BNproducer',  'MCstatus3'),
  mets            =  cms.InputTag  ('BNproducer',  'patMETsPFlow'),
  muons           =  cms.InputTag  ('BNproducer',  'selectedPatMuonsLoosePFlow'),
  photons         =  cms.InputTag  ('BNproducer',  'none'),
  primaryvertexs  =  cms.InputTag  ('BNproducer',  'offlinePrimaryVertices'),
  secMuons        =  cms.InputTag  ('BNproducer',  'selectedPatMuonsLoosePFlow'),
  stops           =  cms.InputTag  ('BNproducer',  'MCstop'),
  superclusters   =  cms.InputTag  ('BNproducer',  'corHybridSCandMulti5x5WithPreshower'),
  taus            =  cms.InputTag  ('BNproducer',  'selectedPatTaus'),
  tracks          =  cms.InputTag  ('BNproducer',  'generalTracks'),
  triggers        =  cms.InputTag  ('BNproducer',  'HLT'),
  trigobjs        =  cms.InputTag  ('BNproducer',  'HLT'),
)

collections.MiniAOD = cms.PSet (
  beamspots       =  cms.InputTag  ("offlineBeamSpot",                ""),
  electrons       =  cms.InputTag  ("slimmedElectrons",               ""),
  genjets         =  cms.InputTag  ("slimmedGenJets",                 ""),
  jets            =  cms.InputTag  ("slimmedJets",                    ""),
  mcparticles     =  cms.InputTag  ("packedGenParticles",             ""),
  mets            =  cms.InputTag  ("slimmedMETs",                    ""),
  muons           =  cms.InputTag  ("slimmedMuons",                   ""),
  photons         =  cms.InputTag  ("slimmedPhotons",                 ""),
  primaryvertexs  =  cms.InputTag  ("offlineSlimmedPrimaryVertices",  ""),
  superclusters   =  cms.InputTag  ("reducedEgamma",                  "reducedSuperClusters"),
  taus            =  cms.InputTag  ("slimmedTaus",                    ""),
  triggers        =  cms.InputTag  ("TriggerResults",                 "",                       "HLT"),
  trigobjs        =  cms.InputTag  ("selectedPatTrigger",             ""),
)

class Cuts:
  pass

cuts = Cuts ()

cuts.MuMETNoMET = cms.PSet (
  name = cms.string ('MuMETNoMET'),
  triggerFilters = cms.vstring ('hltMETClean75'),
  cuts = cms.VPSet (
      cms.PSet (
          inputCollection = cms.vstring ('mets'),
          cutString = cms.string ('pt > -1.0'),
          numberRequired = cms.string ('== 1'),
      ),
  ),
)

cuts.MuMETNoMETNoTrigger = cms.PSet (
  name = cms.string ('MuMETNoMETNoTrigger'),
#  triggerFilters = cms.vstring ('hltMETClean75'),
  cuts = cms.VPSet (
      cms.PSet (
          inputCollection = cms.vstring ('mets'),
          cutString = cms.string ('pt > -1.0'),
          numberRequired = cms.string ('== 1'),
      ),
  ),
)

cuts.MuMETNoMuonPt = cms.PSet (
  name = cms.string ('MuMETNoMuonPt'),
  triggers = cms.vstring ('HLT_MET75_IsoTrk50_v'),
  triggerFilters = cms.vstring ('hltMETClean75'),
  cuts = cms.VPSet (
      cms.PSet (
          inputCollection = cms.vstring ('muons'),
          cutString = cms.string ('abs (eta) < 2.1'),
          numberRequired = cms.string ('== 1'),
      ),
      cms.PSet (
          inputCollection = cms.vstring ('muons'),
          cutString = cms.string (muonID.run2.tightID_displaced),
          numberRequired = cms.string ('== 1'),
          alias = cms.string ('displaced tight muon ID'),
      ),
      cms.PSet (
          inputCollection = cms.vstring ('muons'),
          cutString = cms.string ('(isolationR03_.sumPt / pt) < 0.01'),
          numberRequired = cms.string ('== 1'),
          alias = cms.string ('muon isolation'),
      ),
      cms.PSet (
          inputCollection = cms.vstring ('electrons'),
          cutString = cms.string ('pt > 10.0'),
          numberRequired = cms.string ('== 0'),
          alias = cms.string ('electron veto'),
      ),
  ),
)

cuts.MuMETNoMuonPtNoTrigger = cms.PSet (
  name = cms.string ('MuMETNoMuonPtNoTrigger'),
#  triggers = cms.vstring ('HLT_MET75_IsoTrk50_v'),
  triggerFilters = cms.vstring ('hltMETClean75'),
  cuts = cms.VPSet (
      cms.PSet (
          inputCollection = cms.vstring ('muons'),
          cutString = cms.string ('abs (eta) < 2.1'),
          numberRequired = cms.string ('== 1'),
      ),
      cms.PSet (
          inputCollection = cms.vstring ('muons'),
          cutString = cms.string ('pt > 75.0'),
          numberRequired = cms.string ('== 1'),
      ),
      cms.PSet (
          inputCollection = cms.vstring ('muons'),
          cutString = cms.string (muonID.run2.tightID_displaced),
          numberRequired = cms.string ('== 1'),
          alias = cms.string ('displaced tight muon ID'),
      ),
      cms.PSet (
          inputCollection = cms.vstring ('muons'),
          cutString = cms.string ('(isolationR03_.sumPt / pt) < 0.01'),
          numberRequired = cms.string ('== 1'),
          alias = cms.string ('muon isolation'),
      ),
      cms.PSet (
          inputCollection = cms.vstring ('electrons'),
          cutString = cms.string ('pt > 10.0'),
          numberRequired = cms.string ('== 0'),
          alias = cms.string ('electron veto'),
      ),
  ),
)

class Histograms:
  pass

histograms = Histograms ()

histograms.muons = cms.PSet (
  inputCollection = cms.vstring ('muons'),
  histograms = cms.VPSet (
      cms.PSet (
        name = cms.string ('muonPt'),
        title = cms.string ('Muon Transverse Momentum;muon p_{T} [GeV]'),
        binsX = cms.untracked.vdouble (numpy.logspace (0.0, 3.0, 1000)),
        inputVariables = cms.vstring ('pt'),
      ),
      cms.PSet (
        name = cms.string ('muonEta'),
        title = cms.string ('Muon Pseudorapidity;muon #eta'),
        binsX = cms.untracked.vdouble (1000, -5.0, 5.0),
        inputVariables = cms.vstring ('eta'),
      ),
      cms.PSet (
        name = cms.string ('muonPhi'),
        title = cms.string ('Muon Azimuthal Angle;muon #phi'),
        binsX = cms.untracked.vdouble (1000, -3.2, 3.2),
        inputVariables = cms.vstring ('phi'),
      ),
   ),
)

histograms.mets = cms.PSet (
  inputCollection = cms.vstring ('mets'),
  histograms = cms.VPSet (
      cms.PSet (
        name = cms.string ('metPt'),
        title = cms.string ('Missing Transverse Energy;E_{T}^{miss} [GeV]'),
        binsX = cms.untracked.vdouble (numpy.logspace (0.0, 3.0, 1000)),
        inputVariables = cms.vstring ('pt'),
      ),
      cms.PSet (
        name = cms.string ('metPhi'),
        title = cms.string ('MET Azimuthal Angle;#phi'),
        binsX = cms.untracked.vdouble (1000, -3.2, 3.2),
        inputVariables = cms.vstring ('phi'),
      ),
  ),
)

add_channels (
  process,
  [cuts.MuMETNoMET, cuts.MuMETNoMETNoTrigger, cuts.MuMETNoMuonPt, cuts.MuMETNoMuonPtNoTrigger],
  cms.VPSet (histograms.muons, histograms.mets),
  collections.MiniAOD,
  [],
  True,
)
