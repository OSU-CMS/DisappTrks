#!/usr/bin/env python

# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/systematicConfig_pileup.py

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from systematicConfig_common import *
import os

## usePdfWt = False
useEfficiency = True
usePdfWt = False

systematic_name = "NMissOut"
#channel = "FullSelection"
#channelNoCuts = "NoCuts"

# For muon tag-probe correction:
## minus_condor_dir   = "condor_2014_02_22_FullSelSystSig_NMissOutWithCorr" 
## central_condor_dir = "condor_2014_02_22_FullSelSystSig_NMissOutNoCorr"
## plus_condor_dir    = "condor_2014_02_22_FullSelSystSig_NMissOutWithCorr"

# For electron tag-probe correction:  
minus_condor_dir   = JessDir+"nMissOutCorrNorm_v2" 
#minus_condor_dir   = JessDir+"nMissOutVaryCorr" 
central_condor_dir = JessDir+"fullSelectionWithEcalGapNoCorr"
plus_condor_dir    = JessDir+"nMissOutCorrNorm_v2"
#plus_condor_dir    = JessDir+"nMissOutVaryCorr"

central_gen_condor_dir = WellsDir+"condor_2014_07_09_NoCutsSignal" 
plus_gen_condor_dir = WellsDir+"condor_2014_07_09_NoCutsSignal_NmissoutReweight"
