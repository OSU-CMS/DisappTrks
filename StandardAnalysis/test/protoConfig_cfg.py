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
        "root://xrootd.rcac.purdue.edu//store/user/wulsin/SingleMuon/Run2015D-16Dec2015-v1-DisappTrks-v1/160131_105005/0000/miniAODWithCandidateTracks_1.root",
        #'/store/user/ahart/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160204_180900/0000/miniAODWithCandidateTracks_1.root',
        # "/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_1.root",
        # "/store/user/ahart/AMSB_chargino100GeV_ctau10cm_step4_User/AMSB_chargino_step4_0.root",
        # "file:condor/metMinimalSkim_76X/WJetsToLNu/metMinimalSkim/skim_1.root",
        # "file:condor/electronTagSkim/WJetsToLNu/ElectronTagSkim/skim_0.root",
    ),
)

# Uncomment the following if you need access to collections in AOD. N.B.: since
# the data ntuples are not ancestors of the AOD files, this requires special
# modifications to IOPool/Input. Even after these modifications, saving skims
# for data will not work.

# addSecondaryFiles (process.source)

# Add all files in a directory:
# dirname = "condor/isoTrkSelection/MET_2015D/IsoTrkSelection/"
# for f in glob.glob(dirname + "skim*.root"):
#     process.source.fileNames.extend(cms.untracked.vstring('file:' + f))


# process.source.eventsToProcess = cms.untracked.VEventRange (
#     "1:60:53",
# )



# FIXME:  set_input does not work (because of error with /usr/bin/file) in CMSSW_7_4_5_ROOT5
# argument can be a ROOT file, directory, or dataset name*
# *registered dataset names are listed in 'datasets' in:
#    https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Configuration/python/configurationOptions.py

# sample direcotory
# set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/")

# sample ROOT file
#set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_10_2_Dzw.root")

# sample dataset nickname
#set_input(process, "DYToTauTau_20")
#set_input(process, "DYToMuMu_20")

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
collectionMap.hardInteractionMcparticles = cms.InputTag ('prunedGenParticlePlusGeant')       # For data skim and new samples

################################################################################
##### Set up weights to be used in plotting and cutflows  ######################
################################################################################

weights = cms.VPSet (
    cms.PSet (
        inputCollections = cms.vstring("eventvariables"),
        inputVariable = cms.string("lifetimeWeight")
    ),
)

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
variableProducers.append("LifetimeWeightProducer")
variableProducers.append("PrimaryVtxVarProducer")
variableProducers.append("EventJetVarProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisappTrks.StandardAnalysis.EventSelections import *
from DisappTrks.StandardAnalysis.ElectronTagProbeSelections_alt import *
from DisappTrks.StandardAnalysis.MuonTagProbeSelections import *
from DisappTrks.StandardAnalysis.TauTagProbeSelections import *

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
    MetHistograms,
    MetExtraHistograms,
    JetHistograms,
    EventVariableHistograms,
    EventVariablePVHistograms,
)

histSetsDebug = cms.VPSet(
    TrackHistograms,
    TrackExtraHistograms,
    TrackDebugEcaloHistograms,
)

histSetsMetJet = cms.VPSet (
    MetHistograms,
    JetHistograms
)

histSetsElectron = copy.deepcopy(histSets)
histSetsElectron.append(ElectronHistograms)
histSetsElectron.append(ElectronExtraHistograms)
histSetsElectron.append(DiElectronHistograms)
histSetsElectron.append(TrackElectronHistograms)

histSetsMuon = copy.deepcopy(histSets)
histSetsMuon.append(MuonHistograms)
histSetsMuon.append(MuonExtraHistograms)
histSetsMuon.append(DiMuonHistograms)
histSetsMuon.append(DiMuonExtraHistograms)
histSetsMuon.append(TrackMuonHistograms)

histSetsTau = copy.deepcopy(histSets)
histSetsTau.append(TauExtraHistograms)

test = cms.PSet(
    name = cms.string("test"),
    triggers = cms.vstring(),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.vstring("primaryvertexs"),
            cutString = cms.string("isValid > 0 && ndof >= 4"),
            numberRequired = cms.string(">= 1")
        )
    )
)

################################################################################
##### Sets of channels to be run simultaneously over a single skim. ############
################################################################################

