from DisappTrks.StandardAnalysis.protoConfig_cfg import *

# Central value channels
if False:
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],     histSets, weights, [], collMap, variableProducers + dedxHitInfoVarProducer, branchSets = branchSetsMELA)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],     histSets, weights, [], collMap, variableProducers + dedxHitInfoVarProducer, branchSets = branchSetsMELA)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus], histSets, weights, [], collMap, variableProducers + dedxHitInfoVarProducer, branchSets = branchSetsMELA)

##########################################################################
# MVA channels
##########################################################################

# signal
if False:
    add_channels(
        process, 
        [mvaMETPreselectionSmearedJetsNLayers4, mvaMETPreselectionSmearedJetsNLayers5, mvaMETPreselectionSmearedJetsNLayers6plus],
        cms.VPSet(), 
        weights, 
        [], 
        collMap, 
        variableProducers + dedxHitInfoVarProducer, 
        branchSets = branchSetsMVA)

# electrons
if False:
    add_channels(
        process, 
        [mvaElePreselectionSmearedJetsNLayers4, mvaElePreselectionSmearedJetsNLayers5, mvaElePreselectionSmearedJetsNLayers6plus],
        cms.VPSet(),
        weightsWithEleSF,
        [],
        collMap,
        variableProducersWithElectrons + dedxHitInfoVarProducer,
        branchSets = branchSetsMVA)

# muons
if False:
    add_channels(
        process, 
        [mvaMuonPreselectionSmearedJetsNLayers4, mvaMuonPreselectionSmearedJetsNLayers5, mvaMuonPreselectionSmearedJetsNLayers6plus],
        cms.VPSet(),
        weightsWithMuonSF,
        [],
        collMap,
        variableProducersWithMuons + dedxHitInfoVarProducer,
        branchSets = branchSetsMVA)

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
