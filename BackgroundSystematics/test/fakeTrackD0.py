#!/usr/bin/env python

import math
from OSUT3Analysis.Configuration.histogramUtilities import getEfficiency
from ROOT import TFile, TH1D, THStack, kYellow, kBlue, Double

def getXi (h):
  a = h.FindBin (-0.02)
  b = h.FindBin (0.02) - 1
  n = h.GetNbinsX ()

  numError = Double (0.0)
  num = h.IntegralAndError (a, b, numError)

  denLeftError = Double (0.0)
  denLeft = h.IntegralAndError (-1, a, denLeftError)
  denRightError = Double (0.0)
  denRight = h.IntegralAndError (b, n + 1, denRightError)
  den = denLeft + denRight
  denError = math.hypot (denLeftError, denRightError)

  xi = num / den
  xiError = math.hypot (den * numError, denError * num) / (den * den)

  return (xi, xiError)

def fakeFractionInSideband (real, fake):
  a = real.FindBin (-0.02)
  b = real.FindBin (0.02) - 1
  n = real.GetNbinsX ()

  realLeftError = Double (0.0)
  realLeft = real.IntegralAndError (-1, a, realLeftError)
  realRightError = Double (0.0)
  realRight = real.IntegralAndError (b, n + 1, realRightError)
  realSideband = realLeft + realRight
  realSidebandError = math.hypot (realLeftError, realRightError)

  fakeLeftError = Double (0.0)
  fakeLeft = fake.IntegralAndError (-1, a, fakeLeftError)
  fakeRightError = Double (0.0)
  fakeRight = fake.IntegralAndError (b, n + 1, fakeRightError)
  fakeSideband = fakeLeft + fakeRight
  fakeSidebandError = math.hypot (fakeLeftError, fakeRightError)

  sideband = realSideband + fakeSideband
  sidebandError = math.hypot (realSidebandError, fakeSidebandError)

  return getEfficiency (fakeSideband, fakeSidebandError, sideband, sidebandError)

fin = TFile ("condor/2016_final_prompt/fakeTracksInMC_metMinimalSkim/Background.root")

