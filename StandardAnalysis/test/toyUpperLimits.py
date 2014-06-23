#!/usr/bin/env python

import sys
import random
import math
import numpy as np
from scipy.stats import poisson

import matplotlib.pyplot as plt

## print(poisson.rvs(1,2,size=30))
## s = np.random.poisson(1.139, 10000)
## count, bins, ignored = plt.hist(s, 14, normed=True)
## plt.show()

Nunderlimit  = 0

#method = "flat"
method = "Poisson"  

verbose = False


# in samples, each pair represents:
# * the first element is the yield of the different samples in a control region, 
# which is expected to reflect the relative composition in the signal region  
# * the second element is the lumi weight  

# From preselection, yields are roughly in the proportion:
# 65%:  W+jets;   lumiwt = 0.4
# 15%:  diboson;  lumiwt = 1.9 
# 10%:  Z+jets;   lumiwt = 0.8
# 10%:  TTbar;    lumiwt = 0.1
# lumi weights are approximate  
samples = [ (65, 0.4), (15, 1.9), (10, 0.8), (10, 0.1) ]   # composition in preselection  
#samples = [ (65, 1.0), (15, 1.0), (10, 1.0), (10, 1.0) ]   # lumi wt set to 1
#samples = [ (100, 1.0)] # simplest case, check #1
#samples = [ (50, 1.0), (50, 1.0)] # check #2
#samples = [ (50, 10.0), (50, 10.0)] # check #3
#samples = [ (50, 0.1), (50, 10.0)] # check #4


for i in range(len(samples)):
    print samples[i][1]  

totyieldCtrl = 0
for (y,wt) in samples: 
    totyieldCtrl += y 
    
upperlimit = 0  
print "Using samples:  " 
i = 0
for (y,wt) in samples: 
    if method == "flat": 
        ul = 0.68 * wt * y / totyieldCtrl 
    elif method == "Poisson":  
        ul = 1.139 * wt * y / totyieldCtrl # linear sum; get 68% UL from https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp  
    else: 
        print "Error:  invalid method."
        sys.exit(0)
    upperlimit += ul  # linear sum  
    #    upperlimit = math.sqrt(math.pow(upperlimit,2) + math.pow(ul, 2))  # sum in quadrature
    print "Sample ", str(i), ": fraction = ", str(float(y)/totyieldCtrl), ", lumi wt = ", wt, ", upper limit = ", str(ul)  
    i += 1 

# Uncomment these lines to force the upper limit:  
## forceUpperLimit = 0.88
## upperlimit = forceUpperLimit  
    
print "totyieldCtrl=", totyieldCtrl, " total upperlimit=", upperlimit

ntrials = 10000
trialyields = []  
for iT in range(ntrials):
#for iT in range(10):

    totyield = 0
    if method == "flat": 
        for (y,wt) in samples: 
            totyield += float(wt) * y / totyieldCtrl * random.random()  
    elif method == "Poisson":  
        randSamp = random.random()  # random number between 0, 1  
        if verbose:
            print "iT = ", str(iT), ", randSamp = ", str(randSamp)
        sampFrac = 0
        for (y,wt) in samples: 
            if verbose:
                print "  sampFrac = ", sampFrac, ", (sampFrac + (float(y) / totyieldCtrl)) = ", str((sampFrac + (float(y) / totyieldCtrl)))  
            # Choose a sample at random, based on the relative composition  
            if randSamp > sampFrac and randSamp < (sampFrac + (float(y) / totyieldCtrl)) : 
                totyield += float(wt) * np.random.poisson(1.139)
                if verbose:
                    print "Adding sample with y = ", str(y)  
            sampFrac += float(y) / totyieldCtrl
    else: 
        print "Error:  invalid method."
        sys.exit(0)

    if verbose:
        print "totyield = ", totyield  
    if totyield < upperlimit: 
        Nunderlimit += 1 
    trialyields.append(totyield)
    if verbose:
        print "\n\n\n\n"  

#    print 'totyield=', totyield, ' upperlimit=', upperlimit  

print 'ntrials = ', ntrials, ', Nunderlimit =', Nunderlimit, " fraction under 68% CL = ", str(float(Nunderlimit) / ntrials)  

trialyields.sort()  
#print trialyields

## idx68 = int(0.68 * len(trialyields))
## limit68 = trialyields[idx68]
## print "68% of trials are below:  ", limit68  



    
