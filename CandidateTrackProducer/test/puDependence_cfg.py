import FWCore.ParameterSet.Config as cms
import sys

prefix = sys.argv[2]

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('TRIGGER')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string (
        prefix + ".root",
    )
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
      'file:miniAODWithCandidateTracks.root', 
        # #"/store/user/ahart/" + prefix + ".root"
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_0.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_1.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_10.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_11.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_12.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_13.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_14.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_15.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_16.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_17.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_18.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_19.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_2.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_20.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_21.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_22.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_23.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_24.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_25.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_26.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_27.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_28.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_29.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_3.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_30.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_31.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_32.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_33.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_34.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_35.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_36.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_37.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_38.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_39.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_4.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_40.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_41.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_42.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_43.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_44.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_45.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_46.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_47.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_48.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_49.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_5.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_6.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_7.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_8.root',
        # 'file:/data/users/hart/condor/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_9.root',

    )
)

###########################################################
##### Set up the analyzer #####
###########################################################

class Collections:
  pass

collections = Collections ()

collections.MiniAOD = cms.PSet (
  beamspots       =  cms.InputTag  ("offlineBeamSpot",                ""),
  caloMets        =  cms.InputTag  ("caloMet",                        ""),
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

process.PUDependence = cms.EDAnalyzer ("PUDependence",
  tracks        =  cms.InputTag ("candidateDisappearingTracks", ""),
  vertices      =  collections.MiniAOD.primaryvertexs,
  genParticles  =  collections.MiniAOD.genparticles,
)

process.myPath = cms.Path (process.PUDependence)
