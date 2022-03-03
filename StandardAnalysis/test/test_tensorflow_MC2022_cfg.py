# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein step1_RECO.root --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 120X_mcRun3_2021_realistic_v6 --step PAT --nThreads 4 --scenario pp --era Run3 --python_filename test_tensorflow_MC2022_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 100
import FWCore.ParameterSet.Config as cms
import os
from Configuration.Eras.Era_Run3_cff import Run3

# get the data/ directory
thisdir = os.path.dirname(os.path.abspath("__file__"))
datadir = os.path.join(os.path.dirname(thisdir), "test")

process = cms.Process('PAT',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(#'file:step1_RECO.root'),
    #'/store/mc/Run3Summer21DRPremix/DYToLL_M-50_TuneCP5_14TeV-pythia8/AODSIM/120X_mcRun3_2021_realistic_v6-v2/30002/01326cce-6f8b-40a4-a0e9-8af154b3ac55.root'
    '/store/mc/Run3Summer21DRPremix/DYToLL_M-50_TuneCP5_14TeV-pythia8/AODSIM/120X_mcRun3_2021_realistic_v6-v2/2550000/0088b6cd-2fc0-402a-9905-34419b8abb40.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('step1_PAT.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedCandidates_packedPFCandidates__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenParticles_prunedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('patTriggerObjectStandAlones_slimmedPatTrigger__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedGenParticles_packedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJets__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVertices__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVerticesWithBS__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoCaloClusters_reducedEgamma_reducedESClusters_*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEERecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenJets_slimmedGenJets__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJetsPuppi__*'),
            splitLevel = cms.untracked.int32(99)
        ),
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedESRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        )
    ),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '120X_mcRun3_2021_realistic_v6', '')

process.load('DisappTrks.CandidateTrackProducer.CandidateTrackProducer_cfi')
process.candidateTracks = cms.Path(process.candidateTrackProducer)

# setup tensorflowPlugin by loading the auto-generated cfi (see tensorflowPlugin.fillDescriptions)
process.load("DisappTrks.StandardAnalysis.tensorflowPlugin_cfi")
process.tensorflowPlugin.graphPath = cms.string(os.path.join(datadir, "graph.pb"))
process.tensorflowPlugin.inputTensorName = cms.string("Input_input")
#process.tensorflowPlugin.outputTensorName = cms.string("sequential/output/Sigmoid")
process.tensorflowPlugin.outputTensorName = cms.string("sequential/Output/Sigmoid")


process.load("DisappTrks.StandardAnalysis.fakeTrackVarProducer_cfi")
process.fakeTrackVarProducer.graphPath = cms.string(os.path.join(datadir, "graph.pb"))
process.fakeTrackVarProducer.inputTensorName = cms.string("Input_input")
process.fakeTrackVarProducer.outputTensorName = cms.string("sequential/Output/Sigmoid")
process.fakeTrackVarProducer.triggers = cms.InputTag("TriggerResults", "", "HLT")
process.fakeTrackVarProducer.triggerObjects = cms.InputTag("slimmedPatTrigger")
process.fakeTrackVarProducer.tracks= cms.InputTag("candidateTrackProducer")
process.fakeTrackVarProducer.genParticles = cms.InputTag("prunedGenParticles", "")
process.fakeTrackVarProducer.met = cms.InputTag("slimmedMETs")
process.fakeTrackVarProducer.electrons = cms.InputTag("slimmedElectrons", "")
process.fakeTrackVarProducer.muons = cms.InputTag("slimmedMuons", "")
process.fakeTrackVarProducer.taus = cms.InputTag("slimmedTaus", "")
process.fakeTrackVarProducer.pfCandidates = cms.InputTag("packedPFCandidates", "")
process.fakeTrackVarProducer.vertices = cms.InputTag("offlineSlimmedPrimaryVertices", "")
process.fakeTrackVarProducer.jets = cms.InputTag("slimmedJets", "")

process.fakeTrackVarProducer.rhoCentralCalo = cms.InputTag("fixedGridRhoFastjetCentralCalo")

process.fakeTrackVarProducer.EBRecHits = cms.InputTag("reducedEcalRecHitsEB")
process.fakeTrackVarProducer.EERecHits = cms.InputTag("reducedEcalRecHitsEE")
process.fakeTrackVarProducer.ESRecHits = cms.InputTag("reducedEcalRecHitsES")
process.fakeTrackVarProducer.HBHERecHits = cms.InputTag("reducedHcalRecHits", "hbhereco")
process.fakeTrackVarProducer.CSCSegments = cms.InputTag("cscSegments")
process.fakeTrackVarProducer.DTRecSegments = cms.InputTag("dt4DSegments")
process.fakeTrackVarProducer.RPCRecHits = cms.InputTag("rpcRecHits")

