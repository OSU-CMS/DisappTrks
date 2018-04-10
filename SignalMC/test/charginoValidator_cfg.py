import FWCore.ParameterSet.Config as cms
import glob, sys

dirName = sys.argv[2]
fileName = sys.argv[3]

print "processing \"" + dirName + "/*.root\"..."
print "writing histograms to \"" + fileName + "\""

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
        map (lambda a : "file:" + a, glob.glob (dirName + "/*.root"))
    ),
)
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string (fileName)
)

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.charginoValidator = cms.EDAnalyzer ("CharginoValidator",
    tracks = cms.InputTag ("generalTracks", ""),
    #genParticles = cms.InputTag ("genParticlePlusGeant", ""),
    genParticles = cms.InputTag ("genParticles", ""),
    cutPythia8Flag = cms.untracked.bool (True), # genParticle.fromHardProcessBeforeFSR()
)

process.myPath = cms.Path (process.charginoValidator)
