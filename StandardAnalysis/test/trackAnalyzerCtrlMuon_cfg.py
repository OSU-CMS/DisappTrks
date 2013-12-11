# Usage:
# > cmsRun trackAnalyzerCtrlMuon_cfg.py 2>&1 | tee trackAnalyzerCtrlMuon_cfg.log 

from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *


#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_DISPLACED_LEPTON-v3/bean_989_1_ACv.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_DISPLACED_LEPTON-v3/bean_4514_1_Jov.root')
process.source.fileNames.append('file:/mnt/hadoop/se/store/user/ahart/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6/BEAN2012-v4/4a12a6f1b79fbeb9915fe6064a3d6fce/ttH_pat2bean_53x_1000_1_3pq.root')  
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerSkim/DY_PtZ100/Trigger/bean_0.root')  
#process.source.fileNames.append('file:/data/users/jbrinson/condor/MuTriggerSkim/Wjets/MuTrigger/bean_145.root')  

#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/WJetsToLNu_TuneZ2Star_8TeV/pat2bean_53x_154_2_DeK.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/DYJetsToLL/pat2bean_53x_100_1_2KD.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/abrinke1/SingleElectron/SingleElectron_Run2012A-13Jul2012-v1_BEAN_53xOn53x_V02_CV01/4da6952f3c4fba5e66dcec676ef9c024//ttH_pat2bean_53x_110_1_kpZ.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SingleMu/Run2012D-PromptReco-v1_BEAN2012-v4/ad2797bf6dcd13ca01c5e72b5465df6c/ttH_pat2bean_53x_240_23_ZnR.root')  
#process.source.fileNames.append('file:/mnt/hadoop/mc/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_DISPLACED_LEPTON-v3/bean_1000_3_V4A.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/abrinke1/SingleMu/SingleMu_Run2012A-recover-06Aug2012-v1_BEAN_53xOn53x_V02_CV01/25216cad7390119ce70a2ab4eee94ee1//ttH_pat2bean_53x_10_1_uxf.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/abrinke1/SingleMu/SingleMu_Run2012A-13Jul2012-v1_BEAN_53xOn53x_V02_CV01/de3c20242948dd0d39f546037f2fbda9//ttH_pat2bean_53x_100_2_YMO.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SingleElec_Reco_P1//pat2bean_53x_102_1_CCH.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/ZJetsToNuNu_100_HT_200_TuneZ2Star_8TeV_madgraph/BEAN2012-v4/0ff8045eb3a4a7ce9562dd332df0072c/ttH_pat2bean_53x_100_1_hBP.root')\
                                                                                                                                                                                                          

#process.OSUAnalysis.useTrackCaloRhoCorr = cms.bool(False)
#process.OSUAnalysis.applyLeptonSF       = cms.bool(True)
#process.OSUAnalysis.applyLeptonSF       = cms.bool(False)  
#process.OSUAnalysis.doPileupReweighting = cms.bool(False)  
process.maxEvents.input = 1000 

process.OSUAnalysis.histogramSets.append(MuonHistograms)
#process.OSUAnalysis.histogramSets.append(SecMuonHistograms)
process.OSUAnalysis.histogramSets.append(MuonTrackHistograms)
#process.OSUAnalysis.printEventInfo = cms.bool(True)
#process.OSUAnalysis.printAllTriggers    = cms.bool(True) 
#process.OSUAnalysis.GetPlotsAfterEachCut = cms.bool(True) 


## MyTreeBranchSets = cms.VPSet(
##             EventBranches,
##                         MuonBranches,
##                         ElectronBranches,
##                         TauBranches,
##                         TrackBranches,
##                         MetBranches,
##                         JetBranches,
##                         GenJetBranches,
##                         SuperclusterBranches,
##                         #    PhotonBranches,  # not available in some BEANs
##                         #    TrigObjBranches,
##             #            PrimaryVertexBranches,
##                         BxlumiBranches,
##                         #    McparticleBranches,
##             #            StopBranches,
##                     )
#process.OSUAnalysis.treeBranchSets = cms.VPSet()  


## from DisappTrks.StandardAnalysis.MyDisappTrkBranchSets import *
## process.OSUAnalysis.treeBranchSets = AllSlimTreeBranchSets

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *
from DisappTrks.StandardAnalysis.MyMuonCtrlSampleSelections_disappTrks import *
#process.OSUAnalysis.channels.append(NoCuts)
#process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV1)
#process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NoJetCut)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV3)
# process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV4)
# process.OSUAnalysis.channels.append(WToMuSimple)  
#process.OSUAnalysis.channels.append(ZtoMuTrkNoJetMet)
#process.OSUAnalysis.channels.append(ZtoMuTrkNoJetMet)  
#process.OSUAnalysis.channels.append(SigRegMuTrigMuId)  
#process.OSUAnalysis.channels.append(SigRegIdMuon)
#process.OSUAnalysis.channels.append(WtoMuNuTrackFullPreSel)
#process.OSUAnalysis.channels.append(MuTrigMuId)  
process.OSUAnalysis.channels.append(ZtoMuTrkMuIdNoVeto)  
process.OSUAnalysis.channels.append(ZtoMuTrkMuId)  
#process.OSUAnalysis.channels.append(ZtoMuTrkMuIdInvHits)  
#process.OSUAnalysis.channels.append(ZtoMuTrkMuIdNoTrigMet)  
#process.OSUAnalysis.channels.append(TriggerMetNoMu)  

## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet1)  
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet2)  
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet3) 
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet4)  
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet1BTagVeto)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet2BTagVeto)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet3BTagVeto)
## process.OSUAnalysis.channels.append(PreSelMuonMatchTrigMuonV2NJet4BTagVeto)


## Dump python config if wished
outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()




