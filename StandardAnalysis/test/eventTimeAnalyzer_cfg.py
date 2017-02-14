import FWCore.ParameterSet.Config as cms
import sys, glob

def filePrefix (fileName):
  return "file:" + fileName

run = sys.argv[2]
listOfFiles = map (filePrefix, glob.glob ("/data/users/hart/condor/2016_final/fakeTrackSkim/SingleMu_2016" + run + "/ZtoMuMuDisTrk/skim_*.root"))
print "processing " + str (len (listOfFiles)) + " files for 2016" + run + "..."

###########################################################
##### Set up process #####
###########################################################

process = cms.Process ('ANA2')
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (-1)
)

process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('eventTime_' + run + '.root')
)

#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_2016SeptRepro_v7', '')

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.eventTimeAnalyzer = cms.EDAnalyzer ("EventTimeAnalyzer")

process.myPath = cms.Path (process.eventTimeAnalyzer)

process.source = cms.Source ("PoolSource",
    bypassVersionCheck = cms.untracked.bool (True),
    skipBadFiles = cms.untracked.bool (True),
    fileNames = cms.untracked.vstring (
        listOfFiles
    ),
)
