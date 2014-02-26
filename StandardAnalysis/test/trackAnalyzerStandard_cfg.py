from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *
###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

#uncomment this line to add a single file to be processed


#process.source.fileNames.append('file:/afs/cern.ch/user/j/jbrinson/public/disappTrks/analysisFilesFromOSU/dataFiletoTestTemplate.root')
#process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')

#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2014_01_01_AtlasSel2/AMSB_mGrav61K_0p2ns/AtlasDisappTrk/bean_0.root')

#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/ahart/BN_WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_0/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_100_2_iDY.root')  

#process.source.fileNames.append('file:/store/user/ahart/BN_WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_0/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_1000_7_CiE.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav50K_0p5ns_V5_wulsin-DisappTrkChargino_LL01_mGrav50K_0p5ns_V5-bc901238a19bd91cf436f9dd92d9a527_USER_0/DisappTrkChargino_LL01_mGrav50K_0p5ns_V5_wulsin-DisappTrkChargino_LL01_mGrav50K_0p5ns_V5-bc901238a19bd91cf436f9dd92d9a527_USER_1_3_ivj.root')  
#process.source.fileNames.append('file:/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav50K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav50K_1ns_V5-8d7921bb856d43d2cc7dce00818be4d4_USER_0/DisappTrkChargino_LL01_mGrav50K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav50K_1ns_V5-8d7921bb856d43d2cc7dce00818be4d4_USER_1_4_XLz.root') 


#process.source.fileNames.append('file:/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav61K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav61K_1ns_V5-c1250bd7ba1be8ecace130ea7b0ea4c7_USER_0/DisappTrkChargino_LL01_mGrav61K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav61K_1ns_V5-c1250bd7ba1be8ecace130ea7b0ea4c7_USER_1_3_p3p.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/BN_METParked_Run2012D-22Jan2013-v1_AOD_0/METParked_Run2012D-22Jan2013-v1_AOD_95_1_WHH.root')

process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2014_02_11_FullSelectionAllSig/AMSB_mGrav75K_0p5ns/FullSelection/bean_0.root')  


#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_30_SkimFullTrkSelection/AMSB_mGrav61K_0p5ns/FullTrkSelection/bean_0.root')  
#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_30_SkimFullTrkSelection/AMSB_mGrav61K_1ns/FullTrkSelection/bean_0.root')  

#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_24_AtlasSel5/DY_PtZ100/AtlasDisappTrk/bean_0.root')  
#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_20_SkimMet90/AMSB_mGrav61K_1ns/SkimMet90/bean_0.root')
#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_24_AtlasSel/AMSB_mGrav61K_1ns/AtlasDisappTrk/bean_0.root')  
#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_20_SkimMet90/QCD_1800/SkimMet90/bean_0.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_WToLNu_Pt220_PU_CMSSW_5_3_9_V3_wulsin-WToLNu_Pt220_PU_CMSSW_5_3_9_V3-8c80184e424cbf5fbb864b1ea86d0c47_USER_0/WToLNu_Pt220_PU_CMSSW_5_3_9_V3_wulsin-WToLNu_Pt220_PU_CMSSW_5_3_9_V3-8c80184e424cbf5fbb864b1ea86d0c47_USER_10_1_Yvd.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_DYToLL_Pt220_PU_CMSSW_5_3_9_V3_wulsin-DYToLL_Pt220_PU_CMSSW_5_3_9_V3-fc4e5b14e95e0947c34293af73ae3756_USER_0/DYToLL_Pt220_PU_CMSSW_5_3_9_V3_wulsin-DYToLL_Pt220_PU_CMSSW_5_3_9_V3-fc4e5b14e95e0947c34293af73ae3756_USER_10_1_I84.root') 
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_DYToLL_Pt220_PU_CMSSW_5_3_9_V3_wulsin-DYToLL_Pt220_PU_CMSSW_5_3_9_V3-fc4e5b14e95e0947c34293af73ae3756_USER_0/DYToLL_Pt220_PU_CMSSW_5_3_9_V3_wulsin-DYToLL_Pt220_PU_CMSSW_5_3_9_V3-fc4e5b14e95e0947c34293af73ae3756_USER_10_1_I84.root')
#process.source.fileNames.append('file:/store/user/wulsin/BN_WToLNu_Pt220_PU_CMSSW_5_3_9_V3_wulsin-WToLNu_Pt220_PU_CMSSW_5_3_9_V3-8c80184e424cbf5fbb864b1ea86d0c47_USER_0/WToLNu_Pt220_PU_CMSSW_5_3_9_V3_wulsin-WToLNu_Pt220_PU_CMSSW_5_3_9_V3-8c80184e424cbf5fbb864b1ea86d0c47_USER_1_1_idW.root')

