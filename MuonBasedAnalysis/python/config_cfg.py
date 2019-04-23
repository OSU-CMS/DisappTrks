from DisappTrks.StandardAnalysis.protoConfig_cfg import *

################################################################################
# SingleMuon channels
################################################################################
#  add_channels  (process,  [muonBasedAnalysis.isoTrkSelection],     histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [muonBasedAnalysis.candTrkSelection],    histSets,  weights,  [],  collMap,  variableProducers,  False)
#  add_channels  (process,  [muonBasedAnalysis.disTrkSelection],     histSets,  weights,  [],  collMap,  variableProducers,  False)
################################################################################

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
    
