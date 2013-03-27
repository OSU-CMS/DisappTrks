# Use to run a quick condor job, e.g., to get the number of events.  
#
# Usage:
# > cmsRun trackAnalyzerLxplus_cfg.py 2>&1 | tee trackAnalyzerLxplus_cfg.log 

import FWCore.ParameterSet.Config as cms
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *

process.source.fileNames = cms.untracked.vstring ()
process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')  
#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/WJetsToLNu_TuneZ2Star_8TeV/pat2bean_53x_10_1_80n.root')  


##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *
process.OSUAnalysis.channels = cms.VPSet()  
process.OSUAnalysis.channels.append(PreSelection)
process.OSUAnalysis.channels.append(PreSelectionPMissing)
process.OSUAnalysis.channels.append(PreSelectionPMissingElectronId)
process.OSUAnalysis.channels.append(PreSelectionPMissingPionId)
process.OSUAnalysis.channels.append(PreSelectionPMissingNotGenMatched)
#process.OSUAnalysis.channels.append(ZtoMuMu)


#import the desired sets of histograms from the standard python file which defines them

#import user-defined histograms
from DisappTrksT3ANTemp.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  
from OSUT3Analysis.Configuration.histogramDefinitions import *
process.OSUAnalysis.histogramSets = cms.VPSet()  
process.OSUAnalysis.histogramSets.append(ShortTrackHistograms)
process.OSUAnalysis.histogramSets.append(TestTrackHistograms)
process.OSUAnalysis.histogramSets.append(TestEventHistograms)



# Change other settings as desired
#process.OSUAnalysis.printEventInfo = cms.bool(True)  




