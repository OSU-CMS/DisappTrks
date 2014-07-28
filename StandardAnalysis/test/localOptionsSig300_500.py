#!/usr/bin/env python

from localOptionsAll import * 

from localOptionsAllSigNew import add_charginos   

datasets = [

    ]


options = {}
options['datasets'] = datasets
options['composite_dataset_definitions'] = composite_dataset_definitions
options['dataset_names'] = dataset_names
options['nJobs'] = nJobs
options['maxEvents'] = maxEvents
options['types'] = types
options['labels'] = labels
 
add_charginos (options, [300,500], [10,100,1000])  
            

colors['AMSB_chargino_300GeV_RewtCtau10cm']   = 1
colors['AMSB_chargino_300GeV_RewtCtau100cm']  = 2 
colors['AMSB_chargino_300GeV_RewtCtau1000cm'] = 3 

colors['AMSB_chargino_500GeV_RewtCtau10cm']   = 1
colors['AMSB_chargino_500GeV_RewtCtau100cm']  = 2 
colors['AMSB_chargino_500GeV_RewtCtau1000cm'] = 3 
