#!/usr/bin/env python

import math

from bkgdEstimate_2015 import nEstFakeVsNHits as n2015
from bkgdEstimate_2016 import nEstFakeVsNHits as n2016
from bkgdEstimate_2015 import nEstFakeVsNHitsZtoMuMu as nZtoMuMu2015
from bkgdEstimate_2016 import nEstFakeVsNHitsZtoMuMu as nZtoMuMu2016

from ROOT import TH1D, TFile

nVsNHits = TH1D ("nFakesVsNHits", ";minimum number of valid hits", 5, 2.5, 7.5)
nVsNHitsZtoMuMu = TH1D ("nFakesVsNHitsZtoMuMu", ";minimum number of valid hits", 5, 2.5, 7.5)
for minHits in range (3, 8):
    i = nVsNHits.FindBin (minHits)

    nVsNHits.SetBinContent (i, n2015[minHits][0] + n2016["BC"][minHits][0] + n2016["DEFGH"][minHits][0])
    nVsNHits.SetBinError (i, math.hypot (math.hypot (n2015[minHits][1], n2016["BC"][minHits][1]), n2016["DEFGH"][minHits][0]))

    nVsNHitsZtoMuMu.SetBinContent (i, nZtoMuMu2015[minHits][0] + nZtoMuMu2016["BC"][minHits][0] + nZtoMuMu2016["DEFGH"][minHits][0])
    nVsNHitsZtoMuMu.SetBinError (i, math.hypot (math.hypot (nZtoMuMu2015[minHits][1], nZtoMuMu2016["BC"][minHits][1]), nZtoMuMu2016["DEFGH"][minHits][0]))

fout = TFile ("nFakesVsNHits.root", "recreate")
fout.cd ()
nVsNHits.Write ("nFakesVsNHits")
nVsNHitsZtoMuMu.Write ("nFakesVsNHitsZtoMuMu")
fout.Close ()
