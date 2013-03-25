# Use to run a quick condor job, e.g., to get the number of events.  
#
# Usage:
# > cmsRun trackAnalyzerQuick_cfg.py 2>&1 | tee trackAnalyzerQuick_cfg.log 

import FWCore.ParameterSet.Config as cms
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *
##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *
pset.process.OSUAnalysis.channels = cms.VPSet()  
pset.process.OSUAnalysis.channels.append(PreSelection)


# Run the job.
process = pset.process
                 
