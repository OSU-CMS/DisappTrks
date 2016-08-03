import FWCore.ParameterSet.Config as cms
import copy

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('MINIMALSKIM')
process.load('Configuration.EventContent.EventContent_cff')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_1.root',
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_10.root',
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_100.root',
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_101.root',
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_102.root',
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_103.root',
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_104.root',
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_105.root',
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_106.root',
        '/store/user/ahart/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-DisappTrks-v1/160205_142511/0000/miniAODWithCandidateTracks_107.root',
    )
)

###########################################################
##### Set up the analyzer #####
###########################################################

class Collections:
  pass

collections = Collections ()

collections.MiniAOD = cms.PSet (
  beamspots       =  cms.InputTag  ("offlineBeamSpot",                ""),
  caloMets        =  cms.InputTag  ("caloMet",                        ""),
  conversions     =  cms.InputTag  ("reducedEgamma",                  "reducedConversions",          ""),
  electrons       =  cms.InputTag  ("slimmedElectrons",               ""),
  genjets         =  cms.InputTag  ("slimmedGenJets",                 ""),
  genparticles    =  cms.InputTag  ("prunedGenParticles",             ""),
  jets            =  cms.InputTag  ("slimmedJets",                    ""),
  mcparticles     =  cms.InputTag  ("packedGenParticles",             ""),
  mets            =  cms.InputTag  ("slimmedMETs",                    ""),
  muons           =  cms.InputTag  ("slimmedMuons",                   ""),
  photons         =  cms.InputTag  ("slimmedPhotons",                 ""),
  rho             =  cms.InputTag  ("fixedGridRhoFastjetAll",         "",                            ""),
  superclusters   =  cms.InputTag  ("reducedEgamma",                  "reducedSuperClusters"),
  taus            =  cms.InputTag  ("slimmedTaus",                    ""),
  tracks          =  cms.InputTag  ("generalTracks",                  ""),
  triggers        =  cms.InputTag  ("TriggerResults",                 "",                       "HLT"),
  trigobjs        =  cms.InputTag  ("selectedPatTrigger",             ""),
  vertices        =  cms.InputTag  ("offlineSlimmedPrimaryVertices",  ""),
)

process.metSkimFilter = cms.EDFilter ("METSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  triggerNames =  cms.vstring (
    "HLT_MET75_IsoTrk50_v",
    "HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v2",
    "HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v2",
    "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v2",
    "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v2",
  ),
)

process.electronSkimFilter = cms.EDFilter ("ElectronSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  triggerNames =  cms.vstring (
    "HLT_Ele25_eta2p1_WPLoose_Gsf_v",
  ),
)

process.muonSkimFilter = cms.EDFilter ("MuonSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  triggerNames =  cms.vstring (
    "HLT_IsoMu20_v",
    "HLT_IsoTkMu20_v",
  ),
)

process.tauSkimFilter = cms.EDFilter ("TauSkimFilter",
  triggers     =  collections.MiniAOD.triggers,
  beamspot     =  collections.MiniAOD.beamspots,
  vertices     =  collections.MiniAOD.vertices,
  met          =  collections.MiniAOD.mets,
  muons        =  collections.MiniAOD.muons,
  electrons    =  collections.MiniAOD.electrons,
  conversions  =  collections.MiniAOD.conversions,
  taus         =  collections.MiniAOD.taus,
  rho          =  collections.MiniAOD.rho,
  triggerNames =  cms.vstring (
    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v",
  ),
)

process.metSkimPath = cms.Path (process.metSkimFilter)
process.electronSkimPath = cms.Path (process.electronSkimFilter)
process.muonSkimPath = cms.Path (process.muonSkimFilter)
process.tauSkimPath = cms.Path (process.tauSkimFilter)

process.metSkimOutputModule = cms.OutputModule ("PoolOutputModule",
    splitLevel = cms.untracked.int32 (0),
    eventAutoFlushCompressedSize = cms.untracked.int32 (5242880),
    fileName = cms.untracked.string ("metSkim.root"),
    SelectEvents = cms.untracked.PSet (SelectEvents = cms.vstring ("metSkimPath")),
    outputCommands = copy.deepcopy (process.MINIAODSIMEventContent.outputCommands),
    dropMetaData = cms.untracked.string ("ALL")
)
process.metSkimOutputModule.outputCommands.append ("drop CutResults_*_*_*")
process.metSkimOutputModule.outputCommands.append ("keep *_metSkimFilter_*_*")

process.electronSkimOutputModule = cms.OutputModule ("PoolOutputModule",
    splitLevel = cms.untracked.int32 (0),
    eventAutoFlushCompressedSize = cms.untracked.int32 (5242880),
    fileName = cms.untracked.string ("electronSkim.root"),
    SelectEvents = cms.untracked.PSet (SelectEvents = cms.vstring ("electronSkimPath")),
    outputCommands = copy.deepcopy (process.MINIAODSIMEventContent.outputCommands),
    dropMetaData = cms.untracked.string ("ALL")
)
process.electronSkimOutputModule.outputCommands.append ("drop CutResults_*_*_*")
process.electronSkimOutputModule.outputCommands.append ("keep *_electronSkimFilter_*_*")

process.muonSkimOutputModule = cms.OutputModule ("PoolOutputModule",
    splitLevel = cms.untracked.int32 (0),
    eventAutoFlushCompressedSize = cms.untracked.int32 (5242880),
    fileName = cms.untracked.string ("muonSkim.root"),
    SelectEvents = cms.untracked.PSet (SelectEvents = cms.vstring ("muonSkimPath")),
    outputCommands = copy.deepcopy (process.MINIAODSIMEventContent.outputCommands),
    dropMetaData = cms.untracked.string ("ALL")
)
process.muonSkimOutputModule.outputCommands.append ("drop CutResults_*_*_*")
process.muonSkimOutputModule.outputCommands.append ("keep *_muonSkimFilter_*_*")

process.tauSkimOutputModule = cms.OutputModule ("PoolOutputModule",
    splitLevel = cms.untracked.int32 (0),
    eventAutoFlushCompressedSize = cms.untracked.int32 (5242880),
    fileName = cms.untracked.string ("tauSkim.root"),
    SelectEvents = cms.untracked.PSet (SelectEvents = cms.vstring ("tauSkimPath")),
    outputCommands = copy.deepcopy (process.MINIAODSIMEventContent.outputCommands),
    dropMetaData = cms.untracked.string ("ALL")
)
process.tauSkimOutputModule.outputCommands.append ("drop CutResults_*_*_*")
process.tauSkimOutputModule.outputCommands.append ("keep *_tauSkimFilter_*_*")

process.myEndPath = cms.EndPath (process.metSkimOutputModule + process.electronSkimOutputModule + process.muonSkimOutputModule + process.tauSkimOutputModule)
