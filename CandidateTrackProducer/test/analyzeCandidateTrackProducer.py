import FWCore.ParameterSet.Config as cms
import sys

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('CANDTRK')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1

#output file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string (
        'file:candidateTrackANPlots.root',
    )
)
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

with open('SkimList_700GeV_100cm.txt','r') as file:
     filenames = [line.replace("\n","") for line in file]

with open('MiniAODList_700GeV_100cm.txt','r') as file:
     secondaryfilenames = [line.replace("\n","") for line in file]

print(filenames)
print(secondaryfilenames)

process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        # "file:/data/users/borzari/condor/SignalMC/Run3/2022/Cutflows_AMSB_700_100_candidateTracksNoSkimming_candTrkSelection/CandTrkSelection/skim_402.root",
        filenames
    ),
    secondaryFileNames = cms.untracked.vstring (
        # "file:/data/users/borzari/condor/SignalMC/Run3/2022/step4/CandidateTrackProducerNoSkimming/100cm/700GeV/hist_463.root",
        secondaryfilenames
    )
)

###########################################################
##### Set up the analyzer #####
###########################################################

process.CandidateTrackProducerAnalyzer = cms.EDAnalyzer("CandidateTrackProducerAnalyzer",
  candTrk = cms.InputTag("candidateTrackProducer"),
)
process.myPath = cms.Path(process.CandidateTrackProducerAnalyzer)
