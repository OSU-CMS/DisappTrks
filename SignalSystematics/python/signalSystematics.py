#!/usr/bin/env python
import os
import sys
import math
import copy
from array import array

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TMath, TPaveText, TObject, TLine, TH2D, TChain, gDirectory

from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.SignalMC.signalCrossSecs import signal_cross_sections

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

# 10cmTo1cm not available...
def GetMissingLifetimeWeight(chain):
        w = 0
        # how is this possible otherwise? one event in /data/users/kwei/2017/signalAcceptance_full_v2/AMSB_chargino_100GeV_10cm_94X/
        if chain.eventvariable_cTau_1000024_0 > 0:
            srcPDF = math.exp(-1.0 * chain.eventvariable_cTau_1000024_0 / 10.0) / 10.0
            dstPDF = math.exp(-1.0 * chain.eventvariable_cTau_1000024_0 / 1.0) / 1.0
            w = dstPDF / srcPDF
        if chain.eventvariable_cTau_1000024_1 > 0:
            srcPDF = math.exp(-1.0 * chain.eventvariable_cTau_1000024_1 / 10.0) / 10.0
            dstPDF = math.exp(-1.0 * chain.eventvariable_cTau_1000024_1 / 1.0) / 1.0
            w *= dstPDF / srcPDF
        return w

def MergedWithBadCrossSection(sample, condorDir):
    datasetInfo = open("condor/" + condorDir + "/" + sample + "/datasetInfo_" + sample + "_cfg.py")
    xsec = [x for x in list(datasetInfo) if x.startswith('crossSection = ')]
    datasetInfo.close()
    if len(xsec) > 0:
        xsec = float(xsec[-1].split('=')[-1])
    return (xsec < 0)

# defines a base class simply comparing the yields between central and up/down channels
class SystematicCalculator:

    _integrateHistogram = "Met Plots/metNoMu"
    _fout = ""
    _doFout = False
    _extraSamples = {}

    _systematic = []
    _maxSystematic = 0.0
    _averageSystematic = 0.0
    _n = 0

    # when "fluctuations" is used in EventWeights.py, there is no CutFlowPlotter
    # but the "total, totalError" remain the same as the central value channel
    _isWeightFluctuation = False

    def __init__ (self, masses, lifetimes):
        self._masses = masses
        self._lifetimes = lifetimes

    def addChannel (self, role, name, suffix, condorDir):
        channel = {"name" : name, "suffix" : suffix, "condorDir" : condorDir}
        setattr (self, role, channel)

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def addFout (self, fout):
        self._fout = fout
        self._doFout = True

    def addExtraSamples (self, extraSamples):
        self._extraSamples = extraSamples

    def setIsWeightFluctuation (self, isFluctuation):
        self._isWeightFluctuation = isFluctuation

    def printSampleSystematic (self, mass, lifetime):
        realLifetime = lifetime if lifetime != '1' else '10'
        if hasattr (self, "central") and hasattr (self, "down") and hasattr (self, "up"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (realLifetime) + "cm_" + self.central["suffix"]
            condorDir = self.central["condorDir"]
            name = self.central["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            condorDir = self.down["condorDir"]
            name = self.down["name"]
            if not self._isWeightFluctuation:
                total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            
            metHist = getHist (sample, condorDir, name + "Plotter" if not self._isWeightFluctuation else name, self._integrateHistogram)
            down = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            condorDir = self.up["condorDir"]
            name = self.up["name"]
            if not self._isWeightFluctuation:
                total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter" if not self._isWeightFluctuation else name, self._integrateHistogram)
            up = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]

            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (sample, relDiffDown, relDiffUp)
        else:
            print "central, down, and up not all defined. Not printing systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        self._maxSystematic = 0.0
        self._averageSystematic = 0.0
        self._n = 0
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime)
                self._systematic.append ([sample, str (max (1.0 + relDiffDown, 1.0e-12)), str (max (1.0 + relDiffUp, 1.0e-12))])

                if abs (relDiffDown) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffDown)
                if abs (relDiffUp) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffUp)

                self._averageSystematic += abs (relDiffDown)
                self._averageSystematic += abs (relDiffUp)
                self._n += 2
        self._averageSystematic /= self._n

        print "maximum systematic: " + str (self._maxSystematic * 100.0) + "%"
        print "average systematic: " + str (self._averageSystematic * 100.0) + "%"

        if self._fout:
            width = max (len (word) for row in self._systematic for word in row) + 2
            for row in self._systematic:
                if row[0] in self._extraSamples:
                    extraRow = copy.deepcopy (row)
                    for sample in self._extraSamples[row[0]]:
                        extraRow[0] = sample
                        self._fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")

