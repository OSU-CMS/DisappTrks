# Config file to produce the candidate track collection.
# Similar to candidateTrackProducer_AODInput_cfg.py but uses
# MINIAOD as well as AOD files as input and
# does not run the MINIAOD steps.
#
# Usage:
# To run over data:
# > cmsRun candidateTrackProducer_cfg.py print runOnMC=0

import FWCore.ParameterSet.Config as cms
import os


###########################################################
##### Set up process #####
###########################################################

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.register ('runOnMC',
                  1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Whether jobs will run over MC (1) or data (0)"
              )
options.parseArguments()


process = cms.Process ('DISAPPTRKS')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        "root://cmsxrootd.fnal.gov///store/mc/RunIIFall15MiniAODv2/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/0E84E437-DEBD-E511-8230-00259048A862.root"
    ),
    secondaryFileNames = cms.untracked.vstring (
        "root://cmsxrootd.fnal.gov///store/mc/RunIIFall15DR76/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/72D61EDC-4A8F-E511-A6A9-002590200B6C.root",
        "root://cmsxrootd.fnal.gov///store/mc/RunIIFall15DR76/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/8E851456-518F-E511-B485-001E67397D55.root",
        "root://cmsxrootd.fnal.gov///store/mc/RunIIFall15DR76/WJetsToLNu_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/AODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/CEA474AA-3E8E-E511-BB73-0CC47A78A414.root",
    ),
)

if not options.runOnMC:
    process.source.fileNames = cms.untracked.vstring (
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/MINIAOD/05Oct2015-v1/30000/04F50A91-B46F-E511-A2A3-002618943923.root",
    )
    process.source.secondaryFileNames = cms.untracked.vstring (
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/1A77484B-DB68-E511-AEF6-02163E012456.root",
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/564310C7-F868-E511-BD21-02163E014227.root",
        "root://cmsxrootd.fnal.gov///store/data/Run2015D/MET/AOD/PromptReco-v3/000/257/822/00000/F0519CD5-D868-E511-B0BE-02163E014208.root",
    )

process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
if options.runOnMC:
    process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_v12', '')
else:
    process.GlobalTag = GlobalTag(process.GlobalTag, '76X_dataRun2_v15', '')


###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.load('DisappTrks.CandidateTrackProducer.CandidateTrackProducer_cfi')
process.candidateTracks = cms.Path (process.candidateTrackProducer)

from DisappTrks.CandidateTrackProducer.customize import customizeMiniAODSIMOutput
customizeMiniAODSIMOutput(process)

process.myEndPath = cms.EndPath (process.MINIAODSIMoutput)
