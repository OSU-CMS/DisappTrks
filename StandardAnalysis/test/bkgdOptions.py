# Table produced with makeANTables.py  
#!/usr/bin/env python  
# ../scripts/bkgdFromData.py -l bkgdOptions.py -c condor_2014_MM_DD_BkgdEstFullSel   
# mergeOutput.py -q -C -s FakeBkgd -l localOptionsBkgdEst.py -c condor_2014_MM_DD_BkgdEstFullSel   
# makePlots.py       -l localOptionsBkgdEst.py -c condor_2014_MM_DD_BkgdEstFullSel -o stacked_histograms.root   
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
                    'scale_factor_error' :  6.29392607659e-05,   
                    'channel_map' : {   
    'FullSelectionElecPreveto' : ['FullSelection'],   
    }   
                    },   
       
    'MuonBkgd' :  { 'inputDir'   : JessDir + 'fullSelectionMuPrevetoSkim_24June',   
                    'datasetsIn'  : ['MET'],   
                    'scale_factor' :        0.000155747403082,   
                    'scale_factor_error' :  0.000365649916287,   
                    'channel_map' : {   
    'FullSelectionMuPreveto' : ['FullSelection'],   
    }   
                    },   
       
    'TauBkgd' :  { 'inputDir'   : JessDir +  'fullSelectionTauPrevetoSkim_24June',   
                   'datasetsIn'  : ['MET'],   
                   'scale_factor' :        0.0,   
                   'scale_factor_error' :  0.0190329742492,   
                   'channel_map' : {   
    'FullSelectionTauPreveto' : ['FullSelection'],   
    }   
                   },   
       
       
       
    'FakeMuMuBkgd' :  { 'inputDir'   : JessDir + 'ztoMuMuFakeTrkNHits5',   
                    'datasetsIn'  : ['SingleMu'],   
                    'scale_factor' :        0.00370161027977,   
                    'scale_factor_error' :  0.00210887082788,   
                    'channel_map' : {   
    'ZtoMuMuFakeTrkNHits5' : ['FullSelection'],   
    }   
                    },   
    'FakeEEBkgd' :  { 'inputDir'   : JessDir + 'ztoEEFakeTrk3456NHit',   
                    'datasetsIn'  : ['SingleElectron'],   
                    'scale_factor' :        0.00370161027977,   
                    'scale_factor_error' :  0.00210887082788,   
                    'channel_map' : {   
    'ZtoEEFakeTrkNHits5' : ['FullSelection'],   
    }   
                    },   
       
       
    }   
