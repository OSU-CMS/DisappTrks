#!/usr/bin/env python

import math

from bkgdEstimate_2015 import nElectrons as nElectrons2015
from bkgdEstimate_2015 import nMuons as nMuons2015
from bkgdEstimate_2015 import nTaus as nTaus2015
from bkgdEstimate_2015 import nFakes as nFakes2015

from bkgdEstimate_2016 import nElectrons as nElectrons2016
from bkgdEstimate_2016 import nMuons as nMuons2016
from bkgdEstimate_2016 import nTaus as nTaus2016
from bkgdEstimate_2016 import nFakes as nFakes2016

from DisappTrks.BackgroundSystematics.BackgroundSystematics import *
from ROOT import TMath

def getAbsoluteSystematicFromRelative (N, sysRelErr, statAbsErr):
  if N > 0.0:
    return N * sysRelErr
  upperLimit = 0.5 * TMath.ChisquareQuantile (0.68, 2.0 * (N + 1.0))
  # from http://dx.doi.org/10.1016/0168-9002(92)90794-5
  totalAbsErr = upperLimit * (1.0 + (upperLimit - N) * (sysRelErr * sysRelErr) / 2.0)
  return math.sqrt (totalAbsErr * totalAbsErr - statAbsErr * statAbsErr)

nElectrons2015.setSystematic           (getAbsoluteSystematicFromRelative  (nElectrons2015.centralValue           (),  electronSys["2015"],       nElectrons2015.maxUncertainty           ()))
nElectrons2016["BC"].setSystematic     (getAbsoluteSystematicFromRelative  (nElectrons2016["BC"].centralValue     (),  electronSys["2016BC"],     nElectrons2016["BC"].maxUncertainty     ()))
nElectrons2016["DEFGH"].setSystematic  (getAbsoluteSystematicFromRelative  (nElectrons2016["DEFGH"].centralValue  (),  electronSys["2016DEFGH"],  nElectrons2016["DEFGH"].maxUncertainty  ()))

nMuons2015.setSystematic (0.0)
nMuons2016["BC"].setSystematic (0.0)
nMuons2016["DEFGH"].setSystematic (0.0)

nTaus2015.setSystematic           (getAbsoluteSystematicFromRelative  (nTaus2015.centralValue           (),  tauSys["2015"],       nTaus2015.maxUncertainty           ()))
nTaus2016["BC"].setSystematic     (getAbsoluteSystematicFromRelative  (nTaus2016["BC"].centralValue     (),  tauSys["2016BC"],     nTaus2016["BC"].maxUncertainty     ()))
nTaus2016["DEFGH"].setSystematic  (getAbsoluteSystematicFromRelative  (nTaus2016["DEFGH"].centralValue  (),  tauSys["2016DEFGH"],  nTaus2016["DEFGH"].maxUncertainty  ()))

nFakes2015.setSystematic           (getAbsoluteSystematicFromRelative  (nFakes2015.centralValue           (),  fakeSysDown["2015"],       nFakes2015.maxUncertainty           ()), getAbsoluteSystematicFromRelative  (nFakes2015.centralValue           (),  fakeSysUp["2015"],       nFakes2015.maxUncertainty           ()))
nFakes2016["BC"].setSystematic     (getAbsoluteSystematicFromRelative  (nFakes2016["BC"].centralValue     (),  fakeSysDown["2016BC"],     nFakes2016["BC"].maxUncertainty     ()), getAbsoluteSystematicFromRelative  (nFakes2016["BC"].centralValue     (),  fakeSysUp["2016BC"],     nFakes2016["BC"].maxUncertainty     ()))
nFakes2016["DEFGH"].setSystematic  (getAbsoluteSystematicFromRelative  (nFakes2016["DEFGH"].centralValue  (),  fakeSysDown["2016DEFGH"],  nFakes2016["DEFGH"].maxUncertainty  ()), getAbsoluteSystematicFromRelative  (nFakes2016["DEFGH"].centralValue  (),  fakeSysUp["2016DEFGH"],  nFakes2016["DEFGH"].maxUncertainty  ()))

nLeptons2016 = {}
nLeptons2015 = nElectrons2015 + nMuons2015 + nTaus2015
nLeptons2016["BC"] = nElectrons2016["BC"] + nMuons2016["BC"] + nTaus2016["BC"]
nLeptons2016["DEFGH"] = nElectrons2016["DEFGH"] + nMuons2016["DEFGH"] + nTaus2016["DEFGH"]

nTotal2016 = {}
nTotal2015 = nLeptons2015 + nFakes2015
nTotal2016["BC"] = nLeptons2016["BC"] + nFakes2016["BC"]
nTotal2016["DEFGH"] = nLeptons2016["DEFGH"] + nFakes2016["DEFGH"]

totalElectron  =  nElectrons2015  +  nElectrons2016["BC"]  +  nElectrons2016["DEFGH"]
totalMuon      =  nMuons2015      +  nMuons2016["BC"]      +  nMuons2016["DEFGH"]
totalTau       =  nTaus2015       +  nTaus2016["BC"]       +  nTaus2016["DEFGH"]
totalFake      =  nFakes2015      +  nFakes2016["BC"]      +  nFakes2016["DEFGH"]

totalLepton    =  totalElectron + totalMuon + totalTau
totalTotal     =  totalLepton + totalFake

print "lepton background 2015:      (" + str (nLeptons2015)
print "lepton background 2016BC:    (" + str (nLeptons2016["BC"])
print "lepton background 2016DEFGH: (" + str (nLeptons2016["DEFGH"])
print ""

print "fake background 2015:      (" + str (nFakes2015)
print "fake background 2016BC:    (" + str (nFakes2016["BC"])
print "fake background 2016DEFGH: (" + str (nFakes2016["DEFGH"])
print ""

print "total background 2015:      (" + str (nTotal2015)
print "total background 2016BC:    (" + str (nTotal2016["BC"])
print "total background 2016DEFGH: (" + str (nTotal2016["DEFGH"])
print ""

print "Total lepton background: (" + str (totalLepton)
print "Total fake background:   (" + str (totalFake)
print "Total total:             (" + str (totalTotal)
