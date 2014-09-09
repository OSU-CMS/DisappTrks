from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *
###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

#uncomment this line to add a single file to be processed


#process.source.fileNames.append('file:/afs/cern.ch/user/j/jbrinson/public/disappTrks/analysisFilesFromOSU/dataFiletoTestTemplate.root')
process.source.fileNames.append('file:/data/users/jbrinson/condor/fullSelectionSkim_24June/MET_2012D/FullSelection/bean_0.root')
#process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')

#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/ahart/BN_WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_0/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_100_2_iDY.root')  

#process.source.fileNames.append('file:/store/user/ahart/BN_WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_0/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_1000_7_CiE.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav50K_0p5ns_V5_wulsin-DisappTrkChargino_LL01_mGrav50K_0p5ns_V5-bc901238a19bd91cf436f9dd92d9a527_USER_0/DisappTrkChargino_LL01_mGrav50K_0p5ns_V5_wulsin-DisappTrkChargino_LL01_mGrav50K_0p5ns_V5-bc901238a19bd91cf436f9dd92d9a527_USER_1_3_ivj.root')  
#process.source.fileNames.append('file:/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav50K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav50K_1ns_V5-8d7921bb856d43d2cc7dce00818be4d4_USER_0/DisappTrkChargino_LL01_mGrav50K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav50K_1ns_V5-8d7921bb856d43d2cc7dce00818be4d4_USER_1_4_XLz.root') 


#process.source.fileNames.append('file:/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav61K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav61K_1ns_V5-c1250bd7ba1be8ecace130ea7b0ea4c7_USER_0/DisappTrkChargino_LL01_mGrav61K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav61K_1ns_V5-c1250bd7ba1be8ecace130ea7b0ea4c7_USER_1_3_p3p.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/BN_METParked_Run2012D-22Jan2013-v1_AOD_0/METParked_Run2012D-22Jan2013-v1_AOD_95_1_WHH.root')


#process.source.fileNames.append('file:/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav75K_5ns_V5_wulsin-DisappTrkChargino_LL01_mGrav75K_5ns_V5-5c3ba9e0f2fc83598aa92e5bd06ecf95_USER_1/DisappTrkChargino_LL01_mGrav75K_5ns_V5_wulsin-DisappTrkChargino_LL01_mGrav75K_5ns_V5-5c3ba9e0f2fc83598aa92e5bd06ecf95_USER_1_2_CwN.root')  

#process.source.fileNames.append('file:/store/user/ahart/BN_stop800ToTop_10.0mm_8TeV-pythia6_Summer12-START52_V9-v2_biliu-stop800ToTop_10.0mm_TuneZ2star_8TeV-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v3-e542883f7d1b22c1f30ae55768bc52e5_USER_0/stop800ToTop_10.0mm_8TeV-pythia6_Summer12-START52_V9-v2_biliu-stop800ToTop_10.0mm_TuneZ2star_8TeV-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v3-e542883f7d1b22c1f30ae55768bc52e5_USER_2_1_tql.root')  


#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_20_SkimMet90/QCD_1800/SkimMet90/bean_0.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_WToLNu_Pt220_PU_CMSSW_5_3_9_V3_wulsin-WToLNu_Pt220_PU_CMSSW_5_3_9_V3-8c80184e424cbf5fbb864b1ea86d0c47_USER_0/WToLNu_Pt220_PU_CMSSW_5_3_9_V3_wulsin-WToLNu_Pt220_PU_CMSSW_5_3_9_V3-8c80184e424cbf5fbb864b1ea86d0c47_USER_10_1_Yvd.root')  
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_DYToLL_Pt220_PU_CMSSW_5_3_9_V3_wulsin-DYToLL_Pt220_PU_CMSSW_5_3_9_V3-fc4e5b14e95e0947c34293af73ae3756_USER_0/DYToLL_Pt220_PU_CMSSW_5_3_9_V3_wulsin-DYToLL_Pt220_PU_CMSSW_5_3_9_V3-fc4e5b14e95e0947c34293af73ae3756_USER_10_1_I84.root') 
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_DYToLL_Pt220_PU_CMSSW_5_3_9_V3_wulsin-DYToLL_Pt220_PU_CMSSW_5_3_9_V3-fc4e5b14e95e0947c34293af73ae3756_USER_0/DYToLL_Pt220_PU_CMSSW_5_3_9_V3_wulsin-DYToLL_Pt220_PU_CMSSW_5_3_9_V3-fc4e5b14e95e0947c34293af73ae3756_USER_10_1_I84.root')
#process.source.fileNames.append('file:/store/user/wulsin/BN_WToLNu_Pt220_PU_CMSSW_5_3_9_V3_wulsin-WToLNu_Pt220_PU_CMSSW_5_3_9_V3-8c80184e424cbf5fbb864b1ea86d0c47_USER_0/WToLNu_Pt220_PU_CMSSW_5_3_9_V3_wulsin-WToLNu_Pt220_PU_CMSSW_5_3_9_V3-8c80184e424cbf5fbb864b1ea86d0c47_USER_1_1_idW.root')


