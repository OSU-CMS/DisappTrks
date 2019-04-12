import sys
from ROOT import TFile,	TCanvas, TGraph, TLegend, gROOT

if len(sys.argv) < 2:
	print
	print 'Usage: python makeComparisonPlots.py ${SUFFIX}'
	print
	sys.exit(1)

gROOT.SetBatch()

suffix = sys.argv[1]

fCombined = TFile('limits/limits_2017_all_' + suffix + '/limit_plots.root')
fNLayers4 = TFile('limits/limits_2017_NLayers4_' + suffix + '/limit_plots.root')
fNLayers5 = TFile('limits/limits_2017_NLayers5_' + suffix + '/limit_plots.root')
fNLayers6plus = TFile('limits/limits_2017_NLayers6plus_' + suffix + '/limit_plots.root')

if not fCombined.IsOpen() or not fNLayers4.IsOpen() or not fNLayers5.IsOpen() or not fNLayers6plus.IsOpen():
	print
	print 'An input file is missing. Have you run makeLimitPlots.py for all inputs?'
	print
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
leg.AddEntry(gr_combined, 'Combined categories', 'L')
leg.AddEntry(gr_NLayers4, 'n_{layers} = 4', 'L')
leg.AddEntry(gr_NLayers5, 'n_{layers} = 5', 'L')
leg.AddEntry(gr_NLayers6plus, 'n_{layers} #geq 6', 'L')

leg.Draw('same')

can.SaveAs('limitsLifetimeVsMassCompareNLayers.pdf')
can.SaveAs('limitsLifetimeVsMassCompareNLayers.C')
print 'Created limitsLifetimeVsMassCompareNLayers.pdf'

fNLayers4.Close()
fNLayers5.Close()
fNLayers6plus.Close()

f20156 = TFile('limits/limits_all20156_' + suffix + '/limit_plots.root')
fRun2 = TFile('limits/limits_run2_' + suffix + '/limit_plots.root')

if not f20156.IsOpen() or not fRun2.IsOpen():
	print
	print 'An input file is missing. Have you run makeLimitPlots.py for all inputs?'
	print
	sys.exit(1)

can = fRun2.Get('lifetime_vs_mass')
can.Draw()

gr_20156 = f20156.Get('lifetime_vs_mass_graph_expected')
gr_run2 = fRun2.Get('lifetime_vs_mass_graph_expected')

gr_20156.SetLineColor(600) # kBlue
gr_combined.SetLineColor(632) # kRed

leg.Clear()
leg.AddEntry(gr_run2, '2015 + 2016 + 2017', 'L')
leg.AddEntry(gr_20156, '2015 + 2016', 'L')
leg.AddEntry(gr_combined, '2017', 'L')

can.Draw()
gr_20156.Draw('L same')
gr_combined.Draw('L same')
leg.Draw('same')

can.SaveAs('limitsLifetimeVsMassCombinedRun2CompareYears.pdf')
can.SaveAs('limitsLifetimeVsMassCombinedRun2CompareYears.C')
print 'Created limitsLifetimeVsMassCombinedRun2CompareYears.pdf'

