#!/usr/bin/env python

import os
import math

from OSUT3Analysis.Configuration.Measurement import Measurement
from OSUT3Analysis.Configuration.ProgressIndicator import ProgressIndicator
from DisappTrks.StandardAnalysis.plotUtilities import *

from ROOT import TChain

import numpy as np
from scipy.stats import binom

setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

def getExtraSamples(suffix):
    masses = range(100, 1200 if (suffix == '94X' or suffix == '102X') else 1000, 100)
    ctaus = [1, 10, 100, 1000, 10000]
    extraSamples = { 'AMSB_chargino_{0}GeV_{1}cm_'.format(mass, ctau) + suffix : [] for mass in masses for ctau in ctaus }

    for sample in extraSamples:
        if not re.match (r'AMSB_chargino_[^_]*GeV_[^_]*cm_.*', sample):
            continue
        mass = re.sub (r'AMSB_chargino_([^_]*)GeV_[^_]*cm_.*', r'\1', sample)
        ctau0 = float (re.sub (r'AMSB_chargino_[^_]*GeV_([^_]*)cm_.*', r'\1', sample))
        suffix = re.sub (r'AMSB_chargino_[^_]*GeV_[^_]*cm_(.*)', r'\1', sample)
        for i in range (2, 10):
            ctau = ctauP = 0.1 * i * ctau0
            if int (ctau) * 10 == int (ctau * 10):
                ctau = ctauP = str (int (ctau))
            else:
                ctau = ctauP = str (ctau)
                ctauP = re.sub (r'\.', r'p', ctau)
            dataset = 'AMSB_chargino_' + mass + 'GeV_' + ctauP + 'cm_' + suffix

            extraSamples[sample].append (dataset)

    return extraSamples

