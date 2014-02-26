# Usage:
# > cmsRun trackAnalyzerCtrlElec_cfg.py 2>&1 | tee trackAnalyzerCtrlElec_cfg.log 

from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *


#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToTauTau_M-20_CT10_TuneZ2star_v2_8TeV-powheg-tauola-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_DISPLACED_LEPTON-v3/bean_989_1_ACv.root')
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_DISPLACED_LEPTON-v3/bean_4514_1_Jov.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/WJetsToLNu_TuneZ2Star_8TeV/pat2bean_53x_154_2_DeK.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/DYJetsToLL/pat2bean_53x_100_1_2KD.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/abrinke1/SingleElectron/SingleElectron_Run2012A-13Jul2012-v1_BEAN_53xOn53x_V02_CV01/4da6952f3c4fba5e66dcec676ef9c024//ttH_pat2bean_53x_110_1_kpZ.root')


#process.source.fileNames.append('file:/store/user/ahart/BN_WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_0/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v2_AODSIM_1000_7_CiE.root')
#process.source.fileNames.append('file:/store/user/ahart/BN_DYToEE_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_0/DYToEE_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_1000_5_Lij.root') 

#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2013_11_23_SingleElecTrigger/Wjets/SingleElecTrig/bean_5.root')  
#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_01_22_TriggerSkim/Wjets/Trigger/bean_0.root')
#process.source.fileNames.append('file:/data/users/jbrinson/condor/elecCtrlSkim/SingleElectron_2012A/ZtoETrkEIdNoVeto/bean_1.root') 
#process.source.fileNames.append('file:/data/users/jbrinson/condor/elecCtrlSkim/SingleElectron_2012A/ZtoETrkEIdNoVeto/bean_18.root')
#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_02_04_ZtoETrkEIdNoVetoPreselLoosePt/SingleElectron_2012A/ZtoETrkEIdNoVetoPreselLoosePt/bean_0.root')


##process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SingleMu/Run2012D-PromptReco-v1_BEAN2012-v4/ad2797bf6dcd13ca01c5e72b5465df6c/ttH_pat2bean_53x_240_23_ZnR.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/ZJetsToNuNu_100_HT_200_TuneZ2Star_8TeV_madgraph/BEAN2012-v4/0ff8045eb3a4a7ce9562dd332df0072c/ttH_pat2bean_53x_100_1_hBP.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SingleElectron/BEAN2012-v4/ad2797bf6dcd13ca01c5e72b5465df6c/ttH_pat2bean_53x_100_2_92I.root')
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerSkim/DY_PtZ100/Trigger/bean_0.root') 
                                                                                                                                                                                                        
#dir = '/data/users/wulsin/condor/analysisTemplateV3/condor_2014_01_22_TriggerSkim/Wjets/Trigger/'
## dir = '/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/ZtoETrkEIdPreselMaxCaloSevenHits/'
## for file in os.listdir(dir):
##     if file.find(".root") != -1: # Skip over files that do not contain .root.
##         process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))

## dir = '/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012B/ZtoETrkEIdPreselMaxCaloSevenHits/'
## for file in os.listdir(dir):
##     if file.find(".root") != -1: # Skip over files that do not contain .root.
##         process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))

## dir = '/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012C/ZtoETrkEIdPreselMaxCaloSevenHits/'
## for file in os.listdir(dir):
##     if file.find(".root") != -1: # Skip over files that do not contain .root.
##         process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))

## dir = '/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/ZtoETrkEIdPreselMaxCaloSevenHits/'
## for file in os.listdir(dir):
##     if file.find(".root") != -1: # Skip over files that do not contain .root.
##         process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))


#process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/ZtoETrkEIdPreselMaxCaloSevenHits/bean_11.root')
process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/ZtoETrkEIdPreselMaxCaloSevenHits/bean_58.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/ZtoETrkEIdPreselMaxCaloSevenHits/bean_61.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/ZtoETrkEIdPreselMaxCaloSevenHits/bean_75.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/ZtoETrkEIdPreselMaxCaloSevenHits/bean_9.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012C/ZtoETrkEIdPreselMaxCaloSevenHits/bean_108.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012C/ZtoETrkEIdPreselMaxCaloSevenHits/bean_110.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012C/ZtoETrkEIdPreselMaxCaloSevenHits/bean_145.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012C/ZtoETrkEIdPreselMaxCaloSevenHits/bean_72.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/ZtoETrkEIdPreselMaxCaloSevenHits/bean_139.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/ZtoETrkEIdPreselMaxCaloSevenHits/bean_144.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/ZtoETrkEIdPreselMaxCaloSevenHits/bean_15.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/ZtoETrkEIdPreselMaxCaloSevenHits/bean_20.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/ZtoETrkEIdPreselMaxCaloSevenHits/bean_48.root')
## process.source.fileNames.append('file:/data/users/jbrinson/condor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/ZtoETrkEIdPreselMaxCaloSevenHits/bean_66.root')

## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/condor_11.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  190906:165:143512185
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/condor_58.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  191271:282:306992015
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/condor_61.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  191226:843:1134096335
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/condor_75.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  191247:1008:1238685723
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012A/condor_9.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  191247:262:384259136
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012C/condor_108.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  201097:219:272411653
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012C/condor_110.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  199436:372:255752202
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012C/condor_145.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  198230:219:244099905
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012C/condor_72.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  201278:644:853951195
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/condor_139.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  207905:129:129643120
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/condor_144.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  207886:97:111608028
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/condor_15.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  205667:184:192761430
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/condor_20.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  205694:355:375483792
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/condor_48.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  207920:472:708623666
## condor/JessCondor/printEventElecCtrl_6Feb_v2/SingleElectron_2012D/condor_66.err:Event passed all cuts in channel ZtoETrkEIdPreselMaxCaloSevenHits:  run:lumi:evt=  203909:219:293678747


