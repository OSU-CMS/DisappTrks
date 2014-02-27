import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUESettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(3),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(8000.0),
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
        SLHAParameters = cms.vstring('SLHAFILE = Configuration/Generator/data/amsb_LL01_mGravXXX.slha'),
    ),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(150), 
    slhaFile = cms.untracked.string('Configuration/Generator/data/amsb_LL01_mGravXXX.slha'),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    particleFile = cms.untracked.string('Configuration/Generator/data/geant4_chargino_amsbLL01_mGravXXX_YYYns.slha'),
    pdtFile = cms.FileInPath('Configuration/Generator/data/charginopdt_file.tbl')
)  