class LikelihoodEstimator:
    _variables = []
    _weights = []
    _signalHypotheses = {}
    _backgroundHypothesis = {}
    _nLayersWord = ''

    def __init__(self, nLayersWord):
        self._weights = [
            'eventvariable_lifetimeWeight',
            'eventvariable_isrWeight',
            'eventvariable_grandOrWeight',
            'eventvariable_puScalingFactor',
        ]
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_9_4_"):
            self._weights.append('eventvariable_L1ECALPrefiringWeight')
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_10_2_"):
            self._weightsCentral.append('eventvariable_hem1516weight')
        self._nLayersWord = nLayersWord

    def addSignal(self, sample, channelName, condorDir, mass, ctau):
        self._signalHypotheses[sample] = {
            'mass' : mass,
            'ctau' : ctau,
            'chain' : TChain(channelName + 'TreeMaker/Tree'),
            'cutCharge' : -1,
            'nHitsPass' : 0,
        }

        self._signalHypotheses[sample]['chain'].Add('condor/' + condorDir + '/' + sample + '/hist_*.root')
        print 'Added entries for ' + channelName + ': ' + str(self._signalHypotheses[sample]['chain'].GetEntries())

    def addData(self, sample, channelName, condorDir):
        self._observationFile = TFile('condor/' + condorDir + '/' + sample + '.root')
        self._observation = self._observationFile.Get(channelName + 'TreeMaker/Tree')
        print 'Added entries for ' + channelName + ': ' + str(self._observation.GetEntries())

    def getEfficiencyGrid(self, sample, hitsPdf):
        eff = TH2D(sample + '_eff', sample + '_eff', 1000, 0, 100, 5, 0, 5)
        eff.Sumw2()
        eff.SetDirectory(0)
        for ix in range(hitsPdf.GetNbinsX()):
            chargeEfficiency = float(hitsPdf.Integral(ix+1, -1)) # already normalized
            for iy in range(5):
                p = binom.sf(iy-1, 4, chargeEfficiency) # 1 - cdf
                eff.SetBinContent(ix+1, iy+1, p)
        return eff

    def constructSignalPdfs(self):
        print
        print 'Constructing signal pdfs...'
        fout = TFile('signalPdfs_' + self._nLayersWord + '.root', 'recreate')
        for sample in self._signalHypotheses:
            pixelHits = TH1D(sample, sample, 1000, 0, 100)
            pixelHits.Sumw2()
            pixelHits.SetDirectory(0)

            eff = TH2D(sample + '_eff', sample + '_eff', 1000, 0, 100, 5, 0, 5)
            eff.Sumw2()
            eff.SetDirectory(0)

            nplot = TH1D(sample + '_nOver5', sample + '_nOver5', 10, 0, 10)

            for event in self._signalHypotheses[sample]['chain']:
                hitCharges = [getattr(event, 'eventvariable_hitCharge_0_%d' % i) for i in range(20)]
                hitIsPixel = [getattr(event, 'eventvariable_hitIsPixel_0_%d' % i) for i in range(20)]
                w = 1.0
                for weight in self._weights:
                    w *= getattr(event, weight)
                nOver5 = 0
                for i in range(20):
                    if hitIsPixel[i]:
                        pixelHits.Fill(hitCharges[i], w)
                        if hitCharges[i] > 5:
                            nOver5 += 1
                nplot.Fill(nOver5, w)
                # efficiency for having nHits>=iy with charge > ix/100
                """
                for ix in range(1000):
                    nHitsPass = sum(bool(hitCharges[ihit] > ix/100.0 and hitIsPixel[ihit]) for ihit in range(20))
                    for ihit in range(20):
                        if hitIsPixel[ihit] and hitCharges[ihit] > 
                    for iy in range(1, 5):
                        nHitsPass = 0
                        for ihit in range(20):

                        nHitsPass = len([hit for hit in hitCharges if hit > ix/100.0])
                """

            pixelHits.Scale(1.0 / pixelHits.Integral(1, -1))
            self._signalHypotheses[sample]['pdf'] = pixelHits
            self._signalHypotheses[sample]['efficiencyGrid'] = self.getEfficiencyGrid(sample, pixelHits)
            fout.cd()
            pixelHits.Write()
            self._signalHypotheses[sample]['efficiencyGrid'].Write()
            nplot.Write()
        print 'Created signalPdfs_' + self._nLayersWord + '.root'
        fout.Close()

    def constructDataPdf(self):
        fout = TFile('observationPdf_' + self._nLayersWord + '.root', 'recreate')
        
        pixelHits = TH1D('pixelHits', 'pixelHits', 1000, 0, 100)
        pixelHits.Sumw2()
        pixelHits.SetDirectory(0)

        nplot = TH1D('nOver5', 'nOver5;number of pixel hits (> 5 MeV/cm)', 10, 0, 10)
        nplot.SetDirectory(0)

        pixSize = TH1D('pixelSize', 'pixelSize', 100, 0, 100)
        pixSizeX = TH1D('pixelSizeX', 'pixelSizeX', 100, 0, 100)
        pixSizeY = TH1D('pixelSizeY', 'pixelSizeY', 100, 0, 100)
        pixSizeYvsX = TH2D('pixelSizeYvsX', 'pixelSizeYvsX', 100, 0, 100, 100, 0, 100)
        chargeVsSize = TH2D('chargeVsSize', 'chargeVsSize;pixel cluster size;dE/dx [MeV/cm]', 100, 0, 100, 1000, 0, 100)

        sizeVsHitNumber = TH2D('sizeVsHitNumber', 'sizeVsHitNumber;hit number;pixel cluster size', 6, 0, 6, 100, 0, 100)
        chargeVsHitNumber = TH2D('chargeVsHitNumber', 'chargeVsHitNumber;hit number;dE/dx [MeV/cm]', 6, 0, 6, 100, 0, 100)

        for event in self._observation:
            hitCharges = [getattr(event, 'eventvariable_hitCharge_0_%d' % i) for i in range(20)]
            hitIsPixel = [getattr(event, 'eventvariable_hitIsPixel_0_%d' % i) for i in range(20)]
            pixelSize = [getattr(event, 'eventvariable_pixelSize_0_%d' % i) for i in range(20)]
            pixelSizeX = [getattr(event, 'eventvariable_pixelSizeX_0_%d' % i) for i in range(20)]
            pixelSizeY = [getattr(event, 'eventvariable_pixelSizeY_0_%d' % i) for i in range(20)]
            nOver5 = 0
            for i in range(20):
                if hitIsPixel[i]:
                    pixelHits.Fill(hitCharges[i])
                    chargeVsSize.Fill(pixelSize[i], hitCharges[i])
                    pixSize.Fill(pixelSize[i])
                    pixSizeX.Fill(pixelSizeX[i])
                    pixSizeY.Fill(pixelSizeY[i])
                    pixSizeYvsX.Fill(pixelSizeX[i], pixelSizeY[i])
                    if hitCharges[i] > 5:
                        nOver5 += 1
                    sizeVsHitNumber.Fill(i, pixelSize[i])
                    chargeVsHitNumber.Fill(i, hitCharges[i])
            nplot.Fill(nOver5)

        if pixelHits.Integral(1, -1) > 0:
            pixelHits.Scale(1.0 / pixelHits.Integral(1, -1))
        fout.cd()
        pixelHits.Write()
        nplot.Write()
        pixSize.Write()
        pixSizeX.Write()
        pixSizeY.Write()
        pixSizeYvsX.Write()
        chargeVsSize.Write()
        chargeVsHitNumber.Write()
        sizeVsHitNumber.Write()
        print 'Created observationPdf_' + self._nLayersWord + '.root'
        fout.Close()

    def estimateLikelihood(self):
        return

