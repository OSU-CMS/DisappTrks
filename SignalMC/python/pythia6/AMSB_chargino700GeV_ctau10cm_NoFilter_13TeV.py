import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(3),
    filterEfficiency = cms.untracked.double(1.0),
#    comEnergy = cms.double(8000.0),
    comEnergy = cms.double(13000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'IMSS(1)     = 11    ! Spectrum from external SLHA file',
            'IMSS(21)    = 33    ! LUN number for SLHA File (must be 33) ',
            'IMSS(22)    = 33    ! Read-in SLHA decay table ',
            'MSEL        = 0     ! General SUSY',
            'MSUB(226)   = 1     ! to double chargino',
            'MSUB(229)   = 1     ! to neutralino + chargino',
            'MDCY(312,1) = 0     ! set the chargino stable.',
            ),
        parameterSets = cms.vstring('pythiaUESettings', 'processParameters', 'SLHAParameters'),
        SLHAParameters = cms.vstring('SLHAFILE = DisappTrks/SignalMC/data/AMSB_chargino_700GeV_Isajet780.slha'),
    ),
    slhaFile = cms.untracked.string('DisappTrks/SignalMC/data/AMSB_chargino_700GeV_Isajet780.slha'),
# The following parameters are required by Exotica_HSCP_SIM_cfi:
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(700),
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4/geant4_AMSB_chargino_700GeV_ctau10cm.slha')
)
