import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *


generator = cms.EDFilter("Pythia8HadronizerFilter", 
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            UseTauolaPolarization = cms.bool(True),
            InputCards = cms.PSet(
                mdtau = cms.int32(0),
                pjak2 = cms.int32(0),
                pjak1 = cms.int32(0)
            )
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        processParameters = cms.vstring(
            'Main:timesAllowErrors    = 10000',   
            'ParticleDecays:limitTau0 = on',
            'ParticleDecays:tauMax = 10',   
            'Tune:ee 3',  
            'Tune:pp 5'
            ),
        parameterSets = cms.vstring('processParameters'), 
    ),
# The following parameters are required by Exotica_HSCP_SIM_cfi:  
    slhaFile = cms.untracked.string('DisappTrks/SignalMC/data/AMSB_chargino_500GeV_Isajet780.slha'),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False), 
    hscpFlavor = cms.untracked.string('stau'),          
    massPoint = cms.untracked.int32(500),          
    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/geant4_AMSB_chargino_500GeV_ctau100cm.slha')
)  


ProducerSourceSequence = cms.Sequence(generator)



