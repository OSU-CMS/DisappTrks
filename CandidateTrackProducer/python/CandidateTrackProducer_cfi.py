import FWCore.ParameterSet.Config as cms

# The following are needed for the calculation of associated calorimeter energy
from Configuration.StandardSequences.GeometryRecoDB_cff import *
from Configuration.StandardSequences.MagneticField_38T_cff import *
from TrackingTools.TrackAssociator.DetIdAssociatorESProducer_cff import *
from TrackingTools.TrackAssociator.default_cfi import *
CandTrackAssociatorParameters = TrackAssociatorParameterBlock.TrackAssociatorParameters.clone()
CandTrackAssociatorParameters.useHO = cms.bool(False)
CandTrackAssociatorParameters.CSCSegmentCollectionLabel     = cms.InputTag("cscSegments")
CandTrackAssociatorParameters.DTRecSegment4DCollectionLabel = cms.InputTag("dt4DSegments")
CandTrackAssociatorParameters.EERecHitCollectionLabel       = cms.InputTag("reducedEcalRecHitsEE")
CandTrackAssociatorParameters.EBRecHitCollectionLabel       = cms.InputTag("reducedEcalRecHitsEB")
CandTrackAssociatorParameters.HBHERecHitCollectionLabel     = cms.InputTag("reducedHcalRecHits", "hbhereco")
CandTrackAssociatorParameters.HORecHitCollectionLabel       = cms.InputTag("reducedHcalRecHits", "horeco")

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
  candMinPt = cms.double(10),
  TrackAssociatorParameters = CandTrackAssociatorParameters,
)