class WeightSystematicFromTrees(SystematicCalculator):

    def __init__ (self, masses, lifetimes, intLumi):
        SystematicCalculator.__init__(self, masses, lifetimes)
        self._weightsCentral = [
            'eventvariable_lifetimeWeight',
            'eventvariable_isrWeight',
            'eventvariable_grandOrWeight',
            'eventvariable_puScalingFactor',
        ]
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_9_4_"):
            self._weightsCentral.append('eventvariable_L1ECALPrefiringWeight')
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_10_2_"):
            self._weightsCentral.append('eventvariable_hem1516weight')
        self._weightsUp = copy.deepcopy(self._weightsCentral)
        self._weightsDown = copy.deepcopy(self._weightsCentral)
        self._intLumi = intLumi

    def defineWeightToFluctuate(self, originalWeight):
        for i, w in enumerate(self._weightsCentral):
            if originalWeight == w:
                self._weightsUp[i] = w + 'Up'
                self._weightsDown[i] = w + 'Down'

    def defineFluctuationUp(self, originalWeight, upWeight):
        for i, w in enumerate(self._weightsUp):
            if originalWeight == w:
                self._weightsUp[i] = upWeight
                return
        print originalWeight + ' is not in the original list of weights'
        return

    def defineFluctuationDown(self, originalWeight, downWeight):
        for i, w in enumerate(self._weightsDown):
            if originalWeight == w:
                self._weightsDown[i] = downWeight
                return
        print originalWeight + ' is not in the original list of weights'
        return

    def getOriginalSample(self, condorDir, sample, mass, lifetime):
        lifetimeFloat = float(lifetime.replace('p', '.'))
        if os.path.isfile('condor/' + condorDir + '/' + sample + '.root') and lifetime != '1':
            for i in range(len(self._weightsCentral)):
                if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsCentral[i] = 'eventvariable_lifetimeWeight'
                if self._weightsUp[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsUp[i] = 'eventvariable_lifetimeWeight'
                if self._weightsDown[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsDown[i] = 'eventvariable_lifetimeWeight'
            return sample

        if lifetime in [10, 100, 1000, 10000]:
            raise Exception('Original sample condor/' + condorDir + '/' + sample + '.root does not exist!')

        originalLifetime = int(math.pow(10 , math.ceil((math.log10(lifetimeFloat)))))
        if originalLifetime == 1:
            originalLifetime = 10
        originalSample = 'AMSB_chargino_' + str(mass) + 'GeV_' + str(originalLifetime) + 'cm_' + self.central['suffix']
        if not os.path.isfile('condor/' + condorDir + '/' + originalSample + '.root'):
            raise Exception('Original sample condor/' + condorDir + '/' + originalSample + '.root does not exist!')

        for i in range(len(self._weightsCentral)):
            if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsCentral[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'
            if self._weightsUp[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsUp[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'
            if self._weightsDown[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsDown[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'

        return originalSample

    def GetYieldFromTree(self, sample, condorDir, name, mass, lifetime):
        total = totalUp = totalDown = 0.0

        realSample = self.getOriginalSample(condorDir, sample, mass, lifetime)

        chain = TChain(name + 'TreeMaker/Tree')
        chain.Add('condor/' + condorDir + '/' + realSample + '/hist_*.root')

        realInputFile = TFile('condor/' + condorDir + '/' + realSample + '.root')
        nGenerated = realInputFile.Get(name + 'CutFlowPlotter/eventCounter').GetEntries()
        crossSectionWeight = self._intLumi * float(signal_cross_sections[realSample.split('_')[2][:-3]]['value']) / nGenerated

        for iEvent in range(chain.GetEntries()):
            chain.GetEntry(iEvent)

            if lifetime == '1':
                missingWeight = GetMissingLifetimeWeight(chain)

            thisWeightCentral = crossSectionWeight
            thisWeightUp = crossSectionWeight
            thisWeightDown = crossSectionWeight

            for iWeight in range(len(self._weightsCentral)):
                if self._weightsCentral[iWeight] == 'eventvariable_lifetimeWeight_1000024_10cmTo1cm':
                    thisWeightCentral *= missingWeight
                    thisWeightUp      *= missingWeight
                    thisWeightDown    *= missingWeight
                else:
                    thisWeightCentral *= getattr(chain, self._weightsCentral[iWeight])
                    if not math.isnan(getattr(chain, self._weightsUp[iWeight])):
                        thisWeightUp *= getattr(chain, self._weightsUp[iWeight])
                    else:
                        thisWeightUp *= getattr(chain, self._weightsCentral[iWeight])
                    if not math.isnan(getattr(chain, self._weightsDown[iWeight])):
                        thisWeightDown *= getattr(chain, self._weightsDown[iWeight])
                    else:
                        thisWeightDown *= getattr(chain, self._weightsCentral[iWeight])

            total     += thisWeightCentral
            totalUp   += thisWeightUp
            totalDown += thisWeightDown

        return total, totalUp, totalDown

    def printSampleSystematic(self, mass, lifetime):
        if not hasattr(self, 'central'):
            print '"central" not defined, not printing systematic...'
            return (float ("nan"), float ("nan"), float ("nan"))

        sample = 'AMSB_chargino_' + str(mass) + 'GeV_' + str(lifetime) + 'cm_' + self.central['suffix']
        central, up, down = self.GetYieldFromTree(sample, self.central['condorDir'], self.central['name'], mass, lifetime)

        relDiffDown = (down - central) / central if central > 0.0 else 0.0
        relDiffUp = (up - central) / central if central > 0.0 else 0.0

        print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
        return (sample, relDiffDown, relDiffUp)

    def printSystematic(self):
        self._maxSystematic = 0.0
        self._averageSystematic = 0.0
        self._n = 0
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime)
                self._systematic.append ([sample, str (max (1.0 + relDiffDown, 1.0e-12)), str (max (1.0 + relDiffUp, 1.0e-12))])

                if abs (relDiffDown) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffDown)
                if abs (relDiffUp) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffUp)

                self._averageSystematic += abs (relDiffDown)
                self._averageSystematic += abs (relDiffUp)
                self._n += 2
        self._averageSystematic /= self._n

        print "maximum systematic: " + str (self._maxSystematic * 100.0) + "%"
        print "average systematic: " + str (self._averageSystematic * 100.0) + "%"

        if self._fout:
            width = max (len (word) for row in self._systematic for word in row) + 2
            for row in self._systematic:
                if row[0] in self._extraSamples:
                    extraRow = copy.deepcopy (row)
                    for sample in self._extraSamples[row[0]]:
                        extraRow[0] = sample
                        self._fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")

class SelectionSystematicFromTrees(WeightSystematicFromTrees):
    def __init__ (self, masses, lifetimes, intLumi):
        WeightSystematicFromTrees.__init__(self, masses, lifetimes, intLumi)

    def printSampleSystematic(self, mass, lifetime):
        if not hasattr(self, 'central') or not hasattr(self, 'up') or not hasattr(self, 'down'):
            print '"central", "up", or "down" not defined, not printing systematic...'
            return (float ("nan"), float ("nan"), float ("nan"))

        sample = 'AMSB_chargino_' + str(mass) + 'GeV_' + str(lifetime) + 'cm_' + self.central['suffix']
        
        central = self.GetYieldFromTree(sample, self.central['condorDir'], self.central['name'], mass, lifetime)[0]
        up      = self.GetYieldFromTree(sample, self.up['condorDir'],      self.up['name'],      mass, lifetime)[0]
        down    = self.GetYieldFromTree(sample, self.down['condorDir'],    self.down['name'],    mass, lifetime)[0]

        relDiffDown = (down - central) / central if central > 0.0 else 0.0
        relDiffUp = (up - central) / central if central > 0.0 else 0.0

        print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
        return (sample, relDiffDown, relDiffUp)

    def printSystematic (self):
        self._maxSystematic = 0.0
        self._averageSystematic = 0.0
        self._n = 0
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime)
                self._systematic.append ([sample, str (max (1.0 + relDiffDown, 1.0e-12)), str (max (1.0 + relDiffUp, 1.0e-12))])

                if abs (relDiffDown) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffDown)
                if abs (relDiffUp) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffUp)

                self._averageSystematic += abs (relDiffDown)
                self._averageSystematic += abs (relDiffUp)
                self._n += 2
        self._averageSystematic /= self._n

        print "maximum systematic: " + str (self._maxSystematic * 100.0) + "%"
        print "average systematic: " + str (self._averageSystematic * 100.0) + "%"

        if self._fout:
            width = max (len (word) for row in self._systematic for word in row) + 2
            for row in self._systematic:
                if row[0] in self._extraSamples:
                    extraRow = copy.deepcopy (row)
                    for sample in self._extraSamples[row[0]]:
                        extraRow[0] = sample
                        self._fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")

# Save for 2015-6 use
class TriggerSystematic(SystematicCalculator):

    def __init__ (self, masses, lifetimes):
        SystematicCalculator.__init__ (self, masses, lifetimes)
        self._fluctuations = []
        self._foutPrefix = ""
        self._foutSuffix = ""

        self._overallMaxSystematic = 0.0
        self._overallAverageSystematic = 0.0
        self._nTriggerSystematics = 0

    def addTriggerFluctuations (self, triggerFluctuations):
        self._fluctuations = triggerFluctuations

    def setFoutNames (self, prefix, suffix):
        self._foutPrefix = prefix
        self._foutSuffix = suffix
        self._doFout = True

    def printSampleSystematic (self, mass, lifetime, fluctuation):
        if hasattr (self, "central") and hasattr (self, "down") and hasattr (self, "up"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]
            condorDir = self.central["condorDir"]
            name = self.central["name"]

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central = metHist.Integral ()

            metHist = getHist (sample, condorDir, name + "Plotter_" + fluctuation + "Down", self._integrateHistogram)
            down = metHist.Integral ()

            metHist = getHist (sample, condorDir, name + "Plotter_" + fluctuation + "Up", self._integrateHistogram)
            up = metHist.Integral ()

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (sample, relDiffDown, relDiffUp)

        else:
            print "central, down, and up not all defined. Not printing systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):

        self._overallMaxSystematic = 0.0
        self._overallAverageSystematic = 0.0
        self._nTriggerSystematics = 0

        for fluctuation in self._fluctuations:
            self._systematic = []
            self._maxSystematic = 0.0
            self._averageSystematic = 0.0
            self._n = 0
            for mass in self._masses:
                for lifetime in self._lifetimes:
                    sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime, fluctuation)
                    self._systematic.append ([sample, str (max (1.0 + relDiffDown, 1.0e-12)), str (max (1.0 + relDiffUp, 1.0e-12))])

                    if abs(relDiffDown) > self._maxSystematic:
                        self._maxSystematic = abs (relDiffDown)
                    if abs (relDiffUp) > self._maxSystematic:
                        self._maxSystematic = abs (relDiffUp)

                    if abs(relDiffDown) > self._overallMaxSystematic:
                        self._overallMaxSystematic = abs (relDiffDown)
                    if abs(relDiffUp) > self._overallMaxSystematic:
                        self._overallMaxSystematic = abs (relDiffUp)

                    self._averageSystematic += abs (relDiffDown)
                    self._averageSystematic += abs (relDiffUp)
                    self._n += 2

                    self._overallAverageSystematic += abs (relDiffDown)
                    self._overallAverageSystematic += abs (relDiffUp)
                    self._nTriggerSystematics += 2

            self._averageSystematic /= self._n

            print "maximum %s systematic: %f%%" % (fluctuation, self._maxSystematic * 100.0)
            print "average %s systematic: %f%%" % (fluctuation, self._averageSystematic * 100.0)

            if self._doFout:
                fout = open(self._foutPrefix + fluctuation + "_" + self._foutSuffix, "w")
                width = max (len (word) for row in self._systematic for word in row) + 2
                for row in self._systematic:
                    if row[0] in self._extraSamples:
                        extraRow = copy.deepcopy (row)
                        for sample in self._extraSamples[row[0]]:
                            extraRow[0] = sample
                            fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                    fout.write ("".join (word.ljust (width) for word in row) + "\n")

                fout.close ()

        self._overallAverageSystematic /= self._nTriggerSystematics

        print "\n"
        print "maximum trigger systematic (all types): %f%%" % (self._overallMaxSystematic * 100.0)
        print "average trigger systematic (all types): %f%%" % (self._overallAverageSystematic * 100.0)

