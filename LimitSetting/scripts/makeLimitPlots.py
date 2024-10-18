#!/usr/bin/env python3

# Fixme:  Merge this script with makeLimitPlots.py

import time
import os
import sys
import math
import copy
import re
import subprocess
import glob
from array import *
from decimal import *
from fractions import *
from operator import itemgetter
from ctypes import c_double as Double

from DisappTrks.LimitSetting.limitOptions import *

if not arguments.era in validEras:
  print( "Invalid or empty data-taking era specific (-e). Allowed eras:")
  print( str(validEras))
  sys.exit(0)

if arguments.limitType not in validLimitTypes:
    print( "Invalid or empty limit type to plot (-l). Allowed types:")
    print( str(validLimitTypes))
    sys.exit(0)

if arguments.limitType == "wino":
    from DisappTrks.LimitSetting.winoElectroweakLimits import *
    from DisappTrks.LimitSetting.winoElectroweakPlots import *
elif arguments.limitType == "higgsino":
    from DisappTrks.LimitSetting.higgsinoElectroweakLimits import *
    from DisappTrks.LimitSetting.higgsinoElectroweakPlots import *

if arguments.outputDir:
    if not os.path.exists("limits/" + arguments.outputDir):
        os.system("mkdir limits/" + arguments.outputDir)
else:
    print( "No output directory specified, shame on you")
    sys.exit(0)

from DisappTrks.StandardAnalysis.tdrstyle import *
from ROOT import TF1, TFile, TH2F, TGraph, TGraphAsymmErrors, gROOT, gStyle, TStyle, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TPaveLabel, TH2D, TPave, TMath

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetOptTitle(0)
gStyle.SetCanvasDefH(600)
gStyle.SetCanvasDefW(600)
setTDRStyle()
gROOT.ForceStyle()

colorSchemes = {
    'brazilian' : {
        'obs' : 1,
        'exp' : 1,

        'oneSigma' : 417 if arguments.paperMode else 78,
        'twoSigma' : 800 if arguments.paperMode else 88,
    },

    'theory' : {
        'obs' : 1,
        'exp' : 2,
        'oneSigma' : 921,
        'twoSigma' : 920,
    },
    'red' : {
        'obs' : 633,
        'exp' : 633,
        'oneSigma' : 625,
        'twoSigma' : 623,
    },
    'blue' : {
        'obs' : 601,
        'exp' : 601,
        'oneSigma' : 594,
        'twoSigma' : 591,
    },
    'green' : {
        'obs' : 418,
        'exp' : 418,
        'oneSigma' : 410,
        'twoSigma' : 407,
    },
    'purple' : {
        'obs' : 882,
        'exp' : 882,
        'oneSigma' : 872,
        'twoSigma' : 871,
    },
    'yellow' : {
        'obs' : 402,
        'exp' : 402,
        'oneSigma' : 397,
        'twoSigma' : 393,
    },
}

#set the text for the luminosity label
if(intLumi < 1000.):
    LumiText = str.format('{0:.1f}', intLumi) + " pb^{-1}"
else:
    LumiText = str.format('{0:.1f}', intLumi/1000.) + " fb^{-1}"
    if roundLumiText:
        LumiText = str.format('{0:.0f}', intLumi/1000.) + " fb^{-1}"

# set the text for the fancy heading
HeaderText = LumiText + " (13 TeV)"

def makeSignalName(mass,lifetime):
    lifetime = str(lifetime).replace(".0", "")
    lifetime = str(lifetime).replace("0.", "0p")
    return ("AMSB_mChi" if arguments.limitType == "wino" else "Higgsino_mChi") + str(mass) + "_" + str(lifetime) + "cm"

def makeSignalRootFileName(mass, lifetime, directory, limit_type):
    signal_name = makeSignalName(mass, lifetime)
    if glob.glob("limits/" + directory + "/" + signal_name + "_" + limit_type + "/higgsCombine" + signal_name + ".*.root"):
        os.system ("mv -f limits/" + directory + "/" + signal_name + "_" + limit_type + "/higgsCombine" + signal_name + ".*.root limits/" + directory + "/" + signal_name + "_" + limit_type + "/limits_" + signal_name + ".root")
    return "limits/" + directory + "/" + signal_name + "_" + limit_type + "/limits_" + signal_name + ".root"

def makeSignalSFFileName(mass,lifetime,directory):
    signal_name = makeSignalName(mass,lifetime)
    return "limits/"+directory+"/signalSF_"+signal_name+".txt"

def makeSignalLogFileName(mass,lifetime,directory,limit_type):
    signal_name = makeSignalName(mass,lifetime)
    if glob.glob("limits/"+directory+"/"+signal_name+"_"+limit_type+"/condor_0*.out"):
        os.system ("mv -f limits/"+directory+"/"+signal_name+"_"+limit_type+"/condor_0.out limits/"+directory+"/"+signal_name+"_"+limit_type+"/combine_log_"+signal_name+".txt")
    return "limits/"+directory+"/"+signal_name+"_"+limit_type+"/combine_log_"+signal_name+".txt"

def getTheoryGraph():
    x = [ ]
    y = [ ]
    for mass in masses:
        xSection = float(signal_cross_sections[str(mass)]['value'])
        x.append(float(mass))
        y.append(float(xSection))
    graph = TGraph(len(x), array('d', x), array('d', y))
    graph.SetLineWidth(5)
    graph.SetLineStyle(2)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes['theory']['exp'])
    graph.SetMarkerStyle(21)
    graph.SetMarkerSize(1)
    #graph.SetMarkerColor(1)
    #graph.SetMarkerColor(2)
    graph.SetMarkerColor(colorSchemes['theory']['exp'])
    return graph

def getTheoryOneSigmaGraph():
    x = [ ]
    y = [ ]
    up = [ ]
    down = [ ]
    for mass in masses:
        xSection = float(signal_cross_sections[str(mass)]['value'])
        xSectionError = float(signal_cross_sections[str(mass)]['error'])
        x.append(float(mass))
        y.append(float(xSection))
        up.append(float((xSectionError - 1.0) * xSection))
        down.append(float((xSectionError - 1.0) * xSection))
    graph = TGraphAsymmErrors(
        len(x),
        array('d', x),
        array('d', y),
        array('d', [0 for i in range(0, len(x))]),
        array('d', [0 for i in range(0, len(x))]),
        array('d', down),
        array('d', up)
    )
    graph.SetFillColor(colorSchemes['theory']['oneSigma'])
    graph.SetFillStyle(0)
    graph.SetLineColor(colorSchemes['theory']['oneSigma'])
    graph.SetMarkerColor(colorSchemes['theory']['oneSigma'])

    return graph

def getGraph(limits, x_key, y_key):
    x = [ ]
    y = [ ]
    for limit in limits:
        if x_key not in limit.keys() or y_key not in limit.keys():
            continue
        x.append(float(limit[x_key]))
        y.append(float(limit[y_key]))
    graph = TGraph(len(x), array('d', x), array('d', y))
    return graph

def convertFromCmToMassSplitting_v3(mass, lifetimeInCm):
    # Choose starting value
    speedLightCmPerNs = 29.979  # speed of light in cm / ns
    lifetimeInSec = float(lifetimeInCm) / speedLightCmPerNs * 1.0E-9
    deltaM = 0.160
    prevDeltaMGuess = 0
    (deltaM, prevDeltaMGuess) = calcMassSplitting(mass, lifetimeInSec, deltaM, prevDeltaMGuess)
    #    print "Debug:  found values of: mass=", mass, ", lifetime=", lifetimeInSec, ", deltaM=", deltaM, ", prevDeltaMGuess=", prevDeltaMGuess
    deltaM *= 1000 # convert from GeV to MeV
    return deltaM

