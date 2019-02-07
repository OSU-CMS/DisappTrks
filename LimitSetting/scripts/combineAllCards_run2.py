#!/usr/bin/env python

# Script to combine run periods into single cards for running limits.

import os, sys, glob, re, subprocess
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--date", dest="inputDate",
                  help="Input date. Will expect cards in limits/limits_2015_date/ etc")

(arguments, args) = parser.parse_args()

if arguments.inputDate:
    if not os.path.exists("limits/limits_all_run2_" + arguments.inputDate):
        os.mkdir("limits/limits_all_run2_" + arguments.inputDate)
else:
    print "No input date suffix given. Quitting."
    sys.exit(1)

if not os.path.exists("limits/limits_2015_" + arguments.inputDate) or not os.path.exists("limits/limits_2016BC_" + arguments.inputDate) or not os.path.exists("limits/limits_2016DEFGH_" + arguments.inputDate) or not os.path.exists("limits/limits_2017_NLayers4_" + arguments.inputDate) or not os.path.exists("limits/limits_2017_NLayers5_" + arguments.inputDate) or not os.path.exists("limits/limits_2017_NLayers6plus_" + arguments.inputDate):
    print "Expected cards to exist in limits/limits_<era>_" + arguments.inputDate + " for eras 2015, 2016BC, 2016DEFGH, 2017_NLayers4, 2017_NLayers5, 2017_NLayers6plus . Quitting."
    sys.exit(1)

files2015 = glob.glob('limits/limits_2015_' + arguments.inputDate + "/datacard_AMSB_*.txt")
print "================================================================================"
print "Will combine " + str (len (files2015)) + " datacards."
print "--------------------------------------------------------------------------------"
i = 0
for card in files2015:
    i += 1
    card2015 = card
    card2016BC = card.replace("2015", "2016BC")
    card2016DEFGH = card.replace("2015", "2016DEFGH")
    card2017NLayers4 = card.replace("2015", "2017_NLayers4")
    card2017NLayers5 = card.replace("2015", "2017_NLayers5")
    card2017NLayers6plus = card.replace("2015", "2017_NLayers6plus")
    cardAll = card.replace("2015", "all_run2")

    print "[" + str (i) + "/" + str (len (files2015)) + "] combining " + re.sub (r".*\/([^/]*)$", r"\1", cardAll) + "..."
    subprocess.call("combineCards.py Run2015=" + card2015 + " Run2016BC=" + card2016BC + " Run2016DEFGH=" + card2016DEFGH + " Run2017NLayers4=" + card2017NLayers4 + " Run2017NLayers5=" + card2017NLayers5 + " Run2017NLayers6plus=" + card2017NLayers6plus + " > " + cardAll, shell = True)

    try:
        fin2015 = open (card2015.replace("datacard", "signalSF"))
        fin2016BC = open (card2016BC.replace("datacard", "signalSF"))
        fin2016DEFGH = open (card2016DEFGH.replace("datacard", "signalSF"))
        fin2017NLayers4 = open (card2017NLayers4.replace("datacard", "signalSF"))
        fin2017NLayers5 = open (card2017NLayers5.replace("datacard", "signalSF"))
        fin2017NLayers6plus = open (card2017NLayers6plus.replace("datacard", "signalSF"))
        fout = open (cardAll.replace("datacard", "signalSF"), "w")
        sf2015 = fin2015.readline ().rstrip ("\n")
        sf2016BC = fin2016BC.readline ().rstrip ("\n")
        sf2016DEFGH = fin2016DEFGH.readline ().rstrip ("\n")
        sf2017NLayers4 = fin2017NLayers4.readline ().rstrip ("\n")
        sf2017NLayers5 = fin2017NLayers5.readline ().rstrip ("\n")
        sf2017NLayers6plus = fin2017NLayers6plus.readline ().rstrip ("\n")
        fin2015.close ()
        fin2016BC.close ()
        fin2016DEFGH.close ()
        fin2017NLayers4.close ()
        fin2017NLayers5.close ()
        fin2017NLayers6plus.close ()
        if sf2015 != sf2016BC or sf2015 != sf2016DEFGH or sf2016BC != sf2016DEFGH or sf2015 != sf2017NLayers4 or sf2015 != sf2017NLayers5 or sf2015 != sf2017NLayers6plus:
            print "Inconsistent signal scale factors. Quitting."
            sys.exit (1)
        fout.write (sf2015 + "\n")
        fout.close ()
    except IOError:
        pass

print "Done."
print "================================================================================"
