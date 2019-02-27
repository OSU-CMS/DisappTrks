#!/usr/bin/env python
import os
import sys
import math
import copy
from array import array

from ROOT import gROOT, gStyle, TCanvas, TFile, TGraphAsymmErrors, TH1D, TMath, TPaveText, TObject, TLine, TH2D, TChain

from OSUT3Analysis.Configuration.Measurement import Measurement
from DisappTrks.StandardAnalysis.plotUtilities import *

setTDRStyle()

gROOT.SetBatch()
gStyle.SetOptStat(0)

def getExtraSamples (suffix):
    extraSamples = {
        "AMSB_chargino_100GeV_10000cm_" + suffix : [],
        "AMSB_chargino_100GeV_1000cm_" + suffix : [],
        "AMSB_chargino_100GeV_100cm_" + suffix : [],
        "AMSB_chargino_100GeV_10cm_" + suffix : [],
        "AMSB_chargino_100GeV_1cm_" + suffix : [],
        "AMSB_chargino_200GeV_10000cm_" + suffix : [],
        "AMSB_chargino_200GeV_1000cm_" + suffix : [],
        "AMSB_chargino_200GeV_100cm_" + suffix : [],
        "AMSB_chargino_200GeV_10cm_" + suffix : [],
        "AMSB_chargino_200GeV_1cm_" + suffix : [],
        "AMSB_chargino_300GeV_10000cm_" + suffix : [],
        "AMSB_chargino_300GeV_1000cm_" + suffix : [],
        "AMSB_chargino_300GeV_100cm_" + suffix : [],
        "AMSB_chargino_300GeV_10cm_" + suffix : [],
        "AMSB_chargino_300GeV_1cm_" + suffix : [],
        "AMSB_chargino_400GeV_10000cm_" + suffix : [],
        "AMSB_chargino_400GeV_1000cm_" + suffix : [],
        "AMSB_chargino_400GeV_100cm_" + suffix : [],
        "AMSB_chargino_400GeV_10cm_" + suffix : [],
        "AMSB_chargino_400GeV_1cm_" + suffix : [],
        "AMSB_chargino_500GeV_10000cm_" + suffix : [],
        "AMSB_chargino_500GeV_1000cm_" + suffix : [],
        "AMSB_chargino_500GeV_100cm_" + suffix : [],
        "AMSB_chargino_500GeV_10cm_" + suffix : [],
        "AMSB_chargino_500GeV_1cm_" + suffix : [],
        "AMSB_chargino_600GeV_10000cm_" + suffix : [],
        "AMSB_chargino_600GeV_1000cm_" + suffix : [],
        "AMSB_chargino_600GeV_100cm_" + suffix : [],
        "AMSB_chargino_600GeV_10cm_" + suffix : [],
        "AMSB_chargino_600GeV_1cm_" + suffix : [],
        "AMSB_chargino_700GeV_10000cm_" + suffix : [],
        "AMSB_chargino_700GeV_1000cm_" + suffix : [],
        "AMSB_chargino_700GeV_100cm_" + suffix : [],
        "AMSB_chargino_700GeV_10cm_" + suffix : [],
        "AMSB_chargino_700GeV_1cm_" + suffix : [],
        "AMSB_chargino_800GeV_10000cm_" + suffix : [],
        "AMSB_chargino_800GeV_1000cm_" + suffix : [],
        "AMSB_chargino_800GeV_100cm_" + suffix : [],
        "AMSB_chargino_800GeV_10cm_" + suffix : [],
        "AMSB_chargino_800GeV_1cm_" + suffix : [],
        "AMSB_chargino_900GeV_10000cm_" + suffix : [],
        "AMSB_chargino_900GeV_1000cm_" + suffix : [],
        "AMSB_chargino_900GeV_100cm_" + suffix : [],
        "AMSB_chargino_900GeV_10cm_" + suffix : [],
        "AMSB_chargino_900GeV_1cm_" + suffix : [],
    }

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

