from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################## New channel for particle gun ########################
#add_channels  (process,   [MuonGunSkim],         histSetsParticleGun,  weightsPileupOnly,  [],  collMap,  variableProducers + particleGunMuonVarProducer, branchSets = branchSetsParticleGun)
#add_channels  (process,   [MuonGunSkimPt45to55], histSetsParticleGun,  weightsPileupOnly,  [],  collMap,  variableProducers + particleGunMuonVarProducer, branchSets = branchSetsParticleGun)
########################################################################

if hasattr(process, 'EventJetVarProducer'):
	process.EventJetVarProducer.triggerNames = triggerNamesInclusive
else:
    print
    print 'You haven\'t added any channels. There\'s nothing to do!'
    print
    sys.exit(0)
