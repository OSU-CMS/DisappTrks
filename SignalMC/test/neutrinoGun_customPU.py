# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/FSQ-RunIISpring16FSPremix-00002-fragment.py --fileout file:FSQ-RunIISpring16FSPremix-00002.root --pileup_input dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISpring16FSPremix-80X_mcRun2_asymptotic_2016_v3-v1/GEN-SIM-RECO --mc --eventcontent PREMIX --fast --pileup 2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU --datatier GEN-SIM-DIGI-RAW --conditions 80X_mcRun2_asymptotic_2016_v3 --step GEN,SIM,RECOBEFMIX,DIGIPREMIX,L1,DIGI2RAW --era Run2_25ns --python_filename /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/FSQ-RunIISpring16FSPremix-00002/FSQ-RunIISpring16FSPremix-00002_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 77
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('DIGI2RAW',eras.Run2_25ns,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.Digi_PreMix_cff')
process.load('SimGeneral.MixingModule.digi_noNoise_cfi')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/FSQ-RunIISpring16FSPremix-00002-fragment.py nevts:77'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:FSQ-RunIISpring16FSPremix-00002.root'),
    outputCommands = process.PREMIXEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/000226B9-0D0B-E611-8B41-3417EBE5297E.root', '/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/005DC625-140B-E611-A0B4-00266CF20468.root', '/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/0064BEF8-000B-E611-9EC0-90B11CBCFF9C.root', '/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/025AE15D-080B-E611-9F68-0025905C54B8.root', '/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/026C010B-010B-E611-8C97-0025905D1C56.root', '/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/02E32831-190B-E611-B10B-20CF3019DF00.root', '/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/04D5D1FB-0B0B-E611-B254-3417EBE528A6.root', '/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/04FCF3A4-190B-E611-96CF-00259073E4CE.root', '/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/080C642A-010B-E611-8F90-0025904C63F8.root', '/store/mc/RunIISpring16FSPremix/MinBias_TuneCUETP8M1_13TeV-pythia8/GEN-SIM-RECO/80X_mcRun2_asymptotic_2016_v3-v1/70000/085CEE26-020B-E611-9F98-0025904CF712.root'])
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersNoNoise)

# Custom pileup distribution taken from 2016DEFGH data (data2016_DEFGH in DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root)
process.mix.input.nbPileupEvents.probFunctionVariable = cms.vint32(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99)
process.mix.input.nbPileupEvents.probValue = cms.vdouble(
  8.4937e-06,
  2.71768e-05,
  6.81714e-05,
  8.28672e-05,
  0.00011154,
  0.000150187,
  0.000167938,
  0.000203328,
  0.00026763,
  0.000405385,
  0.001783,
  0.00616946,
  0.0128909,
  0.0203069,
  0.0280718,
  0.036253,
  0.043019,
  0.0473231,
  0.0496637,
  0.0510143,
  0.0524638,
  0.0542179,
  0.055356,
  0.0552566,
  0.0541784,
  0.0524789,
  0.0502414,
  0.047473,
  0.0442041,
  0.0404664,
  0.0363177,
  0.0318826,
  0.0273514,
  0.0229359,
  0.0188199,
  0.0151276,
  0.0119162,
  0.00918979,
  0.0069214,
  0.00507277,
  0.00360342,
  0.00247144,
  0.00163126,
  0.00103344,
  0.000627143,
  0.000364,
  0.000201845,
  0.000106853,
  5.39789e-05,
  2.60175e-05,
  1.19677e-05,
  5.25713e-06,
  2.20828e-06,
  8.88951e-07,
  3.44098e-07,
  1.28694e-07,
  4.68064e-08,
  1.66885e-08,
  5.88759e-09,
  2.07607e-09,
  7.39328e-10,
  2.68713e-10,
  1.00721e-10,
  3.92968e-11,
  1.60502e-11,
  6.85975e-12,
  3.04627e-12,
  1.38962e-12,
  6.43243e-13,
  2.9899e-13,
  1.3848e-13,
  6.35805e-14,
  2.88451e-14,
  1.29061e-14,
  5.68856e-15,
  2.46839e-15,
  1.05404e-15,
  4.42808e-16,
  1.82986e-16,
  7.43693e-17,
  2.97233e-17,
  1.1681e-17,
  4.51336e-18,
  1.71438e-18,
  6.40059e-19,
  2.35094e-19,
  8.46585e-20,
  3.01068e-20,
  1.04357e-20,
  3.42808e-21,
  1.19443e-21,
  4.00211e-22,
  1.94276e-22,
  0,
  0,
  0,
  0,
  0,
  0,
  0
)


process.esDigiToRaw.Label = cms.string('mix')
process.SiStripDigiToRaw.FedReadoutMode = cms.string('PREMIX_RAW')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_mcRun2_asymptotic_2016_v3', '')

process.generator = cms.EDProducer("FlatRandomEGunProducer",
    AddAntiParticle = cms.bool(False),
    PGunParameters = cms.PSet(
        MaxE = cms.double(10.01),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MinE = cms.double(9.99),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359),
        PartID = cms.vint32(12)
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('single Nu E 10')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXoutput_step = cms.EndPath(process.PREMIXoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.PREMIXoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

