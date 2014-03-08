from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *

###############################################################
##### Standard Config File to be Used for Condor #####
###############################################################

#True -> Fill histograms for all objects, False -> Fill histograms only for objects passing all cuts
#False is recommended under normal circumstances
process.OSUAnalysis.plotAllObjectsInPassingEvents = False

#overwrite the default inputs in osuAnalysis_cfi
process.OSUAnalysis.muons     = cms.InputTag('BNproducer', 'selectedPatMuonsLoosePFlow')
#process.OSUAnalysis.secMuons  = cms.InputTag('BNproducer', 'selectedPatMuons')
process.OSUAnalysis.secMuons  = cms.InputTag('BNproducer', 'selectedPatMuonsLoose')
process.OSUAnalysis.electrons = cms.InputTag('BNproducer', 'selectedPatElectrons')



#process.OSUAnalysis.doPileupReweighting = cms.bool(False)
#process.OSUAnalysis.puFile = cms.string (os.environ['CMSSW_BASE']+'/src/OSUT3Analysis/Configuration/data/pu_disappTrks.root')

process.OSUAnalysis.triggerMetSF    = cms.string ('metPt')  
process.OSUAnalysis.trackNMissOutSF = cms.string ('ratio')  
process.OSUAnalysis.isrVarySF       = cms.string ('ratio')  


process.OSUAnalysis.useTrackCaloRhoCorr = cms.bool(True)  
#process.OSUAnalysis.treeBranchSets = AllTreeBranchSets  
process.OSUAnalysis.treeBranchSets = cms.VPSet()  

#number of events to process when running interactively
process.maxEvents.input = 1000
#process.MessageLogger.cerr.FwkReport.reportEvery = 1


########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################

#import the desired sets of histograms from the standard python file which defines them
from OSUT3Analysis.Configuration.histogramDefinitions import *
from DisappTrks.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  

process.OSUAnalysis.histogramSets.append(EventHistograms)

process.OSUAnalysis.histogramSets.append(TrackHistograms)
process.OSUAnalysis.histogramSets.append(ExtraTrackHistograms)
process.OSUAnalysis.histogramSets.append(TrackIsolationHistograms)

process.OSUAnalysis.histogramSets.append(MetHistograms)
process.OSUAnalysis.histogramSets.append(MetExtraHistograms)  

process.OSUAnalysis.histogramSets.append(JetHistograms)
process.OSUAnalysis.histogramSets.append(DiJetHistograms)
process.OSUAnalysis.histogramSets.append(SecondaryJetHistograms)
process.OSUAnalysis.histogramSets.append(SecJetExtraHistograms)  
process.OSUAnalysis.histogramSets.append(TrackJetHistograms)

process.OSUAnalysis.histogramSets.append(MuonHistograms)
process.OSUAnalysis.histogramSets.append(SecMuonHistograms)

process.OSUAnalysis.histogramSets.append(ElectronHistograms)
process.OSUAnalysis.histogramSets.append(TauHistograms)
process.OSUAnalysis.histogramSets.append(MuonTauHistograms)
process.OSUAnalysis.histogramSets.append(ElectronTrackHistograms)

#import user-defined histograms


#process.OSUAnalysis.histogramSets.append(JetExtraHistograms)  






##########################################################
##### Add the Desired Default Channels to the List to be Run #####
##########################################################


##Specify the channels to be run in trackAnalyzer*.py in the test directory##


