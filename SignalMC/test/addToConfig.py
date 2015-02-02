

# The configuration settings below are needed for simulating long-lived charginos:  
from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise  
process = customise(process)    

process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInTracker = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInCalo    = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInMuon    = cms.untracked.bool(True)

process.g4SimHits.SteppingAction.MaxTrackTimes = cms.vdouble(2000.0)
process.g4SimHits.StackingAction.MaxTrackTimes = cms.vdouble(2000.0)
process.common_maximum_time.MaxTrackTimes      = cms.vdouble(2000.0)

process.g4SimHits.Physics.GflashEcal = cms.bool(False)
process.g4SimHits.Physics.GflashHcal = cms.bool(False)
process.g4SimHits.Physics.ElectronStepLimit = cms.bool(False)
process.g4SimHits.Physics.ElectronRangeTest = cms.bool(False)
process.g4SimHits.Physics.PositronStepLimit = cms.bool(False)
process.g4SimHits.Physics.MinStepLimit = cms.double(1.0)
process.g4SimHits.Physics.RusRoElectronEnergyLimit = cms.double(0.0)
process.g4SimHits.Physics.FlagFluo = cms.bool(False)

process.g4SimHits.StackingAction.KillGamma = cms.bool(True)
process.g4SimHits.StackingAction.GammaThreshold = cms.double(0.0001)




