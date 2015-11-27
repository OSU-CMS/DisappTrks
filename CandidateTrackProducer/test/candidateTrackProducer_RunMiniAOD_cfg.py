# Config file to produce the candidate track collection.
# Similar to candidateTrackProducer_cfg.py but uses 
# AOD files as input and runs the MINIAOD steps.  
# 
# Usage:
# To run over data:
# > cmsRun candidateTrackProducer_RunMiniAOD_cfg.py print runOnMC=0
#
#
#
# Get config from DAS:  config dataset=/MET/Run2015D-05Oct2015-v1/MINIAOD
# Make some modifications to avoid conflicts  
###############################################################################
# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: REMINIAOD --conditions 74X_dataRun2_reMiniAOD_v0,frontier://FrontierArc/CMS_CONDITIONS_EJ06 -s PAT --runUnscheduled --data --eventcontent MINIAOD --scenario pp --datatier MINIAOD --customise Configuration/DataProcessing/RecoTLR.customiseDataRun2Common_25ns --filein bla.AOD -n 100 --no_exec --python_filename=MINIAOD_Run2015D_05Oct2015.py

import FWCore.ParameterSet.Config as cms

process = cms.Process('PAT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)


import FWCore.ParameterSet.VarParsing as VarParsing 
options = VarParsing.VarParsing ('analysis')
options.register ('runOnMC',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Whether jobs will run over MC (1) or data (0)"
              )
options.parseArguments()


# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/1A77484B-DB68-E511-AEF6-02163E012456.root",
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/564310C7-F868-E511-BD21-02163E014227.root",
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/F0519CD5-D868-E511-B0BE-02163E014208.root",
    ), 
#    secondaryFileNames = cms.untracked.vstring()
)

if options.runOnMC:
    process.source.fileNames = cms.untracked.vstring (
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
    )

import FWCore.ParameterSet.VarParsing as VarParsing 
options = VarParsing.VarParsing ('analysis')
options.register ('runOnMC',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Whether jobs will run over MC (1) or data (0)"
              )
options.parseArguments()


process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('REMINIAOD nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAOD'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('miniAODWithCandidateTracks.root'),  
    outputCommands = process.MINIAODSIMEventContent.outputCommands,  # Include SIM content to allow running over MC.  
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if options.runOnMC:
    process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')
else:
    process.GlobalTag = GlobalTag(process.GlobalTag, '74X_dataRun2_reMiniAOD_v0,frontier://FrontierArc/CMS_CONDITIONS_EJ06', '')

# Customize for disappearing tracks:
process.load('DisappTrks.CandidateTrackProducer.CandidateTrackProducer_cfi')
process.candidateTracks = cms.Path (process.candidateTrackProducer)  
from DisappTrks.CandidateTrackProducer.customize import disappTrksOutputCommands 
process.MINIAODoutput.outputCommands.extend (disappTrksOutputCommands)

# Path and EndPath definitions
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_METFilters = cms.Path(process.metFilters*process.candidateTrackProducer) 
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODoutput_step = cms.EndPath(process.MINIAODoutput)


# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.candidateTracks,process.endjob_step,process.MINIAODoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.RecoTLR
from Configuration.DataProcessing.RecoTLR import customiseDataRun2Common_25ns 

#call to customisation function customiseDataRun2Common_25ns imported from Configuration.DataProcessing.RecoTLR
process = customiseDataRun2Common_25ns(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
# from FWCore.ParameterSet.Utilities import convertToUnscheduled
# process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PAT_cff')
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)



# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllData 

#call to customisation function miniAOD_customizeAllData imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllData(process)

# End of customisation functions

