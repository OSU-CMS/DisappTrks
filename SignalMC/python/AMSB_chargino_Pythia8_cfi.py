import FWCore.ParameterSet.Config as cms

## #from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
## process.generator = cms.EDFilter("Pythia8GeneratorFilter", 
##     pythiaHepMCVerbosity = cms.untracked.bool(False),
##     maxEventsToPrint = cms.untracked.int32(1),
##     pythiaPylistVerbosity = cms.untracked.int32(3),
##     filterEfficiency = cms.untracked.double(1.0),
##     comEnergy = cms.double(8000.0),
##     SLHAFileForPythia8 = cms.string('DisappTrks/SignalMC/data/AMSB_chargino_MASSPOINTGeV_Isajet780.slha'),  
##     PythiaParameters = cms.PSet(
##     processParameters = cms.vstring('Tune:pp  = 5',
##                                     'SUSY:all = off',
##                                     'SUSY:qqbar2chi+-chi0 = on',
##                                     'SUSY:qqbar2chi+chi-  = on', 
##                                     '1000024:tau0 = 1000.0'),
##     parameterSets = cms.vstring('processParameters')
##     ),
## )



process.generator = cms.EDFilter("Pythia8GeneratorFilter",
                                 pythiaPylistVerbosity = cms.untracked.int32(0),
                                 filterEfficiency = cms.untracked.double(-1),
                                 pythiaHepMCVerbosity = cms.untracked.bool(False),
                                 SLHAFileForPythia8 = cms.string('Configuration/Generator/data/HSCP_stopToBottom_1000_1000.0mm_SLHA.spc'),
                                 comEnergy = cms.double(8000.0),
                                 crossSection = cms.untracked.double(-1),
                                 maxEventsToPrint = cms.untracked.int32(0),
                                 PythiaParameters = cms.PSet(
    processParameters = cms.vstring('Tune:pp  = 5',
                                    'SUSY:all = off',
                                    'SUSY:gg2squarkantisquark  = on',
                                    'SUSY:qqbar2squarkantisquark= on',
                                    'RHadrons:allow  = on',
                                    'RHadrons:allowDecay = on',
                                    'RHadrons:setMasses = on',
                                    '1000006:tau0 = 1000.0'),
    parameterSets = cms.vstring('processParameters')
    ),
                                 hscpFlavor = cms.untracked.string('stop'),
                                 massPoint = cms.untracked.int32(1000),
                                 particleFile = cms.untracked.string('Configuration/Generator/data/particles_stop_1000_GeV.txt'),
                                 slhaFile = cms.untracked.string('Configuration/Generator/data/HSCP_stopToBottom_1000_1000.0mm_SLHA.spc'),
                                 processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/stophadronProcessList.txt'),
                                 pdtFile = cms.FileInPath('Configuration/Generator/data/hscppythiapdtstop1000.tbl'),
                                 useregge = cms.bool(False)
                                 )




