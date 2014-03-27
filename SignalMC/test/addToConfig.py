

# The configuration settings below are needed for simulating long-lived charginos:  
from SimG4Core.CustomPhysics.Exotica_HSCP_SIM_cfi import customise  
process = customise(process)    

process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInTracker = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInCalo    = cms.untracked.bool(True)
process.g4SimHits.StackingAction.SavePrimaryDecayProductsAndConversionsInMuon    = cms.untracked.bool(True)

process.g4SimHits.SteppingAction.MaxTrackTimes = cms.vdouble(2000.0, 500.0, 500.0)
process.g4SimHits.StackingAction.MaxTrackTimes = cms.vdouble(2000.0, 500.0, 500.0)
process.common_maximum_time.MaxTrackTimes      = cms.vdouble(2000.0, 500.0, 500.0)

## Dump python config if wished
outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()




