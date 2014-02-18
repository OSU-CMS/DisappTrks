# Usage:  getHistIntegrals.py -l configHistIntegralsBkgdEstTot.py 

histName = "numEvents" 
min = 0
max = 10 


input_hists = [    

    { 'condor_dir' : 'JessCopy_bkgdFromDataPresel_11Feb',  
      'dataset' : 'Background',  
      'channel' : 'PreSelection',  
      'histName' : histName,  
      'xlo' : min, 
      'xhi' : max, 
      },

    { 'condor_dir' : 'condor_2014_02_10_BkgdEstPreSelCtrlEcalo', 
      'dataset' : 'Background',  
      'channel' : 'PreSelCtrlEcalo',  
      'histName' : histName,  
      'xlo' : min, 
      'xhi' : max, 
      },

    { 'condor_dir' : 'condor_2014_02_10_BkgdEstPreSelCtrlNMiss', 
      'dataset' : 'Background',  
      'channel' : 'PreSelCtrlNMiss',  
      'histName' : histName,  
      'xlo' : min, 
      'xhi' : max, 
      },


    ]


