#!/usr/bin/env python3

# Toy script to determine the upper limit on the bkgd sum, for the PAS.
# Allow an arbitrary number of samples with Poisson distributions, with different upper limits.
# Each contributes with an equal weight.

# To set up ROOT libraries, first configure with ~/cms/root534/root] hwwulsin% source /Users/hwwulsin/cms/root534/root/bin/thisroot.csh

import sys
import random
import math
import numpy as np
from scipy.stats import poisson
from scipy.stats import gamma

#import matplotlib.pyplot as plt

from ROOT import TF1, TMath

from OSUT3Analysis.Configuration.formattingUtilities import *
from amsbLimitConfigBkgds import *

verbose = False

def get68CLRange(useSyst):
    ntrials = 100000
    #ntrials = 2
    trialyields = []
    for iT in range(ntrials):
        totyield = 0
        for bkgd in backgrounds:
            N     = float(backgrounds[bkgd]['N'])
            alpha = float(backgrounds[bkgd]['alpha'])
            if useSyst:
                systErr = float(background_systematics[bkgd]['value']) - 1.0
                scale = np.random.normal(1.0, systErr)
                if scale < 0:
                    scale = 0.01  # set to small number
                alpha *= scale
            totyield += np.random.gamma(((float(N) + 1.0)), alpha)
        if verbose:
            print "totyield = ", totyield
        trialyields.append(totyield)
        ## if verbose:
        ##     print "\n\n\n\n"

    trialyields.sort()
    #print trialyields

    idx16 = int(0.16 * len(trialyields))
    idx50 = int(0.50 * len(trialyields))
    idx68 = int(0.68 * len(trialyields))
    idx84 = int(0.84 * len(trialyields))
    idx90 = int(0.90 * len(trialyields))
    idx95 = int(0.95 * len(trialyields))
    limit16 = trialyields[idx16]
    limit50 = trialyields[idx50]
    limit68 = trialyields[idx68]
    limit84 = trialyields[idx84]
    limit90 = trialyields[idx90]
    limit95 = trialyields[idx95]
    print "16% of trials are below:  ", limit16
    print "50% of trials are below:  ", limit50
    print "68% of trials are below:  ", limit68
    print "84% of trials are below:  ", limit84
    print "90% of trials are below:  ", limit90
    print "95% of trials are below:  ", limit95
    print "68% confidence interval:  [", limit16, ", ", limit84, "]  "

    errStatUp = limit84 - limit50
    errStatDn = limit50 - limit16


    print "68% confidence interval:  [", limit16, ", ", limit84, "]  "

    range68 = (limit50, limit16, limit84)
    return range68

    ## count, bins, ignored = plt.hist(trialyields, 100, normed=False)
    ## plt.show()

def getBkgdSummLineForTable():
    range68Stat = get68CLRange(False)
    range68Tot  = get68CLRange(True)

    central = range68Stat[0]
    errStatUp = range68Stat[2] - central
    errStatDn = central - range68Stat[1]
    errTotUp = range68Tot[2] - central
    errTotDn = central - range68Tot[1]
    errSystUp = math.sqrt(math.pow(errTotUp,2) - math.pow(errStatUp,2))
    errSystDn = math.sqrt(math.pow(errTotDn,2) - math.pow(errStatDn,2))
    errSystAvg = 0.5*(errSystUp + errSystDn)


    line = "background sum & \\multicolumn{2}{c}{ $ " + str(round_sigfigs(central, 2)) + " (^{+" + str(round_sigfigs(errStatUp,2)) + "}_{-" + str(round_sigfigs(errStatDn,1)) + "})_{\\rm stat} " + " \\pm " + str(round_sigfigs(errSystAvg,1)) + "_{\\rm syst} $ } \\\\  \n"
    line += "%background sum & \\multicolumn{2}{c}{ $ $" + str(round_sigfigs(central, 2)) + " (^{+" + str(round_sigfigs(errTotUp,2)) + "}_{-" + str(round_sigfigs(errTotDn,1)) + "})_{\\rm stat+syst} $ }  \\\\  \n"
    return line

# Uncomment the following lines to run in standalone mode:  > ./toyUpperLimitsBkgdSum.py
## line = getBkgdSummLineForTable()
## print line



