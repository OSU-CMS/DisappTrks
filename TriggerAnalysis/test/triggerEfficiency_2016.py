#!/usr/bin/env python

from DisappTrks.TriggerAnalysis.triggerEfficiency import *
from DisappTrks.TriggerAnalysis.AllTriggers import *
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *
from ROOT import gROOT, TCanvas, TFile
import os
import re

gROOT.SetBatch()

dirs = getUser()

canvas = TCanvas("c1", "c1", 561, 482, 800, 830)
canvas.Range(0.644391, -0.1480839, 3.167468, 1.19299)
canvas.SetFillColor(0)
canvas.SetBorderMode(0)
canvas.SetBorderSize(2)
canvas.SetLogx()
canvas.SetTickx(1)
canvas.SetTicky(1)
canvas.SetLeftMargin(0.122807)
canvas.SetRightMargin(0.05012531)
canvas.SetTopMargin(0.06947891)
canvas.SetBottomMargin(0.1104218)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)
canvas.SetFrameFillStyle(0)
canvas.SetFrameBorderMode(0)

path = "all"
if len (sys.argv) > 1:
    path = sys.argv[1]

# '' will gives you Dataset_2016.root for the whole year
#runPeriods = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
runPeriods = ['BC', 'DEFGH']

for runPeriod in runPeriods:

    fout = TFile.Open("triggerEfficiency_2016" + runPeriod + ".root", "recreate")

    for trigger in triggerFiltersMet:

        triggerWithoutUnderscores = re.sub(r"_", "", trigger)

        if path == trigger or path == "all":

            print "********************************************************************************"
            print "Calculating efficiency of", trigger, " in search region (2016", runPeriod, ")"
            print "--------------------------------------------------------------------------------"

            legs = ["METLeg", "TrackLeg"] if "IsoTrk50" in trigger else ["METPath"]

            for leg in legs:

                numeratorName = triggerWithoutUnderscores + "METLegNumerator"
                denominatorName = "METLegDenominator"

                if leg == "TrackLeg":
                    numeratorName = triggerWithoutUnderscores + "TrackLegNumeratorWithMuons"
                    denominatorName = triggerWithoutUnderscores + "TrackLegDenominatorWithMuons"

                efficiency = TriggerEfficiency(trigger, triggerFiltersMet[trigger], leg)
                efficiency.addTFile(fout)
                efficiency.addTCanvas(canvas)
                efficiency.addLuminosityInInvPb(lumi["SingleMuon_2016" + runPeriod])
                efficiency.addChannel("Numerator", numeratorName, "SingleMu_2016" + runPeriod, dirs['Brian'] + "2016_final/triggerEfficiency_allPaths")
                efficiency.addChannel("Denominator", denominatorName, "SingleMu_2016" + runPeriod, dirs['Brian'] + "2016_final/triggerEfficiency_allPaths")
                efficiency.plotEfficiency()
                print "********************************************************************************"


    fout.Close()
