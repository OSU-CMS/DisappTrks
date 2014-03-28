# Auto generated configuration file
# using: 
# Revision: 1.381.2.27 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: DisappTrks/SignalMC/python/amsb_mGravXXX_YYYns_cfi.py -s GEN,SIM --conditions START53_V27::All --beamspot Realistic8TeVCollision --datatier GEN-SIM --eventcontent RAWSIM -n 5 --no_exec --fileout chargino_amsb_GEN_SIM.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.27 $'),
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/amsb_mGravXXX_YYYns_cfi.py nevts:5'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('AMSB_chargino_test_GEN.root'),
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
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V27::All', '')

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(3),
    slhaFile = cms.untracked.string('DisappTrks/SignalMC/data/AMSB_chargino_100GeV_Isajet780.slha'),
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_AMSB_chargino_test.slha'), 
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    comEnergy = cms.double(8000.0),
    maxEventsToPrint = cms.untracked.int32(1),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(150),
    useregge = cms.bool(False), 
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTJ(11)=3     ! Choice of the fragmentation function', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'MSTP(81)=1     ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model', 
            'MSTU(21)=1     ! Check on possible errors during program execution', 
            'PARP(82)=1.8387   ! pt cutoff for multiparton interactions', 
            'PARP(89)=1960. ! sqrts for which PARP82 is set', 
            'PARP(83)=0.5   ! Multiple interactions: matter distrbn parameter', 
            'PARP(84)=0.4   ! Multiple interactions: matter distribution parameter', 
            'PARP(90)=0.16  ! Multiple interactions: rescaling power', 
            'PARP(67)=2.5    ! amount of initial-state radiation', 
            'PARP(85)=1.0  ! gluon prod. mechanism in MI', 
            'PARP(86)=1.0  ! gluon prod. mechanism in MI', 
            'PARP(62)=1.25   ! ', 
            'PARP(64)=0.2    ! ', 
            'MSTP(91)=1      !', 
            'PARP(91)=2.1   ! kt distribution', 
            'PARP(93)=15.0  ! '),
        processParameters = cms.vstring('IMSS(1)     = 11    ! Spectrum from external SLHA file', 
            'IMSS(21)    = 33    ! LUN number for SLHA File (must be 33) ', 
            'IMSS(22)    = 33    ! Read-in SLHA decay table ', 
            'MSEL        = 0     ! General SUSY', 
            'MSUB(226)   = 1     ! to double chargino', 
#            'MSUB(229)   = 1     ! to neutralino + chargino', 
            'MDCY(312,1) = 0     ! set the chargino stable.'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters', 
            'SLHAParameters'),
        SLHAParameters = cms.vstring('SLHAFILE = DisappTrks/SignalMC/data/AMSB_chargino_100GeV_Isajet780.slha')
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


# Lines below special for disappearing tracks:      
from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise  
process = customise(process)    

process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInTracker = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInCalo    = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInMuon    = cms.untracked.bool(True)

process.g4SimHits.SteppingAction.MaxTrackTimes = cms.vdouble(2000.0, 500.0, 500.0)
process.g4SimHits.StackingAction.MaxTrackTimes = cms.vdouble(2000.0, 500.0, 500.0)
process.common_maximum_time.MaxTrackTimes      = cms.vdouble(2000.0, 500.0, 500.0)


## Dump python config if wished
outfile = open('dumpedConfig_GEN_SIM.py','w'); print >> outfile,process.dumpPython(); outfile.close()

    
