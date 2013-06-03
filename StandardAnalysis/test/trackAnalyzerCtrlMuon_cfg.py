# Usage:
# > cmsRun trackAnalyzerCtrlMuon_cfg.py 2>&1 | tee trackAnalyzerCtrlMuon_cfg.log 

from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *


#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_DISPLACED_LEPTON-v3/bean_989_1_ACv.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_DISPLACED_LEPTON-v3/bean_4514_1_Jov.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/WJetsToLNu_TuneZ2Star_8TeV/pat2bean_53x_154_2_DeK.root')
process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/DYJetsToLL/pat2bean_53x_100_1_2KD.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/abrinke1/SingleElectron/SingleElectron_Run2012A-13Jul2012-v1_BEAN_53xOn53x_V02_CV01/4da6952f3c4fba5e66dcec676ef9c024//ttH_pat2bean_53x_110_1_kpZ.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SingleElec_Reco_P1//pat2bean_53x_102_1_CCH.root')


process.OSUAnalysis.useTrackCaloRhoCorr = cms.bool(False)
process.OSUAnalysis.applyLeptonSF       = cms.bool(True)

process.OSUAnalysis.histogramSets.append(MuonHistograms)


from DisappTrksT3ANTemp.StandardAnalysis.MyDisappTrkBranchSets import *
process.OSUAnalysis.treeBranchSets = AllSlimTreeBranchSets


##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrksT3ANTemp.StandardAnalysis.MyMuonCtrlSampleSelections_disappTrks import *
#process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV1)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2)
## #process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV3)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV4)
process.OSUAnalysis.channels.append(WToMuSimple)  


## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet1)  
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet2)  
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet3) 
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet4)  
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet1BTagVeto)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet2BTagVeto)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet3BTagVeto)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet4BTagVeto)





