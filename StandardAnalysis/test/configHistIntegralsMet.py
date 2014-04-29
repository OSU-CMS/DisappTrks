# Usage:  getHistIntegrals.py -l configHistIntegralsMet.py

condor_dir = 'condor_2014_04_28_PreSelectionNoMet' 
channel =  'PreSelectionNoMet'
histName = "metPt"


input_hists = [    

    { 'condor_dir' : condor_dir, 
      'dataset' : 'AMSB_mGrav50K_0p5ns',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 501, 
      },
    { 'condor_dir' : condor_dir, 
      'dataset' : 'AMSB_mGrav50K_0p5ns',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 220, 
      'xhi' : 501, 
      },
    { 'condor_dir' : condor_dir, 
      'dataset' : 'AMSB_mGrav50K_0p5ns',
      'channel' : channel, 
      'histName' : 'numEvents',  
      'xlo' : 0, 
      'xhi' : 10, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'AMSB_mGrav50K_1ns',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 501, 
      },
    { 'condor_dir' : condor_dir, 
      'dataset' : 'AMSB_mGrav50K_1ns',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 220, 
      'xhi' : 501, 
      },
    { 'condor_dir' : condor_dir, 
      'dataset' : 'AMSB_mGrav50K_1ns',
      'channel' : channel, 
      'histName' : 'numEvents',  
      'xlo' : 0, 
      'xhi' : 10, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'AMSB_mGrav50K_5ns',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 501, 
      },
    { 'condor_dir' : condor_dir, 
      'dataset' : 'AMSB_mGrav50K_5ns',
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : 220, 
      'xhi' : 501, 
      },
    { 'condor_dir' : condor_dir, 
      'dataset' : 'AMSB_mGrav50K_5ns',
      'channel' : channel, 
      'histName' : 'numEvents',  
      'xlo' : 0, 
      'xhi' : 10, 
      },



    ]


