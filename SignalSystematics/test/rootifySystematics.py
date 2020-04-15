#!/usr/bin/env python

from array import array
from ROOT import TFile, TH2D

lifetimes = ['0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1',
			 '2', '3', '4', '5', '6', '7', '8', '9', '10',
             '20', '30', '40', '50', '60', '70', '80', '90', '100',
             '200', '300', '400', '500', '600', '700', '800', '900', '1000',
             '2000', '3000', '4000', '5000', '6000', '7000', '8000', '9000', '10000']

def createHistogram(isWino, name):
	masses = ['100', '200', '300', '400', '500', '600', '700', '800', '900']
	if isWino:
		masses.extend(['1000', '1100'])
	xBin = [float(a) for a in masses]
	yBin = [float(a) for a in lifetimes]
	xBin.sort()
	yBin.sort()
	# Add an additional bin boundary, so that the last bin has equal witdth to the second to last bin
	xBin.append(xBin[-1] + (xBin[-1] - xBin[-2])) 
	yBin.append(yBin[-1] + (yBin[-1] - yBin[-2])) 
	# Offset the xaxis bins so that mass values are in center of each bin
	xBinHalfWidth = (xBin[1] - xBin[0]) / 2
	for i in range(0, len(xBin)):
	    xBin[i] -= xBinHalfWidth
	xBinArray = array('d', xBin)
	yBinArray = array('d', yBin)
	h = TH2D(name, name, len(xBin) - 1, xBinArray, len(yBin) - 1, yBinArray)
	h.GetXaxis().SetTitle('Chargino mass [GeV]')
	h.GetYaxis().SetTitle('Chargino lifetime [cm]')
	return h

systNames = [
    'isr',
    'jec',
    'jer',
    'metVaryElectronEn',
    'metVaryJetEn',
    'metVaryJetRes',
    'metVaryPhotonEn',
    'metVaryTauEn',
    'metVaryUnclusteredEn',
    'nMissOut',
    'pileup',
    'trigger_grandOrWeightData',
    'trigger_grandOrWeightMC',
    'triggerTurnOn', # 2017-8
    'electronVetoScaleFactor', # 2017-8
    'L1ECALPrefiringWeight', # 2017
    'muonVetoScaleFactor', # 2017-8
]

fout = TFile('allSystematics.root', 'recreate')

for name in systNames:
	for era in ['2017', '2018']:
		for nlayers in ['NLayers4', 'NLayers5', 'NLayers6plus']:
			for isWino in [True, False]:
				h_up = createHistogram(isWino, name + ('_wino_' if isWino else '_higgsino_') + era + '_' + nlayers + '_fluctuateUp')
				h_down = createHistogram(isWino, name + ('_wino_' if isWino else '_higgsino_') + era + '_' + nlayers + '_fluctuateDown')
				try:
					fin = open('../data/systematic_values__' + ('' if isWino else 'higgsino_') + name + '_' + era + '_' + nlayers + '.txt')
				except IOError:
					print '../data/systematic_values__' + ('' if isWino else 'higgsino_') + name + '_' + era + '_' + nlayers + '.txt -- does not exist, skipping...'
					continue
				for line in fin:
					thisSample = line.split()[0]
					thisMass = float(thisSample.split('_')[-3][:-3])
					thisLifetime = float(thisSample.split('_')[-2][:-2].replace('0p', '0.'))

					systDown = float(line.split()[1]) - 1.0
					systUp = float(line.split()[2]) - 1.0

					h_down.SetBinContent(h_down.FindBin(thisMass, thisLifetime), 100.0 * systDown)
					h_up.SetBinContent(h_up.FindBin(thisMass, thisLifetime), 100.0 * systUp)

				# 1cm broken?
				for thisMass in range(100, 1200 if isWino else 1000, 100):
					h_down.SetBinContent(h_down.FindBin(thisMass, 1.0), h_down.GetBinContent(h_down.FindBin(thisMass, 10.0)))
					h_up.SetBinContent(h_up.FindBin(thisMass, 1.0), h_up.GetBinContent(h_down.FindBin(thisMass, 10.0)))

				fin.close()

				fout.cd()
				h_down.Write()
				h_up.Write()

fout.Write()
fout.Close()

