#!/usr/bin/env python

from ROOT import TFile, TH1D, TH2D, TGraph
import sys
import math
import array
import numpy

chi2Range = range (3, 7)

dataFileName = sys.argv[1]
mcFileName = sys.argv[2]
tobDrop = -1.0
if len (sys.argv) > 3:
  tobDrop = float (sys.argv[3])

mcFile = TFile.Open (mcFileName)
dataFile = TFile.Open (dataFileName)

mc = mcFile.Get ("MuonCtrlSelectionPlotter/Track Plots/trackNHitsTOBVsMissingOuter")
mc.SetName ("mc")
mc.SetDirectory (0)
data = dataFile.Get ("MuonCtrlSelectionPlotter/Track Plots/trackNHitsMissingOuter")
data.SetName ("data")
data.SetDirectory (0)

mcFile.Close ()
dataFile.Close ()

originalMC = mc.ProjectionX ()
originalMC.Scale (1.0 / originalMC.Integral ())

chi2 = 0.0
for i in chi2Range:
  observed = data.GetBinContent (data.FindBin (i))
  expected = originalMC.GetBinContent (originalMC.FindBin (i))
  error = math.hypot (data.GetBinError (data.FindBin (i)), originalMC.GetBinError (originalMC.FindBin (i)))

  if error > 0.0:
    chi2 += ((observed - expected) * (observed - expected)) / (error * error)
print "chi2 for original MC: " + str (chi2)

def getChi2 (tobDrop, writeHistogram = False):
  correctedMC = TH1D ("correctedMC", ";number of missing outer hits", 16, -0.5, 15.5)
  for missingOuterHits in range (0, 16):
    for tobHits in range (0, 16):
      nTracks = mc.GetBinContent (mc.FindBin (missingOuterHits, tobHits))
      nTracksErr = mc.GetBinError (mc.FindBin (missingOuterHits, tobHits))

      tobDropBin = correctedMC.FindBin (missingOuterHits + tobHits)
      noTOBDropBin = correctedMC.FindBin (missingOuterHits)
      tobDropContent = correctedMC.GetBinContent (tobDropBin)
      noTOBDropContent = correctedMC.GetBinContent (noTOBDropBin)
      tobDropErr = correctedMC.GetBinError (tobDropBin)
      noTOBDropErr = correctedMC.GetBinError (noTOBDropBin)

      correctedMC.SetBinContent (tobDropBin, tobDropContent + nTracks * tobDrop)
      correctedMC.SetBinError (tobDropBin, math.hypot (tobDropErr, nTracksErr * tobDrop))
      correctedMC.SetBinContent (noTOBDropBin, noTOBDropContent + nTracks * (1.0 - tobDrop))
      correctedMC.SetBinError (noTOBDropBin, math.hypot (noTOBDropErr, nTracksErr * (1.0 - tobDrop)))

  if writeHistogram:
    fout = TFile.Open ("tobDropHistogram.root", "recreate")
    fout.cd ()
    correctedMC.Write ("correctedMC")
    fout.Close ()

  correctedMC.Scale (1.0 / correctedMC.Integral ())
  data.Scale (1.0 / data.Integral ())

  chi2 = 0.0
  for i in chi2Range:
    observed = data.GetBinContent (data.FindBin (i))
    expected = correctedMC.GetBinContent (correctedMC.FindBin (i))
    error = math.hypot (data.GetBinError (data.FindBin (i)), correctedMC.GetBinError (correctedMC.FindBin (i)))

    if error > 0.0:
      chi2 += ((observed - expected) * (observed - expected)) / (error * error)
  return chi2

if tobDrop >= 0.0:
  chi2 = getChi2 (tobDrop, writeHistogram = True)
  print "chi2 for corrected MC: " + str (chi2)
else:
  tobDrop = numpy.logspace (-6, 0, 1000)
  chi2 = array.array ("d")
  minChi2 = -1.0
  minChi2TOBDrop = -1.0
  for i in tobDrop:
    print "trying TOB drop probability of " + str (i) + "..."
    chi2.append (getChi2 (i))
    if chi2[-1] < minChi2 or minChi2 < 0.0:
      minChi2 = chi2[-1]
      minChi2TOBDrop = i
  print "minimum chi2: " + str (minChi2) + " at " + str (minChi2TOBDrop)

  g = TGraph (len (tobDrop), tobDrop, chi2)
  fout = TFile.Open ("tobDropChi2.root", "recreate")
  fout.cd ()
  g.Write ("chi2VsTOBDropProbability")
  fout.Close ()
