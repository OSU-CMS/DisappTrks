#!/usr/bin/env python

import math, glob, re, sys

from bkgdEstimate_2015 import nEstFakeVsNHits as n2015
from bkgdEstimate_2016 import nEstFakeVsNHits as n2016
from bkgdEstimate_2015 import nEstFakeVsNHitsZtoMuMu as nZtoMuMu2015
from bkgdEstimate_2016 import nEstFakeVsNHitsZtoMuMu as nZtoMuMu2016

from ROOT import TH1D, TFile

def sqrtHist (h):
    for i in range (0, h.GetNbinsX () + 2):
        content = h.GetBinContent (i)
        error = h.GetBinError (i)

        if content == 0.0:
            continue

        content = math.sqrt (content)
        error = error / (2.0 * math.sqrt (content))

        h.SetBinContent (i, content)
        h.SetBinError (i, error)

bVsNHits = TH1D ("nFakesVsNHits", ";minimum number of valid hits", 5, 2.5, 7.5)
bVsNHitsZtoMuMu = TH1D ("nFakesVsNHitsZtoMuMu", ";minimum number of valid hits", 5, 2.5, 7.5)
for minHits in range (3, 8):
    i = bVsNHits.FindBin (minHits)

    bVsNHits.SetBinContent (i, n2015[minHits][0] + n2016["BC"][minHits][0] + n2016["DEFGH"][minHits][0])
    bVsNHits.SetBinError (i, math.hypot (math.hypot (n2015[minHits][1], n2016["BC"][minHits][1]), n2016["DEFGH"][minHits][0]))

    bVsNHitsZtoMuMu.SetBinContent (i, nZtoMuMu2015[minHits][0] + nZtoMuMu2016["BC"][minHits][0] + nZtoMuMu2016["DEFGH"][minHits][0])
    bVsNHitsZtoMuMu.SetBinError (i, math.hypot (math.hypot (nZtoMuMu2015[minHits][1], nZtoMuMu2016["BC"][minHits][1]), nZtoMuMu2016["DEFGH"][minHits][0]))

fout = TFile ("nFakesVsNHits.root", "recreate")
fout.cd ()
bVsNHits.Write ("nFakesVsNHits")
bVsNHitsZtoMuMu.Write ("nFakesVsNHitsZtoMuMu")
fout.Close ()

for signal in glob.glob ("condor/2016_final_prompt/signalAcceptanceVsNHits/AMSB*.root"):
    s = TH1D ("nSignalVsNHits", ";minimum number of valid hits", 5, 2.5, 7.5)
    lifetime = re.sub (r".*GeV_(.*cm)_80X.*", r"\1", signal)
    fin = TFile (signal)
    for minHits in range (3, 8):
        cutFlow = fin.Get ("DisTrkSelectionCutFlowPlotter/cutFlow")
        cutFlow.SetDirectory (0)
        cutFlow3 = fin.Get ("DisTrkSelectionNHits3CutFlowPlotter/cutFlow")
        cutFlow3.SetDirectory (0)
        cutFlow3.SetName ("cutFlow3")
        cutFlow4 = fin.Get ("DisTrkSelectionNHits4CutFlowPlotter/cutFlow")
        cutFlow4.SetDirectory (0)
        cutFlow4.SetName ("cutFlow4")
        cutFlow5 = fin.Get ("DisTrkSelectionNHits5CutFlowPlotter/cutFlow")
        cutFlow5.SetDirectory (0)
        cutFlow5.SetName ("cutFlow5")
        cutFlow6 = fin.Get ("DisTrkSelectionNHits6CutFlowPlotter/cutFlow")
        cutFlow6.SetDirectory (0)
        cutFlow6.SetName ("cutFlow6")

        cutFlow.GetXaxis ().SetBinLabel (22, "")
        cutFlow3.GetXaxis ().SetBinLabel (22, "")
        cutFlow4.GetXaxis ().SetBinLabel (22, "")
        cutFlow5.GetXaxis ().SetBinLabel (22, "")
        cutFlow6.GetXaxis ().SetBinLabel (22, "")

        if minHits < 7:
            cutFlow.Add (cutFlow6)
        if minHits < 6:
            cutFlow.Add (cutFlow5)
        if minHits < 5:
            cutFlow.Add (cutFlow4)
        if minHits < 4:
            cutFlow.Add (cutFlow3)

        i = s.FindBin (minHits)
        print "minHits: " + str (minHits) + ", i: " + str (i)
        print "  filling bin " + str (i) + " with " + str (cutFlow.GetBinContent (cutFlow.GetNbinsX ())) + " +- " + str (cutFlow.GetBinError (cutFlow.GetNbinsX ()))
        s.SetBinContent (i, cutFlow.GetBinContent (cutFlow.GetNbinsX ()))
        s.SetBinError (i, cutFlow.GetBinError (cutFlow.GetNbinsX ()))

    fin.Close ()
    fout = TFile ("nFakesVsNHits.root", "update")
    fout.cd ()
    s.Write ("nSignalVsNHits_" + lifetime)
    fout.Close ()

    sPlusB = s.Clone ("nSignalPlusFakeVsNHits")
    sPlusB.Add (bVsNHitsZtoMuMu)
    sqrtHist (sPlusB)
    s.Divide (sPlusB)

    fout = TFile ("nFakesVsNHits.root", "update")
    fout.cd ()
    s.Write ("sOverSqrtSPlusB_" + lifetime)
    fout.Close ()
