import FWCore.ParameterSet.Config as cms
import os

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('DISAPPTRKS')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_0.root"
    ),
    secondaryFileNames = cms.untracked.vstring (
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_0.root"
    ),
)

###########################################################
##### Set up the analyzer #####
###########################################################

# The following are needed for the calculation of associated calorimeter energy
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')
from TrackingTools.TrackAssociator.default_cfi import *
CandTrackAssociatorParameters = TrackAssociatorParameterBlock.TrackAssociatorParameters.clone()
CandTrackAssociatorParameters.useHO = cms.bool(False)
CandTrackAssociatorParameters.CSCSegmentCollectionLabel     = cms.InputTag("cscSegments")
CandTrackAssociatorParameters.DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments")
CandTrackAssociatorParameters.EERecHitCollectionLabel       = cms.InputTag("reducedEcalRecHitsEE")
CandTrackAssociatorParameters.EBRecHitCollectionLabel       = cms.InputTag("reducedEcalRecHitsEB")
CandTrackAssociatorParameters.HBHERecHitCollectionLabel     = cms.InputTag("reducedHcalRecHits", "hbhereco")
CandTrackAssociatorParameters.HORecHitCollectionLabel       = cms.InputTag("reducedHcalRecHits", "horeco")

process.candidateDisappearingTracks = cms.EDProducer ("CandidateTrackProducer",
  tracks     =  cms.InputTag  ("generalTracks",     ""),
  electrons  =  cms.InputTag  ("slimmedElectrons",  ""),
  muons      =  cms.InputTag  ("slimmedMuons",      ""),
  taus       =  cms.InputTag  ("slimmedTaus",       ""),
  rhoTag     =  cms.InputTag  ("ak4CaloJets",    "rho"),
  candMinPt = cms.double(10),
  TrackAssociatorParameters = CandTrackAssociatorParameters,
)

process.myPath = cms.Path (process.candidateDisappearingTracks)

process.load('Configuration.EventContent.EventContent_cff')
process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string("miniAODWithCandidateTracks.root"),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
)
process.MINIAODSIMoutput.outputCommands.append ("keep recoCaloMETs_*_*_*")
process.MINIAODSIMoutput.outputCommands.append ("keep recoMETs_*_*_*")
process.MINIAODSIMoutput.outputCommands.append ("keep recoPFMETs_*_*_*")
process.MINIAODSIMoutput.outputCommands.append ("keep *_generalTracks_*_*")
process.MINIAODSIMoutput.outputCommands.append ("keep *_candidateDisappearingTracks_*_*")
process.MINIAODSIMoutput.outputCommands.append ("keep *_reducedEcalRecHitsEE_*_*")
process.MINIAODSIMoutput.outputCommands.append ("keep *_reducedEcalRecHitsEB_*_*")
process.MINIAODSIMoutput.outputCommands.append ("keep *_reducedHcalRecHits_*_*")
process.MINIAODSIMoutput.outputCommands.append ("keep *_dt4DSegments_*_*")
process.MINIAODSIMoutput.outputCommands.append ("keep *_cscSegments_*_*")

process.myEndPath = cms.EndPath (process.MINIAODSIMoutput)
