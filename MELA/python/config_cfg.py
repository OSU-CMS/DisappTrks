from DisappTrks.StandardAnalysis.protoConfig_cfg import *

# Central value channels
if True:
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],     histSets, weights, [], collMap, variableProducers + dedxHitInfoVarProducer, branchSets = branchSetsMELA)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],     histSets, weights, [], collMap, variableProducers + dedxHitInfoVarProducer, branchSets = branchSetsMELA)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus], histSets, weights, [], collMap, variableProducers + dedxHitInfoVarProducer, branchSets = branchSetsMELA)

if hasattr(process, 'EventJetVarProducer'):
	process.EventJetVarProducer.triggerNames = triggerNamesInclusive
else:
    print
    print 'You haven\'t added any channels. There\'s nothing to do!'
    print
    sys.exit(0)
    
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    process.fullPatMetSequenceModifiedMETPath = cms.Path(process.fullPatMetSequenceModifiedMET)
    process.schedule.insert(0, process.fullPatMetSequenceModifiedMETPath)