fake = fin.Get ("JustAFakeTrkNoD0CutPlotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
fake.SetDirectory (0)
fake.SetName ("fake")

fake3 = fin.Get ("JustAFakeTrkNoD0CutNHits3Plotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
fake3.SetDirectory (0)
fake3.SetName ("fake3")

fake4 = fin.Get ("JustAFakeTrkNoD0CutNHits4Plotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
fake4.SetDirectory (0)
fake4.SetName ("fake4")

fake5 = fin.Get ("JustAFakeTrkNoD0CutNHits5Plotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
fake5.SetDirectory (0)
fake5.SetName ("fake5")

fake6 = fin.Get ("JustAFakeTrkNoD0CutNHits6Plotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
fake6.SetDirectory (0)
fake6.SetName ("fake6")

real = fin.Get ("JustARealTrkNoD0CutPlotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
real.SetDirectory (0)
real.SetName ("real")

real3 = fin.Get ("JustARealTrkNoD0CutNHits3Plotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
real3.SetDirectory (0)
real3.SetName ("real3")

real4 = fin.Get ("JustARealTrkNoD0CutNHits4Plotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
real4.SetDirectory (0)
real4.SetName ("real4")

real5 = fin.Get ("JustARealTrkNoD0CutNHits5Plotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
real5.SetDirectory (0)
real5.SetName ("real5")

real6 = fin.Get ("JustARealTrkNoD0CutNHits6Plotter/Track-eventvariable Plots/trackd0WRTPV_Zoom")
real6.SetDirectory (0)
real6.SetName ("real6")

fin.Close ()

fakeFraction, fakeFractionErrorLow, fakeFractionErrorHigh = fakeFractionInSideband (real, fake)
fakeFraction3, fakeFraction3ErrorLow, fakeFraction3ErrorHigh = fakeFractionInSideband (real3, fake3)
fakeFraction4, fakeFraction4ErrorLow, fakeFraction4ErrorHigh = fakeFractionInSideband (real4, fake4)
fakeFraction5, fakeFraction5ErrorLow, fakeFraction5ErrorHigh = fakeFractionInSideband (real5, fake5)
fakeFraction6, fakeFraction6ErrorLow, fakeFraction6ErrorHigh = fakeFractionInSideband (real6, fake6)

print "================================================================================"
print "fake fraction in sideband"
print "--------------------------------------------------------------------------------"

print "[>=7 hits] " + str (fakeFraction) + " - " + str (fakeFractionErrorLow) + " + " + str (fakeFractionErrorHigh)
print "[==6 hits] " + str (fakeFraction6) + " - " + str (fakeFraction6ErrorLow) + " + " + str (fakeFraction6ErrorHigh)
print "[==5 hits] " + str (fakeFraction5) + " - " + str (fakeFraction5ErrorLow) + " + " + str (fakeFraction5ErrorHigh)
print "[==4 hits] " + str (fakeFraction4) + " - " + str (fakeFraction4ErrorLow) + " + " + str (fakeFraction4ErrorHigh)
print "[==3 hits] " + str (fakeFraction3) + " - " + str (fakeFraction3ErrorLow) + " + " + str (fakeFraction3ErrorHigh)

print "================================================================================"

maxUp = 0.0
maxDown = 1.0e12

xiFake, xiFakeError = getXi (fake)

xiFake3, xiFake3Error = getXi (fake3)
maxUp = max (maxUp, xiFake3 + xiFake3Error)
maxDown = min (maxDown, xiFake3 - xiFake3Error)

xiFake4, xiFake4Error = getXi (fake4)
maxUp = max (maxUp, xiFake4 + xiFake4Error)
maxDown = min (maxDown, xiFake4 - xiFake4Error)

xiFake5, xiFake5Error = getXi (fake5)
maxUp = max (maxUp, xiFake5 + xiFake5Error)
maxDown = min (maxDown, xiFake5 - xiFake5Error)

xiFake6, xiFake6Error = getXi (fake6)
maxUp = max (maxUp, xiFake6 + xiFake6Error)
maxDown = min (maxDown, xiFake6 - xiFake6Error)

maxUp = maxUp - xiFake3
maxDown = xiFake3 - maxDown

xiReal, xiRealError = getXi (real)
xiReal3, xiReal3Error = getXi (real3)
xiReal4, xiReal4Error = getXi (real4)
xiReal5, xiReal5Error = getXi (real5)
xiReal6, xiReal6Error = getXi (real6)

xi3, xi3Error = getXi (fake3 + real3)

print "================================================================================"
print "transfer factor"
print "--------------------------------------------------------------------------------"

print "[fake, >=7 hits] " + str (xiFake) + " +- " + str (xiFakeError)
print "[fake, ==6 hits] " + str (xiFake6) + " +- " + str (xiFake6Error) + " (" + str (abs (xiFake6 - xiFake) / math.hypot (xiFake6Error, xiFakeError)) + " sigma)"
print "[fake, ==5 hits] " + str (xiFake5) + " +- " + str (xiFake5Error) + " (" + str (abs (xiFake5 - xiFake) / math.hypot (xiFake5Error, xiFakeError)) + " sigma)"
print "[fake, ==4 hits] " + str (xiFake4) + " +- " + str (xiFake4Error) + " (" + str (abs (xiFake4 - xiFake) / math.hypot (xiFake4Error, xiFakeError)) + " sigma)"
print "[fake, ==3 hits] " + str (xiFake3) + " +- " + str (xiFake3Error) + " (" + str (abs (xiFake3 - xiFake) / math.hypot (xiFake3Error, xiFakeError)) + " sigma)"

print ""

print "[==3 hits] " + str (xi3) + " +- " + str (xi3Error) + " (" + str (abs (xi3 - xiFake) / math.hypot (xi3Error, xiFakeError)) + " sigma)"

print ""

print "[real, >=7 hits] " + str (xiReal) + " +- " + str (xiRealError)
print "[real, ==6 hits] " + str (xiReal6) + " +- " + str (xiReal6Error) + " (" + str (abs (xiReal6 - xiReal) / math.hypot (xiReal6Error, xiRealError)) + " sigma)"
print "[real, ==5 hits] " + str (xiReal5) + " +- " + str (xiReal5Error) + " (" + str (abs (xiReal5 - xiReal) / math.hypot (xiReal5Error, xiRealError)) + " sigma)"
print "[real, ==4 hits] " + str (xiReal4) + " +- " + str (xiReal4Error) + " (" + str (abs (xiReal4 - xiReal) / math.hypot (xiReal4Error, xiRealError)) + " sigma)"
print "[real, ==3 hits] " + str (xiReal3) + " +- " + str (xiReal3Error) + " (" + str (abs (xiReal3 - xiReal) / math.hypot (xiReal3Error, xiRealError)) + " sigma)"

print "================================================================================"

print "================================================================================"
print "systematic uncertainty"
print "--------------------------------------------------------------------------------"
print "- " + str (maxDown) + " + " + str (maxUp) + " (- " + str ((maxDown / xiFake3) * 100.0) + " + " + str ((maxUp / xiFake3) * 100.0) + ")%"
print "================================================================================"

fake.Rebin (3)
fake3.Rebin (3)
fake4.Rebin (3)
fake5.Rebin (3)
fake6.Rebin (3)

real.Rebin (3)
real3.Rebin (3)
real4.Rebin (3)
real5.Rebin (3)
real6.Rebin (3)

fake.SetFillColor (kYellow)
fake3.SetFillColor (kYellow)
fake4.SetFillColor (kYellow)
fake5.SetFillColor (kYellow)
fake6.SetFillColor (kYellow)

real.SetFillColor (kBlue)
real3.SetFillColor (kBlue)
real4.SetFillColor (kBlue)
real5.SetFillColor (kBlue)
real6.SetFillColor (kBlue)

hs = THStack ("hs", "")
hs.Add (real)
hs.Add (fake)

hs3 = THStack ("hs3", "")
hs3.Add (real3)
hs3.Add (fake3)

hs4 = THStack ("hs4", "")
hs4.Add (real4)
hs4.Add (fake4)

hs5 = THStack ("hs5", "")
hs5.Add (real5)
hs5.Add (fake5)

hs6 = THStack ("hs6", "")
hs6.Add (real6)
hs6.Add (fake6)

fout = TFile ("fakeTrackD0.root", "recreate")
fout.cd ()
hs.Write ("fakeTrackD0")
hs6.Write ("fakeTrackD0NHits6")
hs5.Write ("fakeTrackD0NHits5")
hs4.Write ("fakeTrackD0NHits4")
hs3.Write ("fakeTrackD0NHits3")
fout.Close ()
