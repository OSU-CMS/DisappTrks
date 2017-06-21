#!/usr/bin/env python

# Script to combine run periods into single cards for running limits.

import os
import sys
import glob
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-d", "--date", dest="inputDate",
                  help="Input date. Will expect cards in limits/limits_2015_date/ etc")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                  help="verbose output")

(arguments, args) = parser.parse_args()

if arguments.inputDate:
    if not os.path.exists("limits/limits_all_" + arguments.inputDate):
        os.system("mkdir limits/limits_all_" + arguments.inputDate)
else:
    print "No input date suffix given. Quitting."
    sys.exit(0)

if not os.path.exists("limits/limits_2015_" + arguments.inputDate) or not os.path.exists("limits/limits_2016BC_" + arguments.inputDate) or not os.path.exists("limits/limits_2016DEFGH_" + arguments.inputDate):
    print "Expected cards to exist in limits/limits_<era>_" + arguments.inputDate + " for eras 2015, 2016BC, and 2016DEFGH. Quitting."
    sys.exit(0)

for card in glob.glob('limits/limits_2015_' + arguments.inputDate + "/datacard_AMSB_*.txt"):
    card2015 = card
    card2016BC = card.replace("2015", "2016BC")
    card2016DEFGH = card.replace("2015", "2016DEFGH")
    cardAll = card.replace("2015", "all")

    os.system("combineCards.py Run2015=" + card2015 + " Run2016BC=" + card2016BC + " Run2016DEFGH=" + card2016DEFGH + " > " + cardAll)

    if arguments.verbose:
        print "Created card:", cardAll
