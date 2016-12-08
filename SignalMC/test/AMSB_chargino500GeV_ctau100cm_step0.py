# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: DisappTrks/SignalMC/python/AMSB_chargino500GeV_ctau100cm_NoFilter_13TeV_pythia8.py --fileout file:AMSB_chargino500GeV_ctau100cm_step0.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --conditions MCRUN2_71_V1::All --beamspot NominalCollision2015 --step GEN --magField 38T_PostLS1 --python_filename AMSB_chargino500GeV_ctau100cm_step0.py --no_exec -n 100000
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedNominalCollision2015_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/AMSB_chargino500GeV_ctau100cm_NoFilter_13TeV_pythia8.py nevts:100000'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:AMSB_chargino500GeV_ctau100cm_weakFSR_step0.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN')
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

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    SLHATableForPythia8 = cms.string('#  ISAJET SUSY parameters in SUSY Les Houches Accord 2 format\n#  Created by ISALHA 2.0 Last revision: C. Balazs 21 Apr 2009\nBlock SPINFO   # Program information\n     1   ISASUGRA from ISAJET          # Spectrum Calculator\n     2   7.80   29-OCT-2009 12:50:36   # Version number\nBlock MODSEL   # Model selection\n     1     3   # Minimal anomaly mediated (AMSB) model             \nBlock SMINPUTS   # Standard Model inputs\n     1     1.27836266E+02   # alpha_em^(-1)\n     2     1.16570000E-05   # G_Fermi\n     3     1.17200002E-01   # alpha_s(M_Z)\n     4     9.11699982E+01   # m_{Z}(pole)\n     5     4.19999981E+00   # m_{b}(m_{b})\n     6     1.73070007E+02   # m_{top}(pole)\n     7     1.77699995E+00   # m_{tau}(pole)\nBlock MINPAR   # SUSY breaking input parameters\n     1     1.50000000E+03   # m_0\n     2     1.74430000E+05   # m_{3/2}\n     3     5.00000000E+00   # tan(beta)\n     4     1.00000000E+00   # sign(mu)\nBlock EXTPAR   # Non-universal SUSY breaking parameters\n     0     1.12737372E+16   # Input scale\nBlock MASS   # Scalar and gaugino mass spectrum\n#  PDG code   mass                 particle\n        24     8.04229965E+01   #  W^+\n        25     1.15511902E+02   #  h^0            \n        35     3.18671997E+03   #  H^0            \n        36     3.16565356E+03   #  A^0            \n        37     3.17845288E+03   #  H^+            \n   1000001     3.56121729E+03   #  dnl            \n   1000002     3.56034009E+03   #  upl            \n   1000003     3.56121729E+03   #  stl            \n   1000004     3.56034033E+03   #  chl            \n   1000005     3.10211743E+03   #  b1             \n   1000006     2.56294897E+03   #  t1             \n   1000011     1.32959814E+03   #  el-            \n   1000012     1.32121753E+03   #  nuel           \n   1000013     1.32959814E+03   #  mul-           \n   1000014     1.32121753E+03   #  numl           \n   1000015     1.28115686E+03   #  tau1           \n   1000016     1.31567761E+03   #  nutl           \n   1000021     3.47622827E+03   #  glss           \n   1000022     4.99829254E+02   #  z1ss           \n   1000023     1.60168201E+03   #  z2ss           \n   1000024     5.00002502E+02   #  w1ss           \n   1000025    -2.81133667E+03   #  z3ss           \n   1000035     2.81305249E+03   #  z4ss           \n   1000037     2.81642407E+03   #  w2ss           \n   2000001     3.61366235E+03   #  dnr            \n   2000002     3.58297388E+03   #  upr            \n   2000003     3.61366235E+03   #  str            \n   2000004     3.58297412E+03   #  chr            \n   2000005     3.58649536E+03   #  b2             \n   2000006     3.13307568E+03   #  t2             \n   2000011     1.28796350E+03   #  er-            \n   2000013     1.28796350E+03   #  mur-           \n   2000015     1.32356653E+03   #  tau2           \nBlock ALPHA   # Effective Higgs mixing parameter\n         -1.97843567E-01   # alpha\nBlock STOPMIX   # stop mixing matrix\n  1  1     1.02065332E-01   # O_{11}\n  1  2    -9.94777679E-01   # O_{12}\n  2  1     9.94777679E-01   # O_{21}\n  2  2     1.02065332E-01   # O_{22}\nBlock SBOTMIX   # sbottom mixing matrix\n  1  1     9.99975383E-01   # O_{11}\n  1  2     7.02077523E-03   # O_{12}\n  2  1    -7.02077523E-03   # O_{21}\n  2  2     9.99975383E-01   # O_{22}\nBlock STAUMIX   # stau mixing matrix\n  1  1     2.05478176E-01   # O_{11}\n  1  2     9.78661716E-01   # O_{12}\n  2  1    -9.78661716E-01   # O_{21}\n  2  2     2.05478176E-01   # O_{22}\nBlock NMIX   # neutralino mixing matrix\n  1  1    -1.00043009E-03   #\n  1  2     9.99558985E-01   #\n  1  3    -2.82598697E-02   #\n  1  4     9.08957701E-03   #\n  2  1     9.99603391E-01   #\n  2  2     1.80333573E-03   #\n  2  3     2.33832896E-02   #\n  2  4    -1.55895352E-02   #\n  3  1     5.53086400E-03   #\n  3  2    -1.35487262E-02   #\n  3  3    -7.06874847E-01   #\n  3  4    -7.07187414E-01   #\n  4  1     2.75947675E-02   #\n  4  2    -2.63707135E-02   #\n  4  3    -7.06387043E-01   #\n  4  4     7.06796229E-01   #\nBlock UMIX   # chargino U mixing matrix\n  1  1    -9.99171793E-01   # U_{11}\n  1  2     4.06901948E-02   # U_{12}\n  2  1    -4.06901948E-02   # U_{21}\n  2  2    -9.99171793E-01   # U_{22}\nBlock VMIX   # chargino V mixing matrix\n  1  1    -9.99882162E-01   # V_{11}\n  1  2     1.53514510E-02   # V_{12}\n  2  1    -1.53514510E-02   # V_{21}\n  2  2    -9.99882162E-01   # V_{22}\nBlock GAUGE Q=  2.70318530E+03   #\n     1     3.57524961E-01   # g`\n     2     6.52378559E-01   # g_2\n     3     1.21927977E+00   # g_3\nBlock YU Q=  2.70318530E+03   #\n  3  3     8.46211851E-01   # y_t\nBlock YD Q=  2.70318530E+03   #\n  3  3     6.63219020E-02   # y_b\nBlock YE Q=  2.70318530E+03   #\n  3  3     5.15569262E-02   # y_tau\nBlock HMIX Q=  2.70318530E+03   # Higgs mixing parameters\n     1     2.81156128E+03   # mu(Q)\n     2     5.00000000E+00   # tan(beta)(M_GUT)\n     3     2.51505371E+02   # Higgs vev at Q\n     4     1.00213620E+07   # m_A^2(Q)\nBlock MSOFT Q=  2.70318530E+03   # DRbar SUSY breaking parameters\n     1     1.62324744E+03   # M_1(Q)          \n     2     4.73120422E+02   # M_2(Q)          \n     3    -3.27709692E+03   # M_3(Q)          \n    31     1.32059900E+03   # MeL(Q)          \n    32     1.32059900E+03   # MmuL(Q)         \n    33     1.31518896E+03   # MtauL(Q)        \n    34     1.28408386E+03   # MeR(Q)          \n    35     1.28408386E+03   # MmuR(Q)         \n    36     1.27127039E+03   # MtauR(Q)        \n    41     3.39131226E+03   # MqL1(Q)         \n    42     3.39131226E+03   # MqL2(Q)         \n    43     2.96472168E+03   # MqL3(Q)         \n    44     3.41352490E+03   # MuR(Q)          \n    45     3.41352490E+03   # McR(Q)          \n    46     2.46472070E+03   # MtR(Q)          \n    47     3.44374805E+03   # MdR(Q)          \n    48     3.44374805E+03   # MsR(Q)          \n    49     3.45781030E+03   # MbR(Q)          \nBlock AU Q=  2.70318530E+03   #\n  1  1     2.80809619E+03   # A_u\n  2  2     2.80809619E+03   # A_c\n  3  3     2.80809619E+03   # A_t\nBlock AD Q=  2.70318530E+03   #\n  1  1     6.67355664E+03   # A_d\n  2  2     6.67355664E+03   # A_s\n  3  3     6.67355664E+03   # A_b\nBlock AE Q=  2.70318530E+03   #\n  1  1     1.82787415E+03   # A_e\n  2  2     1.82787415E+03   # A_mu\n  3  3     1.82787415E+03   # A_tau\n'),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettings = cms.vstring('Main:timesAllowErrors = 10000',
            'Check:epTolErr = 0.01',
            'Beams:setProductionScalesFromLHEF = off',
            'SLHA:keepSM = on',
            'SLHA:minMassSM = 1000.',
            'ParticleDecays:limitTau0 = on',
            'ParticleDecays:tau0Max = 10',
            'ParticleDecays:allowPhotonRadiation = on'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14',
            'Tune:ee 7',
            'MultipartonInteractions:pT0Ref=2.4024',
            'MultipartonInteractions:ecmPow=0.25208',
            'MultipartonInteractions:expPow=1.6'),
        processParameters = cms.vstring('SUSY:all = off',
            'SUSY:qqbar2chi+-chi0 = on',
            'SUSY:qqbar2chi+chi- = on',
            'SpaceShower:weakShower = on', # weak ISR
            'TimeShower:weakShower = on',  # weak FSR
            '1000022:mayDecay = false',
            '1000024:mayDecay = false'),
        parameterSets = cms.vstring('pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters')
    )
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
        getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# End of customisation functions
