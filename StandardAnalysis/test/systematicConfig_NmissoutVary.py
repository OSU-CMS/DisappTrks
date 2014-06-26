
#!/usr/bin/env python

# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/systematicConfig_pileup.py

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

makeRewtdPlot = True
#makeRewtdPlot = False

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

def add_charginos (options, masses, ctaus):
    for mass in masses:
        for ctau in ctaus:
            datasetName       = 'AMSB_chargino_' + str (mass) + "GeV_RewtCtau" + str (ctau)  + "cm"
            sourceDatasetName = 'AMSB_chargino_' + str (mass) + "GeV_ctau" + str(math.floor(source_chargino_ctau(ctau))).rstrip('0').rstrip('.') + "cm"
            options['datasets'].append (datasetName)
            options['dataset_names'][datasetName] = options['dataset_names'][sourceDatasetName]
            options['nJobs']        [datasetName] =  5
            options['maxEvents']    [datasetName] = -1
            options['types']        [datasetName] = "signalMC"
            options['labels']       [datasetName] = str (mass) + " GeV #chi^{#pm} (#LTc#tau#GT = " + str (ctau) + " cm)"
            print "Adding dataset:  " + datasetName + "; sourceDatasetName=" + sourceDatasetName + "; dataset_name[sourceDatasetName]=" + options['dataset_names'][sourceDatasetName]
            
#add_charginos (options, [100,200,300,400,500,600], [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000])
## mass point used for plot in AN
add_charginos (options, [400], [30])
            

systematic_name = "NmissoutRewt"
channel = "FullSelection"
#channel = "FullSelectionFilterMC"
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
#minus_condor_dir   = "condor_2014_04_08_FullSelSystSig_IsrVaryTuneUE" 
#central_condor_dir = "condor_2014_04_08_FullSelSystSig_NoVary"   
#plus_condor_dir    = "condor_2014_04_08_FullSelSystSig_IsrVaryUpTuneUE" 

## ## # Use TuneZ2Star 
## minus_condor_dir   = "condor_2014_04_08_FullSelSystSig_IsrVaryTuneZ2Star" 
## central_condor_dir = "condor_2014_04_08_FullSelSystSig_NoVary"   
## plus_condor_dir    = "condor_2014_04_08_FullSelSystSig_IsrVaryUpTuneZ2Star"  



#########
# Section below to be used for reweighting of totalMuonPt distribution
#########
#condor_dir = 'JessCopy_elecBkgd_9Feb' 
condor_dir = 'ztoETrkEIdNoVetoPresel' 
channel =  'ZtoETrkEIdNoVetoPresel' 
#histName = "totalMuonPt_Reweighted"
histName = "numEvents"
xlo =  0
xhi =  500

input_hists = [

    { 'dataset' : 'Single_Electron', 
      },

    { 'dataset' : 'Background',
      },

    ]





