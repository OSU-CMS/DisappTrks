# Usage:
# > cmsRun trackAnalyzerCtrlSamp_cfg.py 2>&1 | tee trackAnalyzerCtrlSamp_cfg.log 

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *

########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################
#Histograms for the invariant mass plots
from DisappTrksT3ANTemp.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  
process.OSUAnalysis.histogramSets.append(ExtraMuonHistograms)
process.OSUAnalysis.histogramSets.append(ExtraElectronHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *

# First two channels needed to estimate yields
process.OSUAnalysis.channels.append(SigReg)
process.OSUAnalysis.channels.append(SigRegWithTrigJetMet)
process.OSUAnalysis.channels.append(SigRegWithMaxCalo)

# Other channels used to make plots; exact composition of bkgds may not be correct.   
process.OSUAnalysis.channels.append(PreSelection)
process.OSUAnalysis.channels.append(PreSelectionElectronId)
process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMet)
process.OSUAnalysis.channels.append(FitRegWithMaxCalo)
process.OSUAnalysis.channels.append(ZtoMuMu)
process.OSUAnalysis.channels.append(ZtoEE)  


