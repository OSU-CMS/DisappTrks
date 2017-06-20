#!/usr/bin/env python

import math

from bkgdEstimate_2015 import nElectrons as nElectrons2015
from bkgdEstimate_2015 import nMuons as nMuons2015
from bkgdEstimate_2015 import nTaus as nTaus2015
from bkgdEstimate_2015 import nFakes as nFakes2015
from bkgdEstimate_2015 import nLeptons as nLeptons2015
from bkgdEstimate_2015 import nLeptonsError as nLeptonsError2015
from bkgdEstimate_2015 import nTotal as nTotal2015
from bkgdEstimate_2015 import nTotalError as nTotalError2015

from bkgdEstimate_2016 import nElectrons as nElectrons2016
from bkgdEstimate_2016 import nMuons as nMuons2016
from bkgdEstimate_2016 import nTaus as nTaus2016
from bkgdEstimate_2016 import nFakes as nFakes2016
from bkgdEstimate_2016 import nLeptons as nLeptons2016
from bkgdEstimate_2016 import nLeptonsError as nLeptonsError2016
from bkgdEstimate_2016 import nTotal as nTotal2016
from bkgdEstimate_2016 import nTotalError as nTotalError2016

from DisappTrks.BackgroundSystematics.BackgroundSystematics import *
from ROOT import TMath

def getAbsoluteSystematicFromRelative (N, sysRelErr, statAbsErr):
  if N > 0.0:
    return N * sysRelErr
  upperLimit = 0.5 * TMath.ChisquareQuantile (0.68, 2.0 * (N + 1.0))
  # from http://dx.doi.org/10.1016/0168-9002(92)90794-5
  totalAbsErr = upperLimit * (1.0 + (upperLimit - N) * (sysRelErr * sysRelErr) / 2.0)
  return math.sqrt (totalAbsErr * totalAbsErr - statAbsErr * statAbsErr)

totalElectron  =  nElectrons2015[0]  +  nElectrons2016["BC"][0]  +  nElectrons2016["DEFGH"][0]
totalMuon      =  nMuons2015[0]      +  nMuons2016["BC"][0]      +  nMuons2016["DEFGH"][0]
totalTau       =  nTaus2015[0]       +  nTaus2016["BC"][0]       +  nTaus2016["DEFGH"][0]
totalFake      =  nFakes2015[0]      +  nFakes2016["BC"][0]      +  nFakes2016["DEFGH"][0]
totalLepton    =  nLeptons2015       +  nLeptons2016["BC"]       +  nLeptons2016["DEFGH"]
totalTotal     =  nTotal2015         +  nTotal2016["BC"]         +  nTotal2016["DEFGH"]

totalElectronError  =  math.hypot  (math.hypot  (nElectrons2015[1],  nElectrons2016["BC"][1]),  nElectrons2016["DEFGH"][1])
totalMuonError      =  math.hypot  (math.hypot  (nMuons2015[1],      nMuons2016["BC"][1]),      nMuons2016["DEFGH"][1])
totalTauError       =  math.hypot  (math.hypot  (nTaus2015[1],       nTaus2016["BC"][1]),       nTaus2016["DEFGH"][1])
totalFakeError      =  math.hypot  (math.hypot  (nFakes2015[1],      nFakes2016["BC"][1]),      nFakes2016["DEFGH"][1])
totalLeptonError    =  math.hypot  (math.hypot  (nLeptonsError2015,  nLeptonsError2016["BC"]),  nLeptonsError2016["DEFGH"])
totalTotalError     =  math.hypot  (math.hypot  (nTotalError2015,    nTotalError2016["BC"]),    nTotalError2016["DEFGH"])

electronSys2015       =  getAbsoluteSystematicFromRelative  (nElectrons2015[0],           electronSys["2015"],       nElectrons2015[1])
electronSys2016BC     =  getAbsoluteSystematicFromRelative  (nElectrons2016["BC"][0],     electronSys["2016BC"],     nElectrons2016["BC"][1])
electronSys2016DEFGH  =  getAbsoluteSystematicFromRelative  (nElectrons2016["DEFGH"][0],  electronSys["2016DEFGH"],  nElectrons2016["DEFGH"][1])

muonSys2015       =  0.0
muonSys2016BC     =  0.0
muonSys2016DEFGH  =  0.0