#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerSkim/AMSB_mGrav50K_0p5ns_Reco/Trigger/bean_0.root')
#process.source.fileNames.append('file:/store/user/ahart/BN_DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_0/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_968_3_yKs.root')
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerMetSkim_v2/Wjets_PtW100/TriggerMet/bean_119.root')
#process.source.fileNames.append('file:/home/wulsin/workdirTemplateDisTrk/condor/condor_2013_11_23_SingleElecTrigger/Wjets_PtW100/SingleElecTrig/bean_0.root')
#process.source.fileNames.append('file:/home/jbrinson/DisTrack/mainAN/AnTemp/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/TriggerMetSkim_v2/Wjets_PtW100/TriggerMet/bean_9.root')
#process.source.fileNames.append('file:/store/user/jbrinson/MET/BEAN2012-v4/66b7c0b77dff84935489342550a9cb3e/METParked_Run2012D-22Jan2013-v1_AOD_309_1_LCr.root')
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerMetSkim/Wjets_PtW100/TriggerMet/bean_0.root')   
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_0/WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_99_2_ARK.root')


#dir = '/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2014_01_14_PreSelectionTau/Wjets_PtW100/PreSelectionTau/'  
#dir = '/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2014_01_22_PreSelectionTau2/Wjets_PtW100/PreSelectionTau/' 
#dir = '/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_24_AtlasSel5/DY_PtZ100/AtlasDisappTrk/' 
#dir = '/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_24_AtlasSel5/W4jets/AtlasDisappTrk/' 
#dir = '/store/user/ahart/BN_WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_0/'  
#dir = '/store/user/wulsin/BN_WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_0/'
#dir = '/mnt/hadoop/se/store/user/wulsin/WToLNu_Pt220_PU_V1/'
#dir = '/mnt/hadoop/se/store/user/wulsin/DYToLL_Pt220_PU_V1'  
## for file in os.listdir(dir):  
##     if file.find(".root") != -1: # Skip over files that do not contain .root.  
##         process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))

                


process.maxEvents.input = 1000
#process.maxEvents.input = 5
#process.maxEvents.input = -1  
#process.OSUAnalysis.dataset = cms.string ('DYJetsToLL_Reco')
#process.OSUAnalysis.dataset = cms.string ('WJetsToLNu_Reco')
#process.OSUAnalysis.doPileupReweighting = cms.bool(False)
#process.OSUAnalysis.GetPlotsAfterEachCut = cms.bool(True) 
process.OSUAnalysis.printEventInfo   = cms.bool(True) 
#process.OSUAnalysis.printAllTriggers = cms.bool(True)
process.OSUAnalysis.verbose = verbose = cms.int32(0) 

#process.OSUAnalysis.treeBranchSets = cms.VPSet()

#output file name when running interactively
process.TFileService.fileName = 'hist.root'
#process.OSUAnalysis.GetPlotsAfterEachCut = cms.bool(True)
########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################
from OSUT3Analysis.Configuration.histogramDefinitions import *
process.OSUAnalysis.histogramSets.append(MCParticleHistograms)
process.OSUAnalysis.histogramSets.append(TestEventHistograms)
#All histograms are plotted by default as defined in trackAnalyzerCondor_cfg.py

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *
from DisappTrks.StandardAnalysis.MyTauCtrlSampleSelections_disappTrks import *
from DisappTrks.StandardAnalysis.MyElectronCtrlSampleSelections_disappTrks import *

