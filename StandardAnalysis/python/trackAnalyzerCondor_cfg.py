from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *

###############################################################
##### Standard Config File to be Used for Condor #####
###############################################################

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
from DisappTrksT3ANTemp.StandardAnalysis.MyHistogramDefinitions_disappTrks import *  
process.OSUAnalysis.histogramSets.append(ExtraTrackHistograms)

##########################################################
##### Add the Desired Default Channels to the List to be Run #####
##########################################################


##Specify the channels to be run in trackAnalyzer*.py in the test directory##


