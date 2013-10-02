from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *
###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

#uncomment this line to add a single file to be processed
#process.source.fileNames.append('file:'+os.environ['CMSSW_BASE']+'/src/OSUT3Analysis/AnaTools/test/stop600toBottom_100mm.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/j/jbrinson/public/disappTrks/analysisFilesFromOSU/dataFiletoTestTemplate.root')
#process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')


process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerSkim/AMSB_mGrav50K_0p5ns_Reco/Trigger/bean_0.root')
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/wulsin/WJetsToLNu_PtW-100_TuneZ2star_8TeV-madgraph/BEANs-v4/0ff8045eb3a4a7ce9562dd332df0072c/ttH_pat2bean_53x_104_1_jHL.root')
#process.source.fileNames.append('file:/mnt/hadoop/users/wulsin/disappTrksBkgdMC_V5/WJetsToLNu/pat2bean_53x_10_3_NOa.root')
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerSkim/MET_2012D_Reco/Trigger/bean_78.root')  # for evt 279999328
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerSkim/MET_2012D_Reco/Trigger/bean_77.root')  # for evt 271849094
#process.source.fileNames.append('file:/data/users/jbrinson/condor/TriggerSkim/MET_2012D_Reco/Trigger/bean_16.root')  # for evt 874175456
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/disappTrksNew_V2/2012D/pat2bean_53x_146_1_L3w.root')  # for evt 874175456
#process.source.fileNames.append('file:/mnt/hadoop/se/store/user/jbrinson/disappTrksNew_V2/2012D/pat2bean_53x_148_2_1Dq.root')  # for evt 64918484
#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV2/CMSSW_5_3_8_patch1/src/DisappTrksT3ANTemp/StandardAnalysis/test/TriggerJetMet/beanEvt279999328.root')
#process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV2/CMSSW_5_3_8_patch1/src/DisappTrksT3ANTemp/StandardAnalysis/test/TriggerJetMet/beanEvt271849094.root')
#process.source.fileNames.append('file:/data/users/wulsin/analysisTemplateV1/condor/condor_2013_07_22_TriggerJetMet2/MET_2012D/TriggerJetMet/bean_11.root')




#uncomment these 3 lines to add all files in a given directory to be processed
#dir = "/data/se/store/user/abrinke1/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball_Summer12_DR53X-PU_S10_START53_V7A-v1_BEAN_53xOn53x_V02_CV01/894bf83260076a22df0c97ce24c6bb58/"
#for file in os.listdir(dir):
#        process.source.fileNames.extend(cms.untracked.vstring('file:' + dir + file))
        
#output file name when running interactively
process.TFileService.fileName = 'hist.root'

#number of events to process when running interactively
process.maxEvents.input = 1000
#process.MessageLogger.cerr.FwkReport.reportEvery = 1

#True -> Fill histograms for all objects, False -> Fill histograms only for objects passing all cuts
#False is recommended under normal circumstances
process.OSUAnalysis.plotAllObjectsInPassingEvents = False


#overwrite the default inputs in osuAnalysis_cfi
process.OSUAnalysis.muons     = cms.InputTag('BNproducer', 'selectedPatMuons')
process.OSUAnalysis.electrons = cms.InputTag('BNproducer', 'selectedPatElectrons')

process.OSUAnalysis.doPileupReweighting = cms.bool(False)
process.OSUAnalysis.puFile = cms.string (os.environ['CMSSW_BASE']+'/src/OSUT3Analysis/Configuration/data/pu_disappTrks.root')



########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################



#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
process.OSUAnalysis.histogramSets.append(TrackHistograms)
process.OSUAnalysis.histogramSets.append(MetHistograms)
process.OSUAnalysis.histogramSets.append(JetHistograms)


#import user-defined histograms
from DisappTrks.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  
process.OSUAnalysis.histogramSets.append(ExtraTrackHistograms)


##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *

## # First two channels needed to estimate yields
## process.OSUAnalysis.channels.append(SigReg)
## process.OSUAnalysis.channels.append(SigRegWithTrigJetMet)
## process.OSUAnalysis.channels.append(SigRegWithMaxCalo)

## # Other channels used to make plots; exact composition of bkgds may not be correct.   
process.OSUAnalysis.channels.append(PreSelection)
## process.OSUAnalysis.channels.append(PreSelectionPMissing)
## process.OSUAnalysis.channels.append(PreSelectionPEiso)
## process.OSUAnalysis.channels.append(PreSelectionElectronId)
## process.OSUAnalysis.channels.append(PreSelectionPionId)
## process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMet)
## process.OSUAnalysis.channels.append(CtrlReg)
## #process.OSUAnalysis.channels.append(CtrlRegWithTrigJetMet)
## process.OSUAnalysis.channels.append(FitReg)
## process.OSUAnalysis.channels.append(FitRegWithMaxCalo)
## #process.OSUAnalysis.channels.append(FitRegWithTrigJetMet)
## process.OSUAnalysis.channels.append(PreSelectionPt20)
## process.OSUAnalysis.channels.append(PreSelectionPt50)
## process.OSUAnalysis.channels.append(PreSelectionPt75)
## process.OSUAnalysis.channels.append(PreSelectionPt100)
## process.OSUAnalysis.channels.append(PreSelectionPt125)


