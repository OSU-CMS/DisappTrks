from DisappTrks.StandardAnalysis.protoConfig_cfg import *

# Central value channels
if False:
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers4],     histSets, weights, [], collMap, variableProducers + dedxHitInfoVarProducer, branchSets = branchSetsMELA)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers5],     histSets, weights, [], collMap, variableProducers + dedxHitInfoVarProducer, branchSets = branchSetsMELA)
	add_channels  (process,  [disTrkSelectionSmearedJetsNLayers6plus], histSets, weights, [], collMap, variableProducers + dedxHitInfoVarProducer, branchSets = branchSetsMELA)

##########################################################################
# MVA channels
##########################################################################

from DisappTrks.MELA.MVASelections import *

# signal
if False:
    add_channels(
        process, 
        [mvaMETPreselectionSmearedJetsNLayers4, mvaMETPreselectionSmearedJetsNLayers5, mvaMETPreselectionSmearedJetsNLayers6plus],
        histSets, 
        weights, 
        scaleFactorProducers, 
        collMap, 
        variableProducers + dedxHitInfoVarProducer, 
        branchSets = branchSetsMVA)

# fakes
if False:
    add_channels(
        process,
        [ZToMuMuPreselectionNLayers4, ZToMuMuPreselectionNLayers5, ZToMuMuPreselectionNLayers6plus],
        histSetsMuon,
        weightsWithMuonSF,
        scaleFactorProducersWithMuons,
        collMap,
        variableProducersWithMuons + dedxHitInfoVarProducer,
        branchSets = branchSetsMVA)

# electrons
if False:
    add_channels(
        process, 
        [mvaElePreselectionNLayers4, mvaElePreselectionNLayers5, mvaElePreselectionNLayers6plus],
        histSetsElectron, 
        weightsWithEleSF,
        scaleFactorProducersWithElectrons,
        collMap,
        variableProducers + dedxHitInfoVarProducer,
        branchSets = branchSetsMVA)

# muons
if False:
    add_channels(
        process, 
        [mvaMuonPreselectionNLayers4, mvaMuonPreselectionNLayers5, mvaMuonPreselectionNLayers6plus],
        histSetsMuon, 
        weightsWithMuonSF,
        scaleFactorProducersWithMuons,
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
