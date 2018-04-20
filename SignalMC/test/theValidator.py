#!/usr/bin/env python

import os, sys

from ROOT import gROOT, TFile, TH1D, TCanvas, TLegend, kRed, kOrange, kGreen, kBlue, kViolet, kBlack

gROOT.SetBatch()

if len (sys.argv) < 2:
  print "Usage: " + os.path.basename (sys.argv[0]) + " HIST_NAME [REBIN_FACTOR]"
  sys.exit (1)

histName = sys.argv[1]
rebinFactor = 1
if len (sys.argv) > 2:
  rebinFactor = int (sys.argv[2])

def setStyle (h, color = kBlack):
  h.Rebin (rebinFactor)
  h.Scale (1.0 / h.Integral ())

  h.SetMarkerStyle (20)
  h.SetMarkerSize (2.0)
  h.SetLineWidth (3)

  h.SetMarkerColor (color)
  h.SetLineColor (color)

  h.SetStats (0)

  h.GetXaxis ().SetNdivisions (505)
  h.GetXaxis ().SetLabelOffset (0.005)
  h.GetXaxis ().SetLabelSize (0.04)
  h.GetXaxis ().SetTitleOffset (1.0)
  h.GetXaxis ().SetTitleSize (0.04)

  h.GetYaxis ().SetNdivisions (505)
  h.GetYaxis ().SetLabelOffset (0.005)
  h.GetYaxis ().SetLabelSize (0.04)
  h.GetYaxis ().SetTitleOffset (1.25)
  h.GetYaxis ().SetTitleSize (0.04)

fin = TFile ("newOutput_100_100.root")
fin.cd ()
hist_100_100 = fin.Get ("charginoValidator/" + histName)
hist_100_100.SetDirectory (0)
hist_100_100.SetName ("hist_100_100")
fin.Close ()

fin = TFile ("validate.root")
fin.cd ()
hist_300_100 = fin.Get ("charginoValidator/" + histName)
hist_300_100.SetDirectory (0)
hist_300_100.SetName ("newStuff")
fin.Close ()

fin = TFile ("newOutput_500_100.root")
fin.cd ()
hist_500_100 = fin.Get ("charginoValidator/" + histName)
hist_500_100.SetDirectory (0)
hist_500_100.SetName ("hist_500_100")
fin.Close ()

fin = TFile ("newOutput_700_100.root")
fin.cd ()
hist_700_100 = fin.Get ("charginoValidator/" + histName)
hist_700_100.SetDirectory (0)
hist_700_100.SetName ("hist_700_100")
fin.Close ()

fin = TFile ("newOutput_700_10.root")
fin.cd ()
hist_700_10 = fin.Get ("charginoValidator/" + histName)
hist_700_10.SetDirectory (0)
hist_700_10.SetName ("hist_700_10")
fin.Close ()

fin = TFile ("newOutput_700_1000.root")
fin.cd ()
hist_700_1000 = fin.Get ("charginoValidator/" + histName)
hist_700_1000.SetDirectory (0)
hist_700_1000.SetName ("hist_700_1000")
fin.Close ()

setStyle (hist_100_100, kRed)
setStyle (hist_300_100, kOrange)
setStyle (hist_500_100, kGreen)
setStyle (hist_700_100, kBlue)

setStyle (hist_700_10, kBlue + 2)
setStyle (hist_700_1000, kBlue - 7)

leg1 = TLegend (0.402256, 0.702842, 0.632832, 0.894057)
leg1.SetTextSize (0.0387597)
leg1.SetBorderSize (0)
leg1.AddEntry (hist_100_100, "100 GeV #tilde{#chi}^{#pm} (c#tau = 100 cm)", "p")
leg1.AddEntry (hist_300_100, "300 GeV #tilde{#chi}^{#pm} (c#tau = 100 cm)", "p")
leg1.AddEntry (hist_500_100, "500 GeV #tilde{#chi}^{#pm} (c#tau = 100 cm)", "p")
leg1.AddEntry (hist_700_100, "700 GeV #tilde{#chi}^{#pm} (c#tau = 100 cm)", "p")

c1 = TCanvas ("c1", "c1", 800, 800)
c1.SetLeftMargin (0.121554)
c1.SetRightMargin (0.0401003)
c1.SetBottomMargin (0.0956072)
c1.SetTopMargin (0.0607235)
c1.cd ()
hist_100_100.Draw ()
hist_300_100.Draw ("same")
hist_500_100.Draw ("same")
hist_700_100.Draw ("same")
leg1.Draw ("same")

leg2 = TLegend (0.402256, 0.748062, 0.631579, 0.895349)
leg2.SetTextSize (0.0387597)
leg2.SetBorderSize (0)
leg2.AddEntry (hist_700_10, "700 GeV #tilde{#chi}^{#pm} (c#tau = 10 cm)", "p")
leg2.AddEntry (hist_700_100, "700 GeV #tilde{#chi}^{#pm} (c#tau = 100 cm)", "p")
leg2.AddEntry (hist_700_1000, "700 GeV #tilde{#chi}^{#pm} (c#tau = 1000 cm)", "p")

c2 = TCanvas ("c2", "c2", 800, 800)
c2.SetLeftMargin (0.121554)
c2.SetRightMargin (0.0401003)
c2.SetBottomMargin (0.0956072)
c2.SetTopMargin (0.0607235)
c2.cd ()
hist_700_10.Draw ()
hist_700_100.Draw ("same")
hist_700_1000.Draw ("same")
leg2.Draw ("same")

fout = TFile (histName + ".root", "recreate")
fout.cd ()
c1.Write (histName + "_vs_mass")
c2.Write (histName + "_vs_lifetime")
fout.Close ()
