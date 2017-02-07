#!/usr/bin/env python

import os, glob, tarfile, re, math, copy
from ROOT import TFile, TH1D, TGraphAsymmErrors, Double

TH1D.SetDefaultSumw2 ()

numerator = {}

class HLTRate:
  _denominator = 0
  _crossSectionInPb = 0.0
  _nFiles = 0
  _iFile = 0
  _label = ""

  _denominatorHist = None
  _numeratorHist = None
  _rateGraph = None

  def addFile (self, fileName):
    if not fileName:
      return
    if not os.path.isfile (fileName):
      print "\"" + fileName + "\" does not exist or is not a file!"
      return
    if not re.match (r".*\/cmsRun_.*\.log\.tar\.gz", fileName):
      print "\"" + fileName + "\" does not look like a CRAB log file!"
      return

    print "  (" + str (self._iFile) + " / " + str (self._nFiles) + ") Processing file \"" + re.sub (r".*\/([^/]+)$", r"\1", fileName) + "\"..."

    n = re.sub (r".*\/cmsRun_(.*)\.log\.tar\.gz", r"\1", fileName)

    print "    Extracting log file..."

    tin = tarfile.open (fileName)
    fin = tin.extractfile ("cmsRun-stdout-" + n + ".log")

    print "    Parsing log file..."

    for line in fin:
      line = line.rstrip ()
      if not re.match (r"HLT-Report.*", line):
        continue
      if re.match (r".*Events total = .* wasrun = .* passed = .* errors = .*", line):
        self._denominator += int (re.sub (r".*Events total = (.*) wasrun = .* passed = .* errors = .*", r"\1", line))
      if re.match (r".*ETM[^_]*_MET75_IsoTrk50.*", line):
        seed = re.sub (r".*ETM([^_]*)_MET75_IsoTrk50.*", r"\1", line)
        if seed not in numerator[self._label]:
          numerator[self._label][seed] = 0
        numerator[self._label][seed] += int (re.sub (r"HLT-Report *[^ ]* *[^ ]* *[^ ]* *[^ ]* *([^ ]*) *[^ ]* *[^ ]* *[^ ]* *[^ ]* *[^ ]*", r"\1", line))

    fin.close ()
    tin.close ()

  def addDir (self, dirName):
    if not dirName:
      return
    if not os.path.isdir (dirName):
      print "\"" + dirName + "\" does not exist or is not a directory!"
      return

    print "Processing directory \"" + dirName + "\"..."

    logFiles = glob.glob (dirName + "/cmsRun_*.log.tar.gz")
    self._nFiles = len (logFiles)
    self._iFile = 0
    for logFile in logFiles:
      self._iFile += 1
      self.addFile (logFile)

  def setCrossSectionInPb (self, crossSectionInPb):
    self._crossSectionInPb = crossSectionInPb

  def setLabel (self, label):
    self._label = label
    numerator[self._label] = {}

  def __init__ (self, label = "", dirName = "", crossSectionInPb = 0.0):
    self.setLabel (label)
    self.addDir (dirName)
    self.setCrossSectionInPb (crossSectionInPb)

  def getRateInPb (self, seed):
    if seed not in numerator[self._label]:
      print "ETM" + seed + " not found in results!"
      return

    self._denominatorHist = TH1D ("total", "", 1, -0.5, 0.5)
    self._numeratorHist = TH1D ("pass", "", 1, -0.5, 0.5)

    self._denominatorHist.SetBinContent (1, self._denominator)
    self._denominatorHist.SetBinError (1, math.sqrt (self._denominator))
    self._numeratorHist.SetBinContent (1, numerator[self._label][seed])
    self._numeratorHist.SetBinError (1, math.sqrt (numerator[self._label][seed]))

    self._rateGraph = TGraphAsymmErrors (self._numeratorHist, self._denominatorHist)
    x = Double (0.0)
    y = Double (0.0)
    self._rateGraph.GetPoint (0, x, y)
    eLow = self._rateGraph.GetErrorYlow (0)
    eHigh = self._rateGraph.GetErrorYhigh (0)

    y *= self._crossSectionInPb
    eLow *= self._crossSectionInPb
    eHigh *= self._crossSectionInPb

    return (y, eLow, eHigh)

  def getSeeds (self):
    return map (str, sorted (map (int, numerator[self._label].keys ())))

