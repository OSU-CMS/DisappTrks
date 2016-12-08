#!/usr/bin/env python

# Creates plots of signal efficiency

# Much of code taken from https://github.com/OSU-CMS/OSUT3Analysis/blob/master/Configuration/scripts/makeEfficiencyPlots.py

import sys
import os
from array import *

from optparse import OptionParser
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *

parser = OptionParser()
parser = set_commandline_arguments(parser)

parser.add_option("-x", "--xsec", dest="xsecFile",
                  help="Use as denominator of efficiency the lumi * cross section")

(arguments, args) = parser.parse_args()
if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.localConfig) + " import *")

if arguments.xsecFile:
    sys.path.append(os.getcwd())
    exec("from " + re.sub (r".py$", r"", arguments.xsecFile) + " import *")

intLumi = 19500.  # integrated lumi in /pb

from ROOT import TFile, gROOT, gStyle, gDirectory, TStyle, TH1F, TCanvas, TString, TLegend, TLegendEntry, TIter, TKey, TPaveLabel, gPad, TGraphAsymmErrors


gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetCanvasBorderMode(0)
gStyle.SetPadBorderMode(0)
gStyle.SetPadColor(0)
gStyle.SetCanvasColor(0)
gStyle.SetTextFont(42)
gStyle.SetCanvasDefH(600)
gStyle.SetCanvasDefW(600)
gStyle.SetCanvasDefX(0)
gStyle.SetCanvasDefY(0)
gStyle.SetPadTopMargin(0.07)
gStyle.SetPadBottomMargin(0.13)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetTitleColor(1, "XYZ")
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.04, "XYZ")
gStyle.SetTitleXOffset(1.1)
gStyle.SetTitleYOffset(2)
gStyle.SetTextAlign(12)
gStyle.SetLabelColor(1, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelOffset(0.007, "XYZ")
gStyle.SetLabelSize(0.04, "XYZ")
gStyle.SetAxisColor(1, "XYZ")
gStyle.SetStripDecimals(True)
gStyle.SetTickLength(0.03, "XYZ")
gStyle.SetNdivisions(510, "XYZ")
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gROOT.ForceStyle()



colors = {
    'black' : 1,
#    'red' : 623,
    'red' : 632,
    'green' : 407,
    'purple' : 871,
#    'blue' : 591,
    'blue' : 600,
    'yellow' : 393,
    }
colorList = [
    'black',
    'red',
    'green',
    'purple',
    'blue',
    'yellow',
    ]
markers = {
    'circle' : 20,
#    'circle' : 4,
    'square' : 21,
    'triangle' : 22,
    'star' : 3,
    'circSmall' : 4,
    }
fills = {
    'solid' : 0,
    'hollow' : 4,
    }



def MakeOneHist(varXaxis, varConst, xvalues, constval):

    if len(xvalues)<=1:
        return # Do not make plot if there is only 1 xvalue
    Legend = TLegend()
    Legend.SetBorderSize(0)
    Legend.SetFillColor(0)
    Legend.SetFillStyle(0)
    Canvas = TCanvas("sigEff_"+varConst+str(constval)+"_vs_"+varXaxis)
    Histograms = []
    LegendEntries = []
    colorIndex = 0
    for source in input_sources: # loop over different input sources in config file
#        print "Debug:  running over input_source from: ", source['condor_dir'], " for varXaxis=", varXaxis, ", varConst=", varConst

        # Create histogram of efficiencies with appropriate binning
        xAxisBins = array('d')
        xBinWidth = xvalues[1] - xvalues[0]
        for xval in xvalues:
            xAxisBins.append(xval - xBinWidth/2.0)
        xAxisBins.append(xvalues[-1] + xBinWidth/2.0)   # add an extra bin boundary for the last bin.

        Histogram = TH1F("Histogram", ";x title;signal efficiency", len(xvalues), xAxisBins)
        Histogram.SetDirectory(0)

        # Now fill the histogram of efficiencies:
        for xval in xvalues:
            if   varXaxis=="mass" and varConst=="lifetime":
                mass = xval
                lifetime = constval
            elif varXaxis=="lifetime" and varConst=="mass":
                lifetime = xval
                mass = constval
            else:
                print "Unrecognized value of varXaxis=", varXaxis
                return
            dataset_file = "condor/%s/%s.root" % (source['condor_dir'],dataset)
            dataset_file = dataset_file.replace("MASS",     str(mass))
            dataset_file = dataset_file.replace("LIFETIME", str(lifetime))
            inputFile = TFile(dataset_file)
            HistCutflow = inputFile.Get("OSUAnalysis/" + source['channel'] + "CutFlow")
            if not HistCutflow:
                print "WARNING: Could not find histogram OSUAnalysis/" + source['channel'] + "CutFlow in file " + dataset_file + ". Will skip it and continue."
                return

            # calculate efficiency
            nbinsCutflow = HistCutflow.GetNbinsX()
            if arguments.xsecFile:
                xsec = float(signal_cross_sections[str(mass)]['value'])
                denom = xsec * intLumi
            else:
                denom = HistCutflow.GetBinContent(1)  # denominator is the first entry in the cutflow histogram
            eff    = HistCutflow.GetBinContent(nbinsCutflow) / denom
            effErr = HistCutflow.GetBinError  (nbinsCutflow) / denom
            ibin = Histogram.FindBin(xval)
            Histogram.SetBinContent(ibin, eff)
            Histogram.SetBinError  (ibin, effErr)
            print "Setting bin content for varConst = ", varConst, " = ", constval, " in ibin=", ibin, ", xval=", xval, ", eff=", eff, " +- ", effErr, ", fractional error =", effErr/eff, " numerator = ", HistCutflow.GetBinContent(nbinsCutflow), " denom = ", denom, " from file: ", dataset_file
            inputFile.Close()

        if varXaxis=="mass":
            xAxisLabel = "chargino mass [GeV]"
        elif varXaxis=="lifetime":
            xAxisLabel = "chargino c#tau [cm]"
        else:
            print "Unrecognized value of varXaxis=", varXaxis
            return

        yAxisLabel = "efficiency"

        if 'color' in source:
            Histogram.SetMarkerColor(colors[source['color']])
            Histogram.SetLineColor(colors[source['color']])
        else:
            Histogram.SetMarkerColor(colors[colorList[colorIndex]])
            Histogram.SetLineColor(colors[colorList[colorIndex]])
            colorIndex = colorIndex + 1
            if colorIndex is len(colorList):
                colorIndex = 0
        markerStyle = 20
        if 'marker' in source:
            markerStyle = markers[source['marker']]
        if 'fill' in source:
            markerStyle = markerStyle + fills[source['fill']]
        Histogram.SetMarkerStyle(markerStyle)
        Histogram.SetMarkerSize(1)
#        Histogram.SetLineWidth(line_width)
        Histogram.SetFillStyle(0)
        LegendEntries.append(source['legend_entry'])
        Histograms.append(Histogram)

    # Finish loop over input_sources

    # formatting histograms and adding to legend
    legendIndex = 0
    for histogram in Histograms:
#        print "Adding entry to legend:  ", LegendEntries[legendIndex]
#        Legend.AddEntry(histogram,LegendEntries[legendIndex],"LEP")
        Legend.AddEntry(histogram,LegendEntries[legendIndex],"P")
        legendIndex = legendIndex+1

    # finding the maximum value of anything going on the canvas, so we know how to set the y-axis
    finalMax = 0
    for histogram in Histograms:
#        currentMax = histogram.GetMaximum() + histogram.GetBinError(histogram.GetMaximumBin())
        currentMax = histogram.GetMaximum()
        if(currentMax > finalMax):
            finalMax = currentMax
    finalMax = 1.5*finalMax
    if finalMax is 0:
        finalMax = 1
##         if arguments.setYMax:
##             finalMax = float(arguments.setYMax)

    # Drawing histograms to canvas
    makeRatioPlots = arguments.makeRatioPlots
    makeDiffPlots = arguments.makeDiffPlots
    yAxisMin = 0.0
##         if arguments.setYMin:
##             yAxisMin = float(arguments.setYMin)
    if makeRatioPlots or makeDiffPlots:
        Canvas.SetFillStyle(0)
        Canvas.Divide(1,2)
        Canvas.cd(1)
        gPad.SetPad(0,0.25,1,1)
        gPad.SetMargin(0.15,0.05,0.01,0.07)
        gPad.SetFillStyle(0)
        gPad.Update()
        gPad.Draw()
##             if arguments.setLogY:
##                 gPad.SetLogy()
        Canvas.cd(2)
        gPad.SetPad(0,0,1,0.25)
        #format: gPad.SetMargin(l,r,b,t)
        gPad.SetMargin(0.15,0.05,0.4,0.01)
        gPad.SetFillStyle(0)
        gPad.SetGridy(1)
        gPad.Update()
        gPad.Draw()
        Canvas.cd(1)

    histCounter = 0
    plotting_options = "pe, x0"   # x0 suppresses the error bar along x
##         if arguments.plot_hist:
##             plotting_options = "HIST"

    for histogram in Histograms:
        #            histogram.SetTitle(histoTitle)
        histogram.Draw(plotting_options)
        histogram.GetXaxis().SetTitle(xAxisLabel)
        histogram.GetYaxis().SetTitle(yAxisLabel)
        if histogram.InheritsFrom("TH1"):
            histogram.SetMaximum(finalMax)
            histogram.SetMinimum(yAxisMin)
        if makeRatioPlots or makeDiffPlots:
            histogram.GetXaxis().SetLabelSize(0)
        if histCounter is 0:
            if histogram.InheritsFrom("TH1"):
                plotting_options = plotting_options + " SAME"
            elif histogram.InheritsFrom("TGraph"):
                plotting_options = "P"
        histCounter = histCounter + 1

    x_left = 0.15
    x_right = 0.55
    y_min = 0.6
    y_max = 0.8
    Legend.SetX1NDC(x_left)
    Legend.SetY1NDC(y_min)
    Legend.SetX2NDC(x_right)
    Legend.SetY2NDC(y_max)
    Legend.Draw()

    customText = "chargino " + varConst + " " + str(constval)
    if varConst == "mass":
        customText += " GeV"
    elif varConst == "lifetime":
        customText += " cm"
    customText = customText.replace("lifetime", "c#tau")

    CustomLabel = TPaveLabel(x_left, 0.8, x_right, 0.9, customText, "NDC")
    CustomLabel.SetBorderSize(0)
    CustomLabel.SetFillColor(0)
    CustomLabel.SetFillStyle(0)
    CustomLabel.Draw()

    #drawing the ratio or difference plot if requested
    if makeRatioPlots or makeDiffPlots:
        Canvas.cd(2)
        if makeRatioPlots:
#            Comparison = ratioHistogram(Histograms[0],Histograms[1], 1000)
            Comparison = Histograms[0].Clone()
            Comparison.Divide(Histograms[1])
            Comparison.GetYaxis().SetTitle("ratio")
        elif makeDiffPlots:
            Comparison = Histograms[0].Clone("diff")
            Comparison.Add(Histograms[1],-1)
            Comparison.SetTitle("")
            Comparison.GetYaxis().SetTitle("hist1-hist2")
        Comparison.GetXaxis().SetTitle(xAxisLabel)
        Comparison.GetYaxis().CenterTitle()
        Comparison.GetYaxis().SetTitleSize(0.1)
        Comparison.GetYaxis().SetTitleOffset(0.5)
        Comparison.GetXaxis().SetTitleSize(0.15)
        Comparison.GetYaxis().SetLabelSize(0.1)
        Comparison.GetXaxis().SetLabelSize(0.15)
        if makeRatioPlots:
#            RatioYRange = 1.15
            if arguments.ratioYRange:
                RatioYRange = float(arguments.ratioYRange)
            Comparison.GetYaxis().SetRangeUser(0.7, 1.3)
        elif makeDiffPlots:
            YMax = Comparison.GetMaximum()
            YMin = Comparison.GetMinimum()
            if YMax <= 0 and YMin <= 0:
                Comparison.GetYaxis().SetRangeUser(-1.2*YMin,0)
            elif YMax >= 0 and YMin >= 0:
                Comparison.GetYaxis().SetRangeUser(0,1.2*YMax)
            else: #axis crosses y=0
                if abs(YMax) > abs(YMin):
                    Comparison.GetYaxis().SetRangeUser(-1.2*YMax,1.2*YMax)
                else:
                    Comparison.GetYaxis().SetRangeUser(-1.2*YMin,1.2*YMin)
        Comparison.GetYaxis().SetNdivisions(205)
#        Comparison.Draw("E0")
        Comparison.Draw("PE, X0")  # X0 suppresses error bar in x direction

    outputFile.cd()
    Canvas.Write()
    if arguments.savePDFs:
        Canvas.SaveAs("efficiency_histograms_pdfs/"+histogramName+".pdf")



# make output file
outputFileName = "sigEfficiency_histograms.root"
if arguments.outputFileName:
    outputFileName = arguments.outputFileName

outputFile = TFile(outputFileName, "RECREATE")
outputConfigFile = outputFileName.replace(".root", ".py")
if os.path.exists(outputConfigFile):
    os.system("mv " + outputConfigFile + " " + outputConfigFile.replace(".py", "-bkup.py")) # make a backup copy of a previous config file
os.system("cp " + arguments.localConfig + " " + outputConfigFile) # make a copy of the config file

## first_input = input_sources[0]
## #### use the first input file as a template and make efficiency versions of all its histograms
## testFile = TFile("condor/" + first_input['condor_dir'] + "/" + first_input['dataset'] + ".root")
## testFile.cd("OSUAnalysis/" + first_input['num_channel'])
if arguments.savePDFs:
    os.system("rm -rf sigEfficiency_histograms_pdfs")
    os.system("mkdir sigEfficiency_histograms_pdfs")

# make 1D plots for each mass:
for mass in masses:
    MakeOneHist("lifetime", "mass", lifetimes, mass)

# make 1D plots for each lifetime:
for lifetime in lifetimes:
    MakeOneHist("mass", "lifetime", masses, lifetime)


#testFile.Close()
outputFile.Close()
