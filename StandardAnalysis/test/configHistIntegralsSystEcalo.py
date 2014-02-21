# configHistIntegrals.py
#
# Usage:  getHistIntegrals.py -l configHistIntegralsSystEcalo.py  

channel =  'ZtoMuTrkNoVetoPreSel' 
histName = "trackCaloTot_RhoCorr" 

input_hists = [    

    { 'condor_dir' : 'condor_2014_02_12_ZtoMuTrkNoVetoPreSel',  
      'dataset' : 'SingleMu',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 9.9, 
      },

    { 'condor_dir' : 'condor_2014_02_12_ZtoMuTrkNoVetoPreSel',  
      'dataset' : 'SingleMu',
      'channel' : channel, 
      'histName' : 'trackEta', 
      'xlo' : -3, 
      'xhi' :  3, 
      },

    { 'condor_dir' : 'condor_2014_02_12_ZtoMuTrkNoVetoPreSel',  
      'dataset' : 'Background',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 9.9, 
      },

    { 'condor_dir' : 'condor_2014_02_12_ZtoMuTrkNoVetoPreSel',  
      'dataset' : 'Background',
      'channel' : channel, 
      'histName' : 'trackEta', 
      'xlo' : -3, 
      'xhi' :  3, 
      },


    ]


