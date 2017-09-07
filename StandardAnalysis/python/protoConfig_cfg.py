import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from DisappTrks.StandardAnalysis.localConfig import *
from OSUT3Analysis.Configuration.processingUtilities import *
import os
import copy

data_global_tag = '76X_dataRun2_v15'
mc_global_tag = '76X_mcRun2_asymptotic_v12'
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    data_global_tag = '80X_dataRun2_2016SeptRepro_v6'
    mc_global_tag = '80X_mcRun2_asymptotic_2016_v3'
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_2_"):
    data_global_tag = '92X_dataRun2_Prompt_v8'
    mc_global_tag = '92X_upgrade2017_TSG_For90XSamples_V1'

################################################################################
# Create the skeleton process
################################################################################
process = cms.Process ('OSUAnalysis')

# set up the PoolSource with some default MC files suitable for testing
process.source = cms.Source ("PoolSource",
    bypassVersionCheck = cms.untracked.bool (True),
    skipBadFiles = cms.untracked.bool (True),
    fileNames = cms.untracked.vstring ([
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
    ]),
    inputCommands = cms.untracked.vstring ([
      "keep *",
      "drop *_cscSegments_*_*",
      #"drop *_reducedEcalRecHitsEE_*_*",
      #"drop *_reducedHcalRecHits_*_*",
      #"drop *_reducedEcalRecHitsEB_*_*",
      #"drop *_reducedHcalRecHits_*_*",
      "drop *_dt4DSegments_*_*",
    ]),
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_2_"):
    process.source.inputCommands = cms.untracked.vstring(["keep *"])

process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)
################################################################################

################################################################################
# Add the message logger
################################################################################
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
#process.MessageLogger.categories.append ("OSUTrackProducer")
#process.MessageLogger.categories.append ("osu_Track")
process.MessageLogger.categories.append ("InfoPrinter")
process.MessageLogger.categories.append ("osu_GenMatchable")
process.MessageLogger.cerr.osu_GenMatchable = cms.untracked.PSet(
    limit = cms.untracked.int32(0),
)
process.MessageLogger.categories.append ("disappTrks_TriggerWeightProducer")
process.MessageLogger.cerr.disappTrks_TriggerWeightProducer = cms.untracked.PSet(
    limit = cms.untracked.int32(0),
)
process.MessageLogger.categories.append ("OSUJetProducer")
process.MessageLogger.cerr.OSUJetProducer = cms.untracked.PSet(
    limit = cms.untracked.int32(0),
)
################################################################################

################################################################################
# Add the global tag
################################################################################
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, mc_global_tag, '')
if osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] == "data"):
    print "# Using global tag " + data_global_tag + "..."
    process.GlobalTag = GlobalTag(process.GlobalTag, data_global_tag, '')
else:
    print "# Using global tag " + mc_global_tag + "..."
################################################################################

process.metFilterPath = cms.Path ()

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Using BadPFMuonFilter and BadChargedCandidateFilter since we are in 80X..."
    process.load('RecoMET.METFilters.BadPFMuonFilter_cfi')
    process.BadPFMuonFilter.muons = cms.InputTag("slimmedMuons")
    process.BadPFMuonFilter.PFCandidates = cms.InputTag("packedPFCandidates")
    process.BadPFMuonFilter.taggingMode = cms.bool(True)

    process.load('RecoMET.METFilters.BadChargedCandidateFilter_cfi')
    process.BadChargedCandidateFilter.muons = cms.InputTag("slimmedMuons")
    process.BadChargedCandidateFilter.PFCandidates = cms.InputTag("packedPFCandidates")
    process.BadChargedCandidateFilter.taggingMode = cms.bool(True)

    process.metFilterPath = cms.Path (process.BadPFMuonFilter * process.BadChargedCandidateFilter)
else:
    print "# Not using BadPFMuonFilter and BadChargedCandidateFilter since we are in 76X..."

################################################################################
# Set up the collectionMap
################################################################################
from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap

collectionMap.tracks = cms.InputTag ('candidateTrackProducer')
collectionMap.hardInteractionMcparticles = cms.InputTag ('prunedGenParticlePlusGeant')
# Nobody has more respect for consistent input tags than CMS does. Nobody.
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_2_"):
    collectionMap.trigobjs = cms.InputTag  ('slimmedPatTrigger')
################################################################################

################################################################################
# Set up the default event weights
################################################################################
from DisappTrks.StandardAnalysis.EventWeights import *
################################################################################

