
from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *
###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

#uncomment this line to add a single file to be processed
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/WJetsToLNu/pat2bean_53x_10_1_3IZ.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SigMC_LL01_mGrav150K_5ns/pat2bean_53x_5.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/j/jbrinson/public/disappTrks/analysisFilesFromOSU/dataFiletoTestTemplate.root')
#process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')


#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerSkim/AMSB_mGrav50K_0p5ns_Reco/Trigger/bean_0.root')
#process.source.fileNames.append('file:/store/user/ahart/BN_DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_0/DYToMuMu_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_968_3_yKs.root')
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerMetSkim_v2/Wjets_PtW100/TriggerMet/bean_119.root')
process.source.fileNames.append('file:/home/wulsin/workdirTemplateDisTrk/condor/condor_2013_11_23_SingleElecTrigger/Wjets_PtW100/SingleElecTrig/bean_0.root')
#process.source.fileNames.append('file:/home/jbrinson/DisTrack/mainAN/AnTemp/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/TriggerMetSkim_v2/Wjets_PtW100/TriggerMet/bean_9.root')
#process.source.fileNames.append('file:/store/user/jbrinson/MET/BEAN2012-v4/66b7c0b77dff84935489342550a9cb3e/METParked_Run2012D-22Jan2013-v1_AOD_309_1_LCr.root')
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerMetSkim/Wjets_PtW100/TriggerMet/bean_0.root')   
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph/BEANs-v4/0ff8045eb3a4a7ce9562dd332df0072c/ttH_pat2bean_53x_104_1_jHL.root')




process.maxEvents.input = 1000
#process.OSUAnalysis.printEventInfo = cms.bool(True)
#process.OSUAnalysis.dataset = cms.string ('DYJetsToLL_Reco')
#process.OSUAnalysis.dataset = cms.string ('WJetsToLNu_Reco')
#process.OSUAnalysis.doPileupReweighting = cms.bool(False)
#output file name when running interactively
process.TFileService.fileName = 'hist.root'
#process.OSUAnalysis.GetPlotsAfterEachCut = cms.bool(True)
########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################
from OSUT3Analysis.Configuration.histogramDefinitions import *
process.OSUAnalysis.histogramSets.append(MCParticleHistograms)
#All histograms are plotted by default as defined in trackAnalyzerCondor_cfg.py

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *

from DisappTrks.StandardAnalysis.MyTauCtrlSampleSelections_disappTrks import *
from DisappTrks.StandardAnalysis.MyElectronCtrlSampleSelections_disappTrks import *

#process.OSUAnalysis.channels.append(ZtoMuTauHad)

## Signal Region Channels ##

#add_channels (process, [TriggerMet], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#add_channels (process, [Trigger], ["keep *", "drop BNtriggers_BNproducer_L1Talgo_BEANs"])
#process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorr)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloLoose)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorrWithTrigJetMet)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloLooseWithTrigJetMet)

# Other channels used to make plots; exact composition of bkgds may not be correct.   
## Preselection Channels ##

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
process.OSUAnalysis.channels.append(FullSelectionElecPreveto)
process.OSUAnalysis.channels.append(FullSelectionElecId)
process.OSUAnalysis.channels.append(ZtoETrkEId)
process.OSUAnalysis.channels.append(ZtoETrkEIdNoVeto)
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
#process.OSUAnalysis.channels.append(PreSelectionElectron)
#process.OSUAnalysis.channels.append(PreSelectionMu)
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


