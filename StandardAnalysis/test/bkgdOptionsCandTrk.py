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
    'MET' :  { 'inputDir'   : 'candTrkSelection',   
               'datasetsIn'  : ['MET_2015D_05Oct2015'],   
               'scale_factor' :       1.0,   
               'scale_factor_error' : 0.0,   
               'channel_map' : {   
    'CandTrkSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
               },   
       
    'ElecBkgd' :  { 'inputDir'   : 'elecCtrlSelection',   
                    'datasetsIn'  : ['MET_2015D_05Oct2015'],   
                    'scale_factor' :        0.0170313611846,   
                    'scale_factor_error' :  0.00538578929962,   
                    'channel_map' : {   
    'ElecCtrlSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                    },   
       
    'MuonBkgd' :  { 'inputDir'   : 'MuonCtrlSelection',   
                    'datasetsIn'  : ['MET_2015D_05Oct2015'],   
                    'scale_factor' :        0.00466392327056,   
                    'scale_factor_error' :  0.00147486203672,   
                    'channel_map' : {   
    'MuonCtrlSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                    },   
       
    'TauBkgd' :  { 'inputDir'   : 'hartCondor/tauCtrlSelection',   
                   'datasetsIn'  : ['MET_2015D_05Oct2015'],   
                   'scale_factor' :        0.0808763382593,   
                   'scale_factor_error' :  0.0255753437713,   
                   'channel_map' : {   
    'TauCtrlSelectionPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                   },   
       
       
       
    'FakeMuMuBkgd' :  { 'inputDir'   : 'ZtoMuMuDisTrk',   
                    'datasetsIn'  : ['SingleMu_2015D'],   
                    'scale_factor' :        0.646233887509,   
                    'scale_factor_error' :  0.00188361537647,   
                    'channel_map' : {   
    'ZtoMuMuDisTrkPlotter' : ['CandTrkSelectionPlotter'],   
    }   
                    },   
       
       
    }   
