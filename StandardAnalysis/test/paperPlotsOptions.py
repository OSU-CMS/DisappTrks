#!/usr/bin/env python

# Usage:
# makePlots.py -P paperPlotsOptions.py
# AN-12-400/trunk> scp wulsin@cms-in0.mps.ohio-state.edu:"~/workdirTemplateDisTrk/figures/figuresAN/{*pdf}" figures/ 

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *

from localOptionsAll import *
from localOptionsBkgdEst import *
from lumiMet2012 import *

import os

cwd = os.getcwd()
print "Current directory: " + cwd 

if "wulsin" in cwd:
    WellsDir = ""
    JessDir = "JessCondor/"
elif "jbrinson" in cwd:
    WellsDir = "WellsCondorNew/"
    JessDir = "" 
else:
    print "Error:  could not identify user as wulsin or jbrinson."  
    os.exit(0)  

bkgd_datasets = [
    'QCD',
    'SingleTop',
    'TTbar',
    'ZJetsToNuNu',
    'DY',
    'Diboson',
    'WjetsHighPt',
    ]

bkgdEst_datasets = [
    'MET',
    'ElecBkgd',
    'MuonBkgd',
    'TauBkgd',
    'FakeBkgd',
    ]


datasets = []  


def add_charginos (options, masses, ctaus):
    for mass in masses:
        for ctau in ctaus:
            datasetName       = 'AMSB_chargino_' + str (mass) + "GeV_RewtCtau" +                  str (ctau)  + "cm"
            sourceDatasetName = 'AMSB_chargino_' + str (mass) + "GeV_ctau" + str(math.floor(source_chargino_ctau(ctau))).rstrip('0').rstrip('.') + "cm"
            options['datasets'].append (datasetName)
            options['dataset_names'][datasetName] = options['dataset_names'][sourceDatasetName]
#            options['nJobs']        [datasetName] =  5
#            options['maxEvents']    [datasetName] = -1
            options['types']        [datasetName] = "signalMC"
            options['labels']       [datasetName] = str (mass) + " GeV #chi^{#pm} (c#tau = " + str (ctau) + " cm)"
            print "Adding dataset:  " + datasetName + "; sourceDatasetName=" + sourceDatasetName + "; dataset_name[sourceDatasetName]=" + options['dataset_names'][sourceDatasetName]


            

options = {}
options['datasets'] = datasets
options['dataset_names'] = dataset_names
options['types'] = types
options['labels'] = labels
#options['composite_dataset_definitions'] = composite_dataset_definitions
#options['nJobs'] = nJobs
#options['maxEvents'] = maxEvents


## [
##     'AMSB_chargino_400GeV_RewtCtau10cm',
##     'AMSB_chargino_400GeV_RewtCtau100cm',
##     'AMSB_chargino_400GeV_RewtCtau1000cm',
##     ]

add_charginos (options, [400], [10,100,1000])
signal_datasets = datasets

datasetsVaryMass = [ ]  
optionsVaryMass = {}
optionsVaryMass['datasets'] = datasetsVaryMass  
optionsVaryMass['dataset_names'] = dataset_names
optionsVaryMass['types'] = types
optionsVaryMass['labels'] = labels
add_charginos (optionsVaryMass, [200,400,600], [100])  
signalVaryMass_datasets = datasetsVaryMass  

colors['AMSB_chargino_400GeV_RewtCtau10cm']   = 1 # black
colors['AMSB_chargino_400GeV_RewtCtau100cm']  = 2 # red
colors['AMSB_chargino_400GeV_RewtCtau1000cm'] = 4 # blue

colors['AMSB_chargino_200GeV_RewtCtau100cm'] = 1 # black
colors['AMSB_chargino_400GeV_RewtCtau100cm'] = 2 # red
colors['AMSB_chargino_600GeV_RewtCtau100cm'] = 4 # blue


