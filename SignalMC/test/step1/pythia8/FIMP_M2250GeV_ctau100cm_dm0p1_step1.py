# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: DisappTrks/SignalMC/python/pythia8/Hadronizer_TuneCP5_13TeV_generic_LHE_pythia8_cff.py --filein file:unweighted_events_M700GeV_ctau100cm_dm0p1.lhe --fileout file:FIMP_M700GeV_ctau100cm_dm0p1_step1.root --mc --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,SimG4Core/Application/customiseSequentialSim.customiseSequentialSim --datatier LHE-GEN-SIM --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --geometry DB:Extended --era Run2_2017 --python_filename step1/pythia8/FIMP_M700GeV_ctau100cm_dm0p1_step1.py --no_exec -n 1000
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
process.source = cms.Source("LHESource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring('file:unweighted_events_M2250GeV_ctau100cm_dm0p1.lhe'),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop LHEXMLStringProduct_*_*_*')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('DisappTrks/SignalMC/python/pythia8/Hadronizer_TuneCP5_13TeV_generic_LHE_pythia8_cff.py nevts:10'),
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
        dataTier = cms.untracked.string('LHE-GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('file:FIMP_M2250GeV_ctau100cm_dm0p1_step1.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '93X_mc2017_realistic_v3', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14',
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
            'TimeShower:alphaSvalue=0.118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2',
            'Main:timesAllowErrors = 10000',
            'Check:epTolErr = 0.01',
            'Beams:setProductionScalesFromLHEF = off',
            'SLHA:keepSM = on',
            'SLHA:minMassSM = 1000.',
            'ParticleDecays:limitTau0 = on',
            'ParticleDecays:tau0Max = 10000',
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    SLHATableForPythia8 = cms.string('/n######################################################################/n## PARAM_CARD AUTOMATICALY GENERATED BY MG5 FOLLOWING UFO MODEL   ####/n######################################################################/n##                                                                  ##/n##  Width set on Auto will be computed following the information    ##/n##        present in the decay.py files of the model.               ##/n##        See  arXiv:1402.1178 for more details.                    ##/n##                                                                  ##/n######################################################################/n###################################/n## INFORMATION FOR CKMBLOCK/n###################################/nBlock ckmblock /n    1 2.277360e-01 # cabi /n###################################/n## INFORMATION FOR FRBLOCK/n###################################/nBlock frblock /n    1 1.000000e+02 # QS /n    2 2.000000e-05 # yHEeR /n    3 2.000000e-05 # yHEmuR /n    4 2.000000e-05 # yHEtaR /n    5 2.000000e-02 # lams0h /n    6 1.000000e-01 # lams0 /n###################################/n## INFORMATION FOR MASS/n###################################/nBlock mass /n    1 5.040000e-03 # MD /n    2 2.550000e-03 # MU /n    3 1.010000e-01 # MS /n    4 1.270000e+00 # MC /n    5 4.700000e+00 # MB /n    6 1.720000e+02 # MT /n   11 5.110000e-04 # Me /n   13 1.056600e-01 # MMU /n   15 1.777000e+00 # MTA /n   23 9.118760e+01 # MZ /n   25 1.250000e+02 # mh /n  1000022 2.250000e+03 # ms0 /n  1000011 2.250100e+03 # mHE /n## Dependent parameters, given by model restrictions./n## Those values should be edited following the /n## analytical expression. MG5 ignores those values /n## but they are important for interfacing the output of MG5/n## to external program such as Pythia./n  12 0.000000e+00 # ve : 0.0 /n  14 0.000000e+00 # vm : 0.0 /n  16 0.000000e+00 # vt : 0.0 /n  21 0.000000e+00 # g : 0.0 /n  22 0.000000e+00 # a : 0.0 /n  24 7.982436e+01 # w+ : cmath.sqrt(MZ__exp__2/2. + cmath.sqrt(MZ__exp__4/4. - (aEW*cmath.pi*MZ__exp__2)/(Gf*sqrt__2))) /n -1000011 2.250100e+03 # x1- : mHE /n###################################/n## INFORMATION FOR SMINPUTS/n###################################/nBlock sminputs /n    1 1.279000e+02 # aEWM1 /n    2 1.166370e-05 # Gf /n    3 1.184000e-01 # aS /n###################################/n## INFORMATION FOR YUKAWA/n###################################/nBlock yukawa /n    1 5.040000e-03 # ymdo /n    2 2.550000e-03 # ymup /n    3 1.010000e-01 # yms /n    4 1.270000e+00 # ymc /n    5 4.700000e+00 # ymb /n    6 1.720000e+02 # ymt /n   11 5.110000e-04 # yme /n   13 1.056600e-01 # ymm /n   15 1.777000e+00 # ymtau /n###################################/n## INFORMATION FOR DECAY/n###################################/nDECAY   6 1.508336e+00 # WT /nDECAY  23 2.495200e+00 # WZ /nDECAY  24 2.085000e+00 # WW /nDECAY  25 5.000000e-03 # wh /nDECAY 1000022 0.000000e+00 # ws0 /nDECAY 1000011 2.000000e-16 # wHE /n## Dependent parameters, given by model restrictions./n## Those values should be edited following the /n## analytical expression. MG5 ignores those values /n## but they are important for interfacing the output of MG5/n## to external program such as Pythia./nDECAY  1 0.000000e+00 # d : 0.0 /nDECAY  2 0.000000e+00 # u : 0.0 /nDECAY  3 0.000000e+00 # s : 0.0 /nDECAY  4 0.000000e+00 # c : 0.0 /nDECAY  5 0.000000e+00 # b : 0.0 /nDECAY  11 0.000000e+00 # e- : 0.0 /nDECAY  12 0.000000e+00 # ve : 0.0 /nDECAY  13 0.000000e+00 # mu- : 0.0 /nDECAY  14 0.000000e+00 # vm : 0.0 /nDECAY  15 0.000000e+00 # ta- : 0.0 /nDECAY  16 0.000000e+00 # vt : 0.0 /nDECAY  21 0.000000e+00 # g : 0.0 /nDECAY  22 0.000000e+00 # a : 0.0 /nDECAY  -1000011 2.000000e-16 # x1- : wHE /n#===========================================================/n# QUANTUM NUMBERS OF NEW STATE(S) (NON SM PDG CODE)/n#===========================================================/nBlock QNUMBERS 1000022  # n1 /n        1 0  # 3 times electric charge/n        2 1  # number of spin states (2S+1)/n        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)/n        4 0  # Particle/Antiparticle distinction (0=own anti)/nBlock QNUMBERS 1000011  # n1 /n        1 3  # 3 times electric charge/n        2 2  # number of spin states (2S+1)/n        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)/n        4 1  # Particle/Antiparticle distinction (0=own anti)/nBlock QNUMBERS -1000011  # n1 /n        1 -3  # 3 times electric charge/n        2 2  # number of spin states (2S+1)/n        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)/n        4 1  # Particle/Antiparticle distinction (0=own anti)'),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
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
