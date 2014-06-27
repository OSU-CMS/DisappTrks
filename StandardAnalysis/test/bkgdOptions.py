# Table produced with makeANTables.py  
#!/usr/bin/env python  
# ../scripts/bkgdFromData.py -l bkgdOptions.py -c condor_2014_MM_DD_BkgdEstFullSel   
# mergeOutput.py -q -C -s FakeBkgd -l localOptionsBkgdEst.py -c condor_2014_MM_DD_BkgdEstFullSel   
# makePlots.py       -l localOptionsBkgdEst.py -c condor_2014_MM_DD_BkgdEstFullSel -o stacked_histogramsRebin10.root -b 10    
# makePlots.py -P paperPlotsOptions.py      
   
import os   
   
cwd = os.getcwd()   
   
if 'wulsin' in cwd:   
    WellsDir = ''     
    JessDir = 'JessCondor/'   
elif 'jbrinson' in cwd:   
    WellsDir = 'WellsCondorNew/'   
    JessDir = ''   
else:   
    print 'Error: could not identify user as wulsin or jbrinson.'   
    os.exit(0)   
       
impurities = []  # not yet implemented   
       
bkgd_sources = {   
    'MET' :  { 'inputDir'   : JessDir+'fullSelectionSkim_24June',   
               'datasetsIn'  : ['MET'],   
               'scale_factor' :       1.0,   
               'scale_factor_error' : 0.0,   
               'channel_map' : {   
    'FullSelection' : ['FullSelection'],   
    }   
               },   
       
    'ElecBkgd' :  { 'inputDir'   : JessDir + 'fullSelectionElecPrevetoSkim_24June',   
                    'datasetsIn'  : ['MET'],   
                    'scale_factor' :        0.0,   
                    'scale_factor_error' :  7.43569832548e-05,   
                    'channel_map' : {   
    'FullSelectionElecPreveto' : ['FullSelection'],   
    }   
                    },   
       
    'MuonBkgd' :  { 'inputDir'   : JessDir + 'fullSelectionMuPrevetoSkim_24June',   
                    'datasetsIn'  : ['MET'],   
                    'scale_factor' :        0.000156267433365,   
                    'scale_factor_error' :  0.000156267433365,   
                    'channel_map' : {   
    'FullSelectionMuPreveto' : ['FullSelection'],   
    }   
                    },   
       
    'TauBkgd' :  { 'inputDir'   : JessDir +  'fullSelectionTauPrevetoSkim_24June',   
                   'datasetsIn'  : ['MET'],   
                   'scale_factor' :        9.16877356537e-05,   
                   'scale_factor_error' :  0.0209135329003,   
                   'channel_map' : {   
    'FullSelectionTauPreveto' : ['FullSelection'],   
    }   
                   },   
       
       
       
    'FakeMuMuBkgd' :  { 'inputDir'   : JessDir + 'ztoMuMuFakeTrk_24June',   
                    'datasetsIn'  : ['SingleMu'],   
                    'scale_factor' :        0.179528098569,   
                    'scale_factor_error' :  0.00014672139258,   
                    'channel_map' : {   
    'ZtoMuMuFakeTrk' : ['FullSelection'],   
    }   
                    },   
    'FakeEEBkgd' :  { 'inputDir'   : JessDir + 'ztoEEFakeTrk3456NHit',   
                    'datasetsIn'  : ['SingleElectron'],   
                    'scale_factor' :        0.179528098569,   
                    'scale_factor_error' :  0.00014672139258,   
                    'channel_map' : {   
    'ZtoEEFakeTrk' : ['FullSelection'],   
    }   
                    },   
       
       
    }   
