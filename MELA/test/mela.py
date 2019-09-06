from ROOT import TFile, TChain, TTree, TH1D, TCanvas

import numpy as np
from array import array

def getMean(measurements, isPixel):
	pixelMeasurements = [measurements[i] for i in range(len(measurements)) if measurements[i] > 0 and isPixel[i] == True]
	if len(pixelMeasurements) == 0:
		return (-1, -1)
	return (np.mean(pixelMeasurements), np.std(pixelMeasurements, ddof=1))

####################################################################

h_measurements_sig = TH1D('h_measurements_sig', 'h_measurements_sig;dE/dx [MeV/cm]', 300, 0, 30)
h_mean_sig = TH1D('h_mean_sig', 'h_mean_sig;<dE/dx> [MeV/cm]', 300, 0, 30)
h_stdev_sig = TH1D('h_stdev_sig', 'h_stdev_sig;#sigma(<dE/dx>) [MeV/cm]', 300, 0, 30)
h_stdevOverMean_sig = TH1D('h_stdevOverMean_sig', 'h_stdevOverMean_sig;#sigma(<dE/dx>) / <dE/dx>', 100, 0, 10)

chain = TChain('disTrkSelectionSmearedJetsNLayers4TreeMaker/Tree')
chain.Add('condor/2017/signalAcceptance_hitInfo_v8/AMSB_chargino_1100GeV_100cm_94X/hist_*.root')

for event in chain:
	hitCharges = [getattr(event, 'eventvariable_hitCharge_0_%d' % i) for i in range(20)]
	hitIsPixel = [getattr(event, 'eventvariable_hitIsPixel_0_%d' % i) for i in range(20)]
	(mean, stdev) = getMean(hitCharges, hitIsPixel)
	if mean < 0:
		continue
	for i in range(20):
		if not hitIsPixel[i]:
			continue
		h_measurements_sig.Fill(hitCharges[i])
	h_mean_sig.Fill(mean)
	h_stdev_sig.Fill(stdev)
	h_stdevOverMean_sig.Fill(stdev / mean if mean > 0 else -1)

fout = TFile('signal.root', 'recreate')
h_measurements_sig.Write()
h_mean_sig.Write()
h_stdev_sig.Write()
h_stdevOverMean_sig.Write()
fout.Close()

####################################################################

fobs = TFile('condor/2017/signalAcceptance_hitInfo_v8/observation.root')
tobs = fobs.Get('DisTrkSelectionNLayers4TreeMaker/Tree')

h_measurements_obs  = []
h_mean_obs          = TH1D('h_mean_obs',          'h_mean_obs;<dE/dx> [MeV/cm]', 300, 0, 30)
h_meanSimple_obs    = TH1D('h_meanSimple_obs',    'h_meanSimple_obs;<dE/dx> [MeV/cm]', 300, 0, 30)
h_stdev_obs         = TH1D('h_stdev_obs',         'h_stdev_obs;<dE/dx> [MeV/cm]', 300, 0, 30)
h_stdevOverMean_obs = TH1D('h_stdevOverMean_obs', 'h_stdevOverMean_obs;<dE/dx> [MeV/cm]', 100, 0, 10)

fout_obs = TFile('observed.root', 'recreate')

for ievt, event in enumerate(tobs):
	hitCharges = [getattr(event, 'eventvariable_hitCharge_0_%d' % i) for i in range(20)]
	hitIsPixel = [getattr(event, 'eventvariable_hitIsPixel_0_%d' % i) for i in range(20)]
	(mean, stdev) = getMean(hitCharges, hitIsPixel)
	if mean < 0:
		continue
	h_measurements_obs.append(TH1D('h_measurements_obs_%d' % ievt, 'h_measurements_obs_%d;dE/dx [MeV/cm]' % ievt, 300, 0, 30))
	for i in range(20):
		if not hitIsPixel[i]:
			continue
		h_measurements_obs[-1].Fill(hitCharges[i])
	h_mean_obs.Fill(mean)
	h_stdev_obs.Fill(stdev)
	h_stdevOverMean_obs.Fill(stdev / mean if mean > 0 else -1)
	h_measurements_obs[-1].Write()

h_mean_obs.Write()
h_stdev_obs.Write()
h_stdevOverMean_obs.Write()

fout_obs.Close()

