import os
import math
import sys

from ROOT import TGraphAsymmErrors, TFile, TH1D, TCanvas, gROOT, TChain, gStyle

gROOT.SetBatch()
gROOT.SetStyle('Plain')

gStyle.SetLabelSize (0.04, "X")
gStyle.SetLabelSize (0.04, "Y")
gStyle.SetTitleSize (0.04, "X")
gStyle.SetTitleSize (0.04, "Y")
gStyle.SetLabelOffset (0.005, "X")
gStyle.SetLabelOffset (0.005, "Y")
gStyle.SetTitleOffset (1.0, "X")
gStyle.SetTitleOffset (1.0, "Y")
gStyle.SetNdivisions (505, "X")
gStyle.SetNdivisions (505, "Y")
gStyle.SetPadTickX (1)
gStyle.SetPadTickY (1)
gStyle.SetMarkerSize (1.5)

canvas = TCanvas("c1", "c1", 800, 800)

fWeights = TFile(os.environ["CMSSW_BASE"] + '/src/DisappTrks/StandardAnalysis/data/isrWeight_disappTrks_run2.root', 'read')
h_1 = fWeights.Get('SingleMu_2017')
h_2 = fWeights.Get('madgraphOverPythia8_94X')

h_product = h_1.Clone('h_product')
for i in range(0, h_product.GetNbinsX()):
	h_product.SetBinContent(i+1, h_product.GetBinContent(i+1) * h_2.GetBinContent(h_2.FindBin(h_product.GetBinLowEdge(i+1))))

chain4 = TChain('disTrkSelectionSmearedJetsNLayers4TreeMaker/Tree')
chain5 = TChain('disTrkSelectionSmearedJetsNLayers5TreeMaker/Tree')
chain6 = TChain('disTrkSelectionSmearedJetsNLayers6plusTreeMaker/Tree')

chain4.Add('condor/2017/signalAcceptance_full_v8/AMSB_chargino_700GeV_100cm_94X/hist_*.root')
chain5.Add('condor/2017/signalAcceptance_full_v8/AMSB_chargino_700GeV_100cm_94X/hist_*.root')
chain6.Add('condor/2017/signalAcceptance_full_v8/AMSB_chargino_700GeV_100cm_94X/hist_*.root')

h_isr_4 = TH1D('isr_4', 'isr_4', 50, 0, 500)
h_isr_5 = TH1D('isr_5', 'isr_5', 50, 0, 500)
h_isr_6 = TH1D('isr_6', 'isr_6', 50, 0, 500)

for x in chain4:
	h_isr_4.Fill(x.eventvariable_isrPt)
for x in chain5:
	h_isr_5.Fill(x.eventvariable_isrPt)
for x in chain6:
	h_isr_6.Fill(x.eventvariable_isrPt)

h_isr_6.Scale(1. / 10.)
h_isr_6.SetFillStyle(3001)
h_isr_6.SetFillColor(8)
h_isr_6.SetLineColor(1)

h_product.SetLineColor(1)
h_product.SetMarkerStyle(20)
h_product.SetMarkerColor(1)
h_product.GetYaxis().SetRangeUser(0, 5)
h_product.GetYaxis().SetTitle('ISR weight or arbitrary norm.')

h_product.Draw()

if False:
	fNoCuts = TFile('condor/2017/signalAcceptance_noCuts/AMSB_chargino_800GeV_10cm_94X.root')
	hNoCuts = fNoCuts.Get('NoCutsPlotter/Eventvariable Plots/isrPt')
	hNoCuts.Rebin(10)
	hNoCuts.Scale(1. / 25. / 80.)
	hNoCuts.SetFillStyle(3001)
	hNoCuts.SetFillColor(8)
	hNoCuts.SetLineColor(1)
	hNoCuts.Draw('hist same')
else:
	h_isr_6.Draw('hist same')

h_product.Draw('same')

canvas.SaveAs('ay.C')