#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/lantonel/BN_SingleElectron_Run2012A-22Jan2013-v1_AOD_0/SingleElectron_Run2012A-22Jan2013-v1_AOD_190_3_2xz.root')  # Includes event 306992015  

#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_02_04_ZtoETrkEIdNoVetoPreselLoosePt/SingleElectron_2012A/ZtoETrkEIdNoVetoPreselLoosePt/bean_33.root')  # Do not find event 306992015; should contain 2015 events 

#process.source.fileNames.append('file:/data/users/wulsin/condor/analysisTemplateV3/condor_2014_02_04_ZtoETrkEIdNoVetoPreselLoosePt3/SingleElectron_2012A/ZtoETrkEIdNoVetoPreselLoosePt/bean_33.root') 


#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/ZtoETrkEIdNoVetoPreselLoosePt/bean.root')

#process.OSUAnalysis.useTrackCaloRhoCorr = cms.bool(False)
#process.OSUAnalysis.applyLeptonSF       = cms.bool(True)

process.maxEvents.input = 10000

## process.source.eventsToProcess = cms.untracked.VEventRange(
## '191271:306992015', 
## '191226:1134096335', 
## '201097:272411653', 
## '199436:255752202', 
## '198230:244099905', 
## '201278:853951195', 
## '207886:111608028', 
## '205667:192761430', 
## '205694:375483792', 
## '207920:708623666', 
## '203909:293678747', 
## )


process.OSUAnalysis.histogramSets.append(ElectronHistograms)
process.OSUAnalysis.histogramSets.append(ElectronTrackHistograms)
process.OSUAnalysis.histogramSets.append(JetExtraHistograms)
#process.OSUAnalysis.verbose = cms.int32(2)

process.OSUAnalysis.treeBranchSets = cms.VPSet()
#process.OSUAnalysis.printEventInfo = cms.bool(True)  

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *  
from DisappTrks.StandardAnalysis.MyElectronCtrlSampleSelections_disappTrks import *

#add_channels (process, [SingleElecTrig], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [Monojet80Met95TrigLeadJet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [SingleElecTrigTrkPreselNoElecVetoMet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## add_channels (process, [SingleElecTrigTrkPreselNoElecVetoJet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
## process.OSUAnalysis.channels.append(MonojetTrigTrkPreselNoElecVetoJet)

#add_channels (process, [ZtoETrkEIdPreselMaxCalo], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [ZtoETrkEIdPreselMaxCaloNMissOut3], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#process.OSUAnalysis.channels.append(ZtoETrkEIdPreselMaxCalo)  

#add_channels (process, [ZtoETrkEIdNoVetoPreselLoosePt], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])    # For testing lost event
add_channels (process, [ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])    # For testing lost event


#add_channels (process, [ZtoETrkEIdPreselLoosePt7Hits], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [ZtoETrkEIdPreselMaxCalo], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])  
#process.OSUAnalysis.channels.append(ZtoETrkEIdPreselLoosePt7Hits)
#process.OSUAnalysis.channels.append(ZtoETrkEIdPreselLoosePtMaxCalo)  

#add_channels (process, [Monojet80Met95TrigLeadJet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#process.OSUAnalysis.channels.append(SingleElecTrigLeadJet)  
## process.OSUAnalysis.channels.append(Monojet80Met95TrigTrkPreselNoElecVetoMet) 
## process.OSUAnalysis.channels.append(Met120TrigTrkPreselNoElecVetoMet)

## process.OSUAnalysis.channels.append(SingleElecTrigTrkPreselNoElecVetoMet)  
## process.OSUAnalysis.channels.append(MonojetTrigTrkPreselNoElecVetoMet)  


#process.OSUAnalysis.channels.append(NoCuts)

## process.OSUAnalysis.channels.append(SingleElecTrigLeadJet)
## process.OSUAnalysis.channels.append(Monojet80Met95TrigLeadJet)  

## process.OSUAnalysis.channels.append(SingleElecTrigTrkPreselNoElecVeto)  
## process.OSUAnalysis.channels.append(MonojetTrigTrkPreselNoElecVeto)  


#process.OSUAnalysis.channels.append(Jet80TrigLeadJet)  


## process.OSUAnalysis.channels.append(SingleElecTrigTrkPreselNoElecVetoMet)  
## #process.OSUAnalysis.channels.append(MonojetTrigTrkPreselNoElecVetoMet)  
## process.OSUAnalysis.channels.append(Jet80TrigTrkPreselNoElecVetoMet)  
## process.OSUAnalysis.channels.append(SingleElecTrigTrkPreselNoElecVetoJet)  
## process.OSUAnalysis.channels.append(Jet80TrigTrkPreselNoElecVetoJet)  

#process.OSUAnalysis.channels.append(ZtoETrk)

## process.OSUAnalysis.channels.append(ZtoETrkEId)
## process.OSUAnalysis.channels.append(ZtoETrkEIdNoVeto)
## process.OSUAnalysis.channels.append(ZtoETrkEIdNoVetoNoMissOut)  
## process.OSUAnalysis.channels.append(ZtoEE)  
#

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





