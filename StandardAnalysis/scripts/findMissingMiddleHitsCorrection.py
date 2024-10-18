#!/usr/bin/env python3

from ROOT import TFile, TH1D, TH2D, TH3D, TGraph, TMarker
import sys
import math
import array
import numpy
import random
import re
import copy

################################################################################
# The following are parameters that you might want to edit.
################################################################################

nToys = 10000
nIterations = 20
hitDropGrid = numpy.logspace (-3, 0, 5)

################################################################################

TH1D.SetDefaultSumw2 ()

dataFileName = sys.argv[1]
mcFileName = sys.argv[2]
hitDrop = -1.0e13
if len (sys.argv) > 3:
  hitDrop = float (sys.argv[3])

chi2Range = list(range(0, 5))

mcFile = TFile.Open (mcFileName)
dataFile = TFile.Open (dataFileName)

mc = mcFile.Get ("HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsStripLayersVsMissingMiddle")
mc.SetName ("mc")
mc.SetDirectory (0)
data = dataFile.Get ("HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingMiddle")
data.SetName ("data")
data.SetDirectory (0)

mcFile.Close ()
dataFile.Close ()

originalMC = mc.ProjectionX ()
originalMC.SetDirectory (0)
originalMC.Scale (1.0 / originalMC.Integral ())
data.Scale (1.0 / data.Integral ())

extraMissingMiddleHitsPDFDict = {}

def getMissingMiddleHitsPDF (nHits, hitDrop):
  pdf = TH1D ("pdf", ";missing middle hits", 16, -0.5, 15.5)
  pdf.SetDirectory (0)
  for i in range (0, nToys):
    missingMiddleHits = 0
    countMissingMiddleHits = False
    for j in range (0, nHits):
      hit = (random.random () > hitDrop)
      if not hit and countMissingMiddleHits:
        missingMiddleHits += 1
      if hit:
        countMissingMiddleHits = True
    pdf.Fill (missingMiddleHits)

  pdf.Scale (1.0 / pdf.GetEntries ())
  return pdf

def getChi2 (hitDrop, writeHistogram = False):
  fout = 0
  if writeHistogram:
    fout = TFile.Open ("hipHistogram.root", "recreate")
    fout.cd ()

  correctedMC = TH1D ("correctedMC", ";number of missing middle hits", 6, -0.5, 5.5)
  correctedMC.SetDirectory (0)
  for missingMiddleHits in range (0, 6):
    for nHits in range (1, 20):
      nTracks = mc.GetBinContent (mc.FindBin (missingMiddleHits, nHits))
      nTracksErr = mc.GetBinError (mc.FindBin (missingMiddleHits, nHits))

      extraMissingMiddleHitsPDF = None
      if (nHits, hitDrop) in extraMissingMiddleHitsPDFDict:
        extraMissingMiddleHitsPDF = extraMissingMiddleHitsPDFDict[(nHits, hitDrop)]
      else:
        print("  generating missing middle hits PDF for (nHits = " + str (nHits) + ", hitDrop = " + str (hitDrop) + ")...")
        extraMissingMiddleHitsPDF = getMissingMiddleHitsPDF (nHits, hitDrop)
        extraMissingMiddleHitsPDFDict[(nHits, hitDrop)] = extraMissingMiddleHitsPDF

        nHitsStr = str (nHits)
        hitDropStr = str (hitDrop)
        nHitsStr = re.sub (r"\.", r"p", nHitsStr)
        hitDropStr = re.sub (r"\.", r"p", hitDropStr)
        extraMissingMiddleHitsPDF.SetName ("extraMissingMiddleHits_" + nHitsStr + "_" + hitDropStr)
        if writeHistogram:
          fout.cd ()
          extraMissingMiddleHitsPDF.Write ()

      for extraMissingMiddleHits in range (0, 6):
        hitDropProb = extraMissingMiddleHitsPDF.GetBinContent (extraMissingMiddleHitsPDF.FindBin (extraMissingMiddleHits))
        hitDropProbErr = extraMissingMiddleHitsPDF.GetBinError (extraMissingMiddleHitsPDF.FindBin (extraMissingMiddleHits))

        hitAndNoTOBDropBin = correctedMC.FindBin (missingMiddleHits + extraMissingMiddleHits)
        hitAndNoTOBDropContent = correctedMC.GetBinContent (hitAndNoTOBDropBin)
        hitAndNoTOBDropErr = correctedMC.GetBinError (hitAndNoTOBDropBin)

        correctedMC.SetBinContent (hitAndNoTOBDropBin, hitAndNoTOBDropContent + nTracks * hitDropProb)
        correctedMC.SetBinError (hitAndNoTOBDropBin, math.hypot (math.hypot (hitAndNoTOBDropErr, nTracksErr * hitDropProb), nTracks * hitDropProbErr))

  if writeHistogram:
    fout.cd ()
    correctedMC.Write ("correctedMC")
    fout.Close ()

  if correctedMC.Integral () != 0.0:
    correctedMC.Scale (1.0 / correctedMC.Integral ())

  chi2 = 0.0
  N = 0
  for i in chi2Range:
    observed = data.GetBinContent (data.FindBin (i))
    expected = correctedMC.GetBinContent (correctedMC.FindBin (i))
    error = math.hypot (data.GetBinError (data.FindBin (i)), correctedMC.GetBinError (correctedMC.FindBin (i)))

    if error != 0.0:
      chi2 += ((observed - expected) * (observed - expected)) / (error * error)
      N += 1

  return (chi2, N)

