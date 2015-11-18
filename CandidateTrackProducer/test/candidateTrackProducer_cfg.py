import FWCore.ParameterSet.Config as cms
import os

# Usage:
# To run over data:
# > cmsRun candidateTrackProducer_cfg.py print runOnMC=0


###########################################################
##### Set up process #####
###########################################################

import FWCore.ParameterSet.VarParsing as VarParsing 
options = VarParsing.VarParsing ('analysis')
options.register ('runOnMC',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Whether jobs will run over MC (1) or data (0)"
              )
options.parseArguments()


process = cms.Process ('DISAPPTRKS')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (101)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_0.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_1.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_2.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_3.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_4.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_5.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_6.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_7.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_8.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step4_User/AMSB_chargino_step4_9.root",
    ),
    secondaryFileNames = cms.untracked.vstring (
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_0.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_1.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_2.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_3.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_4.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_5.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_6.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_7.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_8.root",
        "/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3_User/AMSB_chargino_step3_9.root",
    ),
)

if not options.runOnMC:
    process.source.fileNames = cms.untracked.vstring (
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/MINIAOD/05Oct2015-v1/30000/04F50A91-B46F-E511-A2A3-002618943923.root", 
        )
    process.source.secondaryFileNames = cms.untracked.vstring (
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/1A77484B-DB68-E511-AEF6-02163E012456.root",
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/564310C7-F868-E511-BD21-02163E014227.root",
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/F0519CD5-D868-E511-B0BE-02163E014208.root",
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

if options.runOnMC:
    process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')
else:
    process.GlobalTag = GlobalTag(process.GlobalTag, '74X_dataRun2_Prompt_v4', '')

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
  rhoTag     =  cms.InputTag  ("fixedGridRhoFastjetAll"), 
  rhoCaloTag     =  cms.InputTag  ("fixedGridRhoFastjetAllCalo"), 
  rhoCentralCaloTag     =  cms.InputTag  ("fixedGridRhoFastjetCentralCalo"), 
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
