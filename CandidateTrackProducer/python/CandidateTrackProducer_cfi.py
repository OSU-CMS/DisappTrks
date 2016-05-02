import FWCore.ParameterSet.Config as cms

# The following are needed for the calculation of associated calorimeter energy
from Configuration.StandardSequences.GeometryRecoDB_cff import *
from Configuration.StandardSequences.MagneticField_38T_cff import *

candidateTrackProducer = cms.EDProducer ("CandidateTrackProducer",
  tracks             =  cms.InputTag  ("generalTracks",                  ""),
  electrons          =  cms.InputTag  ("slimmedElectrons",               ""),
  muons              =  cms.InputTag  ("slimmedMuons",                   ""),
  taus               =  cms.InputTag  ("slimmedTaus",                    ""),
  beamspot           =  cms.InputTag  ("offlineBeamSpot",                ""),
  vertices           =  cms.InputTag  ("offlineSlimmedPrimaryVertices",  ""),
  conversions        =  cms.InputTag  ("reducedEgamma",                  "reducedConversions"),
  rhoTag             =  cms.InputTag  ("fixedGridRhoFastjetAll"),
  rhoCaloTag         =  cms.InputTag  ("fixedGridRhoFastjetAllCalo"),
  rhoCentralCaloTag  =  cms.InputTag  ("fixedGridRhoFastjetCentralCalo"),
  EBRecHits          =  cms.InputTag  ("reducedEcalRecHitsEB"),
  EERecHits          =  cms.InputTag  ("reducedEcalRecHitsEE"),
  HBHERecHits        =  cms.InputTag  ("reducedHcalRecHits", "hbhereco"), 
  candMinPt          =  cms.double(10),
)
