import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *

generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(8000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'IMSS(1)     = 11    ! Spectrum from external SLHA file',
            'MSEL        = 0     ! full user control',
            'MSUB(226)   = 1     ! to double chargino',
            'MSUB(229)   = 1     ! to neutralino + chargino',  
            ),
        parameterSets = cms.vstring('pythiaUESettings', 'processParameters', 'SLHAParameters'),
        SLHAParameters = cms.vstring('SLHAFILE = DisappTrks/SignalMC/data/AMSB_chargino_MASSPOINTGeV_Isajet780.slha'),
    ),
)  



