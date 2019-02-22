#!/usr/bin/env python

# Script to combine run periods into single cards for running limits.

import os, sys, glob, re, subprocess
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-d', '--date', dest='inputDate',
                  help='Input date. Will expect cards in limits/limits_2015_date/ etc')

(arguments, args) = parser.parse_args()

if arguments.inputDate:
    if not os.path.exists('limits/limits_all_' + arguments.inputDate):
        os.mkdir('limits/limits_all_' + arguments.inputDate)
else:
    print 'No input date suffix given. Quitting.'
    sys.exit(1)

if not os.path.exists('limits/limits_2015_2016_save'):
    print 'Expected 2015-6 cards in limits/limits_2015_2016_save. Quitting.'
    sys.exit(1)

if not os.path.exists('limits/limits_2017_NLayers4_' + arguments.inputDate) or not os.path.exists('limits/limits_2017_NLayers5_' + arguments.inputDate) or not os.path.exists('limits/limits_2017_NLayers6plus_' + arguments.inputDate):
    print 'Expected 2017 cards in limits/limits_2017_<nLayersWord>_' + arguments.inputDate + ' for nLayersWords NLayers4, NLayers5, and NLayers6plus. Quitting.'
    sys.exit(1)

files20156 = glob.glob('limits/limits_2015_2016_save/datacard_AMSB_*.txt')
nFiles = str(len(files20156))

print '================================================================================'
print 'Will combine ' + nFiles + ' datacards.'
print '--------------------------------------------------------------------------------'

i = 0
for card in files20156:
    i += 1
    card20156 = card

    card2017NLayers4     = card.replace('limits_2015_2016_save', 'limits_2017_NLayers4_'     + arguments.inputDate)
    card2017NLayers5     = card.replace('limits_2015_2016_save', 'limits_2017_NLayers5_'     + arguments.inputDate)
    card2017NLayers6plus = card.replace('limits_2015_2016_save', 'limits_2017_NLayers6plus_' + arguments.inputDate)
    
    cardAll = card.replace('limits_2015_2016_save', 'limits_all_' + arguments.inputDate)

    print '[' + str(i) + '/' + nFiles + '] combining ' + re.sub(r'.*\/([^/]*)$', r'\1', cardAll) + '...'
    
    subprocess.call('combineCards.py Legacy=' + card20156 + ' Run2017NLayers4=' + card2017NLayers4 + ' Run2017NLayers5=' + card2017NLayers5 + ' Run2017NLayers6plus=' + card2017NLayers6plus + ' > ' + cardAll, shell = True)

    try:
        fin20156            = open(card20156.replace('datacard', 'signalSF'))
        fin2017NLayers4     = open(card2017NLayers4.replace('datacard', 'signalSF'))
        fin2017NLayers5     = open(card2017NLayers5.replace('datacard', 'signalSF'))
        fin2017NLayers6plus = open(card2017NLayers6plus.replace('datacard', 'signalSF'))
        
        sf20156        = fin20156.readline().rstrip ('\n')
        sf2017NLayers4 = fin2017NLayers4.readline().rstrip ('\n')
        sf2017NLayers5 = fin2017NLayers5.readline().rstrip ('\n')
        sf2017NLayers6plus = fin2017NLayers6plus.readline().rstrip ('\n')

        fin20156.close()
        fin2017NLayers4.close()
        fin2017NLayers5.close()
        fin2017NLayers6plus.close()

        if sf20156 != sf2017NLayers4 or sf20156 != sf2017NLayers5 or sf20156 != sf2017NLayers6plus:
            print 'Inconsistent signal scale factors. Quitting.'
            sys.exit(1)

        fout = open (cardAll.replace('datacard', 'signalSF'), 'w')
        fout.write(sf20156 + '\n')
        fout.close ()
    except IOError:
        pass

print 'Done.'
print '================================================================================'
