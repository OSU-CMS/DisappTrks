import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from DisappTrks.StandardAnalysis.useAODFiles import *
from DisappTrks.StandardAnalysis.switchToBestTrack import *
import glob

data_global_tag = '76X_dataRun2_v15'
mc_global_tag = '76X_mcRun2_asymptotic_v12'

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
        "/store/user/bfrancis/MET/Run2016B-PromptReco-v2-DisappTrks-v1/160609_200233/0000/PAT_PAT_10.root",
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

#collectionMap.tracks = cms.InputTag ('candidateDisappearingTracks')  # For signal (old version)
collectionMap.tracks = cms.InputTag ('candidateTrackProducer')       # For data skim and new samples

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
variableProducers.append("LifetimeWeightProducer")
variableProducers.append("PrimaryVtxVarProducer")
variableProducers.append("EventJetVarProducer")
variableProducers.append('PUScalingFactorProducer')

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisappTrks.SignalSystematics.SignalSystematicsSelections import *

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from DisappTrks.StandardAnalysis.HistogramDefinitions import *
from OSUT3Analysis.Configuration.histogramDefinitions import *

histSets = cms.VPSet (
    TrackHistograms,
    TrackBeamspotHistograms,
    TrackEventVarHistograms,
    TrackExtraHistograms,
    TrackDebugEcaloHistograms,
    MetHistograms,
    MetExtraHistograms,
    JetHistograms,
    EventVariableHistograms,
    EventVariablePVHistograms,
)

histSetsMuon = copy.deepcopy(histSets)
histSetsMuon.append(MuonHistograms)
histSetsMuon.append(MuonExtraHistograms)
histSetsMuon.append(DiMuonHistograms)
histSetsMuon.append(TrackMuonHistograms)

################################################################################
##### Sets of channels to be run simultaneously over a single skim. ############
################################################################################

ISRStudyChannels = [
    ZtoMuMuISRStudy,
    ZtoMuMuISRStudyVetoBjets,
    ZtoMuMuISRStudyMoreSimilar,
]

switchToBestTrack(ZtoMuMuISRStudy, histSetsMuon)
switchToBestTrack(ZtoMuMuISRStudyVetoBjets, histSetsMuon)
switchToBestTrack(ZtoMuMuISRStudyMoreSimilar, histSetsMuon)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels(process, ISRStudyChannels, histSetsMuon, weights, [], collectionMap, variableProducers, True)

process.PUScalingFactorProducer.dataset = cms.string("TTJets_DiLept")
process.PUScalingFactorProducer.target = cms.string("data2015")
process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
process.PUScalingFactorProducer.type = cms.string("bgMC")

################################################################################
##### Debugging options
################################################################################
# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")
