#!/usr/bin/env python

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

#from localOptionsAll import *
from lumiMet2012 import *

bkgd_datasets = [
    'QCD',
    'SingleTop',
    'TTbar',
    'ZJetsToNuNu',
    'DY',
    'Diboson',
    'WjetsHighPt',
    ]


datasets = []  

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
            
signal_datasets = datasets
## [
##     'AMSB_chargino_400GeV_RewtCtau10cm',
##     'AMSB_chargino_400GeV_RewtCtau100cm',
##     'AMSB_chargino_400GeV_RewtCtau1000cm',
##     ]

add_charginos (options, [400], [10,100,1000])
colors['AMSB_chargino_400GeV_RewtCtau10cm']   = 1 # black
colors['AMSB_chargino_400GeV_RewtCtau100cm']  = 2 # red
colors['AMSB_chargino_400GeV_RewtCtau1000cm'] = 4 # blue



###################################################
### REQUIRED arguments for each input histogram ###
###################################################

#   Variable name (type)
########################
# condor_dir (string)
# channel (string)
# name (string)
# output_dir (string)

####################################################
### OPTIONAL arguments for each input histogram  ###
####################################################

#   Variable name (type)
########################
# output_name (string)

# datasets (dictionary)
# setYMin,setYMax (double)
# setLogY (bool)
# rebinFactor (double)

# normalizeFactor (double)
# normalizeToUnitArea (bool)
# normalizeToData (bool)

# noStack (bool)
# makeRatioPlots (bool)
# makeDiffPlots (bool)
# ratioYRange (double)
# ratioRelErrMax (double)
# printYields (bool)
# includeSystematics (bool)
# addOverUnderFlow (bool)
# sortOrderByYields (bool)
# makeFancy (bool)


paper_histograms = [

## FIGURE 1: SIGNAL GENERATOR-LEVEL  
  {
    'condor_dir' : 'condor_2014_06_24_NoCutsFilterMC',
    'channel' : 'NoCutsFilterMC',
    'name' : 'mcparticlePt',  
    'output_name': 'mcparticlePt_NoCutsFilterMC', 
    'output_dir' : 'figuresAN',
    'datasets' : signal_datasets,
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : False,
    'makeFancy' : True,
  },
  {
    'condor_dir' : 'condor_2014_06_24_NoCutsFilterMC',
    'channel' : 'NoCutsFilterMC',
    'name' : 'mcparticleEta',  
    'output_name': 'mcparticleEta_NoCutsFilterMC', 
    'output_dir' : 'figuresAN',
    'datasets' : signal_datasets,
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : False,
    'makeFancy' : True,
  },


]


