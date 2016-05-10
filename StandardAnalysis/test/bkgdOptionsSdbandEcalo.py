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
    'MET' :  { 'inputDir'   : 'bkgdCtrlChannelsWithFiducial_76X',   
               'datasetsIn'  : ['MET_2015D'],   
               'scale_factor' :       1.0,   
               'scale_factor_error' : 0.0,   
               'channel_map' : {   
    'CandTrkEcaloSdbandPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
               },   
       
    'ElecBkgd' :  { 'inputDir'   : 'bkgdCtrlChannelsWithFiducial_76X',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.00105017823723,   
                    'scale_factor_error' :  0.000310461227766,   
                    'channel_map' : {   
    'ElecCtrlSelectionPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                    },   
       
    'MuonBkgd' :  { 'inputDir'   : 'bkgdCtrlChannelsWithFiducial_76X',   
                    'datasetsIn'  : ['MET_2015D'],   
                    'scale_factor' :        0.0,   
                    'scale_factor_error' :  2.67875278162e-05,   
                    'channel_map' : {   
    'MuonCtrlSelectionPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                    },   
       
    'TauBkgd' :  { 'inputDir'   : 'bkgdCtrlChannelsWithFiducial_76X',   
                   'datasetsIn'  : ['MET_2015D'],   
                   'scale_factor' :        0.0462962962963,   
                   'scale_factor_error' :  0.0311619698883,   
                   'channel_map' : {   
    'TauCtrlSelectionPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                   },   
       
       
       
    'FakeMuMuBkgd' :  { 'inputDir'   : 'ZtoMuMuTrk_76X',   
                    'datasetsIn'  : ['SingleMu_2015D'],   
                    'scale_factor' :        0.490734603053,   
                    'scale_factor_error' :  0.000726406991797,   
                    'channel_map' : {   
    'ZtoMuMuCandTrkEcaloSdbandPlotter' : ['CandTrkEcaloSdbandPlotter'],   
    }   
                    },   
       
       
    }   
