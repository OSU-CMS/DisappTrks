#!/usr/bin/env python

# Usage:
# ../scripts/makeSystTextFileNew.py -l systematicConfig_Nmissin.py
from systematicConfig_common import *


makeRewtdPlot = False

systematic_name = "Nmissin" 

channelNoCuts = "NoCutsFilterMCTrack"  # eventually use this 

# Produce ratio hist with:
## ~/workdirTemplateDisTrk]$ getRatioFromCanvas.py -i condor/condor_2014_06_02_PreSelectionMuonNoMissInMid/stacked_histogramsNorm.root -o condor/condor_2014_06_02_PreSelectionMuonNoMissInMid/trackNHitsMissingInnerRatio.root -n OSUAnalysis/PreSelectionMuonNoMissInMid/trackNHitsMissingInner
## ~/workdirTemplateDisTrk]$ cp condor/condor_2014_06_02_PreSelectionMuonNoMissInMid/trackNHitsMissingInnerRatio.root ../data/
ratioHistFile = "../data/trackNHitsMissingInnerRatio.root"  
ratioHistName = "ratio"  

histRewtName = "trackNHitsMissingInner"  
histMin = 0
histMax = 16

central_condor_dir = WellsDir+"JessCopy_fullSelectionWithEcalGapNoCorr"  
central_gen_condor_dir = WellsDir+"condor_2014_07_10_NoCutsFilterMCTrack"  # correct