class MetSystematic(SystematicCalculator):

    def __init__ (self, masses, lifetimes):
        SystematicCalculator.__init__ (self, masses, lifetimes)
        self._metCut = 100.0
        self._metTypes = []
        self._foutPrefix = ""
        self._foutSuffix = ""

        self._overallMaxSystematic = 0.0
        self._overallAverageSystematic = 0.0
        self._nMetSystematics = 0

    def addMetTypes (self, metTypes):
        self._metTypes = metTypes

    def setMetCut (self, metCut):
        self._metCut = metCut

    def setFoutNames (self, prefix, suffix):
        self._foutPrefix = prefix
        self._foutSuffix = suffix
        self._doFout = True

    def printSampleSystematic (self, mass, lifetime, metType):
        realLifetime = lifetime if lifetime != '1' else '10'
        if hasattr (self, "central") and hasattr (self, "down") and hasattr (self, "up"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (realLifetime) + "cm_" + self.central["suffix"]
            condorDir = self.central["condorDir"]
            name = self.central["name"]

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            total = metHist.Integral (0, metHist.GetNbinsX () + 1)
            central = metHist.Integral (metHist.GetXaxis ().FindBin (self._metCut), metHist.GetNbinsX () + 1) / total if total > 0.0 else 0.0

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram + "_" + metType + "Down")
            total = metHist.Integral (0, metHist.GetNbinsX () + 1)
            down = metHist.Integral (metHist.GetXaxis ().FindBin (self._metCut), metHist.GetNbinsX () + 1) / total if total > 0.0 else 0.0

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram + "_" + metType + "Up")
            total = metHist.Integral (0, metHist.GetNbinsX () + 1)
            up = metHist.Integral (metHist.GetXaxis ().FindBin (self._metCut), metHist.GetNbinsX () + 1) / total if total > 0.0 else 0.0

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]

            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (sample, relDiffDown, relDiffUp)

        else:
            print "central, down, and up not all defined. Not printing systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):

        self._overallMaxSystematic = 0.0
        self._overallAverageSystematic = 0.0
        self._nMetSystematics = 0

        for metType in self._metTypes:
            self._systematic = []
            self._maxSystematic = 0.0
            self._averageSystematic = 0.0
            self._n = 0
            for mass in self._masses:
                for lifetime in self._lifetimes:
                    sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime, metType)
                    self._systematic.append ([sample, str (max (1.0 + relDiffDown, 1.0e-12)), str (max (1.0 + relDiffUp, 1.0e-12))])

                    if abs(relDiffDown) > self._maxSystematic:
                        self._maxSystematic = abs (relDiffDown)
                    if abs (relDiffUp) > self._maxSystematic:
                        self._maxSystematic = abs (relDiffUp)

                    if abs(relDiffDown) > self._overallMaxSystematic:
                        self._overallMaxSystematic = abs (relDiffDown)
                    if abs(relDiffUp) > self._overallMaxSystematic:
                        self._overallMaxSystematic = abs (relDiffUp)

                    self._averageSystematic += abs (relDiffDown)
                    self._averageSystematic += abs (relDiffUp)
                    self._n += 2

                    self._overallAverageSystematic += abs (relDiffDown)
                    self._overallAverageSystematic += abs (relDiffUp)
                    self._nMetSystematics += 2

            self._averageSystematic /= self._n

            print "maximum %s systematic: %f%%" % (metType, self._maxSystematic * 100.0)
            print "average %s systematic: %f%%" % (metType, self._averageSystematic * 100.0)

            if self._doFout:
                fout = open(self._foutPrefix + metType + "_" + self._foutSuffix, "w")
                width = max (len (word) for row in self._systematic for word in row) + 2
                for row in self._systematic:
                    if row[0] in self._extraSamples:
                        extraRow = copy.deepcopy (row)
                        for sample in self._extraSamples[row[0]]:
                            extraRow[0] = sample
                            fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                    fout.write ("".join (word.ljust (width) for word in row) + "\n")

                fout.close ()

        self._overallAverageSystematic /= self._nMetSystematics

        print "\n"
        print "maximum met systematic (all types): %f%%" % (self._overallMaxSystematic * 100.0)
        print "average met systematic (all types): %f%%" % (self._overallAverageSystematic * 100.0)

