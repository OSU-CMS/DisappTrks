# Usage:
# > cmsRun trackAnalyzerCtrlSamp_cfg.py 2>&1 | tee trackAnalyzerCtrlSamp_cfg.log 

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *


#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
process.source.fileNames.append('file:/mnt/hadoop/mc/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_DISPLACED_LEPTON-v3/bean_989_1_ACv.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_DISPLACED_LEPTON-v3/bean_4514_1_Jov.root')
process.maxEvents.input = 1000

process.OSUAnalysis.useTrackCaloRhoCorr = cms.bool(False)

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

#from DisappTrksT3ANTemp.StandardAnalysis.MyCtrlSampleSelections_disappTrks import *
from DisappTrksT3ANTemp.StandardAnalysis.MyElectronCtrlSampleSelections_disappTrks import *
process.OSUAnalysis.channels.append(ZtoEE)  
process.OSUAnalysis.channels.append(ZtoETrackPreSel)  
process.OSUAnalysis.channels.append(ZtoETrackFullPreSel)

from DisappTrksT3ANTemp.StandardAnalysis.MyMuonCtrlSampleSelections_disappTrks import *
process.OSUAnalysis.channels.append(ZtoMuMu)
process.OSUAnalysis.channels.append(ZtoMuTrackPreSel)
process.OSUAnalysis.channels.append(ZtoMuTrackFullPreSel)

from DisappTrksT3ANTemp.StandardAnalysis.MyTauCtrlSampleSelections_disappTrks import *
process.OSUAnalysis.channels.append(ZtoTauTau)
process.OSUAnalysis.channels.append(ZtoMuTau)
process.OSUAnalysis.channels.append(ZtoTauTrackPreSel)
process.OSUAnalysis.channels.append(ZtoTauTrackFullPreSel)