#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_01_25_MetJetSkim/AMSB_mGrav100K_1ns/MetJet/bean_0.root')
#process.source.fileNames.append('file:/home/wulsin/disappTrks/BeanStopTesting/STOP2012-v6Dev/CMSSW_5_3_11/src/BEAN/BEANmaker/test/testBean.root')  

## process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_04_29_FullSelectionUnBlinded/MET_2012B/FullSelection/bean_6.root')  # Event 1 in signal region
## process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_04_29_FullSelectionUnBlinded/MET_2012D/FullSelection/bean_23.root') # Event 2 in signal region  
#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_04_29_FullSelectionUnBlinded/AMSB_mGrav100K_1ns/MetJet/bean_0.root')

#process.source.fileNames.append('file:/store/user/wulsin/BN_AMSB_chargino_200GeV_ctau30cm_NoFilter_8TeV_pythia6_V1_wulsin-AMSB_chargino_200GeV_ctau30cm_NoFilter_8TeV_pythia6_V1-ae3f86cb5b5e41389e02b4b277502ec0_USER_0/AMSB_chargino_200GeV_ctau30cm_NoFilter_8TeV_pythia6_V1_wulsin-AMSB_chargino_200GeV_ctau30cm_NoFilter_8TeV_pythia6_V1-ae3f86cb5b5e41389e02b4b277502ec0_USER_10_1_ioH.root')

#process.source.fileNames.append('file:/store/user/jbrinson/MET/BEAN2012-v4/66b7c0b77dff84935489342550a9cb3e/METParked_Run2012D-22Jan2013-v1_AOD_381_1_8xR.root')  


#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_04_23_NoTrigJetSel/Wjets/NoTrigJetSel/bean_0.root') 
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav100K_5ns_V5_wulsin-DisappTrkChargino_LL01_mGrav100K_5ns_V5-dbf8f833b677731a66afce2dfb79acf9_USER_2/DisappTrkChargino_LL01_mGrav100K_5ns_V5_wulsin-DisappTrkChargino_LL01_mGrav100K_5ns_V5-dbf8f833b677731a66afce2dfb79acf9_USER_1_5_srp.root')

#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_03_10_FullSelection/AMSB_mGrav100K_5ns/FullSelection/bean_3.root')  

## process.source.fileNames.append('file:/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav100K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav100K_1ns_V5-342f049f6ad2a5ef899bc9ba72599219_USER_2/DisappTrkChargino_LL01_mGrav100K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav100K_1ns_V5-342f049f6ad2a5ef899bc9ba72599219_USER_1_1_LJI.root')
## process.OSUAnalysis.dataset = cms.string ('AMSB_mGrav100K_1ns')  


#process.source.fileNames.append('file:/store/user/ahart/BN_DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_0/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_968_3_yKs.root')
#process.source.fileNames.append('file:/home/wulsin/workdirTemplateDisTrk/condor/condor_2013_11_23_SingleElecTrigger/Wjets_PtW100/SingleElecTrig/bean_0.root')
#process.source.fileNames.append('file:/home/jbrinson/DisTrack/mainAN/AnTemp/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/TriggerMetSkim_v2/Wjets_PtW100/TriggerMet/bean_9.root')
#process.source.fileNames.append('file:/store/user/jbrinson/MET/BEAN2012-v4/66b7c0b77dff84935489342550a9cb3e/METParked_Run2012D-22Jan2013-v1_AOD_309_1_LCr.root')
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerMetSkim/Wjets_PtW100/TriggerMet/bean_0.root')   
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/BN_WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_0/WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_99_2_ARK.root')


