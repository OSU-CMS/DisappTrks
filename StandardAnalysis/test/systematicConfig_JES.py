#!/usr/bin/env python
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

datasets = [
##     'AMSB_mGrav32K_0p5ns',
##     'AMSB_mGrav32K_1ns',
##     'AMSB_mGrav32K_5ns',

##     'AMSB_mGrav50K_0p5ns',
##     'AMSB_mGrav50K_1ns',
##     'AMSB_mGrav50K_5ns',

##     'AMSB_mGrav61K_0p2ns',
##     'AMSB_mGrav61K_0p5ns',
##     'AMSB_mGrav61K_1ns',
##     'AMSB_mGrav61K_5ns',

##     'AMSB_mGrav75K_0p5ns',
##     'AMSB_mGrav75K_1ns',
##     'AMSB_mGrav75K_5ns',

##     'AMSB_mGrav100K_0p5ns',
##     'AMSB_mGrav100K_1ns',
##     'AMSB_mGrav100K_5ns',

##     'AMSB_mGrav125K_0p5ns',
##     'AMSB_mGrav125K_1ns',
##     'AMSB_mGrav125K_5ns',

##     'AMSB_mGrav150K_0p5ns',
##     'AMSB_mGrav150K_1ns',
##     'AMSB_mGrav150K_5ns',

    ]

options = {}
options['datasets'] = datasets
options['composite_dataset_definitions'] = composite_dataset_definitions
options['dataset_names'] = dataset_names
options['nJobs'] = nJobs
options['maxEvents'] = maxEvents
options['types'] = types
options['labels'] = labels


def add_charginos (options, masses, ctaus):
    for mass in masses:
        for ctau in ctaus:
            datasetName       = 'AMSB_chargino_' + str (mass) + "GeV_RewtCtau" +                  str (ctau)  + "cm"
            sourceDatasetName = 'AMSB_chargino_' + str (mass) + "GeV_ctau" + str(math.floor(source_chargino_ctau(ctau))).rstrip('0').rstrip('.') + "cm"
            options['datasets'].append (datasetName)
            options['dataset_names'][datasetName] = options['dataset_names'][sourceDatasetName]
            options['nJobs']        [datasetName] =  5
            options['maxEvents']    [datasetName] = -1
            options['types']        [datasetName] = "signalMC"
            options['labels']       [datasetName] = str (mass) + " GeV #chi^{#pm} (#LTc#tau#GT = " + str (ctau) + " cm)"
            print "Adding dataset:  " + datasetName + "; sourceDatasetName=" + sourceDatasetName + "; dataset_name[sourceDatasetName]=" + options['dataset_names'][sourceDatasetName]
#add_stops (options, [200], [1.0,10.0,100.0])
#add_stops (options, [200], [0.2])
#add_stops (options, [200,300,400,500,600,700,800], [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0])

add_charginos (options, [100,200,300,400,500,600], [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])

systematic_name = "JES"
channel = "FullSelection"
usePdfWt = False

#minus_condor_dir   = "condor_2014_02_19_FullSelSystSig_PULo"   
minus_condor_dir   = "jesDown"   
central_condor_dir = "fullSelectionAllSigWithEcalGapVeto"  
plus_condor_dir    = "jesUp" 

