from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *
###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

#uncomment this line to add a single file to be processed
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/WJetsToLNu/pat2bean_53x_10_1_3IZ.root')
process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/SigMC_LL01_mGrav150K_5ns/pat2bean_53x_5.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/j/jbrinson/public/disappTrks/analysisFilesFromOSU/dataFiletoTestTemplate.root')
#process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')
process.maxEvents.input = 1000
#process.OSUAnalysis.dataset = cms.string ('DYJetsToLL_Reco')
#process.OSUAnalysis.dataset = cms.string ('WJetsToLNu_Reco')
#process.OSUAnalysis.doPileupReweighting = cms.bool(False)
#output file name when running interactively
process.TFileService.fileName = 'hist.root'

########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#All histograms are plotted by default as defined in trackAnalyzerCondor_cfg.py

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *

## Signal Region Channels ##

## process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorr)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloLoose)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorrWithTrigJetMet)
## process.OSUAnalysis.channels.append(SigRegWithMaxCaloLooseWithTrigJetMet)

# Other channels used to make plots; exact composition of bkgds may not be correct.   
## Preselection Channels ##

#process.OSUAnalysis.channels.append(PreSelection)

process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMet)
process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyElecMatch)
process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyMuonMatch)
process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyNoMuonMatch)  
process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyNoElecMatch)  



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


