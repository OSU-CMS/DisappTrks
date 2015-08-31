import FWCore.ParameterSet.Config as cms

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('OSUAnalysis')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string (
        "AMSB_chargino500GeV_ctau100cm_step4.root"
        #"AMSB_chargino500GeV_ctau100cm_step4_missHitsIn.root"
        #"AMSB_chargino500GeV_ctau100cm_step4_missHitsMid.root"
        #"AMSB_chargino500GeV_ctau100cm_step4_noTrkIso.root"
        #"AMSB_chargino500GeV_ctau100cm_step4_noTrkIso_missHitsIn_missHitsMid.root"
    )
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "/store/user/ahart/AMSB_chargino500GeV_ctau100cm_step4.root"
        #"/store/user/ahart/AMSB_chargino500GeV_ctau100cm_step4_missHitsIn.root"
        #"/store/user/ahart/AMSB_chargino500GeV_ctau100cm_step4_missHitsMid.root"
        #"/store/user/ahart/AMSB_chargino500GeV_ctau100cm_step4_noTrkIso.root"
        #"/store/user/ahart/AMSB_chargino500GeV_ctau100cm_step4_noTrkIso_missHitsIn_missHitsMid.root"
    )
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
  genparticles    =  cms.InputTag  ("prunedGenParticles",             ""),
  jets            =  cms.InputTag  ("slimmedJets",                    ""),
  mcparticles     =  cms.InputTag  ("packedGenParticles",             ""),
  mets            =  cms.InputTag  ("slimmedMETs",                    ""),
  muons           =  cms.InputTag  ("slimmedMuons",                   ""),
  photons         =  cms.InputTag  ("slimmedPhotons",                 ""),
  primaryvertexs  =  cms.InputTag  ("offlineSlimmedPrimaryVertices",  ""),
  superclusters   =  cms.InputTag  ("reducedEgamma",                  "reducedSuperClusters"),
  taus            =  cms.InputTag  ("slimmedTaus",                    ""),
  tracks          =  cms.InputTag  ("generalTracks",                  ""),
  triggers        =  cms.InputTag  ("TriggerResults",                 "",                       "HLT"),
  trigobjs        =  cms.InputTag  ("selectedPatTrigger",             ""),
)

process.TriggerEfficiency = cms.EDAnalyzer ("TriggerEfficiencyWithTracks",
  mets         =  collections.MiniAOD.mets,
  tracks       =  collections.MiniAOD.tracks,
  triggerBits  =  collections.MiniAOD.triggers,
  triggerObjs  =  collections.MiniAOD.trigobjs,
  vertices     =  collections.MiniAOD.primaryvertexs,
  genParticles =  collections.MiniAOD.genparticles,
)

process.myPath = cms.Path (process.TriggerEfficiency)