# defines a base class simply comparing the yields between central and up/down channels
class YieldSystematic:

    def __init__ (self, masses, lifetimes):
        self._masses = masses
        self._lifetimes = lifetimes

        self._integrateHistogram = "Met Plots/metNoMu"
        self._fout = ""
        self._doFout = False
        self._extraSamples = {}

        self._systematic = []
        self._maxSystematic = 0.0
        self._averageSystematic = 0.0
        self._n = 0

        # when "fluctuations" is used in EventWeights.py, there is no CutFlowPlotter
        # but the "total, totalError" remain the same as the central value channel
        self._isWeightFluctuation = False

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

    def checkLifetimeReweight (self, condorDir, sample, mass, lifetime):
        lifetimeFloat = float(lifetime.replace('p', '.'))
        lifetime_reweight_flag = False
        if not os.path.isfile( "condor/%s/%s.root" % (condorDir,sample) ):
            if lifetime not in [1, 10, 100, 1000, 10000]:
                ceil_lifetime = int(math.pow(10 , math.ceil((math.log10( lifetimeFloat )))))
                sample_origin = "AMSB_chargino_" + str (mass) + "GeV_" + str (ceil_lifetime) + "cm_" + self.central["suffix"]
                if os.path.isfile( "condor/%s/%s.root" % (condorDir,sample_origin) ):
                    sample = sample_origin
                    lifetime_reweight_flag = True
                else:
                    raise Exception('Sample\n{0}\n{1}\ncan not be found'.format(sample,sample_origin))
            else:
                raise Exception('Sample {} can not be found'.format(sample))
        else:
            ceil_lifetime = lifetime
            sample_origin = sample
        return sample, ceil_lifetime, lifetime_reweight_flag

    def GetValue (self, sample, condorDir, name, ceil_lifetime, lifetime, lifetime_reweight_flag):

        total = 0
        chain = TChain( name + "TreeMaker/Tree")
        chain.Add("condor/"+condorDir + "/" + sample + "/*.root")
        totalWeight = 0

        for i_event in range(chain.GetEntries()):
            chain.GetEntry(i_event)
            lifetimeWeight       = chain.eventvariable_lifetimeWeight
            isrWeight            = chain.eventvariable_isrWeight
            grandOrTriggerWeight = chain.eventvariable_grandOrWeight
            puWeight             = chain.eventvariable_puScalingFactor
            if lifetime_reweight_flag == True:
                lifetimeReweight  = getattr(chain, 'eventvariable_lifetimeWeight_1000024_'+ str(ceil_lifetime) +'cmTo'+str(lifetime)+'cm')
                total            +=  lifetimeReweight
                totalWeight      +=  lifetimeReweight * lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight
            else:
                total            +=  1.0
                totalWeight      +=  lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight
            
        return total, totalWeight
 

    def printSampleSystematic (self, mass, lifetime):
        if hasattr (self, "central") and hasattr (self, "down") and hasattr (self, "up"):
           
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]
            input_sample = sample
            condorDir = self.central["condorDir"]
            lifetime_reweight_flag = False
            name = self.central["name"]

            sample, ceil_lifetime, lifetime_reweight_flag = self.checkLifetimeReweight ( condorDir, sample, mass, lifetime )

            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            central_total = total
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central_ref = metHist.Integral (0, metHist.GetNbinsX () + 1) / total
            raw_total = total * total / (totalError * totalError)

            total, totalWeight = self.GetValue (sample, condorDir, name, ceil_lifetime, lifetime, lifetime_reweight_flag)

            central_total = total
            central = totalWeight / raw_total if total > 0.0 else 0.0

            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.down["suffix"]
            condorDir = self.down["condorDir"]
            name = self.down["name"]

            sample, ceil_lifetime, lifetime_reweight_flag = self.checkLifetimeReweight ( condorDir, sample, mass, lifetime )

            if not self._isWeightFluctuation:
                total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)  
            metHist = getHist (sample, condorDir, name + "Plotter" if not self._isWeightFluctuation else name, self._integrateHistogram)
            down_ref = metHist.Integral (0, metHist.GetNbinsX () + 1) / total
            raw_total_down = total * total / (totalError * totalError)

            total, totalWeightDown = self.GetValue (sample, condorDir, name, ceil_lifetime, lifetime, lifetime_reweight_flag)

            if not self._isWeightFluctuation:
                down = totalWeightDown / raw_total_down if raw_total_down > 0.0 else 0.0
            else:
                down = totalWeightDown / raw_total if raw_total > 0.0 else 0.0

                 
        
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.up["suffix"]
            condorDir = self.up["condorDir"]
            name = self.up["name"]

            sample, ceil_lifetime, lifetime_reweight_flag = self.checkLifetimeReweight ( condorDir, sample, mass, lifetime )
            if not self._isWeightFluctuation:
                total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter" if not self._isWeightFluctuation else name, self._integrateHistogram)
            up_ref = metHist.Integral (0, metHist.GetNbinsX () + 1) / total
            raw_total_up = total * total / (totalError * totalError)

            total, totalWeightUp = self.GetValue (sample, condorDir, name, ceil_lifetime, lifetime, lifetime_reweight_flag)

            if not self._isWeightFluctuation:
                up = totalWeightUp / raw_total_up if raw_total_up > 0.0 else 0.0
            else:
                up = totalWeightUp / raw_total if raw_total > 0.0 else 0.0


            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0
            print "input dataset:", input_sample
            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (input_sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (input_sample, relDiffDown, relDiffUp)

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

class TriggerSystematic(YieldSystematic):

    def __init__ (self, masses, lifetimes):
        YieldSystematic.__init__ (self, masses, lifetimes)
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

    def GetValue (self, sample, condorDir, name, ceil_lifetime, lifetime, lifetime_reweight_flag, fluctuation = None):
        total = 0
        chain = TChain( name + "TreeMaker/Tree")
        chain.Add("condor/"+condorDir + "/" + sample + "/*.root")
        totalWeight = 0

        for i_event in range(chain.GetEntries()):
            chain.GetEntry(i_event)
            lifetimeWeight       = chain.eventvariable_lifetimeWeight
            isrWeight            = chain.eventvariable_isrWeight
            grandOrTriggerWeight = chain.eventvariable_grandOrWeight
            puWeight             = chain.eventvariable_puScalingFactor

            if not fluctuation is None:
                grandOrTriggerWeight_fluc = getattr(chain,"eventvariable_" + fluctuation)
            else:
                grandOrTriggerWeight_fluc = grandOrTriggerWeight
            if lifetime_reweight_flag == True:
                lifetimeReweight  = getattr(chain, 'eventvariable_lifetimeWeight_1000024_'+ str(ceil_lifetime) +'cmTo'+str(lifetime)+'cm')
                total            +=  lifetimeReweight
                totalWeight      +=  lifetimeReweight * lifetimeWeight * isrWeight * grandOrTriggerWeight_fluc * puWeight
            else:
                total            +=  1.0
                totalWeight      +=  lifetimeWeight * isrWeight * grandOrTriggerWeight_fluc * puWeight

        return total, totalWeight

    def printSampleSystematic (self, mass, lifetime, fluctuation):
        if hasattr (self, "central") and hasattr (self, "down") and hasattr (self, "up"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]
            input_sample = sample
            condorDir = self.central["condorDir"]
            name = self.central["name"]

            sample, ceil_lifetime, lifetime_reweight_flag = self.checkLifetimeReweight ( condorDir, sample, mass, lifetime )

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central_ref = metHist.Integral ()
            total, totalWeight = self.GetValue (sample, condorDir, name, ceil_lifetime, lifetime, lifetime_reweight_flag)
            total_central = total

            sample, ceil_lifetime, lifetime_reweight_flag = self.checkLifetimeReweight ( condorDir, sample, mass, lifetime )
            metHist = getHist (sample, condorDir, name + "Plotter_" + fluctuation + "Down", self._integrateHistogram)
            down_ref = metHist.Integral ()
            total, totalWeightDown = self.GetValue (sample, condorDir, name, ceil_lifetime, lifetime, lifetime_reweight_flag, fluctuation + "Down")

            sample, ceil_lifetime, lifetime_reweight_flag = self.checkLifetimeReweight ( condorDir, sample, mass, lifetime )
            metHist = getHist (sample, condorDir, name + "Plotter_" + fluctuation + "Up", self._integrateHistogram, fluctuation + "Up")
            up_ref = metHist.Integral ()
            total, totalWeightUp = self.GetValue (sample, condorDir, name, ceil_lifetime, lifetime, lifetime_reweight_flag)

            central = totalWeight
            down    = totalWeightDown
            up      = totalWeightUp

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (input_sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (input_sample, relDiffDown, relDiffUp)

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

class MetSystematic(YieldSystematic):

    def __init__ (self, masses, lifetimes):
        YieldSystematic.__init__ (self, masses, lifetimes)
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
        if hasattr (self, "central") and hasattr (self, "down") and hasattr (self, "up"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]
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

            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (sample, relDiffDown, relDiffUp)

        elif hasattr (self, "central") and not hasattr (self, "down") and not hasattr (self, "up"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.central["suffix"]
            input_sample = sample
            lifetime_reweight_flag = False
            condorDir = self.central["condorDir"]
            lifetimeFloat = float(lifetime.replace('p', '.'))
            if not os.path.isfile( "condor/%s/%s.root" % (condorDir,sample) ):
                if lifetime not in [1, 10, 100, 1000, 10000]:
                    ceil_lifetime = int(math.pow(10 , math.ceil((math.log10( lifetimeFloat )))))
                    sample_origin = "AMSB_chargino_" + str (mass) + "GeV_" + str (ceil_lifetime) + "cm_" + self.central["suffix"]
                    if os.path.isfile( "condor/%s/%s.root" % (condorDir,sample_origin) ):
                        sample = sample_origin
                        lifetime_reweight_flag = True
                    else:
                        raise Exception('Sample\n{0}\n{1}\ncan not be found'.format(sample,sample_origin))
                else:
                    raise Exception('Sample {} can not be found'.format(sample))
            

            name = self.central["name"]

            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            total = metHist.Integral (0, metHist.GetNbinsX () + 1)
            central_ref = metHist.Integral (metHist.GetXaxis ().FindBin (self._metCut), metHist.GetNbinsX () + 1) / total if total > 0.0 else 0.0

            chain = TChain( name + "TreeMaker/Tree")
            chain.Add("condor/"+condorDir + "/" + sample + "/*.root")

            raw_total = total 
            totalWeight = 0
            totalWeightUp = 0
            totalWeightDown = 0
            totalWeight_lifetime = 0

            for i_event in range(chain.GetEntries()):
                chain.GetEntry(i_event)
                met               = getattr(chain, "met_noMuPt")
                metUp             = getattr(chain, "met_noMuPt_" + metType + "Up")
                metDown           = getattr(chain, "met_noMuPt_" + metType + "Down")
                lifetimeWeight       = chain.eventvariable_lifetimeWeight
                isrWeight            = chain.eventvariable_isrWeight
                grandOrTriggerWeight = chain.eventvariable_grandOrWeight
                puWeight             = chain.eventvariable_puScalingFactor

                if lifetime_reweight_flag == True:
                    lifetimeReweight  = getattr(chain, 'eventvariable_lifetimeWeight_1000024_'+ str(ceil_lifetime) +'cmTo'+str(lifetime)+'cm') 
                    totalWeight      += int( met > self._metCut ) * lifetimeReweight * lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight
                    totalWeightUp    += int( metUp > self._metCut ) * lifetimeReweight * lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight
                    totalWeightDown  += int( metDown > self._metCut ) * lifetimeReweight * lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight
                else:
                    totalWeight      += int( met > self._metCut ) * lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight
                    totalWeightUp    += int( metUp > self._metCut ) * lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight
                    totalWeightDown  += int( metDown > self._metCut ) * lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight

            central = totalWeight / raw_total if raw_total > 0.0 else 0.0
            up      = totalWeightUp / raw_total if raw_total > 0.0 else 0.0
            down    = totalWeightDown / raw_total if raw_total > 0.0 else 0.0

            print central , up , down , total 

            if (lifetime_reweight_flag == False) and  abs( (central-central_ref) ) > 0.001:
                print "Something might go wrong with central value"
                print "central = ", central
                print "central from histogram = ", central_ref
            else:
                print "central values match"

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(%s) down: %f, central: %f, up: %f, systematic uncertainty: %f%%/%f%%" % (input_sample, down, central, up, (relDiffDown * 100.0), (relDiffUp * 100.0))
            return (input_sample, relDiffDown, relDiffUp)

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
        elif hasattr (self, "PileupCentral") and not hasattr (self, "PileupDown") and not hasattr (self, "PileupUp"):
            sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm_" + self.PileupCentral["suffix"]
            input_sample = sample
            lifetime_reweight_flag = False
            condorDir = self.PileupCentral["condorDir"]
            lifetimeFloat = float(lifetime.replace('p', '.'))
            if not os.path.isfile( "condor/%s/%s.root" % (condorDir,sample) ):
                if lifetime not in [1, 10, 100, 1000, 10000]:
                    ceil_lifetime = int(math.pow(10 , math.ceil((math.log10( lifetimeFloat )))))
                    sample_origin = "AMSB_chargino_" + str (mass) + "GeV_" + str (ceil_lifetime) + "cm_" + self.PileupCentral["suffix"]
                    if os.path.isfile( "condor/%s/%s.root" % (condorDir,sample_origin) ):
                        sample = sample_origin
                        lifetime_reweight_flag = True
                    else:
                        raise Exception('Sample\n{0}\n{1}\ncan not be found'.format(sample,sample_origin))
                else:
                    raise Exception('Sample {} can not be found'.format(sample))
            

            name = self.PileupCentral["name"]
            total, totalError = getYieldInBin (sample, condorDir, name + "CutFlowPlotter", 1)
            metHist = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)
            central_ref = metHist.Integral (0, metHist.GetNbinsX () + 1) / total

            chain = TChain( name + "TreeMaker/Tree")
            chain.Add("condor/"+condorDir + "/" + sample + "/*.root")
            totalWeight = 0
            totalWeightUp = 0
            totalWeightDown = 0
            totalWeight_lifetime = 0

            if lifetime_reweight_flag == True:
                lifetimeReweight_cmd = 'lifetimeReweight =   chain.eventvariable_lifetimeWeight_1000024_'+ str(ceil_lifetime) +'cmTo'+str(lifetime)+'cm'
            for i_event in range(chain.GetEntries()):
                chain.GetEntry(i_event)
                lifetimeWeight       = chain.eventvariable_lifetimeWeight
                isrWeight            = chain.eventvariable_isrWeight
                grandOrTriggerWeight = chain.eventvariable_grandOrWeight 
                puWeight             = chain.eventvariable_puScalingFactor
                puWeightUp           = chain.eventvariable_puScalingFactorUp
                puWeightDown         = chain.eventvariable_puScalingFactorDown
                # print "i_event:  " , i_event, " lifetimeWeight: ", lifetimeWeight, "  isrWeight:  ", isrWeight, " grandOrWeight: ", grandOrTriggerWeight, " puweight: ", puWeight, "  puWeightUp:  ", puWeightUp, " puWeightDown: ", puWeightDown
                if lifetime_reweight_flag == True:
                    exec(lifetimeReweight_cmd)
                    totalWeight      += lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight * lifetimeReweight
                    totalWeightUp    += lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeightUp * lifetimeReweight
                    totalWeightDown  += lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeightDown * lifetimeReweight
                else:
                    totalWeight      += lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeight 
                    totalWeightUp    += lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeightUp 
                    totalWeightDown  += lifetimeWeight * isrWeight * grandOrTriggerWeight * puWeightDown
            
            raw_total = total * total / (totalError * totalError)                
            central = totalWeight / raw_total
            up      = totalWeightUp / raw_total
            down    = totalWeightDown / raw_total
         
            print central , up , down , total , raw_total

            if (lifetime_reweight_flag == False)  and abs( central-central_ref ) > 0.001:
                print "Something might go wrong with central value"
                print "central = ", central
                print "central from histogram = ", central_ref
            else:
                print "central values match"

            relDiffDown = (down - central) / central if central > 0.0 else 0.0
            relDiffUp = (up - central) / central if central > 0.0 else 0.0

            print "(" + input_sample + ") down: " + str (down) + ", central: " + str (central) + ", up: " + str (up) + ", systematic uncertainty: " + str (relDiffDown * 100.0) + "%/" + str (relDiffUp * 100.0) + "%"
            return (input_sample, relDiffDown, relDiffUp)
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

    def __init__ (self, masses, lifetimes):
        self._masses = masses
        self._lifetimes = lifetimes

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

    def getNMissOutEfficiency (self, dataOrMC, nLow, nHigh = -1, hits = None, sample = None):
        if hasattr (self, dataOrMC):
            if not hits:
                channel = getattr (self, dataOrMC)
                if dataOrMC != "Signal":
                    sample = channel["sample"]
                condorDir = channel["condorDir"]
                name = channel["name"]
                hits = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)

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

    def getSignalYield (self, mass, lifetime, nLow, nHigh = -1, hits = None):
        if hasattr (self, "Signal"):
            if not hits:
                channel = getattr (self, "Signal")
                sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm" + self._signalSuffix
                condorDir = channel["condorDir"]
                name = channel["name"]
                hits = getHist (sample, condorDir, name + "Plotter", self._integrateHistogram)

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
        lifetimes = map (float, self._lifetimes)
        massBins = array ("d", masses + [masses[-1] + 100])
        lifetimeBins = array ("d", lifetimes + [lifetimes[-1] * 10.0])
        h = TH2D ("nMissOutSystematic", ";chargino mass [GeV];chargino lifetime [cm/c]", len (massBins) - 1, massBins, len (lifetimeBins) - 1, lifetimeBins)
        for mass in self._masses:
            for lifetime in self._lifetimes:
                sample = "AMSB_chargino_" + str (mass) + "GeV_" + str (lifetime) + "cm" + self._signalSuffix
                eTrue3ToInf, signalHits = self.getNMissOutEfficiency ("Signal", 3, 12, hits = None, sample = sample)
                eTrue2, signalHits = self.getNMissOutEfficiency ("Signal", 2, 2, hits = signalHits, sample = sample)
                eTrue1, signalHits = self.getNMissOutEfficiency ("Signal", 1, 1, hits = signalHits, sample = sample)
                eTrue0, signalHits = self.getNMissOutEfficiency ("Signal", 0, 0, hits = signalHits, sample = sample)

                eMC1ToInf, mcHits = self.getNMissOutEfficiency ("MC", 1, 12, hits = mcHits)
                eMC2ToInf, mcHits = self.getNMissOutEfficiency ("MC", 2, 12, hits = mcHits)
                eMC3ToInf, mcHits = self.getNMissOutEfficiency ("MC", 3, 12, hits = mcHits)

                eData1ToInf, dataHits = self.getNMissOutEfficiency ("Data", 1, 12, hits = dataHits)
                eData2ToInf, dataHits = self.getNMissOutEfficiency ("Data", 2, 12, hits = dataHits)
                eData3ToInf, dataHits = self.getNMissOutEfficiency ("Data", 3, 12, hits = dataHits)

                mcEff = eTrue3ToInf + eTrue2 * eMC1ToInf + eTrue1 * eMC2ToInf + eTrue0 * eMC3ToInf
                dataEff = eTrue3ToInf + eTrue2 * eData1ToInf + eTrue1 * eData2ToInf + eTrue0 * eData3ToInf
                #mcEff = eTrue2 * eMC1ToInf + eTrue1 * eMC2ToInf + eTrue0 * eMC3ToInf
                #dataEff = eTrue2 * eData1ToInf + eTrue1 * eData2ToInf + eTrue0 * eData3ToInf

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
