# Use to run a quick condor job, e.g., to get the number of events.  
#
# Usage:
# > cmsRun trackAnalyzerLxplus_cfg.py 2>&1 | tee trackAnalyzerLxplus_cfg.log 

import FWCore.ParameterSet.Config as cms
import trackAnalyzer_cfg as pset

pset.process.source.fileNames = cms.untracked.vstring ()
pset.process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')


##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *
pset.process.OSUAnalysis.channels = cms.VPSet()  
pset.process.OSUAnalysis.channels.append(PreSelection)


# Run the job.
process = pset.process
                 
