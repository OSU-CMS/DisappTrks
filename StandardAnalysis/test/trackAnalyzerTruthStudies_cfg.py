# Usage:
# > cmsRun trackAnalyzerTruthStudies_cfg.py 2>&1 | tee trackAnalyzerTruthStudies_cfg.log 

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *

#uncomment this line to add a single file to be processed
#process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')  
#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/WJetsToLNu_TuneZ2Star_8TeV/pat2bean_53x_10_1_80n.root')  
process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')



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
process.OSUAnalysis.channels.append(PreSelection)
process.OSUAnalysis.channels.append(PreSelectionElectronId)
process.OSUAnalysis.channels.append(PreSelectionPionId)
process.OSUAnalysis.channels.append(PreSelectionNotGenMatched)
process.OSUAnalysis.channels.append(PreSelectionPMissing)
process.OSUAnalysis.channels.append(PreSelectionPMissingElectronId)
process.OSUAnalysis.channels.append(PreSelectionPMissingPionId)
process.OSUAnalysis.channels.append(PreSelectionPMissingNotGenMatched)
process.OSUAnalysis.channels.append(PreSelectionPMissingLtMesonId)  
process.OSUAnalysis.channels.append(PreSelectionPMissingKMesonId)  
process.OSUAnalysis.channels.append(PreSelectionPMissingLtBaryonId)  
process.OSUAnalysis.channels.append(PreSelectionPMissingKBaryonId)  


