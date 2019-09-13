#!/usr/bin/env python

import os
import math
import glob

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
    _printObservationTracks = False

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

    def addData(self, role, sample, channelName, condorDir, useTrees = False, eras = []):
        channel = {}
        if useTrees:
            channel['tree'] = TChain(channelName + 'TreeMaker/Tree')
            for era in eras:
                channel['tree'].Add('condor/' + condorDir + '/' + sample + era + '/hist_*.root')
        else:
            channel['file'] = TFile('condor/' + condorDir + '/' + sample + '.root')
            channel['tree'] = channel['file'].Get(channelName + 'TreeMaker/Tree')
        setattr(self, role, channel)
        print 'Added entries for role ' + role + ': ' + str(channel['tree'].GetEntries())

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

    def setPrintObservedTracks(self, doPrint = True):
        self._printObservationTracks = doPrint

    def printTrackInformation(self, event):
        print
        print '*****************************'
        print 'Observed track:'
        print '\tp =', event.track_p
        print '\tpt =', event.track_pt
        print '\t(eta, phi) = (', event.track_eta, ',', event.track_phi, ')'
        print '\tnLayersWithmeasurement =', getattr(event, 'track_hitPattern_.trackerLayersWithMeasurement')
        print '\t\tpackedPixelBarrelHitPattern =', event.track_packedPixelBarrelHitPattern
        print '\t\tpackedPixelEndcapHitPattern =', event.track_packedPixelEndcapHitPattern
        for i in range(20):
            isPixel  = getattr(event, 'eventvariable_hitIsPixel_0_%d' % i)
            charge   = getattr(event, 'eventvariable_hitCharge_0_%d' % i)
            if charge < 0:
                continue
            pixSize  = getattr(event, 'eventvariable_pixelSize_0_%d' % i)
            pixSizeX = getattr(event, 'eventvariable_pixelSizeX_0_%d' % i)
            pixSizeY = getattr(event, 'eventvariable_pixelSizeY_0_%d' % i)
            print '\thit {0} -- {1}: {2} MeV/cm ; cluster size = ({3}, {4}) = {5}'.format(i, 'PIX' if isPixel else 'STRIPS', charge, pixSizeX, pixSizeY, pixSize)

    def constructSignalPdfs(self):
        print
        print 'Constructing signal pdfs...'
        fout = TFile('signalPdfs_' + self._nLayersWord + '.root', 'recreate')
        for sample in self._signalHypotheses:

            pixelHits = TH1D(sample, sample, 1000, 0, 100)
            pixelHits_noBigClusters = TH1D(sample + '_noBigClusters', sample + '_noBigClusters', 1000, 0, 100)

            pixelHits_hit0 = TH1D(sample + '_hit0', sample + '_hit0', 1000, 0, 100)
            pixelHits_hit1 = TH1D(sample + '_hit1', sample + '_hit1', 1000, 0, 100)
            pixelHits_hit2 = TH1D(sample + '_hit2', sample + '_hit2', 1000, 0, 100)
            pixelHits_hit3 = TH1D(sample + '_hit3', sample + '_hit3', 1000, 0, 100)

            nplot = TH1D(sample + '_nOver5', sample + '_nOver5;number of pixel hits (> 5 MeV/cm)', 10, 0, 10)

            pixSize      = TH1D(sample + '_pixelSize',     sample + '_pixelSize', 100, 0, 100)
            pixSizeX     = TH1D(sample + '_pixelSizeX',    sample + '_pixelSizeX', 100, 0, 100)
            pixSizeY     = TH1D(sample + '_pixelSizeY',    sample + '_pixelSizeY', 100, 0, 100)
            pixSizeYvsX  = TH2D(sample + '_pixelSizeYvsX', sample + '_pixelSizeYvsX', 100, 0, 100, 100, 0, 100)
            chargeVsSize = TH2D(sample + '_chargeVsSize',  sample + '_chargeVsSize;pixel cluster size;dE/dx [MeV/cm]', 100, 0, 100, 1000, 0, 100)

            sizeVsHitNumber   = TH2D(sample + '_sizeVsHitNumber',   sample + '_sizeVsHitNumber;hit number;pixel cluster size', 6, 0, 6, 100, 0, 100)
            chargeVsHitNumber = TH2D(sample + '_chargeVsHitNumber', sample + '_chargeVsHitNumber;hit number;dE/dx [MeV/cm]', 6, 0, 6, 100, 0, 100)

            for event in self._signalHypotheses[sample]['chain']:
                hitCharges = [getattr(event, 'eventvariable_hitCharge_0_%d' % i) for i in range(20)]
                hitIsPixel = [getattr(event, 'eventvariable_hitIsPixel_0_%d' % i) for i in range(20)]
                pixelSize  = [getattr(event, 'eventvariable_pixelSize_0_%d' % i) for i in range(20)]
                pixelSizeX = [getattr(event, 'eventvariable_pixelSizeX_0_%d' % i) for i in range(20)]
                pixelSizeY = [getattr(event, 'eventvariable_pixelSizeY_0_%d' % i) for i in range(20)]

                hasBigCluster = False
                for i in range(20):
                    if hitIsPixel[i] and pixelSize[i] >= 6:
                        hasBigCluster = True
                        break
                    if hasBigCluster:
                        break

                w = 1.0
                for weight in self._weights:
                    w *= getattr(event, weight)
                nOver5 = 0
                for i in range(20):
                    if hitIsPixel[i]:
                        pixelHits.Fill(hitCharges[i], w)
                        if not hasBigCluster:
                            pixelHits_noBigClusters.Fill(hitCharges[i], w)
                        if i == 0: pixelHits_hit0.Fill(hitCharges[i], w)
                        if i == 1: pixelHits_hit1.Fill(hitCharges[i], w)
                        if i == 2: pixelHits_hit2.Fill(hitCharges[i], w)
                        if i == 3: pixelHits_hit3.Fill(hitCharges[i], w)
                        chargeVsSize.Fill(pixelSize[i], hitCharges[i])
                        pixSize.Fill(pixelSize[i])
                        pixSizeX.Fill(pixelSizeX[i])
                        pixSizeY.Fill(pixelSizeY[i])
                        pixSizeYvsX.Fill(pixelSizeX[i], pixelSizeY[i])
                        if hitCharges[i] > 5:
                            nOver5 += 1
                        sizeVsHitNumber.Fill(i, pixelSize[i])
                        chargeVsHitNumber.Fill(i, hitCharges[i])
                nplot.Fill(nOver5, w)

            self._signalHypotheses[sample]['pdf'] = pixelHits
            fout.cd()
            pixelHits.Write()
            pixelHits_noBigClusters.Write()
            pixelHits_hit0.Write()
            pixelHits_hit1.Write()
            pixelHits_hit2.Write()
            pixelHits_hit3.Write()
            nplot.Write()
            pixSize.Write()
            pixSizeX.Write()
            pixSizeY.Write()
            sizeVsHitNumber.Write()
            chargeVsSize.Write()
        print 'Created signalPdfs_' + self._nLayersWord + '.root'
        fout.Close()

    def constructDataPdf(self, role):
        fout = TFile(role + 'Pdf_' + self._nLayersWord + '.root', 'recreate')
        
        pixelHits = TH1D('pixelHits', 'pixelHits', 1000, 0, 100)

        pixelHits_noBigClusters = TH1D('pixelHits_noBigClusters', 'pixelHits_noBigClusters', 1000, 0, 100)

        pixelHits_hit0 = TH1D('pixelHits_hit0', 'pixelHits_hit0', 1000, 0, 100)
        pixelHits_hit1 = TH1D('pixelHits_hit1', 'pixelHits_hit1', 1000, 0, 100)
        pixelHits_hit2 = TH1D('pixelHits_hit2', 'pixelHits_hit2', 1000, 0, 100)
        pixelHits_hit3 = TH1D('pixelHits_hit3', 'pixelHits_hit3', 1000, 0, 100)

        nplot = TH1D('nOver5', 'nOver5;number of pixel hits (> 5 MeV/cm)', 10, 0, 10)

        pixSize = TH1D('pixelSize', 'pixelSize', 100, 0, 100)
        pixSizeX = TH1D('pixelSizeX', 'pixelSizeX', 100, 0, 100)
        pixSizeY = TH1D('pixelSizeY', 'pixelSizeY', 100, 0, 100)
        pixSizeYvsX = TH2D('pixelSizeYvsX', 'pixelSizeYvsX', 100, 0, 100, 100, 0, 100)
        chargeVsSize = TH2D('chargeVsSize', 'chargeVsSize;pixel cluster size;dE/dx [MeV/cm]', 100, 0, 100, 1000, 0, 100)

        sizeVsHitNumber = TH2D('sizeVsHitNumber', 'sizeVsHitNumber;hit number;pixel cluster size', 6, 0, 6, 100, 0, 100)
        chargeVsHitNumber = TH2D('chargeVsHitNumber', 'chargeVsHitNumber;hit number;dE/dx [MeV/cm]', 6, 0, 6, 100, 0, 100)

        for event in getattr(self, role)['tree']:

            if self._printObservationTracks:
                self.printTrackInformation(event)

            hitCharges = [getattr(event, 'eventvariable_hitCharge_0_%d' % i) for i in range(20)]
            hitIsPixel = [getattr(event, 'eventvariable_hitIsPixel_0_%d' % i) for i in range(20)]
            pixelSize  = [getattr(event, 'eventvariable_pixelSize_0_%d' % i) for i in range(20)]
            pixelSizeX = [getattr(event, 'eventvariable_pixelSizeX_0_%d' % i) for i in range(20)]
            pixelSizeY = [getattr(event, 'eventvariable_pixelSizeY_0_%d' % i) for i in range(20)]
            nOver5 = 0

            hasBigCluster = False
            for i in range(20):
                if hitIsPixel[i] and pixelSize[i] >= 6:
                    hasBigCluster = True
                    break
                if hasBigCluster:
                    break

            for i in range(20):
                if hitIsPixel[i]:
                    pixelHits.Fill(hitCharges[i])
                    if not hasBigCluster:
                        pixelHits_noBigClusters.Fill(hitCharges[i])
                    if i == 0: pixelHits_hit0.Fill(hitCharges[i])
                    if i == 1: pixelHits_hit1.Fill(hitCharges[i])
                    if i == 2: pixelHits_hit2.Fill(hitCharges[i])
                    if i == 3: pixelHits_hit3.Fill(hitCharges[i])
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

        fout.cd()
        pixelHits.Write()
        pixelHits_noBigClusters.Write()
        pixelHits_hit0.Write()
        pixelHits_hit1.Write()
        pixelHits_hit2.Write()
        pixelHits_hit3.Write()
        nplot.Write()
        pixSize.Write()
        pixSizeX.Write()
        pixSizeY.Write()
        pixSizeYvsX.Write()
        chargeVsSize.Write()
        chargeVsHitNumber.Write()
        sizeVsHitNumber.Write()
        print 'Created ' + role + 'Pdf_' + self._nLayersWord + '.root'
        fout.Close()