LepCtrlChannels = [ # Run over isoTrkSelection skim
    elecCtrlSelection,
    muonCtrlSelection,
    tauCtrlSelection,
]
BkgdEstChannels = [
    candTrkLoose,
    candTrkLooseElec,
    candTrkLooseMuon, 
    candTrkLooseTau,
    candTrkSelection,
    candTrkEcaloSdband,
    candTrkNMissOutSdband,
]
BkgdCtrlChannels = LepCtrlChannels + BkgdEstChannels

DisTrkChannels = [
    # disTrkIdElec,
    # disTrkIdMuon,
    # disTrkIdTau,
    # disTrkIdFake,
    disTrkNoNMissOut,
    disTrkSelection,
]

FakeTrkSystChannels = [
    disTrkSelectionNHits3,
    disTrkSelectionNHits4,
    disTrkSelectionNHits5,
    disTrkSelectionNHits6,
]

ZtoMuMuTrkChannels = [ # run over ZtoMuMu skim
    ZtoMuMuCandTrk,
    ZtoMuMuDisTrk,
    ZtoMuMuCandTrkEcaloSdband,
    ZtoMuMuCandTrkNMissOutSdband,
    ZtoMuMuDisTrkNHits3,
    ZtoMuMuDisTrkNHits4,
    ZtoMuMuDisTrkNHits5,
    ZtoMuMuDisTrkNHits6,
]

ElecBkgdClosureTest = [ # run over Wjets and TTjets MC sample (no skim)
    ElectronTagPt35,
    ElectronTagPt35NoTrig,
    ElectronTagPt35MetTrig,
    candTrkIdElecPt35,
    candTrkIdElecPt35NoMet,
]

ElecBkgdEstimate = [ # run over data
    ElectronTagPt55,
    ElectronTagPt55MetTrig,
]

ElecTagProbeChannels = [ # run over ZtoEleProbeTrkWithZCuts skim
    ZtoEleCandTrk,
    ZtoEleDisTrk,
    ZtoEleDisTrkNoNMissOut,
    ZtoEleCandTrkSdbandEcalo,
    ZtoEleCandTrkSdbandNMissOut,
]

MuonBkgdClosureTest = [ # run over Wjets and TTjets MC sample (no skim)
    MuonTagPt35,
    MuonTagPt35NoTrig,
    MuonTagPt35MetCut,
    MuonTagPt35MetTrig,
    candTrkIdMuPt35,
    candTrkIdMuPt35NoMet,
]

MuonBkgdEstimateNoNMissOut = [ 
    MuonTagPt55NoNMissOut,
    MuonTagPt55NoNMissOutMetTrig,
]

MuonBkgdEstimate = [ 
    MuonTagPt55,
    # MuonTagPt55NoTrig,
    # MuonTagPt55MetCut,
    MuonTagPt55MetTrig,
]

TauBkgdClosureTest = [ # run over Wjets and TTjets MC sample (no skim)
    TauTagPt50,
    TauTagPt50NoTrig,
    TauTagPt50MetCut,
    TauTagPt50MetTrig,
    candTrkIdTauPt50,
    candTrkIdTauPt50NoMet,
]

TauBkgdEstimate = [ # run over data
    TauTagPt55,
    TauTagPt55NoTrig,
    TauTagPt55MetCut,
    TauTagPt55MetTrig,
]

switchToBestTrack (disTrkSelection, histSets)

switchToBestTrack (ZtoEleProbeTrkWithZCuts, histSetsElectron)
switchToBestTrack (ZtoEleDisTrk, histSetsElectron)
switchToBestTrack (ElectronTagPt55, histSetsElectron)
switchToBestTrack (ElectronTagPt55MetTrig, histSetsElectron)

switchToBestTrack (ZtoMuProbeTrkWithZCuts, histSetsMuon)
switchToBestTrack (ZtoMuDisTrk, histSetsMuon)
switchToBestTrack (MuonTagPt55, histSetsMuon)
switchToBestTrack (MuonTagPt55MetTrig, histSetsMuon)

switchToBestTrack (ZtoTauToEleProbeTrkWithZCuts, histSetsMuon)
switchToBestTrack (ZtoTauToEleDisTrk, histSetsMuon)

switchToBestTrack (ZtoTauToMuProbeTrkWithZCuts, histSetsMuon)
switchToBestTrack (ZtoTauToMuDisTrk, histSetsMuon)