################################################################################
# Set up the lepton scale factor producers
# N.B.: These are only producers for eventvariables, the application of the SFs is controlled by the weights
#       Defaults are given as 76X in case customize() is not called to change them.
#       Further a general note: there are indeed "VetoID" scale factors for electrons, but to implement this you need to throw random numbers on these SFs, a la b-tagging SFs...call this a to-do.
# N.B. 2: These will look for framework object producers, meaning if you don't apply any cuts on say electrons it will throw a product-not-found error for osu::electrons
#         Meaning, only use these if they make sense to use
################################################################################
from DisappTrks.StandardAnalysis.LeptonScaleFactors import *
scaleFactorProducers = []
scaleFactorProducersWithElectrons = [ElectronScaleFactorProducer]
scaleFactorProducersWithMuons = [MuonScaleFactorProducer]
################################################################################

################################################################################
# Set up the default variable producers
################################################################################
variableProducers = []
variableProducers.append('LifetimeWeightProducer')
variableProducers.append('PrimaryVtxVarProducer')
variableProducers.append('EventJetVarProducer')
variableProducers.append('PUScalingFactorProducer')
variableProducers.append('ISRWeightProducer')
variableProducers.append('TriggerWeightProducer')
################################################################################

################################################################################
# Set up the collections of channels
################################################################################
from DisappTrks.StandardAnalysis.EventSelections import *
from DisappTrks.MuonBasedAnalysis.EventSelections import *
from DisappTrks.BackgroundEstimation.ElectronTagProbeSelections import *
from DisappTrks.BackgroundEstimation.MuonTagProbeSelections import *
from DisappTrks.BackgroundEstimation.TauTagProbeSelections import *
from DisappTrks.BackgroundEstimation.WtoMuNuSelections import *
from DisappTrks.BackgroundEstimation.ZtoMuMuSelections import *
from DisappTrks.BackgroundEstimation.ZtoEESelections import *
from DisappTrks.SignalSystematics.SignalSystematicSelections import *
from DisappTrks.TriggerAnalysis.TriggerAnalysisSelections import *
################################################################################

################################################################################
# Set up the collections of histograms
################################################################################
from OSUT3Analysis.Configuration.histogramDefinitions import * # import this first so we can overwrite standard histogram definitions if needed
from DisappTrks.StandardAnalysis.HistogramDefinitions import *

histSets = cms.VPSet (
    TrackHistograms,
    TrackBeamspotHistograms,
    TrackEventVarHistograms,
    TrackExtraHistograms,
    MetHistograms,
    MetExtraHistograms,
    MetEventVariableHistograms,
    JetHistograms,
    EventVariableHistograms,
    EventVariablePVHistograms,
    TrackMETHistograms,
    TrackEventVariableHistograms,
)

histSetsDebug = cms.VPSet(
    TrackHistograms,
    TrackExtraHistograms,
    TrackDebugEcaloHistograms,
    TrackDebugHitPatternHistograms,
)

histSetsMetJet = cms.VPSet (
    MetHistograms,
    MetExtraHistograms,
    MetEventVariableHistograms,
    JetHistograms,
    EventVariableHistograms,
    EventVariablePVHistograms,
)

histSetsElectron = copy.deepcopy(histSets)
histSetsElectron.append(ElectronHistograms)
histSetsElectron.append(ElectronExtraHistograms)
histSetsElectron.append(DiElectronHistograms)
histSetsElectron.append(TrackElectronHistograms)
histSetsElectron.append(ElectronMETHistograms)
histSetsElectron.append(TrackElectronMETHistograms)
histSetsElectron.append(ElectronEventVariableHistograms)
histSetsElectron.append(ElectronIPHistograms)

histSetsMuon = copy.deepcopy(histSets)
histSetsMuon.append(MuonHistograms)
histSetsMuon.append(MuonExtraHistograms)
histSetsMuon.append(DiMuonHistograms)
histSetsMuon.append(DiMuonExtraHistograms)
histSetsMuon.append(TrackMuonHistograms)
histSetsMuon.append(MuonMETHistograms)
histSetsMuon.append(TrackMuonMETHistograms)
histSetsMuon.append(MuonEventVariableHistograms)
histSetsMuon.append(MuonIPHistograms)

histSetsTau = copy.deepcopy(histSets)
histSetsTau.append(TauExtraHistograms)
histSetsTau.append(TrackTauHistograms)
histSetsTau.append(TauEventVariableHistograms)

histSetsTrigger = cms.VPSet(
    MetTriggerHistograms,
    EventTriggerVarHistograms,
    EventTriggerVarVsMetHistograms,
)

################################################################################
