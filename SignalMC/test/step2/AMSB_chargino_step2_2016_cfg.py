# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: step1 --filein dbs:/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/RunIISummer15wmLHEGS-MCRUN2_71_V1-v1/GEN-SIM --fileout file:EXO-RunIISpring16DR80-02856_step1.root --pileup_input dbs:/Neutrino_E-10_gun/RunIISpring15PrePremix-PU2016_80X_mcRun2_asymptotic_v14-v2/GEN-SIM-DIGI-RAW --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_v14 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:25ns10e33_v2 --nThreads 4 --datamix PreMix --era Run2_2016 --python_filename digi_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 960
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_25ns10e33_v2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(960)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/00CA136C-B93C-E611-8999-0025905C3E38.root',
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/022C5F76-B93C-E611-84E1-0025905C42F2.root',
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/0872B1B9-093D-E611-91FB-001E675A6D10.root',
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/14345472-FE3C-E611-ABA8-FA163E7F9948.root',
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/1698DF88-D33C-E611-9A65-0CC47A78A414.root',
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/18456E54-013D-E611-89CC-002590D60038.root',
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/1E6AF736-013D-E611-B2B1-FA163E999600.root',
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/205A752B-C53C-E611-87CA-0CC47A7452DA.root',
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/2E880440-033D-E611-8947-001A648F1A4E.root',
        '/store/mc/RunIISummer15wmLHEGS/MonoHZZ4l_ZpBaryonic_MZp-100_MChi-1_13TeV-madgraph/GEN-SIM/MCRUN2_71_V1-v1/00000/38E2BCA5-033D-E611-B3EC-003048CDBB94.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:960'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:EXO-RunIISpring16DR80-02856_step1.root'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
process.mixData.input.fileNames = cms.untracked.vstring([
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/0007596B-4543-E611-B86B-0CC47A4D7662.root',
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/0043B987-2C44-E611-A578-0025905C431A.root',
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/006EA8AD-0143-E611-9A58-0025905A6138.root',
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/007639A2-F142-E611-B2B6-0025905C3DD6.root',
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/00A47C69-3643-E611-8C35-0CC47A4D769C.root',
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/00BDAF47-2043-E611-9BBE-0CC47A4D75F2.root',
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/00C0978A-2943-E611-AF9A-0CC47A4D76CC.root',
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/00C81959-5D43-E611-A150-842B2B019EE5.root',
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/00EA78D9-5643-E611-965B-0CC47A78A4B8.root',
    '/store/mc/RunIISpring15PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PU2016_80X_mcRun2_asymptotic_v14-v2/00000/00F1DD25-4E43-E611-A345-0025905A612E.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_v14', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.PREMIXRAWoutput_step])

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from DisappTrks.SignalMC.genParticlePlusGeant
from DisappTrks.SignalMC.genParticlePlusGeant import customizeKeep

#call to customisation function customizeKeep imported from DisappTrks.SignalMC.genParticlePlusGeant
process = customizeKeep(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforFullSim(process)

# End of customisation functions
