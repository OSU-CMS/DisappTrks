from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrksT3ANTemp.StandardAnalysis.trackAnalyzerCondor_cfg import *
###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

#uncomment this line to add a single file to be processed
process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/DYJetsToLL_V6/pat2bean_53x_363_1_5wf.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/WJetsToLNu/pat2bean_53x_10_1_3IZ.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/j/jbrinson/public/disappTrks/analysisFilesFromOSU/dataFiletoTestTemplate.root')
#process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')

#output file name when running interactively
process.TFileService.fileName = 'hist.root'

########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#All histograms are plotted by default as defined in trackAnalyzerCondor_cfg.py

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *

# First two channels needed to estimate yields
process.OSUAnalysis.channels.append(SigRegWithMaxCaloPUCorr)
process.OSUAnalysis.channels.append(SigRegWithMaxCaloLoose)
process.OSUAnalysis.channels.append(SigRegWithTrigJetMetPUCorr)
process.OSUAnalysis.channels.append(SigRegWithTrigJetMet)

# Other channels used to make plots; exact composition of bkgds may not be correct.   
process.OSUAnalysis.channels.append(PreSelection)
process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMet)
process.OSUAnalysis.channels.append(PreSelectionPEiso)

process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyWithTrigJetMet)  
process.OSUAnalysis.channels.append(PreSelectionMuonVetoOnlyWithTrigJetMet)  

#Other available channels
#process.OSUAnalysis.channels.append(PreSelectionPMissing)
#process.OSUAnalysis.channels.append(PreSelectionPEiso)
#process.OSUAnalysis.channels.append(PreSelectionElectronId)
#process.OSUAnalysis.channels.append(PreSelectionPionId)
#process.OSUAnalysis.channels.append(CtrlReg)
#process.OSUAnalysis.channels.append(CtrlRegWithTrigJetMet)
#process.OSUAnalysis.channels.append(PreSelectionPt20)
#process.OSUAnalysis.channels.append(PreSelectionPt50)
#process.OSUAnalysis.channels.append(PreSelectionPt75)
#process.OSUAnalysis.channels.append(PreSelectionPt100)
#process.OSUAnalysis.channels.append(PreSelectionPt125)


