import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from DisappTrks.StandardAnalysis.useAODFiles import *
from DisappTrks.StandardAnalysis.utilities import *
import glob

data_global_tag = '80X_dataRun2_2016SeptRepro_v6'
mc_global_tag = '80X_mcRun2_asymptotic_2016_miniAODv2_v1'

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.categories.append ("OSUTrackProducer")
process.MessageLogger.categories.append ("GenMatchable")
process.MessageLogger.cerr.GenMatchable = cms.untracked.PSet(
    limit = cms.untracked.int32(1),
)

# Use the following block for the Calo calculation.
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, mc_global_tag, '')
if osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] == "data"):
    print "using global tag " + data_global_tag + "..."
    process.GlobalTag = GlobalTag(process.GlobalTag, data_global_tag, '')
else:
    print "using global tag " + mc_global_tag + "..."


# input source when running interactively
# ---------------------------------------
process.source = cms.Source ("PoolSource",
    #bypassVersionCheck = cms.untracked.bool (True),
    skipBadFiles = cms.untracked.bool (True),
    fileNames = cms.untracked.vstring (
        "root://cmsxrootd-site2.fnal.gov:1092//store/data/Run2016G/SingleMuon/MINIAOD/23Sep2016-v1/90001/FCE3D2A7-8299-E611-899F-549F3525BF58.root",
            #"root://cmsxrootd-site2.fnal.gov:1093//store/mc/RunIISpring16MiniAODv2/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/20000/C6562975-AB56-E611-B9A4-0025905B8566.root",
        #"file:/data/users/hart/condor/signalMC/2016/AMSB_chargino_M-500_CTau-10_TuneZ2star_13TeV_pythia6_step4/hist_365.root",
    ),
)

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap  # miniAOD

collectionMap.tracks = cms.InputTag  ("candidateTrackProducer", "")
collectionMap.hardInteractionMcparticles = cms.InputTag ('prunedGenParticlePlusGeant')

################################################################################
##### Set up weights to be used in plotting and cutflows  ######################
################################################################################

weights = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("lifetimeWeight")
    ),
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("puScalingFactor")
    ),
)

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
variableProducers.append("EventTriggerVarProducer")
variableProducers.append('PUScalingFactorProducer')

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisappTrks.TriggerAnalysis.EventSelections_2016 import *

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from DisappTrks.TriggerAnalysis.HistogramDefinitions import *

histSets = cms.VPSet(
    METHistograms,
    MuonHistograms,
    EventVariableHistograms,
)

histSetsTracks = cms.VPSet(
    METHistograms,
    TrackHistograms,
    EventVariableHistograms,
)

################################################################################
##### Sets of channels to be run simultaneously over a single skim. ############
################################################################################

DataWJetsChannels = [
    METLegDenominator,
    METLegNumerator,
    TrackLegDenominatorWithMuons,
    TrackLegNumeratorWithMuons,
    TrackLegNumeratorWithMuonsAnyHLTMatch,
]

DataWJetsMet90Channels = [
    # METLegDenominator,
    MET90LegNumerator,
    TrackLegDenominatorWithMuonsMet90,
    TrackLegNumeratorWithMuonsMet90,
    TrackLegNumeratorWithMuonsAnyHLTMatchMet90,
]

SignalChannels = [
    METLegDenominator,
    METLegNumerator,
    TrackLegDenominatorWithTracksNoTrig,
    TrackLegNumeratorWithTracksNoTrig,
]

SignalMet90Channels = [
    # METLegDenominator,
    MET90LegNumerator,
    TrackLegDenominatorWithTracksNoTrigMet90,
    TrackLegNumeratorWithTracksNoTrigMet90,
]

for ch in DataWJetsChannels:
    switchToBestTrack(ch, histSets)

for ch in DataWJetsMet90Channels:
    switchToBestTrack(ch, histSets)

for ch in SignalChannels:
    switchToBestTrack(ch, histSetsTracks)

for ch in SignalMet90Channels:
    switchToBestTrack(ch, histSetsTracks)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels(process, DataWJetsChannels, histSets, weights, [], collectionMap, variableProducers, False)
#add_channels(process, DataWJetsMet90Channels, histSets, weights, [], collectionMap, variableProducers, False)
#add_channels(process, SignalChannels, histSetsTracks, weights, [], collectionMap, variableProducers, False)

process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
process.PUScalingFactorProducer.target = cms.string("data2016")
process.PUScalingFactorProducer.dataset = cms.string("data2016")
process.PUScalingFactorProducer.type = cms.string("data")

################################################################################
##### Debugging options
################################################################################
# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")