def calcMassSplitting(mass, lifetimeInSec, deltaM, prevDeltaMGuess):
    #    print "Debug:  running calcMassSplitting with mass=", mass, ", lifetimeInSec=", lifetimeInSec, ", deltaM=", deltaM, ", prevDeltaMGuess=", prevDeltaMGuess
    if mass < 1:  # protect against 0
        return (0, 0)
    fPi = float(0.093)
    gF = 1.166379E-5   # units if GeV^-2
    mPi = 0.13957018  # units of GeV, from PDG
    hBarinGeVs = 6.582119E-25
    neuMass = float(mass) - float(deltaM)
    # First calculate what the lifetime is, for the assumption of deltaM
    a = math.pow(float(fPi),2) * math.pow(float(gF),2) / (4 * math.pi * math.pow(float(mass),2))
    numBTerm1 = float(math.pow(float(mass),2) + math.pow(float(neuMass),2) - math.pow(float(mPi),2))
    numBTerm1Squared = float(math.pow(float(numBTerm1),2))
    numBTerm2 = float(4) * float(math.pow(float(mass),2)) * float(math.pow(float(neuMass),2))
    #    b = float(math.sqrt(float(math.fabs(numBTerm1Squared - numBTerm2))))/(2*float(mass))  #old, mostly works
    b = (math.sqrt((math.fabs(math.pow((math.pow((mass),2) + math.pow((neuMass),2) - math.pow((mPi),2)), 2) - (4) * (math.pow((mass),2)) * (math.pow((neuMass),2)) ))))/(2*(mass))  #old, mostly works
    ##     if float(numBTerm1Squared) - numBTerm2 > 0:
    ##         b = math.sqrt(numBTerm1Squared - numBTerm2)/(2*float(mass))
    ##     else:
    ##         print "Error:  trying to take sqrt of negative number:  numBTerm1Squared=", numBTerm1Squared, ", numBTerm2=", numBTerm2
    ##         b  = 0
    #    c = float(math.pow(float(mass) + float(neuMass),2))  #old, wrong
    c = math.pow(math.pow(mass, 2) - math.pow(neuMass, 2),2)
    d = float(math.pow(float(mPi),2))
    if (a == 0) or (b == 0):
        print( "Debug found bad values for a or b:  a=", a, ", b=", b, ", c=", c, ", d=", d, ", mass = ", mass, "neumass = ", neuMass, ", sqrt(c)=", math.pow(mass,2) - math.pow(neuMass,2))
        print( "Debug: lifetimeInSec=", lifetimeInSec, ", deltaM=", deltaM, ", prevDeltaMGuess=", prevDeltaMGuess)
        #        print "Debug:  lifetimeGuess = ", lifetimeGuess, ", lifetimeInSec=", lifetimeInSec, ", deltaM=", deltaM, ", prevDeltaMGuess=", prevDeltaMGuess, "(lifetimeInSec - lifetimeGuess) / lifetimeInSec = ", (lifetimeInSec - lifetimeGuess) / lifetimeInSec
        return (0, 0)

    lifetimeGuess = hBarinGeVs / (4.0 * a * b * (c - d * deltaM))
    precision = 0.0001  # precision of desired result
    lowerlimit = mPi  # value below which deltaM is undefined
    if math.fabs((lifetimeInSec - lifetimeGuess) / lifetimeInSec) < precision:
        return (deltaM, prevDeltaMGuess)
    elif math.fabs((deltaM - prevDeltaMGuess) / deltaM) < precision / 10:
        #        print "Difference between deltaM=", deltaM, " and prevDeltaMGuess=", prevDeltaMGuess, " is less than precision = ', precision
        return (deltaM, prevDeltaMGuess)
    else:
        if (lifetimeInSec - lifetimeGuess) > 0:
            tmp = deltaM
            deltaM -= 0.5 * math.fabs(deltaM - prevDeltaMGuess)
            if deltaM < lowerlimit:
                deltaM = lowerlimit * (1.0 + precision)
            prevDeltaMGuess = tmp
            return calcMassSplitting(mass, lifetimeInSec, deltaM, prevDeltaMGuess)
        else:
            tmp = deltaM
            deltaM += 0.5 * math.fabs(deltaM - prevDeltaMGuess)
            if deltaM < lowerlimit:
                deltaM = lowerlimit * (1.0 + precision)
            prevDeltaMGuess = tmp
            return calcMassSplitting(mass, lifetimeInSec, deltaM, prevDeltaMGuess)

