import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from DisappTrks.StandardAnalysis.useAODFiles import *
from DisappTrks.StandardAnalysis.switchToBestTrack import *
import glob

data_global_tag = '80X_dataRun2_Prompt_v14'
mc_global_tag = '80X_mcRun2_asymptotic_2016_v3'

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
        "/store/data/Run2016B/SingleMuon/MINIAOD/PromptReco-v2/000/273/150/00000/34A57FB8-D819-E611-B0A4-02163E0144EE.root",
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

collectionMap.tracks = cms.InputTag  ("generalTracks", "")

################################################################################
##### Set up weights to be used in plotting and cutflows  ######################
################################################################################

weights = cms.VPSet ()

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
variableProducers.append("EventTriggerVarProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisappTrks.TriggerAnalysis.EventSelections import *

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from DisappTrks.TriggerAnalysis.HistogramDefinitions import *

histSets = cms.VPSet(
    METHistograms,
    TrackHistograms,
)

################################################################################
##### Sets of channels to be run simultaneously over a single skim. ############
################################################################################

DataChannels = [
    METLegDenominator,
    METLegNumerator,
    #TrackLegDenominatorWithTracks,
    #TrackLegNumeratorWithTracks,
    TrackLegDenominatorWithMuons,
    TrackLegNumeratorWithMuons,
]

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels(process, DataChannels, histSets, weights, [], collectionMap, variableProducers, False)

################################################################################
##### Debugging options
################################################################################
# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")
