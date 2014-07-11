#!/usr/bin/env python

from systematicConfig_common import *

makeRewtdPlot = False

systematic_name = "Ecalo"

channelNoCuts = "NoCutsFilterMCTrack"  # eventually use this 

ratioHistFile = "../data/EcaloVarySFNorm.root"
ratioHistName = "ratio"  

histRewtName = "trackCaloTot_RhoCorr"  

histMin = 0
histMax = 110  

## minus_condor_dir   = JessDir+"ecaloVaryCorrNorm"
## plus_condor_dir    = JessDir+"ecaloVaryCorrNorm"
## central_condor_dir = JessDir+"fullSelectionWithEcalGapNoCorr"
central_condor_dir = WellsDir+"JessCopy_fullSelectionWithEcalGapNoCorr"  
central_gen_condor_dir = WellsDir+"condor_2014_07_10_NoCutsFilterMCTrack"  # correct
#central_gen_condor_dir = WellsDir+"condor_2014_07_09_NoCutsSignal"  # testing
# plus_gen_condor_dir = JessDir+"ecaloVaryCorrNormNoCuts"



# from localOptionsAll import *

## datasets = [
##     ]

## options = {}
## options['datasets'] = datasets
## options['composite_dataset_definitions'] = composite_dataset_definitions
## options['dataset_names'] = dataset_names
## options['nJobs'] = nJobs
## options['maxEvents'] = maxEvents
## options['types'] = types
## options['labels'] = labels



## def add_charginos (options, masses, ctaus):
##     for mass in masses:
##         for ctau in ctaus:
##             datasetName       = 'AMSB_chargino_' + str (mass) + "GeV_RewtCtau" + str (ctau)  + "cm"
##             sourceDatasetName = 'AMSB_chargino_' + str (mass) + "GeV_ctau" + str(math.floor(source_chargino_ctau(ctau))).rstrip('0').rstrip('.') + "cm"
##             options['datasets'].append (datasetName)
##             options['dataset_names'][datasetName] = options['dataset_names'][sourceDatasetName]
##             options['nJobs']        [datasetName] =  5
##             options['maxEvents']    [datasetName] = -1
##             options['types']        [datasetName] = "signalMC"
##             options['labels']       [datasetName] = str (mass) + " GeV #chi^{#pm} (#LTc#tau#GT = " + str (ctau) + " cm)"
##             print "Adding dataset:  " + datasetName + "; sourceDatasetName=" + sourceDatasetName + "; dataset_name[sourceDatasetName]=" + options['dataset_names'][sourceDatasetName]

## #add_charginos (options, [100,200,300,400,500,600], [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
## add_charginos (options, [100,200,300,400,500,600], [3,10,30,100,300,1000])  # short

## mass point used for plot in AN
#add_charginos (options, [400], [30])
            
