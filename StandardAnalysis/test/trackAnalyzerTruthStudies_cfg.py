# Usage:
# > cmsRun trackAnalyzerTruthStudies_cfg.py 2>&1 | tee trackAnalyzerTruthStudies_cfg.log 

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *

#uncomment this line to add a single file to be processed
#pset.process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')  
process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/WJetsToLNu_TuneZ2Star_8TeV/pat2bean_53x_10_1_80n.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')



########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################
#Histograms for the invariant mass plots
#from DisappTrksT3ANTemp.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *

# First two channels needed to estimate yields

# Other channels used to make plots; exact composition of bkgds may not be correct.   
pset.process.OSUAnalysis.channels.append(PreSelection)
pset.process.OSUAnalysis.channels.append(PreSelectionElectronId)
pset.process.OSUAnalysis.channels.append(PreSelectionPionId)
pset.process.OSUAnalysis.channels.append(PreSelectionNotGenMatched)
pset.process.OSUAnalysis.channels.append(PreSelectionPMissing)
pset.process.OSUAnalysis.channels.append(PreSelectionPMissingElectronId)
pset.process.OSUAnalysis.channels.append(PreSelectionPMissingPionId)
pset.process.OSUAnalysis.channels.append(PreSelectionPMissingNotGenMatched)