chi2 = 0.0
N = 0
for i in chi2Range:
  observed = data.GetBinContent (data.FindBin (i))
  expected = originalMC.GetBinContent (originalMC.FindBin (i))
  error = math.hypot (data.GetBinError (data.FindBin (i)), originalMC.GetBinError (originalMC.FindBin (i)))

  if error != 0.0:
    chi2 += ((observed - expected) * (observed - expected)) / (error * error)
    N += 1
print("chi2 for original MC: " + str (chi2 / N))

if hitDrop > -1.0e12:
  chi2, N = getChi2 (hitDrop, writeHistogram = True)
  print("chi2 for corrected MC: " + str (chi2 / N))
else:
  for iteration in range (0, nIterations):
    hitDrop = hitDropGrid
    minChi2 = -1.0
    minChi2HitAndTOBDrop = -1.0
    minChi2Index = -1.0
    g = TGraph ()
    n = 0
    index = -1
    for i in hitDrop:
      index += 1
      print("(" + str (iteration + 1) + " / " + str (nIterations) + ") trying hit inefficiency of " + str (i) + "...")
      chi2, N = getChi2 (i)
      if N == 0:
        continue
      chi2 /= N
      if chi2 < minChi2 or minChi2 < 0.0:
        minChi2 = chi2
        minChi2HitAndTOBDrop = i
        minChi2Index = copy.deepcopy (index)
      g.SetPoint (n, i, chi2)
      n += 1
    print("(" + str (iteration + 1) + " / " + str (nIterations) + ") minimum chi2: " + str (minChi2) + " at " + str (minChi2HitAndTOBDrop))

    m = TMarker (minChi2HitAndTOBDrop, minChi2, 29)
    m.SetMarkerSize (3)

    hitDropGridLower = hitDropGrid[minChi2Index - 1] if minChi2Index > 0 else hitDropGrid[minChi2Index] - hitDropGrid[minChi2Index + 1]
    hitDropGridUpper = hitDropGrid[minChi2Index + 1] if minChi2Index < len (hitDropGrid) - 1 else hitDropGrid[minChi2Index] + hitDropGrid[minChi2Index - 1]
    hitDropGrid     = numpy.linspace (max (hitDropGridLower, 0.0), hitDropGridUpper, 5)

    foutMode = "update" if iteration > 0 else "recreate"
    fout = TFile.Open ("hipChi2.root", foutMode)
    fout.cd ()
    g.Write ("chi2VsHitDropProbability_" + str (iteration))
    m.Write ("bestFitPoint_" + str (iteration))
    fout.Close ()
