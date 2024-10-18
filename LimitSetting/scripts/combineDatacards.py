#!/usr/bin/env python3

# Script to combine run periods into single cards for running limits.

import os, sys, glob, re, subprocess
from optparse import OptionParser
from threading import Thread, Semaphore, Lock
from multiprocessing import cpu_count

from OSUT3Analysis.Configuration.ProgressIndicator import ProgressIndicator

from DisappTrks.LimitSetting.limitOptions import *

if arguments.limitType not in validLimitTypes:
    print ("\nInvalid or empty limit type to plot (-l). Allowed types:\n")
    print (str(validLimitTypes))
    sys.exit(0)

if arguments.limitType == "wino":
    from DisappTrks.LimitSetting.winoElectroweakLimits import *
elif arguments.limitType == "higgsino":
    from DisappTrks.LimitSetting.higgsinoElectroweakLimits import *

# format the suffix
suffix = ""
if not arguments.suffix:
    if "SUFFIX" in os.environ:
        suffix = os.environ["SUFFIX"]
        print( 'Taking suffix from environment: ' + suffix)
    else:
        print( 'Either provide an input date with "-s" or define the $SUFFIX variable in your environment.')
        sys.exit(1)
else:
    suffix = arguments.suffix
    print( 'Using suffix: ' + suffix)

# check the input directories exist
for combinedCard in datacardCombinations:
    for card in datacardCombinations[combinedCard]:
        if not os.path.exists('limits/limits_' + card + '_' + suffix):
            print( 'The input directory limits/limits_' + card + '_' + suffix + ' is missing! Quitting.')
            sys.exit(1)

# create the output directories
for combinedCard in datacardCombinations:
    if not os.path.exists('limits/limits_' + combinedCard + '_' + suffix):
        os.mkdir('limits/limits_' + combinedCard + '_' + suffix)

