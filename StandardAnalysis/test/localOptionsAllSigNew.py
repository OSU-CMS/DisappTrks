#!/usr/bin/env python

from localOptionsAll import * 

#config_file = "trackAnalyzerSystSig_cfg.py"  

datasets = [

##     'AMSB_chargino_100GeV_ctau10cm',
##     'AMSB_chargino_100GeV_ctau100cm',
##     'AMSB_chargino_100GeV_ctau1000cm',

##     'AMSB_chargino_200GeV_ctau10cm',
##     'AMSB_chargino_200GeV_ctau30cm',
##     'AMSB_chargino_200GeV_ctau100cm',
##     'AMSB_chargino_200GeV_ctau1000cm',

## ##     'AMSB_chargino_200GeV_ctau10cmNoFilter',
## ##     'AMSB_chargino_200GeV_ctau30cmNoFilter',
## ##     'AMSB_chargino_200GeV_ctau100cmNoFilter',
## ##     'AMSB_chargino_200GeV_ctau1000cmNoFilter',

## ##     'AMSB_chargino_200GeV_ctau30cmFilter',

##     'AMSB_chargino_300GeV_ctau10cm',
##     'AMSB_chargino_300GeV_ctau100cm',
##     'AMSB_chargino_300GeV_ctau1000cm',

##     'AMSB_chargino_400GeV_ctau10cm',
##     'AMSB_chargino_400GeV_ctau100cm',
##     'AMSB_chargino_400GeV_ctau1000cm',

##     'AMSB_chargino_500GeV_ctau10cm',
##     'AMSB_chargino_500GeV_ctau100cm',
##     'AMSB_chargino_500GeV_ctau1000cm',

## ##     'AMSB_chargino_500GeV_ctau10cmNoFilter',
## ##     'AMSB_chargino_500GeV_ctau30cmNoFilter',
## ##     'AMSB_chargino_500GeV_ctau100cmNoFilter',
## ##     'AMSB_chargino_500GeV_ctau1000cmNoFilter',

##     'AMSB_chargino_600GeV_ctau10cm',
##     'AMSB_chargino_600GeV_ctau100cm',
##     'AMSB_chargino_600GeV_ctau1000cm', 

    ]


colors['AMSB_mGrav100K_1.0cm'] = 1
colors['AMSB_mGrav100K_2.0cm'] = 2
colors['AMSB_mGrav100K_5.0cm'] = 3
colors['AMSB_mGrav100K_10.0cm'] = 4
colors['AMSB_mGrav100K_20.0cm'] = 6

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
                                                                                                            

# all samples:
#add_charginos (options, [400], [20,90,100])  
#add_charginos (options, [400], [5,10,50,100,500,1000])  
#add_charginos (options, [200], [10,30,100,1000])  
#add_charginos (options, [500], [10,30,100,1000])  
#add_charginos (options, [200], [1000])  
#add_charginos (options, [200,400,600], [10000])  


add_charginos (options, [100,200,300,400,500,600], [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])  
#add_charginos (options, [100,200,300,400,500,600], [15,150])  


#add_charginos (options, ["32K", "50K", "75K", "100K", "125K", "150K"], [0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
# testing:
#add_charginos (options, ["100K"], [1.5, 5.0, 10.0, 20.0, 50.0, 100.0, 175.0, 200.0, 300.0])
#add_charginos (options, ["100K"], [50.0, 100.0, 175.0, 200.0])  
            
colors['AMSB_chargino_200GeV_RewtCtau1000cm'] = 1
colors['AMSB_chargino_400GeV_RewtCtau1000cm'] = 2 
colors['AMSB_chargino_600GeV_RewtCtau1000cm'] = 3 

colors['AMSB_chargino_200GeV_RewtCtau10000cm'] = 1
colors['AMSB_chargino_400GeV_RewtCtau10000cm'] = 2 
colors['AMSB_chargino_600GeV_RewtCtau10000cm'] = 3 


colors['AMSB_chargino_400GeV_RewtCtau5cm'] = 1 
colors['AMSB_chargino_400GeV_RewtCtau10cm'] = 2 
colors['AMSB_chargino_400GeV_RewtCtau50cm'] = 3 
colors['AMSB_chargino_400GeV_RewtCtau100cm'] = 4 
colors['AMSB_chargino_400GeV_RewtCtau500cm'] = 6 
colors['AMSB_chargino_400GeV_RewtCtau1000cm'] = 7 
colors['AMSB_chargino_400GeV_RewtCtau2000cm'] = 8 
