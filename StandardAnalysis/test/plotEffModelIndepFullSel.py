#!/usr/bin/env python
#

cutName = "Disappearing Track"

## ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 10 -l plotEffModelIndepFullSel.py  -o condor/condor_2014_07_26_ModelIndepFullSel/eff_histograms300GeVRebin10TGraph.root  
## ## ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 10 -l plotEffModelIndepFullSel.py  -o condor/condor_2014_07_26_ModelIndepFullSel/eff_histograms300GeVRebin10.root --noTGraph
## input_sources = [

##      { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
##        'dataset' : 'AMSB_chargino_300GeV_RewtCtau1000cm',
##        'num_channel' : 'ModelIndepFullSel', 
##        'den_channel' : 'ModelIndepMetJet',
##        'legend_entry' : '300 GeV, 1000 cm',  
##        'marker' : 'triangle',
##        'fill' : 'hollow',
##        'color' : 'black', 
##            },
##      { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
##        'dataset' : 'AMSB_chargino_300GeV_RewtCtau100cm',
##        'num_channel' : 'ModelIndepFullSel', 
##        'den_channel' : 'ModelIndepMetJet',
##        'legend_entry' : '300 GeV, 100 cm',  
##        'marker' : 'circle',
##        'fill' : 'hollow',
##        'color' : 'blue', 
##            },
##      { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
##        'dataset' : 'AMSB_chargino_300GeV_RewtCtau10cm',
##        'num_channel' : 'ModelIndepFullSel', 
##        'den_channel' : 'ModelIndepMetJet',
##        'legend_entry' : '300 GeV, 10 cm',  
##        'marker' : 'square',
##        'fill' : 'hollow',
##        'color' : 'red', 
##            },

##      ]

## # ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 10 -l plotEffModelIndepFullSel.py  -o condor/condor_2014_07_26_ModelIndepFullSel/eff_histograms500GeVRebin10TGraph.root  
## # ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 10 -l plotEffModelIndepFullSel.py  -o condor/condor_2014_07_26_ModelIndepFullSel/eff_histograms500GeVRebin10.root  --noTGraph
## input_sources = [

##      { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
##        'dataset' : 'AMSB_chargino_500GeV_RewtCtau1000cm',
##        'num_channel' : 'ModelIndepFullSel', 
##        'den_channel' : 'ModelIndepMetJet',
##        'legend_entry' : '500 GeV, 1000 cm',  
##        'marker' : 'triangle',
##        'fill' : 'hollow',
##        'color' : 'black', 
##            },
##      { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
##        'dataset' : 'AMSB_chargino_500GeV_RewtCtau100cm',
##        'num_channel' : 'ModelIndepFullSel', 
##        'den_channel' : 'ModelIndepMetJet',
##        'legend_entry' : '500 GeV, 100 cm',  
##        'marker' : 'circle',
##        'fill' : 'hollow',
##        'color' : 'blue', 
##            },
##      { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
##        'dataset' : 'AMSB_chargino_500GeV_RewtCtau10cm',
##        'num_channel' : 'ModelIndepFullSel', 
##        'den_channel' : 'ModelIndepMetJet',
##        'legend_entry' : '500 GeV, 10 cm',  
##        'marker' : 'square',
##        'fill' : 'hollow',
##        'color' : 'red', 
##            },

##      ]



## ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -f -b 10 -l plotEffModelIndepFullSel.py  -o condor/condor_2014_07_26_ModelIndepFullSel/eff_histograms100cmRebin10.root --noTGraph 
input_sources = [

     { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
       'dataset' : 'AMSB_chargino_100GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepFullSel', 
       'den_channel' : 'ModelIndepMetJet',
       'legend_entry' : '100 GeV, 100 cm',  
       'marker' : 'square',
       'fill' : 'solid',
       'color' : 'black', 
           },
     { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
       'dataset' : 'AMSB_chargino_200GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepFullSel', 
       'den_channel' : 'ModelIndepMetJet',
       'legend_entry' : '200 GeV, 100 cm',  
       'marker' : 'square',
       'fill' : 'solid',
       'color' : 'red', 
           },
     { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
       'dataset' : 'AMSB_chargino_300GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepFullSel', 
       'den_channel' : 'ModelIndepMetJet',
       'legend_entry' : '300 GeV, 100 cm',  
       'marker' : 'square',
       'fill' : 'solid',
       'color' : 'blue', 
           },
     { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
       'dataset' : 'AMSB_chargino_400GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepFullSel', 
       'den_channel' : 'ModelIndepMetJet',
       'legend_entry' : '400 GeV, 100 cm',  
       'marker' : 'circle',
       'fill' : 'hollow',
       'color' : 'black', 
           },
     { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
       'dataset' : 'AMSB_chargino_500GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepFullSel', 
       'den_channel' : 'ModelIndepMetJet',
       'legend_entry' : '500 GeV, 100 cm',  
       'marker' : 'circle',
       'fill' : 'hollow',
       'color' : 'red', 
           },
     { 'condor_dir' : 'condor_2014_07_26_ModelIndepFullSel',
       'dataset' : 'AMSB_chargino_600GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepFullSel', 
       'den_channel' : 'ModelIndepMetJet',
       'legend_entry' : '600 GeV, 100 cm',  
       'marker' : 'circle',
       'fill' : 'hollow',
       'color' : 'blue', 
           },

     ]



