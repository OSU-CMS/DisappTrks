#!/usr/bin/env python

import os
import re
import math
from OSUT3Analysis.Configuration.configurationOptions import *  # Needed if you want to modify (not replace) one of the parameters.
from DisappTrks.SignalMC.signalCrossSecs import *

# Produce this file with:
# /afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV4/CMSSW_5_3_11/src/DisappTrks/SignalMC/test > grep "Filter efficiency" AMSB_chargino_*GeV_ctau*cm_FilterSumPt50__FilterEff/res/CMSSW_1.stdout > filterEff.txt
filterEffFile = os.environ['CMSSW_BASE']+'/src/DisappTrks/SignalMC/data/filterEff.txt'  

fin = open(filterEffFile, "r")
for line in fin:
    words = line.split()
    mass =  (re.sub (r"AMSB_chargino_(.*)GeV_ctau(.*)cm.*", r"\1", words[0])) 
    ctau =  (re.sub (r"AMSB_chargino_(.*)GeV_ctau(.*)cm.*", r"\2", words[0]))
    filterEff = float(words[3])  
    dataset = 'AMSB_chargino_' + mass + "GeV_ctau" + ctau + "cm"
    longDataset = dataset_names[dataset]
    xsecTot = float(signal_cross_sections[mass]['value'])
    xsecFiltered = xsecTot * filterEff 
    command = "osudb -x " + str(xsecFiltered) + " update " + longDataset
#    print "Debug:  found line: " + line
#    print "Found mass = " + mass + "; ctau = " + ctau + "; dataset = " + dataset + "; longDataset = "  + longDataset + "; xsecTot = " + str(xsecTot) + "; filterEff = " + str(filterEff) + "; xsecFiltered = " + str(xsecFiltered)
    print "Command = " + command
    os.system(command)  
#    print "\n\n\n"
    
fin.close()


# Now register NoFilter datasets
masses = [
    "200",
    "500",
    ]

ctaus = [
    "1000",
    "100",
    "30",
    "10",
    ]
    
for mass in masses:
    for ctau in ctaus:
        dataset = 'AMSB_chargino_' + str(mass) + "GeV_ctau" + str(ctau) + "cmNoFilter"
        longDataset = dataset_names[dataset]
        xsecTot = float(signal_cross_sections[mass]['value'])
        command = "osudb -x " + str(xsecTot) + " update " + longDataset
        print "Command = " + command
        os.system(command)
        
        

