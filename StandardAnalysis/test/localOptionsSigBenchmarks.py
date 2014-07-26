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
 
add_charginos (options, [100,200,300,400,500,600], [3,10,30,100,300,1000])

