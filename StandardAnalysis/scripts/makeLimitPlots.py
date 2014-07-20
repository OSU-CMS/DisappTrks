#!/usr/bin/env python

import time
import os
import sys
import math
import copy
import re
import subprocess
import glob
from array import *
from fractions import *
from operator import itemgetter
from optparse import OptionParser
from decimal import *



parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                  help="output directory")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False, 
                  help="verbose output")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")
else:
    print "No local config specified, shame on you"
    sys.exit(0)
if arguments.outputDir:
    if not os.path.exists("limits/"+arguments.outputDir):
        os.system("mkdir limits/"+arguments.outputDir)
else:
    print "No output directory specified, shame on you"
    sys.exit(0)


from ROOT import TF1, TFile, TGraph, TGraphAsymmErrors, gROOT, gStyle, TStyle, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TPaveLabel, TH2D, TPave, Double

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

gROOT.ForceStyle()

colorSchemes = {
    'brazilian' : {
        'obs' : 1,
        'exp' : 1,
        'oneSigma' : 78, #410,
        'twoSigma' : 88, #393,
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
    LumiInPb = lumi
##     LumiText = "L_{int} = " + str(intLumi) + " pb^{-1}"
##     LumiText = "L_{int} = " + str.format('{0:.1f}', LumiInPb) + " pb^{-1}"
    LumiText = "L = " + str(intLumi) + " pb^{-1}"
    LumiText = "L = " + str.format('{0:.1f}', LumiInPb) + " pb^{-1}"
else:
    LumiInFb = intLumi/1000.
#    LumiText = "L_{int} = " + str.format('{0:.1f}', LumiInFb) + " fb^{-1}"
    LumiText = "L = " + str.format('{0:.1f}', LumiInFb) + " fb^{-1}"

#set the text for the fancy heading
HeaderText = "CMS Preliminary: " + LumiText + " at #sqrt{s} = 8 TeV"



def makeSignalName(mass,lifetime):
    lifetime = str(lifetime).replace(".0", "")
    lifetime = str(lifetime).replace("0.5", "0p5")
#    return "AMSB_mChi"+str(mass)+"_"+str(lifetime)+"ns"
    return "AMSB_mChi"+str(mass)+"_"+str(lifetime)+"cm"

def makeSignalRootFileName(mass,lifetime,directory,limit_type):
    signal_name = makeSignalName(mass,lifetime)
    if glob.glob("limits/"+directory+"/"+signal_name+"_"+limit_type+"/higgsCombine"+signal_name+".*.root"):
        os.system ("mv -f limits/"+directory+"/"+signal_name+"_"+limit_type+"/higgsCombine"+signal_name+".*.root limits/"+directory+"/"+signal_name+"_"+limit_type+"/limits_"+signal_name+".root")
    print "limits/"+directory+"/"+signal_name+"_"+limit_type+"/limits_"+signal_name+".root"
    return "limits/"+directory+"/"+signal_name+"_"+limit_type+"/limits_"+signal_name+".root"

def makeSignalLogFileName(mass,lifetime,directory,limit_type):
    signal_name = makeSignalName(mass,lifetime)
    if glob.glob("limits/"+directory+"/"+signal_name+"_"+limit_type+"/condor_0*.out"):
        os.system ("mv -f limits/"+directory+"/"+signal_name+"_"+limit_type+"/condor_0.out limits/"+directory+"/"+signal_name+"_"+limit_type+"/combine_log_"+signal_name+".txt")
    print "limits/"+directory+"/"+signal_name+"_"+limit_type+"/combine_log_"+signal_name+".txt"
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
        if not limit.has_key(x_key) or not limit.has_key(y_key):
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
    if mass < 1:  # protect against 0
        return (0, 0)
    fPi = float(0.093)
    gF = 1.166379E-5
    mPi = 0.14
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
        print "Debug found bad values for a or b:  a=", a, ", b=", b, ", c=", c, ", d=", d, ", mass = ", mass, "neumass = ", neuMass, ", sqrt(c)=", math.pow(mass,2) - math.pow(neuMass,2)
        print "Debug: lifetimeInSec=", lifetimeInSec, ", deltaM=", deltaM, ", prevDeltaMGuess=", prevDeltaMGuess
        #        print "Debug:  lifetimeGuess = ", lifetimeGuess, ", lifetimeInSec=", lifetimeInSec, ", deltaM=", deltaM, ", prevDeltaMGuess=", prevDeltaMGuess, "(lifetimeInSec - lifetimeGuess) / lifetimeInSec = ", (lifetimeInSec - lifetimeGuess) / lifetimeInSec
        return (0, 0)
        
    lifetimeGuess = hBarinGeVs / (4.0 * a * b * (c - d * deltaM))
    precision = 0.001  # precision of desired result
    if math.fabs((lifetimeInSec - lifetimeGuess) / lifetimeInSec) < precision:
        return (deltaM, prevDeltaMGuess)
    elif math.fabs((deltaM - prevDeltaMGuess) / deltaM) < precision / 10:
        #        print "Difference between deltaM=", deltaM, " and prevDeltaMGuess=", prevDeltaMGuess, " is less than precision=", precision
        return (deltaM, prevDeltaMGuess)
    else:
        if (lifetimeInSec - lifetimeGuess) > 0:
            tmp = deltaM
            deltaM -= 0.5 * math.fabs(deltaM - prevDeltaMGuess)
            if math.fabs(deltaM - 0.140) < 0.005:
                deltaM = 0.145
            prevDeltaMGuess = tmp
            return calcMassSplitting(mass, lifetimeInSec, deltaM, prevDeltaMGuess)
        else:
            tmp = deltaM
            deltaM += 0.5 * math.fabs(deltaM - prevDeltaMGuess)
            if math.fabs(deltaM - 0.140) < 0.005:
                deltaM = 0.145
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
        if experiment_key is 'up1' or experiment_key is 'up2':
            limit_dict[lifetime][mass]['experiment'] += limit['expected']
        if experiment_key is 'down1' or experiment_key is 'down2':
            limit_dict[lifetime][mass]['experiment'] = limit['expected'] - limit_dict[lifetime][mass]['experiment']
        for theory_mass in signal_cross_sections:
            if abs (float (theory_mass) - mass) < 1.0e-3:
                limit_dict[lifetime][mass]['theory'] = float (signal_cross_sections[theory_mass]['value'])
                theory_error = float (signal_cross_sections[theory_mass]['error'])
                if theory_key is 'up2' or theory_key is 'down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                if theory_key is 'up1' or theory_key is 'up2':
                    limit_dict[lifetime][mass]['theory'] *= theory_error
                if theory_key is 'down1' or theory_key is 'down2':
                    limit_dict[lifetime][mass]['theory'] *= (2.0 - theory_error)
    for lifetime in sorted (limit_dict.keys ()):
        ordered_masses = sorted (limit_dict[lifetime].keys ())
        first_allowed_mass = ordered_masses[0]
        previous_mass = ordered_masses[0]
        for mass in ordered_masses:
            if limit_dict[lifetime][mass]['theory'] < limit_dict[lifetime][mass]['experiment']:
                first_allowed_mass = mass
                break
            previous_mass = mass
        mass_limit = 0.0
        if previous_mass != first_allowed_mass:
            # find intersection using http://en.wikipedia.org/wiki/Line-line_intersection
            x1 = previous_mass
            x3 = previous_mass
            x2 = first_allowed_mass
            x4 = first_allowed_mass
            y1 = limit_dict[lifetime][previous_mass]['theory']
            y3 = limit_dict[lifetime][previous_mass]['experiment']
            y2 = limit_dict[lifetime][first_allowed_mass]['theory']
            y4 = limit_dict[lifetime][first_allowed_mass]['experiment']
            mass_limit = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
            mass_limit /= (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if math.isnan (mass_limit):
                mass_limit = 0.0
        x.append (mass_limit)
        y.append (lifetime)
        if arguments.verbose:
            print "Debug getGraph2D:  adding point: " + str(mass_limit) + ", " + str(lifetime)
            print "  Debug:  previous_mass=" + str(previous_mass) + ", first_allowed_mass=" + str(first_allowed_mass)  
            print "  Debug:  limit_dict[lifetime][first_allowed_mass]['experiment'] = " + str(limit_dict[lifetime][first_allowed_mass]['experiment']) + ", experiment_key = " + experiment_key 
            if previous_mass != first_allowed_mass:
                print "  Debug x1,x2,x3,x4=" + str(x1) + ","+ str(x2) + "," + str(x3) + "," + str(x4) + ","  + ", y1,y2,y3,y4=" + str(y1) + ","+ str(y2) + "," + str(y3) + "," + str(y4) + ","
        if x_key is 'lifetime' and y_key is 'mass':
            x[-1], y[-1] = y[-1], x[-1]

    if convertToMassSplitting:
        print "Debug:  about to print all the values that go into TGraph:"
        for i in range(len(x)):
            print i, ": ", x[i], ", ", y[i]

        lifetimeInCm = copy.deepcopy(y)

        print "Debug:  about to print all the values that go into TGraph, after converting to massSplitting:"
        for i in range(len(y)):
            y[i] = convertFromCmToMassSplitting_v3(x[i], y[i])
            print i, ": ", x[i], ", ", y[i]
            graphTest = TGraph(len(y), lifetimeInCm, y)
            graphTest.Write()

    graph = TGraph (len (x), x, y)
    return graph

def makeExpLimitsTable(limits, x_key, y_key, experiment_key, theory_key):
    x = array ('d')
    y = array ('d')
    limit_dict = {}
    expTable = open("limits/" + limit_dir + "/" + "expTable.tex", "w")
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
        if experiment_key is 'up1' or experiment_key is 'up2':
            limit_dict[lifetime][mass]['experiment'] += limit['expected']
        if experiment_key is 'down1' or experiment_key is 'down2':
            limit_dict[lifetime][mass]['experiment'] = limit['expected'] - limit_dict[lifetime][mass]['experiment']
        for theory_mass in signal_cross_sections:
            if abs (float (theory_mass) - mass) < 1.0e-3:
                limit_dict[lifetime][mass]['theory'] = float (signal_cross_sections[theory_mass]['value'])
                theory_error = float (signal_cross_sections[theory_mass]['error'])
                if theory_key is 'up2' or theory_key is 'down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                if theory_key is 'up1' or theory_key is 'up2':
                    limit_dict[lifetime][mass]['theory'] *= theory_error
                if theory_key is 'down1' or theory_key is 'down2':
                    limit_dict[lifetime][mass]['theory'] *= (2.0 - theory_error)
    for lifetime in sorted (limit_dict.keys ()):
        ordered_masses = sorted (limit_dict[lifetime].keys ())
        first_allowed_mass = ordered_masses[0]
        previous_mass = ordered_masses[0]
        for mass in ordered_masses:
            if limit_dict[lifetime][mass]['theory'] < limit_dict[lifetime][mass]['experiment']:
                first_allowed_mass = mass
                break
            previous_mass = mass
        mass_limit = 0.0
        if previous_mass != first_allowed_mass:
            # find intersection using http://en.wikipedia.org/wiki/Line-line_intersection
            x1 = previous_mass
            x3 = previous_mass
            x2 = first_allowed_mass
            x4 = first_allowed_mass
            y1 = limit_dict[lifetime][previous_mass]['theory']
            y3 = limit_dict[lifetime][previous_mass]['experiment']
            y2 = limit_dict[lifetime][first_allowed_mass]['theory']
            y4 = limit_dict[lifetime][first_allowed_mass]['experiment']
            mass_limit = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
            mass_limit /= (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if math.isnan (mass_limit):
                mass_limit = 0.0
        x.append (mass_limit)
        y.append (lifetime)

        with open ("limits/" + limit_dir + "/" + "expTable.tex", 'a') as file:
            file.write(str(lifetime) + ' & ' + str(round(mass_limit,1)) + '\\\\')
            file.write('\n')
            expTable.close()
                
    if x_key is 'lifetime' and y_key is 'mass':
        x[-1], y[-1] = y[-1], x[-1]
    graph = TGraph (len (x), x, y)

    expTable = open("limits/" + limit_dir + "/" + "expTable.tex", "a")
    expTable.write('\hline \hline')
    expTable.write('\n')
    expTable.write(' \end{tabular} \end{center}')
    expTable.close()
    print "Table of expected limits for AN stored in: limits/" + limit_dir 
    return 'Success'

def makeObsLimitsTable(limits, x_key, y_key, experiment_key, theory_key):
    x = array ('d')
    y = array ('d')
    limit_dict = {}
    obsTable = open("limits/" + limit_dir + "/" + "obsTable.tex", "w")
    obsTable.write('\\begin{center} \\begin{tabular}{cc}')
    obsTable.write('\n')
    obsTable.write('\hline \hline')
    obsTable.write('\n')
    obsTable.write('$\\tau$ (ns) & Obs. Excluded Mass (\gev) \\\\')
    obsTable.write('\hline')
    obsTable.write('\n')
    obsTable.close()
    
    for limit in limits:
        mass = float (limit['mass'])
        lifetime = float (limit['lifetime'])
        if lifetime not in limit_dict:
            limit_dict[lifetime] = {}
        if mass not in limit_dict[lifetime]:
            limit_dict[lifetime][mass] = {}
        limit_dict[lifetime][mass]['experiment'] = limit[experiment_key]
        if experiment_key is 'up1' or experiment_key is 'up2':
            limit_dict[lifetime][mass]['experiment'] += limit['expected']
        if experiment_key is 'down1' or experiment_key is 'down2':
            limit_dict[lifetime][mass]['experiment'] = limit['expected'] - limit_dict[lifetime][mass]['experiment']
        for theory_mass in signal_cross_sections:
            if abs (float (theory_mass) - mass) < 1.0e-3:
                limit_dict[lifetime][mass]['theory'] = float (signal_cross_sections[theory_mass]['value'])
                theory_error = float (signal_cross_sections[theory_mass]['error'])
                if theory_key is 'up2' or theory_key is 'down2':
                    theory_error = 1.0 + 2.0 * (theory_error - 1.0)
                if theory_key is 'up1' or theory_key is 'up2':
                    limit_dict[lifetime][mass]['theory'] *= theory_error
                if theory_key is 'down1' or theory_key is 'down2':
                    limit_dict[lifetime][mass]['theory'] *= (2.0 - theory_error)
    for lifetime in sorted (limit_dict.keys ()):
        ordered_masses = sorted (limit_dict[lifetime].keys ())
        first_allowed_mass = ordered_masses[0]
        previous_mass = ordered_masses[0]
        for mass in ordered_masses:
            if limit_dict[lifetime][mass]['theory'] < limit_dict[lifetime][mass]['experiment']:
                first_allowed_mass = mass
                break
            previous_mass = mass
        mass_limit = 0.0
        if previous_mass != first_allowed_mass:
            # find intersection using http://en.wikipedia.org/wiki/Line-line_intersection
            x1 = previous_mass
            x3 = previous_mass
            x2 = first_allowed_mass
            x4 = first_allowed_mass
            y1 = limit_dict[lifetime][previous_mass]['theory']
            y3 = limit_dict[lifetime][previous_mass]['experiment']
            y2 = limit_dict[lifetime][first_allowed_mass]['theory']
            y4 = limit_dict[lifetime][first_allowed_mass]['experiment']
            mass_limit = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
            mass_limit /= (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if math.isnan (mass_limit):
                mass_limit = 0.0
            x.append (mass_limit)
            y.append (lifetime)
            
            with open ("limits/" + limit_dir + "/" + "obsTable.tex", 'a') as file:
                file.write(str(lifetime) + ' & ' + str(round(mass_limit,1)) + '\\\\')
                file.write('\n')
            obsTable.close()
            
            if x_key is 'lifetime' and y_key is 'mass':
                x[-1], y[-1] = y[-1], x[-1]
    graph = TGraph (len (x), x, y)
        
    obsTable = open("limits/" + limit_dir + "/" + "obsTable.tex", "a")
    obsTable.write('\hline \hline')
    obsTable.write('\n')
    obsTable.write(' \end{tabular} \end{center}')
    obsTable.close()
    print "Table of observed limits for AN stored in: limits/" + limit_dir
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
        if not limit.has_key(x_key) or not limit.has_key(up_key) or not limit.has_key(down_key) or not limit.has_key(y_key):
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
        if errorType is 'horizontal':
            eHigh = graph.GetErrorXhigh (i)
            eLow = graph.GetErrorXlow (i)
            otherSideX.append (xPoint - eLow)
            otherSideY.append (yPoint)
            x.append (xPoint + eHigh)
            y.append (yPoint)
        if errorType is 'vertical':
            eHigh = graph.GetErrorYhigh (i)
            eLow = graph.GetErrorYlow (i)
            otherSideX.append (xPoint)
            otherSideY.append (yPoint - eLow)
            x.append (xPoint)
            y.append (yPoint + eHigh)
    for i in range (0, -N, -1):
        x.append (otherSideX[i - 1])
        y.append (otherSideY[i - 1])
    borderGraph = TGraph (len (x), x, y)
    return borderGraph

def getGraphAsymmErrors2D(limits, x_key, y_key, experiment_key, up_key, down_key):
    central = getGraph2D (limits, x_key, y_key, experiment_key, 'theory')
    up = TGraph ()
    down = TGraph ()
    if experiment_key is 'expected':
        up = getGraph2D (limits, x_key, y_key, down_key, 'theory')
        down = getGraph2D (limits, x_key, y_key, up_key, 'theory')
    if experiment_key is 'observed':
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
            print "Debug:  appending point: (" + str(xPoint) + ", " + str(yPoint) 
        if y_key is 'lifetime':
            eXHigh.append (upXPoint)
            eXLow.append (downXPoint)
            eYHigh.append (0.0)
            eYLow.append (0.0)
        if x_key is 'lifetime':
            eXHigh.append (0.0)
            eXLow.append (0.0)
            eYHigh.append (upYPoint)
            eYLow.append (downYPoint)
    for i in range (0, len (x)):
        if y_key is 'lifetime':
            eXHigh[i] -= x[i]
            eXLow[i] = x[i] - eXLow[i]
        if x_key is 'lifetime':
            eYHigh[i] -= y[i]
            eYLow[i] = y[i] - eYLow[i]
    graph = TGraphAsymmErrors (len (x),
                               array ('d', x),
                               array ('d', y),
                               array ('d', eXLow),
                               array ('d', eXHigh),
                               array ('d', eYLow),
                               array ('d', eYHigh))
    borderGraph = TGraphAsymmErrors ()
    if y_key is 'lifetime':
        borderGraph = getBorderGraph (graph, 'horizontal')
    if x_key is 'lifetime':
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
#def fetchLimits(chMass,lifetime,directories):

    limit = { }
    limit['expected'] = 1.0e12

    if arguments.verbose:
        print "Debug:  running fetchLimits for mass = " + str(mass) + "; lifetime = " + str(lifetime) + "; directories = " + str(directories) 
    for directory in directories:
        if not os.path.exists(os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/test/limits/"+directory+"/method.txt"):
            return -1
        with open(os.environ["CMSSW_BASE"]+"/src/DisappTrks/StandardAnalysis/test/limits/"+directory+"/method.txt", 'r') as methodFile:
            method = methodFile.readline()

        #########################################################

        tmp_limit = { }
        # for Asymptotic CLs, get the limits from the root file
        if method == "Asymptotic":
            file = TFile(makeSignalRootFileName(mass,lifetime,directory,"expected"))
#       file = TFile(makeSignalRootFileName(chiMasses[mass]['value'],lifetime,directory,"expected"))
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
                return -1
            limit_tree = file.Get('limit')
            if not limit_tree:
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

        # for other methods, get the ranges from the log file
        else:
            file = open(makeSignalLogFileName(mass,lifetime,directory,"expected"))
#            print "Debug:  opening file: "
#            print makeSignalLogFileName(mass,lifetime,directory,"expected")  
            for line in file:
#                print "Debug: line = " + line  
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
#            print "Debug:  finished expected"  

            file = open(makeSignalLogFileName(mass,lifetime,directory,"observed"))
#            print "Debug:  opening observed file: "
#            print makeSignalLogFileName(mass,lifetime,directory,"observed")  
            for line in file:
                line = line.rstrip("\n").split(":")
                if line[0] =="Limit": #observed limit
                    tmp_limit['observed'] = float(line[1].split(" ")[3])
            file.close()
                    
        tmp_limit['up2'] = math.fabs(tmp_limit['up2'] - tmp_limit['expected'])
        tmp_limit['up1'] = math.fabs(tmp_limit['up1'] - tmp_limit['expected'])
        tmp_limit['down2'] = math.fabs(tmp_limit['down2'] - tmp_limit['expected'])
        tmp_limit['down1'] = math.fabs(tmp_limit['down1'] - tmp_limit['expected'])

        xSection = float(signal_cross_sections[str(mass)]['value'])
#        xSection = float(signal_cross_sections[str(chMass)]['value'])
        tmp_limit['up2'] *= xSection
        tmp_limit['up1'] *= xSection
        tmp_limit['observed'] *= xSection
        tmp_limit['expected'] *= xSection
        tmp_limit['down1'] *= xSection
        tmp_limit['down2'] *= xSection

        tmp_limit['mass'] = mass
        tmp_limit['lifetime'] = lifetime
        if convertCmToNs:
            speedLightCmPerNs = 29.979  # speed of light in cm / ns
            tmp_limit['lifetime'] = float(lifetime) / speedLightCmPerNs  
##         if convertToMassSplitting:
##             speedLightCmPerNs = 29.979  
##             muMass = 0.1056
##             massSplitToTheFifth = (8 * 10E-8) / (float(lifetime) * 10E-9) * math.pow(float(muMass) ,5)
##             massSplit = 1000 * (math.pow(massSplitToTheFifth, Fraction(1,5)) )
##             tmp_limit['lifetime'] = massSplit
##             print massSplit
        if tmp_limit['expected'] < limit['expected']:
            limit = tmp_limit
    return (limit if limit['expected'] < 9.9e11 else -1)


def drawPlot(plot):
    is2D = 'yAxisType' in plot
    isMakeTable = False
    outputFile.cd()
    canvas = TCanvas(plot['title'])
    xAxisMin = 1
    yAxisMin = 1
    xAxisMax = 2
    yAxisMax = 2
    xAxisBins = array('d')
    yAxisBins = array('d')
    nBinsX = 1
    nBinsY = 1
    if plot['xAxisType'] is 'mass':
        xAxisMin = float(masses[0])
        xAxisMax = float(masses[-1])
    elif plot['xAxisType'] is 'lifetime':
        # convert lifetime to cm
#        xAxisMin = 0.1*float(lifetimes[0])
        xAxisMin = float(lifetimes[0])
#        xAxisMax = 0.1*float(lifetimes[-1])
        xAxisMax = float(lifetimes[-1])
    if is2D:
        canvas.SetLogz()
        if plot['yAxisType'] is 'mass':
            yAxisMin = float(masses[0])
            yAxisMax = float(masses[-1])
            #xAxisBins.extend ([0.1 * float (lifetime) for lifetime in lifetimes])
            xAxisBins.extend ([float (lifetime) for lifetime in lifetimes])
            #xAxisBins.append (0.1 * 2.0 * float (lifetimes[-1]))
            xAxisBins.append (2.0 * float (lifetimes[-1]))
            yAxisBins.extend ([float (mass) for mass in masses])
            yAxisBins.append (2.0 * float (masses[-1]) - float (masses[-2]))
            yAxisBins.append (8.0 * float (masses[-1]) - 4.0 * float (masses[-2]))
        elif plot['yAxisType'] is 'lifetime':
            #yAxisMin = 0.1*float(lifetimes[0])
            yAxisMin = float(lifetimes[0])
            #yAxisMax = 0.1*float(lifetimes[-1])
            #yAxisMax = float(lifetimes[-1])
            yAxisMax = 2 * float(lifetimes[-1])
            if not convertToMassSplitting:
                canvas.SetLogy()
            xAxisBins.extend ([float (mass) for mass in masses])
            xAxisBins.append (2.0 * float (masses[-1]) - float (masses[-2]))
            #yAxisBins.extend ([0.1 * float (lifetime) for lifetime in lifetimes])
            yAxisBins.extend ([float (lifetime) for lifetime in lifetimes])
            #yAxisBins.append (0.1 * 2.0 * float (lifetimes[-1]))
            yAxisBins.append (2.0 * float (lifetimes[-1]))
            #yAxisBins.append (0.1 * 8.0 * float (lifetimes[-1]))
            yAxisBins.append (8.0 * float (lifetimes[-1]))
        nBinsX = len (xAxisBins) - 1
        nBinsY = len (yAxisBins) - 1
    else:
        canvas.SetLogy()

#    legend = TLegend(0.5, 0.6, 0.9, 0.88) # old
    legend = TLegend(0.1895973,0.3548951,0.5889262,0.6346154)  
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetTextFont(42)  

    #construct tGraph objects for all curves and draw them
    tGraphs = []
    plotDrawn = False
    if (not is2D) and ('showTheory' in plot and plot['showTheory']) and ('showTheoryError' in plot and plot['showTheoryError']):
        if plot['xAxisType'] is 'mass':
            tGraphs.append(getTheoryOneSigmaGraph())
            if plotDrawn:
                tGraphs[-1].Draw('3')
            else:
                tGraphs[-1].Draw('A3')
            plotDrawn = True
            legend.AddEntry(tGraphs[-1], "#pm 1 #sigma: theory", 'F')
            tGraphs.append(getTheoryGraph())
            if plotDrawn:
                tGraphs[-1].Draw('L')
            else:
                tGraphs[-1].Draw('AL')
            plotDrawn = True
            legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')
    for graph in plot['graphs']:
        colorScheme = 'brazilian'
        if 'colorScheme' in graph:
            colorScheme = graph['colorScheme']
        if not is2D:
            for graphName in graph['graphsToInclude']:
                if graphName is 'twoSigma':
                    tGraphs.append(getTwoSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
                    if plotDrawn:
                        tGraphs[-1].Draw('3')
                    else:
                        tGraphs[-1].Draw('A3')
                    plotDrawn = True
                    legendEntry = '#pm 2 #sigma'
                    if graphName is 'legendEntry':
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                if graphName is 'oneSigma':
                    tGraphs.append(getOneSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
                    if plotDrawn:
                        tGraphs[-1].Draw('3')
                    else:
                        tGraphs[-1].Draw('A3')
                    plotDrawn = True
                    legendEntry = '#pm 1 #sigma'
                    if graphName is 'legendEntry':
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                if graphName is 'exp':
                    tGraphs.append(getExpectedGraph(graph['limits'],plot['xAxisType'],colorScheme))
                    if plotDrawn:
                        tGraphs[-1].Draw('L')
                    else:
                        tGraphs[-1].Draw('AL')
                    plotDrawn = True
                    legendEntry = 'exp. limit'
                    if graphName is 'legendEntry':
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                if graphName is 'obs':
                    tGraphs.append(getObservedGraph(graph['limits'],plot['xAxisType'],colorScheme))
                    if plotDrawn:
                        tGraphs[-1].Draw('L')
                    else:
                        tGraphs[-1].Draw('AL')
                    plotDrawn = True
                    legendEntry = 'obs. limit'
                    if graphName is 'legendEntry':
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'L')
        else:
            for graphName in graph['graphsToInclude']:
                if graphName is 'twoSigma':
                    tGraphs.append(getTwoSigmaGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],colorScheme))
                    if plotDrawn:
                        if 'legendEntry' in graph:  # make transparent if graphs from two sources are being compared
                            tGraphs[-1].SetFillStyle(3001)
                        tGraphs[-1].Draw('F')
                    else:
                        tGraphs[-1].Draw('AF')
                    plotDrawn = True
                    legendEntry = 'expected limit #pm2 #sigma'
                    if 'legendEntry' in graph:
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                if graphName is 'oneSigma':
                    tGraphs.append(getOneSigmaGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],colorScheme))
                    if plotDrawn:
                        if 'legendEntry' in graph:  # make transparent if graphs from two sources are being compared
                            tGraphs[-1].SetFillStyle(3001)
                        tGraphs[-1].Draw('F')
                    else:
                        tGraphs[-1].Draw('AF')
                    plotDrawn = True
                    legendEntry = 'expected limit #pm1 #sigma'
                    if 'legendEntry' in graph:
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'F')
                if graphName is 'exp':
                    tGraphs.append(getExpectedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'expected','theory',colorScheme))
                    #makeExpLimitsTable(graph['limits'],plot['xAxisType'],plot['yAxisType'],'expected','theory',colorScheme)
                    makeExpLimitsTable(graph['limits'],plot['xAxisType'],plot['yAxisType'],'expected','theory')
                    
                    if plotDrawn:
                        tGraphs[-1].Draw('L')
                    else:
                        tGraphs[-1].Draw('AL')
                    plotDrawn = True
                    legendEntry = 'expected limit'
                    if 'legendEntry' in graph:
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                if graphName is 'twoSigmaTheory':
                    isMakeTable = True
                    tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','down2',colorScheme))
                    lineWidth = tGraphs[-1].GetLineWidth ()
                    tGraphs[-1].SetLineWidth (lineWidth - 4)
                    if plotDrawn:
                        tGraphs[-1].Draw('L')
                    else:
                        tGraphs[-1].Draw('AL')
                    plotDrawn = True
                    tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','up2',colorScheme))
                    tGraphs[-1].SetLineWidth (lineWidth - 4)
                    tGraphs[-1].Draw('L')
                    legendEntry = '#pm 2 #sigma_{theory}'
                    if 'legendEntry' in graph:
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                if graphName is 'oneSigmaTheory':
                    tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','down1',colorScheme))
                    lineWidth = tGraphs[-1].GetLineWidth ()
                    tGraphs[-1].SetLineWidth (lineWidth - 2)
                    if plotDrawn:
                        tGraphs[-1].Draw('L')
                    else:
                        tGraphs[-1].Draw('AL')
                    plotDrawn = True
                    tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','up1',colorScheme))
                    tGraphs[-1].SetLineWidth (lineWidth - 2)
                    tGraphs[-1].Draw('L')
                    legendEntry = '#pm 1 #sigma_{theory}'
                    if 'legendEntry' in graph:
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'L')
                if graphName is 'obs':
                    tGraphs.append(getObservedGraph2D(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','theory',colorScheme))
                    makeObsLimitsTable(graph['limits'],plot['xAxisType'],plot['yAxisType'],'observed','theory')
                    if plotDrawn:
                        tGraphs[-1].Draw('L')
                    else:
                        tGraphs[-1].Draw('AL')
                    plotDrawn = True
                    legendEntry = 'observed limit'
                    if 'legendEntry' in graph:
                        legendEntry = legendEntry + ": " + graph['legendEntry']
                    legend.AddEntry(tGraphs[-1], legendEntry, 'L')
    if (not is2D) and ('showTheory' in plot and plot['showTheory']) and ('showTheoryError' not in plot or not plot['showTheoryError']):
        if plot['xAxisType'] is 'mass':
            tGraphs.append(getTheoryGraph())
            if plotDrawn:
                tGraphs[-1].Draw('L')
            else:
                tGraphs[-1].Draw('AL')
            plotDrawn = True
            legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')
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

    for tGraph in tGraphs:
        tGraph.SetTitle("")
        tGraph.GetXaxis().SetTitle(plot['xAxisLabel'])
        if 'xAxisFixMin' in plot:  
            tGraph.GetXaxis().SetLimits   (plot['xAxisFixMin'],plot['xAxisFixMax'])  
            tGraph.GetXaxis().SetRangeUser(plot['xAxisFixMin'],plot['xAxisFixMax'])    
        else:
            tGraph.GetXaxis().SetLimits(0.9*xAxisMin,1.1*xAxisMax)
            tGraph.GetXaxis().SetRangeUser(xAxisMin,xAxisMax)
        if not is2D:
            #tGraph.GetYaxis().SetTitle('#sigma_{95%CL} [pb]')
            tGraph.GetYaxis().SetTitle('#sigma (pp#rightarrow #chi#chi) [pb]')
            if 'yAxis' in plot:
                tGraph.GetYaxis().SetRangeUser(plot['yAxis'][0],plot['yAxis'][1])
            else:
                tGraph.GetYaxis().SetRangeUser(0.9*absMin,1.1*absMax)
        else:
            tGraph.GetYaxis().SetTitle(plot['yAxisLabel'])
            if 'yAxisFixMin' in plot:  
                tGraph.GetYaxis().SetLimits   (plot['yAxisFixMin'],plot['yAxisFixMax'])  
                tGraph.GetYaxis().SetRangeUser(plot['yAxisFixMin'],plot['yAxisFixMax'])    
            else:
                tGraph.GetYaxis().SetLimits(0.9*yAxisMin,1.1*yAxisMax)
                tGraph.GetYaxis().SetRangeUser(yAxisMin,yAxisMax)

    if not drawTheoryCurve: 
        legend.Draw()
    canvas.SetTitle('')
    #draw the header label
#    HeaderLabel = TPaveLabel(0.1652299,0.9110169,0.9037356,0.9576271,HeaderText,"NDC")
    HeaderLabel = TPaveLabel(0.08892617, 0.9458042, 0.9681208, 0.9965035,HeaderText,"NDC") # from makePlots.py  
    HeaderLabel.SetTextAlign(32)
    HeaderLabel.SetBorderSize(0)
    HeaderLabel.SetFillColor(0)
    HeaderLabel.SetFillStyle(0)
    HeaderLabel.Draw()

    if 'theoryLabel' in plot: 
#        TheoryLabel = TPaveLabel(0.1637931,0.8220339,0.362069,0.8919492,plot['theoryLabel'],"NDC") # old
        TheoryLabel = TPaveLabel(0.5218121,0.8339161,0.9362416,0.9038462,plot['theoryLabel'],"NDC")
        TheoryLabel.SetTextAlign(32)
        TheoryLabel.SetBorderSize(0)
        TheoryLabel.SetFillColor(0)
        TheoryLabel.SetFillStyle(0)
        TheoryLabel.Draw()

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


    canvas.Update()
 
    canvas.RedrawAxis('g')

    if drawTheoryCurve:
        function = TF1("function","-413.315+305.383*log(x) - 60.8831*log(x)^2 + 5.41948 * log(x)^3 - 0.181509*log(x)^4",100,600)
        function.SetLineStyle(2)
        function.Draw("same")
        legend.AddEntry(function, "Theory (Phys. Lett. B721 252 (2013))" ,"L")
        legend.Draw("same")
        
    canvas.Write()
    canvas.SaveAs("limits/"+arguments.outputDir+"/"+plot['title']+".pdf")
 



######################################################################################################


outputFileName = "limits/"+arguments.outputDir+"/limit_plot.root"
outputFile = TFile(outputFileName, "RECREATE")

# for each plot that has been defined, extract the limits and draw the plot accordingly
for plot in plotDefinitions:

    #fetch all the limits needed for this plot

    for graph in plot['graphs']:
        graph['limits'] = []
        if plot['xAxisType'] is 'lifetime' and 'yAxisType' not in plot:
            for lifetime in lifetimes:
                lifetime = lifetime.replace(".0", "")
                lifetime = lifetime.replace("0.5", "0p5")
#                limit = fetchLimits(graph['mass'],lifetime,graph['br'],graph['source'])
                limit = fetchLimits(graph['mass'],lifetime,graph['source'])
                if limit is not -1:
                    graph['limits'].append(limit)
                else:
                    print "WARNING: not plotting lifetime " + str (lifetime) + " mm"
        elif plot['xAxisType'] is 'mass' and 'yAxisType' not in plot:
            for mass in masses:
                for lifetime in lifetimes:
                    lifetime = lifetime.replace(".0", "")
                    lifetime = lifetime.replace("0.5", "0p5")    
#                limit = fetchLimits(mass,graph['lifetime'],graph['br'],graph['source'])
                limit = fetchLimits(mass,graph['lifetime'],graph['source'])
                if arguments.verbose:
                    print "Debug:  limit = " + str(limit) + " for mass " + str(mass) + ", limit['expected'] = " + limit['expected'] 
                if limit is not -1:
                    graph['limits'].append(limit)
                else:
                    print "WARNING: for xAxisType=mass, not plotting mass: " + str (mass) + " GeV, lifetime: " + str (lifetime) + ", source: " + graph['source']  
        elif 'yAxisType' in plot:
            for mass in masses:
                for lifetime in lifetimes:
#                    limit = fetchLimits(mass,lifetime,graph['br'],graph['source'])
                    limit = fetchLimits(mass,lifetime,graph['source'])
                    if limit is not -1:
                        graph['limits'].append(limit)
                        if arguments.verbose:
                            print "Debug:  limit for mass " + str(mass) + ", lifetime = " + str(lifetime) + ", limit['expected'] = " + str(limit['expected']) + ", limit['observed'] = " + str(limit['observed'])
                    else:
                        print "WARNING: not plotting mass " + str (mass) + " GeV, lifetime " + str (lifetime) + " mm"
    #now that all the limits are in place, draw the plot
    drawPlot(plot)


outputFile.Close()
