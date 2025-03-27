#!/usr/bin/env python3

import sys
from ROOT import TFile,	TCanvas, TGraph, TLegend, gROOT

def printSpecificLimits(era):
	fin = TFile('limits/limits_' + era + '_' + sys.argv[1] + '/limit_plots.root')
	grObs = fin.Get('lifetime_vs_mass_graph_observed')
	grExp = fin.Get('lifetime_vs_mass_graph_expected')
	grObsRotated = TGraph(grObs.GetN(), grObs.GetY(), grObs.GetX())
	grExpRotated = TGraph(grExp.GetN(), grExp.GetY(), grExp.GetX())
	taus = [7, 3, 0.2, 0.05]
	print ('--------------------')
	print ('For era:', era)
	print ('Observed =', ', '.join([str(grObsRotated.Eval(tau)) + ' GeV (' + str(tau) + ' ns)' for tau in taus]))
	print ('Expected =', ', '.join([str(grExpRotated.Eval(tau)) + ' GeV (' + str(tau) + ' ns)' for tau in taus]))
	print ('--------------------')

def compareNLayersBins(year):
	fCombined = TFile('limits/limits_' + year + '_all_' + suffix + '/limit_plots.root')
	fNLayers4 = TFile('limits/limits_' + year + '_NLayers4_' + suffix + '/limit_plots.root')
	fNLayers5 = TFile('limits/limits_' + year + '_NLayers5_' + suffix + '/limit_plots.root')
	fNLayers6plus = TFile('limits/limits_' + year + '_NLayers6plus_' + suffix + '/limit_plots.root')

	if not fCombined.IsOpen() or not fNLayers4.IsOpen() or not fNLayers5.IsOpen() or not fNLayers6plus.IsOpen():
		print()
		print ('An input file is missing. Have you run makeLimitPlots.py for all inputs?')
		print()
		sys.exit(1)

	gr_combined = fCombined.Get('lifetime_vs_mass_graph_expected')
	gr_NLayers4 = fNLayers4.Get('lifetime_vs_mass_graph_expected')
	gr_NLayers5 = fNLayers5.Get('lifetime_vs_mass_graph_expected')
	gr_NLayers6plus = fNLayers6plus.Get('lifetime_vs_mass_graph_expected')

	gr_NLayers4.SetLineColor(632) # kRed
	gr_NLayers5.SetLineColor(8) # a lovely shade of green
	gr_NLayers6plus.SetLineColor(600) # kBlue

	can = fCombined.Get('lifetime_vs_mass')
	can.Draw()

	gr_NLayers4.Draw('same L')
	gr_NLayers5.Draw('same L')
	gr_NLayers6plus.Draw('same L')

	# 0.180451,0.352067,0.538847,0.482558

	leg = TLegend(0.582707, 0.151515, 0.934837, 0.297258, '', 'brNDC')
	leg.AddEntry(gr_combined, 'Combined categories (' + year + ')', 'L')
	leg.AddEntry(gr_NLayers4, 'n_{layers} = 4', 'L')
	leg.AddEntry(gr_NLayers5, 'n_{layers} = 5', 'L')
	leg.AddEntry(gr_NLayers6plus, 'n_{layers} #geq 6', 'L')

	leg.Draw('same')

	can.SaveAs('limitsLifetimeVsMassCompareNLayers_' + year + '.pdf')
	can.SaveAs('limitsLifetimeVsMassCompareNLayers_' + year + '.C')
	print ('Created limitsLifetimeVsMassCompareNLayers_' + year + '.pdf')

	fNLayers4.Close()
	fNLayers5.Close()
	fNLayers6plus.Close()

if len(sys.argv) < 2:
	print()
	print ('Usage: python makeComparisonPlots.py ${SUFFIX}')
	print()
	sys.exit(1)

gROOT.SetBatch()

suffix = sys.argv[1]

compareNLayersBins('2017')
compareNLayersBins('2018AB')
compareNLayersBins('2018CD')

f20156 = TFile('limits/limits_all20156_' + suffix + '/limit_plots.root')
f2017 = TFile('limits/limits_2017_all_' + suffix + '/limit_plots.root')
f2018 = TFile('limits/limits_2018_all_' + suffix + '/limit_plots.root')
fRun2 = TFile('limits/limits_run2_' + suffix + '/limit_plots.root')

if not f20156.IsOpen() or not f2017.IsOpen() or not f2018.IsOpen() or not fRun2.IsOpen():
	print()
	print ('An input file is missing. Have you run makeLimitPlots.py for all inputs?')
	print()
	sys.exit(1)

can = fRun2.Get('lifetime_vs_mass')
can.Draw()

gr_20156 = f20156.Get('lifetime_vs_mass_graph_expected')
gr_2017 = f2017.Get('lifetime_vs_mass_graph_expected')
gr_2018 = f2018.Get('lifetime_vs_mass_graph_expected')
gr_run2 = fRun2.Get('lifetime_vs_mass_graph_expected')

gr_20156.SetLineColor(616) # kGreen
gr_2017.SetLineColor(632) # kRed
gr_2018.SetLineColor(600) # kBlue

leg = TLegend(0.582707, 0.151515, 0.934837, 0.297258, '', 'brNDC')
leg.AddEntry(gr_run2, 'Run 2', 'L')
leg.AddEntry(gr_20156, '2015-6', 'L')
leg.AddEntry(gr_2017, '2017', 'L')
leg.AddEntry(gr_2018, '2018', 'L')

can.Draw()
gr_20156.Draw('L same')
gr_2017.Draw('L same')
gr_2018.Draw('L same')
leg.Draw('same')

can.SaveAs('limitsLifetimeVsMassCombinedRun2CompareYears.pdf')
can.SaveAs('limitsLifetimeVsMassCombinedRun2CompareYears.C')
print ('Created limitsLifetimeVsMassCombinedRun2CompareYears.pdf')

printSpecificLimits('all20178')
printSpecificLimits('run2')
