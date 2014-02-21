from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *
###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################
process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2014_01_25_MetJetSkim/AMSB_mGrav75K_1ns/MetJet/bean_0.root')  
process.maxEvents.input = 200

# For pile-up systematic:  
## process.OSUAnalysis.dataPU = cms.string ('PU_data_190456_208686_66805xSec')  # PU low xsec
process.OSUAnalysis.dataPU = cms.string ('PU_data_190456_208686_69300xSec')  # PU central value 
## process.OSUAnalysis.dataPU = cms.string ('PU_data_190456_208686_71795xSec')  # PU high xsec 

# For trigger efficiency systematic:  
process.OSUAnalysis.triggerMetSFFile = cms.string ('')    # no trigger eff correction  
#process.OSUAnalysis.triggerMetSFFile = cms.string (os.environ['CMSSW_BASE']+'/src/DisappTrks/StandardAnalysis/data/TriggerMetSF.root')  # with trigger eff correction  



########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################


##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *


################################
## Channels for Analysis Note ##
################################
process.OSUAnalysis.channels.append(FullSelection)

