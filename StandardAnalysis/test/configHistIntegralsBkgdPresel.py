# configHistIntegrals.py
#
# Usage:  getHistIntegrals.py -l configHistIntegralsBkgdPresel.py

condor_dir = 'JessCopy_preselId_11Feb' 
channel1 =  'PreSelIdOther' 
channel2 =  'PreSelIdTau' 
histName = "trackCaloTot_RhoCorrWide" 
histName2 = "trackNHitsMissingOuter" 

input_hists = [    

    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background', 
      'channel' : channel1, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 500, 
##       'rebin' : 20, 
##       'splitBins' : False, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background', 
      'channel' : channel1, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 79, 
##       'rebin' : 20, 
##       'splitBins' : True, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background', 
      'channel' : channel2, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 600, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background', 
      'channel' : channel2, 
      'histName' : histName,  
      'xlo' : 0, 
      'xhi' : 79, 
      },


    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background', 
      'channel' : channel1, 
      'histName' : histName2,  
      'xlo' : 0, 
      'xhi' : 15, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background', 
      'channel' : channel1, 
      'histName' : histName2,  
      'xlo' : 3, 
      'xhi' : 15, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background', 
      'channel' : channel2, 
      'histName' : histName2,  
      'xlo' : 0, 
      'xhi' : 15,
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'Background', 
      'channel' : channel2, 
      'histName' : histName2,  
      'xlo' : 3, 
      'xhi' : 15, 
      },

    ]


