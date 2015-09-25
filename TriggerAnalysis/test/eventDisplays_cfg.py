import FWCore.ParameterSet.Config as cms
import sys

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('DISPLAY')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (2500)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_0.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_1.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_10.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_11.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_12.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_13.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_14.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_15.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_16.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_17.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_18.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_19.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_2.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_20.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_21.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_22.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_23.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_24.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_25.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_26.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_27.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_28.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_29.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_3.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_30.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_31.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_32.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_33.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_34.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_35.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_36.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_37.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_38.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_39.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_4.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_40.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_41.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_42.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_43.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_44.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_45.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_46.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_47.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_48.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_49.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_5.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_6.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_7.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_8.root',
        '/store/user/ahart/AMSB_chargino700GeV_ctau1000cm_step3/AMSB_chargino_step3_9.root',
    ),
)

###########################################################
##### Set up the analyzer #####
###########################################################

process.EventDisplays = cms.EDFilter ("EventDisplays",
  mets          =  cms.InputTag ("pfMet", ""),
  muons         =  cms.InputTag ("muons", ""),
  genParticles  =  cms.InputTag ("genParticlePlusGeant", ""),
  jets          =  cms.InputTag ("ak4PFJetsCHS", ""),
)

process.myPath = cms.Path (process.EventDisplays)

process.load('Configuration.EventContent.EventContent_cff')
process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECOSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('eventDisplays.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    SelectEvents = cms.untracked.PSet (
      SelectEvents = cms.vstring ("myPath")
    )
)
process.RECOSIMoutput.outputCommands.append ("keep *_genParticlePlusGeant_*_*")
process.myEndPath = cms.EndPath (process.RECOSIMoutput)
