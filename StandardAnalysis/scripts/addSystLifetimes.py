#!/usr/bin/env python3

# Add lifetime points to systematic files
# Usage:
# $ ../scripts/addSystLifetimes.py
# If mistake is made, revert the changes with, e.g.:
# $ git checkout HEAD data/systematic_values__pileup.txt


import sys
import math

masses = [100, 200, 300, 400, 500, 600]
#masses = [100]
lifetimes = [11, 12, 13, 14, 15, 16, 17, 18, 19]

systs = [
    'Isr',
    'JES',
    'JER',
    'PDFWt',
    'trigEff',
    'NMissOut',
    'pileup',
    ]

for syst in systs:
    infile = "../data/systematic_values__" + syst + ".txt"
    fin = open(infile, "r")
    contentOld = fin.read()
    words = contentOld.split()
    for mass in masses:
        largestErr = -1
        sample = "AMSB_chargino_" + str(mass) + "GeV_RewtCtau10cm"
        idx = words.index(sample)
#        print "idx of ", sample, " = ", idx
        errDn = float(words[idx+1])
        errUp = float(words[idx+2])
        if math.fabs(1.0 - errDn) > largestErr:
            largestErr = math.fabs(1.0 - errDn)
#        print "1largestErr = ", largestErr
        if math.fabs(1.0 - errUp) > largestErr:
            largestErr = math.fabs(1.0 - errUp)
#        print "2largestErr = ", largestErr
        sample = "AMSB_chargino_" + str(mass) + "GeV_RewtCtau20cm"
        idx = words.index(sample)
        errDn2 = float(words[idx+1])
        errUp2 = float(words[idx+2])
        if math.fabs(1.0 - errDn2) > largestErr or math.fabs(1.0 - errUp2) > largestErr:  # if the error is larger from the second, use it
            errDn = errDn2
            errUp = errUp2
#        print "idx of ", sample, " = ", idx
#        print "largestErr = ", largestErr
        contentNew = ""
        for lifetime in lifetimes:
            sample = "AMSB_chargino_" + str(mass) + "GeV_RewtCtau" + str(lifetime) + "cm"
            line = '{0: <40}'.format(str(sample)) + " " + '{0: <8}'.format(errDn) + " " + '{0: <8}'.format(errUp) + "\n"
            contentNew += line
        sample = "AMSB_chargino_" + str(mass) + "GeV_RewtCtau20cm"
        contentOld = contentOld.replace(sample, contentNew + sample)

##     for word in words:
##         if "10cm" in word:
##             sys.exit(0)
##         print word

#    outputFile = infile.replace(".txt", "_add.txt")
    outputFile = infile
    fout = open (outputFile, "w")
    fout.write(contentOld)
    fout.close()
#    os.system("cat " + outputFile)
    print "Finished writing " + outputFile + " using as input: " + infile + "\n\n\n"










