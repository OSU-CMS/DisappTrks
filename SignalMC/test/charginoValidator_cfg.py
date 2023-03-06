import FWCore.ParameterSet.Config as cms
import glob, sys, os

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('CHARGINO')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        'file:/data/users/borzari/condor/SignalMC/Run3/2022/step3/1000cm/700GeV/AMSB_chargino_M_700GeV_CTau_1000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/hist_4.root'
    ),
)

process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('outputFile.root')
)

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.charginoValidator = cms.EDAnalyzer ("CharginoValidator",
    tracks = cms.InputTag ("generalTracks", ""),
    #genParticles = cms.InputTag ("genParticlePlusGeant", ""),
    pfmet = cms.InputTag ("pfMet", ""),
    genParticles = cms.InputTag ("genParticles", ""),
    #pileupInfo = cms.InputTag ("addPileupInfo"),
    genMets = cms.InputTag ("genMetTrue"),
    muonsCol = cms.InputTag ("muons", ""),
    cutPythia8Flag = cms.untracked.bool (True), # genParticle.fromHardProcessBeforeFSR()
)

process.myPath = cms.Path (process.charginoValidator)
