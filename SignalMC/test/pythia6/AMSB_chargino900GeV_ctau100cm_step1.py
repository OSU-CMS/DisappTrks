# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: DisappTrks/SignalMC/python/AMSB_chargino900GeV_ctau100cm_NoFilter_13TeV.py --fileout file:AMSB_chargino700GeV_ctau10cm_step1.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,DisappTrks/SignalMC/genParticlePlusGeant.customizeProduce,DisappTrks/SignalMC/genParticlePlusGeant.customizeKeep --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 --python_filename AMSB_chargino900GeV_ctau100cm_step1.py --no_exec -n 46
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(46)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/AMSB_chargino900GeV_ctau100cm_NoFilter_13TeV.py nevts:46'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:AMSB_chargino700GeV_ctau10cm_step1.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'MCRUN2_71_V1::All', '')

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(3),
    comEnergy = cms.double(13000.0),
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_AMSB_chargino_900GeV_ctau100cm.slha'),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    slhaFile = cms.untracked.string('DisappTrks/SignalMC/data/AMSB_chargino_900GeV_Isajet780.slha'),
    massPoint = cms.untracked.int32(900),
    hscpFlavor = cms.untracked.string('stau'),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution',
            'MSTJ(22)=2     ! Decay those unstable particles',
            'PARJ(71)=10 .  ! for which ctau  10 mm',
            'MSTP(33)=0     ! no K factors in hard cross sections',
            'MSTP(2)=1      ! which order running alphaS',
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
            'MSTP(52)=2     ! work with LHAPDF',
            'PARP(82)=1.921 ! pt cutoff for multiparton interactions',
            'PARP(89)=1800. ! sqrts for which PARP82 is set',
            'PARP(90)=0.227 ! Multiple interactions: rescaling power',
            'MSTP(95)=6     ! CR (color reconnection parameters)',
            'PARP(77)=1.016 ! CR',
            'PARP(78)=0.538 ! CR',
            'PARP(80)=0.1   ! Prob. colored parton from BBR',
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',
            'PARP(62)=1.025 ! ISR cutoff',
            'MSTP(91)=1     ! Gaussian primordial kT',
            'PARP(93)=10.0  ! primordial kT-max',
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring('IMSS(1)     = 11    ! Spectrum from external SLHA file',
            'IMSS(21)    = 33    ! LUN number for SLHA File (must be 33) ',
            'IMSS(22)    = 33    ! Read-in SLHA decay table ',
            'MSEL        = 0     ! General SUSY',
            'MSUB(226)   = 1     ! to double chargino',
            'MSUB(229)   = 1     ! to neutralino + chargino',
            'MDCY(312,1) = 0     ! set the chargino stable.'),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters',
            'SLHAParameters'),
        SLHAParameters = cms.vstring('SLHAFILE = DisappTrks/SignalMC/data/AMSB_chargino_900GeV_Isajet780.slha')
    )
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
        getattr(process,path)._seq = process.generator * getattr(process,path)._seq

# customisation of the process.

# Automatic addition of the customisation function from DisappTrks.SignalMC.genParticlePlusGeant
from DisappTrks.SignalMC.genParticlePlusGeant import customizeProduce,customizeKeep

#call to customisation function customizeProduce imported from DisappTrks.SignalMC.genParticlePlusGeant
process = customizeProduce(process)

#call to customisation function customizeKeep imported from DisappTrks.SignalMC.genParticlePlusGeant
process = customizeKeep(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise

#call to customisation function customise imported from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
process = customise(process)

# End of customisation functions
