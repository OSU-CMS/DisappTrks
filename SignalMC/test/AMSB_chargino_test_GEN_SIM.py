# Auto generated configuration file
# using: 
# Revision: 1.381.2.27 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: DisappTrks/SignalMC/python/AMSB_chargino_cfi.py -s GEN,SIM --conditions START53_V27::All --beamspot Realistic8TeVCollision --datatier GEN-SIM --eventcontent RAWSIM -n 5 --no_exec --fileout AMSB_chargino_test_GEN_SIM.root
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
        output = cms.untracked.int32(3)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.27 $'),
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/AMSB_chargino_cfi.py nevts:5'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('AMSB_chargino_test_GEN_SIM.root'),
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

process.dicharginoSumPtFilter = cms.EDFilter("MCParticlePairSumPtFilter",
    MinSumPt = cms.untracked.double(50.0),
    ParticleIDs = cms.untracked.vint32(1000022, 1000024)
)


process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(3),
    comEnergy = cms.double(8000.0),
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_AMSB_chargino_100GeV_ctau10cm.slha'),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    slhaFile = cms.untracked.string('DisappTrks/SignalMC/data/AMSB_chargino_100GeV_Isajet780.slha'),
    massPoint = cms.untracked.int32(-999),
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
        SLHAParameters = cms.vstring('SLHAFILE = DisappTrks/SignalMC/data/AMSB_chargino_100GeV_Isajet780.slha')
    )
)


process.ProductionFilterSequence = cms.Sequence(process.generator+process.dicharginoSumPtFilter)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genParticlePlusGeant = cms.EDProducer("GenPlusSimParticleProducer",
					      src           = cms.InputTag("g4SimHits"),   # use "famosSimHits" for FAMOS
					      setStatus     = cms.int32(8),                # set status = 8 for GEANT GPs
					      filter        = cms.vstring("pt > 0.0"),     # just for testing (optional)
					      genParticles  = cms.InputTag("genParticles") # original genParticle list
					      )
process.simulation_step = cms.Path(process.psim + process.genParticlePlusGeant)  
process.RAWSIMoutput.outputCommands.extend( [
	"keep *_genParticlePlusGeant_*_*",
	] )   
#process.simulation_step = cms.Path(process.psim)  # original
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 



# The configuration settings below are needed for simulating long-lived charginos:  



from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise  
process = customise(process)    


process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInTracker = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInCalo    = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInMuon    = cms.untracked.bool(True)

process.g4SimHits.SteppingAction.MaxTrackTimes = cms.vdouble(2000.0, 500.0, 500.0)
process.g4SimHits.StackingAction.MaxTrackTimes = cms.vdouble(2000.0, 500.0, 500.0)
process.common_maximum_time.MaxTrackTimes      = cms.vdouble(2000.0, 500.0, 500.0)

## Dump python config if wished
outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()