process.fakeTrackVarProducer.dEdxPixel = cms.InputTag ("dedxPixelHarmonic2", "")
process.fakeTrackVarProducer.dEdxStrip = cms.InputTag ("dedxHarmonic2", "")
process.fakeTrackVarProducer.isolatedTracks = cms.InputTag("isolatedTracks", "")
process.fakeTrackVarProducer.isoTrk2dedxHitInfo = cms.InputTag("isolatedTracks", "")
process.fakeTrackVarProducer.genTracks = cms.InputTag("generalTracks", "")
process.fakeTrackVarProducer.pileupInfo = cms.InputTag ("addPileupInfo")

process.fakeTrackVarProducer.minTrackPt = cms.double(20.0)
process.fakeTrackVarProducer.minGenParticlePt = cms.double(-1)
process.fakeTrackVarProducer.maxRelTrackIso = cms.double(-1)
process.fakeTrackVarProducer.dataTakingPeriod = cms.string("2017")
process.fakeTrackVarProducer.etaRangeNearTrack = cms.double(-1)
process.fakeTrackVarProducer.phiRangeNearTrack = cms.double(-1)
process.fakeTrackVarProducer.maxNumOfRecHits = cms.int32(-1)
process.fakeTrackVarProducer.signalTriggerNames = cms.vstring([
        'HLT_MET105_IsoTrk50_v',
        'HLT_PFMET120_PFMHT120_IDTight_v',
        'HLT_PFMET130_PFMHT130_IDTight_v',
        'HLT_PFMET140_PFMHT140_IDTight_v',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
        'HLT_PFMET250_HBHECleaned_v',
        'HLT_PFMET300_HBHECleaned_v'])
process.fakeTrackVarProducer.metFilterNames = cms.vstring([
        "Flag_goodVertices",
        "Flag_globalTightHalo2016Filter",
        "Flag_HBHENoiseFilter",
        "Flag_HBHENoiseIsoFilter",
        "Flag_EcalDeadCellTriggerPrimitiveFilter",
        "Flag_BadPFMuonFilter",
        "Flag_globalTightHalo2016Filter",
        "Flag_globalSuperTightHalo2016Filter"])

process.load("DisappTrks.StandardAnalysis.deepSetElectronVarProducer_cfi")
process.deepSetElectronVarProducer.graphPath = cms.string(os.path.join(datadir, "graph_electron.pb"))
process.deepSetElectronVarProducer.inputTensorName = cms.string("input")
process.deepSetElectronVarProducer.inputTrackTensorName = cms.string("input_track")
process.deepSetElectronVarProducer.outputTensorName = cms.string("model_1/output_xyz/Softmax")
process.deepSetElectronVarProducer.triggers = cms.InputTag("TriggerResults", "", "HLT")
process.deepSetElectronVarProducer.triggerObjects = cms.InputTag("slimmedPatTrigger")
process.deepSetElectronVarProducer.tracks= cms.InputTag("candidateTrackProducer")
process.deepSetElectronVarProducer.genParticles = cms.InputTag("prunedGenParticles", "")
process.deepSetElectronVarProducer.met = cms.InputTag("slimmedMETs")
process.deepSetElectronVarProducer.electrons = cms.InputTag("slimmedElectrons", "")
process.deepSetElectronVarProducer.muons = cms.InputTag("slimmedMuons", "")
process.deepSetElectronVarProducer.taus = cms.InputTag("slimmedTaus", "")
process.deepSetElectronVarProducer.pfCandidates = cms.InputTag("packedPFCandidates", "")
process.deepSetElectronVarProducer.vertices = cms.InputTag("offlineSlimmedPrimaryVertices", "")
process.deepSetElectronVarProducer.jets = cms.InputTag("slimmedJets", "")

process.deepSetElectronVarProducer.rhoCentralCalo = cms.InputTag("fixedGridRhoFastjetCentralCalo")

