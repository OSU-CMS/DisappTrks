#!/usr/bin/env python3

from ROOT import TFile, TH1D, TH2D, TH3D, TGraph2D, TMarker
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
tobDropGrid = numpy.logspace (-3, 0, 5)

################################################################################

TH1D.SetDefaultSumw2 ()

dataFileName = sys.argv[1]
mcFileName = sys.argv[2]
preOrPostTOB = sys.argv[3]
hitDrop = -1.0e13
tobDrop = -1.0e13
if len (sys.argv) > 4:
  hitDrop = float (sys.argv[4])
if len (sys.argv) > 5:
  tobDrop = float (sys.argv[5])

chi2Range = range (1, 10)
if preOrPostTOB.upper () == "POST_TOB":
  chi2Range = range (6, 10)
else:
  chi2Range = range (1, 7)

mcFile = TFile.Open (mcFileName)
dataFile = TFile.Open (dataFileName)

mc = mcFile.Get ("MuonCtrlSelectionPlotter/Track Plots/trackNHitsStripLayersVsTOBLayersVsMissingOuter")
mc.SetName ("mc")
mc.SetDirectory (0)
data = dataFile.Get ("MuonCtrlSelectionPlotter/Track Plots/trackNHitsMissingOuter")
data.SetName ("data")
data.SetDirectory (0)

mcFile.Close ()
dataFile.Close ()

originalMC = mc.ProjectionX ()
originalMC.SetDirectory (0)
originalMC.Scale (1.0 / originalMC.Integral ())
data.Scale (1.0 / data.Integral ())

extraMissingOuterHitsPDFDict = {}

def getMissingOuterHitsPDF (nHits, hitDrop):
  pdf = TH1D ("pdf", ";missing outer hits", 16, -0.5, 15.5)
  pdf.SetDirectory (0)
  for i in range (0, nToys):
    missingOuterHits = 0
    for j in range (0, nHits):
      hit = (random.random () > hitDrop)
      if not hit:
        missingOuterHits += 1
      if hit:
        break
    pdf.Fill (missingOuterHits)

  pdf.Scale (1.0 / pdf.GetEntries ())
  return pdf

def getChi2 (hitDrop, tobDrop, writeHistogram = False):
  fout = 0
  if writeHistogram:
    fout = TFile.Open ("hitAndTOBDropHistogram.root", "recreate")
    fout.cd ()

  correctedMC = TH1D ("correctedMC", ";number of missing outer hits", 16, -0.5, 15.5)
  correctedMC.SetDirectory (0)
  for missingOuterHits in range (0, 16):
    for tobHits in range (0, 16):
      for nHits in range (1, 20):
        nTracks = mc.GetBinContent (mc.FindBin (missingOuterHits, tobHits, nHits))
        nTracksErr = mc.GetBinError (mc.FindBin (missingOuterHits, tobHits, nHits))

        extraMissingOuterHitsPDF = None
        if (nHits, hitDrop) in extraMissingOuterHitsPDFDict:
          extraMissingOuterHitsPDF = extraMissingOuterHitsPDFDict[(nHits, hitDrop)]
        else:
          print("  generating missing outer hits PDF for (nHits = " + str (nHits) + ", hitDrop = " + str (hitDrop) + ")...")
          extraMissingOuterHitsPDF = getMissingOuterHitsPDF (nHits, hitDrop)
          extraMissingOuterHitsPDFDict[(nHits, hitDrop)] = extraMissingOuterHitsPDF

          nHitsStr = str (nHits)
          hitDropStr = str (hitDrop)
          nHitsStr = re.sub (r"\.", r"p", nHitsStr)
          hitDropStr = re.sub (r"\.", r"p", hitDropStr)
          extraMissingOuterHitsPDF.SetName ("extraMissingOuterHits_" + nHitsStr + "_" + hitDropStr)
          if writeHistogram:
            fout.cd ()
            extraMissingOuterHitsPDF.Write ()

        for extraMissingOuterHits in range (0, 16):
          hitDropProb = extraMissingOuterHitsPDF.GetBinContent (extraMissingOuterHitsPDF.FindBin (extraMissingOuterHits))
          hitDropProbErr = extraMissingOuterHitsPDF.GetBinError (extraMissingOuterHitsPDF.FindBin (extraMissingOuterHits))

          if preOrPostTOB.upper () == "POST_TOB":
            hitAndTOBDropBin = correctedMC.FindBin (missingOuterHits + extraMissingOuterHits + tobHits)
            hitAndNoTOBDropBin = correctedMC.FindBin (missingOuterHits)
          else:
            hitAndTOBDropBin = correctedMC.FindBin (missingOuterHits + tobHits)
            hitAndNoTOBDropBin = correctedMC.FindBin (missingOuterHits + extraMissingOuterHits)
          hitAndTOBDropContent = correctedMC.GetBinContent (hitAndTOBDropBin)
          hitAndNoTOBDropContent = correctedMC.GetBinContent (hitAndNoTOBDropBin)
          hitAndTOBDropErr = correctedMC.GetBinError (hitAndTOBDropBin)
          hitAndNoTOBDropErr = correctedMC.GetBinError (hitAndNoTOBDropBin)

          correctedMC.SetBinContent (hitAndTOBDropBin, hitAndTOBDropContent + nTracks * hitDropProb * tobDrop)
          correctedMC.SetBinError (hitAndTOBDropBin, math.hypot (math.hypot (hitAndTOBDropErr, nTracksErr * hitDropProb * tobDrop), nTracks * hitDropProbErr * tobDrop))
          correctedMC.SetBinContent (hitAndNoTOBDropBin, hitAndNoTOBDropContent + nTracks * hitDropProb * (1.0 - tobDrop))
          correctedMC.SetBinError (hitAndNoTOBDropBin, math.hypot (math.hypot (hitAndNoTOBDropErr, nTracksErr * hitDropProb * (1.0 - tobDrop)), nTracks * hitDropProbErr * (1.0 - tobDrop)))

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