def getGraph2D(limits, x_key, y_key, experiment_key, theory_key):
    x = array ('d')
    y = array ('d')
    limit_dict = {}
    for limit in limits:
        mass = float (limit['mass'])
        lifetime = float (limit['lifetime'])
        if lifetime not in limit_dict:
            limit_dict[lifetime] = {}
        if mass not in limit_dict[lifetime]:
            limit_dict[lifetime][mass] = {}
        limit_dict[lifetime][mass]['experiment'] = limit[experiment_key]
        if experiment_key == 'up1' or experiment_key == 'up2':
            limit_dict[lifetime][mass]['experiment'] += limit['expected']
        if experiment_key == 'down1' or experiment_key == 'down2':
            limit_dict[lifetime][mass]['experiment'] = limit['expected'] - limit_dict[lifetime][mass]['experiment']
        for theory_mass in signal_cross_sections:
            if abs (float (theory_mass) - mass) < 1.0e-3:
                limit_dict[lifetime][mass]['theory'] = float (signal_cross_sections[theory_mass]['value'])
                theory_error = float (signal_cross_sections[theory_mass]['error'])
                if theory_key =='up2' or theory_key == 'down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                if theory_key == 'up1' or theory_key == 'up2':
                    limit_dict[lifetime][mass]['theory'] *= theory_error
                if theory_key == 'down1' or theory_key == 'down2':
                    limit_dict[lifetime][mass]['theory'] *= (2.0 - theory_error)
    if arguments.verbose:
        print( "Debug:  limit_dict.keys() = ")
        print( limit_dict.keys())
    for lifetime in sorted (limit_dict.keys ()):
        ordered_masses = sorted (limit_dict[lifetime].keys (), reverse=True)
        first_allowed_mass = ordered_masses[0]
        previous_mass = ordered_masses[0]
        for mass in ordered_masses:
            if limit_dict[lifetime][mass]['theory'] > limit_dict[lifetime][mass]['experiment']:
                previous_mass = mass
                break
            first_allowed_mass = mass
        mass_limit = 0.0
        if previous_mass == first_allowed_mass and len(ordered_masses) > 1:
            first_allowed_mass = ordered_masses[1]
        if previous_mass != first_allowed_mass:
            # find intersection using http://en.wikipedia.org/wiki/Line-line_intersection
            x1 = previous_mass  # lower mass value
            x3 = previous_mass
            x2 = first_allowed_mass  # higher mass value
            x4 = first_allowed_mass
            # Use log10 because the theory cross section is roughly linear
            # on a log scale, not on a linear scale.
            y1 = math.log10(limit_dict[lifetime][previous_mass]['theory'])
            y3 = math.log10(limit_dict[lifetime][previous_mass]['experiment'])
            y2 = math.log10(limit_dict[lifetime][first_allowed_mass]['theory'])
            y4 = math.log10(limit_dict[lifetime][first_allowed_mass]['experiment'])
            mass_limit = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
            mass_limit /= (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if math.isnan (mass_limit):
                mass_limit = 0.0
        if mass_limit > first_allowed_mass:
            print( "ERROR:  Something went wrong with lifetime", lifetime, ": first_allowed_mass = ", first_allowed_mass, " is less than the calculated mass limit, ", mass_limit, ".  Please investigate.")
            mass_limit = previous_mass
        x.append (mass_limit)
        y.append (lifetime)
        if arguments.verbose:
            print( "Debug getGraph2D:  adding point: " + str(mass_limit) + ", " + str(lifetime))
            print( "  Debug:  previous_mass=" + str(previous_mass) + ", first_allowed_mass=" + str(first_allowed_mass))
            print( "  Debug:  limit_dict[lifetime][first_allowed_mass]['experiment'] = " + str(limit_dict[lifetime][first_allowed_mass]['experiment']) + ", experiment_key = " + experiment_key)
            if previous_mass != first_allowed_mass:
                print( "  Debug x1,x2,x3,x4=" + str(x1) + ","+ str(x2) + "," + str(x3) + "," + str(x4) + ","  + ", y1,y2,y3,y4=" + str(y1) + ","+ str(y2) + "," + str(y3) + "," + str(y4) + ",")
        if x_key == 'lifetime' and y_key == 'mass':
            x[-1], y[-1] = y[-1], x[-1]
    if plot['convertToMassSplitting']:
        if "observed" == experiment_key:
            print( "Debug:  about to print all the values that go into TGraph for experiment_key = ", experiment_key, ":")
            for i in range(len(x)):
                print( i, ": ", x[i], ", ", y[i])

        lifetimeInCm = copy.deepcopy(y)

        if "observed" == experiment_key:
            print( "Debug:  about to print all the values that go into TGraph, after converting to massSplitting, for experiment_key = ", experiment_key, ":")
        for i in range(len(y)):
            y[i] = convertFromCmToMassSplitting_v3(x[i], y[i])
            if "observed" == experiment_key:
                print( i, ": ", x[i], ", ", y[i])
##         graphTest = TGraph(len(y), lifetimeInCm, y)
##         graphTest.Write()

    graph = TGraph (len(x), x, y)
    return graph

# function to fill 'potholes' in th2f's
# for empty bins, this sets the bin content to the average of
# all non-empty adjacenet bins
def fillPotHolesTH2F(histogram):
    nBinsX = histogram.GetXaxis().GetNbins()
    nBinsY = histogram.GetYaxis().GetNbins()

    for ix in range(1, nBinsX+1):
        for iy in range(1, nBinsY+1):
            if histogram.GetBinContent(ix, iy) > 0:
                continue

            n = sum = sumErr = 0
            nUp = histogram.GetBinContent(ix, iy+1)
            nDown = histogram.GetBinContent(ix, iy-1)
            nLeft = histogram.GetBinContent(ix-1, iy)
            nRight = histogram.GetBinContent(ix+1, iy)

            if nUp > 0 and iy < nBinsY:
                sum += nUp
                sumErr = math.hypot(sumErr, histogram.GetBinError(ix, iy+1))
                n += 1
            if nDown > 0 and iy > 1:
                sum += nDown
                sumErr = math.hypot(sumErr, histogram.GetBinError(ix, iy-1))
                n += 1
            if nLeft > 0 and ix > 1:
                sum += nLeft
                sumErr = math.hypot(sumErr, histogram.GetBinError(ix-1, iy))
                n += 1
            if nRight > 0 and ix < nBinsX:
                sum += nRight
                sumErr = math.hypot(sumErr, histogram.GetBinError(ix+1, iy))
                n += 1

            if n > 0:
                print( "Filling pothole in histogram", histogram.GetName(), "-- bin (", ix, ", ", iy, ")")
                histogram.SetBinContent(ix, iy, sum / n)
                histogram.SetBinError(ix, iy, sumErr / n)

def getTH2F(limits,x_key,y_key,experiment_key,theory_key):
    xBin_tmp = []
    yBin_tmp = []
    limit_dict = {}
    for limit in limits:
        xBin_tmp.append(float(limit['mass']))
        yBin_tmp.append(float(limit['lifetime']))
    xBin = list(set(xBin_tmp))
    yBin = list(set(yBin_tmp))
    xBin.sort()
    yBin.sort()
    xBin.append(xBin[-1] + (xBin[-1] - xBin[-2]))  # Add an additional bin boundary, so that the last bin has equal witdth to the second to last bin
    yBin.append(yBin[-1] + (yBin[-1] - yBin[-2]))  # Add an additional bin boundary, so that the last bin has equal witdth to the second to last bin
    # Offset the xaxis bins so that mass values are in center of each bin
    xBinHalfWidth = (xBin[1] - xBin[0]) / 2
    for i in range(0,len(xBin)):
        xBin[i] -= xBinHalfWidth
    yBinArray = array("d", yBin)
    xBinArray = array("d", xBin)
    if arguments.verbose:
        print( "Printing xBin:")
        print( xBin)
        print( "Printing yBin:")
        print( yBin)
    plot2D = TH2F("","",len(xBin)-1,xBinArray,len(yBin)-1,yBinArray)
    for limit in limits:
        mass = float (limit['mass'])
        lifetime = float (limit['lifetime'])
        if lifetime not in limit_dict:
            limit_dict[lifetime] = {}
        if mass not in limit_dict[lifetime]:
            limit_dict[lifetime][mass] = {}
        limit_dict[lifetime][mass]['experiment'] = limit[experiment_key]
        if experiment_key =='up1' or experiment_key =='up2':
            limit_dict[lifetime][mass]['experiment'] += limit['expected']
        if experiment_key =='down1' or experiment_key =='down2':
            limit_dict[lifetime][mass]['experiment'] = limit['expected'] - limit_dict[lifetime][mass]['experiment']
        for theory_mass in signal_cross_sections:
            if abs (float (theory_mass) - mass) < 1.0e-3:
                limit_dict[lifetime][mass]['theory'] = float (signal_cross_sections[theory_mass]['value'])
                theory_error = float (signal_cross_sections[theory_mass]['error'])
                if theory_key =='up2' or theory_key =='down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                if theory_key =='up1' or theory_key =='up2':
                    limit_dict[lifetime][mass]['theory'] *= theory_error
                if theory_key =='down1' or theory_key =='down2':
                    limit_dict[lifetime][mass]['theory'] *= (2.0 - theory_error)
    for lifetime in sorted (limit_dict.keys ()):
        ordered_masses = sorted (limit_dict[lifetime].keys ())
        first_allowed_mass = ordered_masses[0]
        previous_mass = ordered_masses[0]
        for mass in ordered_masses:
#            plot2D.Fill(mass,lifetime, limit_dict[lifetime][mass]['experiment']/limit_dict[lifetime][mass]['theory'])
            plot2D.Fill(mass,lifetime, limit_dict[lifetime][mass]['experiment'])
    th2f = plot2D
    th2f.SetDirectory(0)

    return th2f


def makeExpLimitsTable(limits, x_key, y_key, experiment_key, theory_key):
    x = array ('d')
    y = array ('d')
    limit_dict = {}
    expTable = open("limits/" + arguments.outputDir + "/" + "expTable.tex", "w")
    expTable.write('\\begin{center} \\begin{tabular}{cc}')
    expTable.write('\n')
    expTable.write('\hline \hline')
    expTable.write('\n')
    expTable.write('$\\tau$ (ns) & Exp. Excluded Mass (\gev) \\\\')
    expTable.write('\hline')
    expTable.write('\n')
    expTable.close()

    for limit in limits:
        mass = float (limit['mass'])
        lifetime = float (limit['lifetime'])
        if lifetime not in limit_dict:
            limit_dict[lifetime] = {}
        if mass not in limit_dict[lifetime]:
            limit_dict[lifetime][mass] = {}
        limit_dict[lifetime][mass]['experiment'] = limit[experiment_key]
        if experiment_key =='up1' or experiment_key =='up2':
            limit_dict[lifetime][mass]['experiment'] += limit['expected']
        if experiment_key =='down1' or experiment_key =='down2':
            limit_dict[lifetime][mass]['experiment'] = limit['expected'] - limit_dict[lifetime][mass]['experiment']
        for theory_mass in signal_cross_sections:
            if abs (float (theory_mass) - mass) < 1.0e-3:
                limit_dict[lifetime][mass]['theory'] = float (signal_cross_sections[theory_mass]['value'])
                theory_error = float (signal_cross_sections[theory_mass]['error'])
                if theory_key =='up2' or theory_key =='down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                if theory_key =='up1' or theory_key =='up2':
                    limit_dict[lifetime][mass]['theory'] *= theory_error
                if theory_key =='down1' or theory_key =='down2':
                    limit_dict[lifetime][mass]['theory'] *= (2.0 - theory_error)

    for lifetime in sorted (limit_dict.keys ()):
        ordered_masses = sorted (limit_dict[lifetime].keys (), reverse=True)
        first_allowed_mass = ordered_masses[0]
        previous_mass = ordered_masses[0]
        for mass in ordered_masses:
            if limit_dict[lifetime][mass]['theory'] > limit_dict[lifetime][mass]['experiment']:
                previous_mass = mass
                break
            first_allowed_mass = mass
        mass_limit = 0.0
        if previous_mass == first_allowed_mass and len(ordered_masses) > 1:
            first_allowed_mass = ordered_masses[1]
        if previous_mass != first_allowed_mass:
            # find intersection using http://en.wikipedia.org/wiki/Line-line_intersection
            x1 = previous_mass  # lower mass value
            x3 = previous_mass
            x2 = first_allowed_mass  # higher mass value
            x4 = first_allowed_mass
            # Use log10 because the theory cross section is roughly linear
            # on a log scale, not on a linear scale.
            y1 = math.log10(limit_dict[lifetime][previous_mass]['theory'])
            y3 = math.log10(limit_dict[lifetime][previous_mass]['experiment'])
            y2 = math.log10(limit_dict[lifetime][first_allowed_mass]['theory'])
            y4 = math.log10(limit_dict[lifetime][first_allowed_mass]['experiment'])
            mass_limit = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
            mass_limit /= (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if math.isnan (mass_limit):
                mass_limit = 0.0
        if mass_limit > first_allowed_mass:
            print( "ERROR:  Something went wrong with lifetime", lifetime, ": first_allowed_mass = ", first_allowed_mass, " is less than the calculated mass limit, ", mass_limit, ".  Please investigate.")
            mass_limit = previous_mass
        x.append (mass_limit)
        y.append (lifetime)

        with open ("limits/" + arguments.outputDir + "/" + "expTable.tex", 'a') as file:
            file.write(str(lifetime) + ' & ' + str(round(mass_limit,1)) + '\\\\')
            file.write('\n')
            expTable.close()

    if x_key =='lifetime' and y_key =='mass':
        x[-1], y[-1] = y[-1], x[-1]
    graph = TGraph (len (x), x, y)

    expTable = open("limits/" + arguments.outputDir + "/" + "expTable.tex", "a")
    expTable.write('\hline \hline')
    expTable.write('\n')
    expTable.write(' \end{tabular} \end{center}')
    expTable.close()
    print( "Table of expected limits for AN stored in: limits/" + arguments.outputDir)
    return 'Success'

def makeObsLimitsTable(limits, x_key, y_key, experiment_key, theory_key):
    x = array ('d')
    y = array ('d')
    limit_dict = {}
    obsTable = open("limits/" + arguments.outputDir + "/" + "obsTable.tex", "w")
    obsTable.write('\\begin{center} \\begin{tabular}{cc}')
    obsTable.write('\n')
    obsTable.write('\hline \hline')
    obsTable.write('\n')
    obsTable.write('$\\tau$ (ns) & Obs. Excluded Mass (\gev) \\\\')
    obsTable.write('\hline')
    obsTable.write('\n')
    obsTable.close()
    print( "Table of observed limits for AN stored in: limits/" + arguments.outputDir)
    for limit in limits:
        mass = float (limit['mass'])
        lifetime = float (limit['lifetime'])
        if lifetime not in limit_dict:
            limit_dict[lifetime] = {}
        if mass not in limit_dict[lifetime]:
            limit_dict[lifetime][mass] = {}
        limit_dict[lifetime][mass]['experiment'] = limit[experiment_key]
        if experiment_key =='up1' or experiment_key =='up2':
            limit_dict[lifetime][mass]['experiment'] += limit['expected']
        if experiment_key =='down1' or experiment_key =='down2':
            limit_dict[lifetime][mass]['experiment'] = limit['expected'] - limit_dict[lifetime][mass]['experiment']
        for theory_mass in signal_cross_sections:
            if abs (float (theory_mass) - mass) < 1.0e-3:
                limit_dict[lifetime][mass]['theory'] = float (signal_cross_sections[theory_mass]['value'])
                theory_error = float (signal_cross_sections[theory_mass]['error'])
                if theory_key =='up2' or theory_key =='down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                if theory_key =='up1' or theory_key =='up2':
                    limit_dict[lifetime][mass]['theory'] *= theory_error
                if theory_key =='down1' or theory_key =='down2':
                    limit_dict[lifetime][mass]['theory'] *= (2.0 - theory_error)

    for lifetime in sorted (limit_dict.keys ()):
        ordered_masses = sorted (limit_dict[lifetime].keys (), reverse=True)
        first_allowed_mass = ordered_masses[0]
        previous_mass = ordered_masses[0]
        for mass in ordered_masses:
            if limit_dict[lifetime][mass]['theory'] > limit_dict[lifetime][mass]['experiment']:
                previous_mass = mass
                break
            first_allowed_mass = mass
        mass_limit = 0.0
        if previous_mass == first_allowed_mass and len(ordered_masses) > 1:
            first_allowed_mass = ordered_masses[1]
        if previous_mass != first_allowed_mass:
            # find intersection using http://en.wikipedia.org/wiki/Line-line_intersection
            x1 = previous_mass  # lower mass value
            x3 = previous_mass
            x2 = first_allowed_mass  # higher mass value
            x4 = first_allowed_mass
            # Use log10 because the theory cross section is roughly linear
            # on a log scale, not on a linear scale.
            y1 = math.log10(limit_dict[lifetime][previous_mass]['theory'])
            y3 = math.log10(limit_dict[lifetime][previous_mass]['experiment'])
            y2 = math.log10(limit_dict[lifetime][first_allowed_mass]['theory'])
            y4 = math.log10(limit_dict[lifetime][first_allowed_mass]['experiment'])
            mass_limit = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
            mass_limit /= (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if math.isnan (mass_limit):
                mass_limit = 0.0
        if mass_limit > first_allowed_mass:
            print( "ERROR:  Something went wrong with lifetime", lifetime, ": first_allowed_mass = ", first_allowed_mass, " is less than the calculated mass limit, ", mass_limit, ".  Please investigate.")
            mass_limit = previous_mass
        x.append (mass_limit)
        y.append (lifetime)

        with open ("limits/" + arguments.outputDir + "/" + "obsTable.tex", 'a') as file:
            file.write(str(lifetime) + ' & ' + str(round(mass_limit,1)) + '\\\\')
            file.write('\n')
        obsTable.close()

    if x_key =='lifetime' and y_key =='mass':
        x[-1], y[-1] = y[-1], x[-1]
    graph = TGraph (len (x), x, y)

    obsTable = open("limits/" + arguments.outputDir + "/" + "obsTable.tex", "a")
    obsTable.write('\hline \hline')
    obsTable.write('\n')
    obsTable.write(' \end{tabular} \end{center}')
    obsTable.close()
    print ("Table of observed limits for AN stored in: limits/" + arguments.outputDir)
    return 'Success'



def getObservedGraph(limits,xAxisType,colorScheme):
    graph = getGraph(limits, xAxisType, 'observed')
    graph.SetLineWidth(5)
    graph.SetLineStyle(1)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['obs'])
    graph.SetMarkerStyle(21)
    graph.SetMarkerSize(1)
    graph.SetMarkerColor(colorSchemes[colorScheme]['obs'])
    return graph

def getObservedGraph2D(limits,xAxisType,yAxisType,experiment_key,theory_key,colorScheme):
    graph = getGraph2D(limits, xAxisType, yAxisType, experiment_key, theory_key)
    graph.SetLineWidth(5)
    graph.SetLineStyle(1)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['obs'])
    graph.SetMarkerStyle(21)
    graph.SetMarkerSize(1)
    graph.SetMarkerColor(colorSchemes[colorScheme]['obs'])
    return graph

def getExpectedGraph(limits,xAxisType,colorScheme):
    graph = getGraph(limits, xAxisType, 'expected')
    graph.SetLineWidth(5)
    graph.SetLineStyle(2)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['exp'])
    graph.SetMarkerStyle(21)
    graph.SetMarkerSize(1)
    graph.SetMarkerColor(colorSchemes[colorScheme]['exp'])
    return graph

