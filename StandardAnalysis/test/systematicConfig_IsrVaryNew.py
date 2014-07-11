#!/usr/bin/env python

from systematicConfig_common import *

makeRewtdPlot = False

systematic_name = "Isr"

channel = "FullSelectionFilterMC"  
channelNoCuts = "NoCutsFilterMCTrack"  # eventually use this 

ratioHistFile = "../data/isrVarySFNorm.root" 
ratioHistName = "ratio"  

histRewtName = "totalMcparticlePt"  

histMin = 0
histMax = 510  

#central_condor_dir = WellsDir+"JessCopy_fullSelectionWithEcalGapNoCorr"  
central_condor_dir = WellsDir+"condor_2014_07_10_FullSelectionFilterMCSignal"  
central_gen_condor_dir = WellsDir+"condor_2014_07_10_NoCutsFilterMCTrack"  # correct
#central_gen_condor_dir = WellsDir+"condor_2014_07_09_NoCutsSignal"  # testing
# plus_gen_condor_dir = JessDir+"ecaloVaryCorrNormNoCuts"


