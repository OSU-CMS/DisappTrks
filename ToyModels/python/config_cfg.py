from DisappTrks.StandardAnalysis.protoConfig_fakedecay_cfg import *

################## New channel for particle gun ########################
#add_channels  (process,   [MuonGunSkim],          histSetsParticleGun,  weightsPileupOnly,  [],  collMap,  variableProducers + muonPGunProducer, branchSets = branchSetsParticleGun)
#add_channels  (process,   [MuonGunSkim_Pt45to55], histSetsParticleGun,  weightsPileupOnly,  [],  collMap,  variableProducers + muonPGunProducer, branchSets = branchSetsParticleGun)
########################################################################

process.EventJetVarProducer.triggerNames = triggerNamesInclusive
