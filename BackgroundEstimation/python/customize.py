import FWCore.ParameterSet.Config as cms

def addMoreCaloTowers (process):
  process.interestingTrackEcalDetIds.MinTrackPt = cms.double (20.0)
  return process

def addMoreElectronSeeds (process):
  process.trackerDrivenElectronSeeds.MaxPt = cms.double (20.0)
  return process