def getExpectedGraph2D(limits,xAxisType,yAxisType,experiment_key,theory_key,colorScheme):
    graph = getGraph2D(limits, xAxisType, yAxisType, experiment_key, theory_key)
    graph.SetLineWidth(5)
    graph.SetLineStyle(2)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['exp'])
    graph.SetMarkerStyle(21)
    graph.SetMarkerSize(1)
    graph.SetMarkerColor(colorSchemes[colorScheme]['exp'])
    return graph


def getGraphAsymmErrors(limits, x_key, y_key, up_key, down_key):
    x = [ ]
    up = [ ]
    down = [ ]
    y = [ ]
    for limit in limits:
        if x_key not in limit.keys() or up_key not in limit.keys() or down_key not in limit.keys() or y_key not in limit.keys():
            continue
        x.append(float(limit[x_key]))
        up.append(float(limit[up_key]))
        down.append(float(limit[down_key]))
        y.append(float(limit[y_key]))
    graph = TGraphAsymmErrors(
        len(x),
        array('d', x),
        array('d', y),
        array('d', [0 for i in range(0, len(x))]),
        array('d', [0 for i in range(0, len(x))]),
        array('d', down),
        array('d', up)
        )
    return graph


def getBorderGraph(graph, errorType):
    N = graph.GetN ()
    otherSideX = []
    otherSideY = []
    x = array ('d')
    y = array ('d')
    for i in range (0, N):
        xPoint = Double (0.0)
        yPoint = Double (0.0)
        graph.GetPoint (i, xPoint, yPoint)
        if errorType =='horizontal':
            eHigh = graph.GetErrorXhigh (i)
            eLow = graph.GetErrorXlow (i)
            otherSideX.append (xPoint.value - eLow)
            otherSideY.append (yPoint.value)
            x.append (xPoint.value + eHigh)
            y.append (yPoint.value)
        if errorType =='vertical':
            eHigh = graph.GetErrorYhigh (i)
            eLow = graph.GetErrorYlow (i)
            otherSideX.append (xPoint.value)
            otherSideY.append (yPoint.value - eLow)
            x.append (xPoint.value)
            y.append (yPoint.value + eHigh)
    for i in range (0, -N, -1):
        x.append (otherSideX[i - 1])
        y.append (otherSideY[i - 1])
    borderGraph = TGraph (len (x), x, y)
    return borderGraph

def getGraphAsymmErrors2D(limits, x_key, y_key, experiment_key, up_key, down_key):
    central = getGraph2D (limits, x_key, y_key, experiment_key, 'theory')
    up = TGraph ()
    down = TGraph ()
    if experiment_key =='expected':
        up = getGraph2D (limits, x_key, y_key, down_key, 'theory')
        down = getGraph2D (limits, x_key, y_key, up_key, 'theory')
    if experiment_key =='observed':
        up = getGraph2D (limits, x_key, y_key, 'observed', up_key)
        down = getGraph2D (limits, x_key, y_key, 'observed', down_key)
    x = []
    y = []
    eXLow = []
    eXHigh = []
    eYLow = []
    eYHigh = []
    for i in range (0, central.GetN ()):
        xPoint = Double (0.0)
        yPoint = Double (0.0)
        upXPoint = Double (0.0)
        upYPoint = Double (0.0)
        downXPoint = Double (0.0)
        downYPoint = Double (0.0)
        central.GetPoint (i, xPoint, yPoint)
        up.GetPoint (i, upXPoint, upYPoint)
        down.GetPoint (i, downXPoint, downYPoint)
        x.append (xPoint)
        y.append (yPoint)
        if arguments.verbose:
            print( "Debug:  appending point: (" + str(xPoint) + ", " + str(yPoint))
        if y_key =='lifetime':
            eXHigh.append (upXPoint)
            eXLow.append (downXPoint)
            eYHigh.append (0.0)
            eYLow.append (0.0)
        if x_key =='lifetime':
            eXHigh.append (0.0)
            eXLow.append (0.0)
            eYHigh.append (upYPoint)
            eYLow.append (downYPoint)
    for i in range (0, len (x)):
        if y_key =='lifetime':
            eXHigh[i] = Double(eXHigh[i].value - x[i].value)
            eXLow[i] = Double(x[i].value - eXLow[i].value)
        if x_key =='lifetime':
            eYHigh[i] = Double(eYHigh[i].value - y[i].value)
            eYLow[i] = Double(y[i].value - eYLow[i].value)
    graph = TGraphAsymmErrors (len (x),
                               array ('d', [i.value for i in x]),
                               array ('d', [i.value for i in y]),
                               array ('d', [i.value for i in eXLow]),
                               array ('d', [i.value for i in eXHigh]),
                               array ('d', eYLow),
                               array ('d', eYHigh))
    borderGraph = TGraphAsymmErrors ()
    if y_key =='lifetime':
        borderGraph = getBorderGraph (graph, 'horizontal')
    if x_key =='lifetime':
        borderGraph = getBorderGraph (graph, 'vertical')
    return borderGraph


