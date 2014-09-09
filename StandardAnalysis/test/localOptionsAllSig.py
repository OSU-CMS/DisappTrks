#!/usr/bin/env python

from localOptionsAll import * 

#config_file = "trackAnalyzerSystSig_cfg.py"  

datasets = [
    
    'AMSB_mGrav32K_0p5ns',
    'AMSB_mGrav32K_1ns',
    'AMSB_mGrav32K_5ns',

    'AMSB_mGrav50K_0p5ns',
    'AMSB_mGrav50K_1ns',
    'AMSB_mGrav50K_5ns',

    'AMSB_mGrav61K_0p2ns',
    'AMSB_mGrav61K_0p5ns',
    'AMSB_mGrav61K_1ns',
    'AMSB_mGrav61K_5ns',
 
    'AMSB_mGrav75K_0p5ns',
    'AMSB_mGrav75K_1ns',
    'AMSB_mGrav75K_5ns',

    'AMSB_mGrav100K_0p5ns',
    'AMSB_mGrav100K_1ns',
    'AMSB_mGrav100K_5ns',

    'AMSB_mGrav125K_0p5ns',
    'AMSB_mGrav125K_1ns',
    'AMSB_mGrav125K_5ns',

    'AMSB_mGrav150K_0p5ns',
    'AMSB_mGrav150K_1ns',
    'AMSB_mGrav150K_5ns',

    ]


nJobs = {
     'AMSB_mGrav32K_0p5ns' : 5,
     'AMSB_mGrav32K_1ns' : 5,
     'AMSB_mGrav32K_5ns' : 5,
  
     'AMSB_mGrav50K_0p5ns' : 5,
     'AMSB_mGrav50K_1ns' : 5,
     'AMSB_mGrav50K_5ns' : 5,
  
     'AMSB_mGrav61K_0p2ns' : 5,
     'AMSB_mGrav61K_0p5ns' : 5,
     'AMSB_mGrav61K_1ns' : 5,
     'AMSB_mGrav61K_5ns' : 5,
  
     'AMSB_mGrav75K_0p5ns' : 5,
     'AMSB_mGrav75K_1ns' : 5,
     'AMSB_mGrav75K_5ns' : 5,
  
     'AMSB_mGrav100K_0p5ns' : 5,
     'AMSB_mGrav100K_1ns' : 5,
     'AMSB_mGrav100K_5ns' : 5,
  
     'AMSB_mGrav125K_0p5ns' : 5,
     'AMSB_mGrav125K_1ns' : 5,
     'AMSB_mGrav125K_5ns' : 5,
  
     'AMSB_mGrav150K_0p5ns' : 5,
     'AMSB_mGrav150K_1ns' : 5,
     'AMSB_mGrav150K_5ns' : 5,
  
 }



## dataset_names['AMSB_mGrav100K_0p5ns'] = 'AMSBChargino_BeanTest_100K0p5ns'
## dataset_names['AMSB_mGrav100K_1ns']   = 'AMSBChargino_BeanTest_100K1ns'
## dataset_names['AMSB_mGrav100K_5ns']   = 'AMSBChargino_BeanTest_100K5ns'

## colors['AMSB_mGrav100K_1.0cm'] = 1
## colors['AMSB_mGrav100K_2.0cm'] = 2
## colors['AMSB_mGrav100K_5.0cm'] = 3
## colors['AMSB_mGrav100K_10.0cm'] = 4
## colors['AMSB_mGrav100K_20.0cm'] = 6

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
##             datasetName       = 'AMSB_mGrav' + str (mass) + "_" +                      str (ctau)  + "cm"
##             sourceDatasetName = 'AMSB_mGrav' + str (mass) + "_" + str (source_chargino_tauFromCtau_Str(ctau)) + "ns"
##             options['datasets'].append (datasetName)
##             options['dataset_names'][datasetName] = options['dataset_names'][sourceDatasetName]
##             options['nJobs']        [datasetName] =  1
##             options['maxEvents']    [datasetName] = -1
##             options['types']        [datasetName] = "signalMC"
##             options['labels']       [datasetName] = str (mass) + " GeV #chi^{#pm} (#LTc#tau#GT = " + str (ctau) + " cm)"
##             print "Adding dataset:  " + datasetName + "; sourceDatasetName=" + sourceDatasetName + "; dataset_name[sourceDatasetName]=" + options['dataset_names'][sourceDatasetName]
                                                                                                            

## # all samples:
## #add_charginos (options, ["32K", "50K", "75K", "100K", "125K", "150K"], [0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
## # testing:
## add_charginos (options, ["100K"], [1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 150.0])


            
