import FWCore.ParameterSet.Config as cms
from OSUT3Analysis.Configuration.processingUtilities import *
import math
import os

################################################################################
##### Set up the 'process' object ##############################################
################################################################################

process = cms.Process ('OSUAnalysis')

# how often to print a log message
process.load ('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# input source when running interactively
# ---------------------------------------
process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring (
#                                 "file:/store/user/ahart/AMSB_chargino500GeV_ctau100cm_step4.root"
                                 "file:/home/wulsin/disappTrksRun2/signalDigiReco/CMSSW_7_4_5_ROOT5/src/DisappTrks/CandidateTrackProducer/test/miniAODWithCandidateTracks.root" 
#                                 "file:/data/users/wulsin/OSUT3AnalysisTutorial/DisplacedSUSY_StopToBL_M-1000_CTau-100_13TeV_MiniAOD_numEvent1000.root", # a local copy of the xrootd file on the next line
                                 # "root://cmsxrootd.fnal.gov///store/mc/RunIISpring15DR74/DisplacedSUSY_StopToBL_M-1000_CTau-100_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/70000/02737839-2108-E511-AE42-0CC47A0107D0.root", 
                             ),
)

# FIXME:  set_input does not work (because of error with /usr/bin/file) in CMSSW_7_4_5_ROOT5   
# argument can be a ROOT file, directory, or dataset name*
# *registered dataset names are listed in 'datasets' in:
#    https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Configuration/python/configurationOptions.py

# sample direcotory
# set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/")

# sample ROOT file
#set_input(process, "/store/user/ahart/BN_stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_1/stopToBottom_M_800_10mm_Tune4C_8TeV_pythia8_lantonel-Summer12_DR53X-PU_S10_START53_V19-v1-ab45720b22c4f98257a2f100c39d504b_USER_10_2_Dzw.root")

# sample dataset nickname
#set_input(process, "DYToTauTau_20")
#set_input(process, "DYToMuMu_20")

# output histogram file name when running interactively
process.TFileService = cms.Service ('TFileService',
    fileName = cms.string ('hist.root')
)

# number of events to process when running interactively
process.maxEvents = cms.untracked.PSet (
    input = cms.untracked.int32 (1000)
)

################################################################################
##### Set up the 'collections' map #############################################
################################################################################

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import collectionMap  # miniAOD

collectionMap.tracks = cms.InputTag ('generalTracks') 

################################################################################
##### Set up any user-defined variable producers ###############################
################################################################################

variableProducers = []
#variableProducers.append("MyVariableProducer")

################################################################################
##### Import the channels to be run ############################################
################################################################################

from DisappTrks.StandardAnalysis.EventSelections import *

################################################################################
##### Import the histograms to be plotted ######################################
################################################################################

from DisappTrks.StandardAnalysis.MyHistogramDefinitions_disappTrks import *

################################################################################
##### Attach the channels and histograms to the process ########################
################################################################################

add_channels (process, [disTrkSelection], cms.VPSet (histograms), collectionMap, variableProducers, False)

# uncomment to produce a full python configuration log file
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()
