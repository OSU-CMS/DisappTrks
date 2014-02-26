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
from operator import itemgetter
from optparse import OptionParser



parser = OptionParser()
parser.add_option("-l", "--localConfig", dest="localConfig",
                  help="local configuration file")
parser.add_option("-c", "--outputDir", dest="outputDir",
                  help="output directory")

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


from ROOT import TFile, TGraph, TGraphAsymmErrors, gROOT, gStyle, TStyle, TH1F, TCanvas, TString, TLegend, TArrow, THStack, TPaveLabel

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetOptTitle(0)
gROOT.ForceStyle()

colorSchemes = {
    'brazilian' : {
        'obs' : 1,
        'exp' : 1,
        'oneSigma' : 78, #410,
        'twoSigma' : 88, #393,
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
    LumiText = "L_{int} = " + str(intLumi) + " pb^{-1}"
    LumiText = "L_{int} = " + str.format('{0:.1f}', LumiInPb) + " pb^{-1}"
else:
    LumiInFb = intLumi/1000.
    LumiText = "L_{int} = " + str.format('{0:.1f}', LumiInFb) + " fb^{-1}"

#set the text for the fancy heading
HeaderText = "CMS Preliminary: " + LumiText + " at #sqrt{s} = 8 TeV"



def makeSignalName(mass,lifetime):
    lifetime = str(lifetime).replace(".0", "")
    lifetime = str(lifetime).replace("0.5", "0p5")
    return "AMSB_mChi"+str(mass)+"_"+str(lifetime)+"ns"

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
    graph.SetLineWidth(4)
    graph.SetLineStyle(3)
    graph.SetFillColor(0)
    #graph.SetLineColor(1)
    graph.SetLineColor(2)
    graph.SetMarkerSize(0.8)
    #graph.SetMarkerColor(1)
    graph.SetMarkerColor(2)
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

def getObservedGraph(limits,xAxisType,colorScheme):
    graph = getGraph(limits, xAxisType, 'observed')
    graph.SetLineWidth(4)
    graph.SetLineStyle(1)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['obs'])
    graph.SetMarkerStyle(21)
    graph.SetMarkerSize(1)
    graph.SetMarkerColor(colorSchemes[colorScheme]['obs'])
    return graph

def getExpectedGraph(limits,xAxisType,colorScheme):
    graph = getGraph(limits, xAxisType, 'expected')
    graph.SetLineWidth(4)
    graph.SetLineStyle(2)
    graph.SetFillColor(0)
    graph.SetLineColor(colorSchemes[colorScheme]['exp'])
    graph.SetMarkerStyle(20)
    graph.SetMarkerSize(0.8)
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
    
def getOneSigmaGraph(limits,xAxisType,colorScheme):
    graph = getGraphAsymmErrors(limits, xAxisType, 'expected', 'up1', 'down1')
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


def fetchLimits(mass,lifetime,directories):
#def fetchLimits(chMass,lifetime,directories):

    limit = { }
    limit['expected'] = 1.0e6

    for directory in directories:
#        with open(os.environ["CMSSW_BASE"]+"/src/DisplacedSUSY/LimitsCalculation/test/limits/"+directory+"/method.txt", 'r') as methodFile:
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
            for line in file:
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

        file = open(makeSignalLogFileName(mass,lifetime,directory,"observed"))
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
        # convert lifetime to cm
        tmp_limit['lifetime'] = 0.1 * float(lifetime)
#        tmp_limit['branching_ratio'] = branching_ratio

        if tmp_limit['expected'] < limit['expected']:
            limit = tmp_limit

        #print limit
        #print

    return (limit if limit['expected'] < 9.9e5 else -1)
        

def drawPlot(plot):
    outputFile.cd()
    canvas = TCanvas(plot['title'])
#    canvas.SetGridx()
#    canvas.SetGridy()
    xAxisMin = 1
    xAxisMax = 2
    if plot['xAxisType'] is 'mass':
        canvas.SetLogy()
        xAxisMin = float(masses[0])
       # xAxisMin = float(chMasses[0])
       # xAxisMax = float(chMasses[-1])
        xAxisMax = float(masses[-1])
    elif plot['xAxisType'] is 'lifetime':
        canvas.SetLogy()
        canvas.SetLogx()
        # convert lifetime to cm
        xAxisMin = 0.1*float(lifetimes[0])
        xAxisMax = 0.1*float(lifetimes[-1])

    legend = TLegend(0.5, 0.6, 0.9, 0.88)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)

    #construct tGraph objects for all curves and draw them
    tGraphs = []
    plotDrawn = False
    for graph in plot['graphs']:
        colorScheme = 'brazilian'
        if 'colorScheme' in graph:
            colorScheme = graph['colorScheme']
        if 'twoSigma' in graph['graphsToInclude']:
            tGraphs.append(getTwoSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
            if plotDrawn:
                tGraphs[-1].Draw('3')
            else:
                tGraphs[-1].Draw('A3')
            plotDrawn = True
            legendEntry = '#pm 2 #sigma'
            if 'legendEntry' in graph:
                legendEntry = legendEntry + ": " + graph['legendEntry']
            legend.AddEntry(tGraphs[-1], legendEntry, 'F')
        if 'oneSigma' in graph['graphsToInclude']:
            tGraphs.append(getOneSigmaGraph(graph['limits'],plot['xAxisType'],colorScheme))
            if plotDrawn:
                tGraphs[-1].Draw('3')
            else:
                tGraphs[-1].Draw('A3')
            plotDrawn = True

            legendEntry = '#pm 1 #sigma'
            if 'legendEntry' in graph:
                legendEntry = legendEntry + ": " + graph['legendEntry']
            legend.AddEntry(tGraphs[-1], legendEntry, 'F')
        if 'exp' in graph['graphsToInclude']:
            tGraphs.append(getExpectedGraph(graph['limits'],plot['xAxisType'],colorScheme))
            if plotDrawn:
                tGraphs[-1].Draw('LP')
            else:
                tGraphs[-1].Draw('ALP')
            plotDrawn = True

            legendEntry = 'exp. limit'
            if 'legendEntry' in graph:
                legendEntry = legendEntry + ": " + graph['legendEntry']
            legend.AddEntry(tGraphs[-1], legendEntry, 'L')
        if 'obs' in graph['graphsToInclude']:
            tGraphs.append(getObservedGraph(graph['limits'],plot['xAxisType'],colorScheme))
            if plotDrawn:
                tGraphs[-1].Draw('LP')
            else:
                tGraphs[-1].Draw('ALP')
            plotDrawn = True

            legendEntry = 'obs. limit'
            if 'legendEntry' in graph:
                legendEntry = legendEntry + ": " + graph['legendEntry']
            legend.AddEntry(tGraphs[-1], legendEntry, 'L')

    if 'showTheory' in plot:
        if 'showTheory':
            if plot['xAxisType'] is 'mass':
                tGraphs.append(getTheoryGraph())
                if plotDrawn:
                    tGraphs[-1].Draw('LP')
                else:
                    tGraphs[-1].Draw('ALP')

                legend.AddEntry(tGraphs[-1], 'theory prediction', 'L')


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

    #now set the axis limits
    for tGraph in tGraphs:
        tGraph.SetTitle("")
        tGraph.GetXaxis().SetTitle(plot['xAxisLabel'])
        tGraph.GetXaxis().SetRangeUser(xAxisMin,xAxisMax)
        tGraph.GetYaxis().SetTitle('#sigma(pp #rightarrow #chi #chi) [pb], #tau = ' + plot['yAxisLabel'])
        if 'yAxis' in plot:
            tGraph.GetYaxis().SetRangeUser(plot['yAxis'][0],plot['yAxis'][1])
        else:
            tGraph.GetYaxis().SetRangeUser(0.9*absMin,1.1*absMax)

        
    legend.Draw()
    canvas.SetTitle('')

    #draw the header label
    HeaderLabel = TPaveLabel(0.1652299,0.9110169,0.9037356,0.9576271,HeaderText,"NDC")
    HeaderLabel.SetTextAlign(32)
    HeaderLabel.SetBorderSize(0)
    HeaderLabel.SetFillColor(0)
    HeaderLabel.SetFillStyle(0)
    HeaderLabel.Draw()

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
    canvas.Write()
#    canvas.SaveAs("test.pdf")




######################################################################################################


outputFileName = "limits/"+arguments.outputDir+"/limit_plot.root"
outputFile = TFile(outputFileName, "RECREATE")

# for each plot that has been defined, extract the limits and draw the plot accordingly
for plot in plotDefinitions:

    #fetch all the limits needed for this plot

    for graph in plot['graphs']:
        graph['limits'] = []
        if plot['xAxisType'] is 'lifetime':
            for lifetime in lifetimes:
                lifetime = lifetime.replace(".0", "")
                lifetime = lifetime.replace("0.5", "0p5")
#                limit = fetchLimits(graph['mass'],lifetime,graph['br'],graph['source'])
                limit = fetchLimits(graph['mass'],lifetime,graph['source'])
                if limit is not -1:
                    graph['limits'].append(limit)
                else:
                    print "WARNING: not plotting lifetime " + str (lifetime) + " mm"
        elif plot['xAxisType'] is 'mass':
            for mass in masses:
#            for chMass in chMasses:
                for lifetime in lifetimes:
                    lifetime = lifetime.replace(".0", "")
                    lifetime = lifetime.replace("0.5", "0p5")    
#                limit = fetchLimits(mass,graph['lifetime'],graph['br'],graph['source'])
                limit = fetchLimits(mass,graph['lifetime'],graph['source'])
                if limit is not -1:
                    graph['limits'].append(limit)
                else:
                    print "WARNING: not plotting mass " + str (mass) + " GeV"

    #now that all the limits are in place, draw the plot
    drawPlot(plot)


outputFile.Close()
