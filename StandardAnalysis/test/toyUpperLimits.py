#!/usr/bin/env python

# Toy script to determine the upper limit on an observation of 0 events,
# for an arbitrary number of samples with different lumi weights
# and different relative contributions in a control region, assumed to be the same contribution in the search region.

import sys
import random
import math
import numpy as np
from scipy.stats import poisson
from scipy.stats import gamma

import matplotlib.pyplot as plt

#from ROOT import TF1, TMath

## print(poisson.rvs(1,2,size=30))
## s = np.random.poisson(1.139, 10000)
## count, bins, ignored = plt.hist(s, 14, normed=True)
## plt.show()

Nunderlimit  = 0
Noverobserved = 0

#method = "flat"
method = "Poisson"

verbose = False

ul68CLobs0 = 1.139 # 68% CL upper limit on observation of 0, from https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp
Nobs = 0  # number of observed events in each sample

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
samples = [ (100, 1.0)] # simplest case, check #1
#samples = [ (100, 10.0)] # simplest case, check #1
#samples = [ (50, 1.0), (50, 1.0)] # check #2
#samples = [ (25, 1.0), (75, 1.0)] # check #2
#samples = [ (25, 5.0), (75, 5.0)] # check #2
#samples = [ (50, 1.0), (50, 1.0), (50, 1.0)] # check #2
#samples = [ (50, 10.0), (50, 10.0)] # check #3
#samples = [ (50, 1.0), (50, 100.0)] # check #4
#samples = [ (50, 1.0), (50, 10.0)] # check #4
#samples = [ (65, 1.0), (15, 1.0), (10, 1.0), (10, 1.0) ]   # lumi wt set to 1
#samples = [ (65, 0.5), (15, 0.5), (10, 0.5), (10, 0.5) ]   # lumi wt set to 1
#samples = [ (65, 0.4), (15, 1.9), (10, 0.8), (10, 0.1) ]   # composition in preselection

# Assume in the search region that 0 events are observered.

#for i in range(len(samples)):
#    print samples[i][1]

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
        ul = ul68CLobs0 * wt * y / totyieldCtrl # linear sum; get 68% UL from https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp    # original
    else:
        print "Error:  invalid method."
        sys.exit(0)
    upperlimit += ul  # linear sum
    print "Sample ", str(i), ": fraction = ", str(float(y)/totyieldCtrl), ", lumi wt = ", wt, ", Nobs = ", str(Nobs), ", 68% UL contribution = ", str(ul)
    i += 1

# Uncomment these lines to force the upper limit:
#forceUpperLimit = 19
#upperlimit = forceUpperLimit

#print "totyieldCtrl=", totyieldCtrl, ", calculated upperlimit=", upperlimit
print "estimated 68% CL upperlimit for Nobs=0: ", upperlimit


#fun = TF1("fun", "TMath::Poisson(x,1.139)", 0, 100);   # continuous Poisson

ntrials = 100000
trialyields = []
for iT in range(ntrials):
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
            ## if randSamp > sampFrac and randSamp < (sampFrac + (float(y) / totyieldCtrl)) :
            ##     #                totyield += float(wt) * np.random.poisson(ul68CLobs0)  # discrete Poisson
            ##     #                totyield += float(wt) * fun.GetRandom()   # continuous Poisson
            ##     totyield += np.random.gamma(Nobs + 1, wt) # gamma
            ##     if verbose:
            ##         print "Adding sample with y = ", str(y)
            ## sampFrac += float(y) / totyieldCtrl
            frac = float(y) / totyieldCtrl
            totyield += np.random.gamma(((float(Nobs) + 1.0) * frac), wt)
    else:
        print "Error:  invalid method."
        sys.exit(0)

    if verbose:
        print "totyield = ", totyield
    if totyield < upperlimit:
        Nunderlimit += 1
    if totyield > 0:
        Noverobserved += 1
    trialyields.append(totyield)
    if verbose:
        print "\n\n\n\n"

#    print 'totyield=', totyield, ' upperlimit=', upperlimit

# Old print outs:
## print 'ntrials = ', ntrials, ', Nunderlimit =', Nunderlimit, " fraction under 68% CL = ", str(float(Nunderlimit) / ntrials)
## print 'ntrials = ', ntrials, ', Noverobserved =', Noverobserved, " fraction of trials with more than 0 observed (should be 68%) = ", str(float(Noverobserved) / ntrials)

trialyields.sort()
#print trialyields

idx68 = int(0.68 * len(trialyields))
idx90 = int(0.90 * len(trialyields))
idx95 = int(0.95 * len(trialyields))
limit68 = trialyields[idx68]
limit90 = trialyields[idx90]
limit95 = trialyields[idx95]
print "68% of trials are below:  ", limit68
print "90% of trials are below:  ", limit90
print "95% of trials are below:  ", limit95


count, bins, ignored = plt.hist(trialyields, 100, normed=False)
plt.show()