#process.source.fileNames.append('file:/data/users/wulsin/condor/signalMCGenV3/AMSB_chargino_200GeV_ctau1000cm_BEAN/condor/AMSB_chargino_200GeV_ctau1000cm_BEAN/testBean_4.root')  



#dir = '/mnt/hadoop/se/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav125K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav125K_1ns_V5-98811528007bf485888cb4fef749973b_USER_1/'  
#dir = '/store/user/wulsin/BN_DisappTrkChargino_LL01_mGrav61K_1ns_V5_wulsin-DisappTrkChargino_LL01_mGrav61K_1ns_V5-c1250bd7ba1be8ecace130ea7b0ea4c7_USER_2/' # old sample
#dir = '/store/user/wulsin/BN_AMSB_chargino_200GeV_ctau30cm_NoFilter_8TeV_pythia6_V1_wulsin-AMSB_chargino_200GeV_ctau30cm_NoFilter_8TeV_pythia6_V1-f8c638816d5a5ac84cb91405fa24a5dc_USER_0/'   # new sample
#dir = '/store/user/wulsin/BN_AMSB_chargino_200GeV_ctau30cm_FilterSumPt50_8TeV_pythia6_V1_wulsin-AMSB_chargino_200GeV_ctau30cm_FilterSumPt50_8TeV_pythia6_V1-f8c638816d5a5ac84cb91405fa24a5dc_USER_0/'
#dir = '/store/user/wulsin/BN_AMSB_chargino_200GeV_ctau1000cm_FilterSumPt50_8TeV_pythia6_V1_wulsin-AMSB_chargino_200GeV_ctau1000cm_FilterSumPt50_8TeV_pythia6_V1-4757b2dbddadf9637490e4c44e0caa70_USER_0/'  
#dir = '/data/users/wulsin/condor/signalMCGenV3/AMSB_chargino_200GeV_ctau1000cm_BEANV6/'  
#dir = '/data/users/wulsin/condor/signalMCGenV3/AMSB_chargino_200GeV_ctau1000cm_BEAN/'  
#dir = '/home/wulsin/disappTrks/BeanStopTesting/STOP2012-v4Test3/CMSSW_5_3_11/src/BEAN/BEANmaker/test/condor/amsbChargino_mGrav50K_5ns/'  
#dir = '/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2014_01_14_PreSelectionTau/Wjets_PtW100/PreSelectionTau/'  
#dir = '/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2014_01_22_PreSelectionTau2/Wjets_PtW100/PreSelectionTau/' 
#dir = '/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_24_AtlasSel5/DY_PtZ100/AtlasDisappTrk/' 
#dir = '/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2013_12_24_AtlasSel5/W4jets/AtlasDisappTrk/' 
#dir = '/store/user/ahart/BN_WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_0/'  
#dir = '/store/user/wulsin/BN_WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_0/'
#dir = '/mnt/hadoop/se/store/user/wulsin/WToLNu_Pt220_PU_V1/'
#dir = '/mnt/hadoop/se/store/user/wulsin/DYToLL_Pt220_PU_V1'
## dir = '/data/users/wulsin/condor/analysisTemplateV3/condor_2014_04_29_FullSelectionUnBlinded/MET_2012D/FullSelection/' 
## for file in os.listdir(dir):  
##     if file.find(".root") != -1: # Skip over files that do not contain .root.  
##         process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))

## process.source.eventsToProcess = cms.untracked.VEventRange(
##     '1:15:462', 
##     )


process.MessageLogger.cerr.FwkReport.reportEvery = 100
#process.maxEvents.input = -1
process.maxEvents.input = 1000
#process.OSUAnalysis.dataset = cms.string ('DYJetsToLL_Reco')
#process.OSUAnalysis.dataset = cms.string ('AMSB_chargino_200GeV_ctau30cm')
#process.OSUAnalysis.dataset = cms.string ('AMSB_chargino_400GeV_RewtCtau5cm')  
#process.OSUAnalysis.doPileupReweighting = cms.bool(False)
#process.OSUAnalysis.GetPlotsAfterEachCut = cms.bool(True) 
#process.OSUAnalysis.printEventInfo   = cms.bool(True) 
#process.OSUAnalysis.printAllTriggers = cms.bool(True)
#process.OSUAnalysis.verbose = verbose = cms.int32(1) 
process.OSUAnalysis.datasetType = cms.string ('data')
#process.OSUAnalysis.stopCTau = cms.vdouble(10.0, 5.0)  

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')  # Needed for running over signal produced on Tier 3  

