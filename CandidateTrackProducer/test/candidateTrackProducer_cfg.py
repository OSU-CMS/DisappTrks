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
#      "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User.root"
        "file:/home/wulsin/disappTrksRun2/signalDigiReco/CMSSW_7_4_5_ROOT5/src/DisappTrks/SignalMC/test/AMSB_chargino_step4.root"
    )
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
process.MINIAODSIMoutput.outputCommands.append ("keep *_candidateDisappearingTracks_*_*")

process.myEndPath = cms.EndPath (process.MINIAODSIMoutput)