################################
## Channels for Analysis Note ##
################################
#process.OSUAnalysis.channels.append(FullSelection)
## process.OSUAnalysis.channels.append(FullSelectionMet80Trig)
#process.OSUAnalysis.channels.append(FullSelectionNoMet) 
#process.OSUAnalysis.channels.append(FakeTrackSel)  
#process.OSUAnalysis.channels.append(PreSelection)
#process.OSUAnalysis.channels.append(PreSelectionMuon)

process.OSUAnalysis.channels.append(FullSelectionMCSig)
#process.OSUAnalysis.channels.append(FullSelectionMuPreveto)
#process.OSUAnalysis.channels.append(FullSelectionIdMuon)  
#process.OSUAnalysis.channels.append(FullSelectionMuPrevetoNoMet)  
## process.OSUAnalysis.channels.append(FullSelectionNoMetMuId) 
## process.OSUAnalysis.channels.append(FullSelectionNoMetNoTrkCuts)  
## process.OSUAnalysis.channels.append(FullSelectionNoMetFakeTrk)  





################################
################################
## Skim Channels  ##

## add_channels (process, [FullTrkSelectionWTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelection], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelectionUpToElecVetoWTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelectionUpToElecVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelectionUpToMuonVetoWTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelectionUpToMuonVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelection], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelection], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionElec], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionMuon], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionMuonMetNoMu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionPt30NoLepVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionMuonMet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionTau], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionMuPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionTauPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [MetJet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelNoLepVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [SkimMet90], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [TriggerMet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [Trigger], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FakeTrkTestCorr], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FakeTrkTestCorrLoose], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [AtlasDisappTrk], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [AtlasDisappTrkCharginoId], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [AtlasDisappTrkIsoTrk], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [AtlasDisappTrkUptoMet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionCharginoId], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionNHits4], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionNHits4MinFake], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])



## add_channels (process, [PreSelectionElec], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionElecNoTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionMuon], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionMuonNoTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelCtrlNMiss], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## process.OSUAnalysis.channels.append(PreSelCtrlNMissElec)
## process.OSUAnalysis.channels.append(PreSelCtrlNMissMuon)
## process.OSUAnalysis.channels.append(PreSelCtrlNMissTau)
## process.OSUAnalysis.channels.append(PreSelCtrlNMissIdElec)
## process.OSUAnalysis.channels.append(PreSelCtrlNMissIdMuon)
## process.OSUAnalysis.channels.append(PreSelCtrlNMissIdTau)
## process.OSUAnalysis.channels.append(PreSelCtrlNMissIdFake)
## process.OSUAnalysis.channels.append(PreSelCtrlNMissIdOther)
## add_channels (process, [PreSelCtrlEcalo], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## process.OSUAnalysis.channels.append(PreSelCtrlEcaloElec)
## process.OSUAnalysis.channels.append(PreSelCtrlEcaloMuon)
## process.OSUAnalysis.channels.append(PreSelCtrlEcaloTau)
## process.OSUAnalysis.channels.append(PreSelCtrlEcaloIdElec)
## process.OSUAnalysis.channels.append(PreSelCtrlEcaloIdMuon)
## process.OSUAnalysis.channels.append(PreSelCtrlEcaloIdTau)
## process.OSUAnalysis.channels.append(PreSelCtrlEcaloIdFake)
## process.OSUAnalysis.channels.append(PreSelCtrlEcaloIdOther)


#process.OSUAnalysis.channels.append(DebugCuts)

    

#process.OSUAnalysis.channels.append(ZtoMuTauHad)

## Signal Region Channels ##

## process.OSUAnalysis.channels.append(FullSelectionCharginoIdDeadEcalLast) 
## process.OSUAnalysis.channels.append(FullSelectionCharginoIdNHitsLast) 