switchToBestTrack (ZtoMuMuCandTrk, histSetsMuon)
switchToBestTrack (ZtoMuMuDisTrk, histSetsMuon)
switchToBestTrack (ZtoMuMuCandTrkEcaloSdband, histSetsMuon)
switchToBestTrack (ZtoMuMuCandTrkNMissOutSdband, histSetsMuon)
switchToBestTrack (ZtoMuMuDisTrkNHits3, histSetsMuon)
switchToBestTrack (ZtoMuMuDisTrkNHits4, histSetsMuon)
switchToBestTrack (ZtoMuMuDisTrkNHits5, histSetsMuon)
switchToBestTrack (ZtoMuMuDisTrkNHits6, histSetsMuon)

switchToBestTrack (disTrkSelectionNHits3, histSets)
switchToBestTrack (disTrkSelectionNHits4, histSets)
switchToBestTrack (disTrkSelectionNHits5, histSets)
switchToBestTrack (disTrkSelectionNHits6, histSets)

switchToBestTrack (TauTagPt55, histSetsTau)
switchToBestTrack (TauTagPt55MetTrig, histSetsTau)

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

## MANDATORY CHANNELS FOR MET DATASET
#  add_channels  (process,  [metMinimalSkim],     histSetsMetJet,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [isoTrkSelection],    histSets,        weights,  [],  collectionMap,  variableProducers,  True)  # use metMinimalSkim as input
# add_channels  (process,  BkgdEstChannels,      histSets,        weights,  [],  collectionMap,  variableProducers,  True)  # use isoTrkSelection skim as input
#  add_channels  (process,  LepCtrlChannels,      histSets,        weights,  [],  collectionMap,  variableProducers,  True)  # use isoTrkSelection skim as input
#  add_channels  (process,  DisTrkChannels,       histSets,        weights,  [],  collectionMap,  variableProducers,  True)  # For MC only!  Use isoTrkSelection skim as input.
#  add_channels  (process,  FakeTrkSystChannels,  histSets,        weights,  [],  collectionMap,  variableProducers,  True)  # use metMinimalSkim as input

## MANDATORY CHANNELS FOR TAU DATASET
#  add_channels  (process,  [TauTagSkim],        histSetsTau,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  TauBkgdClosureTest,  histSetsTau,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  TauBkgdEstimate,     histSetsTau,  weights,  [],  collectionMap,  variableProducers,  True)

## MANDATORY CHANNELS FOR SINGLEMUON DATASET
#  add_channels  (process,  [MuonTagSkim],              histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuMu],                  histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  ZtoMuMuTrkChannels,         histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuIsoTrk],              histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuProbeTrk],            histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuProbeTrkWithZCuts],   histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoMuDisTrk],              histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauIsoTrk],             histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauProbeTrk],           histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauProbeTrkWithZCuts],  histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoTauDisTrk],             histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  MuonBkgdClosureTest,        histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  MuonBkgdEstimateNoNMissOut, histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  MuonBkgdEstimate,           histSetsMuon,  weights,  [],  collectionMap,  variableProducers,  True)

## MANDATORY CHANNELS FOR SINGLEELECTRON DATASET
#  add_channels  (process,  [ElectronTagSkim],          histSetsElectron,  weights,  [],  collectionMap,  variableProducers,  True) # no input skim
#  add_channels  (process,  [ZtoEleIsoTrk],             histSetsElectron,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoEleProbeTrk],           histSetsElectron,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoEleProbeTrkWithZCuts],  histSetsElectron,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [ZtoEleDisTrk],             histSetsElectron,  weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  ElecTagProbeChannels,       histSetsElectron,  weights,  [],  collectionMap,  variableProducers,  True) # use ZtoEleProbeTrkWithZCuts skim as input
#  add_channels  (process,  ElecBkgdEstimate,           histSetsElectron,  weights,  [],  collectionMap,  variableProducers,  True) # use ElectronTagSkim skim as input
#  add_channels  (process,  ElecBkgdClosureTest,        histSetsElectron,  weights,  [],  collectionMap,  variableProducers,  True) # run over Wjets and TTjets MC sample

## CHANNELS FOR TESTING
#  add_channels  (process,  [test],               cms.VPSet(),       weights,  [],  collectionMap,  variableProducers,  True)
#  add_channels  (process,  [NoCuts],             cms.VPSet(),       weights,  [],  collectionMap,  variableProducers,  True)

## OTHER CHANNELS
#  add_channels  (process,  [nonIsoTrkSelection],     histSets,        weights,  [],  collectionMap,  variableProducers,  False)


################################################################################
##### Debugging options
################################################################################
# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")

