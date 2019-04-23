import sys

mChargino=sys.argv[1]
mNeutralino=sys.argv[2]
ctau=sys.argv[3]
pt=sys.argv[4]
dR=sys.argv[5]

output_file = sys.environ["CMSSW_BASE"]+'/DisappTrks/SignalMC/test/FakeDecay_step1_data/Fakedecay_chargino'+mChargino+'GeV_ctau'+ctau+'cm_pt'+pt+'GeV_neutralino'+mNeutralino+'GeV_maxdR'+dR+'_3bd_step1.root'
slha_source = 'DisappTrks/SignalMC/data/Fakedecay_SLHA/FakeDecay_chargino_'+mChargino+'GeV_neutralino_'+mNeutralino+'GeV_Isajet780.slha' 
qslha_source = '''  'DisappTrks/SignalMC/data/Fakedecay_SLHA/FakeDecay_chargino_'''+mChargino+'GeV_neutralino_'+mNeutralino +'''GeV_Isajet780.slha' '''
decay_source = '''  'DisappTrks/SignalMC/data/geant4_fakedecay/geant4_chargino_'''+mChargino+'GeV_ctau_'+ctau+'cm_neutralino_'+mNeutralino+'''GeV_3bd.slha' '''

cfg_file_name = 'Fakedecay_chargino'+mChargino+'GeV_ctau'+ctau+'cm_pt'+pt+'GeV_neutralino'+mNeutralino+'GeV_maxdR'+dR+'_3bd_step1.py' 
working_directory = 'chargino'+mChargino+'GeV_ctau'+ctau+'cm_pt'+pt+'GeV_neutralino'+mNeutralino+'GeV_dR'+dR

condor_file = open("run_osusub_auto.sh","w+")
condor_file.write(
'''osusub.py -n 100\
 -t None\
 -f process.RAWSIMoutput.fileName\
 -U -r\
 -m 100000\
 -c '''
+
cfg_file_name
+
'''\
 -w FakeDecay/step1/'''
+
working_directory
+
'''/ \
 -g
'''
)

cfg_file = open(cfg_file_name,"w+")
cfg_file.write(
'''
# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: DisappTrks/SignalMC/python/charginoParticleGun_cfi.py -s GEN,SIM --conditions auto:mc --mc --datatier GEN-SIM --eventcontent RAWSIM -n 5 --no_exec --fileout charginoPartGun_GEN_SIM.root
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
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')  # old
#process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')  # old
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/charginoParticleGun_cfi.py nevts:5'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition


process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('p2')
#        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string(' '''
+
output_file
+
''' '),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDProducer("Pythia6PtGun",
#                                   pythiaPylistVerbosity = cms.untracked.int32(0),
                                   slhaFile = cms.untracked.string('''
+
qslha_source
+
''' ),
                                   particleFile = cms.untracked.string('''
+
decay_source
+
''' ),
                                   filterEfficiency = cms.untracked.double(1.0),
                                   pythiaHepMCVerbosity = cms.untracked.bool(False),
                                   processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
                                   useregge = cms.bool(False),
#                                   comEnergy = cms.double(8000.0),
                                   maxEventsToPrint = cms.untracked.int32(0),
                                   hscpFlavor = cms.untracked.string('stau'),
                                   massPoint = cms.untracked.int32(100),
    PGunParameters = cms.PSet(
        MaxEta = cms.double(2.2),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double( %.2f ),
        MinEta = cms.double(-2.2),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double( %.2f ),
        PartID = cms.vint32(1000024),
        ParticleID = cms.vint32(1000024),
        AddAntiParticle = cms.bool(False),
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('chargino pt 50'),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution',
            'MSTJ(22)=2     ! Decay those unstable particles',
            'PARJ(71)=100. ! for which ctau  100 mm',
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
        SLHAParameters = cms.vstring('SLHAFILE = ''' %( float(pt)+10.0 , float(pt))
+
slha_source
+
''' '),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters',
            'SLHAParameters'),
    )
)

process.filter1 = cms.EDFilter("HepMCDecayFilter",
				  ModuleLabel = cms.untracked.string('generator'),
				  ParticleIDs = cms.untracked.vint32(1000024),
#				  DecayRadius = cms.untracked.double(50),
)
process.p1 = cms.Path(process.filter1)

process.filter2 = cms.EDFilter("DecayPositionFilter",
				  ModuleLabel = cms.untracked.string('generator'),
				  ParticleIDs = cms.untracked.vint32(1000024),
				  DecayRadius = cms.untracked.vdouble(50),
                                  maxDeltaR = cms.untracked.vdouble( %.2f ),
)

process.p2 = cms.Path(process.filter2)

# Path and EndPath definitions
process.ProductionFilterSequence = cms.Sequence(process.generator * process.filter1)
process.generation_step = cms.Path(process.pgen)

process.genParticlePlusGeant = cms.EDProducer("GenPlusSimParticleProducer",
                                              src = cms.InputTag("g4SimHits"), # use "famosSimHits" for FAMOS
                                              setStatus = cms.int32(8), # set status = 8 for GEANT GPs
                                              filter = cms.vstring("pt > 0.0"), # just for testing (optional)
                                              genParticles = cms.InputTag("genParticles") # original genParticle list
                                              )
process.simulation_step = cms.Path(process.psim + process.genParticlePlusGeant)
process.RAWSIMoutput.outputCommands.extend( [
                "keep *_genParticlePlusGeant_*_*",
                ] )

#process.simulation_step = cms.Path(process.psim)

process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step, process.genfiltersummary_step,process.simulation_step, process.p2,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
        getattr(process,path)._seq = process.generator * getattr(process,path)._seq


from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise
process = customise(process)

process.MessageLogger = cms.Service("MessageLogger",
                                    destinations   = cms.untracked.vstring(
                                            'detailedInfo'
                                            ,'critical'
                                            ,'cerr'
                                    ),
                                    debugModules     = cms.untracked.vstring('CustomPhysics'),
                                    critical       = cms.untracked.PSet(
                                            threshold = cms.untracked.string('ERROR')
                                    ),
                                    detailedInfo   = cms.untracked.PSet(
                                            threshold  = cms.untracked.string('INFO')
                                    ),
                                    cerr           = cms.untracked.PSet(
                                            threshold  = cms.untracked.string('WARNING')
                                    )
)

# Dump config file:
outfile = open('dumpedConfig_GEN_SIM.py','w'); print >> outfile,process.dumpPython(); outfile.close()
''' %(float(dR)/10.0)
)

cfg_file.close()
