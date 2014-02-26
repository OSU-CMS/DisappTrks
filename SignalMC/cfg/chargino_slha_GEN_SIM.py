# Auto generated configuration file
# using: 
# Revision: 1.352 
# Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/EightTeV/HSCPppstau_M_126_TuneZ2star_8TeV_pythia6_cff.py -s GEN,SIM --customise Configuration/GenProduction/EightTeV/Exotica_HSCP_SIM_cfi.customise --conditions START50_V13::All --beamspot Realistic8TeVCollision --datatier GEN-SIM --eventcontent RAWSIM -n 20 --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(3)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    annotation = cms.untracked.string('Configuration/GenProduction/python/EightTeV/HSCPppstau_M_126_TuneZ2star_8TeV_pythia6_cff.py nevts:20'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    #fileName = cms.untracked.string('HSCPppstau_M_126_TuneZ2star_8TeV_pythia6_cff_py_GEN_SIM.root'),
    fileName = cms.untracked.string('chargino_250GeV_32ctau_slha_GEN_SIM.root'),
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
#process.GlobalTag.globaltag = 'START53_V7::All'
process.GlobalTag.globaltag = 'START53_V11::All'

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    #pythiaPylistVerbosity = cms.untracked.int32(0),
    #stopHadrons = cms.bool(False),
    filterEfficiency = cms.untracked.double(1.0),
    #comEnergy = cms.double(8000.0),
    crossSection = cms.untracked.double(-1),
    maxEventsToPrint = cms.untracked.int32(1),
    #gluinoHadrons = cms.bool(False),
    #crossSection = cms.untracked.double(-1),
    #pythiaHepMCVerbosity = cms.untracked.bool(True),
    #maxEventsToPrint = cms.untracked.int32(10),
    #filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(8000.0),
    pythiaPylistVerbosity = cms.untracked.int32(3),

    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring(
            #'MSTU(21)=1     ! Check on possible errors during program execution', 
            #'MSTJ(22)=2     ! Decay those unstable particles', 
            #'PARJ(71)=10 .  ! for which ctau  10 mm', 
            #'MSTP(33)=0     ! no K factors in hard cross sections', 
            #'MSTP(2)=1      ! which order running alphaS', 
            #'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            #'MSTP(52)=2     ! work with LHAPDF', 
            #'PARP(82)=1.921 ! pt cutoff for multiparton interactions', 
            #'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            #'PARP(90)=0.227 ! Multiple interactions: rescaling power', 
            #'MSTP(95)=6     ! CR (color reconnection parameters)', 
            #'PARP(77)=1.016 ! CR', 
            #'PARP(78)=0.538 ! CR', 
            #'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            #'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            #'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            #'PARP(62)=1.025 ! ISR cutoff', 
            #'MSTP(91)=1     ! Gaussian primordial kT', 
            #'PARP(93)=10.0  ! primordial kT-max', 
            #'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            #'MSTP(82)=4     ! Defines the multi-parton model
                        'MSTU(21)=1      ! Check on possible errors during program execution',
            'MSTJ(11)=3      ! Choice of the fragmentation function',
            'MSTJ(22)=2      ! Decay those unstable particles',
            'PARJ(71)=10.    ! for which ctau  100 mm',
            #'PARJ(71)=2000.  ! for which ctau  100 mm',
            'MSTP(2)=1       ! which order running alphaS',
            'MSTP(33)=0      ! no K factors in hard cross sections',
            'MSTP(51)=10042  ! structure function chosen (external PDF CTEQ6L1)',
            'MSTP(52)=2      ! work with LHAPDF',
            'MSTP(81)=1      ! multiple parton interactions 1 is Pythia default',
            'MSTP(82)=4      ! Defines the multi-parton model',
            'MSTU(21)=1      ! Check on possible errors during program execution',
            'PARP(82)=1.8387 ! pt cutoff for multiparton interactions',
            'PARP(89)=1960.  ! sqrts for which PARP82 is set',
            'PARP(83)=0.5    ! Multiple interactions: matter distrbn parameter',
            'PARP(84)=0.4    ! Multiple interactions: matter distribution parameter',
            'PARP(90)=0.16   ! Multiple interactions: rescaling power',
            'PARP(67)=2.5    ! amount of initial-state radiation',
            'PARP(85)=1.0    ! gluon prod. mechanism in MI',
            'PARP(86)=1.0    ! gluon prod. mechanism in MI',
            'PARP(62)=1.25   !',
            'PARP(64)=0.2    !',
            'MSTP(91)=1      !',
            'PARP(91)=2.1    ! kt distribution',
            'PARP(93)=15.0   !'
        ),
        processParameters = cms.vstring(
            #'MSEL=0                  ! full user control ', 
            #'MSUB(207)=1             ! stau-staubar', 
#            'IMSS(1) = 1             ! Spectrum from external SLHA file', 
            #'IMSS(21) = 33            ! LUN number for SLHA File (must be 33)', 
            #'IMSS(22) = 33            ! Read-in SLHA decay table ', 
            #'MDCY(C1000015,1)=0       ! set the stau stable.'

            'IMSS(1) = 11             ! Spectrum from external SLHA file',
            'IMSS(21) = 33            ! LUN number for SLHA File (must be 33) ',
            'IMSS(22) = 33            ! Read-in SLHA decay table ',

            'MSEL        = 0        ! General SUSY',
#            'MSUB(243)   = 1        ! q + qbar -> ~g + ~g',
#            'MSUB(244)   = 1        ! g + g -> ~g + ~g',
#            'MSUB(258)   = 1        ! qj + g -> ~qj_L + ~g',
#            'MSUB(259)   = 1        ! qj + g -> ~qj_R + ~g',
#            'MSUB(271)   = 1        ! qi + qj -> ~qi_L + ~qj_L',
#            'MSUB(272)   = 1        ! qi + qj -> ~qi_R + ~qj_R',
#            'MSUB(273)   = 1        ! qi + qj -> ~qi_L + ~qj_R',
#            'MSUB(274)   = 1        ! qi+qjbar -> ~qi_L + ~qj_Lbar',
#            'MSUB(275)   = 1        ! qi+qjbar -> ~qi_R + ~qj_Rbar',
#            'MSUB(276)   = 1        ! qi+qjbar -> ~qi_L + ~qj_Rbar',
#            'MSUB(277)   = 1        ! f + fbar -> ~qi_L + ~qi_Lbar',
#            'MSUB(278)   = 1        ! f + fbar -> ~qi_R + ~qi_Rbar',
#            'MSUB(279)   = 1        ! g + g -> ~qi_L + ~qi_Lbar',
#           'MSUB(280)   = 1        ! g + g -> ~qi_R + ~qi_Rbar',
            'MSUB(226)    = 1        !to double chargino',
#	    'PMAS(312,1) = 250.0',
#	    'PMAS(310,1) = 249.0',
#            'MDCY(312,1)=0     ! set the chargino stable.',
#            'BRAT(2595)  = 1.0      ! branching ratio for IDC 2595',
#	    'KFDP(2595,1)= 1000022  ! decay into a neutralino -five positions reserved for each channel IDC',
#	    'KFDP(2595,2)= 211      ! decay into a pion',
#	    'KFDP(2595,3)= 0        ! decay into nothing',
#	    'KFDP(2595,4)= 0        ! same as above',
#	    'KFDP(2595,5)= 0        ! same as above',

        ),
        SLHAParameters = cms.vstring(
          'SLHAFILE = Configuration/Generator/data/pythia6_chargino_250.slha'
        ),
        parameterSets = cms.vstring('pythiaUESettings', 'processParameters', 'SLHAParameters')
    ),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(250),
    slhaFile = cms.untracked.string('Configuration/Generator/data/pythia6_chargino_250.slha'),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    particleFile = cms.untracked.string('Configuration/Generator/data/geant4_chargino_250.slha'),
    pdtFile = cms.FileInPath('Configuration/Generator/data/charginopdt_file.tbl')
)

# GEANT 4 Logging
# HWW:  This produces a lot of output!  Comment it out.  
#process.MessageLogger.destinations = ('cout', 'G4msg')
#process.MessageLogger.categories = ('PhysicsList','G4cout','G4cerr')
#process.MessageLogger.G4msg =  cms.untracked.PSet(
#    noTimeStamps = cms.untracked.bool(True),
#    PhysicsList = cms.untracked.PSet(limit = cms.untracked.int32(-1)),
#    G4cout = cms.untracked.PSet(limit = cms.untracked.int32(-1)),
#    G4cerr = cms.untracked.PSet(limit = cms.untracked.int32(-1))
#)


process.ProductionFilterSequence = cms.Sequence(process.generator)

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
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.GenProduction.EightTeV.Exotica_HSCP_SIM_cfi
from Configuration.GenProduction.EightTeV.Exotica_HSCP_SIM_cfi import customise 

#call to customisation function customise imported from Configuration.GenProduction.EightTeV.Exotica_HSCP_SIM_cfi
process = customise(process)

# End of customisation functions