#process.OSUAnalysis.treeBranchSets = cms.VPSet()

#output file name when running interactively
process.TFileService.fileName = 'hist.root'
#process.OSUAnalysis.GetPlotsAfterEachCut = cms.bool(True)
########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################
from OSUT3Analysis.Configuration.histogramDefinitions import *
process.OSUAnalysis.histogramSets.append(MCParticleHistograms)
process.OSUAnalysis.histogramSets.append(MCParticleExtraHistograms)
process.OSUAnalysis.histogramSets.append(EventExtraHistograms)
#process.OSUAnalysis.histogramSets.append(MuonTrackHistograms)
#process.OSUAnalysis.histogramSets = cms.VPSet() 
#process.OSUAnalysis.histogramSets.append(StopHistograms) 
#All histograms are plotted by default as defined in trackAnalyzerCondor_cfg.py

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *
from DisappTrks.StandardAnalysis.MyTauCtrlSampleSelections_disappTrks import *
from DisappTrks.StandardAnalysis.MyElectronCtrlSampleSelections_disappTrks import *


##for jes systematic
#process.OSUAnalysis.flagJESJERCorr = cms.bool(True)
#process.OSUAnalysis.jESJERCorr = cms.string('JESup')
#process.OSUAnalysis.jESJERCorr = cms.string('JESdown')
#process.OSUAnalysis.jESJERCorr = cms.string('JERup')
#process.OSUAnalysis.jESJERCorr = cms.string('JERdown')



################################
## Channels for Analysis Note ##
################################
#process.OSUAnalysis.channels.append(TauBkgdMismeasure)
#process.OSUAnalysis.channels.append(ElecBkgdMismeasure)
#process.OSUAnalysis.channels.append(TauBkgdPresel)
#process.OSUAnalysis.channels.append(TauBkgdPreselNoTau)
#process.OSUAnalysis.channels.append(FakeTrackSel)  
#process.OSUAnalysis.channels.append(PreSelection)
#process.OSUAnalysis.channels.append(PreSelectionMuon)

#process.OSUAnalysis.channels.append(FullSelectionMCSig)
#process.OSUAnalysis.channels.append(FullSelectionMuPreveto)
#process.OSUAnalysis.channels.append(FullSelectionIdMuon)  
#process.OSUAnalysis.channels.append(FullSelectionMuPrevetoNoMet)  

##channels for elec bkgd
#process.OSUAnalysis.channels.append(PreSelNoElecVeto)
#process.OSUAnalysis.channels.append(FullSelectionElecPreveto)
#process.OSUAnalysis.channels.append(FullSelectionElecId)
process.OSUAnalysis.channels.append(FullSelection)
#process.OSUAnalysis.channels.append(PreSelElecId)

#process.OSUAnalysis.channels.append(ZtoETrkEId)
#process.OSUAnalysis.channels.append(ZtoETrkEIdLoosePt)
#process.OSUAnalysis.channels.append(ZtoETrkEIdLoosePtNoVeto)
#process.OSUAnalysis.channels.append(ZtoETrkEIdNoVeto)
#process.OSUAnalysis.channels.append(ZtoETrkEIdPresel)
#process.OSUAnalysis.channels.append(ZtoETrkEIdPreselMaxCalo)
#process.OSUAnalysis.channels.append(ZtoETrkEIdNoVetoPresel)

#process.OSUAnalysis.channels.append(ZtoETrkEIdPreselSevenHits)
#process.OSUAnalysis.channels.append(ZtoETrkEIdPreselMaxCaloSevenHits)
#process.OSUAnalysis.channels.append(ZtoETrkEIdNoVetoPreselSevenHits)
#process.OSUAnalysis.channels.append(PreSelectionNoDeadEcal)

#process.OSUAnalysis.channels.append(ZtoETrkEIdNoVetoPreselMinCalo)
#process.OSUAnalysis.channels.append(ZtoETrkEIdPreselLoosePtMaxCalo)
#process.OSUAnalysis.channels.append(ZtoETrkVetoPreselLoosePtNoDeadEcalMaxCalo)
#process.OSUAnalysis.channels.append(ZtoETrkEIdNoVetoNoMissOut)




