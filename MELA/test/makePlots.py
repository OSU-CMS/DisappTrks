#!/usr/bin/env python

from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *

from ROOT import TFile, TH1D, TH2D, TPaveText, TLegend, TLatex, TString

gROOT.SetBatch() # I am Groot.

dirs = getUser()
canvas = TCanvas("c1", "c1", 10, 10, 800, 800)
#setCanvasStyle(canvas)

nLayersWords = ["NLayers4", "NLayers5", "NLayers6plus"]

lumiString = str(round(lumi['MET_2017'] / 1000.0, 2)) + ' + ' + str(round(lumi['MET_2018'] / 1000.0, 2)) + ' fb^{-1} 13 TeV'
yearString = '20178'

drawSignal = False

def normToObs(obs, h):
	if h.Integral() > 0:
		h.Scale(obs.Integral() / h.Integral())

prelim = TLatex()
prelim.SetNDC()
prelim.SetTextAngle(0)
prelim.SetTextFont(62)
prelim.SetTextAlign(12)
prelim.SetTextSize(0.04)

run = TLatex()
run.SetNDC()
run.SetTextAngle(0)
run.SetTextFont(42)
run.SetTextAlign(32)
run.SetTextSize(0.035)

for nLayersWord in nLayersWords:
 	observation = TFile('observationPdf_' + nLayersWord + '.root', 'read')
 	fake = TFile('fakePdf_' + nLayersWord + '.root', 'read')
 	signal = TFile('signalPdfs_' + nLayersWord + '.root', 'read')

	observation2018 = TFile('2018/observationPdf_' + nLayersWord + '.root', 'read')
	fake2018 = TFile('2018/fakePdf_' + nLayersWord + '.root', 'read')
	signal2018 = TFile('2018/signalPdfs_' + nLayersWord + '.root', 'read')

 	dedx_obs = observation.Get('pixelHits')
 	dedx_fake = fake.Get('pixelHits')
 	dedx_signal = signal.Get('AMSB_chargino_700GeV_100cm_94X')

	dedx_obs.Add(observation2018.Get('pixelHits'))
	dedx_fake.Add(fake2018.Get('pixelHits'))
	dedx_signal.Add(signal2018.Get('AMSB_chargino_700GeV_100cm_102X'), -1.0)

 	dedx_obs_noBigClusters = observation.Get('pixelHits_noBigClusters')
 	dedx_fake_noBigClusters = fake.Get('pixelHits_noBigClusters')

	dedx_obs_noBigClusters.Add(observation2018.Get('pixelHits_noBigClusters'))
	dedx_fake_noBigClusters.Add(fake2018.Get('pixelHits_noBigClusters'))

 	dedx_obs_0 = observation.Get('pixelHits_hit0')
 	dedx_fake_0 = fake.Get('pixelHits_hit0')

	dedx_obs_0.Add(observation2018.Get('pixelHits_hit0'))
	dedx_fake_0.Add(fake2018.Get('pixelHits_hit0'))

	dedx_obs_1 = observation.Get('pixelHits_hit1')
 	dedx_fake_1 = fake.Get('pixelHits_hit1')

	dedx_obs_1.Add(observation2018.Get('pixelHits_hit1'))
	dedx_fake_1.Add(fake2018.Get('pixelHits_hit1'))

 	dedx_obs_2 = observation.Get('pixelHits_hit2')
 	dedx_fake_2 = fake.Get('pixelHits_hit2')

	dedx_obs_2.Add(observation2018.Get('pixelHits_hit2'))
	dedx_fake_2.Add(fake2018.Get('pixelHits_hit2'))

	dedx_obs_3 = observation.Get('pixelHits_hit3')
 	dedx_fake_3 = fake.Get('pixelHits_hit3')

	dedx_obs_3.Add(observation2018.Get('pixelHits_hit3'))
	dedx_fake_3.Add(fake2018.Get('pixelHits_hit3'))

 	nOver5_obs = observation.Get('nOver5')
 	nOver5_fake = fake.Get('nOver5')
 	nOver5_signal = signal.Get('AMSB_chargino_700GeV_100cm_94X_nOver5')

	nOver5_obs.Add(observation2018.Get('nOver5'))
	nOver5_fake.Add(fake2018.Get('nOver5'))
	nOver5_signal.Add(signal2018.Get('AMSB_chargino_700GeV_100cm_102X_nOver5'), -1.0)

 	pixelSize_obs = observation.Get('pixelSize')
 	pixelSize_fake = fake.Get('pixelSize')
 	pixelSize_signal = signal.Get('AMSB_chargino_700GeV_100cm_94X_pixelSize')

	pixelSize_obs.Add(observation2018.Get('pixelSize'))
	pixelSize_fake.Add(fake2018.Get('pixelSize'))
	pixelSize_signal.Add(signal2018.Get('AMSB_chargino_700GeV_100cm_102X_pixelSize'))

 	##############################################################

 	dedx_obs.Rebin(5)
 	dedx_fake.Rebin(5)
 	dedx_signal.Rebin(5)
 	normToObs(dedx_obs, dedx_fake)
 	normToObs(dedx_obs, dedx_signal)

 	dedx_obs_noBigClusters.Rebin(5)
 	dedx_fake_noBigClusters.Rebin(5)
 	normToObs(dedx_obs_noBigClusters, dedx_fake_noBigClusters)

 	dedx_obs_0.Rebin(5)
 	dedx_fake_0.Rebin(5)
	normToObs(dedx_obs_0, dedx_fake_0)

 	dedx_obs_1.Rebin(5)
 	dedx_fake_1.Rebin(5)
	normToObs(dedx_obs_1, dedx_fake_1)

  	dedx_obs_2.Rebin(5)
 	dedx_fake_2.Rebin(5)
 	normToObs(dedx_obs_2, dedx_fake_2)

 	dedx_obs_3.Rebin(5)
 	dedx_fake_3.Rebin(5)
 	normToObs(dedx_obs_3, dedx_fake_3)

 	normToObs(nOver5_obs, nOver5_fake)
 	normToObs(nOver5_obs, nOver5_signal)

 	normToObs(pixelSize_obs, pixelSize_fake)
 	normToObs(pixelSize_obs, pixelSize_signal)

 	##############################################################

	# durp
	#leg = TLegend (0.413534, 0.729328, 0.794486, 0.815891)
	leg = TLegend (0.313534, 0.729328, 0.694486, 0.815891)
	leg.SetBorderSize(0)
	leg.SetFillStyle(0)
	leg.SetTextFont(42)
	#leg.SetTextSize(0.0387597)
	leg.SetTextSize(0.025)
	leg.AddEntry(dedx_obs,  "Observation", "pe")
	leg.AddEntry(dedx_fake, "Fake track estimate", "l")
	if drawSignal:
		leg.AddEntry(dedx_signal, "AMSB chargino (700 GeV, c#tau = 100 cm)", "l")

	legHits = TLegend (0.413534, 0.729328, 0.794486, 0.815891, "Pixel hit number")
	legHits.SetBorderSize(0)
	legHits.SetFillStyle(0)
	legHits.SetTextFont(42)
	legHits.SetTextSize(0.0387597)
	legHits.AddEntry(dedx_fake_0,  "1st", "l")
	legHits.AddEntry(dedx_fake_1,  "2nd", "l")
	legHits.AddEntry(dedx_fake_2,  "3rd", "l")
	legHits.AddEntry(dedx_fake_3,  "4th", "l")

	# durp
	#ks = TPaveText(0.421053, 0.824289, 0.820802, 0.872093, "brNDC")
	ks = TPaveText(0.351053, 0.824289, 0.750802, 0.872093, "brNDC")
	ks.SetBorderSize(0)
	ks.SetFillStyle(0)
	ks.SetTextFont(42)
	#ks.SetTextSize(0.0387597)
	ks.SetTextSize(0.03)

 	##############################################################

	setStyle(dedx_obs)
 	setStyle(dedx_fake, 600)
 	setStyle(dedx_signal, 632)
	dedx_fake.GetXaxis().SetRangeUser(0, 25)
	dedx_fake.GetXaxis().SetTitle('Hit dE/dx measurement [MeV/cm]')
	dedx_fake.GetXaxis().SetTitleSize(0.04)
	dedx_fake.GetXaxis().SetLabelSize(0.04)
	dedx_fake.GetYaxis().SetTitle('Number of hits (normalized to observation)')
	dedx_fake.GetYaxis().SetTitleSize(0.04)
	dedx_fake.GetYaxis().SetLabelSize(0.04)

 	dedx_fake.Draw('hist')
 	if drawSignal:
 		dedx_signal.Draw('hist same')
 	dedx_obs.Draw('e1 same')
	ks.Clear()
	ks.AddText("KS test (obs, fake) p-value: " + str (round (dedx_obs.KolmogorovTest (dedx_fake), 3)))
	ks.Draw('same')
	leg.Draw('same')
	prelim.DrawLatex(0.105, 0.925, 'CMS Preliminary')
	run.DrawLatex(0.9, 0.93, lumiString)
 	canvas.SaveAs('dedx_' + yearString + '_' + nLayersWord + '.pdf')
 	canvas.SaveAs('dedx_' + yearString + '_' + nLayersWord + '.C')

 	##############################################################

	setStyle(dedx_obs_noBigClusters)
 	setStyle(dedx_fake_noBigClusters, 600)
	dedx_fake_noBigClusters.GetXaxis().SetRangeUser(0, 25)
	dedx_fake_noBigClusters.GetXaxis().SetTitle('Hit dE/dx measurement [MeV/cm]')
	dedx_fake_noBigClusters.GetXaxis().SetTitleSize(0.04)
	dedx_fake_noBigClusters.GetXaxis().SetLabelSize(0.04)
	dedx_fake_noBigClusters.GetYaxis().SetTitle('Number of hits (normalized to observation)')
	dedx_fake_noBigClusters.GetYaxis().SetTitleSize(0.04)
	dedx_fake_noBigClusters.GetYaxis().SetLabelSize(0.04)

 	dedx_fake_noBigClusters.Draw('hist')
 	dedx_obs_noBigClusters.Draw('e1 same')
	ks.Clear()
	ks.AddText("KS test p-value: " + str (round (dedx_obs_noBigClusters.KolmogorovTest (dedx_fake_noBigClusters), 3)))
	ks.Draw('same')
	leg.Draw('same')
	prelim.DrawLatex(0.105, 0.925, 'CMS Preliminary')
	run.DrawLatex(0.9, 0.93, lumiString)
 	canvas.SaveAs('dedx_noBigClusters_' + yearString + '_' + nLayersWord + '.pdf')
 	canvas.SaveAs('dedx_noBigClusters_' + yearString + '_' + nLayersWord + '.C')

 	##############################################################

	setStyle(dedx_obs_0)
 	setStyle(dedx_fake_0, 600)
	dedx_fake_0.GetXaxis().SetRangeUser(0, 25)
	dedx_fake_0.GetXaxis().SetTitle('Hit dE/dx measurement (1st hit only) [MeV/cm]')
	dedx_fake_0.GetXaxis().SetTitleSize(0.04)
	dedx_fake_0.GetXaxis().SetLabelSize(0.04)
	dedx_fake_0.GetYaxis().SetTitle('Number of hits (normalized to observation)')
	dedx_fake_0.GetYaxis().SetTitleSize(0.04)
	dedx_fake_0.GetYaxis().SetLabelSize(0.04)

 	dedx_fake_0.Draw('hist')
 	dedx_obs_0.Draw('e1 same')
 	ks.Clear()
	ks.AddText("KS test p-value: " + str (round (dedx_obs_0.KolmogorovTest (dedx_fake_0), 3)))
	ks.Draw('same')
	leg.Draw('same')
	prelim.DrawLatex(0.105, 0.925, 'CMS Preliminary')
	run.DrawLatex(0.9, 0.93, lumiString)
 	canvas.SaveAs('dedx_hit0_' + yearString + '_' + nLayersWord + '.pdf')
 	canvas.SaveAs('dedx_hit0_' + yearString + '_' + nLayersWord + '.C')

 	##############################################################

	setStyle(dedx_obs_1)
 	setStyle(dedx_fake_1, 600)
	dedx_fake_1.GetXaxis().SetRangeUser(0, 25)
	dedx_fake_1.GetXaxis().SetTitle('Hit dE/dx measurement (2nd hit only) [MeV/cm]')
	dedx_fake_1.GetXaxis().SetTitleSize(0.04)
	dedx_fake_1.GetXaxis().SetLabelSize(0.04)
	dedx_fake_1.GetYaxis().SetTitle('Number of hits (normalized to observation)')
	dedx_fake_1.GetYaxis().SetTitleSize(0.04)
	dedx_fake_1.GetYaxis().SetLabelSize(0.04)

 	dedx_fake_1.Draw('hist')
 	dedx_obs_1.Draw('e1 same')
 	ks.Clear()
	ks.AddText("KS test p-value: " + str (round (dedx_obs_1.KolmogorovTest (dedx_fake_1), 3)))
	ks.Draw('same')
	leg.Draw('same')
	prelim.DrawLatex(0.105, 0.925, 'CMS Preliminary')
	run.DrawLatex(0.9, 0.93, lumiString)
 	canvas.SaveAs('dedx_hit1_' + yearString + '_' + nLayersWord + '.pdf')
 	canvas.SaveAs('dedx_hit1_' + yearString + '_' + nLayersWord + '.C')

 	##############################################################

	setStyle(dedx_obs_2)
 	setStyle(dedx_fake_2, 600)
	dedx_fake_2.GetXaxis().SetRangeUser(0, 25)
	dedx_fake_2.GetXaxis().SetTitle('Hit dE/dx measurement (3rd hit only) [MeV/cm]')
	dedx_fake_2.GetXaxis().SetTitleSize(0.04)
	dedx_fake_2.GetXaxis().SetLabelSize(0.04)
	dedx_fake_2.GetYaxis().SetTitle('Number of hits (normalized to observation)')
	dedx_fake_2.GetYaxis().SetTitleSize(0.04)
	dedx_fake_2.GetYaxis().SetLabelSize(0.04)

 	dedx_fake_2.Draw('hist')
 	dedx_obs_2.Draw('e1 same')
 	ks.Clear()
	ks.AddText("KS test p-value: " + str (round (dedx_obs_2.KolmogorovTest (dedx_fake_2), 3)))
	ks.Draw('same')
	leg.Draw('same')
	prelim.DrawLatex(0.105, 0.925, 'CMS Preliminary')
	run.DrawLatex(0.9, 0.93, lumiString)
 	canvas.SaveAs('dedx_hit2_' + yearString + '_' + nLayersWord + '.pdf')
 	canvas.SaveAs('dedx_hit2_' + yearString + '_' + nLayersWord + '.C')

 	##############################################################

	setStyle(dedx_obs_3)
 	setStyle(dedx_fake_3, 600)
	dedx_fake_3.GetXaxis().SetRangeUser(0, 25)
	dedx_fake_3.GetXaxis().SetTitle('Hit dE/dx measurement (4th hit only) [MeV/cm]')
	dedx_fake_3.GetXaxis().SetTitleSize(0.04)
	dedx_fake_3.GetXaxis().SetLabelSize(0.04)
	dedx_fake_3.GetYaxis().SetTitle('Number of hits (normalized to observation)')
	dedx_fake_3.GetYaxis().SetTitleSize(0.04)
	dedx_fake_3.GetYaxis().SetLabelSize(0.04)

 	dedx_fake_3.Draw('hist')
 	dedx_obs_3.Draw('e1 same')
 	ks.Clear()
	ks.AddText("KS test p-value: " + str (round (dedx_obs_3.KolmogorovTest (dedx_fake_3), 3)))
	ks.Draw('same')
	leg.Draw('same')
	prelim.DrawLatex(0.105, 0.925, 'CMS Preliminary')
	run.DrawLatex(0.9, 0.93, lumiString)
 	canvas.SaveAs('dedx_hit3_' + yearString + '_' + nLayersWord + '.pdf')
 	canvas.SaveAs('dedx_hit3_' + yearString + '_' + nLayersWord + '.C')

 	############################################################## 	

  	setStyle(nOver5_obs)
 	setStyle(nOver5_fake, 600)
 	setStyle(nOver5_signal, 632)
	nOver5_fake.GetXaxis().SetRangeUser(0, 5)
	nOver5_fake.GetXaxis().SetTitle('Number of hits > 5 MeV/cm')
	nOver5_fake.GetXaxis().SetTitleSize(0.04)
	nOver5_fake.GetXaxis().SetLabelSize(0.04)
	nOver5_fake.GetYaxis().SetTitle('Number of tracks (normalized to observation)')
	nOver5_fake.GetYaxis().SetTitleSize(0.04)
	nOver5_fake.GetYaxis().SetLabelSize(0.04)

 	nOver5_fake.Draw('hist')
 	if drawSignal:
 		nOver5_signal.Draw('hist same')
 	nOver5_obs.Draw('e1 same')
 	ks.Clear()
 	ks.AddText("KS test p-value: " + str (round (nOver5_obs.KolmogorovTest (nOver5_fake), 3)))
 	ks.Draw('same')
 	leg.Draw('same')
	prelim.DrawLatex(0.105, 0.925, 'CMS Preliminary')
	run.DrawLatex(0.9, 0.93, lumiString)
 	canvas.SaveAs('nOver5_' + yearString + '_' + nLayersWord + '.pdf')
 	canvas.SaveAs('nOver5_' + yearString + '_' + nLayersWord + '.C')

 	##############################################################

 	setStyle(pixelSize_obs)
 	setStyle(pixelSize_fake, 600)
 	setStyle(pixelSize_signal, 632)
	pixelSize_fake.GetXaxis().SetRangeUser(0, 50)
	pixelSize_fake.GetXaxis().SetTitle('Pixel cluster size')
	pixelSize_fake.GetXaxis().SetTitleSize(0.04)
	pixelSize_fake.GetXaxis().SetLabelSize(0.04)
	pixelSize_fake.GetYaxis().SetTitle('Number of clusters (normalized to observation)')
	pixelSize_fake.GetYaxis().SetTitleSize(0.04)
	pixelSize_fake.GetYaxis().SetLabelSize(0.04)

 	canvas.SetLogy(True)
 	pixelSize_fake.Draw('hist')
 	if drawSignal:
 		pixelSize_signal.Draw('hist same')
 	pixelSize_obs.Draw('e1 same')
 	ks.Clear()
 	ks.AddText("KS test p-value: " + str (round (pixelSize_obs.KolmogorovTest (pixelSize_fake), 3)))
 	ks.Draw('same')
 	leg.Draw('same')
	prelim.DrawLatex(0.105, 0.925, 'CMS Preliminary')
	run.DrawLatex(0.9, 0.93, lumiString)
 	canvas.SaveAs('pixelSize_' + yearString + '_' + nLayersWord + '.pdf')
 	canvas.SaveAs('pixelSize_' + yearString + '_' + nLayersWord + '.C')
 	canvas.SetLogy(False)

 	##############################################################

 	observation.Close()
 	fake.Close()
 	signal.Close()