# Save for 2015-6 use
class PileupSystematic:

    _integrateHistogram = "Met Plots/metNoMu"
    _masses = []
    _lifetimes = []
    _fout = ""
    _extraSamples = {}

    def addChannel (self, role, name, suffix, condorDir):
        channel = {"name" : name, "suffix" : suffix, "condorDir" : condorDir}
        setattr (self, role, channel)

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def addMasses (self, masses):
        self._masses = masses

    def addLifetimes (self, lifetimes):
        self._lifetimes = lifetimes

    def addFout (self, fout):
        self._fout = fout

    def addExtraSamples (self, extraSamples):
        self._extraSamples = extraSamples

    def __init__ (self, masses, lifetimes):
        self.addMasses (masses)
        self.addLifetimes (lifetimes)

    def printPileupSystematic (self, mass, lifetime):
        if hasattr (self, "PileupCentral") and hasattr (self, "PileupDown") and hasattr (self, "PileupUp"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupCentral["suffix"]
            condorDir = self.PileupCentral["condorDir"]
            name = self.PileupCentral["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupDown["suffix"]
            condorDir = self.PileupDown["condorDir"]
            name = self.PileupDown["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            down = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupUp["suffix"]
            condorDir = self.PileupUp["condorDir"]
            name = self.PileupUp["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            up = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(" + sample + ") down: " + str (down) + ", central: " + str (central) + ", up: " + str (up) + ", systematic uncertainty: " + str (relDiffDown * 100.0) + "%/" + str (relDiffUp * 100.0) + "%"
            return (sample, relDiffDown, relDiffUp)
        else:
            print "PileupCentral, PileupDown, and PileupUp not all defined. Not printing pileup systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        systematic = []
        maxSystematic = 0.0
        averageSystematic = 0.0
        n = 0
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample, relDiffDown, relDiffUp = self.printPileupSystematic (mass, lifetime)
                systematic.append ([sample, str (max (1.0 + relDiffDown, 1.0e-12)), str (max (1.0 + relDiffUp, 1.0e-12))])

                if abs (relDiffDown) > maxSystematic:
                  maxSystematic = abs (relDiffDown)
                if abs (relDiffUp) > maxSystematic:
                  maxSystematic = abs (relDiffUp)

                averageSystematic += abs (relDiffDown)
                averageSystematic += abs (relDiffUp)
                n += 2
        averageSystematic /= n

        print "maximum systematic: " + str (maxSystematic * 100.0) + "%"
        print "average systematic: " + str (averageSystematic * 100.0) + "%"

        if self._fout:
            width = max (len (word) for row in systematic for word in row) + 2
            for row in systematic:
                if row[0] in self._extraSamples:
                    extraRow = copy.deepcopy (row)
                    for sample in self._extraSamples[row[0]]:
                        extraRow[0] = sample
                        self._fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")

class ECaloSystematic:

    _integrateHistogram = "Track Plots/trackCaloTot_RhoCorr"

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "Plotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def printECaloSystematic (self, dataOrMC = "Data"):
        if hasattr (self, dataOrMC):
            channel = getattr (self, dataOrMC)
            sample = channel["sample"]
            condorDir = channel["condorDir"]
            name = channel["name"]
            ecalo = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)

            passesError = Double (0.0)
            totalError = Double (0.0)
            passes = ecalo.IntegralAndError (0, ecalo.FindBin (10.0) - 1, passesError)
            total = ecalo.IntegralAndError (0, ecalo.GetNbinsX () + 1, totalError)

            eff, effErrorLow, effErrorHigh = getEfficiency (passes, passesError, total, totalError)

            print "efficiency of ECalo cut in " + dataOrMC + ": " + str (eff) + " - " + str (effErrorLow) + " + " + str (effErrorHigh)
            return (eff, effErrorLow, effErrorHigh)
        else:
            print dataOrMC + " not defined. Not printing ECalo systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        data, dataErrorLow, dataErrorHigh = self.printECaloSystematic ("Data")
        mc, mcErrorLow, mcErrorHigh = self.printECaloSystematic ("MC")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%"

class HitsSystematic:

    _integrateHistogram = "Track Plots/trackNHitsMissingMiddleVsInner"

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "Plotter")
        channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
        channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
        setattr (self, role, channel)
        print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def printHitsSystematic (self, dataOrMC = "Data", xOrY = "XY"):
        if hasattr (self, dataOrMC):
            channel = getattr (self, dataOrMC)
            sample = channel["sample"]
            condorDir = channel["condorDir"]
            name = channel["name"]
            hits = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)

            passesError = Double (0.0)
            totalError = Double (0.0)
            passes = 0.0
            total = hits.IntegralAndError (0, hits.GetNbinsX () + 1, 0, hits.GetNbinsY () + 1, totalError)
            label = ""
            if xOrY == "XY":
                passes = hits.IntegralAndError (0, hits.GetXaxis ().FindBin (0.0), 0, hits.GetYaxis ().FindBin (0.0), passesError)
                label = "combined"
            elif xOrY == "X":
                passes = hits.IntegralAndError (0, hits.GetXaxis ().FindBin (0.0), 0, hits.GetNbinsY () + 1, passesError)
                label = hits.GetXaxis ().GetTitle ()
            elif xOrY == "Y":
                passes = hits.IntegralAndError (0, hits.GetNbinsX () + 1, 0, hits.GetYaxis ().FindBin (0.0), passesError)
                label = hits.GetYaxis ().GetTitle ()

            eff, effErrorLow, effErrorHigh = getEfficiency (passes, passesError, total, totalError)

            print "efficiency of " + label + " cut in " + dataOrMC + ": " + str (eff) + " - " + str (effErrorLow) + " + " + str (effErrorHigh)
            return (eff, effErrorLow, effErrorHigh)
        else:
            print dataOrMC + " not defined. Not printing hits systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        data, dataErrorLow, dataErrorHigh = self.printHitsSystematic ("Data", "X")
        mc, mcErrorLow, mcErrorHigh = self.printHitsSystematic ("MC", "X")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%\n"

        data, dataErrorLow, dataErrorHigh = self.printHitsSystematic ("Data", "Y")
        mc, mcErrorLow, mcErrorHigh = self.printHitsSystematic ("MC", "Y")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%\n"

        data, dataErrorLow, dataErrorHigh = self.printHitsSystematic ("Data")
        mc, mcErrorLow, mcErrorHigh = self.printHitsSystematic ("MC")

        print "systematic uncertainty: " + str ((abs (data - mc) / data) * 100.0) + "%"

class MissingOuterHitsSystematic:

    _integrateHistogram = "Track Plots/trackNHitsMissingOuterCorrected"
    _fout = ""
    _masses = None
    _lifetimes = None
    _signalSuffix = ""
    _fout = None
    _foutForPlot = None

    def __init__ (self, masses, lifetimes, intLumi = None):
        self._masses = masses
        self._lifetimes = lifetimes
        self._weightsCentral = [
            'eventvariable_lifetimeWeight',
            'eventvariable_isrWeight',
            'eventvariable_grandOrWeight',
            'eventvariable_puScalingFactor',
        ]
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_9_4_"):
            self._weightsCentral.append('eventvariable_L1ECALPrefiringWeight')
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_10_2_"):
            self._weightsCentral.append('eventvariable_hem1516weight')
        self._weightsUp = copy.deepcopy(self._weightsCentral)
        self._weightsDown = copy.deepcopy(self._weightsCentral)
        self._intLumi = intLumi

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        if sample != "":
            channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "Plotter")
            channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
            print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])
        setattr (self, role, channel)

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def addSignalSuffix (self, signalSuffix):
        self._signalSuffix = signalSuffix

    def addFout (self, fout):
        self._fout = fout

    def addFoutForPlot (self, foutForPlot):
        self._foutForPlot = foutForPlot

    def getNMissOutEfficiency (self, dataOrMC, nLow, nHigh = -1, hits = None, sample = None, mass = None, lifetime = None):
        if hasattr (self, dataOrMC):
            if not hits:
                channel = getattr (self, dataOrMC)
                if dataOrMC != "Signal":
                    sample = channel["sample"]
                condorDir = channel["condorDir"]
                name = channel["name"]
                if os.path.isfile('condor/' + condorDir + '/' + sample + '.root') and lifetime != '1':
                    hits = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
                else:
                    hits = self.GetHitsFromTree(sample, condorDir, name, mass, lifetime)

            if nHigh < 0:
                nHigh = nLow

            passesError = Double (0.0)
            totalError = Double (0.0)
            passes = hits.IntegralAndError (hits.FindBin (nLow), hits.FindBin (nHigh), totalError)
            total = hits.IntegralAndError (0, hits.GetNbinsX () + 1, totalError)

            eff, effErrorLow, effErrorHigh = getEfficiency (passes, passesError, total, totalError)
            eff = Measurement (eff, effErrorLow, effErrorHigh)

            return (eff, hits)
        else:
            print dataOrMC + " not defined. Not printing missing outer hits systematic..."
            return (float ("nan"), float ("nan"))

    def getOriginalSample(self, condorDir, sample, mass, lifetime):
        lifetimeFloat = float(lifetime.replace('p', '.'))
        if os.path.isfile('condor/' + condorDir + '/' + sample + '.root') and lifetime != '1':
            for i in range(len(self._weightsCentral)):
                if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsCentral[i] = 'eventvariable_lifetimeWeight'
                if self._weightsUp[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsUp[i] = 'eventvariable_lifetimeWeight'
                if self._weightsDown[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsDown[i] = 'eventvariable_lifetimeWeight'
            return sample

        if lifetime in [10, 100, 1000, 10000]:
            raise Exception('Original sample condor/' + condorDir + '/' + sample + '.root does not exist!')

        originalLifetime = int(math.pow(10 , math.ceil((math.log10(lifetimeFloat)))))
        if originalLifetime == 1:
            originalLifetime = 10
        originalSample = 'AMSB_chargino_' + str(mass) + 'GeV_' + str(originalLifetime) + 'cm' + self._signalSuffix
        if not os.path.isfile('condor/' + condorDir + '/' + originalSample + '.root'):
            raise Exception('Original sample condor/' + condorDir + '/' + originalSample + '.root does not exist!')

        for i in range(len(self._weightsCentral)):
            if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsCentral[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'
            if self._weightsUp[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsUp[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'
            if self._weightsDown[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsDown[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'

        return originalSample

    def GetHitsFromTree(self, sample, condorDir, name, mass, lifetime):
        realSample = self.getOriginalSample(condorDir, sample, mass, lifetime)

        chain = TChain(name + 'TreeMaker/Tree')
        chain.Add('condor/' + condorDir + '/' + realSample + '/hist_*.root')

        if chain.GetEntries() == 0:
            hHits = TH1D('trackNHitsMissingOuterCorrected', 'trackNHitsMissingOuterCorrected', 16, -0.5, 15.5)
            hHits.SetDirectory(0)
            return hHits

        realInputFile = TFile('condor/' + condorDir + '/' + realSample + '.root')
        nGenerated = realInputFile.Get(name + 'CutFlowPlotter/eventCounter').GetEntries()
        crossSectionWeight = self._intLumi * float(signal_cross_sections[realSample.split('_')[2][:-3]]['value']) / nGenerated

        if 'eventvariable_lifetimeWeight_1000024_10cmTo1cm' in self._weightsCentral:
            hHits = TH1D('trackNHitsMissingOuterCorrected', 'trackNHitsMissingOuterCorrected', 16, -0.5, 15.5)
            for iEvent in range(chain.GetEntries()):
                chain.GetEntry(iEvent)
                w = crossSectionWeight
                for wgt in self._weightsCentral:
                    if wgt == 'eventvariable_lifetimeWeight_1000024_10cmTo1cm':
                        w *= GetMissingLifetimeWeight(chain)
                    else:
                        w *= getattr(chain, wgt)
                hHits.Fill(chain.track_hitAndTOBDrop_bestTrackMissingOuterHits, w)
            hHits.SetDirectory(0)
            return hHits

        weightString = str(crossSectionWeight)
        for w in self._weightsCentral:
            weightString = weightString + ' * ' + w

        chain.Draw('track_hitAndTOBDrop_bestTrackMissingOuterHits >> hHits(16, -0.5, 15.5)', weightString, 'goff')
        hHits = gDirectory.Get('hHits') 
        hHits.SetDirectory(0)
        return hHits

    def getSignalYield (self, mass, lifetime, nLow, nHigh = -1, hits = None):
        if hasattr (self, "Signal"):
            if not hits:
                channel = getattr (self, "Signal")
                sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm" + self._signalSuffix
                condorDir = channel["condorDir"]
                name = channel["name"]

                if os.path.isfile('condor/' + condorDir + '/' + sample + '.root') and lifetime != '1':
                    hits = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
                else:
                    hits = self.GetHitsFromTree(sample, condorDir, name, mass, lifetime)

            if nHigh < 0:
                nHigh = nLow

            nError = Double (0.0)
            n = hits.IntegralAndError (hits.FindBin (nLow), hits.FindBin (nHigh), nError)
            n = Measurement (n, nError)

            return (n, hits)
        else:
            print "\"Signal\" not defined. Not printing missing outer hits systematic..."
            return (float ("nan"), float ("nan"))

    def printSystematic (self):
        dataHits = None
        mcHits = None
        signalHits = None
        systematic = []
        masses = map (float, self._masses)
        lifetimes = [float(x.replace('0p', '0.')) for x in self._lifetimes]
        massBins = array ("d", masses + [masses[-1] + 100])
        lifetimeBins = array ("d", lifetimes + [lifetimes[-1] * 10.0])
        h = TH2D ("nMissOutSystematic", ";chargino mass [GeV];chargino lifetime [cm/c]", len (massBins) - 1, massBins, len (lifetimeBins) - 1, lifetimeBins)
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm" + self._signalSuffix
                eTrue3ToInf, signalHits = self.getNMissOutEfficiency ("Signal", 3, 12, hits = None, sample = sample, mass = mass, lifetime = lifetime)
                eTrue2, signalHits = self.getNMissOutEfficiency      ("Signal", 2, 2,  hits = signalHits, sample = sample, mass = mass, lifetime = lifetime)
                eTrue1, signalHits = self.getNMissOutEfficiency      ("Signal", 1, 1,  hits = signalHits, sample = sample, mass = mass, lifetime = lifetime)
                eTrue0, signalHits = self.getNMissOutEfficiency      ("Signal", 0, 0,  hits = signalHits, sample = sample, mass = mass, lifetime = lifetime)

                eMC1ToInf, mcHits = self.getNMissOutEfficiency ("MC", 1, 12, hits = mcHits)
                eMC2ToInf, mcHits = self.getNMissOutEfficiency ("MC", 2, 12, hits = mcHits)
                eMC3ToInf, mcHits = self.getNMissOutEfficiency ("MC", 3, 12, hits = mcHits)

                eData1ToInf, dataHits = self.getNMissOutEfficiency ("Data", 1, 12, hits = dataHits)
                eData2ToInf, dataHits = self.getNMissOutEfficiency ("Data", 2, 12, hits = dataHits)
                eData3ToInf, dataHits = self.getNMissOutEfficiency ("Data", 3, 12, hits = dataHits)

                mcEff = eTrue3ToInf + eTrue2 * eMC1ToInf + eTrue1 * eMC2ToInf + eTrue0 * eMC3ToInf
                dataEff = eTrue3ToInf + eTrue2 * eData1ToInf + eTrue1 * eData2ToInf + eTrue0 * eData3ToInf

                sys = abs (mcEff - dataEff) / mcEff if mcEff > 0.0 else Measurement (0.0, 0.0)
                systematic.append ([sample, str (max (1.0 - sys.centralValue (), 1.0e-12)), str (max (1.0 + sys.centralValue (), 1.0e-12))])

                sys *= 100.0
                sys.printUncertainty (False)
                sys.printLongFormat (True)
                h.Fill (mass, lifetime, abs (sys.centralValue () / 100.0))
                print "[" + str (mass) + " GeV, " + str (lifetime) + " cm] data eff.: " + str (dataEff) + ", MC eff.: " + str (mcEff) + ", systematic uncertainty: " + str (sys) + "%"

        if self._foutForPlot:
            self._foutForPlot.cd ()
            h.Write ()
            self._foutForPlot.Close ()

        if self._fout:
            width = max (len (word) for row in systematic for word in row) + 2
            for row in systematic:
                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")

class LeptonVetoScaleFactorSystematic:

    _integrateHistogram = ""
    _treeVariableName = ""
    _fout = ""
    _masses = None
    _lifetimes = None
    _signalSuffix = ""
    _fout = None
    _foutForPlot = None
    _vetoDeltaR = 0.15
    _pogPayloadFile = ""
    _pogPayloadName = ""

    def __init__ (self, flavor, masses, lifetimes, intLumi = None):
        self._integrateHistogram = "Track Plots/trackDeltaRToClosest" + flavor
        self._treeVariableName = "track_deltaRToClosest" + flavor
        self._masses = masses
        self._lifetimes = lifetimes
        self._weightsCentral = [
            'eventvariable_lifetimeWeight',
            'eventvariable_isrWeight',
            'eventvariable_grandOrWeight',
            'eventvariable_puScalingFactor',
        ]
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_9_4_"):
            self._weightsCentral.append('eventvariable_L1ECALPrefiringWeight')
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_10_2_"):
            self._weightsCentral.append('eventvariable_hem1516weight')
        self._weightsUp = copy.deepcopy(self._weightsCentral)
        self._weightsDown = copy.deepcopy(self._weightsCentral)
        self._intLumi = intLumi

    def addChannel (self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        if sample != "":
            channel["yield"], channel["yieldError"] = getYield (sample, condorDir, name + "Plotter")
            channel["total"], channel["totalError"] = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            channel["weight"] = (channel["totalError"] * channel["totalError"]) / channel["total"]
            print "yield for " + name + ": " + str (channel["yield"]) + " +- " + str (channel["yieldError"])
        setattr (self, role, channel)

    def setVetoDeltaR(self, deltaR):
        self._vetoDeltaR = deltaR

    def setPOGPayload(self, filePath, payloadName):
        self._pogPayloadFile = os.path.abspath(filePath)
        self._pogPayloadName = payloadName

    def addSignalSuffix (self, signalSuffix):
        self._signalSuffix = signalSuffix

    def addFout (self, fout):
        self._fout = fout

    def addFoutForPlot (self, foutForPlot):
        self._foutForPlot = foutForPlot

    def getOriginalSample(self, condorDir, sample, mass, lifetime):
        lifetimeFloat = float(lifetime.replace('p', '.'))
        if os.path.isfile('condor/' + condorDir + '/' + sample + '.root') and lifetime != '1':
            for i in range(len(self._weightsCentral)):
                if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsCentral[i] = 'eventvariable_lifetimeWeight'
                if self._weightsUp[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsUp[i] = 'eventvariable_lifetimeWeight'
                if self._weightsDown[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsDown[i] = 'eventvariable_lifetimeWeight'
            return sample

        if lifetime in [10, 100, 1000, 10000]:
            raise Exception('Original sample condor/' + condorDir + '/' + sample + '.root does not exist!')

        originalLifetime = int(math.pow(10 , math.ceil((math.log10(lifetimeFloat)))))
        if originalLifetime == 1:
            originalLifetime = 10
        originalSample = 'AMSB_chargino_' + str(mass) + 'GeV_' + str(originalLifetime) + 'cm' + self._signalSuffix
        if not os.path.isfile('condor/' + condorDir + '/' + originalSample + '.root'):
            raise Exception('Original sample condor/' + condorDir + '/' + originalSample + '.root does not exist!')

        for i in range(len(self._weightsCentral)):
            if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsCentral[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'
            if self._weightsUp[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsUp[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'
            if self._weightsDown[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsDown[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'

        return originalSample

    def GetHistogramFromTree(self, sample, condorDir, name, mass, lifetime):
        realSample = self.getOriginalSample(condorDir, sample, mass, lifetime)

        chain = TChain(name + 'TreeMaker/Tree')
        chain.Add('condor/' + condorDir + '/' + realSample + '/hist_*.root')

        if chain.GetEntries() == 0:
            h = TH1D(self._integrateHistogram, self._integrateHistogram, 100, 0, 1)
            h.SetDirectory(0)
            return h

        realInputFile = TFile('condor/' + condorDir + '/' + realSample + '.root')
        nGenerated = realInputFile.Get(name + 'CutFlowPlotter/eventCounter').GetEntries()
        crossSectionWeight = self._intLumi * float(signal_cross_sections[realSample.split('_')[2][:-3]]['value']) / nGenerated

        if 'eventvariable_lifetimeWeight_1000024_10cmTo1cm' in self._weightsCentral:
            h = TH1D(self._integrateHistogram, self._integrateHistogram, 100, 0, 1)
            for iEvent in range(chain.GetEntries()):
                chain.GetEntry(iEvent)
                w = crossSectionWeight
                for wgt in self._weightsCentral:
                    if wgt == 'eventvariable_lifetimeWeight_1000024_10cmTo1cm':
                        w *= GetMissingLifetimeWeight(chain)
                    else:
                        w *= getattr(chain, wgt)
                h.Fill(getattr(chain, self._treeVariableName), w)
            h.SetDirectory(0)
            return h

        weightString = str(crossSectionWeight)
        for w in self._weightsCentral:
            weightString = weightString + ' * ' + w

        chain.Draw(self._treeVariableName + ' >> h(100, 0, 1)', weightString, 'goff')
        h = gDirectory.Get('h') 
        h.SetDirectory(0)
        return h

    def getRelativeVetoEfficiency(self, channel, sample = "", mass = None, lifetime = None):
        if channel["sample"] != "":
            sample = channel["sample"]
        if os.path.isfile('condor/' + channel["condorDir"] + '/' + sample + '.root') and lifetime != '1':
            h = getHist(sample, channel["condorDir"], channel["name"] + "Plotter", self._integrateHistogram)
        elif mass is not None and lifetime is not None:
            h = self.GetHistogramFromTree(sample, channel["condorDir"], channel["name"], mass, lifetime)
        else:
            print 'Provide mass and lifetime for tree-based integration!'
            return Measurement(0, 0, 0)

        # eff(veto) / eff(loose veto) = (npass(veto)/nTracks) / (npass(loose veto)/nTracks) 
        #                             = npass(veto)/npass(loose veto)
        #                             = Integral(>= 0.15) / Integral()

        passesError = Double(0.0)
        totalError = Double(0.0)

        passes = h.IntegralAndError(h.GetXaxis().FindBin(self._vetoDeltaR), -1, passesError)
        total = h.IntegralAndError(0, -1, totalError)

        eff, effErrorLow, effErrorHigh = getEfficiency (passes, passesError, total, totalError)
        
        if math.isnan(effErrorLow) or math.isnan(effErrorHigh):
            return Measurement(eff, 0.0, 0.0)

        return Measurement(eff, effErrorLow, effErrorHigh)

    def getEffectiveLoosePOGScaleFactor(self, sample, condorDir, name, mass, lifetime):
        # only from trees
        realSample = self.getOriginalSample(condorDir, sample, mass, lifetime)

        chain = TChain(name + 'TreeMaker/Tree')
        chain.Add('condor/' + condorDir + '/' + realSample + '/hist_*.root')

        totalWeight = Measurement(0.0, 0.0, 0.0)
        unweightedTotal = 0.0

        if chain.GetEntries() == 0:
            return Measurement(1.0, 0.0, 0.0)

        realInputFile = TFile('condor/' + condorDir + '/' + realSample + '.root')
        nGenerated = realInputFile.Get(name + 'CutFlowPlotter/eventCounter').GetEntries()
        crossSectionWeight = self._intLumi * float(signal_cross_sections[realSample.split('_')[2][:-3]]['value']) / nGenerated

        fSF_POG = TFile(self._pogPayloadFile)
        hSF_POG = fSF_POG.Get(self._pogPayloadName)

        for iEvent in range(chain.GetEntries()):
            chain.GetEntry(iEvent)
            w = crossSectionWeight
            for wgt in self._weightsCentral:
                if wgt == 'eventvariable_lifetimeWeight_1000024_10cmTo1cm':
                    w *= GetMissingLifetimeWeight(chain)
                else:
                    w *= getattr(chain, wgt)
                
            if "electron" in self._pogPayloadFile:
                pogBinX = hSF_POG.GetXaxis().FindBin(chain.track_eta)
                pogBinY = hSF_POG.GetYaxis().FindBin(chain.track_pt)
            elif "muon" in self._pogPayloadFile:
                pogBinX = hSF_POG.GetXaxis().FindBin(chain.track_pt)
                pogBinY = hSF_POG.GetYaxis().FindBin(abs(chain.track_eta))

            # check against overflow
            if pogBinX > hSF_POG.GetNbinsX():
                pogBinX = hSF_POG.GetNbinsX()
            if pogBinY > hSF_POG.GetNbinsY():
                pogBinY = hSF_POG.GetNbinsY()

            # check against underflow
            if pogBinX == 0:
                pogBinX = 1
            if pogBinY == 0:
                pogBinY = 1

            pogSF = hSF_POG.GetBinContent(pogBinX, pogBinY)
            pogSF_error = hSF_POG.GetBinError(pogBinX, pogBinY)

            totalWeight += w * Measurement(pogSF, pogSF_error, pogSF_error)
            unweightedTotal += w
        
        fSF_POG.Close()
        return totalWeight / unweightedTotal

    def printSystematic(self):
        systematic = []
        masses = map(float, self._masses)
        lifetimes = [float(x.replace('0p', '0.')) for x in self._lifetimes]
        massBins = array("d", masses + [masses[-1] + 100])
        lifetimeBins = array("d", lifetimes + [lifetimes[-1] * 10.0])
        hSF         = TH2D("leptonVetoScaleFactors", ";chargino mass [GeV];chargino lifetime [cm/c]", len(massBins) - 1, massBins, len(lifetimeBins) - 1, lifetimeBins)
        hPOG        = TH2D("leptonPOGScaleFactors", ";chargino mass [GeV];chargino lifetime [cm/c]", len(massBins) - 1, massBins, len(lifetimeBins) - 1, lifetimeBins)
        hSystematic = TH2D("leptonVetoScaleFactorsSystematics", ";chargino mass [GeV];chargino lifetime [cm/c]", len(massBins) - 1, massBins, len(lifetimeBins) - 1, lifetimeBins)

        dataEfficiencyRatio = self.getRelativeVetoEfficiency(self.Data)
        print 'Data ratio =', str(dataEfficiencyRatio), '\n'

        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm" + self._signalSuffix
                signalEfficiencyRatio = self.getRelativeVetoEfficiency(self.Signal, sample, mass, lifetime)

                scaleFactor = dataEfficiencyRatio / signalEfficiencyRatio if signalEfficiencyRatio.centralValue() > 0 else Measurement(1.0)
                scaleFactorPOG = self.getEffectiveLoosePOGScaleFactor(sample, self.Signal["condorDir"], self.Signal["name"], mass, lifetime)
                
                if signalEfficiencyRatio.centralValue() > 0 and not math.isnan(signalEfficiencyRatio.uncertaintyDown()) and not math.isnan(signalEfficiencyRatio.uncertaintyUp()):
                    scaleFactorTotal = scaleFactor * scaleFactorPOG
                else:
                    scaleFactorTotal = scaleFactorPOG

                if scaleFactorTotal.centralValue() < 1.0:
                    systematic.append([sample, str(scaleFactorTotal.centralValue()), "1.0"])
                else:
                    systematic.append([sample, "1.0", str(scaleFactorTotal.centralValue())])

                scaleFactor.printUncertainty(False)
                scaleFactor.printLongFormat(True)
                hSF.Fill(mass, lifetime, scaleFactor.centralValue())
                hPOG.Fill(mass, lifetime, scaleFactorPOG.centralValue())
                hSystematic.Fill(mass, lifetime, (scaleFactorTotal.centralValue() - 1.0) * 100.0)
                print "[{0} GeV, {1} cm] SF: {2}, SF(POG): {3}, SF(total): {4}".format(
                    mass,
                    lifetime,
                    str(scaleFactor),
                    str(scaleFactorPOG),
                    str(scaleFactorTotal)
                )

        if self._foutForPlot:
            self._foutForPlot.cd()
            hSF.Write()
            hPOG.Write()
            hSystematic.Write()
            self._foutForPlot.Close()

        if self._fout:
            width = max(len(word) for row in systematic for word in row) + 2
            for row in systematic:
                self._fout.write("".join(word.ljust(width) for word in row) + "\n")

class WeightSystematicFromTrees(SystematicCalculator):

    def __init__ (self, masses, lifetimes, intLumi):
        SystematicCalculator.__init__(self, masses, lifetimes)
        self._weightsCentral = [
            'eventvariable_lifetimeWeight',
            'eventvariable_isrWeight',
            'eventvariable_grandOrWeight',
            'eventvariable_puScalingFactor',
        ]
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_9_4_"):
            self._weightsCentral.append('eventvariable_L1ECALPrefiringWeight')
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_10_2_"):
            self._weightsCentral.append('eventvariable_hem1516weight')
        self._weightsUp = copy.deepcopy(self._weightsCentral)
        self._weightsDown = copy.deepcopy(self._weightsCentral)
        self._intLumi = intLumi

    def defineWeightToFluctuate(self, originalWeight):
        for i, w in enumerate(self._weightsCentral):
            if originalWeight == w:
                self._weightsUp[i] = w + 'Up'
                self._weightsDown[i] = w + 'Down'

    def defineFluctuationUp(self, originalWeight, upWeight):
        for i, w in enumerate(self._weightsUp):
            if originalWeight == w:
                self._weightsUp[i] = upWeight
                return
        print originalWeight + ' is not in the original list of weights'
        return

    def defineFluctuationDown(self, originalWeight, downWeight):
        for i, w in enumerate(self._weightsDown):
            if originalWeight == w:
                self._weightsDown[i] = downWeight
                return
        print originalWeight + ' is not in the original list of weights'
        return

    def getOriginalSample(self, condorDir, sample, mass, lifetime):
        lifetimeFloat = float(lifetime.replace('p', '.'))
        if os.path.isfile('condor/' + condorDir + '/' + sample + '.root') and lifetime != '1':
            for i in range(len(self._weightsCentral)):
                if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsCentral[i] = 'eventvariable_lifetimeWeight'
                if self._weightsUp[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsUp[i] = 'eventvariable_lifetimeWeight'
                if self._weightsDown[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsDown[i] = 'eventvariable_lifetimeWeight'
            return sample

        if lifetime in [10, 100, 1000, 10000]:
            raise Exception('Original sample condor/' + condorDir + '/' + sample + '.root does not exist!')

        originalLifetime = int(math.pow(10 , math.ceil((math.log10(lifetimeFloat)))))
        if originalLifetime == 1:
            originalLifetime = 10
        originalSample = 'AMSB_chargino_' + str(mass) + 'GeV_' + str(originalLifetime) + 'cm_' + self.central['suffix']
        if not os.path.isfile('condor/' + condorDir + '/' + originalSample + '.root'):
            raise Exception('Original sample condor/' + condorDir + '/' + originalSample + '.root does not exist!')

        for i in range(len(self._weightsCentral)):
            if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsCentral[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'
            if self._weightsUp[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsUp[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'
            if self._weightsDown[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsDown[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'

        return originalSample

    def GetYieldFromTree(self, sample, condorDir, name, mass, lifetime):
        total = totalUp = totalDown = 0.0

        realSample = self.getOriginalSample(condorDir, sample, mass, lifetime)

        chain = TChain(name + 'TreeMaker/Tree')
        chain.Add('condor/' + condorDir + '/' + realSample + '/hist_*.root')

        realInputFile = TFile('condor/' + condorDir + '/' + realSample + '.root')
        nGenerated = realInputFile.Get(name + 'CutFlowPlotter/eventCounter').GetEntries()
        crossSectionWeight = self._intLumi * float(signal_cross_sections[realSample.split('_')[2][:-3]]['value']) / nGenerated

        for iEvent in range(chain.GetEntries()):
            chain.GetEntry(iEvent)

            if lifetime == '1':
                missingWeight = GetMissingLifetimeWeight(chain)

            thisWeightCentral = crossSectionWeight
            thisWeightUp = crossSectionWeight
            thisWeightDown = crossSectionWeight

            for iWeight in range(len(self._weightsCentral)):
                if self._weightsCentral[iWeight] == 'eventvariable_lifetimeWeight_1000024_10cmTo1cm':
                    thisWeightCentral *= missingWeight
                    thisWeightUp      *= missingWeight
                    thisWeightDown    *= missingWeight
                else:
                    thisWeightCentral *= getattr(chain, self._weightsCentral[iWeight])
                    if not math.isnan(getattr(chain, self._weightsUp[iWeight])):
                        thisWeightUp *= getattr(chain, self._weightsUp[iWeight])
                    else:
                        thisWeightUp *= getattr(chain, self._weightsCentral[iWeight])
                    if not math.isnan(getattr(chain, self._weightsDown[iWeight])):
                        thisWeightDown *= getattr(chain, self._weightsDown[iWeight])
                    else:
                        thisWeightDown *= getattr(chain, self._weightsCentral[iWeight])

            total     += thisWeightCentral
            totalUp   += thisWeightUp
            totalDown += thisWeightDown

        return total, totalUp, totalDown

    def printSampleSystematic(self, mass, lifetime):
        if not hasattr(self, 'central'):
            print '"central" not defined, not printing systematic...'
            return (float ("nan"), float ("nan"), float ("nan"))

        sample = 'AMSB_chargino_' + str(mass) + 'GeV_' + str(lifetime) + 'cm_' + self.central['suffix']
        central, up, down = self.GetYieldFromTree(sample, self.central['condorDir'], self.central['name'], mass, lifetime)

        relDiffDown = (down - central) / central if central > 0.0 else 0.0
        relDiffUp = (up - central) / central if central > 0.0 else 0.0

        print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
        return (sample, relDiffDown, relDiffUp)

    def printSystematic(self):
        self._maxSystematic = 0.0
        self._averageSystematic = 0.0
        self._n = 0
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime)
                self._systematic.append ([sample, str (max (1.0 + relDiffDown, 1.0e-12)), str (max (1.0 + relDiffUp, 1.0e-12))])

                if abs (relDiffDown) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffDown)
                if abs (relDiffUp) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffUp)

                self._averageSystematic += abs (relDiffDown)
                self._averageSystematic += abs (relDiffUp)
                self._n += 2
        self._averageSystematic /= self._n

        print "maximum systematic: " + str (self._maxSystematic * 100.0) + "%"
        print "average systematic: " + str (self._averageSystematic * 100.0) + "%"

        if self._fout:
            width = max (len (word) for row in self._systematic for word in row) + 2
            for row in self._systematic:
                if row[0] in self._extraSamples:
                    extraRow = copy.deepcopy (row)
                    for sample in self._extraSamples[row[0]]:
                        extraRow[0] = sample
                        self._fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")

class TriggerTurnOnSystematic:

    _integrateHistogram = "Met Plots/metNoMu"
    _treeVariableName = "met_noMuPt"
    _fout = ""
    _doFout = False

    _systematic = []
    _maxSystematic = 0.0
    _averageSystematic = 0.0
    _n = 0

    _signalSuffix = ""
    _extraSamples = {}

    def __init__ (self, masses, lifetimes, intLumi):
        self._masses = masses
        self._lifetimes = lifetimes
        self._weightsCentral = [
            'eventvariable_lifetimeWeight',
            'eventvariable_isrWeight',
            'eventvariable_grandOrWeight',
            'eventvariable_puScalingFactor',
        ]
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_9_4_"):
            self._weightsCentral.append('eventvariable_L1ECALPrefiringWeight')
        if os.environ["CMSSW_VERSION"].startswith("CMSSW_10_2_"):
            self._weightsCentral.append('eventvariable_hem1516weight')
        self._intLumi = intLumi

    def addChannel (self, role, name, suffix, condorDir):
        channel = {"name" : name, "suffix" : suffix, "condorDir" : condorDir}
        setattr (self, role, channel)

    def addEfficiencies (self, role, name, inputFile):
        channel = {"name" : name, "inputFile" : inputFile}
        setattr (self, role, channel)

    def addSignalSuffix (self, signalSuffix):
        self._signalSuffix = signalSuffix
    
    def addExtraSamples (self, extraSamples):
        self._extraSamples = extraSamples

    def addIntegrateHistogram (self, integrateHistogram):
        self._integrateHistogram = integrateHistogram

    def addFout (self, fout):
        self._fout = fout
        self._doFout = True

    def getOriginalSample(self, condorDir, sample, mass, lifetime):
        lifetimeFloat = float(lifetime.replace('p', '.'))
        if os.path.isfile('condor/' + condorDir + '/' + sample + '.root') and lifetime != '1':
            for i in range(len(self._weightsCentral)):
                if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                    self._weightsCentral[i] = 'eventvariable_lifetimeWeight'
            return sample

        if lifetime in [10, 100, 1000, 10000]:
            raise Exception('Original sample condor/' + condorDir + '/' + sample + '.root does not exist!')

        originalLifetime = int(math.pow(10 , math.ceil((math.log10(lifetimeFloat)))))
        if originalLifetime == 1:
            originalLifetime = 10
        originalSample = 'AMSB_chargino_' + str(mass) + 'GeV_' + str(originalLifetime) + 'cm' + self._signalSuffix
        if not os.path.isfile('condor/' + condorDir + '/' + originalSample + '.root'):
            raise Exception('Original sample condor/' + condorDir + '/' + originalSample + '.root does not exist!')

        for i in range(len(self._weightsCentral)):
            if self._weightsCentral[i].startswith('eventvariable_lifetimeWeight'):
                self._weightsCentral[i] = 'eventvariable_lifetimeWeight_1000024_' + str(originalLifetime) + 'cmTo' + str(lifetime) + 'cm'

        return originalSample

    def GetHistogramFromTree(self, sample, condorDir, name, mass, lifetime):
        realSample = self.getOriginalSample(condorDir, sample, mass, lifetime)

        chain = TChain(name + 'TreeMaker/Tree')
        chain.Add('condor/' + condorDir + '/' + realSample + '/hist_*.root')

        if chain.GetEntries() == 0:
            h = TH1D(self._integrateHistogram, self._integrateHistogram, 2000, 0.0, 10000.0)
            h.SetDirectory(0)
            return h

        realInputFile = TFile('condor/' + condorDir + '/' + realSample + '.root')
        nGenerated = realInputFile.Get(name + 'CutFlowPlotter/eventCounter').GetEntries()
        crossSectionWeight = self._intLumi * float(signal_cross_sections[realSample.split('_')[2][:-3]]['value']) / nGenerated

        if 'eventvariable_lifetimeWeight_1000024_10cmTo1cm' in self._weightsCentral:
            h = TH1D(self._integrateHistogram, self._integrateHistogram, 2000, 0.0, 10000.0)
            for iEvent in range(chain.GetEntries()):
                chain.GetEntry(iEvent)
                w = crossSectionWeight
                for wgt in self._weightsCentral:
                    if wgt == 'eventvariable_lifetimeWeight_1000024_10cmTo1cm':
                        w *= GetMissingLifetimeWeight(chain)
                    else:
                        w *= getattr(chain, wgt)
                h.Fill(getattr(chain, self._treeVariableName), w)
            h.SetDirectory(0)
            return h

        weightString = str(crossSectionWeight)
        for w in self._weightsCentral:
            weightString = weightString + ' * ' + w

        chain.Draw(self._treeVariableName + ' >> h(2000, 0.0, 10000.0)', weightString, 'goff')
        h = gDirectory.Get('h') 
        h.SetDirectory(0)
        return h

    def printSampleSystematic (self, mass, lifetime):

        if hasattr (self, "central") and hasattr (self, "Denominator") and hasattr (self, "Numerator"):
            realLifetime = lifetime if lifetime != '1' else '10'
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (realLifetime) + "cm_" + self.central["suffix"]
            condorDir = self.central["condorDir"]
            name = self.central["name"]
            if os.path.isfile('condor/' + condorDir + '/' + sample + '.root') and lifetime != '1':
                metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            else:
                metHist = self.GetHistogramFromTree(sample, condorDir, name, mass, lifetime)
            central = metHist.Integral (0, metHist.GetNbinsX () + 1)

            denominatorEfficiencyFile = TFile (self.Denominator["inputFile"])
            denominatorEfficiency = denominatorEfficiencyFile.Get(self.Denominator["name"].replace('XYZ', str(mass)))
            numeratorEfficiencyFile = TFile (self.Numerator["inputFile"])
            numeratorEfficiency = numeratorEfficiencyFile.Get(self.Numerator["name"].replace('XYZ', str(mass)))

            scaledValue = 0.0

            for ibin in range(metHist.GetNbinsX()):
                x = metHist.GetBinCenter(ibin+1)
                scaledValue += metHist.GetBinContent(ibin+1) * numeratorEfficiency.Eval(x) / denominatorEfficiency.Eval(x) if denominatorEfficiency.Eval(x) > 0.0 else 0.0

            relDiff = (scaledValue - central) / central if central > 0.0 else 0.0
            if relDiff < 0.0:
                print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, scaledValue, central, central, (relDiff * 100.0), 0.0)
                return (sample, relDiff, 0.0)
            elif relDiff == 0.0:
                print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, central, central, central, 0.0, 0.0)
                return (sample, 0.0, 0.0)
            else:
                print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, central, central, scaledValue, 0.0, (relDiff * 100.0))
                return (sample, 0.0, relDiff)
        else:
            print "central, Denominator, and Denominator not all defined. Not printing systematic..."
            return (float ("nan"), float ("nan"), float ("nan"))

    def printSystematic (self):
        self._maxSystematic = 0.0
        self._averageSystematic = 0.0
        self._n = 0
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample, relDiffDown, relDiffUp = self.printSampleSystematic (mass, lifetime)
                self._systematic.append ([sample, str (max (1.0 + relDiffDown, 1.0e-12)), str (max (1.0 + relDiffUp, 1.0e-12))])

                if abs (relDiffDown) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffDown)
                if abs (relDiffUp) > self._maxSystematic:
                  self._maxSystematic = abs (relDiffUp)

                self._averageSystematic += abs (relDiffDown)
                self._averageSystematic += abs (relDiffUp)
                self._n += 2
        self._averageSystematic /= self._n

        print "maximum systematic: " + str (self._maxSystematic * 100.0) + "%"
        print "average systematic: " + str (self._averageSystematic * 100.0) + "%"

        if self._fout:
            width = max (len (word) for row in self._systematic for word in row) + 2
            for row in self._systematic:
                if row[0] in self._extraSamples:
                    extraRow = copy.deepcopy (row)
                    for sample in self._extraSamples[row[0]]:
                        extraRow[0] = sample
                        self._fout.write ("".join (word.ljust (width) for word in extraRow) + "\n")

                self._fout.write ("".join (word.ljust (width) for word in row) + "\n")
