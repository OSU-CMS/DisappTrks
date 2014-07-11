#!/usr/bin/env python

from systematicConfig_common import *

makeRewtdPlot = False

systematic_name = "NMissOut"

channelNoCuts = "NoCutsFilterMCTrack"  # eventually use this 

ratioHistFile = "../data/NHitsMissingOuterSF_elecTagProbeNorm.root" 
ratioHistName = "ratio"  

histRewtName = "trackNHitsMissingOuter"  
histMin = 0
histMax = 16

central_condor_dir = WellsDir+"JessCopy_fullSelectionWithEcalGapNoCorr"  
central_gen_condor_dir = WellsDir+"condor_2014_07_10_NoCutsFilterMCTrack"  # correct
#central_gen_condor_dir = WellsDir+"condor_2014_07_09_NoCutsSignal"  # testing
# plus_gen_condor_dir = JessDir+"ecaloVaryCorrNormNoCuts"


