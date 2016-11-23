from DisappTrks.StandardAnalysis.protoConfig_cfg import *
import sys

if not os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_"):
    print "Please use a CMSSW_7_6_X release..."
    sys.exit (0)

process.source.fileNames = cms.untracked.vstring (
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_1.root",
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_10.root",
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_100.root",
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_101.root",
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_102.root",
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_103.root",
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_104.root",
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_105.root",
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_106.root",
    "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_107.root",
)

################################################################################
# MET channels
################################################################################
# Channels requiring only MET+jet
#  add_channels  (process,  [metMinimalSkim],  histSetsMetJet,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [basicSelection],  histSetsMetJet,  weights,  [],  collectionMap,  variableProducers,  True)

# Channels requiring MET+jet+track
#  add_channels  (process,  [isoTrkSelection],    histSets,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [candTrkSelection],   histSets,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [elecCtrlSelection],  histSets,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [muonCtrlSelection],  histSets,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [tauCtrlSelection],   histSets,  weights,  [],  collectionMap,  variableProducers,  True)

# Variations of the disappearing tracks search region
#  add_channels  (process,  [disTrkIdElec],      histSets,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [disTrkIdMuon],      histSets,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [disTrkIdTau],       histSets,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [disTrkIdFake],      histSets,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [disTrkNoNMissOut],  histSets,  weights,  [],  collectionMap,  variableProducers,  True)

# THE disappearing tracks search region
#  add_channels  (process,  [disTrkSelection],  histSets,  weights,  [],  collectionMap,  variableProducers,  True)
################################################################################

process.PUScalingFactorProducer.PU     = cms.string (os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
process.PUScalingFactorProducer.target = cms.string ("data2015")

setMissingHitsCorrection (process, "2015")