## process.OSUAnalysis.channels.append(FullSelectionMuPrevetoNoMet)  
## process.OSUAnalysis.channels.append(FullSelectionNoMetMuId) 
## process.OSUAnalysis.channels.append(FullSelectionNoMetNoTrkCuts)  
## process.OSUAnalysis.channels.append(FullSelectionNoMetFakeTrk)  




################################
################################
## Skim Channels  ##


#add_channels (process, [NoCuts], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelectionWTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelection], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelectionUpToElecVetoWTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelectionUpToElecVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelectionUpToMuonVetoWTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullTrkSelectionUpToMuonVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullSelection], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [TrkSelectionNoTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionFilterMC], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelection], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionElec], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionElecPt30], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionMuon], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionMuonNoMissInMid], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionMuonMetNoMu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionTau], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoLepVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionPt30NoLepVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullSelectionElecPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullSelectionMuPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [FullSelectionTauPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [MetJetTrig105], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelNoLepVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoPt], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoNHit], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoIso], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoMissIn], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoMissMid], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionNoRelIsoRp3], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionNoTrkJetDR],  ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [MetJetSelNoJetJetDPhi], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionNoJetJetDPhi_NoMetDPhi], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionNoJetJetDPhi], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [PreSelectionNoMetDPhi], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoMuonFiducial], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionNoMuonFiducial], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoJet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoJet_LeadingJetFilter], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoMet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 


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
#add_channels (process, [FullSelectionNHits3Min], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionNHits4MinFake], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])


## add_channels (process, [NoTrigTrkPresel], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [MonojetTrigTrkPresel], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [Jet80MetnoMu95TrigTrkPresel], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [MET120TrigTrkPresel], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])

## add_channels (process, [MonojetTrigJetSel], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [Jet80MetnoMu95TrigJetSel], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [MET120TrigJetSel], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [NoTrigJetSel], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])

## add_channels (process, [MonojetTrigJetSelWENu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [Jet80MetnoMu95TrigJetSelWENu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [MET120TrigJetSelWENu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [NoTrigJetSelWENu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])

## add_channels (process, [MonojetTrigJetSelWMuNu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [Jet80MetnoMu95TrigJetSelWMuNu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [MET120TrigJetSelWMuNu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [NoTrigJetSelWMuNu], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])



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

## process.OSUAnalysis.channels.append(FullSelectionNHits3)
## process.OSUAnalysis.channels.append(FullSelectionNHits5)
## process.OSUAnalysis.channels.append(FullSelectionNHits6)


#add_channels (process, [FullSelectionDeadEcalLast], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionElecId], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [FullSelectionElecIdPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [ZtoETrkEId], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [ZtoETrkEIdNoVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [ZtoETrkVetoPreSelLoosePtNoDeadEcal], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [ZtoETrkEIdPreselMaxCaloSevenHits], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [ZtoETrkEIdPreselLoosePtMaxCalo], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [PreSelectionPt30NoLepVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [PreSelNoLepVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [PreSelection], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [PreSelectionElec], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [PreSelectionTau], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [PreSelectionMuon], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [PreSelectionMuonMet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
## add_channels (process, [FullSelectionElecPrevetoKeepEcalo], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [FullSelectionNoCalo], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [FullSelectionElecPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [FullSelectionMuPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [FullSelectionTauPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [ZtoMuTauHad], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [ZtoMuTauHadNoTau], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
## add_channels (process, [FullSelectionNoMetNoTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
## process.OSUAnalysis.channels.append(FullSelectionNoMet)
## add_channels (process, [FullSelectionNoCalo],    ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 
#add_channels (process, [FullSelectionNoMissHit], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"]) 

#process.OSUAnalysis.channels.append(DebugCuts)
#process.OSUAnalysis.channels.append(PreSelIdElec)
#process.OSUAnalysis.channels.append(PreSelIdMuon)
#process.OSUAnalysis.channels.append(PreSelIdTau)
#process.OSUAnalysis.channels.append(PreSelIdFake)
#process.OSUAnalysis.channels.append(PreSelIdOther)


