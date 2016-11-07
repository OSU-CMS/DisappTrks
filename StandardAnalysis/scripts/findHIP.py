#!/usr/bin/env python

from ROOT import TFile, TH1D, TH2D, TGraph
import sys
import math
import array
import numpy
import random

chi2Range = range (0, 16)
nToys = 1000

mcWithHIPFileName = sys.argv[1]
mcFileName = sys.argv[2]
hip = -1.0
if len (sys.argv) > 3:
  hip = float (sys.argv[3])

mcFile = TFile.Open (mcFileName)
mcWithHIPFile = TFile.Open (mcWithHIPFileName)

mc = mcFile.Get ("MuonTagSkim/Muon Plots/trackNHitsTrackerLayersVsMissingMiddle")
mc.SetName ("mc")
mc.SetDirectory (0)
mcWithHIP = mcWithHIPFile.Get ("MuonTagSkim/Muon Plots/muonNHitsMissingMiddle")
mcWithHIP.SetName ("mcWithHIP")
mcWithHIP.SetDirectory (0)

mcFile.Close ()
mcWithHIPFile.Close ()

originalMC = mc.ProjectionX ()
originalMC.Scale (1.0 / originalMC.Integral ())

chi2 = 0.0
for i in chi2Range:
  observed = mcWithHIP.GetBinContent (mcWithHIP.FindBin (i))
  expected = originalMC.GetBinContent (originalMC.FindBin (i))
  error = math.hypot (mcWithHIP.GetBinError (mcWithHIP.FindBin (i)), originalMC.GetBinError (originalMC.FindBin (i)))

  if error > 0.0:
    chi2 += ((observed - expected) * (observed - expected)) / (error * error)
print "chi2 for original MC: " + str (chi2)

def getMissingMiddleHitsPDF (nHits, hip):
  pdf = TH1D ("pdf", ";missing middle hits", 16, -0.5, 15.5)
  for i in range (0, nToys):
    hitPattern = []
    missingMiddleHits = 0
    countMissingMiddleHits = False
    for hit in range (0, nHits):
      hitPattern.append (random.random () > hip)
    for hit in hitPattern:
      if not hit and countMissingMiddleHits:
        missingMiddleHits += 1
      if hit:
        countMissingMiddleHits = True
    pdf.Fill (missingMiddleHits)
  pdf.Scale (1.0 / pdf.Integral ())

def getChi2 (hip, writeHistogram = False):
  correctedMC = TH1D ("correctedMC", ";number of missing middle hits", 16, -0.5, 15.5)
  for missingMiddleHits in range (0, 16):
    for nHits in range (0, 50):
      nTracks = mc.GetBinContent (mc.FindBin (missingMiddleHits, nHits))
      nTracksErr = mc.GetBinError (mc.FindBin (missingMiddleHits, nHits))

      extraMissingMiddleHitsPDF = getMissingMiddleHitsPDF (nHits, hip)

      for extraMissingMiddleHits in range (0, 16):
        hipProb = extraMissingMiddleHitsPDF.GetBinContent (extraMissingMiddleHitsPDF.FindBin (extraMissingMiddleHits))
        hipProbErr = extraMissingMiddleHitsPDF.GetBinError (extraMissingMiddleHitsPDF.FindBin (extraMissingMiddleHits))

        hipBin = correctedMC.FindBin (missingMiddleHits + extraMissingMiddleHits)
        noHIPBin = correctedMC.FindBin (missingMiddleHits)
        hipContent = correctedMC.GetBinContent (hipBin)
        noHIPContent = correctedMC.GetBinContent (noHIPBin)
        hipErr = correctedMC.GetBinError (hipBin)
        noHIPErr = correctedMC.GetBinError (noHIPBin)

        correctedMC.SetBinContent (hipBin, hipContent + nTracks * hipProb)
        correctedMC.SetBinError (hipBin, math.hypot (math.hypot (hipProb * nTracksErr, hipProbErr * nTracks), hipErr))
        correctedMC.SetBinContent (noHIPBin, noHIPContent + nTracks * (1.0 - hipProb))
        correctedMC.SetBinError (noHIPBin, math.hypot (math.hypot ((1.0 - hipProb) * nTracksErr, hipProbErr * nTracks), hipErr))

  if writeHistogram:
    fout = TFile.Open ("hipHistogram.root", "recreate")
    fout.cd ()
    correctedMC.Write ("correctedMC")
    fout.Close ()

  correctedMC.Scale (1.0 / correctedMC.Integral ())
  mcWithHIP.Scale (1.0 / mcWithHIP.Integral ())

  chi2 = 0.0
  for i in chi2Range:
    observed = mcWithHIP.GetBinContent (mcWithHIP.FindBin (i))
    expected = correctedMC.GetBinContent (correctedMC.FindBin (i))
    error = math.hypot (mcWithHIP.GetBinError (mcWithHIP.FindBin (i)), correctedMC.GetBinError (correctedMC.FindBin (i)))

    if error > 0.0:
      chi2 += ((observed - expected) * (observed - expected)) / (error * error)
  return chi2

if hip >= 0.0:
  chi2 = getChi2 (hip, writeHistogram = True)
  print "chi2 for corrected MC: " + str (chi2)
else:
  hip = numpy.logspace (-6, 0, 1000)
  chi2 = array.array ("d")
  minChi2 = -1.0
  minChi2TOBDrop = -1.0
  for i in hip:
    print "trying TOB drop probability of " + str (i) + "..."
    chi2.append (getChi2 (i))
    if chi2[-1] < minChi2 or minChi2 < 0.0:
      minChi2 = chi2[-1]
      minChi2TOBDrop = i
  print "minimum chi2: " + str (minChi2) + " at " + str (minChi2TOBDrop)

  g = TGraph (len (hip), hip, chi2)
  fout = TFile.Open ("hipChi2.root", "recreate")
  fout.cd ()
  g.Write ("chi2VsTOBDropProbability")
  fout.Close ()
