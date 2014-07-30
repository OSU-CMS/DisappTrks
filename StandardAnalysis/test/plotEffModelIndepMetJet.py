#!/usr/bin/env python
#

cutName = "basic"  

# ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 5 -l plotEffModelIndepMetJet.py  -o condor/condor_2014_07_24_ModelIndepMetJet/eff_histogramsRebin5TGraph.root  
## # ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 5 -l plotEffModelIndepMetJet.py  -o condor/condor_2014_07_24_ModelIndepMetJet/eff_histogramsRebin5.root  --noTGraph
## input_sources = [

##      { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
##        'dataset' : 'AMSB_chargino_300GeV_RewtCtau10cm',
##        'num_channel' : 'ModelIndepMetJet', 
##        'den_channel' : 'ModelIndepGen',
##        'legend_entry' : '300 GeV, 10 cm',  
##        'marker' : 'square',
##        'fill' : 'hollow',
##        'color' : 'red', 
##            },
##      { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
##        'dataset' : 'AMSB_chargino_300GeV_RewtCtau100cm',
##        'num_channel' : 'ModelIndepMetJet', 
##        'den_channel' : 'ModelIndepGen',
##        'legend_entry' : '300 GeV, 100 cm',  
##        'marker' : 'circle',
##        'fill' : 'hollow',
##        'color' : 'blue', 
##            },
##      { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
##        'dataset' : 'AMSB_chargino_300GeV_RewtCtau1000cm',
##        'num_channel' : 'ModelIndepMetJet', 
##        'den_channel' : 'ModelIndepGen',
##        'legend_entry' : '300 GeV, 1000 cm',  
##        'marker' : 'triangle',
##        'fill' : 'hollow',
##        'color' : 'black', 
##            },

##      ]

# ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 5 -l plotEffModelIndepMetJet.py  -o condor/condor_2014_07_24_ModelIndepMetJet/eff_histograms500GeVRebin5TGraph.root  
## # ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -b 5 -l plotEffModelIndepMetJet.py  -o condor/condor_2014_07_24_ModelIndepMetJet/eff_histograms500GeVRebin5.root  --noTGraph
## input_sources = [

##      { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
##        'dataset' : 'AMSB_chargino_500GeV_RewtCtau10cm',
##        'num_channel' : 'ModelIndepMetJet', 
##        'den_channel' : 'ModelIndepGen',
##        'legend_entry' : '500 GeV, 10 cm',  
##        'marker' : 'square',
##        'fill' : 'hollow',
##        'color' : 'red', 
##            },
##      { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
##        'dataset' : 'AMSB_chargino_500GeV_RewtCtau100cm',
##        'num_channel' : 'ModelIndepMetJet', 
##        'den_channel' : 'ModelIndepGen',
##        'legend_entry' : '500 GeV, 100 cm',  
##        'marker' : 'circle',
##        'fill' : 'hollow',
##        'color' : 'blue', 
##            },
##      { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
##        'dataset' : 'AMSB_chargino_500GeV_RewtCtau1000cm',
##        'num_channel' : 'ModelIndepMetJet', 
##        'den_channel' : 'ModelIndepGen',
##        'legend_entry' : '500 GeV, 1000 cm',  
##        'marker' : 'triangle',
##        'fill' : 'hollow',
##        'color' : 'black', 
##            },

##      ]


# ~/workdirTemplateDisTrk]$ makeEfficiencyPlots.py -f -b 5 -l plotEffModelIndepMetJet.py  -o condor/condor_2014_07_24_ModelIndepMetJet/eff_histograms100cmRebin5.root  --noTGraph
input_sources = [

     { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
       'dataset' : 'AMSB_chargino_100GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepMetJet', 
       'den_channel' : 'ModelIndepGen',
       'legend_entry' : '100 GeV, 100 cm',  
       'marker' : 'square',
       'fill' : 'solid',
       'color' : 'black', 
           },
     { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
       'dataset' : 'AMSB_chargino_200GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepMetJet', 
       'den_channel' : 'ModelIndepGen',
       'legend_entry' : '100 GeV, 100 cm',  
       'marker' : 'square',
       'fill' : 'solid',
       'color' : 'red', 
           },
     { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
       'dataset' : 'AMSB_chargino_300GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepMetJet', 
       'den_channel' : 'ModelIndepGen',
       'legend_entry' : '100 GeV, 100 cm',  
       'marker' : 'square',
       'fill' : 'solid',
       'color' : 'blue', 
           },
     { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
       'dataset' : 'AMSB_chargino_400GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepMetJet', 
       'den_channel' : 'ModelIndepGen',
       'legend_entry' : '100 GeV, 100 cm',  
       'marker' : 'square',
       'fill' : 'hollow',
       'color' : 'black', 
           },
     { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
       'dataset' : 'AMSB_chargino_500GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepMetJet', 
       'den_channel' : 'ModelIndepGen',
       'legend_entry' : '100 GeV, 100 cm',  
       'marker' : 'square',
       'fill' : 'hollow',
       'color' : 'red', 
           },
     { 'condor_dir' : 'condor_2014_07_24_ModelIndepMetJet',
       'dataset' : 'AMSB_chargino_600GeV_RewtCtau100cm',
       'num_channel' : 'ModelIndepMetJet', 
       'den_channel' : 'ModelIndepGen',
       'legend_entry' : '100 GeV, 100 cm',  
       'marker' : 'square',
       'fill' : 'hollow',
       'color' : 'blue', 
           },

     ]



