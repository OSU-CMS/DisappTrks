# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: DisappTrks/SignalMC/python/pythia8Decay/AMSB_chargino100GeV_ctau10cm_NoFilter_13TeV.py --fileout file:AMSB_chargino100GeV_ctau10cm_step1.root --mc --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,SimG4Core/Application/customiseSequentialSim.customiseSequentialSim --datatier GEN-SIM --conditions 94X_mc2017_realistic_v10 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --geometry DB:Extended --era Run2_2017 --python_filename step1/pythia8Decay/AMSB_chargino100GeV_ctau10cm_step1.py --no_exec -n 10
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
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/pythia8Decay/AMSB_chargino100GeV_ctau10cm_NoFilter_13TeV.py nevts:10'),
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
    fileName = cms.untracked.string('file:AMSB_chargino100GeV_ctau10cm_step1.root'),
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
            'pythia8CP5Settings', 
            'processParameters'),
        processParameters = cms.vstring('SUSY:all = off', 
            'SUSY:qqbar2chi+chi- = on', 
            'SUSY:qqbar2chi+-chi0 = on', 
            '1000024:isResonance = false', 
            '1000024:oneChannel = 1 1.0 100 1000022 211', 
            '1000024:tau0 = 100.0', 
            'ParticleDecays:tau0Max = 1000.0'),
        pythia8CP5Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'PDF:pSet=20', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118'),
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
    SLHATableForPythia8 = cms.string('\n#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format\n#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009\nBlock SPINFO   # Program information\n     1   ISASUGRA from ISAJET          # Spectrum Calculator\n     2   7.80   29-OCT-2009 12:50:36   # Version number\nBlock MODSEL   # Model selection\n     1     3   # Minimal anomaly mediated (AMSB) model\nBlock SMINPUTS   # Standard Model inputs\n     1     1.27843697E+02   # alpha_em^(-1)\n     2     1.16570000E-05   # G_Fermi\n     3     1.17200002E-01   # alpha_s(M_Z)\n     4     9.11699982E+01   # m_{Z}(pole)\n     5     4.19999981E+00   # m_{b}(m_{b})\n     6     1.73070007E+02   # m_{top}(pole)\n     7     1.77699995E+00   # m_{tau}(pole)\nBlock MINPAR   # SUSY breaking input parameters\n     1     1.50000000E+03   # m_0\n     2     3.50800000E+04   # m_{3/2}\n     3     5.00000000E+00   # tan(beta)\n     4     1.00000000E+00   # sign(mu)\nBlock EXTPAR   # Non-universal SUSY breaking parameters\n     0     1.26820216E+16   # Input scale\nBlock MASS   # Scalar and gaugino mass spectrum\n#  PDG code   mass                 particle\n        24     8.04229965E+01   #  W^+\n        25     1.09165016E+02   #  h^0\n        35     1.69811304E+03   #  H^0\n        36     1.68658362E+03   #  A^0\n        37     1.69844373E+03   #  H^+\n   1000001     1.64875269E+03   #  dnl\n   1000002     1.64692371E+03   #  upl\n   1000003     1.64875269E+03   #  stl\n   1000004     1.64692432E+03   #  chl\n   1000005     1.36096313E+03   #  b1\n   1000006     1.00422571E+03   #  t1\n   1000011     1.49030664E+03   #  el-\n   1000012     1.48858191E+03   #  nuel\n   1000013     1.49030664E+03   #  mul-\n   1000014     1.48858191E+03   #  numl\n   1000015     1.48539880E+03   #  tau1\n   1000016     1.48676428E+03   #  nutl\n   1000021     8.64298706E+02   #  glss\n   1000022     9.98443985E+01   #  z1ss\n   1000023     3.20083069E+02   #  z2ss\n   1000024     1.00132974E+02   #  w1ss\n   1000025    -7.42030518E+02   #  z3ss\n   1000035     7.49072571E+02   #  z4ss\n   1000037     7.49086609E+02   #  w2ss\n   2000001     1.65904858E+03   #  dnr\n   2000002     1.65516052E+03   #  upr\n   2000003     1.65904858E+03   #  str\n   2000004     1.65516113E+03   #  chr\n   2000005     1.65050024E+03   #  b2\n   2000006     1.37387744E+03   #  t2\n   2000011     1.49084143E+03   #  er-\n   2000013     1.49084143E+03   #  mur-\n   2000015     1.48991235E+03   #  tau2\nBlock ALPHA   # Effective Higgs mixing parameter\n         -1.98805586E-01   # alpha\nBlock STOPMIX   # stop mixing matrix\n  1  1     6.12325780E-02   # O_{11}\n  1  2    -9.98123527E-01   # O_{12}\n  2  1     9.98123527E-01   # O_{21}\n  2  2     6.12325780E-02   # O_{22}\nBlock SBOTMIX   # sbottom mixing matrix\n  1  1     9.99970913E-01   # O_{11}\n  1  2     7.62549881E-03   # O_{12}\n  2  1    -7.62549881E-03   # O_{21}\n  2  2     9.99970913E-01   # O_{22}\nBlock STAUMIX   # stau mixing matrix\n  1  1     5.97260058E-01   # O_{11}\n  1  2     8.02047670E-01   # O_{12}\n  2  1    -8.02047670E-01   # O_{21}\n  2  2     5.97260058E-01   # O_{22}\nBlock NMIX   # neutralino mixing matrix\n  1  1     1.02890544E-02   #\n  1  2    -9.93297398E-01   #\n  1  3     1.09105095E-01   #\n  1  4    -3.67495306E-02   #\n  2  1    -9.96177256E-01   #\n  2  2    -1.99755784E-02   #\n  2  3    -7.35215694E-02   #\n  2  4     4.27322201E-02   #\n  3  1     2.25971118E-02   #\n  3  2    -5.08868955E-02   #\n  3  3    -7.03913569E-01   #\n  3  4    -7.08099306E-01   #\n  4  1     8.37496892E-02   #\n  4  2    -1.01842113E-01   #\n  4  3    -6.97993875E-01   #\n  4  4     7.03859687E-01   #\nBlock UMIX   # chargino U mixing matrix\n  1  1    -9.88591433E-01   # U_{11}\n  1  2     1.50621936E-01   # U_{12}\n  2  1    -1.50621936E-01   # U_{21}\n  2  2    -9.88591433E-01   # U_{22}\nBlock VMIX   # chargino V mixing matrix\n  1  1    -9.98679578E-01   # V_{11}\n  1  2     5.13723604E-02   # V_{12}\n  2  1    -5.13723604E-02   # V_{21}\n  2  2    -9.98679578E-01   # V_{22}\nBlock GAUGE Q=  1.13725037E+03   #\n     1     3.57492119E-01   # g`\n     2     6.52496159E-01   # g_2\n     3     1.22099471E+00   # g_3\nBlock YU Q=  1.13725037E+03   #\n  3  3     8.78648043E-01   # y_t\nBlock YD Q=  1.13725037E+03   #\n  3  3     6.93556666E-02   # y_b\nBlock YE Q=  1.13725037E+03   #\n  3  3     5.13891652E-02   # y_tau\nBlock HMIX Q=  1.13725037E+03   # Higgs mixing parameters\n     1     7.33976440E+02   # mu(Q)\n     2     5.00000000E+00   # tan(beta)(M_GUT)\n     3     2.51144409E+02   # Higgs vev at Q\n     4     2.84456425E+06   # m_A^2(Q)\nBlock MSOFT Q=  1.13725037E+03   # DRbar SUSY breaking parameters\n     1     3.23079498E+02   # M_1(Q)\n     2     9.78689346E+01   # M_2(Q)\n     3    -7.54845886E+02   # M_3(Q)\n    31     1.48517932E+03   # MeL(Q)\n    32     1.48517932E+03   # MmuL(Q)\n    33     1.48340161E+03   # MtauL(Q)\n    34     1.48875891E+03   # MeR(Q)\n    35     1.48875891E+03   # MmuR(Q)\n    36     1.48529724E+03   # MtauR(Q)\n    41     1.61164856E+03   # MqL1(Q)\n    42     1.61164856E+03   # MqL2(Q)\n    43     1.33004492E+03   # MqL3(Q)\n    44     1.61942517E+03   # MuR(Q)\n    45     1.61942517E+03   # McR(Q)\n    46     9.72402039E+02   # MtR(Q)\n    47     1.62276147E+03   # MdR(Q)\n    48     1.62276147E+03   # MsR(Q)\n    49     1.62246484E+03   # MbR(Q)\nBlock AU Q=  1.13725037E+03   #\n  1  1     6.08556396E+02   # A_u\n  2  2     6.08556396E+02   # A_c\n  3  3     6.08556396E+02   # A_t\nBlock AD Q=  1.13725037E+03   #\n  1  1     1.45460706E+03   # A_d\n  2  2     1.45460706E+03   # A_s\n  3  3     1.45460706E+03   # A_b\nBlock AE Q=  1.13725037E+03   #\n  1  1     3.71930389E+02   # A_e\n  2  2     3.71930389E+02   # A_mu\n  3  3     3.71930389E+02   # A_tau\n#\n#\n#\n#                             =================\n#                             |The decay table|\n#                             =================\n#\n#         PDG            Width\nDECAY   1000024     1.97326979e-15 # chargino decay\n#\n#\n'),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(1.0),
    filterEfficiency = cms.untracked.double(-1),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(100),
    maxEventsToPrint = cms.untracked.int32(0),
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4/geant4_AMSB_chargino_100GeV_ctau10cm.slha'),
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
