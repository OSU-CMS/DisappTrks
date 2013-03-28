# Usage:
# > cmsRun trackAnalyzerCtrlSamp_cfg.py 2>&1 | tee trackAnalyzerCtrlSamp_cfg.log 

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *


process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
process.maxEvents.input = 1000

########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################
#Histograms for the invariant mass plots
from DisappTrksT3ANTemp.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  
process.OSUAnalysis.histogramSets.append(ExtraMuonHistograms)
process.OSUAnalysis.histogramSets.append(ExtraElectronHistograms)
process.OSUAnalysis.histogramSets.append(ExtraElectronTrackHistograms)
#For pions
process.OSUAnalysis.histogramSets.append(ExtraTauHistograms)
process.OSUAnalysis.histogramSets.append(ExtraMuonTauHistograms)
process.OSUAnalysis.histogramSets.append(ExtraMuonTrackHistograms)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *

# First two channels needed to estimate yields
#process.OSUAnalysis.channels.append(SigReg)
#process.OSUAnalysis.channels.append(SigRegWithTrigJetMet)
#process.OSUAnalysis.channels.append(SigRegWithMaxCalo)

# Other channels used to make plots; exact composition of bkgds may not be correct.   
#process.OSUAnalysis.channels.append(PreSelection)
#process.OSUAnalysis.channels.append(PreSelectionElectronId)
#process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMet)
#process.OSUAnalysis.channels.append(FitRegWithMaxCalo)

from DisappTrksT3ANTemp.StandardAnalysis.MyCtrlSampleSelections_disappTrks import *
process.OSUAnalysis.channels.append(ZtoMuMu)
process.OSUAnalysis.channels.append(ZtoEE)  
process.OSUAnalysis.channels.append(ZtoEEPreSel)  
process.OSUAnalysis.channels.append(ZtoETrackPreSel)  
process.OSUAnalysis.channels.append(ZtoETrackFullPreSel)  
##For pions
process.OSUAnalysis.channels.append(ZtoTauTau)
process.OSUAnalysis.channels.append(ZtoMuTau)
process.OSUAnalysis.channels.append(ZtoMuTrackPreSel)
process.OSUAnalysis.channels.append(ZtoMuTrackFullPreSel)


