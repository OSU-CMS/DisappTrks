
#!/usr/bin/env python

# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/systematicConfig_pileup.py

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

datasets = [
##     'AMSB_mGrav32K_0p5ns',
##     'AMSB_mGrav32K_1ns',
##     'AMSB_mGrav32K_5ns',

##     'AMSB_mGrav50K_0p5ns',
##     'AMSB_mGrav50K_1ns',
##     'AMSB_mGrav50K_5ns',

## #    'AMSB_mGrav61K_0p2ns',
## ##     'AMSB_mGrav61K_0p5ns',
## ##     'AMSB_mGrav61K_1ns',
## ##     'AMSB_mGrav61K_5ns',

##     'AMSB_mGrav75K_0p5ns',
##     'AMSB_mGrav75K_1ns',
##     'AMSB_mGrav75K_5ns',

    'AMSB_mGrav100K_0p5ns',
    'AMSB_mGrav100K_1ns',
    'AMSB_mGrav100K_5ns',

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

#add_stops (options, [200], [1.0,10.0,100.0])
#add_stops (options, [200], [0.2])
#add_stops (options, [200,300,400,500,600,700,800], [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0,100.0])


systematic_name = "IsrRewtPt"
#channel = "FullSelection"
channel = "FullSelectionFilterMC"
usePdfWt = False  


## # For variation using compareIsr75KStdVsDnRatio.root:  
## minus_condor_dir   = "condor_2014_03_07_FullSelSystSig_IsrVary"  
## central_condor_dir = "condor_2014_02_22_FullSelSystSig_NMissOutNoCorr"  
## plus_condor_dir    = "condor_2014_03_07_FullSelSystSig_IsrVary" 

## # For variation using compareIsr150KStdVsDnRatio.root:  
## minus_condor_dir   = "condor_2014_04_07_FullSelSystSig_IsrVary"  
## central_condor_dir = "condor_2014_02_22_FullSelSystSig_NMissOutNoCorr"  
## plus_condor_dir    = "condor_2014_04_07_FullSelSystSig_IsrVary" 

## # Sanity check that no variation gives the correct result:
## # It does!  (2014-04-07)  
## minus_condor_dir   = "condor_2014_04_07_FullSelSystSig_NoVary" 
## central_condor_dir = "condor_2014_02_22_FullSelSystSig_NMissOutNoCorr"  
## plus_condor_dir    = "condor_2014_04_07_FullSelSystSig_NoVary"  

# Use different ratio histograms for each mass point  
minus_condor_dir   = "condor_2014_04_08_FullSelSystSig_IsrVaryTuneUE" 
central_condor_dir = "condor_2014_04_08_FullSelSystSig_NoVary"   
plus_condor_dir    = "condor_2014_04_08_FullSelSystSig_IsrVaryUpTuneUE" 

## ## # Use TuneZ2Star 
## minus_condor_dir   = "condor_2014_04_08_FullSelSystSig_IsrVaryTuneZ2Star" 
## central_condor_dir = "condor_2014_04_08_FullSelSystSig_NoVary"   
## plus_condor_dir    = "condor_2014_04_08_FullSelSystSig_IsrVaryUpTuneZ2Star"  



#########
# Section below to be used for reweighting of totalMuonPt distribution
#########
condor_dir = 'condor_2014_04_11_ZToMuMuIsrStudy'
channel =  'ZtoMuMuIsrStudy'
#histName = "totalMuonPt_Reweighted"
histName = "numEvents"
xlo =  0
xhi =  500

input_hists = [

    { 'dataset' : 'DoubleMu_22Jan2013', 
      },

    { 'dataset' : 'Background',
      },

    ]