process.deepSetElectronVarProducer.EBRecHits = cms.InputTag("reducedEcalRecHitsEB")
process.deepSetElectronVarProducer.EERecHits = cms.InputTag("reducedEcalRecHitsEE")
process.deepSetElectronVarProducer.ESRecHits = cms.InputTag("reducedEcalRecHitsES")
process.deepSetElectronVarProducer.HBHERecHits = cms.InputTag("reducedHcalRecHits", "hbhereco")
process.deepSetElectronVarProducer.CSCSegments = cms.InputTag("cscSegments")
process.deepSetElectronVarProducer.DTRecSegments = cms.InputTag("dt4DSegments")
process.deepSetElectronVarProducer.RPCRecHits = cms.InputTag("rpcRecHits")

process.deepSetElectronVarProducer.dEdxPixel = cms.InputTag ("dedxPixelHarmonic2", "")
process.deepSetElectronVarProducer.dEdxStrip = cms.InputTag ("dedxHarmonic2", "")
process.deepSetElectronVarProducer.isolatedTracks = cms.InputTag("isolatedTracks", "")
process.deepSetElectronVarProducer.isoTrk2dedxHitInfo = cms.InputTag("isolatedTracks", "")
process.deepSetElectronVarProducer.genTracks = cms.InputTag("generalTracks", "")
process.deepSetElectronVarProducer.pileupInfo = cms.InputTag ("addPileupInfo")

process.deepSetElectronVarProducer.minTrackPt = cms.double(20.0)
process.deepSetElectronVarProducer.minGenParticlePt = cms.double(-1)
process.deepSetElectronVarProducer.maxRelTrackIso = cms.double(-1)
process.deepSetElectronVarProducer.dataTakingPeriod = cms.string("2017")
process.deepSetElectronVarProducer.etaRangeNearTrack = cms.double(-1)
process.deepSetElectronVarProducer.phiRangeNearTrack = cms.double(-1)
process.deepSetElectronVarProducer.maxNumOfRecHits = cms.int32(-1)
process.deepSetElectronVarProducer.signalTriggerNames = cms.vstring([
        'HLT_MET105_IsoTrk50_v',
        'HLT_PFMET120_PFMHT120_IDTight_v',
        'HLT_PFMET130_PFMHT130_IDTight_v',
        'HLT_PFMET140_PFMHT140_IDTight_v',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
        'HLT_PFMET250_HBHECleaned_v',
        'HLT_PFMET300_HBHECleaned_v'])
process.deepSetElectronVarProducer.metFilterNames = cms.vstring([
        "Flag_goodVertices",
        "Flag_globalTightHalo2016Filter",
        "Flag_HBHENoiseFilter",
        "Flag_HBHENoiseIsoFilter",
        "Flag_EcalDeadCellTriggerPrimitiveFilter",
        "Flag_BadPFMuonFilter",
        "Flag_globalTightHalo2016Filter",
        "Flag_globalSuperTightHalo2016Filter"])


