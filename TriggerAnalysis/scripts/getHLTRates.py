#!/usr/bin/env python

import os, glob, tarfile, re
from ROOT import TFile, TH1D, TGraphAsymmErrors

TH1D.SetDefaultSumw2 ()

class HLTRate:
  _denominator = 0
  _numerator = {}
  _crossSectionInPb = 0.0
  _nFiles = 0
  _iFile = 0

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
        if seed not in self._numerator:
          self._numerator[seed] = 0.0
        self._numerator[seed] += self._crossSectionInPb * int (re.sub (r"HLT-Report *[^ ]* *[^ ]* *[^ ]* *[^ ]* *([^ ]*) *[^ ]* *[^ ]* *[^ ]* *[^ ]* *[^ ]*", r"\1", line))

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

  def __init__ (self, dirName = "", crossSectionInPb = 0.0):
    self.addDir (dirName)
    self.setCrossSectionInPb (crossSectionInPb)

  def getRateInPb (self, seed):
    if seed not in self._numerator:
      print "ETM" + seed + " not found in results!"
      return

    return (self._numerator[seed], self._denominator)

  def getSeeds (self):
    return self._numerator.keys ()

# datasets and cross sections taken from https://twiki.cern.ch/twiki/bin/viewauth/CMS/TriggerStudiesRunIISummer16DR80

hltRate = HLTRate ()
hltRate.setCrossSectionInPb (5.07E+04)
hltRate.addDir ("/store/user/ahart/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_hlt_WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/170203_210125/0000/log/")
hltRate.setCrossSectionInPb (2.00E+04)
hltRate.addDir ("/store/user/ahart/DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/crab_hlt_DYToLL_M_1_TuneCUETP8M1_13TeV_pythia8/170203_204751/0000/log/")
hltRate.setCrossSectionInPb (1.84E+09)
hltRate.addDir ("/store/user/ahart/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/170203_204832/0000/log/")
hltRate.setCrossSectionInPb (1.41E+08)
hltRate.addDir ("/store/user/ahart/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/170203_204901/0000/log/")
hltRate.setCrossSectionInPb (1.92E+07)
hltRate.addDir ("/store/user/ahart/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/170203_204922/0000/log/")
hltRate.addDir ("/store/user/ahart/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8_ext1/170203_211149/0000/log/")
hltRate.setCrossSectionInPb (2.76E+06)
hltRate.addDir ("/store/user/ahart/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/170203_204943/0000/log/")
hltRate.addDir ("/store/user/ahart/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8_ext1/170203_211208/0000/log/")
hltRate.setCrossSectionInPb (4.71E+05)
hltRate.addDir ("/store/user/ahart/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/170203_205003/0000/log/")
hltRate.setCrossSectionInPb (1.17E+05)
hltRate.addDir ("/store/user/ahart/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/170203_210145/0000/log/")
hltRate.setCrossSectionInPb (7.82E+03)
hltRate.addDir ("/store/user/ahart/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/170203_205050/0000/log/")
hltRate.setCrossSectionInPb (6.48E+02)
hltRate.addDir ("/store/user/ahart/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/crab_hlt_QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/170203_210209/0000/log/")

total = TH1D ("total", "", 150, -0.5, 149.5)
passing = TH1D ("pass", "", 150, -0.5, 149.5)
for seed in hltRate.getSeeds ():
  (numerator, denominator) = hltRate.getRateInPb (seed)
  total.Fill (float (seed), denominator)
  passing.Fill (float (seed), numerator)

passing_1p7E34 = passing.Clone ("passing_1p7E34")
passing_2p0E34 = passing.Clone ("passing_2p0E34")
passing_2p2E34 = passing.Clone ("passing_2p2E34")
passing_1p7E34.Scale (1.7E34 * 1.0E-36)
passing_2p0E34.Scale (2.0E34 * 1.0E-36)
passing_2p2E34.Scale (2.2E34 * 1.0E-36)

rate_1p7E34 = TGraphAsymmErrors (passing_1p7E34, total)
rate_2p0E34 = TGraphAsymmErrors (passing_2p0E34, total)
rate_2p2E34 = TGraphAsymmErrors (passing_2p2E34, total)
fout = TFile ("hltRate.root", "recreate")
rate_1p7E34.Write ("hltRate_1p7E34")
rate_2p0E34.Write ("hltRate_2p0E34")
rate_2p2E34.Write ("hltRate_2p2E34")
fout.Close ()
