#!/usr/bin/env python

# Copied from https://raw.github.com/DisplacedSUSY/DisplacedSUSY/master/LimitsCalculation/test/systematicConfig_pileup.py

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from systematicConfig_common import *

systematic_name = "PDFWt"
usePdfWt = True  

condor_dir_CTEQ  = JessDir+"/condor_2014_10_06_pdfSyst_CTEQ"  
condor_dir_MSTW  = JessDir+"/condor_2014_10_06_pdfSyst_MSTW"  
condor_dir_NNPDF = JessDir+"/condor_2014_10_06_pdfSyst_NNPDF"  

