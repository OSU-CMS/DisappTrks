# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --filein file:AMSB_chargino700GeV_ctau100cm_step2.root --fileout file:AMSB_chargino700GeV_ctau100cm_step3.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 112X_mcRun3_2021_realistic_v16 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 4 --era Run3 --python_filename step3/AMSB_chargino_step3_Run3Trigger_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('RECO',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('file:AMSB_chargino700GeV_ctau100cm_step2.root'),
    fileNames = cms.untracked.vstring(
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_1.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_10.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_100.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_101.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_102.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_103.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_104.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_105.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_106.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_107.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_108.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_109.root',
    '/store/group/lpclonglived/DisappTrks/AMSB_chargino_M-700GeV_CTau-1cm_TuneCP5_PSweights_14TeV_pythia8/Run3Winter21DRMiniAOD-FlatPU20to70_112X_mcRun3_2021_realistic_v16/210526_150654/0000/AMSB_chargino700GeV_ctau100cm_step2_110.root',
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
#process.AODSIMEventContent.outputCommands = cms.untracked.vstring("keep *")
process.AODSIMEventContent.outputCommands.extend(["keep FEDRawDataCollection_*_*_*"])
process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    fileName = cms.untracked.string('file:AMSB_chargino700GeV_ctau100cm_step3.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '112X_mcRun3_2021_realistic_v16', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.recosim_step = cms.Path(process.recosim)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.recosim_step,process.eventinterpretaion_step,process.endjob_step,process.AODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
