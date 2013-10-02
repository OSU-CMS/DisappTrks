# Usage:
# > cmsRun trackAnalyzerCtrlElec_cfg.py 2>&1 | tee trackAnalyzerCtrlElec_cfg.log 

from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *


#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_DISPLACED_LEPTON-v3/bean_989_1_ACv.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_DISPLACED_LEPTON-v3/bean_4514_1_Jov.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/WJetsToLNu_TuneZ2Star_8TeV/pat2bean_53x_154_2_DeK.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/DYJetsToLL/pat2bean_53x_100_1_2KD.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/abrinke1/SingleElectron/SingleElectron_Run2012A-13Jul2012-v1_BEAN_53xOn53x_V02_CV01/4da6952f3c4fba5e66dcec676ef9c024//ttH_pat2bean_53x_110_1_kpZ.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SingleElec_Reco_P1//pat2bean_53x_102_1_CCH.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SingleMu/Run2012D-PromptReco-v1_BEAN2012-v4/ad2797bf6dcd13ca01c5e72b5465df6c/ttH_pat2bean_53x_240_23_ZnR.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/ZJetsToNuNu_100_HT_200_TuneZ2Star_8TeV_madgraph/BEAN2012-v4/0ff8045eb3a4a7ce9562dd332df0072c/ttH_pat2bean_53x_100_1_hBP.root')
process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SingleElectron/BEAN2012-v4/ad2797bf6dcd13ca01c5e72b5465df6c/ttH_pat2bean_53x_100_2_92I.root')

                                                                                                                                                                                                        

#process.OSUAnalysis.useTrackCaloRhoCorr = cms.bool(False)
#process.OSUAnalysis.applyLeptonSF       = cms.bool(True)


process.OSUAnalysis.histogramSets.append(ElectronHistograms)
process.OSUAnalysis.histogramSets.append(ElectronTrackHistograms)
process.OSUAnalysis.verbose = cms.int32(2)

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrks.StandardAnalysis.MyElectronCtrlSampleSelections_disappTrks import *

add_channels (process, [SingleElecTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])

## process.OSUAnalysis.channels.append(ZtoETrk)
# process.OSUAnalysis.channels.append(SingleElecTrig)
## process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV1)

#process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV2)
#process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV3)
#process.OSUAnalysis.channels.append(WToENuSimple)
## process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV2NJet1)  
## process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV2NJet2)  
## process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV2NJet3) 
## process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV2NJet4)  
## process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV2NJet1BTagVeto)
## process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV2NJet2BTagVeto)
## process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV2NJet3BTagVeto)
## process.OSUAnalysis.channels.append(PreSelElecMatchTrigElecV2NJet4BTagVeto)