tauSys2015       =  getAbsoluteSystematicFromRelative  (nTaus2015[0],           tauSys["2015"],       nTaus2015[1])
tauSys2016BC     =  getAbsoluteSystematicFromRelative  (nTaus2016["BC"][0],     tauSys["2016BC"],     nTaus2016["BC"][1])
tauSys2016DEFGH  =  getAbsoluteSystematicFromRelative  (nTaus2016["DEFGH"][0],  tauSys["2016DEFGH"],  nTaus2016["DEFGH"][1])

leptonSys2015       =  math.hypot  (math.hypot  (electronSys2015,       muonSys2015),       tauSys2015)
leptonSys2016BC     =  math.hypot  (math.hypot  (electronSys2016BC,     muonSys2016BC),     tauSys2016BC)
leptonSys2016DEFGH  =  math.hypot  (math.hypot  (electronSys2016DEFGH,  muonSys2016DEFGH),  tauSys2016DEFGH)

fakeSys2015       =  getAbsoluteSystematicFromRelative  (nFakes2015[0],           fakeSys["2015"],       nFakes2015[1])
fakeSys2016BC     =  getAbsoluteSystematicFromRelative  (nFakes2016["BC"][0],     fakeSys["2016BC"],     nFakes2016["BC"][1])
fakeSys2016DEFGH  =  getAbsoluteSystematicFromRelative  (nFakes2016["DEFGH"][0],  fakeSys["2016DEFGH"],  nFakes2016["DEFGH"][1])

totalSys2015 = math.hypot (leptonSys2015, fakeSys2015)
totalSys2016BC = math.hypot (leptonSys2016BC, fakeSys2016BC)
totalSys2016DEFGH = math.hypot (leptonSys2016DEFGH, fakeSys2016DEFGH)
totalLeptonSys    =  math.hypot  (math.hypot  (leptonSys2015,    leptonSys2016BC),    leptonSys2016DEFGH)
totalFakeSys      =  math.hypot  (math.hypot  (fakeSys2015,      fakeSys2016BC),      fakeSys2016DEFGH)
totalSys_0 = math.hypot (totalLeptonSys, totalFakeSys)
totalSys_1 = math.hypot (math.hypot (totalSys2015, totalSys2016BC), totalSys2016DEFGH)

print "lepton background 2015:      " + str (nLeptons2015) + " +- " + str (nLeptonsError2015) + " +- " + str (leptonSys2015)
print "lepton background 2016BC:    " + str (nLeptons2016["BC"]) + " +- " + str (nLeptonsError2016["BC"]) + " +- " + str (leptonSys2016BC)
print "lepton background 2016DEFGH: " + str (nLeptons2016["DEFGH"]) + " +- " + str (nLeptonsError2016["DEFGH"]) + " +- " + str (leptonSys2016DEFGH)
print ""

print "fake background 2015:      " + str (nFakes2015[0]) + " +- " + str (nFakes2015[1]) + " +- " + str (fakeSys2015)
print "fake background 2016BC:    " + str (nFakes2016["BC"][0]) + " +- " + str (nFakes2016["BC"][1]) + " +- " + str (fakeSys2016BC)
print "fake background 2016DEFGH: " + str (nFakes2016["DEFGH"][0]) + " +- " + str (nFakes2016["DEFGH"][1]) + " +- " + str (fakeSys2016DEFGH)
print ""

print "total background 2015:      " + str (nTotal2015) + " +- " + str (nTotalError2015) + " +- " + str (totalSys2015)
print "total background 2016BC:    " + str (nTotal2016["BC"]) + " +- " + str (nTotalError2016["BC"]) + " +- " + str (totalSys2016BC)
print "total background 2016DEFGH: " + str (nTotal2016["DEFGH"]) + " +- " + str (nTotalError2016["DEFGH"]) + " +- " + str (totalSys2016DEFGH)
print ""

print "Total lepton background: " + str (totalLepton) + " +- " + str (totalLeptonError) + " +- " + str (totalLeptonSys)
print "Total fake background:   " + str (totalFake) + " +- " + str (totalFakeError) + " +- " + str (totalFakeSys)
print "Total total:             " + str (totalTotal) + " +- " + str (totalTotalError) + " +- " + str (totalSys_0) + " (" + str (totalSys_1) + ")"