def makeCombinedCard (i, N, combinedCard, mass, lifetime, ignoreSignalScaleFactor):
    global semaphore
    global printLock
    global progress

    semaphore.acquire ()

    printLock.acquire ()
    progress.setPercentDone(float(i+1) / N * 100.0)
    progress.printProgress(False)
    printLock.release ()

    sample = ('AMSB' if arguments.limitType == "wino" else 'Higgsino') + '_mChi' + mass + '_' + lifetime.replace('0.', '0p') + 'cm'

    # create the combined card
    outputCardFile = 'limits/limits_' + combinedCard + '_' + suffix + '/datacard_' + sample + '.txt'
    cmd = 'combineCards.py '
    cardsExist = False
    for card in datacardCombinations[combinedCard]:
        inputCardFile = 'limits/limits_' + card + '_' + suffix + '/datacard_' + sample + '.txt'
        # if an input card is missing, skip this bin in the combined card
        # this happens for example with 1000, 1100 GeV cards missing for 2015-6 in the run2 combination
        # for such points we just set the limit using the 2017 bins
        if not os.path.isfile(inputCardFile):
            continue
        else:
            cardsExist = True
        cmd += ' Bin' + card.replace('_', '') + '=' + inputCardFile

    # if no input cards exist, there's nothing to combine
    if not cardsExist:
        semaphore.release()
        return

    subprocess.call(cmd + ' > ' + outputCardFile, shell = True)

    # from the input cards, figure out the original, unscaled yields
    # these are always written as the last line in the card
    realYields = {}
    sumYields = 0.0
    for card in datacardCombinations[combinedCard]:
        inputCardFile = 'limits/limits_' + card + '_' + suffix + '/datacard_' + sample + '.txt'
        if not os.path.isfile(inputCardFile):
            continue
        with open(inputCardFile) as f:
            first = f.readline()
            for last in f: pass
        realYields['Bin' + card.replace('_', '')] = float(last.strip().split()[-1])
        sumYields += realYields['Bin' + card.replace('_', '')]

    # now scale the bins in the combined card so that their total is 10.0 events
    if not ignoreSignalScaleFactor:
        scaleFactor = 10.0 / sumYields if sumYields > 0.0 else 1.0
        scaledYields = {x : realYields[x] * scaleFactor for x in realYields}

        # edit the combined card, replacing the rates -- currently all scaled to 10.0 -- to (realYield * scaleFactor)
        rateLines = subprocess.check_output('sed -n "/^rate/p" ' + outputCardFile, shell = True).split()
        processLines = subprocess.check_output('sed -n "/^process\s*0\s*/p" ' + outputCardFile, shell = True).split()
        binLines = subprocess.check_output('awk "/^bin/{c++; if (c==2) {print}}" ' + outputCardFile, shell = True).split()

        rateLines = [x.decode('utf-8') for x in rateLines][1:] # need to decode, first entry is string 'rate'
        processLines = [x.decode('utf-8') for x in processLines][1:] # need to decode, first entry is string 'process'
        binLines = [x.decode('utf-8') for x in binLines][1:] # need to decode, first entry is string 'bin'

        for iBin in range(len(rateLines)):
            # if this is a signal process (0), replace the rate with this new scaled value
            if processLines[iBin] == '0':
                rateLines[iBin] = str(scaledYields[binLines[iBin]])

        rateLines = ['rate','\t','\t'] + rateLines # re-add the rate at the beginning of the line and "skip" two columns

        # now replace the rates in the combined card
        subprocess.call('sed -i "s/^rate.*/' + ' '.join(rateLines) + '/" ' + outputCardFile, shell = True)

        # also now fix the signalSF file
        subprocess.call('echo ' + str(scaleFactor) + ' > ' + outputCardFile.replace('datacard_', 'signalSF_'), shell = True)

        # find the signal stat lines, since these will need to change
        signalStatLines = subprocess.check_output('sed -n "/^signal_stat_.*gmN.*/p" ' + outputCardFile, shell = True).decode('utf-8')
        signalStatLines = signalStatLines.split('\n')
        for iLine in range(len(signalStatLines)):
            if not signalStatLines[iLine].startswith('signal_stat_Bin'):
                continue
            gmN_number = -1
            stat_idx = -1
            binName = ''
            lineEntries = signalStatLines[iLine].split()
            for ix, x in enumerate(lineEntries):
                if x.startswith('signal_stat_Bin'):
                    binName = x.replace('signal_stat_', '')
                if x.isdigit():
                    gmN_number = int(x)
                if '.' in x:
                    stat_idx = ix
            if stat_idx < 0:
                printLock.acquire()
                print( 'WARNING: cannot find signal stat error in file ' + outputCardFile + ', line = ' + signalStatLines[iLine])
                printLock.release()
                continue
            lineEntries[stat_idx] = str(scaledYields[binName] / gmN_number)
            signalStatLines[iLine] = ' '.join(lineEntries)
            subprocess.call('sed -i "s/^signal_stat_' + binName + '.*/' + signalStatLines[iLine] + '/" ' + outputCardFile, shell = True)

    semaphore.release ()

#######################################################################

semaphore = Semaphore (cpu_count () + 1)
printLock = Lock ()
nCards = len(allMasses) * len(allLifetimes)
progressTitle = 'Combining ' + str(nCards) + ' datacards into "{0}"'
progress = ProgressIndicator("")

for combinedCard in datacardCombinations:
    progress = ProgressIndicator(progressTitle.format(combinedCard))
    progress.printProgress(False)

    threads = []
    i = 0
    for mass in allMasses:
        for lifetime in allLifetimes:
            i += 1
            threads.append(Thread(target = makeCombinedCard, args = (i, nCards, combinedCard, mass, lifetime, arguments.ignoreSignalScaleFactor)))
            threads[-1].start()

    for thread in threads:
        thread.join()

    progress.setPercentDone(100.0)
    progress.printProgress(True)

print('All done!')
