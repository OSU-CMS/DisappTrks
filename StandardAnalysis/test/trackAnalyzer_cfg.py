from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *

###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################

#uncomment this line to add a single file to be processed
#process.source.fileNames.append('file:'+os.environ['CMSSW_BASE']+'/src/OSUT3Analysis/AnaTools/test/stop600toBottom_100mm.root')
#process.source.fileNames.append('file:/data/se/store/user/jbrinson/disappTrksNew_V2/2012A/pat2bean_53x_10_1_38g.root')
#process.source.fileNames.append('file:/data/se/store/user/jbrinson/disappTrksNew_V2/2012A_V2/pat2bean_53x_9_3_wHZ.root')
#process.source.fileNames.append('file:/data/se/store/user/wulsin/disappTrksBkgdMC_V6/WJetsToLNu//pat2bean_53x_19_1_n6n.root')
#process.source.fileNames.append('file:/afs/cern.ch/user/j/jbrinson/public/disappTrks/analysisFilesFromOSU/dataFiletoTestTemplate.root')
process.source.fileNames.append('file:/afs/cern.ch/work/j/jbrinson/public/analysisFilesFromOSU/SigFiletoTestTemp.root')

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

#overwrite the default collections
process.OSUAnalysis.muons     = cms.InputTag('BNproducer', 'selectedPatMuons')
process.OSUAnalysis.electrons = cms.InputTag('BNproducer', 'selectedPatElectrons')



########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################



#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
process.OSUAnalysis.histogramSets.append(TrackHistograms)
process.OSUAnalysis.histogramSets.append(MetHistograms)
process.OSUAnalysis.histogramSets.append(JetHistograms)


#import user-defined histograms
from DisappTrksT3ANTemp.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  
process.OSUAnalysis.histogramSets.append(ExtraTrackHistograms)


##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################

from DisappTrksT3ANTemp.StandardAnalysis.MyEventSelections_disappTrks import *

# First two channels needed to estimate yields
process.OSUAnalysis.channels.append(SigReg)
process.OSUAnalysis.channels.append(SigRegWithTrigJetMet)
process.OSUAnalysis.channels.append(SigRegWithMaxCalo)

# Other channels used to make plots; exact composition of bkgds may not be correct.   
process.OSUAnalysis.channels.append(PreSelection)
process.OSUAnalysis.channels.append(PreSelectionWithTrigJetMet)
process.OSUAnalysis.channels.append(CtrlReg)
#process.OSUAnalysis.channels.append(CtrlRegWithTrigJetMet)
process.OSUAnalysis.channels.append(FitReg)
process.OSUAnalysis.channels.append(FitRegWithMaxCalo)
#process.OSUAnalysis.channels.append(FitRegWithTrigJetMet)
process.OSUAnalysis.channels.append(PreSelectionPt20)
process.OSUAnalysis.channels.append(PreSelectionPt50)
process.OSUAnalysis.channels.append(PreSelectionPt75)
process.OSUAnalysis.channels.append(PreSelectionPt100)
process.OSUAnalysis.channels.append(PreSelectionPt125)


