# Usage:
# > cmsRun trackAnalyzerTruthStudies_cfg.py 2>&1 | tee trackAnalyzerTruthStudies_cfg.log 

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *

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
process.OSUAnalysis.channels.append(PreSelectionElectronId)
process.OSUAnalysis.channels.append(PreSelectionPionId)
process.OSUAnalysis.channels.append(PreSelectionNotGenMatched)
pset.process.OSUAnalysis.channels.append(PreSelectionPMissing)
pset.process.OSUAnalysis.channels.append(PreSelectionPMissingElectronId)
pset.process.OSUAnalysis.channels.append(PreSelectionPMissingPionId)
pset.process.OSUAnalysis.channels.append(PreSelectionPMissingNotGenMatched)
