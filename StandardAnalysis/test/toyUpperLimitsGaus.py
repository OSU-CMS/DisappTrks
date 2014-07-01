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
#from scipy.stats import normal

import matplotlib.pyplot as plt

#from ROOT import TF1, TMath

## print(poisson.rvs(1,2,size=30))
## s = np.random.poisson(1.139, 10000)
## count, bins, ignored = plt.hist(s, 14, normed=True)
## plt.show()

Nunderlimit  = 0
Noverobserved = 0

method = "Gaus"

verbose = False

ul68CLobs0 = 1.139 # 68% CL upper limit on observation of 0, from https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp    
Nobs = 0  # number of observed events in each sample  

## GausMean = [20.0, 20.0, 20.0, 5.0]
## GausWidth = [1.0, 5.0, 10.0, 2.0]  

GausMean = [20.0, 30.0, 5.0, 1.0]
GausWidth = [1.0, 2.0, 5.0, 0.5 ] 

## GausMean =  [20.0, 20.0, 20.0, 20.0]
## GausWidth = [1.0, 1.0, 1.0, 1.0] 

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
#samples = [ (100, 1.0)] # simplest case, check #1
#samples = [ (100, 10.0)] # simplest case, check #1
#samples = [ (50, 1.0), (50, 1.0)] # check #2
#samples = [ (25, 1.0), (75, 1.0)] # check #2
#samples = [ (25, 5.0), (75, 5.0)] # check #2
#samples = [ (50, 1.0), (50, 1.0), (50, 1.0)] # check #2
#samples = [ (50, 10.0), (50, 10.0)] # check #3
#samples = [ (50, 1.0), (50, 2.0)] # check #4
#samples = [ (50, 1.0), (50, 10.0)] # check #4
#samples = [ (65, 1.0), (15, 1.0), (10, 1.0), (10, 1.0) ]   # lumi wt set to 1
#samples = [ (65, 0.5), (15, 0.5), (10, 0.5), (10, 0.5) ]   
samples = [ (65, 0.4), (15, 1.9), (10, 0.8), (10, 0.1) ]   # composition in preselection  

# Assume in the search region that 0 events are observered.  

#for i in range(len(samples)):
#    print samples[i][1]  

totyieldCtrl = 0
for (y,wt) in samples: 
    totyieldCtrl += y 

upperlimit = 0  
upperlimitCenter = 0  
upperlimitErr = 0  
print "Using samples:  " 
i = 0
for (y,wt) in samples: 
    frac = float(y) / totyieldCtrl
    if method == "Gaus":  
        # See http://mathworld.wolfram.com/NormalSumDistribution.html for linear sum of multiple normal distributions 
        # y = Sum_i (a_i x_i), where a_i are weights (here a_i = wt * frac), and x_i are normal distributions
        # muTot = Sum_i (a_i mu_i)
        # sigmaTot^2 = Sum_i (a_i^2 sigma_i^2)  
        upperlimitCenter += (GausMean[i]) * wt * frac  # linear sum
        upperlimitErr    +=  math.pow(GausWidth[i] * wt * frac, 2)  # sum in quad
    else: 
        print "Error:  invalid method."
        sys.exit(0)
    #    upperlimit += ul  # linear sum  
    #    print "Sample ", str(i), ": fraction = ", str(float(y)/totyieldCtrl), ", lumi wt = ", wt, ", Nobs = ", str(Nobs), ", 68% UL contribution = ", str(ul)
    print "Sample ", str(i), ": fraction = ", str(frac), ", lumi wt = ", wt, ", mu = ", GausMean[i], ", sigma = ", GausWidth[i]  
    i += 1 

upperlimitErr = math.sqrt(upperlimitErr)  

print "Calculated total Gaus mean:  ", upperlimitCenter
print "Calculated total Gaus width:  ", upperlimitErr

upperlimit = upperlimitCenter + upperlimitErr  
lowerlimit = upperlimitCenter - upperlimitErr  


# Uncomment these lines to force the upper limit:  
#forceUpperLimit = 19
#upperlimit = forceUpperLimit  
    
#print "totyieldCtrl=", totyieldCtrl, ", calculated upperlimit=", upperlimit
#print "estimated 68% CL upperlimit for Nobs=0: ", upperlimit
#print "estimated one-sigma (84%) CL upperlimit: ", upperlimit
print "estimated 68% CL interval:      ", lowerlimit, " - ", upperlimit


#fun = TF1("fun", "TMath::Poisson(x,1.139)", 0, 100);   # continuous Poisson

ntrials = 100000
#ntrials = 10
trialyields = []  
for iT in range(ntrials):
    totyield = 0
    if method == "Gaus": 
        i = 0
        randSamp = random.random()  # random number between 0, 1  
        sampFrac = 0
        for (y,wt) in samples: 
            if verbose:
                print "  sampFrac = ", sampFrac, ", (sampFrac + (float(y) / totyieldCtrl)) = ", str((sampFrac + (float(y) / totyieldCtrl)))  
            frac = float(y) / totyieldCtrl
            ## # Choose a sample at random, based on the relative composition  
            ## if randSamp > sampFrac and randSamp < (sampFrac + (float(y) / totyieldCtrl)) : 
            ##     #            totyield += np.random.gamma(Nobs + 1, wt) # gamma 
            ##     totyield += np.random.normal(GausMean[i] * wt, GausWidth[i] * wt)  
            ##     if verbose:
            ##         print "Adding sample with y = ", str(y)  
            ## sampFrac += float(y) / totyieldCtrl
            samp = np.random.normal(GausMean[i] * wt * frac, GausWidth[i] * wt * frac)  
            totyield += samp
            if verbose:
                print "Adding for iT=", iT, ", samp = ", samp, ", i = ", i 
            i += 1  
              
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

idx16 = int(0.16 * len(trialyields))  # for normal distribution, 84% are below one-sigma (one-sided limit)  
idx84 = int(0.84 * len(trialyields))  # for normal distribution, 84% are below one-sigma (one-sided limit)  
idx68 = int(0.68 * len(trialyields))
idx90 = int(0.90 * len(trialyields))
idx95 = int(0.95 * len(trialyields))
limit16 = trialyields[idx16]
limit68 = trialyields[idx68]
limit84 = trialyields[idx84]
limit90 = trialyields[idx90]
limit95 = trialyields[idx95]
print "68% of trials are in interval:  ", limit16, " - ", limit84 
#print "84% of trials are below:  ", limit84  
## print "90% of trials are below:  ", limit90  
## print "95% of trials are below:  ", limit95  


## count, bins, ignored = plt.hist(trialyields, 100, normed=False) 
## plt.show()                                                                                                                                          


    