#process.OSUAnalysis.channels.append(AtlasDisappTrkCharginoId)
#process.OSUAnalysis.channels.append(AtlasDisappTrkCharginoIdTrigMet)
#process.OSUAnalysis.channels.append(AtlasDisappTrkDeadEcal)
## process.OSUAnalysis.channels.append(AtlasDisappTrk)
## process.OSUAnalysis.channels.append(AtlasDisappTrkTrigMet)
#process.OSUAnalysis.channels.append(AtlasDisappTrkDeadEcalMuonCuts)  
#process.OSUAnalysis.channels.append(AtlasDisappTrkDeadEcalSecMuonVeto) 
#process.OSUAnalysis.channels.append(AtlasDisappTrkDeadEcalSecMuonVetoEcalo)  
## process.OSUAnalysis.channels.append(AtlasDisappTrkIsoTrkMissOut3)
## process.OSUAnalysis.channels.append(AtlasDisappTrkIsoTrkMissOut6)
## process.OSUAnalysis.channels.append(AtlasDisappTrkIsoTrkMissOut7)
## process.OSUAnalysis.channels.append(AtlasDisappTrkIsoTrkMissOut8)

#add_channels (process, [TriggerMet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [Trigger], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorr)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloLoose)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorrWithTrigJetMet)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloLooseWithTrigJetMet)

# Other channels used to make plots; exact composition of bkgds may not be correct.   
## Preselection Channels ##

#process.OSUAnalysis.channels.append(NoCuts)

#process.OSUAnalysis.channels.append(ZMCPart)
#process.OSUAnalysis.channels.append(WMCPart)




## process.OSUAnalysis.channels.append(PreSelIdMuonNoVeto)
## process.OSUAnalysis.channels.append(PreSelIdElec)
#process.OSUAnalysis.channels.append(PreSelIdMuon)
## process.OSUAnalysis.channels.append(PreSelIdTau)
## process.OSUAnalysis.channels.append(PreSelIdFake)  
## process.OSUAnalysis.channels.append(PreSelIdOther)  

#process.OSUAnalysis.channels.append(FullSelection)
## process.OSUAnalysis.channels.append(FullSelIdElec)
## process.OSUAnalysis.channels.append(FullSelIdMuon)
## process.OSUAnalysis.channels.append(FullSelIdTau)
## process.OSUAnalysis.channels.append(FullSelIdFake)  
## process.OSUAnalysis.channels.append(FullSelIdOther)  


#process.OSUAnalysis.channels.append(FullSelectionIdMuon)
#process.OSUAnalysis.channels.append(FullSelectionMuPreveto)
#process.OSUAnalysis.channels.append(FakeTrkTestCorr)
#process.OSUAnalysis.channels.append(FullSelectionFakeTrk)
## process.OSUAnalysis.channels.append(FullSelectionFakeTrkCtrlNom)
## process.OSUAnalysis.channels.append(FullSelectionFakeTrkCtrlInv)
#process.OSUAnalysis.channels.append(FullTrkSelectionUpToMissIn)
## process.OSUAnalysis.channels.append(FullTrkSelectionLeadingJet)
## process.OSUAnalysis.channels.append(FullTrkSelectionJetPt)

## process.OSUAnalysis.channels.append(FullSelectionNoPt)
## process.OSUAnalysis.channels.append(FullSelectionNoEta)
## process.OSUAnalysis.channels.append(FullSelectionNoBadCSC)
## process.OSUAnalysis.channels.append(FullSelectionNoD0)
## process.OSUAnalysis.channels.append(FullSelectionNoDZ)
## process.OSUAnalysis.channels.append(FullSelectionNoNhits)
## process.OSUAnalysis.channels.append(FullSelectionNoRelIso)
## process.OSUAnalysis.channels.append(FullSelectionNoCalo)
#process.OSUAnalysis.channels.append(FullSelectionNoMissHit)

