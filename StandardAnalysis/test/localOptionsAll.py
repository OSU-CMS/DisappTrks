#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.  
from OSUT3Analysis.Configuration.processingUtilities import *
from lumiMet2012 import *

config_file = "trackAnalyzerStandard_cfg.py"

datasets = [
    
##     'AMSB_mGrav50K_0p5ns',
##     'AMSB_mGrav50K_1ns',
##     'AMSB_mGrav50K_5ns',

##     # put bkgd datasets in roughly ascending order of size of contribution after preselection
    'QCD',    
    'SingleTop',
    'TTbar',
    'ZJetsToNuNu', 
    'DY',  
    'Diboson',
    'WjetsHighPt',

    'MET',
    ]

composite_dataset_definitions['Background'] = [
    'QCD',    
    'SingleTop',
    'TTbar',
    'ZJetsToNuNu', 
    'DY', 
    'Diboson',
    'WjetsHighPt',
    ]

labels['WjetsHighPt'] = "W#rightarrowl#nu"

composite_dataset_definitions['QCD'] = [
    'QCD_80to120',
    'QCD_120to170',
    'QCD_170to300',
    'QCD_300to470',
    'QCD_470to600',
    'QCD_600to800',
    'QCD_800to1000',
    'QCD_1000to1400',
    'QCD_1400to1800',
    'QCD_1800'
    ]


histsToBlind = [
#    'CaloTot', 
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
            options['labels']       [datasetName] = str (mass) + " GeV #chi^{#pm} (c#tau = " + str (ctau) + " cm)"
            print "Adding dataset:  " + datasetName + "; sourceDatasetName=" + sourceDatasetName + "; dataset_name[sourceDatasetName]=" + options['dataset_names'][sourceDatasetName]
            
# Do all lifetimes:
add_charginos (options, [100,200,300,400,500,600], [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])

# Do a subset of signal lifetimes:  
#add_charginos (options, [100,200,300,400,500,600], [3,10,30,100,300,1000])