def getOneSigmaGraph(limits,xAxisType,colorScheme):
    graph = getGraphAsymmErrors(limits, xAxisType, 'expected', 'up1', 'down1')
    graph.SetFillColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetFillStyle(1001)
    graph.SetLineColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['oneSigma'])
    return graph

def getOneSigmaGraph2D(limits,xAxisType,yAxisType,colorScheme):
    graph = getGraphAsymmErrors2D(limits, xAxisType, yAxisType, 'expected', 'up1', 'down1')
    graph.SetFillColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetFillStyle(1001)
    graph.SetLineColor(colorSchemes[colorScheme]['oneSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['oneSigma'])
    return graph

def getTwoSigmaGraph(limits,xAxisType,colorScheme):
    graph = getGraphAsymmErrors(limits, xAxisType, 'expected', 'up2', 'down2')
    graph.SetFillColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetFillStyle(1001)
    graph.SetLineColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['twoSigma'])
    return graph

def getTwoSigmaGraph2D(limits,xAxisType,yAxisType,colorScheme):
    graph = getGraphAsymmErrors2D(limits, xAxisType, yAxisType, 'expected', 'up2', 'down2')
    graph.SetFillColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetFillStyle(1001)
    graph.SetLineColor(colorSchemes[colorScheme]['twoSigma'])
    graph.SetMarkerColor(colorSchemes[colorScheme]['twoSigma'])
    return graph


def fetchLimits(mass,lifetime,directories):
    limit = { }
    limit['expected'] = 1.0e12

    if arguments.verbose:
        print( "Debug:  running fetchLimits for mass = " + str(mass) + "; lifetime = " + str(lifetime) + "; directories = " + str(directories))
    for directory in directories:
        if not os.path.exists(os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/test/limits/"+directory+"/method.txt"):
            print( "Returning -1 for no method.txt file")
            return -1
        with open(os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/test/limits/"+directory+"/method.txt", 'r') as methodFile:
            method = methodFile.readline()

        #########################################################

        tmp_limit = { }
        # for Asymptotic CLs, get the limits from the root file
        if method == "AsymptoticLimits":
            file = TFile(makeSignalRootFileName(mass,lifetime,directory,"expected"))
            #file = TFile(makeSignalRootFileName(chiMasses[mass]['value'],lifetime,directory,"expected"))
            limit_tree = file.Get('limit')
            if limit_tree.GetEntries() < 6:
                continue
            for i in range(0,limit_tree.GetEntries()):
                limit_tree.GetEntry(i)
                quantileExpected = limit_tree.quantileExpected
                if quantileExpected == 0.5:
                    tmp_limit['expected'] = limit_tree.limit
                if math.fabs(quantileExpected - 0.025) < 0.0001:
                    tmp_limit['down2'] = limit_tree.limit
                if math.fabs(quantileExpected - 0.16) < 0.0001:
                    tmp_limit['down1'] = limit_tree.limit
                if math.fabs(quantileExpected - 0.84) < 0.0001:
                    tmp_limit['up1'] = limit_tree.limit
                if math.fabs(quantileExpected - 0.975) < 0.0001:
                    tmp_limit['up2'] = limit_tree.limit
            file.Close()

            file = TFile(makeSignalRootFileName(mass,lifetime,directory,"observed"))
            limit_tree = file.Get('limit')
            if not file.GetNkeys():
                print( "Returning -1 for file.GetNKeys")
                return -1

            limit_tree = file.Get('limit')
            if not limit_tree:
                print ("Returning -1 for no limit_tree")
                return -1
            if limit_tree.GetEntries() < 6:
                continue
            for i in range(0,limit_tree.GetEntries()):
                limit_tree.GetEntry(i)
                quantileExpected = limit_tree.quantileExpected
                if quantileExpected == -1.0:
                    tmp_limit['observed'] = limit_tree.limit
            file.Close()
        #########################################################

        elif method == "AsymptoticSignificance":
            file = TFile(makeSignalRootFileName(mass, lifetime, directory, "expected"))
            limit_tree = file.Get('limit')
            if not file.GetNkeys():
                print ("Returning -1 for file.GetNkeys")
                return -1
            limit_tree = file.Get('limit')
            if not limit_tree:
                print ("Returning -1 for no limit_tree")
                return -1
            if limit_tree.GetEntries() != 1:
                continue
            limit_tree.GetEntry(0)
            tmp_limit['expected'] = limit_tree.limit
            tmp_limit['down1'] = 0
            tmp_limit['down2'] = 0
            tmp_limit['up1'] = 0
            tmp_limit['up2'] = 0
            file.Close()

            file = TFile(makeSignalRootFileName(mass, lifetime, directory, "observed"))
            limit_tree = file.Get('limit')
            if not file.GetNkeys():
                print( "Returning -1 for file.GetNkeys")
                return -1
            limit_tree = file.Get('limit')
            if not limit_tree:
                print( "Returning -1 for no limit_tree")
                return -1
            if limit_tree.GetEntries() != 1:
                continue
            limit_tree.GetEntry(0)
            tmp_limit['observed'] = limit_tree.limit
            file.Close()
        #########################################################

        elif method == "HybridNew":
            # Initialize to large default value, to avoid errors if a single point fails
            tmp_limit['observed'] = 99999.
            tmp_limit['expected'] = 99999.
            tmp_limit['up1'] = 99999.
            tmp_limit['up2'] = 99999.
            tmp_limit['down1'] = 99999.
            tmp_limit['down2'] = 99999.

            # print "Debug: opening file: "
            file = open(makeSignalLogFileName(mass,lifetime,directory,"expected"))
            # print makeSignalLogFileName(mass,lifetime,directory,"expected")
            i = 0
            for line in file:
                ## if i < 10:
                ## print "Debug: line = ", line
                ## i += 1
                if "Limit:" in line:
                    tmp_limit['expected'] = float(line.split(" ")[3]) # Use the last occurence of "Limit:" as the most accurate
                    # print "Debug: Setting limit from line: ", line
            file.close()
            if arguments.verbose:
                print( "Debug: found expected limit: ", tmp_limit['expected'])

            # print "Debug: opening observed file: "
            file = open(makeSignalLogFileName(mass,lifetime,directory,"observed"))
            for line in file:
                if "Limit:" in line:
                    tmp_limit['observed'] = float(line.split(" ")[3]) # Use the last occurence of "Limit:" as the most accurate
            file.close()
            if arguments.verbose:
                print( "Debug: found observed limit: ", tmp_limit['observed'])

            # print "Debug: opening up1 file: "
            file = open(makeSignalLogFileName(mass,lifetime,directory,"expected_up1"))
            for line in file:
                if "Limit:" in line:
                    tmp_limit['up1'] = float(line.split(" ")[3]) # Use the last occurence of "Limit:" as the most accurate
            file.close()
            if arguments.verbose:
                print( "Debug: found up1 limit: ", tmp_limit['up1'])

            # print "Debug: opening up2 file: "
            file = open(makeSignalLogFileName(mass,lifetime,directory,"expected_up2"))
            for line in file:
                if "Limit:" in line:
                    tmp_limit['up2'] = float(line.split(" ")[3]) # Use the last occurence of "Limit:" as the most accurate
            file.close()
            if arguments.verbose:
                print( "Debug: found up2 limit: ", tmp_limit['up2'])

            # print "Debug: opening down1 file: "
            file = open(makeSignalLogFileName(mass,lifetime,directory,"expected_down1"))
            for line in file:
                if "Limit:" in line:
                    tmp_limit['down1'] = float(line.split(" ")[3]) # Use the last occurence of "Limit:" as the most accurate
            file.close()
            if arguments.verbose:
                print( "Debug: found down1 limit: ", tmp_limit['down1'])

            # print "Debug: opening down2 file: "
            file = open(makeSignalLogFileName(mass,lifetime,directory,"expected_down2"))
            for line in file:
                if "Limit:" in line:
                    tmp_limit['down2'] = float(line.split(" ")[3]) # Use the last occurence of "Limit:" as the most accurate
            file.close()
            if arguments.verbose:
                print( "Debug: found down2 limit: ", tmp_limit['down2'])

        # for other methods, get the ranges from the log file
        else:
            file = open(makeSignalLogFileName(mass,lifetime,directory,"expected"))
            #print "Debug:  opening file: "
            #print makeSignalLogFileName(mass,lifetime,directory,"expected")
            for line in file:
                #print "Debug: line = " + line
                line = line.rstrip("\n").split(":")
                if line[0] == "median expected limit":
                    tmp_limit['expected'] = float(line[1].split(" ")[3])
                elif line[0] == "   68% expected band ":
                    tmp_limit['down1'] = float(line[1].split(" ")[1])
                    tmp_limit['up1'] = float(line[1].split(" ")[5])
                elif line[0] == "   95% expected band ":
                    tmp_limit['down2'] = float(line[1].split(" ")[1])
                    tmp_limit['up2'] = float(line[1].split(" ")[5])
            file.close()
            #print "Debug:  finished expected"

            file = open(makeSignalLogFileName(mass,lifetime,directory,"observed"))
            #print "Debug:  opening observed file: "
            #print makeSignalLogFileName(mass,lifetime,directory,"observed")
            for line in file:
                line = line.rstrip("\n").split(":")
                if line[0] =="Limit": #observed limit
                    tmp_limit['observed'] = float(line[1].split(" ")[3])
            file.close()

        if not arguments.plotSignificance:
            tmp_limit['up2'] = math.fabs(tmp_limit['up2'] - tmp_limit['expected'])
            tmp_limit['up1'] = math.fabs(tmp_limit['up1'] - tmp_limit['expected'])
            tmp_limit['down2'] = math.fabs(tmp_limit['down2'] - tmp_limit['expected'])
            tmp_limit['down1'] = math.fabs(tmp_limit['down1'] - tmp_limit['expected'])

            xSection = float(signal_cross_sections[str(mass)]['value'])
            # The limits are given as fractions r of the estimated yield: r = Y_limit / Y_est,
            # where Y_est = Lumi*xSection_theory*eff
            # Note that since lumi and eff are constant, r = xSection_limit / xSection_theory
            # So to get the limit in pb, multiply by the theory cross section:
            # xSection_limit = r * xSection_theory
            tmp_limit['up2'] *= xSection
            tmp_limit['up1'] *= xSection
            tmp_limit['observed'] *= xSection
            tmp_limit['expected'] *= xSection
            tmp_limit['down1'] *= xSection
            tmp_limit['down2'] *= xSection

        try:
            f = open (makeSignalSFFileName (mass,lifetime,directory))
            sf = float (f.readline ().rstrip ("\n"))
            f.close ()

            tmp_limit['up2'] *= sf
            tmp_limit['up1'] *= sf
            tmp_limit['observed'] *= sf
            tmp_limit['expected'] *= sf
            tmp_limit['down1'] *= sf
            tmp_limit['down2'] *= sf
        except IOError:
            pass

        if arguments.verbose:
            print( "Debug:  observed limit in pb = ", tmp_limit['observed'], ", xSection in pb = ", xSection)

        tmp_limit['mass'] = mass
        tmp_limit['lifetime'] = lifetime
        if convertCmToNs:
            speedLightCmPerNs = TMath.C () * 1.0e-7
            tmp_limit['lifetime'] = float(lifetime) / speedLightCmPerNs
        if tmp_limit['expected'] < limit['expected']:
            limit = tmp_limit
    return (limit if limit['expected'] < 9.9e11 else -1)

def drawPlot(plot, th2fType=""):
    gStyle.SetPalette(62) # kColorPrintableOnGrey
    is2D = 'yAxisType' in plot
    isMakeTable = False
    hasTH2F = False
    outputFile.cd()
    canvas = TCanvas(plot['title'], "", 800, 800)
    if 'th2fs' in plot:
        hasTH2F = True
        canvas = TCanvas(plot['title']+th2fType, "", 800, 800)
    canvas.SetLeftMargin (0.1425)
    canvas.SetRightMargin (0.035)
    canvas.SetTopMargin (0.065)
    canvas.SetBottomMargin (0.11625)

    xAxisMin = 1
    yAxisMin = 1
    xAxisMax = 2
    yAxisMax = 2
    xAxisBins = array('d')
    yAxisBins = array('d')
    nBinsX = 1
    nBinsY = 1
    if plot['xAxisType'] =='mass':
        xAxisMin = float(masses[0])
        xAxisMax = float(masses[-1])
    elif plot['xAxisType'] =='lifetime':
        xAxisMin = float(lifetimes[0])
        xAxisMax = float(lifetimes[-1])
    if is2D:
        canvas.SetLogz()
        if plot['yAxisType'] =='mass':
            yAxisMin = float(masses[0])
            yAxisMax = float(masses[-1])
            xAxisBins.extend ([float (lifetime) for lifetime in lifetimes])
            xAxisBins.append (2.0 * float (lifetimes[-1]))
            yAxisBins.extend ([float (mass) for mass in masses])
            yAxisBins.append (2.0 * float (masses[-1]) - float (masses[-2]))
            yAxisBins.append (8.0 * float (masses[-1]) - 4.0 * float (masses[-2]))
        elif plot['yAxisType'] =='lifetime':
            yAxisMin = float(lifetimes[0])
            yAxisMax = 2 * float(lifetimes[-1])
            if not plot['convertToMassSplitting']:
                canvas.SetLogy()
            xAxisBins.extend ([float (mass) for mass in masses])
            xAxisBins.append (2.0 * float (masses[-1]) - float (masses[-2]))
            yAxisBins.extend ([float (lifetime) for lifetime in lifetimes])
            yAxisBins.append (2.0 * float (lifetimes[-1]))
            yAxisBins.append (8.0 * float (lifetimes[-1]))
        nBinsX = len (xAxisBins) - 1
        nBinsY = len (yAxisBins) - 1
    else:
        canvas.SetLogy()
    if plot['convertToMassSplitting']:
        legend = TLegend(0.180451, 0.352067, 0.538847, 0.482558)  # determine coordinates empirically
    else:
        if plot['title'] == 'lifetime_vs_mass':
            legend = TLegend(0.180451, 0.392067, 0.538847, 0.522558)
        else:
            legend = TLegend(0.5877193, 0.7422481, 0.9461153, 0.872739)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.0361757)

    #construct tGraph objects for all curves and draw them
    tGraphs = []
    tTh2fs = []

    # build a dummy background histogram to better control axis ranges
    hBackground = TH1F('hBackground', 'hBackground', int(xAxisMax - xAxisMin), xAxisMin, xAxisMax)
    hBackground.GetXaxis().SetTitle(plot['xAxisLabel'])
    hBackground.GetXaxis().SetLabelOffset (0.005)
    hBackground.GetXaxis().SetLabelSize (0.04)
    hBackground.GetXaxis().SetTitleOffset (1.25)
    hBackground.GetXaxis().SetTitleSize (0.04)
    hBackground.GetYaxis().SetLabelOffset (0.005)
    hBackground.GetYaxis().SetLabelSize (0.04)
    hBackground.GetYaxis().SetTitleOffset (1.25)
    hBackground.GetYaxis().SetTitleSize (0.04)
    hBackground.GetXaxis().SetNdivisions (505)
    hBackground.GetYaxis().SetNdivisions (505)
    if 'xAxisFixMin' in plot:
        hBackground.GetXaxis().SetLimits   (plot['xAxisFixMin'], plot['xAxisFixMax'])
        hBackground.GetXaxis().SetRangeUser(plot['xAxisFixMin'], plot['xAxisFixMax'])
    else:
        hBackground.GetXaxis().SetLimits(0.9 * xAxisMin, 1.1 * xAxisMax)
        hBackground.GetXaxis().SetRangeUser(xAxisMin, xAxisMax)
    if not is2D:
        if arguments.paperMode:
            hBackground.GetYaxis().SetTitle('#sigma #bf{#it{#Beta}} [pb]')
        else:
            hBackground.GetYaxis().SetTitle('#sigma (pp #rightarrow #tilde{#chi}#tilde{#chi}) [pb]')
        if 'yAxis' in plot:
            hBackground.GetYaxis().SetRangeUser(plot['yAxis'][0], plot['yAxis'][1])
        else:
            hBackground.GetYaxis().SetRangeUser(0.9 * absMin, 1.1 * absMax)
    else:
        hBackground.GetYaxis().SetTitle(plot['yAxisLabel'])
        if 'yAxisFixMin' in plot:
            hBackground.GetYaxis().SetLimits   (plot['yAxisFixMin'], plot['yAxisFixMax'])
            hBackground.GetYaxis().SetRangeUser(plot['yAxisFixMin'], plot['yAxisFixMax'])
        else:
            hBackground.GetYaxis().SetLimits(0.9 * yAxisMin, 1.1 * yAxisMax)
            hBackground.GetYaxis().SetRangeUser(yAxisMin, yAxisMax)

    if hasTH2F:
        th2f = plot['th2fs']
        if th2fType =='exp':
            tTh2fs.append(getTH2F(th2f['limits'],plot['xAxisType'],plot['yAxisType'],'expected', 'theory'))
        if th2fType =='obs':
            tTh2fs.append(getTH2F(th2f['limits'],plot['xAxisType'],plot['yAxisType'],'observed', 'theory'))
        tTh2fs[-1].SetTitle("")
        tTh2fs[-1].GetXaxis().SetTitle(plot['xAxisLabel'])
        tTh2fs[-1].GetYaxis().SetTitle(plot['yAxisLabel'])
        tTh2fs[-1].GetZaxis().SetTitle(plot['zAxisLabel'])

        tTh2fs[-1].GetXaxis().SetTitleOffset(1.25)
        tTh2fs[-1].GetYaxis().SetTitleOffset(1.25)
        tTh2fs[-1].GetZaxis().SetTitleOffset(1.45)

        tTh2fs[-1].GetXaxis().SetTitleSize(0.04)
        tTh2fs[-1].GetYaxis().SetTitleSize(0.04)
        tTh2fs[-1].GetZaxis().SetTitleSize(0.03)

        tTh2fs[-1].GetXaxis().SetLabelOffset(0.005)
        tTh2fs[-1].GetYaxis().SetLabelOffset(0.005)
        tTh2fs[-1].GetZaxis().SetLabelOffset(0.005)

        tTh2fs[-1].GetXaxis().SetLabelSize(0.04)
        tTh2fs[-1].GetYaxis().SetLabelSize(0.04)
        tTh2fs[-1].GetZaxis().SetLabelSize(0.03)

        tTh2fs[-1].GetXaxis().SetNdivisions(505)
        tTh2fs[-1].GetYaxis().SetNdivisions(505)
        tTh2fs[-1].GetZaxis().SetNdivisions(505)

        if 'xAxisFixMin' in plot and 'xAxisFixMax' in plot:
            tTh2fs[-1].GetXaxis().SetRangeUser(plot['xAxisFixMin'],plot['xAxisFixMax'])
        if 'yAxisFixMin' in plot and 'yAxisFixMax' in plot:
            tTh2fs[-1].GetYaxis().SetRangeUser(plot['yAxisFixMin'],plot['yAxisFixMax'])
        if 'zAxisFixMin' in plot:
            tTh2fs[-1].SetMinimum(plot['zAxisFixMin'])
        if 'zAxisFixMax' in plot:
            tTh2fs[-1].SetMaximum(plot['zAxisFixMax'])
        if 'fillPotHoles' in plot:
            if plot['fillPotHoles']:
                fillPotHolesTH2F(tTh2fs[-1])
        tTh2fs[-1].SetContour(99)
        if 'extraDrawOptions' in plot:
            tTh2fs[-1].Draw('colz ' + extraDrawOptions)
        else:
            tTh2fs[-1].Draw('colz')
    else:
        hBackground.Draw('axis')

    if (not is2D) and ('showTheory' in plot and plot['showTheory']) and ('showTheoryError' in plot and plot['showTheoryError']):
        if plot['xAxisType'] =='mass':
            tGraphs.append(getTheoryOneSigmaGraph())
            tGraphs[-1].Draw('3')
            legend.AddEntry(tGraphs[-1], "#pm1 #sigma: theory", 'F')
            tGraphs.append(getTheoryGraph())
            tGraphs[-1].Draw('L')
            if arguments.paperMode:
                legend.AddEntry(tGraphs[-1], 'NLO+NLL prediction', 'L')
            else:
                legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')
    if 'graphs' in plot.keys():
        if arguments.paperMode:
            if not plot['title'] == 'lifetime_vs_mass':
                legend.SetHeader('95% CL upper limits')
            else:
                legend.SetHeader('95% CL limit')
        for graph in plot['graphs']:
            colorScheme = 'brazilian'
            if 'colorScheme' in graph:
                colorScheme = graph['colorScheme']
            if not is2D:
                for graphName in graph['graphsToInclude']:

                    if graphName =='twoSigma':
                        tGraphs.append(getTwoSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
                        tGraphs[-1].Draw('3')
                        if arguments.paperMode:
                            legendEntry = '#pm2 #sigma_{experiment}'
                        else:
                            legendEntry = '#pm2 #sigma'
                        if graphName =='legendEntry':
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                        tGraphs[-1].SetName(plot['title']+"_graph_twoSigma")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()

                    if graphName =='oneSigma':
                        tGraphs.append(getOneSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
                        tGraphs[-1].Draw('3')
                        if arguments.paperMode:
                            legendEntry = '#pm1 #sigma_{experiment}'
                        else:
                            legendEntry = '#pm1 #sigma'
                        if graphName =='legendEntry':
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                        tGraphs[-1].SetName(plot['title']+"_graph_oneSigma")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()

                    if graphName =='exp':
                        tGraphs.append(getExpectedGraph(graph['limits'],plot['xAxisType'],colorScheme))
                        tGraphs[-1].Draw('L')
                        if arguments.paperMode:
                            legendEntry = 'Median expected'
                        else:
                            legendEntry = 'exp. limit'
                        if graphName =='legendEntry':
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                        tGraphs[-1].SetName(plot['title']+"_graph_expected")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()

                    if graphName =='obs':
                        tGraphs.append(getObservedGraph(graph['limits'],plot['xAxisType'],colorScheme))
                        tGraphs[-1].Draw('L')
                        if arguments.paperMode:
                            legendEntry = 'Observed'
                        else:
                            legendEntry = 'obs. limit'
                        if graphName =='legendEntry':
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                        tGraphs[-1].SetName(plot['title']+"_graph_observed")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()

            else:  # is2D == True
                for graphName in graph['graphsToInclude']:
                    if graphName =='twoSigma':
                        tGraphs.append(getTwoSigmaGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],colorScheme))
                        if 'legendEntry' in graph:  # make transparent if graphs from two sources are being compared
                            tGraphs[-1].SetFillStyle(3001)
                        tGraphs[-1].Draw('F')
                        if arguments.paperMode:
                            legendEntry = '#pm2 #sigma_{experiment}'
                        else:
                            legendEntry = 'Expected limit #pm2 #sigma'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                        tGraphs[-1].SetName(plot['title']+"_graph_twoSigma")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()
                    if graphName =='oneSigma':
                        tGraphs.append(getOneSigmaGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],colorScheme))
                        if 'legendEntry' in graph:  # make transparent if graphs from two sources are being compared
                            tGraphs[-1].SetFillStyle(3001)
                        tGraphs[-1].Draw('F')
                        if arguments.paperMode:
                            legendEntry = '#pm1 #sigma_{experiment}'
                        else:
                            legendEntry = 'Expected limit #pm1 #sigma'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                        tGraphs[-1].SetName(plot['title']+"_graph_oneSigma")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()
                    if graphName =='exp':
                        tGraphs.append(getExpectedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'expected','theory',colorScheme))
                        #makeExpLimitsTable(graph['limits'],plot['xAxisType'],plot['yAxisType'],'expected','theory',colorScheme)
                        makeExpLimitsTable(graph['limits'],plot['xAxisType'],plot['yAxisType'],'expected','theory')
                        tGraphs[-1].Draw('L')
                        if arguments.paperMode:
                            legendEntry = 'Median expected'
                        else:
                            legendEntry = 'Expected limit'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                        tGraphs[-1].SetName(plot['title']+"_graph_expected")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()
                    if graphName =='twoSigmaTheory':
                        isMakeTable = True
                        tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','down2',colorScheme))
                        lineWidth = tGraphs[-1].GetLineWidth ()
                        tGraphs[-1].SetLineWidth (lineWidth - 4)
                        tGraphs[-1].Draw('L')
                        tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','up2',colorScheme))
                        tGraphs[-1].SetLineWidth (lineWidth - 4)
                        tGraphs[-1].Draw('L')
                        legendEntry = '#pm2 #sigma_{theory}'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                        tGraphs[-1].SetName(plot['title']+"_graph_twoSigmaTheory")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()
                    if graphName =='oneSigmaTheory':
                        tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','down1',colorScheme))
                        lineWidth = tGraphs[-1].GetLineWidth ()
                        tGraphs[-1].SetLineWidth (lineWidth - 2)
                        tGraphs[-1].Draw('L')
                        tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','up1',colorScheme))
                        tGraphs[-1].SetLineWidth (lineWidth - 2)
                        tGraphs[-1].Draw('L')
                        legendEntry = '#pm1 #sigma_{theory}'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                        tGraphs[-1].SetName(plot['title']+"_graph_oneSigmaTheory")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()
                    if graphName =='obs':
                        tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','theory',colorScheme))
                        makeObsLimitsTable(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','theory')
                        tGraphs[-1].Draw('L')
                        if arguments.paperMode:
                            legendEntry = 'Observed'
                        else:
                            legendEntry = 'Observed limit'
                        if 'legendEntry' in graph:
                            legendEntry = legendEntry + ": " + graph['legendEntry']
                        legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                        tGraphs[-1].SetName(plot['title']+"_graph_observed")
                        print( "Writing TGraph with name: ", tGraphs[-1].GetName())
                        tGraphs[-1].Write()
    if (not is2D) and ('showTheory' in plot and plot['showTheory']) and ('showTheoryError' not in plot or not plot['showTheoryError']):
        if plot['xAxisType'] =='mass':
            tGraphs.append(getTheoryGraph())
            tGraphs[-1].Draw('L')
            if arguments.paperMode:
                legend.AddEntry(tGraphs[-1], 'NLO+NLL prediction', 'L')
            else:
                legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')
            tGraphs[-1].SetName(plot['title']+"_graph_theory")
            print( "Writing TGraph with name: ", tGraphs[-1].GetName())
            tGraphs[-1].Write()
    if not is2D:
    #get the min and max of all graphs, so the y-axis can be set appropriately
        absMin =  999
        absMax = -999
        for tGraph in tGraphs:
            histo = tGraph.GetHistogram()
            plotMax = histo.GetMaximum()
            plotMin = histo.GetMinimum()
            if plotMin < absMin:
                absMin = plotMin
            if plotMax > absMax:
                absMax = plotMax

    if not 'drawTheoryCurve' in plot or not plot['drawTheoryCurve']:
        legend.Draw()
    legend.Draw()
    canvas.SetTitle('')

    #draw the header label
    HeaderLabel = TPaveLabel(0.695489, 0.939276, 0.974937, 0.989664, HeaderText, "NDC") # from makePlots.py

    HeaderLabel.SetTextAlign(32)
    HeaderLabel.SetTextFont(42)
    HeaderLabel.SetTextSize(0.756287)
    HeaderLabel.SetBorderSize(0)
    HeaderLabel.SetFillColor(0)
    HeaderLabel.SetFillStyle(0)
    HeaderLabel.Draw()

    if 'theoryHeader' in plot:
        TheoryHeaderLabel = TPaveLabel(0.14787, 0.932171, 0.434837, 0.982558, plot['theoryHeader'], "NDC")
        TheoryHeaderLabel.SetTextSize(0.512816)
        TheoryHeaderLabel.SetTextFont(42)
        TheoryHeaderLabel.SetTextAlign(12)
        TheoryHeaderLabel.SetBorderSize(0)
        TheoryHeaderLabel.SetFillColor(0)
        TheoryHeaderLabel.SetFillStyle(0)
        TheoryHeaderLabel.Draw()

    if plot['makeColorPlot']:
        LumiLabel = TPaveLabel(0.150376,0.93863,0.438596,0.989018, "CMS" if arguments.paperMode else "CMS Preliminary", "NDC")
        LumiLabel.SetTextSize(0.769225)
    elif plot['convertToMassSplitting']:
        LumiLabel = TPaveLabel(0.186717,0.615285,0.383459,0.71606,"CMS Preliminary","NDC")
        LumiLabel.SetTextSize(0.448718)
    else:
        if plot['title'] == 'lifetime_vs_mass':
            LumiLabel = TPaveLabel(0.180451, 0.675065, 0.377193, 0.777132, "CMS" if arguments.paperMode else "CMS Preliminary", "NDC")
        else:
            LumiLabel = TPaveLabel(0.179198, 0.8074935,0.3270677,0.9095607, "CMS" if arguments.paperMode else "CMS Preliminary", "NDC")
        LumiLabel.SetTextSize(0.448718)
    LumiLabel.SetTextFont(62)
    LumiLabel.SetTextAlign(12)
    LumiLabel.SetBorderSize(0)
    LumiLabel.SetFillColor(0)
    LumiLabel.SetFillStyle(0)
    LumiLabel.Draw()

    theoryLabels = []
    if 'theoryLabel' in plot:
        for i in range (0, len (plot["theoryLabel"])):
            label = plot['theoryLabel'][i]
            if plot['makeColorPlot'] or plot['convertToMassSplitting']:
                TheoryLabel = TPaveLabel(0.0200501, 0.541641, 0.433584, 0.611409, label, "NDC")
            else:
                if plot['title'] == 'lifetime_vs_mass':
                    if i == 0:
                        TheoryLabel = TPaveLabel(0.04636591, 0.5736434, 0.4598997, 0.6434109, label, "NDC")
                    else:
                        TheoryLabel = TPaveLabel(0.10401, 0.6369509, 0.5175439, 0.7067183, label, "NDC")
                    TheoryLabel.SetTextAlign(32)
                else:
                    if i == 0:
                        TheoryLabel = TPaveLabel(0.14787, 0.726098, 0.531328, 0.776486, label, "NDC")
                        TheoryLabel.SetTextAlign(22)
                    else:
                        TheoryLabel = TPaveLabel(0.1065163, 0.77261, 0.5200501, 0.842377, label, "NDC")
                        TheoryLabel.SetTextAlign(32)
            TheoryLabel.SetTextFont(42)
            TheoryLabel.SetTextSize(0.517241)
            TheoryLabel.SetBorderSize(0)
            TheoryLabel.SetFillColor(0)
            TheoryLabel.SetFillStyle(0)
            TheoryLabel.Draw()
            theoryLabels.append (TheoryLabel)

    if 'massLabel' in plot:
        MassLabel = TPaveLabel(0.1637931,0.8220339,0.362069,0.8919492,plot['massLabel'],"NDC")
        MassLabel.SetTextSize(0.5454546)
        MassLabel.SetTextAlign(12)
        MassLabel.SetBorderSize(0)
        MassLabel.SetFillColor(0)
        MassLabel.SetFillStyle(0)
        MassLabel.Draw()

    if 'brLabel' in plot:
        BRLabel = TPaveLabel(0.1609195,0.779661,0.5014368,0.8368644,plot['brLabel'],"NDC")
        BRLabel.SetTextSize(0.6666667)
        BRLabel.SetTextAlign(12)
        BRLabel.SetBorderSize(0)
        BRLabel.SetFillColor(0)
        BRLabel.SetFillStyle(0)
        BRLabel.Draw()

    if plot['makeColorPlot']:
        canvas.SetLeftMargin(0.15)
        canvas.SetRightMargin(0.15)
    canvas.Update()

    canvas.RedrawAxis('g')
    if 'drawTheoryCurve' in plot and plot['drawTheoryCurve']:
        function = TF1("function","-413.315+305.383*log(x) - 60.8831*log(x)^2 + 5.41948 * log(x)^3 - 0.181509*log(x)^4",100,600)
        function.SetLineStyle(2)
        function.Draw("same")
        legend.AddEntry(function, "Theory (Phys. Lett. B721 (2013) 252)" ,"L")
        legend.Draw("same")
        gStyle.SetHatchesSpacing(0.01)
        mPi = 0.13957018  # units of GeV, from PDG
        stableChiLabel = TPaveLabel(100, plot['yAxisFixMin'], 600, mPi*1000, "")
        legend.AddEntry(stableChiLabel, "#tilde{#chi}^{#pm} #rightarrow #tilde{#chi}^{0} #pi^{#pm} forbidden" ,"F")
        stableChiLabel.SetTextSize(0.6666667)
        stableChiLabel.SetTextAlign(12)
        stableChiLabel.SetBorderSize(0)
        stableChiLabel.SetFillColor(13)
        stableChiLabel.SetFillStyle(3001)
        stableChiLabel.Draw("same")

    canvas.Write()

    outputPlotName = "limits/"+arguments.outputDir+"/"+plot['title']
    if 'th2fs' in plot:
        outputPlotName = outputPlotName + "_" + th2fType
    canvas.SaveAs(outputPlotName+".pdf")
    canvas.SaveAs(outputPlotName+".C")
    # canvas.SetLogy(0)
    # canvas.SaveAs("limits/"+arguments.outputDir+"/"+plot['title']+"_lin.pdf")
    print ("Wrote plot to " + outputPlotName + ".pdf")

######################################################################################################


outputFileName = "limits/"+arguments.outputDir+"/"+outputName
outputFile = TFile(outputFileName, "RECREATE")

# for each plot that has been defined, extract the limits and draw the plot accordingly
for plot in plotDefinitions:

    if arguments.plotSignificance:
        if not plot['title'].startswith('significance'):
            continue
    else:
        if plot['title'].startswith('significance'):
            continue

    #fetch all the limits needed for this plot
    if 'th2fs' in plot:
        th2f = plot['th2fs']
        th2f['limits'] = []
        if 'xAxisType' not in plot or 'yAxisType' not in plot:
            print( "You want to draw a 2D plot but either X or Y axis is not defined.")
        else:
            for mass in masses:
                for lifetime in lifetimes:
                    limit = fetchLimits(mass,lifetime,[arguments.outputDir])
                    if limit != -1:
                        th2f['limits'].append(limit)
                    else:
                        print( "WARNING: not plotting mass " + str (mass) + " GeV, lifetime " + str (lifetime) + " cm")
    if 'graphs' in plot.keys():
        for graph in plot['graphs']:
            graph['limits'] = []
            if plot['xAxisType'] == 'lifetime' and 'yAxisType' not in plot:
                for lifetime in lifetimes:
                    lifetime = lifetime.replace(".0", "")
                    lifetime = lifetime.replace("0.", "0p")
                    limit = fetchLimits(graph['mass'],lifetime,[arguments.outputDir])
                    if limit != -1:
                        graph['limits'].append(limit)
                    else:
                        print( "WARNING: not plotting lifetime " + str (lifetime) + " cm")
            elif plot['xAxisType'] == 'mass' and 'yAxisType' not in plot:
                for mass in masses:
                    for lifetime in lifetimes:
                        lifetime = lifetime.replace(".0", "")
                        lifetime = lifetime.replace("0.", "0p")
                        limit = fetchLimits(mass,graph['lifetime'],[arguments.outputDir])
                    if arguments.verbose:
                        print ("Debug:  limit = " + str(limit) + " for mass " + str(mass) + ", limit['expected'] = " + str(limit['expected']))
                    if limit != -1:
                        graph['limits'].append(limit)
                    else:
                        print ("WARNING: for xAxisType=mass, not plotting mass: " + str (mass) + " GeV, lifetime: " + str (lifetime) + ", source: " + arguments.outputDir)
            elif 'yAxisType' in plot:
                for mass in masses:
                    for lifetime in lifetimes:
                        limit = fetchLimits(mass,lifetime,[arguments.outputDir])
                        if limit != -1:
                            graph['limits'].append(limit)
                            if arguments.verbose:
                                print( "Debug:  limit for mass " + str(mass) + ", lifetime = " + str(lifetime) + ", limit['expected'] = " + str(limit['expected']) + ", limit['observed'] = " + str(limit['observed']))
                        else:
                            print( "WARNING: not plotting mass " + str (mass) + " GeV, lifetime " + str (lifetime) + " cm")
    #now that all the limits are in place, draw the plot
    if 'th2fs' in plot:
        for th2fType in (plot['th2fs'])['th2fsToInclude']:
            drawPlot(plot, th2fType)
    else:
        drawPlot(plot)

outputFile.Close()
print( "Finished writing ", outputFile.GetName())