# For fake track bkgd estimate:
#process.OSUAnalysis.channels.append(BadCSCVetoRegions)  
## process.OSUAnalysis.channels.append(MuTrigNoCuts)
## process.OSUAnalysis.channels.append(FakeTrkMuTrig)
## process.OSUAnalysis.channels.append(FullSelectionNoTrkCuts)
## process.OSUAnalysis.channels.append(FullSelectionFakeTrk)
## process.OSUAnalysis.channels.append(FakeTrkTestCorr)
## process.OSUAnalysis.channels.append(FullSelectionInvD0Loose)
## process.OSUAnalysis.channels.append(FullSelectionInvDZLoose)
## process.OSUAnalysis.channels.append(FullSelectionInvNHitsLoose)
## process.OSUAnalysis.channels.append(FullSelectionInvNMissMidLoose)
## process.OSUAnalysis.channels.append(FullSelectionInvD0InvDZ)
## process.OSUAnalysis.channels.append(FullSelectionInvD0InvNHits)
## process.OSUAnalysis.channels.append(FullSelectionInvD0InvNMissMid)
## process.OSUAnalysis.channels.append(FullSelectionInvDZInvNHits)
## process.OSUAnalysis.channels.append(FullSelectionInvDZInvNMissMid)
## process.OSUAnalysis.channels.append(FullSelectionInvNHitsInvNMissMid)
## process.OSUAnalysis.channels.append(FullSelectionInvD0InvDZInvNHits)
## process.OSUAnalysis.channels.append(FullSelectionInvD0InvDZInvNMissMid)
## process.OSUAnalysis.channels.append(FullSelectionInvD0InvNHitsInvNMissMid)
## process.OSUAnalysis.channels.append(FullSelectionInvDZInvNHitsInvNMissMid)
#process.OSUAnalysis.channels.append(FullSelectionInvD0InvDZInvNHitsInvNMissMid)


## process.OSUAnalysis.channels.append(FullSelectionInvD0Loose)
## process.OSUAnalysis.channels.append(FullSelectionInvDZLoose)
## process.OSUAnalysis.channels.append(FullSelectionInvNHitsLoose)
## process.OSUAnalysis.channels.append(FullSelectionInvMissMidLoose)
## process.OSUAnalysis.channels.append(FullSelectionInvNoneLoose)



#process.OSUAnalysis.channels.append(PreSelIdMuonInvHits)
#process.OSUAnalysis.channels.append(SimpleIdMuon)  
#process.OSUAnalysis.channels.append(SigRegNominal)  
#process.OSUAnalysis.channels.append(StudyMuVeto)
#process.OSUAnalysis.channels.append(StudyMuVeto2)
#process.OSUAnalysis.channels.append(PreSelInvElecVeto)  
#process.OSUAnalysis.channels.append(PreSelInvMuonVeto)  

