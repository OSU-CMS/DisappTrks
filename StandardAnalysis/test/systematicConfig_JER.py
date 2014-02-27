#!/usr/bin/env python
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

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

options = {}
options['datasets'] = datasets
options['composite_dataset_definitions'] = composite_dataset_definitions
options['dataset_names'] = dataset_names
options['nJobs'] = nJobs
options['maxEvents'] = maxEvents
options['types'] = types
options['labels'] = labels

#add_stops (options, [200], [1.0,10.0,100.0])
#add_stops (options, [200], [0.2])
#add_stops (options, [200,300,400,500,600,700,800], [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0])


systematic_name = "JER"
channel = "FullSelection"
usePdfWt = False

#minus_condor_dir   = "condor_2014_02_19_FullSelSystSig_PULo"   
minus_condor_dir   = "jERDown_26Feb"   
central_condor_dir = "WellsCondorNew/condor_2014_02_11_FullSelectionAllSig"  
plus_condor_dir    = "jERUp_26Feb" 