#process.OSUAnalysis.channels.append(ZtoMuTauHad)
#process.OSUAnalysis.channels.append(ZtoMuTauHadNoTau)

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
#add_channels (process, [FullSelectionElecPreveto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [PreSelectionNoLepVeto], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [MuTauHadCtrl], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [Trigger], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [SimpleIdMuon], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])


#process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorr)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloLoose)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorrWithTrigJetMet)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloLooseWithTrigJetMet)

# Other channels used to make plots; exact composition of bkgds may not be correct.   
## Preselection Channels ##

#process.OSUAnalysis.channels.append(ZtoMuTauHad)
#process.OSUAnalysis.channels.append(ZtoMuTauHadNoTau)

#process.OSUAnalysis.channels.append(NoCuts)
#process.OSUAnalysis.channels.append(NoCutsFilterMC)
#process.OSUAnalysis.channels.append(NoCutsFilterMCFilterJet)
#process.OSUAnalysis.channels.append(StopLifetime)  
#process.OSUAnalysis.channels.append(NoCutsFilterMCCtauZero)
#process.OSUAnalysis.channels.append(NoCutsFilterMCCtauNonZero)
#process.OSUAnalysis.channels.append(NoCutsDecayInTrackerN2)
#process.OSUAnalysis.channels.append(FullSelectionStopCtauZero)
#process.OSUAnalysis.channels.append(FullSelectionStopCtauNonZero)
#process.OSUAnalysis.channels.append(FullSelectionFilterMC)

#process.OSUAnalysis.channels.append(ZMCPart)
#process.OSUAnalysis.channels.append(WMCPart)




## process.OSUAnalysis.channels.append(PreSelIdMuonNoVeto)
## process.OSUAnalysis.channels.append(PreSelIdElec)
#process.OSUAnalysis.channels.append(PreSelIdMuon)
## process.OSUAnalysis.channels.append(PreSelIdTau)
## process.OSUAnalysis.channels.append(PreSelIdFake)  
## process.OSUAnalysis.channels.append(PreSelIdOther)  

## process.OSUAnalysis.channels.append(FullSelection)
## process.OSUAnalysis.channels.append(FullSelIdElec)
## process.OSUAnalysis.channels.append(FullSelIdMuon)
## process.OSUAnalysis.channels.append(FullSelIdTau)
## process.OSUAnalysis.channels.append(FullSelIdFake)  
## process.OSUAnalysis.channels.append(FullSelIdOther)  


#process.OSUAnalysis.channels.append(FullSelectionIdMuon)
#process.OSUAnalysis.channels.append(FullSelectionMuPreveto)
#process.OSUAnalysis.channels.append(ZtoETrkEIdPreselLoosePt)
#process.OSUAnalysis.channels.append(ZtoETrkVetoPreSelLoosePt)
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
#process.OSUAnalysis.channels.append(PreSelectionSeven)
#process.OSUAnalysis.channels.append(PreSelectionSevenElec)
#process.OSUAnalysis.channels.append(PreSelectionSevenMu)
#process.OSUAnalysis.channels.append(PreSelectionSevenTau)
#process.OSUAnalysis.channels.append(PreSelectionNoNHits)
#process.OSUAnalysis.channels.append(PreSelectionNoNoiseClean)
#process.OSUAnalysis.channels.append(PreSelectionNoPt)
#process.OSUAnalysis.channels.append(PreSelectionNoIso)
#process.OSUAnalysis.channels.append(FullSelectionNoMet)
#process.OSUAnalysis.channels.append(PreSelectionElecIdNoLepVeto)
## process.OSUAnalysis.channels.append(FullSelectionElecPreveto)
## process.OSUAnalysis.channels.append(FullSelectionElecId)
## process.OSUAnalysis.channels.append(ZtoETrkEId)
## process.OSUAnalysis.channels.append(ZtoETrkEIdNoVeto)
#process.OSUAnalysis.channels.append(FullSelectionElecPrevetoNoMet)
#process.OSUAnalysis.channels.append(FullSelectionElecPreveto)
#process.OSUAnalysis.channels.append(FullSelectionElecId)

#process.OSUAnalysis.channels.append(ZtoETrkEIdPresel)
#process.OSUAnalysis.channels.append(ZtoETrkEIdNoVetoPresel)
#process.OSUAnalysis.channels.append(ZtoETrkEId)
#process.OSUAnalysis.channels.append(ZtoETrkEIdNoVeto)

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

