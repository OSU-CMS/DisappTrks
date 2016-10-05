import FWCore.ParameterSet.Config as cms
import sys
import os

prefix = 'eff'
doSkim = False

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('TRIGGER')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string (
        "triggerEfficiency.root",
    )
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "/store/user/ahart/" + prefix + ".root"
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
  electrons       =  cms.InputTag  ("slimmedElectrons",               ""),
  genjets         =  cms.InputTag  ("slimmedGenJets",                 ""),
  genparticles    =  cms.InputTag  ("prunedGenParticles",             ""),
  jets            =  cms.InputTag  ("slimmedJets",                    ""),
  mcparticles     =  cms.InputTag  ("packedGenParticles",             ""),
  mets            =  cms.InputTag  ("slimmedMETs",                    ""),
  muons           =  cms.InputTag  ("slimmedMuons",                   ""),
  photons         =  cms.InputTag  ("slimmedPhotons",                 ""),
  primaryvertexs  =  cms.InputTag  ("offlineSlimmedPrimaryVertices",  ""),
  superclusters   =  cms.InputTag  ("reducedEgamma",                  "reducedSuperClusters"),
  taus            =  cms.InputTag  ("slimmedTaus",                    ""),
  tracks          =  cms.InputTag  ("generalTracks",                  ""),
  triggers        =  cms.InputTag  ("TriggerResults",                 "",                       "HLT"),
  trigobjs        =  cms.InputTag  ("selectedPatTrigger",             ""),
)

process.TriggerEfficiency = cms.EDFilter ("TriggerEfficiencyWithMuons",
  matchToHLTTrack  =  cms.bool (True),
  isMC             =  cms.bool (False),
  mets             =  collections.MiniAOD.mets,
  muons            =  collections.MiniAOD.muons,
  tracks           =  collections.MiniAOD.muons,
  triggerBits      =  collections.MiniAOD.triggers,
  triggerObjs      =  collections.MiniAOD.trigobjs,
  vertices         =  collections.MiniAOD.primaryvertexs,
  genParticles     =  collections.MiniAOD.genparticles,
  jets             =  collections.MiniAOD.jets,
)

if not process.TriggerEfficiency.isMC:
  import FWCore.PythonUtilities.LumiList as LumiList
  import FWCore.ParameterSet.Types as CfgTypes
  myLumis = LumiList.LumiList(filename = os.environ['CMSSW_BASE']+'/src/DisappTrks/TriggerAnalysis/test/Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2.txt').getCMSSWString().split(',')
  process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
  process.source.lumisToProcess.extend(myLumis)

process.myPath = cms.Path (process.TriggerEfficiency)

if doSkim:
  print "creating skim..."
  process.load('Configuration.EventContent.EventContent_cff')
  process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
      compressionAlgorithm = cms.untracked.string('LZMA'),
      compressionLevel = cms.untracked.int32(4),
      dataset = cms.untracked.PSet(
          dataTier = cms.untracked.string('MINIAODSIM'),
          filterName = cms.untracked.string('')
      ),
      dropMetaData = cms.untracked.string('ALL'),
      eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
      fastCloning = cms.untracked.bool(False),
      fileName = cms.untracked.string(prefix + '_skim.root'),
      outputCommands = process.MINIAODSIMEventContent.outputCommands,
      overrideInputFileSplitLevels = cms.untracked.bool(True),
      SelectEvents = cms.untracked.PSet (
        SelectEvents = cms.vstring ("myPath")
      )
  )
  process.myEndPath = cms.EndPath (process.MINIAODSIMoutput)
