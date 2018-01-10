# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: DisappTrks/SignalMC/python/pythia8Decay/AMSB_chargino300GeV_ctau100cm_NoFilter_13TeV.py --fileout file:AMSB_chargino300GeV_ctau100cm_step1.root --mc --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,SimG4Core/Application/customiseSequentialSim.customiseSequentialSim --datatier GEN-SIM --conditions 94X_mc2017_realistic_v10 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --geometry DB:Extended --era Run2_2017 --python_filename step1/pythia8Decay/AMSB_chargino300GeV_ctau100cm_step1.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
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
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/pythia8Decay/AMSB_chargino300GeV_ctau100cm_NoFilter_13TeV.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:AMSB_chargino300GeV_ctau100cm_step1.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v10', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters'),
        processParameters = cms.vstring('SUSY:all = off', 
            'SUSY:qqbar2chi+chi- = on', 
            'SUSY:qqbar2chi+-chi0 = on', 
            '1000024:tau0 = 1000.0', 
            'ParticleDecays:tau0Max = 10000.0'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    SLHATableForPythia8 = cms.string('\n#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format\n#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009\nBlock SPINFO   # Program information\n     1   ISASUGRA from ISAJET          # Spectrum Calculator\n     2   7.80   29-OCT-2009 12:50:36   # Version number\nBlock MODSEL   # Model selection\n     1     3   # Minimal anomaly mediated (AMSB) model\nBlock SMINPUTS   # Standard Model inputs\n     1     1.27843719E+02   # alpha_em^(-1)\n     2     1.16570000E-05   # G_Fermi\n     3     1.17200002E-01   # alpha_s(M_Z)\n     4     9.11699982E+01   # m_{Z}(pole)\n     5     4.19999981E+00   # m_{b}(m_{b})\n     6     1.73070007E+02   # m_{top}(pole)\n     7     1.77699995E+00   # m_{tau}(pole)\nBlock MINPAR   # SUSY breaking input parameters\n     1     1.50000000E+03   # m_0\n     2     1.03650000E+05   # m_{3/2}\n     3     5.00000000E+00   # tan(beta)\n     4     1.00000000E+00   # sign(mu)\nBlock EXTPAR   # Non-universal SUSY breaking parameters\n     0     1.21940317E+16   # Input scale\nBlock MASS   # Scalar and gaugino mass spectrum\n#  PDG code   mass                 particle\n        24     8.04229965E+01   #  W^+\n        25     1.13281731E+02   #  h^0\n        35     2.31703979E+03   #  H^0\n        36     2.30156934E+03   #  A^0\n        37     2.31312744E+03   #  H^+\n   1000001     2.49383179E+03   #  dnl\n   1000002     2.49261523E+03   #  upl\n   1000003     2.49383179E+03   #  stl\n   1000004     2.49261548E+03   #  chl\n   1000005     2.15123779E+03   #  b1\n   1000006     1.73482275E+03   #  t1\n   1000011     1.43890710E+03   #  el-\n   1000012     1.43549438E+03   #  nuel\n   1000013     1.43890710E+03   #  mul-\n   1000014     1.43549438E+03   #  numl\n   1000015     1.42184009E+03   #  tau1\n   1000016     1.43293103E+03   #  nutl\n   1000021     2.18962207E+03   #  glss\n   1000022     2.99864838E+02   #  z1ss\n   1000023     9.52063293E+02   #  z2ss\n   1000024     3.00137323E+02   #  w1ss !!! IMPORTANT NOTE: 100 MeV has been added to this to get past ResonanceDecays::MSAFETY = 100 MeV\n   1000025    -1.74983081E+03   #  z3ss\n   1000035     1.75280737E+03   #  z4ss\n   1000037     1.75418726E+03   #  w2ss\n   2000001     2.52172412E+03   #  dnr\n   2000002     2.50711743E+03   #  upr\n   2000003     2.52172412E+03   #  str\n   2000004     2.50711792E+03   #  chr\n   2000005     2.50527832E+03   #  b2\n   2000006     2.17448901E+03   #  t2\n   2000011     1.42790625E+03   #  er-\n   2000013     1.42790625E+03   #  mur-\n   2000015     1.43795154E+03   #  tau2\nBlock ALPHA   # Effective Higgs mixing parameter\n         -1.98217750E-01   # alpha\nBlock STOPMIX   # stop mixing matrix\n  1  1     1.15278468E-01   # O_{11}\n  1  2    -9.93333220E-01   # O_{12}\n  2  1     9.93333220E-01   # O_{21}\n  2  2     1.15278468E-01   # O_{22}\nBlock SBOTMIX   # sbottom mixing matrix\n  1  1     9.99966919E-01   # O_{11}\n  1  2     8.13260302E-03   # O_{12}\n  2  1    -8.13260302E-03   # O_{21}\n  2  2     9.99966919E-01   # O_{22}\nBlock STAUMIX   # stau mixing matrix\n  1  1     3.27634096E-01   # O_{11}\n  1  2     9.44804668E-01   # O_{12}\n  2  1    -9.44804668E-01   # O_{21}\n  2  2     3.27634096E-01   # O_{22}\nBlock NMIX   # neutralino mixing matrix\n  1  1    -1.78793352E-03   #\n  1  2     9.98812914E-01   #\n  1  3    -4.60493490E-02   #\n  1  4     1.57782547E-02   #\n  2  1     9.99014318E-01   #\n  2  2     3.87472054E-03   #\n  2  3     3.69140282E-02   #\n  2  4    -2.43423060E-02   #\n  3  1     8.95513594E-03   #\n  3  2    -2.13845931E-02   #\n  3  3    -7.06530809E-01   #\n  3  4    -7.07302272E-01   #\n  4  1     4.34374809E-02   #\n  4  2    -4.35934253E-02   #\n  4  3    -7.05217123E-01   #\n  4  4     7.06315577E-01   #\nBlock UMIX   # chargino U mixing matrix\n  1  1    -9.97862458E-01   # U_{11}\n  1  2     6.53490350E-02   # U_{12}\n  2  1    -6.53490350E-02   # U_{21}\n  2  2    -9.97862458E-01   # U_{22}\nBlock VMIX   # chargino V mixing matrix\n  1  1    -9.99705255E-01   # V_{11}\n  1  2     2.42768954E-02   # V_{12}\n  2  1    -2.42768954E-02   # V_{21}\n  2  2    -9.99705255E-01   # V_{22}\nBlock GAUGE Q=  1.85234131E+03   #\n     1     3.57492119E-01   # g`\n     2     6.52495980E-01   # g_2\n     3     1.22099257E+00   # g_3\nBlock YU Q=  1.85234131E+03   #\n  3  3     8.58246148E-01   # y_t\nBlock YD Q=  1.85234131E+03   #\n  3  3     6.76042885E-02   # y_b\nBlock YE Q=  1.85234131E+03   #\n  3  3     5.14520593E-02   # y_tau\nBlock HMIX Q=  1.85234131E+03   # Higgs mixing parameters\n     1     1.74554053E+03   # mu(Q)\n     2     5.00000000E+00   # tan(beta)(M_GUT)\n     3     2.51296097E+02   # Higgs vev at Q\n     4     5.29722150E+06   # m_A^2(Q)\nBlock MSOFT Q=  1.85234131E+03   # DRbar SUSY breaking parameters\n     1     9.59482605E+02   # M_1(Q)\n     2     2.83875336E+02   # M_2(Q)\n     3    -2.03255798E+03   # M_3(Q)\n    31     1.43290662E+03   # MeL(Q)\n    32     1.43290662E+03   # MmuL(Q)\n    33     1.43040063E+03   # MtauL(Q)\n    34     1.42463135E+03   # MeR(Q)\n    35     1.42463135E+03   # MmuR(Q)\n    36     1.41936206E+03   # MtauR(Q)\n    41     2.38789746E+03   # MqL1(Q)\n    42     2.38789746E+03   # MqL2(Q)\n    43     2.05947778E+03   # MqL3(Q)\n    44     2.40229883E+03   # MuR(Q)\n    45     2.40229883E+03   # McR(Q)\n    46     1.66603821E+03   # MtR(Q)\n    47     2.41674878E+03   # MdR(Q)\n    48     2.41674878E+03   # MsR(Q)\n    49     2.42613452E+03   # MbR(Q)\nBlock AU Q=  1.85234131E+03   #\n  1  1     1.71933716E+03   # A_u\n  2  2     1.71933716E+03   # A_c\n  3  3     1.71933716E+03   # A_t\nBlock AD Q=  1.85234131E+03   #\n  1  1     4.09207031E+03   # A_d\n  2  2     4.09207031E+03   # A_s\n  3  3     4.09207031E+03   # A_b\nBlock AE Q=  1.85234131E+03   #\n  1  1     1.09036902E+03   # A_e\n  2  2     1.09036902E+03   # A_mu\n  3  3     1.09036902E+03   # A_tau\n#\n#\n#\n#                             =================\n#                             |The decay table|\n#                             =================\n#\n#         PDG            Width\nDECAY   1000024     1.97326979e-16 # chargino decay\n#          BR         NDA      ID1       ID2\n           1.0        2        1000022   211\n'),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(1.0),
    filterEfficiency = cms.untracked.double(-1),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(300),
    maxEventsToPrint = cms.untracked.int32(0),
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_add100MeV/AMSBchargino_300GeV.slha'),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    slhaFile = cms.untracked.string(''),
    useregge = cms.bool(False)
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise 

#call to customisation function customise imported from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi
process = customise(process)

# Automatic addition of the customisation function from SimG4Core.Application.customiseSequentialSim
from SimG4Core.Application.customiseSequentialSim import customiseSequentialSim 

#call to customisation function customiseSequentialSim imported from SimG4Core.Application.customiseSequentialSim
process = customiseSequentialSim(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
