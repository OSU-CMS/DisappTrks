# Usage:
# > cmsRun trackAnalyzerCtrlSamp_cfg.py 2>&1 | tee trackAnalyzerCtrlSamp_cfg.log 

from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *


#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_DISPLACED_LEPTON-v3/bean_989_1_ACv.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_DISPLACED_LEPTON-v3/bean_4514_1_Jov.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/WJetsToLNu_TuneZ2Star_8TeV/pat2bean_53x_154_2_DeK.root')
process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/DYJetsToLL/pat2bean_53x_100_1_2KD.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/abrinke1/SingleElectron/SingleElectron_Run2012A-13Jul2012-v1_BEAN_53xOn53x_V02_CV01/4da6952f3c4fba5e66dcec676ef9c024//ttH_pat2bean_53x_110_1_kpZ.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SingleElec_Reco_P1//pat2bean_53x_102_1_CCH.root')

process.maxEvents.input = 1000
#process.maxEvents.input = -1
process.MessageLogger.cerr.FwkReport.reportEvery = 100

#process.OSUAnalysis.muons     = cms.InputTag('BNproducer', 'selectedPatMuonsLoosePFlow')
#process.OSUAnalysis.electrons = cms.InputTag('BNproducer', 'selectedPatElectronsLoosePFlow')



process.OSUAnalysis.useTrackCaloRhoCorr = cms.bool(True)
#process.OSUAnalysis.puFile = cms.string (os.environ['CMSSW_BASE']+'/src/OSUT3Analysis/Configuration/data/pu.root')
########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################
from OSUT3Analysis.Configuration.histogramDefinitions import *
#process.OSUAnalysis.histogramSets = cms.VPSet()
#process.OSUAnalysis.histogramSets.append(EventHistograms)
#process.OSUAnalysis.histogramSets.append(TrackHistograms)  
#process.OSUAnalysis.histogramSets.append(MuonHistograms)  # causes a seg fault?  

from DisappTrks.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  
#Histograms for the invariant mass plots
process.OSUAnalysis.histogramSets.append(DiMuonHistograms)
## process.OSUAnalysis.histogramSets.append(DiElectronHistograms)
#process.OSUAnalysis.histogramSets.append(ElectronTrackHistograms)
### #For pions
process.OSUAnalysis.histogramSets.append(DiTauHistograms)
process.OSUAnalysis.histogramSets.append(MuonTauHistograms)
process.OSUAnalysis.histogramSets.append(MuonTrackHistograms)
#process.OSUAnalysis.histogramSets.append(MuonHistograms)  


##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrks.StandardAnalysis.MyElectronCtrlSampleSelections_disappTrks import *
#process.OSUAnalysis.channels.append(ZtoEE)  
#process.OSUAnalysis.channels.append(ZtoETrack)
#process.OSUAnalysis.channels.append(ZtoETrackPreSel)  
#process.OSUAnalysis.channels.append(ZtoETrackFullPreSel)
#process.OSUAnalysis.channels.append(WtoENuTrigElec)  
#process.OSUAnalysis.channels.append(WtoENuTrigMET)  

from DisappTrks.StandardAnalysis.MyMuonCtrlSampleSelections_disappTrks import *
#process.OSUAnalysis.channels.append(ZtoMuMu)
#process.OSUAnalysis.channels.append(ZtoMuTrackPreSel)
#process.OSUAnalysis.channels.append(ZtoMuTrackFullPreSel)
#process.OSUAnalysis.channels.append(WtoMuNuTrackFullPreSel)
#process.OSUAnalysis.channels.append(DebugOnly)

from DisappTrks.StandardAnalysis.MyTauCtrlSampleSelections_disappTrks import *
#process.OSUAnalysis.channels.append(ZtoTauTau)
process.OSUAnalysis.channels.append(ZtoMuTauHad)
#process.OSUAnalysis.channels.append(ZtoTauTrackPreSel)
#process.OSUAnalysis.channels.append(ZtoTauTrackFullPreSel)
#process.OSUAnalysis.channels.append(WtoTauNu)


#process.OSUAnalysis.printEventInfo = cms.bool(True)



