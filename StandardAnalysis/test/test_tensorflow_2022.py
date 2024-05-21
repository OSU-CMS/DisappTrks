# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: REMINIAOD -s PAT --runUnscheduled --nThreads 4 --data --era Run2_2018 --scenario pp --conditions 102X_dataRun2_Sep2018Rereco_v1 --eventcontent MINIAOD --datatier MINIAOD --filein file:pippo.root -n 100 --python_filename=treeMaker_real2018_cfg.py --no_exec
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
import os

# get the data/ directory
thisdir = os.path.dirname(os.path.abspath("__file__"))
datadir = os.path.join(os.path.dirname(thisdir), "test")

process = cms.Process('PAT',eras.Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PAT_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring("file:/store/user/mcarrigan/DisappTrks/EGamma_2022F/EGamma_2022F/NoCuts/skim_0.root"),
    fileNames = cms.untracked.vstring("file:/home/mcarrigan/scratch0/disTracksML/CMSSW_12_4_11_patch3/src/DisappTrks/StandardAnalysis/test/skim_1.root"),
)

'''process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('images.root')
)'''

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('REMINIAOD nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAOD'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('REMINIAOD_PAT.root'),
    outputCommands = process.MINIAODEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(cms.untracked.PSet(
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
        #cms.untracked.PSet(
        #    branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedESRecHits_*'),
        #    splitLevel = cms.untracked.int32(99)
        #)
    ),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '124X_dataRun3_Prompt_v4', '')

#process.load('DisappTrks.CandidateTrackProducer.CandidateTrackProducer_cfi')
#process.candidateTracks = cms.Path(process.candidateTrackProducer)
#from DisappTrks.CandidateTrackProducer.customize import disappTrksOutputCommands
#process.MINIAODoutput.outputCommands.extend(disappTrksOutputCommands)

'''process.trackImageProducer = cms.EDAnalyzer ("TrackImageProducerMINIAOD",
    triggers       = cms.InputTag("TriggerResults", "", "HLT"),
    triggerObjects = cms.InputTag("slimmedPatTrigger"),
    tracks         = cms.InputTag("isolatedTracks"),
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
    #ESRecHits     =  cms.InputTag("reducedEcalRecHitsES"),
    HBHERecHits   =  cms.InputTag("reducedHcalRecHits", "hbhereco"),
    #CSCSegments   =  cms.InputTag("cscSegments"),
    #DTRecSegments =  cms.InputTag("dt4DSegments"),
    #RPCRecHits    =  cms.InputTag("rpcRecHits"),

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

    minGenParticlePt = cms.double(10.0),
    minTrackPt       = cms.double(25.0),
    maxRelTrackIso   = cms.double(-1.0),
    maxTrackEta = cms.double(2.1,),

    dataTakingPeriod = cms.string("2022")
)
process.trackImageProducerPath = cms.Path(process.trackImageProducer)'''

# setup tensorflowProducer by loading the auto-generated cfi (see tensorflowProducer.fillDescriptions)
process.load("DisappTrks.StandardAnalysis.tensorflowProducer_cfi")
#process.tensorflowProducer.graphPath = cms.string(os.path.join(datadir, "graph.pb")
process.tensorflowProducer.graphPath = cms.string(os.path.join(datadir, "graph_oct25.pb"))
process.tensorflowProducer.inputTensorName = cms.string("Input_input")
process.tensorflowProducer.outputTensorName = cms.string("sequential/Output_xyz/Sigmoid")

process.tensorflowProducer.graphPathDS = cms.string(os.path.join(datadir, "graph_electron.pb"))
process.tensorflowProducer.inputTensorNameDS = cms.string("input")
process.tensorflowProducer.inputTrackTensorNameDS = cms.string("input_track")
process.tensorflowProducer.outputTensorNameDS = cms.string("model_1/output_xyz/Softmax")

process.tensorflowProducer.triggers = cms.InputTag("TriggerResults", "", "HLT")
process.tensorflowProducer.triggerObjects = cms.InputTag("slimmedPatTrigger")
process.tensorflowProducer.genParticles = cms.InputTag("prunedGenParticles", "")
process.tensorflowProducer.met = cms.InputTag("slimmedMETs")
process.tensorflowProducer.electrons = cms.InputTag("slimmedElectrons", "")
process.tensorflowProducer.muons = cms.InputTag("slimmedMuons", "")
process.tensorflowProducer.taus = cms.InputTag("slimmedTaus", "")
process.tensorflowProducer.pfCandidates = cms.InputTag("packedPFCandidates", "")
process.tensorflowProducer.vertices = cms.InputTag("offlineSlimmedPrimaryVertices", "")
process.tensorflowProducer.jets = cms.InputTag("slimmedJets", "")

process.tensorflowProducer.rhoCentralCalo = cms.InputTag("fixedGridRhoFastjetCentralCalo")

process.tensorflowProducer.EBRecHits = cms.InputTag("reducedEcalRecHitsEB")
process.tensorflowProducer.EERecHits = cms.InputTag("reducedEcalRecHitsEE")
#process.tensorflowProducer.ESRecHits = cms.InputTag("reducedEcalRecHitsES")
process.tensorflowProducer.HBHERecHits = cms.InputTag("reducedHcalRecHits", "hbhereco")
#process.tensorflowProducer.CSCSegments = cms.InputTag("cscSegments")
#process.tensorflowProducer.DTRecSegments = cms.InputTag("dt4DSegments")
#process.tensorflowProducer.RPCRecHits = cms.InputTag("rpcRecHits")

process.tensorflowProducer.dEdxPixel = cms.InputTag ("dedxPixelHarmonic2", "")
process.tensorflowProducer.dEdxStrip = cms.InputTag ("dedxHarmonic2", "")
process.tensorflowProducer.isolatedTracks = cms.InputTag("isolatedTracks", "")
process.tensorflowProducer.isoTrk2dedxHitInfo = cms.InputTag("isolatedTracks", "")
#process.tensorflowProducer.genTracks = cms.InputTag("generalTracks", "")
process.tensorflowProducer.pileupInfo = cms.InputTag ("addPileupInfo")

process.tensorflowProducer.minTrackPt = cms.double(20.0)
process.tensorflowProducer.minGenParticlePt = cms.double(-1)
process.tensorflowProducer.maxRelTrackIso = cms.double(-1)
process.tensorflowProducer.dataTakingPeriod = cms.string("2022")
process.tensorflowProducer.etaRangeNearTrack = cms.double(-1)
process.tensorflowProducer.phiRangeNearTrack = cms.double(-1)
process.tensorflowProducer.maxNumOfRecHits = cms.int32(-1)
process.tensorflowProducer.signalTriggerNames = cms.vstring([
        'HLT_MET105_IsoTrk50_v',
        'HLT_PFMET120_PFMHT120_IDTight_v',
        'HLT_PFMET130_PFMHT130_IDTight_v',
        'HLT_PFMET140_PFMHT140_IDTight_v',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
        'HLT_PFMET250_HBHECleaned_v',
        'HLT_PFMET300_HBHECleaned_v'])
process.tensorflowProducer.metFilterNames = cms.vstring([
        "Flag_goodVertices",
        "Flag_globalTightHalo2016Filter",
        "Flag_HBHENoiseFilter",
        "Flag_HBHENoiseIsoFilter",
        "Flag_EcalDeadCellTriggerPrimitiveFilter",
        "Flag_BadPFMuonFilter",
        "Flag_globalTightHalo2016Filter",
        "Flag_globalSuperTightHalo2016Filter"])

process.tensorflowPluginPath = cms.Path(process.tensorflowProducer)


#process.load("DisappTrks.StandardAnalysis.testMETProducer_cfi")
#process.testMETProducer.graphPath = cms.string(os.path.join(datadir, "graph.pb"))
#process.testMETProducer.inputTensorName = cms.string("Input_input")
#process.testMETProducer.outputTensorName = cms.string("sequential/Output/Sigmoid")
'''
process.testMETProducer.triggers = cms.InputTag("TriggerResults", "", "HLT")
process.testMETProducer.triggerObjects = cms.InputTag("slimmedPatTrigger")
process.testMETProducer.genParticles = cms.InputTag("prunedGenParticles", "")
process.testMETProducer.met = cms.InputTag("slimmedMETs")
process.testMETProducer.electrons = cms.InputTag("slimmedElectrons", "")
process.testMETProducer.muons = cms.InputTag("slimmedMuons", "")
process.testMETProducer.taus = cms.InputTag("slimmedTaus", "")
process.testMETProducer.pfCandidates = cms.InputTag("packedPFCandidates", "")
process.testMETProducer.vertices = cms.InputTag("offlineSlimmedPrimaryVertices", "")
process.testMETProducer.jets = cms.InputTag("slimmedJets", "")
'''
#process.testMETPluginPath = cms.Path(process.testMETProducer)


'''process.load("DisappTrks.StandardAnalysis.fakeTrackVarProducer_cfi")
process.fakeTrackVarProducer.graphPath = cms.string(os.path.join(datadir, "graph.pb"))
process.fakeTrackVarProducer.inputTensorName = cms.string("Input_input")
process.fakeTrackVarProducer.outputTensorName = cms.string("Identity")
process.fakeTrackVarProducer.triggers = cms.InputTag("TriggerResults", "", "HLT")
process.fakeTrackVarProducer.triggerObjects = cms.InputTag("slimmedPatTrigger")
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
#process.fakeTrackVarProducer.ESRecHits = cms.InputTag("reducedEcalRecHitsES")
process.fakeTrackVarProducer.HBHERecHits = cms.InputTag("reducedHcalRecHits", "hbhereco")
#process.fakeTrackVarProducer.CSCSegments = cms.InputTag("cscSegments")
#process.fakeTrackVarProducer.DTRecSegments = cms.InputTag("dt4DSegments")
#process.fakeTrackVarProducer.RPCRecHits = cms.InputTag("rpcRecHits")

process.fakeTrackVarProducer.dEdxPixel = cms.InputTag ("dedxPixelHarmonic2", "")
process.fakeTrackVarProducer.dEdxStrip = cms.InputTag ("dedxHarmonic2", "")
process.fakeTrackVarProducer.isolatedTracks = cms.InputTag("isolatedTracks", "")
process.fakeTrackVarProducer.isoTrk2dedxHitInfo = cms.InputTag("isolatedTracks", "")
#process.fakeTrackVarProducer.genTracks = cms.InputTag("generalTracks", "")
process.fakeTrackVarProducer.pileupInfo = cms.InputTag ("addPileupInfo")

process.fakeTrackVarProducer.minTrackPt = cms.double(20.0)
process.fakeTrackVarProducer.minGenParticlePt = cms.double(-1)
process.fakeTrackVarProducer.maxRelTrackIso = cms.double(-1)
process.fakeTrackVarProducer.dataTakingPeriod = cms.string("2022")
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

#process.deepSetElectronVarProducerPath = cms.Path(process.deepSetElectronVarProducer)

process.FakeTrackVarProducerPath = cms.Path(process.fakeTrackVarProducer)'''

process.MINIAODoutput.outputCommands = cms.untracked.vstring('keep networkScores_*_*_*',
                                                             'keep NetworkOutput_*_*_*',
                                                             'keep *')

process.isolatedTracks.saveDeDxHitInfoCut = cms.string("pt > 1.")

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODoutput_step = cms.EndPath(process.MINIAODoutput)

# Schedule definition

'''process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,
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
				process.Flag_BadChargedCandidateSummer16Filter,
				process.Flag_BadPFMuonSummer16Filter,
				process.Flag_trkPOG_manystripclus53X,
				process.Flag_trkPOG_toomanystripclus53X,
				process.Flag_trkPOG_logErrorTooManyClusters,
				process.Flag_METFilters,
				#process.trackImageProducerPath,
				process.tensorflowPluginPath,
				process.endjob_step,
				process.MINIAODoutput_step)'''


process.schedule = cms.Schedule(process.tensorflowPluginPath, process.endjob_step, process.MINIAODoutput_step)

#process.schedule.associate(process.patTask)
#from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
#associatePatAlgosToolsTask(process)


#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks = 1

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllData 

#call to customisation function miniAOD_customizeAllData imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllData(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