# datasets and cross sections taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TriggerStudiesRunIISummer16DR80

hltRates = []
hltRates.append (copy.deepcopy (HLTRate ("WJetsToLNu", "/store/user/ahart/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_hlt_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/170203_210125/0000/log/", 5.07E+04)))
hltRates.append (copy.deepcopy (HLTRate ("DYToLL", "/store/user/ahart/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/crab_hlt_DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/170203_204751/0000/log/", 2.00E+04)))
#hltRates.append (copy.deepcopy (HLTRate ("QCD_Pt_15to30", "/store/user/ahart/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/170203_204832/0000/log/", 1.84E+09)))
#hltRates.append (copy.deepcopy (HLTRate ("QCD_Pt_30to50", "/store/user/ahart/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/170203_204901/0000/log/", 1.41E+08)))
hltRates.append (copy.deepcopy (HLTRate ("QCD_Pt_50to80", "/store/user/ahart/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/170203_204922/0000/log/", 1.92E+07)))
hltRates[-1].addDir ("/store/user/ahart/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8_ext1/170203_211149/0000/log/")
hltRates.append (copy.deepcopy (HLTRate ("QCD_Pt_80to120", "/store/user/ahart/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/170203_204943/0000/log/", 2.76E+06)))
hltRates[-1].addDir ("/store/user/ahart/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8_ext1/170203_211208/0000/log/")
hltRates.append (copy.deepcopy (HLTRate ("QCD_Pt_120to170", "/store/user/ahart/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/170203_205003/0000/log/", 4.71E+05)))
hltRates.append (copy.deepcopy (HLTRate ("QCD_Pt_170to300", "/store/user/ahart/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/170203_210145/0000/log/", 1.17E+05)))
hltRates.append (copy.deepcopy (HLTRate ("QCD_Pt_300to470", "/store/user/ahart/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/170203_205050/0000/log/", 7.82E+03)))
hltRates.append (copy.deepcopy (HLTRate ("QCD_Pt_470to600", "/store/user/ahart/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/170203_210209/0000/log/", 6.48E+02)))

print "Calculating and plotting rates..."

luminosities = ["1.7E34", "2.0E34", "2.2E34"]

################################################################################
# Create and initialize the graphs.
################################################################################
seeds = hltRates[0].getSeeds ()
n = len (seeds)
rates = []
for luminosity in luminosities:
  rates.append (copy.deepcopy (TGraphAsymmErrors (n)))
  rates[-1].SetName ("rate_" + re.sub (r"\.", r"p", luminosity))

for i in range (0, n):
  for rate in rates:
    rate.SetPoint (i, int (seeds[i]), 0.0)
    rate.SetPointEYlow (i, 0.0)
    rate.SetPointEYhigh (i, 0.0)
################################################################################

################################################################################
# Fill the graphs with the results from the HLTRate objects.
################################################################################
for hltRate in hltRates:
  for i in range (0, n):
    (r, eLow, eHigh) = hltRate.getRateInPb (seeds[i])
    for rate in rates:
      x = Double (0.0)
      y = Double (0.0)
      rate.GetPoint (i, x, y)
      yLow = rate.GetErrorYlow (i)
      yHigh = rate.GetErrorYhigh (i)

      rate.SetPoint (i, x, y + r)
      rate.SetPointEYlow (i, math.hypot (yLow, eLow))
      rate.SetPointEYhigh (i, math.hypot (yHigh, eHigh))
################################################################################

################################################################################
# Convert all the points to Hertz.
################################################################################
for i in range (0, n):
  for j in range (0, len (luminosities)):
    x = Double (0.0)
    y = Double (0.0)
    rates[j].GetPoint (i, x, y)
    yLow = rates[j].GetErrorYlow (i)
    yHigh = rates[j].GetErrorYhigh (i)

    rates[j].SetPoint (i, x, y * float (luminosities[j]) * 1.0E-36)
    rates[j].SetPointEYlow (i, yLow * float (luminosities[j]) * 1.0E-36)
    rates[j].SetPointEYhigh (i, yHigh * float (luminosities[j]) * 1.0E-36)
################################################################################

################################################################################
# Write graphs to hltRate.root.
################################################################################
fout = TFile ("hltRate.root", "recreate")
for rate in rates:
  rate.Write ()
fout.Close ()
################################################################################