process.trackImageProducer = cms.EDAnalyzer ("TrackImageProducerMINIAOD",
    triggers       = cms.InputTag("TriggerResults", "", "HLT"),
    triggerObjects = cms.InputTag("slimmedPatTrigger"),
    tracks         = cms.InputTag("candidateTrackProducer"),
    genParticles   = cms.InputTag("prunedGenParticles", ""),
    met            = cms.InputTag("slimmedMETs"),
    electrons      = cms.InputTag("slimmedElectrons", ""),
    muons          = cms.InputTag("slimmedMuons", ""),
    taus           = cms.InputTag("slimmedTaus", ""),
    pfCandidates   = cms.InputTag("packedPFCandidates", ""),
    vertices       = cms.InputTag("offlineSlimmedPrimaryVertices", ""),
    jets           = cms.InputTag("slimmedJets", ""),

    rhoCentralCalo = cms.InputTag("fixedGridRhoFastjetCentralCalo"),

    EBRecHits     =  cms.InputTag("reducedEcalRecHitsEB"),
    EERecHits     =  cms.InputTag("reducedEcalRecHitsEE"),
    ESRecHits     =  cms.InputTag("reducedEcalRecHitsES"),
    HBHERecHits   =  cms.InputTag("reducedHcalRecHits", "hbhereco"),
    CSCSegments   =  cms.InputTag("cscSegments"),
    DTRecSegments =  cms.InputTag("dt4DSegments"),
    RPCRecHits    =  cms.InputTag("rpcRecHits"),

    tauDecayModeFinding      = cms.InputTag("hpsPFTauDiscriminationByDecayModeFinding"),
    tauElectronDiscriminator = cms.InputTag("hpsPFTauDiscriminationByMVA6LooseElectronRejection"),
    tauMuonDiscriminator     = cms.InputTag("hpsPFTauDiscriminationByLooseMuonRejection3"),

    dEdxPixel = cms.InputTag ("dedxPixelHarmonic2", ""),
    dEdxStrip = cms.InputTag ("dedxHarmonic2", ""),
    isolatedTracks = cms.InputTag("isolatedTracks", ""),
    isoTrk2dedxHitInfo = cms.InputTag("isolatedTracks", ""),
    genTracks = cms.InputTag("generalTracks", ""),
    pileupInfo = cms.InputTag ("addPileupInfo"),

    signalTriggerNames = cms.vstring([
        'HLT_MET105_IsoTrk50_v',
        'HLT_PFMET120_PFMHT120_IDTight_v',
        'HLT_PFMET130_PFMHT130_IDTight_v',
        'HLT_PFMET140_PFMHT140_IDTight_v',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
        'HLT_PFMET250_HBHECleaned_v',
        'HLT_PFMET300_HBHECleaned_v']),

    metFilterNames = cms.vstring([
        "Flag_goodVertices",
        "Flag_globalTightHalo2016Filter",
        "Flag_HBHENoiseFilter",
        "Flag_HBHENoiseIsoFilter",
        "Flag_EcalDeadCellTriggerPrimitiveFilter",
        "Flag_BadPFMuonFilter",
        "Flag_globalTightHalo2016Filter",
        "Flag_globalSuperTightHalo2016Filter"]),

    minGenParticlePt = cms.double(-1),
    minTrackPt       = cms.double(20.0),
    maxRelTrackIso   = cms.double(-1.0),

    dataTakingPeriod = cms.string("2017")
)
process.trackImageProducerPath = cms.Path(process.trackImageProducer)

process.MINIAODSIMoutput.outputCommands = cms.untracked.vstring('drop *')

process.isolatedTracks.saveDeDxHitInfoCut = cms.string("pt > 1.")
# Path and EndPath definitions
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_BadPFMuonDzFilter = cms.Path(process.BadPFMuonDzFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_hfNoisyHitsFilter = cms.Path(process.hfNoisyHitsFilter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

process.deepSetElectronVarProducerPath = cms.Path(process.deepSetElectronVarProducer)
process.FakeTrackVarProducerPath = cms.Path(process.fakeTrackVarProducer)
process.tensorflowPluginPath = cms.Path(process.tensorflowPlugin)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,
				process.Flag_HBHENoiseIsoFilter,
				process.Flag_CSCTightHaloFilter,
				process.Flag_CSCTightHaloTrkMuUnvetoFilter,
				process.Flag_CSCTightHalo2015Filter,
				process.Flag_globalTightHalo2016Filter,
				process.Flag_globalSuperTightHalo2016Filter,
				process.Flag_HcalStripHaloFilter,
				process.Flag_hcalLaserEventFilter,
				process.Flag_EcalDeadCellTriggerPrimitiveFilter,
				process.Flag_EcalDeadCellBoundaryEnergyFilter,
				process.Flag_ecalBadCalibFilter,
				process.Flag_goodVertices,
				process.Flag_eeBadScFilter,
				process.Flag_ecalLaserCorrFilter,
				process.Flag_trkPOGFilters,
				process.Flag_chargedHadronTrackResolutionFilter,
				process.Flag_muonBadTrackFilter,
				process.Flag_BadChargedCandidateFilter,
				process.Flag_BadPFMuonFilter,
				process.Flag_BadPFMuonDzFilter,
				process.Flag_hfNoisyHitsFilter,
				process.Flag_BadChargedCandidateSummer16Filter,
				process.Flag_BadPFMuonSummer16Filter,
				process.Flag_trkPOG_manystripclus53X,
				process.Flag_trkPOG_toomanystripclus53X,
				process.Flag_trkPOG_logErrorTooManyClusters,
				process.Flag_METFilters,
				process.candidateTracks,
				#process.tensorflowPluginPath,
				#process.deepSetElectronVarProducerPath,
                                process.FakeTrackVarProducerPath,
				process.endjob_step,
				process.MINIAODSIMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 4
process.options.numberOfStreams = 0
process.options.numberOfConcurrentLuminosityBlocks = 2
process.options.eventSetup.numberOfConcurrentIOVs = 1
if hasattr(process, 'DQMStore'): process.DQMStore.assertLegacySafe=cms.untracked.bool(False)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
