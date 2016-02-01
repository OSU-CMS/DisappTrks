# Table produced with makeANTables.py  
#!/usr/bin/env python  
# ../scripts/bkgdFromData.py -l bkgdOptionsSdbandNmissout.py -w condor_2016_MM_DD_BkgdEstFullSel   
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
    'MET' :  { 'inputDir'   : 'candTrkNMissOutSdband',   
               'datasetsIn'  : ['MET_2015D'],   
               'scale_factor' :       1.0,   
               'scale_factor_error' : 0.0,   
               'channel_map' : {   
    'CandTrkNMissOutSdbandPlotter' : ['CandTrkNMissOutSdbandPlotter'],   
    }   
               },   
       
    'ElecBkgd' :  { 'inputDir'   : 'elecCtrlSelection',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.00208130235614,   
                    'scale_factor_error' :  0.000576662345777,   
                    'channel_map' : {   
    'ElecCtrlSelectionPlotter' : ['CandTrkNMissOutSdbandPlotter'],   
    }   
                    },   
       
    'MuonBkgd' :  { 'inputDir'   : 'muonCtrlSelection',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        3.3892560583e-05,   
                    'scale_factor_error' :  7.75639419197e-05,   
                    'channel_map' : {   
    'MuonCtrlSelectionPlotter' : ['CandTrkNMissOutSdbandPlotter'],   
    }   
                    },   
       
    'TauBkgd' :  { 'inputDir'   : 'tauCtrlSelection',   
                   'datasetsIn'  : ['MET_2015D'],   
                   'scale_factor' :        0.00221157390343,   
                   'scale_factor_error' :  0.00131424671026,   
                   'channel_map' : {   
    'TauCtrlSelectionPlotter' : ['CandTrkNMissOutSdbandPlotter'],   
    }   
                   },   
       
       
       
    'FakeMuMuBkgd' :  { 'inputDir'   : 'ZtoMuMuCandTrkSdband',   
                    'datasetsIn'  : ['SingleMu_2015D'],   
                    'scale_factor' :        2.63909686671,   
                    'scale_factor_error' :  0.00565947398431,   
                    'channel_map' : {   
    'ZtoMuMuCandTrkNMissOutSdbandPlotter' : ['CandTrkNMissOutSdbandPlotter'],   
    }   
                    },   
       
       
    }   
