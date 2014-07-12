#!/usr/bin/env python

# Usage:
# ../scripts/makeSystTextFileNew.py -l systematicConfig_Nmissmid.py
from systematicConfig_common import *


makeRewtdPlot = False

systematic_name = "Nmissmid" 

channelNoCuts = "NoCutsFilterMCTrack"  # eventually use this 

# Produce ratio hist with:
## ~/workdirTemplateDisTrk]$ getRatioFromCanvas.py -i condor/condor_2014_06_02_PreSelectionMuonNoMissInMid/stacked_histogramsNorm.root -o condor/condor_2014_06_02_PreSelectionMuonNoMissInMid/trackNHitsMissingMiddleRatio.root -n OSUAnalysis/PreSelectionMuonNoMissInMid/trackNHitsMissingMiddle
## ~/workdirTemplateDisTrk]$ cp condor/condor_2014_06_02_PreSelectionMuonNoMissInMid/trackNHitsMissingMiddleRatio.root ../data/  
ratioHistFile = "../data/trackNHitsMissingMiddleRatio.root"  
ratioHistName = "ratio"  

histRewtName = "trackNHitsMissingMiddle"  
histMin = 0
histMax = 16

central_condor_dir = WellsDir+"JessCopy_fullSelectionWithEcalGapNoCorr"  
central_gen_condor_dir = WellsDir+"condor_2014_07_10_NoCutsFilterMCTrack"  




