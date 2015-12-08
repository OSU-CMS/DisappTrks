# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein file:AMSB_chargino_step1.root --fileout file:AMSB_chargino_step2a.root --pileup_input dbs:/MinBias_TuneZ2star_8TeV-pythia6/Summer12-START50_V13-v3/GEN-SIM --mc --eventcontent RAWSIM --pileup 2012_Summer_50ns_PoissonOOTPU --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring,DisappTrks/SignalMC/genParticlePlusGeant.customizeKeep --datatier GEN-SIM-RAW --conditions MCRUN2_74_V9 --step DIGI,L1,DIGI2RAW --magField 38T_PostLS1 --python_filename AMSB_chargino_8TeV_step2a_cfg.py --no_exec -n 82
import FWCore.ParameterSet.Config as cms

process = cms.Process('DIGI2RAW')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_2012_Summer_50ns_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(82)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:AMSB_chargino_step1.root'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:82'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:AMSB_chargino_step2a.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.input.fileNames = cms.untracked.vstring(['/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/0005E496-3661-E111-B31E-003048F0E426.root', '/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/003EEBD4-8061-E111-9A23-003048D437F2.root', '/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/005825F1-F260-E111-BD97-003048C692DA.root', '/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/0065594C-B35E-E111-8B8C-003048C693EA.root', '/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/0091FFD0-6B5E-E111-92FE-003048C693DA.root', '/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/00C69AE3-FE60-E111-BC48-0030487D8633.root', '/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/02079692-AC61-E111-97BB-0025901D4D54.root', '/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/021BD915-2D61-E111-8BAD-002481E76052.root', '/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/02386E4D-DC5E-E111-9413-00266CF1074C.root', '/store/mc/Summer12/MinBias_TuneZ2star_8TeV-pythia6/GEN-SIM/START50_V13-v3/0000/02446A08-515E-E111-82C7-00266CF330B8.root'])
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_74_V9', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step,process.endjob_step,process.RAWSIMoutput_step)

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

# End of customisation functions