#process.OSUAnalysis.channels.append(PreSelIdMuonNoVeto)
#process.OSUAnalysis.channels.append(PreSelIdMuon) #this goes to sig reg
#process.OSUAnalysis.channels.append(PreSelIdElec) #this goes to sig reg
#process.OSUAnalysis.channels.append(PreSelIdTau) #this goes to sig reg
#process.OSUAnalysis.channels.append(PreSelMuonId)
#process.OSUAnalysis.channels.append(PreSelElecId)
#process.OSUAnalysis.channels.append(PreSelTauId)
#process.OSUAnalysis.channels.append(PreSelIdMuonInvHits)
##process.OSUAnalysis.channels.append(SimpleIdMuon)  
#process.OSUAnalysis.channels.append(SigRegNominal)  
#process.OSUAnalysis.channels.append(PreSelection)
#process.OSUAnalysis.channels.append(PreSelectionNoNHits)
#process.OSUAnalysis.channels.append(PreSelectionNoNoiseClean)
#process.OSUAnalysis.channels.append(PreSelectionNoJetJetDPhi)
#process.OSUAnalysis.channels.append(PreSelectionNoPt)
#process.OSUAnalysis.channels.append(PreSelectionNoIso)
#process.OSUAnalysis.channels.append(PreSelectionElecIdNoLepVeto)
## process.OSUAnalysis.channels.append(FullSelectionElecPreveto)
## process.OSUAnalysis.channels.append(FullSelectionElecId)
## process.OSUAnalysis.channels.append(ZtoETrkEId)
## process.OSUAnalysis.channels.append(ZtoETrkEIdNoVeto)
#process.OSUAnalysis.channels.append(MCPartWFromMu)
#process.OSUAnalysis.channels.append(NoCuts)
#process.OSUAnalysis.channels.append(PreSelection)
#process.OSUAnalysis.channels.append(FullSelection)
#process.OSUAnalysis.channels.append(PreselPCalo)
#process.OSUAnalysis.channels.append(FullSelectionElectron)
#process.OSUAnalysis.channels.append(FullSelectionUnMatched)
#process.OSUAnalysis.channels.append(FullSelectionTauNoD0)
#process.OSUAnalysis.channels.append(FullSelectionTauNoDz)
#process.OSUAnalysis.channels.append(FullSelectionTauNoNHit)
#process.OSUAnalysis.channels.append(FullSelectionNoNHit)
#process.OSUAnalysis.channels.append(PreSelectionElec)
#process.OSUAnalysis.channels.append(PreSelectionElecNoTrig)
#process.OSUAnalysis.channels.append(PreSelectionMuon)
#process.OSUAnalysis.channels.append(PreSelectionMuMet100)
##process.OSUAnalysis.channels.append(PreSelectionMuMet300)
#process.OSUAnalysis.channels.append(PreSelectionTau)

#process.OSUAnalysis.channels.append(PreSelectionMotherW)
#process.OSUAnalysis.channels.append(PreSelectionMotherWTrkLep)
#process.OSUAnalysis.channels.append(PreSelectionNoMuEta)
## process.OSUAnalysis.channels.append(PreSelInvElecVeto)  
## process.OSUAnalysis.channels.append(PreSelInvMuonVeto)  

## process.OSUAnalysis.channels.append(PreSelIdMuonNoMetJetNoVeto)
## process.OSUAnalysis.channels.append(PreSelIdMuonNoMetJet)

## process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMet)
## process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyElecMatch)
## process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyMuonMatch)
## process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyNoMuonMatch)  
## process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyNoElecMatch)  



#process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyWithTrigJetMet)  
#process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyNoD0WithTrigJetMet)  
#process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyNoDzWithTrigJetMet)  
#process.OSUAnalysis.channels.append(PreSelectionMuonVetoOnlyWithTrigJetMet)  
#process.OSUAnalysis.channels.append(PreSelectionPMissingWithTrigJetMet)

## For AOD Samples ##

#process.OSUAnalysis.channels.append(PreSelectionNoHitCutWithTrigJetMet)
#process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet)  
#process.OSUAnalysis.channels.append(PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet)  

## d0 and dz sidebands ##

#process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyDzSideWithTrigJetMet)  
#process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyD0SideWithTrigJetMet)  

## GenMatched Channels ##

#process.OSUAnalysis.channels.append(PreSelectionPMissingNotGenMatched)
#process.OSUAnalysis.channels.append(PreSelectionPMissingPionId)
#process.OSUAnalysis.channels.append(PreSelectionPMissingElectronId)
#process.OSUAnalysis.channels.append(PreSelectionElectronId)
#process.OSUAnalysis.channels.append(PreSelectionPionId)

## Other Channels ##

#process.OSUAnalysis.channels.append(CtrlReg)
#process.OSUAnalysis.channels.append(CtrlRegWithTrigJetMet)
#process.OSUAnalysis.channels.append(PreSelectionPt20)
#process.OSUAnalysis.channels.append(PreSelectionPt50)
#process.OSUAnalysis.channels.append(PreSelectionPt75)
#process.OSUAnalysis.channels.append(PreSelectionPt100)
#process.OSUAnalysis.channels.append(PreSelectionPt125)



## Dump python config if wished
#outfile = open('dumpedConfig.py','w'); print >> outfile,process.dumpPython(); outfile.close()

