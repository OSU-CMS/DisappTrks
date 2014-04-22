# configHistIntegrals.py
#
# Usage:  getHistIntegrals.py -l configHistIntegralsSystEcalo.py  

condor_dir = 'condor_2014_03_18_ZtoMuMuFakeTrkNHits4NoEcalo'
channel =  'ZtoMuMuFakeTrkNHits4NoEcalo'
histName = "trackCaloTot_RhoCorr"


input_hists = [    

    { 'condor_dir' : condor_dir, 
      'dataset' : 'SingleMu',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 9.9, 
      },

    { 'condor_dir' : condor_dir,
      'dataset' : 'SingleMu',
      'channel' : channel,
      'histName' : histName,
      'xlo' : 0,
      'xhi' : 110,    # include the overflow
      },
    
    { 'condor_dir' : condor_dir, 
      'dataset' : 'SingleMu',
      'channel' : channel, 
      'histName' : 'trackEta', 
      'xlo' : -3, 
      'xhi' :  3, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 9.9, 
      },

    { 'condor_dir' : condor_dir,
      'dataset' : 'Background',
      'channel' : channel,
      'histName' : histName,
      'xlo' : 0,
      'xhi' : 110,    # include the overflow
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background',
      'channel' : channel, 
      'histName' : 'trackEta', 
      'xlo' : -3, 
      'xhi' :  3, 
      },


    ]