sigBkgd_datasets = signal_datasets + bkgd_datasets 

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
    'condor_dir' : WellsDir+'condor_2014_06_24_NoCutsFilterMCb',
    'channel' : 'NoCutsFilterMC',
    'name' : 'mcparticlePt',  
    'output_name': 'mcparticlePt_NoCutsFilterMC', 
    'output_dir' : 'figuresAN',
    'normalizeToUnitArea' : True, 
    'datasets' : signalVaryMass_datasets,
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : False,
    'makeFancy' : True,
  },
  {
    'condor_dir' : WellsDir+'condor_2014_06_24_NoCutsFilterMCb',
    'channel' : 'NoCutsFilterMC',
    'name' : 'mcparticleEta',  
    'output_name': 'mcparticleEta_NoCutsFilterMC', 
    'output_dir' : 'figuresAN',
    'normalizeToUnitArea' : True, 
    'datasets' : signalVaryMass_datasets,
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : False,
    'makeFancy' : True,
  },

  #  met DeltaPhi N-1
  {
    'condor_dir' : WellsDir+'condor_2014_04_30_PreSelectionNoMetDPhi_NoJetJetDPhi',
    'channel' : 'PreSelectionNoMetDPhi',
    'name' : 'metDeltaPhiMin2Jets',  
    'output_name': 'metDeltaPhiMin2Jets_PreSelectionNoMetDPhi', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,  
#    'rebinFactor' : 20,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,
    'makeFancy' : True,
  },

  # dijetDPhi N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_04_30_PreSelectionNoMetDPhi_NoJetJetDPhi',
    'channel' : 'PreSelectionNoJetJetDPhi_NoMetDPhi',
    'name' : 'dijetDeltaPhiMax',  
    'output_name': 'dijetDeltaPhiMax_PreSelectionNoJetJetDPhi_NoMetDPhi', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 20,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


