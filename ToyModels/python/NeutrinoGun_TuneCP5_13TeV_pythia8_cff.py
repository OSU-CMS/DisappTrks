import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer('FlatRandomPtGunProducer',
  PGunParameters = cms.PSet(
    PartID = cms.vint32(12),  ## eminus
    MinPhi = cms.double(-3.14159265359), ## in radians
    MaxPhi = cms.double(3.14159265359),
    MinEta = cms.double(-3),
    MaxEta = cms.double(3),
    MinPt = cms.double(2),
    MaxPt = cms.double(20),
  ),
  Verbosity = cms.untracked.int32(0),
  psethack = cms.string('single neutrino 2<Pt<20 -3<Eta<3'),
  AddAntiParticle = cms.bool(False),  ## only eminus
)
