import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from DisappTrks.StandardAnalysis.useAODFiles import *
import glob
import re

data_global_tag = '76X_dataRun2_v15'
mc_global_tag = '76X_mcRun2_asymptotic_v12'

def switchToBestTrack (channel, histogramSets):
    for cut in channel.cuts:
        cutString = cut.cutString.pythonValue ()[1:-1]
        if re.search (r"missingOuterHits", cutString):
            cutString = re.sub (r"missingOuterHits", r"bestTrackMissingOuterHits", cutString)
        cut.cutString = cms.string (cutString)

    for histogramSet in histogramSets:
        for histogram in histogramSet.histograms:
            i = 0
            for inputVariable in histogram.inputVariables:
                if re.search (r"missingOuterHits", inputVariable):
                    inputVariable = re.sub (r"missingOuterHits", r"bestTrackMissingOuterHits", inputVariable)
                histogram.inputVariables[i] = inputVariable
                i += 1

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.MessageLogger.categories.append ("OSUTrackProducer")
if osusub.batchMode and (osusub.datasetLabel in types) and (types[osusub.datasetLabel] != "data"):
    process.MessageLogger.categories.append ("GenMatchable")
    process.MessageLogger.cerr.GenMatchable = cms.untracked.PSet(
        limit = cms.untracked.int32(1),
    )

#process.ProfilerService = cms.Service ("ProfilerService",
#    firstEvent = cms.untracked.int32(2),
#    lastEvent = cms.untracked.int32(20),
#    paths = cms.untracked.vstring('variableProducerPath', 'metMinimalSkim')
#)

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
    bypassVersionCheck = cms.untracked.bool (True),
    skipBadFiles = cms.untracked.bool (True),
    fileNames = cms.untracked.vstring ([
        "file:/home/hart/CMSSW_7_6_3/src/DisappTrks/StandardAnalysis/test/condor/2015/baseSkims/DYJetsToLL_50/metMinimalSkim/skim_972.root"
    ]),
)
#addSecondaryFiles (process.source)

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
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

from DisappTrks.StandardAnalysis.EventSelections import *
#from DisappTrks.StandardAnalysis.ElectronTagProbeSelections import *
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
    MetShiftHistograms,
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
histSetsElectron.append(ElectronMETHistograms)
histSetsElectron.append(TrackMETHistograms)
histSetsElectron.append(TrackElectronMETHistograms)

histSetsMuon = copy.deepcopy(histSets)
histSetsMuon.append(MuonHistograms)
histSetsMuon.append(MuonExtraHistograms)
histSetsMuon.append(DiMuonHistograms)
histSetsMuon.append(TrackMuonHistograms)
histSetsMuon.append(MuonMETHistograms)
histSetsMuon.append(TrackMETHistograms)
histSetsMuon.append(TrackMuonMETHistograms)

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
    #ElectronTagPt35,
    #ElectronTagPt35MetTrig,
    candTrkIdElecPt35,
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
    MuonTagPt35MetTrig,
    #candTrkIdMuPt35,
]

MuonBkgdEstimateNoNMissOut = [
    MuonTagPt55NoNMissOut,
    MuonTagPt55NoNMissOutMetTrig,
]

MuonBkgdEstimate = [
    MuonTagPt55,
    MuonTagPt55MetTrig,
]

TauBkgdClosureTest = [ # run over Wjets and TTjets MC sample (no skim)
    TauTagPt50,
    TauTagPt50MetTrig,
    candTrkIdTauPt50,
]

TauBkgdEstimate = [ # run over data
    TauTagPt55,
    TauTagPt55MetTrig,
]

addSingleCut (ZtoEleDisTrk.cuts, cutTrkNMissOut, cutTrkEcalo)

addSingleCut (ZtoMuDisTrk.cuts, cutTrkNMissOut, cutTrkMuonVeto)

addSingleCut (ZtoTauToEleDisTrk.cuts, cutTrkJetDeltaPhi, cutTrkEcalo)
addSingleCut (ZtoTauToEleDisTrk.cuts, cutTrkNMissOut, cutTrkJetDeltaPhi)

addSingleCut (ZtoTauToMuDisTrk.cuts, cutTrkJetDeltaPhi, cutTrkEcalo)
addSingleCut (ZtoTauToMuDisTrk.cuts, cutTrkNMissOut, cutTrkJetDeltaPhi)

removeCuts (ElectronTagPt55.cuts, [cutTrkEcalo])
removeCuts (ElectronTagPt55MetTrig.cuts, [cutTrkEcalo])

removeCuts (ElectronTagPt55.cuts, [cutTrkNMissOut])
removeCuts (ElectronTagPt55MetTrig.cuts, [cutTrkNMissOut])

removeCuts (MuonTagPt55.cuts, [cutTrkNMissOut])
removeCuts (MuonTagPt55MetTrig.cuts, [cutTrkNMissOut])

removeCuts (TauTagPt55.cuts, [cutTrkEcalo])
removeCuts (TauTagPt55MetTrig.cuts, [cutTrkEcalo])

removeCuts (TauTagPt55.cuts, [cutTrkJetDeltaPhi])
removeCuts (TauTagPt55MetTrig.cuts, [cutTrkJetDeltaPhi])

removeCuts (TauTagPt55.cuts, [cutTrkNMissOut])
removeCuts (TauTagPt55MetTrig.cuts, [cutTrkNMissOut])

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

add_channels  (process,  [disTrkSelection, disTrkNoMet],       histSets,        weights,  [],  collectionMap,  variableProducers,  False)  # For MC only!  Use isoTrkSelection skim as input.

process.PUScalingFactorProducer.PU = cms.string(os.environ['CMSSW_BASE'] + '/src/DisappTrks/StandardAnalysis/data/pu_disappTrks_run2.root')
process.PUScalingFactorProducer.target = cms.string("data2015")
process.PUScalingFactorProducer.dataset = cms.string("data2015")
process.PUScalingFactorProducer.type = cms.string("data")

################################################################################
##### Debugging options
################################################################################
# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

#process.Tracer = cms.Service("Tracer")
