#!/usr/bin/python

import os
import sys
import math

from ROOT import gROOT, gStyle, TFile, TH2D, TCanvas, TEllipse, TLatex, TH1D

from DisappTrks.StandardAnalysis.plotUtilities import *
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import *

gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

class FiducialMapCalculator:
    _fout = None
    _canvas = None
    _plotLabel = float ("nan")
    _histogramName = 'Track Plots/trackEtaVsPhi'
    _thresholdInSigma = 2.0
    _luminosityInInvFb = float ("nan")
    _meanInefficiency = 0.0
    _stdDevInefficiency = 0.0
    _hotSpotsList = []
    _verboseComparison = False

    def __init__(self):
        pass

    def addTFile(self, fout):
        self._fout = fout

    def addTCanvas(self, canvas):
        self._canvas = canvas

    def setHistogramName(self, name):
        self._histogramName = name

    def setThresholdInSigma(self, threshold):
        self._thresholdInSigma = threshold

    def addLuminosityInInvPb(self, luminosityInInvPb):
        self._luminosityInInvFb = luminosityInInvPb / 1000.0

    def setVerboseComparison(self, isVerbose):
        self._verboseComparison = isVerbose

    def addChannel(self, role, name, sample, condorDir):
        channel = {"name" : name, "sample" : sample, "condorDir" : condorDir}
        channel["histogram"] = getHist(sample, condorDir, name + "Plotter", self._histogramName)
        setattr(self, role, channel)
        print("yield for " + name + ": " + str(channel["histogram"].Integral()))

    def FindHotSpots(self, beforeVeto, afterVeto):
        hotSpots = []
        totalEventsBeforeVeto = 0
        totalEventsAfterVeto = 0
        nRegionsWithTag = 0

        # loop over all bins in eta-phi and count events before/after to calculate the mean inefficiency
        for xbin in range(1, beforeVeto.GetXaxis().GetNbins()):
            for ybin in range(1, beforeVeto.GetYaxis().GetNbins()):
                if beforeVeto.GetBinContent(xbin, ybin) > 0:
                    nRegionsWithTag += 1
                else:
                    continue
                totalEventsBeforeVeto += beforeVeto.GetBinContent(xbin, ybin)
                totalEventsAfterVeto  += afterVeto.GetBinContent(xbin, ybin)
        meanInefficiency = totalEventsAfterVeto / totalEventsBeforeVeto

        print('\nMean inefficiency (including any hot spots) = ', meanInefficiency)
        meanInefficiency_withHotSpots = meanInefficiency

        # now with the mean, calculate the standard deviation as stdDev^2 = 1/(N-1) * sum(inefficiency - meanInefficiency)^2
        stdDevInefficiency = 0

        efficiency = afterVeto.Clone('efficiency')
        efficiency.Divide(beforeVeto)

        for xbin in range(1, efficiency.GetXaxis().GetNbins()):
            for ybin in range(1, efficiency.GetYaxis().GetNbins()):
                if beforeVeto.GetBinContent(xbin, ybin) == 0:
                    continue
                thisInefficiency = efficiency.GetBinContent(xbin, ybin)
                stdDevInefficiency += (thisInefficiency - meanInefficiency)**2

        if nRegionsWithTag < 2:
            print('Only ', nRegionsWithTag, ' regions with a tag lepton exist, cannot calculate fiducial map!!!')
            return hotSpots

        stdDevInefficiency /= nRegionsWithTag - 1
        stdDevInefficiency = math.sqrt(stdDevInefficiency)

        self._meanInefficiency = meanInefficiency
        self._stdDevInefficiency = stdDevInefficiency

        print(f"Standard Dev of Inefficiency: {stdDevInefficiency}, nRegions: {nRegionsWithTag}")

        # now find hot spots where the inefficiency is larger than the meanInefficiency by at least threshold * stdDevInefficiency

        for xbin in range(1, efficiency.GetXaxis().GetNbins()):
            for ybin in range(1, efficiency.GetYaxis().GetNbins()):
                thisInefficiency = efficiency.GetBinContent(xbin, ybin)
                if thisInefficiency == 0:
                    continue
                if (thisInefficiency - meanInefficiency) > self._thresholdInSigma * stdDevInefficiency:
                    eta = "{0:0.2f}".format(efficiency.GetXaxis().GetBinCenter(xbin))
                    phi = "{0:0.2f}".format(efficiency.GetYaxis().GetBinCenter(ybin))
                    hotSpots.append((eta, phi))

        # do this again to calculate the mean inefficiency without hot spots
        totalEventsBeforeVeto = 0
        totalEventsAfterVeto = 0

        for xbin in range(1, beforeVeto.GetXaxis().GetNbins()):
            for ybin in range(1, beforeVeto.GetYaxis().GetNbins()):
                if beforeVeto.GetBinContent(xbin, ybin) <= 0:
                    continue
                isHotSpot_ = False
                for hs_ in hotSpots:
                    eta = "{0:0.2f}".format(efficiency.GetXaxis().GetBinCenter(xbin))
                    phi = "{0:0.2f}".format(efficiency.GetYaxis().GetBinCenter(ybin))
                    if hs_[0] == eta and hs_[1] == phi:
                        isHotSpot_ = True
                        break
                if isHotSpot_:
                        continue
                totalEventsBeforeVeto += beforeVeto.GetBinContent(xbin, ybin)
                totalEventsAfterVeto  += afterVeto.GetBinContent(xbin, ybin)
        meanInefficiency = totalEventsAfterVeto / totalEventsBeforeVeto

        print('Mean inefficiency (excluding identified hot spots) = ', meanInefficiency)
        meanInefficiency_withoutHotSpots = meanInefficiency
        print('\nRatio of mean inefficiency excluding/including hot spots = ', meanInefficiency_withoutHotSpots / meanInefficiency_withHotSpots, '\n')
        print('\nPercentage drop = ', (meanInefficiency_withoutHotSpots - meanInefficiency_withHotSpots) / meanInefficiency_withHotSpots)
        print('\nPer-invfb rate, difference = ', (meanInefficiency_withoutHotSpots - meanInefficiency_withHotSpots) / self._luminosityInInvFb)

        return hotSpots

    def CalculateFiducialMap(self):
        if not hasattr(self, "Numerator") or not hasattr(self, "Denominator"):
            print("Either Numerator or Denominator has not been defined. Not finding hot spots...")
            self._hotSpotsList = []
            return

        self._hotSpotsList = self.FindHotSpots(self.Denominator["histogram"], self.Numerator["histogram"])

        self._fout.cd()
        self.Denominator["histogram"].Write('beforeVeto')
        self.Numerator["histogram"].Write('afterVeto')

    def MakePlots(self):
        if not hasattr(self, "Numerator") or not hasattr(self, "Denominator"):
            print("Either Numerator or Denominator has not been defined. Not finding hot spots...")
            return

        circles = []
        for spots in self._hotSpotsList:
            circle = TEllipse(float(spots[0]), float(spots[1]), 0.06)
            circle.SetLineColor(820) # kSpring
            circle.SetLineWidth(1)
            circle.SetFillStyle(0)
            circles.append(circle)

        LumiText = str.format('{0:.1f}', self._luminosityInInvFb) + " fb^{-1} (13 TeV)"

        pasLumiLatex = TLatex()
        pasLumiLatex.SetNDC()
        pasLumiLatex.SetTextAngle(0)
        pasLumiLatex.SetTextFont(42)
        pasLumiLatex.SetTextAlign(32)
        pasLumiLatex.SetTextSize(0.04)

        pasCMSLatex = TLatex()
        pasCMSLatex.SetNDC()
        pasCMSLatex.SetTextAngle(0)
        pasCMSLatex.SetTextFont(62)
        pasCMSLatex.SetTextAlign(12)
        pasCMSLatex.SetTextSize(0.04)

        pasPrelimLatex = TLatex()
        pasPrelimLatex.SetNDC()
        pasPrelimLatex.SetTextAngle(0)
        pasPrelimLatex.SetTextFont(62)
        pasPrelimLatex.SetTextAlign(12)
        pasPrelimLatex.SetTextSize(0.04)

        self.Denominator["histogram"].Draw('colz')
        pasLumiLatex.DrawLatex(0.96, 0.93, LumiText)
        pasCMSLatex.DrawLatex(0.12, 0.925, "CMS Preliminary")
        self._canvas.SaveAs('fiducialMapCalc_beforeVeto_' + self.Denominator["sample"] + '.pdf')

        self.Numerator["histogram"].Draw('colz')
        pasLumiLatex.DrawLatex(0.96, 0.93, LumiText)
        pasCMSLatex.DrawLatex(0.12, 0.925, "CMS Preliminary")
        self._canvas.SaveAs('fiducialMapCalc_afterVeto_' + self.Numerator["sample"] + '.pdf')

        self._canvas.SetLogz(False)
        self.Numerator["histogram"].Divide(self.Denominator["histogram"])
        self.Numerator["histogram"].Draw('colz')

        if 'SingleEle' in self.Numerator["sample"]:
            self.Numerator["histogram"].GetZaxis().SetRangeUser(0, 0.5)
        elif 'SingleMu' in self.Numerator["sample"]:
            self.Numerator["histogram"].GetZaxis().SetRangeUser(0, 0.05)
        self.Numerator["histogram"].GetZaxis().SetLabelSize(0.025)

        for circle in circles:
            circle.Draw("same")

        pasLumiLatex.DrawLatex(0.96, 0.93, LumiText)
        pasCMSLatex.DrawLatex(0.12, 0.925, "CMS Preliminary")
        self._canvas.SaveAs('fiducialMapCalc_efficiency_' + self.Numerator["sample"] + '.pdf')

        h_rawSigma = TH1D('rawSigma', 'rawSigma', 40, -20, 20)

        for xbin in range(1, self.Numerator["histogram"].GetXaxis().GetNbins()):
            for ybin in range(1, self.Numerator["histogram"].GetYaxis().GetNbins()):

                thisInefficiency = self.Numerator["histogram"].GetBinContent(xbin, ybin)
                if thisInefficiency == 0:
                    continue

                valueInSigma = (thisInefficiency - self._meanInefficiency) / self._stdDevInefficiency

                h_rawSigma.Fill(valueInSigma)

                if valueInSigma < 0:
                    valueInSigma = 0

                self.Numerator["histogram"].SetBinContent(xbin, ybin, valueInSigma)

        fout_rawSigma = TFile('rawSigma.root', 'recreate')
        h_rawSigma.Write('rawSigma')
        fout_rawSigma.Close()

        self._canvas.SetLogz(False)
        self.Numerator["histogram"].GetZaxis().SetLabelSize(0.04)
        self.Numerator["histogram"].Draw('colz')

        if 'SingleEle' in self.Numerator["sample"]:
            if '2017' in self.Numerator["sample"]:
                self.Numerator["histogram"].GetZaxis().SetRangeUser(0, 7)
            self.Numerator["histogram"].GetZaxis().SetRangeUser(0, 12)
        elif 'SingleMu' in self.Numerator["sample"]:
            self.Numerator["histogram"].GetZaxis().SetRangeUser(0, 23)
        self.Numerator["histogram"].GetZaxis().SetLabelSize(0.025)

        for circle in circles:
            circle.Draw("same")

        pasLumiLatex.DrawLatex(0.96, 0.93, LumiText)
        pasCMSLatex.DrawLatex(0.12, 0.925, "CMS Preliminary")
        self._canvas.SaveAs('fiducialMapCalc_efficiencyInSigma_' + self.Numerator["sample"] + '.pdf')

    def CompareFiducialMap(self):
        # first get the list of existing hot spots from the fiducial map
        existingHotSpots = []
        existingMapName = os.environ['CMSSW_BASE'] + '/src/OSUT3Analysis/Configuration/data/'
        existingMapName += 'electronFiducialMap_' if ('SingleEle' in self.Numerator["sample"] or 'EGamma' in self.Numerator["sample"]) else 'muonFiducialMap_'
        if '2015' in self.Numerator["sample"]:
            existingMapName += '2015_data.root'
        elif '2016' in self.Numerator["sample"]:
            existingMapName += '2016ReReco_data.root'
        elif '2017' in self.Numerator["sample"]:
            existingMapName += '2017_data.root'
        elif '2018' in self.Numerator["sample"]:
            existingMapName += '2017_data.root' # doesn't exist yet, compare to 2017
        elif '2022' in self.Numerator['sample']:
            existingMapName += '2022F_data.root' #doesn't exist yet, compare to 2017
        existingMapFile = TFile(existingMapName, 'read')
        existingMapDenominator = existingMapFile.Get('beforeVeto')
        existingMapNumerator = existingMapFile.Get('afterVeto')
        oldHotSpots = self.FindHotSpots(existingMapDenominator, existingMapNumerator)
        existingMapFile.Close()

        print("********************************************************************************")
        print("Compared to the existing map (" + existingMapName + "):")
        print("********************************************************************************")

        if self._verboseComparison:
            print('\n\nHot spots that went away with new data:')
        nWentAway = 0
        # look through all the old hot spots
        for old in oldHotSpots:
            thisInNew = False

            # look through all the new ones and see if we find the old one
            for new in self._hotSpotsList:
                if old == new:
                    thisInNew = True
                    break

            # if you didn't find the old spot in the new list, it went away
            if not thisInNew:
                if self._verboseComparison:
                    print(old)
                nWentAway += 1

        print('Total hot spots that went away = ', nWentAway)

        if self._verboseComparison:
            print('\nNew hot spots:')
        nNewSpots = 0
        # look through new hot spots
        for new in self._hotSpotsList:
            thisInOld = False

            # look through all the old ones and see if we find the new one
            for old in oldHotSpots:
                if new == old:
                    thisInOld = True
                    break

            # if you didn't find the new spot in the old list, it appeared as a new one
            if not thisInOld:
                if self._verboseComparison:
                    print(new)
                nNewSpots += 1

        print('Total new hot spots = ', nNewSpots)

        if self._verboseComparison:
            print('\nHot spots that are in both maps:')
        nInBoth = 0
        # look thorugh old list
        for old in oldHotSpots:

            # look through the new list and see if we find the new one
            for new in self._hotSpotsList:
                if old == new:
                    if self._verboseComparison:
                        print(old)
                    nInBoth += 1

        print('Total that were in both = ', nInBoth)

def remakePayload(flavor, year, eras = ['']):
    combineInclusive = (len(eras) > 1)
    fNewPayload = TFile(flavor + '.root', 'RECREATE')
    for era in eras:
        fInput = TFile('new' + flavor + 'FiducialMap_2018' + era + '.root', 'READ')
        hBefore = fInput.Get('beforeVeto')
        hAfter = fInput.Get('afterVeto')
        fNewPayload.cd()
        hBefore.Write('beforeVeto_2018' + era)
        hAfter.Write('afterVeto_2018' + era)
        if combineInclusive:
            if era == eras[0]:
                hBefore_inclusive = hBefore.Clone()
                hAfter_inclusive = hAfter.Clone()
                hBefore_inclusive.SetDirectory(0)
                hAfter_inclusive.SetDirectory(0)
            else:
                hBefore_inclusive.Add(hBefore)
                hAfter_inclusive.Add(hAfter)
    if combineInclusive:
        fNewPayload.cd()
        hBefore_inclusive.Write('beforeVeto')
        hAfter_inclusive.Write('afterVeto')
    fNewPayload.Close()
    print('\nNew fiducial map payload file: ' + flavor + '.root')
