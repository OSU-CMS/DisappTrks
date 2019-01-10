# https://raw.githubusercontent.com/cms-sw/genproductions/master/python/EightTeV/DYToEE_M_20_Tune4C_8TeV_pythia8_cff.py

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(0.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'Main:timesAllowErrors = 10000',
            'WeakSingleBoson:ffbar2gmZ = on', # turn on Z production
            'ParticleDecays:limitTau0 = on',
            'ParticleDecays:tau0Max = 10.',

            'PartonLevel:MI = on',
            'SecondHard:generate = off',
            'SecondHard:TwoJets = off',
            'PhaseSpace:sameForSecond = off', 
       
            'PhaseSpace:mHatMin = 20',
            '23:onMode = off',  #turn off all Z decays
            '23:onIfAny = 13',   # turn ON Z->mumu
       ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters')
    ),
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/DYToEE_M_20_Tune4C_8TeV_pythia8_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA8 Z/gamma* to ee, M(e+e-) > 20 GeV at sqrt(s) = 8TeV, Tune 4c')
)
