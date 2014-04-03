# Auto generated configuration file
# using: 
# Revision: 1.381.2.27 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: DisappTrks/SignalMC/python/charginoParticleGun_cfi.py -s GEN,SIM --conditions START53_V27::All --beamspot Realistic8TeVCollision --datatier GEN-SIM --eventcontent RAWSIM -n 5 --no_exec --fileout charginoPartGun_GEN_SIM.root
# 
# Usage:
# > cmsRun charginoParticleGun_cfi_py_GEN_SIM.py 2>&1 | tee charginoParticleGun_cfi_py_GEN_SIM.log 
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
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.27 $'),
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/charginoParticleGun_cfi.py nevts:5'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('charginoPartGun_GEN_SIM_test.root'),
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

process.generator = cms.EDProducer("FlatRandomPtGunProducer",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    slhaFile = cms.untracked.string('Configuration/Generator/data/AMSB_chargino_100GeV_Isajet780.slha'),
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_AMSB_chargino_test.slha'), 
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    comEnergy = cms.double(8000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(150),
    PGunParameters = cms.PSet(
        MaxPt = cms.double(100.01),
        MinPt = cms.double(99.99),
        PartID = cms.vint32(1000024),
        MaxEta = cms.double(2.5),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-2.5),
        MinPhi = cms.double(-3.14159265359)
    ),
    Verbosity = cms.untracked.int32(0),
    psethack = cms.string('chargino pt 100'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
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

from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise  
#from DisappTrks.SignalMC.Exotica_HSCP_SIM_cfi import customise  
process = customise(process)    



# Testing:  
#process.RAWSIMoutput.fileName = cms.untracked.string('charginoPartGun_GEN_SIM_5nsDefault.root')

process.RAWSIMoutput.fileName = cms.untracked.string('charginoPartGun_GEN_SIM_5nsWithDecayFlagsOn.root') 
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInTracker = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInCalo    = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInMuon    = cms.untracked.bool(True)

process.g4SimHits.SteppingAction.MaxTrackTimes = cms.vdouble(2000.0, 500.0, 500.0)
process.g4SimHits.StackingAction.MaxTrackTimes = cms.vdouble(2000.0, 500.0, 500.0)
process.common_maximum_time.MaxTrackTimes      = cms.vdouble(2000.0, 500.0, 500.0)

## process.RAWSIMoutput.fileName = cms.untracked.string('charginoPartGun_GEN_SIM_5nsWithDecayFlagsOnCodeFixed.root')   # Must fix code in StackingAction.cc and then recompile!
## process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInTracker = cms.untracked.bool(True)
## process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInCalo    = cms.untracked.bool(True)
## process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInMuon    = cms.untracked.bool(True)

# Dump config file:  
outfile = open('dumpedConfig_GEN_SIM.py','w'); print >> outfile,process.dumpPython(); outfile.close()
