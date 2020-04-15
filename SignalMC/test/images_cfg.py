import FWCore.ParameterSet.Config as cms
import glob, sys, os

# The following are needed for the calculation of associated calorimeter energy
from Configuration.StandardSequences.GeometryRecoDB_cff import *
from Configuration.StandardSequences.MagneticField_38T_cff import *

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

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v11', '')

process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (100)
)
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring (
        map (lambda a : "file:" + a, [f for f in glob.glob (dirName + "/*.root") if os.path.getsize(f) != 0])
    ),
)
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string (fileName)
)

###########################################################
##### Set up the producer and the end path            #####
###########################################################

process.charginoImageAnalyzer = cms.EDAnalyzer ("CharginoImageAnalyzer",
    genParticles = cms.InputTag ("genParticles", ""),
    EBRecHits          =  cms.InputTag  ("reducedEcalRecHitsEB"),
    EERecHits          =  cms.InputTag  ("reducedEcalRecHitsEE"),
    HBHERecHits        =  cms.InputTag  ("reducedHcalRecHits", "hbhereco"),
    x_lo = cms.double (-1.6),
    x_hi = cms.double (1.6),
    n_x = cms.int32 (32),
    y_lo = cms.double (-1.6),
    y_hi = cms.double (1.6),
    n_y = cms.int32 (32),
)

process.myPath = cms.Path (process.charginoImageAnalyzer)