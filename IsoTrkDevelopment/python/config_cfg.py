from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################## New channel for particle gun ########################
#add_channels  (process,   [NoCuts],         histSetsIsoTrkChargino,  weightsPileupOnly,  [],  collMap,  variableProducers + genMatchedTrackProducer)
#add_channels  (process,   [CharginoMatchedSkim], histSetsIsoTrkChargino,  weightsPileupOnly,  [],  collMap,  variableProducers + genMatchedTrackProducer)
########################################################################

if hasattr(process, 'EventJetVarProducer'):
	process.EventJetVarProducer.triggerNames = triggerNamesInclusive
else:
    print
    print 'You haven\'t added any channels. There\'s nothing to do!'
    print
    sys.exit(0)
