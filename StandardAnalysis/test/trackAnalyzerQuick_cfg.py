# Use to run a quick condor job, e.g., to get the number of events.  
#
# Usage:
# > cmsRun trackAnalyzerQuick_cfg.py |& tee trackAnalyzerQuick_cfg.log 



import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *

#uncomment this line to add a single file to be processed
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/WJetsToLNu/pat2bean_53x_10_1_3IZ.root')



##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *
process.OSUAnalysis.channels = cms.VPSet()  
process.OSUAnalysis.channels.append(PreSelection)




                 