if hitDrop > -1.0e12 and tobDrop > -1.0e12:
  chi2, N = getChi2 (hitDrop, tobDrop, writeHistogram = True)
  print("chi2 for corrected MC: " + str (chi2 / N))
else:
  for iteration in range (0, nIterations):
    hitDrop = hitDropGrid
    tobDrop = tobDropGrid
    minChi2 = -1.0
    minChi2HitAndTOBDrop = (-1.0, -1.0)
    minChi2Index = [-1.0, -1.0]
    g = TGraph2D ()
    n = 0
    index = [-1, -1]
    for i in hitDrop:
      index[0] += 1
      index[1] = -1
      for j in tobDrop:
        index[1] += 1
        print("(" + str (iteration + 1) + " / " + str (nIterations) + ") trying hit inefficiency of " + str (i) + " and TOB drop of " + str (j) + "...")
        chi2, N = getChi2 (i, j)
        if N == 0:
          continue
        chi2 /= N
        if chi2 < minChi2 or minChi2 < 0.0:
          minChi2 = chi2
          minChi2HitAndTOBDrop = (i, j)
          minChi2Index = copy.deepcopy (index)
        g.SetPoint (n, i, j, chi2)
        n += 1
    print("(" + str (iteration + 1) + " / " + str (nIterations) + ") minimum chi2: " + str (minChi2) + " at (" + str (minChi2HitAndTOBDrop[0]) + ", " + str (minChi2HitAndTOBDrop[1]) + ")")

    m = TMarker (minChi2HitAndTOBDrop[0], minChi2HitAndTOBDrop[1], 29)
    m.SetMarkerSize (3)

    hitDropGridLower = hitDropGrid[minChi2Index[0] - 1] if minChi2Index[0] > 0 else hitDropGrid[minChi2Index[0]] - hitDropGrid[minChi2Index[0] + 1]
    hitDropGridUpper = hitDropGrid[minChi2Index[0] + 1] if minChi2Index[0] < len (hitDropGrid) - 1 else hitDropGrid[minChi2Index[0]] + hitDropGrid[minChi2Index[0] - 1]
    tobDropGridLower = tobDropGrid[minChi2Index[1] - 1] if minChi2Index[1] > 0 else tobDropGrid[minChi2Index[1]] - tobDropGrid[minChi2Index[1] + 1]
    tobDropGridUpper = tobDropGrid[minChi2Index[1] + 1] if minChi2Index[1] < len (tobDropGrid) - 1 else tobDropGrid[minChi2Index[1]] + tobDropGrid[minChi2Index[1] - 1]
    hitDropGrid     = numpy.linspace (max (hitDropGridLower, 0.0), hitDropGridUpper, 5)
    tobDropGrid = numpy.linspace (max (tobDropGridLower, 0.0), tobDropGridUpper, 5)

    foutMode = "update" if iteration > 0 else "recreate"
    fout = TFile.Open ("hitAndTOBDropChi2.root", foutMode)
    fout.cd ()
    g.Write ("chi2VsHitAndTOBDropProbability_" + str (iteration))
    m.Write ("bestFitPoint_" + str (iteration))
    fout.Close ()
