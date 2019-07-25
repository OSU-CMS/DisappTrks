import math
import sys

from ROOT import TGraphAsymmErrors, TFile, TH1D, TCanvas, gROOT, TChain

gROOT.SetBatch()

def reweightMET(chain, ratio):
    nTotal = chain.GetEntries()
    nWeighted = 0
    for x in chain:
	nWeighted += 1.0 + ratio.Eval(x.met_noMuPt)
    return (nTotal, nWeighted)

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

fEle = TFile('triggerEfficiency_SingleEle_2017.root')
fMu  = TFile('triggerEfficiency_SingleMu_2017.root')

grEle = fEle.Get('GrandOr_METPath')
grMu  = fMu.Get('GrandOr_METPath')

grRatio = TGraphAsymmErrors()

for i in range(0, 100):
	x = grMu.GetX()[i]
	if x != grEle.GetX()[i]:
		print 'WRONG X!!!!!!'
		sys.exit()

	ex_lo = grMu.GetErrorXlow(i)
	ex_hi = grMu.GetErrorXhigh(i)

	y_mu = grMu.GetY()[i]
	y_ele = grEle.GetY()[i]
	y_ratio = y_ele / y_mu - 1.0 if y_mu > 0.0 else 1.0

	ey_lo_mu = grMu.GetErrorYlow(i)
	ey_lo_ele = grEle.GetErrorYlow(i)
	if y_mu < 1.e-9 or y_ele < 1.e-9:
		ey_lo_ratio = 0.0
	else:
		ey_lo_ratio = y_ratio * math.hypot(ey_lo_mu / y_mu, ey_lo_ele / y_ele)

	ey_hi_mu = grMu.GetErrorYhigh(i)
	ey_hi_ele = grEle.GetErrorYhigh(i)
	if y_mu < 1.e-9 or y_ele < 1.e-9:
		ey_hi_ratio = 0.0
	else:
		ey_hi_ratio = y_ratio * math.hypot(ey_hi_mu / y_mu, ey_hi_ele / y_ele)

	grRatio.SetPoint(i, x, y_ratio)
	grRatio.SetPointEXlow(i, ex_lo)
	grRatio.SetPointEXhigh(i, ex_hi)
	grRatio.SetPointEYlow(i, ey_lo_ratio)
	grRatio.SetPointEYhigh(i, ey_hi_ratio)

if True:
    grRatio.SetMarkerStyle(20)
    grRatio.SetMarkerSize(1.5)
    grRatio.SetMarkerColor(1)

    grRatio.SetLineStyle(1)
    grRatio.SetLineColor(1)
    grRatio.SetLineWidth(1)

    grRatio.GetXaxis().SetLabelSize(0.04)
    grRatio.GetXaxis().SetTitleSize(0.04)
    grRatio.GetXaxis().SetTitleOffset(1.25)

    grRatio.GetYaxis().SetLabelSize(0.04)
    grRatio.GetYaxis().SetTitleSize(0.04)
    grRatio.GetYaxis().SetTitleOffset(1.5)
#    grRatio.GetYaxis().SetRangeUser(ylo, yhi)

grRatio.Draw("ALP")

fOutput = TFile('durp.root', 'recreate')
grRatio.Write('durp')
canvas.Write('canv')
fOutput.Close()

chain4 = TChain('disTrkSelectionSmearedJetsNLayers4TreeMaker/Tree')
chain5 = TChain('disTrkSelectionSmearedJetsNLayers5TreeMaker/Tree')
chain6 = TChain('disTrkSelectionSmearedJetsNLayers6plusTreeMaker/Tree')

chain4.Add('condor/2017/signalAcceptance_full_v8/AMSB_chargino_700GeV_100cm_94X/hist_*.root')
chain5.Add('condor/2017/signalAcceptance_full_v8/AMSB_chargino_700GeV_100cm_94X/hist_*.root')
chain6.Add('condor/2017/signalAcceptance_full_v8/AMSB_chargino_700GeV_100cm_94X/hist_*.root')

(n4, w4) = reweightMET(chain4, grRatio)
(n5, w5) = reweightMET(chain5, grRatio)
(n6, w6) = reweightMET(chain6, grRatio)

print
print 'Reweighted NLayers4 =', w4/n4
print 'Reweighted NLayers5 =', w5/n5
print 'Reweighted NLayers6plus =', w6/n6

