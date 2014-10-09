#!/usr/bin/env python

# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/systematicConfig_pileup.py

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from systematicConfig_common import *


systematic_name = "PDFWt"
usePdfWt = True  

central_condor_dir = JessDir+"/pdfSyst_23June"  

