# trackAnalyzerAOD_cfg.py
# Use to run over AOD samples.


from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *
###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

#uncomment this line to add a single file to be processed
#process.source.fileNames.append('file:/mnt/hadoop/mc/DYToEE_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_DISPLACED_LEPTON-v3/bean_1000_1_V1m.root')
process.source.fileNames.append('file:/afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/dataCopyFromOSU/BEANsAOD/bean_DYToEE_M-20_CT10_TuneZ2star_v2_8TeV-powheg-pythia6_Summer12_DR53X-PU_S10_START53_V7A-v1_AODSIM_DISPLACED_LEPTON-v3_1000_1_V1m.root')  


#process.source.fileNames.append('file:/afs/cern.ch/user/j/jbrinson/public/disappTrks/analysisFilesFromOSU/dataFiletoTestTemplate.root')
#process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')

#output file name when running interactively
process.TFileService.fileName = 'hist.root'


process.OSUAnalysis.useTrackCaloRhoCorr = cms.bool(False)  

########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#All histograms are plotted by default as defined in trackAnalyzerCondor_cfg.py

##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *


process.OSUAnalysis.channels.append(PreSelection)                # Try this one for fun, but I think the hit cuts will be invalid.  
process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMet)  # Try this one for fun, but I think the hit cuts will be invalid.  

process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMetNoHitCut)
process.OSUAnalysis.channels.append(PreSelectionIsoTrkOnlyWithTrigJetMetNoHitCut)  
process.OSUAnalysis.channels.append(PreSelectionMuonVetoOnlyWithTrigJetMetNoHitCut)  



