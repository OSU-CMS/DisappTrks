# Table produced with makeANTables.py  
#!/usr/bin/env python  
# ../scripts/bkgdFromData.py -l bkgdOptionsSdbandEcalo.py -w condor_2016_MM_DD_BkgdEstFullSel   
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
    'MET' :  { 'inputDir'   : 'ecaloSideband_76X',   
               'datasetsIn'  : ['MET_2015D'],   
               'scale_factor' :       1.0,   
               'scale_factor_error' : 0.0,   
               'channel_map' : {   
    'CandTrkEcaloSdbandPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
               },   
       
    'ElecBkgd' :  { 'inputDir'   : 'leptonControlRegions_76X',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.00523818456198,   
                    'scale_factor_error' :  0.00067579279341,   
                    'channel_map' : {   
    'ElecCtrlSelectionPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                    },   
       
    'MuonBkgd' :  { 'inputDir'   : 'leptonControlRegions_76X',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.0,   
                    'scale_factor_error' :  2.55421269489e-05,   
                    'channel_map' : {   
    'MuonCtrlSelectionPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                    },   
       
    'TauBkgd' :  { 'inputDir'   : 'leptonControlRegions_76X',   
                   'datasetsIn'  : ['MET_2015D'],   
                   'scale_factor' :        0.0342844379867,   
                   'scale_factor_error' :  0.00998100260159,   
                   'channel_map' : {   
    'TauCtrlSelectionPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                   },   
       
       
       
    'FakeMuMuBkgd' :  { 'inputDir'   : 'wellsCondor/ZtoMuMuCandTrkSdband',   
                    'datasetsIn'  : ['SingleMu_2015D'],   
                    'scale_factor' :        1.3419234778,   
                    'scale_factor_error' :  0.00150559004352,   
                    'channel_map' : {   
    'ZtoMuMuCandTrkEcaloSdbandPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                    },   
       
       
    }   
