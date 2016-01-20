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
    'MET' :  { 'inputDir'   : 'candTrkEcaloSdband',   
               'datasetsIn'  : ['MET_2015D'],   
               'scale_factor' :       1.0,   
               'scale_factor_error' : 0.0,   
               'channel_map' : {   
    'CandTrkEcaloSdbandPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
               },   
       
    'ElecBkgd' :  { 'inputDir'   : 'elecCtrlSelection',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.00534579063707,   
                    'scale_factor_error' :  0.000837685597082,   
                    'channel_map' : {   
    'ElecCtrlSelectionPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                    },   
       
    'MuonBkgd' :  { 'inputDir'   : 'muonCtrlSelection',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.0,   
                    'scale_factor_error' :  3.86183454733e-05,   
                    'channel_map' : {   
    'MuonCtrlSelectionPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                    },   
       
    'TauBkgd' :  { 'inputDir'   : 'tauCtrlSelection',   
                   'datasetsIn'  : ['MET_2015D'],   
                   'scale_factor' :        0.00778015839792,   
                   'scale_factor_error' :  0.00119623453534,   
                   'channel_map' : {   
    'TauCtrlSelectionPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                   },   
       
       
       
    'FakeMuMuBkgd' :  { 'inputDir'   : 'ZtoMuMuCandTrkSdband',   
                    'datasetsIn'  : ['SingleMu_2015D'],   
                    'scale_factor' :        2.63909686671,   
                    'scale_factor_error' :  0.00565947398431,   
                    'channel_map' : {   
    'ZtoMuMuCandTrkEcaloSdbandPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                    },   
       
       
    }   
