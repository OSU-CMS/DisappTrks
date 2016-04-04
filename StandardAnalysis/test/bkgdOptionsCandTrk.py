# Table produced with makeANTables.py  
#!/usr/bin/env python  
# ../scripts/bkgdFromData.py -l bkgdOptionsCandTrk.py -w condor_2016_MM_DD_BkgdEstFullSel   
# mergeOutput.py -q -C -s FakeBkgd -l localConfigBkgdEst.py -w condor_2016_MM_DD_BkgdEstFullSel  # To combine ee and mumu fake track samples (optional) 
# makePlots.py       -l localConfigBkgdEst.py -w condor_2016_MM_DD_BkgdEstFullSel -o stacked_histograms.root   
# makePlots.py -P paperPlotsOptions.py      
   
import os   
   
cwd = os.getcwd()   
   
if 'wulsin' in cwd:   
    WellsDir = ''     
    AndrewDir = 'hartCondor/'   
elif 'hart' in cwd:   
    WellsDir = 'WellsCondorNew/'   
    AndrewDir = ''   
else:   
    print 'Error: could not identify user as wulsin or hart.'   
    os.exit(0)   
       
impurities = []  # not yet implemented   
       
bkgd_sources = {   
    'MET' :  { 'inputDir'   : 'candTrkSelection_76X',   
               'datasetsIn'  : ['MET_2015D'],   
               'scale_factor' :       1.0,   
               'scale_factor_error' : 0.0,   
               'channel_map' : {   
    'CandTrkSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
               },   
       
    'ElecBkgd' :  { 'inputDir'   : 'leptonControlRegions_76X',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.0207556269614,   
                    'scale_factor_error' :  0.00133799778499,   
                    'channel_map' : {   
    'ElecCtrlSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                    },   
       
    'MuonBkgd' :  { 'inputDir'   : 'leptonControlRegions_76X',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.0,   
                    'scale_factor_error' :  2.55421269489e-05,   
                    'channel_map' : {   
    'MuonCtrlSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                    },   
       
    'TauBkgd' :  { 'inputDir'   : 'leptonControlRegions_76X',   
                   'datasetsIn'  : ['MET_2015D'],   
                   'scale_factor' :        0.186052169772,   
                   'scale_factor_error' :  0.0231537271339,   
                   'channel_map' : {   
    'TauCtrlSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                   },   
       
       
       
    'FakeMuMuBkgd' :  { 'inputDir'   : 'wellsCondor/ZtoMuMuCandTrk',   
                    'datasetsIn'  : ['SingleMu_2015D'],   
                    'scale_factor' :        1.3419234778,   
                    'scale_factor_error' :  0.00150559004352,   
                    'channel_map' : {   
    'ZtoMuMuCandTrkPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                    },   
       
       
    }   
