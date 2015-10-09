# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step3 --filein file:AMSB_chargino_step3.root --fileout file:AMSB_chargino_step4.root --mc --eventcontent MINIAODSIM --runUnscheduled --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring,DisappTrks/SignalMC/genParticlePlusGeant.customizeKeep,DisappTrks/SignalMC/recoCollectionsToKeep.customize --datatier MINIAODSIM --conditions MCRUN2_74_V9 --step PAT --python_filename AMSB_chargino_step4_cfg.py --no_exec -n 82
import FWCore.ParameterSet.Config as cms

process = cms.Process('PAT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(82)
)

# Input source
process.source = cms.Source("PoolSource",
                            #    fileNames = cms.untracked.vstring('file:AMSB_chargino_step3.root'),
#    fileNames = cms.untracked.vstring('file:root://cmsxrootd.fnal.gov///store/mc/RunIISpring15DR74/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/00682F91-475D-E511-8516-000F5327349C.root'),
    fileNames = cms.untracked.vstring('file:root://cmsxrootd.fnal.gov///store/mc/RunIISpring15DR74/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/Asympt25ns_MCRUN2_74_V9-v2/40000/5604BB8E-2C2A-E511-A9A4-A0369F3102B6.root'), 
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:82'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

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
  rhoTag     =  cms.InputTag  ("fixedGridRhoFastjetAll"), 
  rhoCaloTag     =  cms.InputTag  ("fixedGridRhoFastjetAllCalo"), 
  rhoCentralCaloTag     =  cms.InputTag  ("fixedGridRhoFastjetCentralCalo"), 
  candMinPt = cms.double(10),
  TrackAssociatorParameters = CandTrackAssociatorParameters,
)

process.myPath = cms.Path (process.candidateDisappearingTracks)

# Output definition

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
    fileName = cms.untracked.string('file:AMSB_chargino_step4.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from DisappTrks.SignalMC.genParticlePlusGeant
from DisappTrks.SignalMC.genParticlePlusGeant import customizeKeep 

#call to customisation function customizeKeep imported from DisappTrks.SignalMC.genParticlePlusGeant
process = customizeKeep(process)

# Automatic addition of the customisation function from DisappTrks.SignalMC.recoCollectionsToKeep
from DisappTrks.SignalMC.recoCollectionsToKeep import customize 

#call to customisation function customize imported from DisappTrks.SignalMC.recoCollectionsToKeep
process = customize(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PATMC_cff')

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions
