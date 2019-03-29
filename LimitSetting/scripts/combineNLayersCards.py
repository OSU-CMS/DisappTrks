#!/usr/bin/env python

# Script to combine run periods into single cards for running limits.

import os, sys, glob, re, subprocess
from optparse import OptionParser
from threading import Thread, Semaphore, Lock
from multiprocessing import cpu_count

parser = OptionParser()
parser.add_option("-d", "--date", dest="inputDate",
                  help="Input date. Will expect cards in limits/limits_2015_date/ etc")

(arguments, args) = parser.parse_args()

if arguments.inputDate:
    if not os.path.exists("limits/limits_2017_all_" + arguments.inputDate):
        os.mkdir("limits/limits_2017_all_" + arguments.inputDate)
else:
    print "No input date suffix given. Quitting."
    sys.exit(1)

if not os.path.exists("limits/limits_2017_NLayers4_" + arguments.inputDate) or not os.path.exists("limits/limits_2017_NLayers5_" + arguments.inputDate) or not os.path.exists("limits/limits_2017_NLayers6plus_" + arguments.inputDate):
    print "Expected cards to exist in limits/limits_2017_NLayers<X>" + arguments.inputDate + " for X = 4, 5, and 6plus. Quitting."
    sys.exit(1)

def combineCards (i, N, card4, card5, card6, cardAll):
    global semaphore
    global printLock

    semaphore.acquire ()

    printLock.acquire ()
    print "[" + str (i) + "/" + str (N) + "] combining " + re.sub (r".*\/([^/]*)$", r"\1", cardAll) + "..."
    printLock.release ()
    subprocess.call("combineCards.py Bin2017NLayers4=" + card4 + " Bin2017NLayers5=" + card5 + " Bin2017NLayers6plus=" + card6 + " > " + cardAll, shell = True)

    try:
        fin4 = open (card4.replace("datacard", "signalSF"))
        fin5 = open (card5.replace("datacard", "signalSF"))
        fin6 = open (card6.replace("datacard", "signalSF"))
        sf4 = fin4.readline ().rstrip ("\n")
        sf5 = fin5.readline ().rstrip ("\n")
        sf6 = fin6.readline ().rstrip ("\n")
        fin4.close ()
        fin5.close ()
        fin6.close ()
        if sf4 != sf5 or sf4 != sf6 or sf5 != sf6:
            print "Inconsistent signal scale factors. Quitting."
            sys.exit (1)
        fout = open (cardAll.replace("datacard", "signalSF"), "w")
        fout.write (sf4 + "\n")
        fout.close ()
    except IOError:
        pass

    semaphore.release ()


filesNLayers4 = glob.glob('limits/limits_2017_NLayers4_' + arguments.inputDate + '/datacard_AMSB_*.txt')
print "================================================================================"
print "Will combine " + str (len (filesNLayers4)) + " datacards."
print "--------------------------------------------------------------------------------"
semaphore = Semaphore (cpu_count () + 1)
printLock = Lock ()
threads = []
i = 0
for card in filesNLayers4:
    i += 1
    card4 = card
    card5 = card.replace("NLayers4", "NLayers5")
    card6 = card.replace("NLayers4", "NLayers6plus")
    cardAll = card.replace("NLayers4", "all")

    threads.append (Thread (target = combineCards, args = (i, len (filesNLayers4), card4, card5, card6, cardAll)))
    threads[-1].start ()

for thread in threads:
    thread.join ()

print "Done."
print "================================================================================"