# Bkgd jobs are missing:  
  # met N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_04_28_PreSelectionNoMet',
    'channel' : 'PreSelectionNoMet',
    'name' : 'metPt',  
    'output_name': 'metPt_PreSelectionNoMet', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 10,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # jet pT N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_05_28_PreSelectionNoJet_LeadingJetFilterBugFix', 
    'channel' : 'PreSelectionNoJet_LeadingJetFilter', 
    'name' : 'secondaryJetPt',  
    'output_name': 'secondaryJetPt_PreSelectionNoJet_LeadingJetFilter', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 10,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,
    'setYMax' : 0.6,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },

  # track pT N-1  
  {
    'condor_dir' : WellsDir+'JessCopy_preselNoPtForAN_18Feb', 
    'channel' : 'PreSelectionNoPt', 
    'name' : 'trackPt',  
    'output_name': 'trackPt_PreSelectionNoPt', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 5,
    'normalizeToUnitArea' : True, 
    'setYMin' : 1.0e-5,
    'setYMax' : 1.0e5,
    'setLogY' : True,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # track NHits N-1  
  {
    'condor_dir' : WellsDir+'JessCopy_preselPlotsForAN_18Feb', 
    'channel' : 'PreSelectionNoNHit', 
    'name' : 'trackNumValidHits',  
    'output_name': 'trackNumValidHits_PreSelectionNoNHit', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
#    'rebinFactor' : 5,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # track NHitsMissIn N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_04_17_PreSelectionNoMissIn', 
    'channel' : 'PreSelectionNoMissIn', 
    'name' : 'trackNHitsMissingInner', 
    'output_name': 'trackNHitsMissingInner_PreSelectionNoMissIn',
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
#    'rebinFactor' : 5,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # track NHitsMissMid N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_04_17_PreSelectionNoMissMid', 
    'channel' : 'PreSelectionNoMissMid', 
    'name' : 'trackNHitsMissingMiddle', 
    'output_name': 'trackNHitsMissingMiddle_PreSelectionNoMissMid', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
#    'rebinFactor' : 5,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # track relIso N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_04_30_PreSelectionNoTrkJetDR',
    'channel' : 'PreSelectionNoRelIsoRp3', 
    'name' : 'trackRelIsoRp3', 
    'output_name': 'trackRelIsoRp3_PreSelectionNoRelIsoRp3', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 2,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # track deltaR(trk-jet) N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_04_30_PreSelectionNoTrkJetDR',
    'channel' : 'PreSelectionNoTrkJetDR', 
    'name' : 'trackDeltaRMinSubLeadJet', 
    'output_name': 'trackDeltaRMinSubLeadJet_PreSelectionNoTrkJetDR', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 2,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # track DeltaRElec N-1  
  {
    'condor_dir' : JessDir+'preselElecSkim_9Feb', 
    'channel' : 'PreSelectionElec', 
    'name' : 'trackDeltaRMinElecLooseMvaId', 
    'output_name': 'trackDeltaRElec_PreSelectionElec', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 2,
    'normalizeToUnitArea' : True, 
    'setYMin' : 1.0e-6,
    'setYMax' : 1.0e2,
    'setLogY' : True,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # track DeltaRMuon N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_01_19_PreSelectionMuon', 
    'channel' : 'PreSelectionMuon', 
    'name' : 'trackDeltaRMinMuonLooseId', 
    'output_name': 'trackDeltaRMuon_PreSelectionMuon', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 2,
    'normalizeToUnitArea' : True, 
    'setYMin' : 1.0e-6,
    'setYMax' : 1.0e2,
    'setLogY' : True,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # track DeltaRTau N-1  
  {
    'condor_dir' : JessDir+'preselTauSkim_11Feb', 
    'channel' : 'PreSelectionTau', 
    'name' : 'trackDeltaRMinTauLooseHadronicId', 
    'output_name': 'trackDeltaRTau_PreSelectionTau', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 2,
    'normalizeToUnitArea' : True, 
    'setYMin' : 1.0e-6,
    'setYMax' : 1.0e2,
    'setLogY' : True,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },


  # track Ecalo N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_05_06_FullSelectionNoCaloNoMissHit', 
    'channel' : 'FullSelectionNoCalo', 
    'name' : 'trackCaloTot_RhoCorr', 
    'output_name': 'trackCaloTot_RhoCorr_FullSelectionNoCalo', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
    'rebinFactor' : 5,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,  
##     'setYMax' : 1.0e2,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  

    'BkgdLegX1' : 0.7030201,  
    'BkgdLegY1' : 0.5996503,  
    'BkgdLegX2' : 0.9647651,  
    'BkgdLegY2' : 0.9195804,  

    'SigLegX1' : 0.2030201,  
    'SigLegY1' : 0.6346154,  
    'SigLegX2' : 0.5352349,  
    'SigLegY2' : 0.8339161,  
    'SigLineWidth' : 5,  
    'SigLineStyle' : 7,  
    'SigTextSize' : 0.035,  

    'makeFancy' : True,
    'quickRenameX' : 'E_{calo} [GeV]',
    'quickRenameY' : 'Entries / 5 GeV (Unit Area Norm.)',
  },


  # track Nmissout N-1  
  {
    'condor_dir' : WellsDir+'condor_2014_05_06_FullSelectionNoCaloNoMissHit', 
    'channel' : 'FullSelectionNoMissHit', 
    'name' : 'trackNHitsMissingOuter', 
    'output_name': 'trackNHitsMissingOuter_FullSelectionNoMissHit', 
    'output_dir' : 'figuresAN',
    'datasets' : sigBkgd_datasets,
#    'rebinFactor' : 5,
    'normalizeToUnitArea' : True, 
    'setYMin' : 0,  
##     'setYMax' : 1.0e2,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,

    'BkgdLegX1' : 0.7030201,
    'BkgdLegY1' : 0.5996503,
    'BkgdLegX2' : 0.9647651,
    'BkgdLegY2' : 0.9195804,

    'SigLegX1' : 0.2030201,
    'SigLegY1' : 0.6346154,
    'SigLegX2' : 0.5352349,
    'SigLegY2' : 0.8339161,
    'SigLineWidth' : 5,
    'SigLineStyle' : 7,
    'SigTextSize' : 0.035,

    'quickRenameY' : 'Entries / hit (Unit Area Norm.)',
    'makeFancy' : True,
  },



  #  deltaPhi(track-Met):  signal
  {
    'condor_dir' : WellsDir+'condor_2014_02_12_FullSelectionNHits4', 
    'channel' : 'FullSelectionNHits4', 
    'name' : 'trackdPhiMet', 
    'output_name': 'trackdPhiMet_FullSelectionNHits4_signal', 
    'output_dir' : 'figuresAN',
    'datasets' : signal_datasets, 
    'rebinFactor' : 10,
    'normalizeToUnitArea' : False, 
    'setYMin' : 0,  
##     'setYMax' : 1.0e2,
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'makeFancy' : True,
  },



  #  numEvents: data & bkgd estimate (use as sanity check)
  {
    'condor_dir' : WellsDir+'condor_2014_07_03_BkgdEstFullSel', 
    'channel' : 'FullSelection', 
    'name' : 'numEvents', 
    'output_name': 'numEvents_FullSelEst', 
    'output_dir' : 'figuresAN',
    'datasets' : bkgdEst_datasets, 
#    'rebinFactor' : 2,
    'normalizeToUnitArea' : False,
#    'setYMin' : 1e-3,  
#    'setYMax' : 10, 
#    'setLogY' : True,
#    'includeSystematics' : False,
    'addOverUnderFlow' : True,
    'poisErr' : True,  
    'makeFancy' : True,
    'normalizeFactor' : 1.39,  # from slide 16 of https://cms-in0.mps.ohio-state.edu:8080/DisappearingTracks/408 
  },

  #  track pT: data & bkgd estimate 
  {
    'condor_dir' : WellsDir+'condor_2014_07_03_BkgdEstFullSel', 
    'channel' : 'FullSelection', 
    'name' : 'trackPt', 
    'output_name': 'trackPt_FullSelEst', 
    'output_dir' : 'figuresAN',
    'datasets' : bkgdEst_datasets, 
    'rebinFactor' : 2,
    'normalizeToUnitArea' : False, 
    'setYMin' : 1e-3,  
    'setYMax' : 10, 
    'setLogY' : True,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,
    'poisErr' : True,  
    'makeFancy' : True,
    'normalizeFactor' : 1.39,  # from slide 16 of https://cms-in0.mps.ohio-state.edu:8080/DisappearingTracks/408 
    'quickRenameY' : 'Entries / 10 GeV',
    'quickRenameX' : 'track p_{T} [GeV]',
  },

  #  track NHits: data & bkgd estimate 
  {
    'condor_dir' : WellsDir+'condor_2014_06_27_BkgdEstFullSel', 
    'channel' : 'FullSelection', 
    'name' : 'trackNumValidHits', 
    'output_name': 'trackNumValidHits_FullSelEst', 
    'output_dir' : 'figuresAN',
    'datasets' : bkgdEst_datasets, 
#    'rebinFactor' : 10,
    'normalizeToUnitArea' : False, 
##     'setYMin' : 1e-3,  
    'setYMax' : 4, 
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,
    'poisErr' : True,  
    'quickRenameY' : 'Entries / hit',
    'quickRenameX' : 'Number of valid hits',
    'makeFancy' : True,
    'normalizeFactor' : 1.39,  # from slide 16 of https://cms-in0.mps.ohio-state.edu:8080/DisappearingTracks/408 
  },

  #  track NMissOut: data & bkgd estimate 
  {
    'condor_dir' : WellsDir+'condor_2014_07_03_BkgdEstFullSel', 
    'channel' : 'FullSelection', 
    'name' : 'trackNHitsMissingOuter', 
    'output_name': 'trackNHitsMissingOuter_FullSelEst', 
    'output_dir' : 'figuresAN',
    'datasets' : bkgdEst_datasets, 
#    'rebinFactor' : 10,
    'normalizeToUnitArea' : False, 
##     'setYMin' : 1e-3,  
    'setYMax' : 4, 
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,  
    'poisErr' : True,  
    'makeFancy' : True,
    'normalizeFactor' : 1.39,  # from slide 16 of https://cms-in0.mps.ohio-state.edu:8080/DisappearingTracks/408 
    'quickRenameY' : 'Entries / hit',
  },

  #  track Ecalo: data & bkgd estimate 
  {
    'condor_dir' : WellsDir+'condor_2014_07_03_BkgdEstFullSel', 
    'channel' : 'FullSelection', 
    'name' : 'trackCaloTot_RhoCorr', 
    'output_name': 'trackCaloTot_RhoCorr_FullSelEst', 
    'output_dir' : 'figuresAN',
    'datasets' : bkgdEst_datasets, 
#    'rebinFactor' : 10,
    'normalizeToUnitArea' : False, 
##     'setYMin' : 1e-3,  
    'setYMax' : 4, 
    'setXMin' : 0, 
    'setXMax' : 20, 
    'setLogY' : False,
    'includeSystematics' : False,
    'addOverUnderFlow' : True,
    'quickRenameX' : 'E_{calo} [GeV]',
    'poisErr' : True,  
    'makeFancy' : True,
    'normalizeFactor' : 1.39,  # from slide 16 of https://cms-in0.mps.ohio-state.edu:8080/DisappearingTracks/408 
    'quickRenameY' : 'Entries / 1 GeV',
  },





]


