# Usage:  getHistIntegrals.py -l configHistIntegralsBkgdEst.py 

#condor_dir = 'condor_2014_01_13_BkgdEstFromData3'  
#condor_dir = 'condor_2014_01_15_BkgdEstFromData4'
condor_dir = 'condor_2014_01_15_BkgdEstFromData5'  
channel =  'PreSelection' 
histName = "numEvents" 
min = 0
max = 10 


input_hists = [    

    { 'condor_dir' : condor_dir, 
      'dataset' : 'ElecBkgd',  
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : min, 
      'xhi' : max, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'MuonBkgd',  
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : min, 
      'xhi' : max, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'TauBkgd',  
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : min, 
      'xhi' : max, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'FakeBkgd',  
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : min, 
      'xhi' : max, 
      },

    { 'condor_dir' : condor_dir, 
      'dataset' : 'OthrBkgd',  
      'channel' : channel, 
      'histName' : histName,  
      'xlo' : min, 
      'xhi' : max, 
      },


##     { 'condor_dir' : condor_dir, 
##       'dataset' : 'ElecBkgdHiPt',  
##       'channel' : channel, 
##       'histName' : histName,  
##       'xlo' : min, 
##       'xhi' : max, 
##       },

##     { 'condor_dir' : condor_dir, 
##       'dataset' : 'MuonBkgdHiPt',  
##       'channel' : channel, 
##       'histName' : histName,  
##       'xlo' : min, 
##       'xhi' : max, 
##       },

##     { 'condor_dir' : condor_dir, 
##       'dataset' : 'TauBkgdHiPt',  
##       'channel' : channel, 
##       'histName' : histName,  
##       'xlo' : min, 
##       'xhi' : max, 
##       },

##     { 'condor_dir' : condor_dir, 
##       'dataset' : 'OthrBkgdHiPt',  
##       'channel' : channel, 
##       'histName' : histName,  
##       'xlo' : min, 
##       'xhi' : max, 
##       },

    ]


