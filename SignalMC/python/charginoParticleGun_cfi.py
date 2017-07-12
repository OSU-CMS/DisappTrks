# Use as model:
# https://cmssdt.cern.ch/SDT/lxr/source/Configuration/Generator/python/SingleMuPt100_cfi.py?v=CMSSW_5_3_12

import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("FlatRandomPtGunProducer",
    PGunParameters = cms.PSet(
        PartID = cms.vint32(1000024),
        MinPt = cms.double(99.99),
        MaxPt = cms.double(100.01),
        MinEta = cms.double(-2.5),
        MaxEta = cms.double(2.5),
        MinPhi = cms.double(-3.14159265359), ## in radians
        MaxPhi = cms.double(3.14159265359)
    ),
    Verbosity = cms.untracked.int32(0), ## set to 1 (or greater)  for printouts
    psethack = cms.string('chargino pt 100'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
)
