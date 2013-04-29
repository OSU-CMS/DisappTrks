# Use to run a quick condor job, e.g., to get the number of events.  
#
# Usage:
# > cmsRun trackAnalyzerLxplus_cfg.py 2>&1 | tee trackAnalyzerLxplus_cfg.log 

import FWCore.ParameterSet.Config as cms
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *

## process.source.fileNames = cms.untracked.vstring ()
## process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')  
process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/WJetsToLNu_TuneZ2Star_8TeV/pat2bean_53x_154_2_DeK.root')  


## process.source = cms.Source ('PoolSource',
##     fileNames = cms.untracked.vstring ()
## )
## dir = '/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/sigMCBEANs/SigMC_LL01_mGrav50K_1ns/'  
## for file in os.listdir(dir):
##     if file.find(".root") != -1:  # Skip over files that do not contain .root.  
##         process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))    

## process.OSUAnalysis.dataset     = cms.string ('AMSB_mGrav50K_1ns_Reco')
## process.OSUAnalysis.doPileupReweighting = cms.bool(True)
## process.OSUAnalysis.datasetType = cms.string ('signalMC')




##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *
process.OSUAnalysis.channels = cms.VPSet()  
process.OSUAnalysis.channels.append(NoCuts)


## process.OSUAnalysis.channels.append(PreSelNoTrigNoDzNotGenMatched)
## process.OSUAnalysis.channels.append(PreSelNoTrigNoD0NotGenMatched)
## process.OSUAnalysis.channels.append(PreSelNoTrigPMissingNotGenMatched)  

process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMetSigRegBlind)  
process.OSUAnalysis.channels.append(PreSelectionPMissingWithTrigJetMetSigRegBlind)  

## process.OSUAnalysis.channels.append(PreSelection)
## ## process.OSUAnalysis.channels.append(PreSelectionPMissing)
## process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMet)  

## process.OSUAnalysis.channels.append(PreSelectionPMissingLtMesonId)  
## process.OSUAnalysis.channels.append(PreSelectionPMissingKMesonId)  
## process.OSUAnalysis.channels.append(PreSelectionPMissingLtBaryonId)  
## process.OSUAnalysis.channels.append(PreSelectionPMissingKBaryonId)  

## process.OSUAnalysis.channels.append(PreSelectionCharginoId)  
## process.OSUAnalysis.channels.append(PreSelectionPMissingD0Side)
## process.OSUAnalysis.channels.append(PreSelectionPMissingDzSide)


## process.OSUAnalysis.channels.append(PreSelectionPMissingElectronId)
## process.OSUAnalysis.channels.append(PreSelectionPMissingPionId)
## process.OSUAnalysis.channels.append(PreSelectionPMissingNotGenMatched)
#process.OSUAnalysis.channels.append(ZtoMuMu)

## process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorr)
## process.OSUAnalysis.channels.append(SigRegWithTrigJetMetPUCorr)  


#import the desired sets of histograms from the standard python file which defines them

#import user-defined histograms
from DisappTrksT3ANTemp.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  
from OSUT3Analysis.Configuration.histogramDefinitions import *
process.OSUAnalysis.histogramSets = cms.VPSet()  
#process.OSUAnalysis.histogramSets.append(ShortTrackHistograms)
#process.OSUAnalysis.histogramSets.append(TestTrackHistograms)
#process.OSUAnalysis.histogramSets.append(TestEventHistograms)
process.OSUAnalysis.histogramSets.append(TestTrackEventHistograms)
process.OSUAnalysis.histogramSets.append(ExtraTrackHistograms)


process.maxEvents.input = 1000
#process.MessageLogger.cerr.FwkReport.reportEvery = 1


# Change other settings as desired
#process.OSUAnalysis.printEventInfo = cms.bool(True)  

#process.OSUAnalysis.doPileupReweighting = cms.bool(True)
#process.OSUAnalysis.puFile = cms.string (os.environ['CMSSW_BASE']+'/src/OSUT3Analysis/Configuration/data/pu_disappTrks.root')




