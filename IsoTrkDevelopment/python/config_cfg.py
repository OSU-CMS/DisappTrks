from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################## New channel for particle gun ########################
if False:
  add_channels  (process,   [NoCuts],         histSetsIsoTrkChargino,  weightsPileupOnly,  [],  collMap,  variableProducers + genMatchedTrackProducer, branchSets = branchSetIsolatedTracksMini)
  add_channels  (process,   [IsoTrkSkim],         histSetsIsoTrkChargino,  weightsPileupOnly,  [],  collMap,  variableProducers + genMatchedTrackProducer, branchSets = branchSetIsolatedTracksMini)
  add_channels  (process,   [CharginoMatchedSkim], histSetsIsoTrkChargino,  weightsPileupOnly,  [],  collMap,  variableProducers + genMatchedTrackProducer, branchSets = branchSetIsolatedTracksMini)
########################################################################

if hasattr(process, 'EventJetVarProducer'):
	process.EventJetVarProducer.triggerNames = triggerNamesInclusive
else:
    print
    print 'You haven\'t added any channels. There\'s nothing to do!'
    print
    sys.exit(0)
