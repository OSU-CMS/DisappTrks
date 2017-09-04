#!/usr/bin/env python

import math

electronSys = {
    "2015"      : 0.106,
    "2016BC"    : 0.117,
    "2016DEFGH" : 0.117,
}

tauSys = {
    "2015"      : 0.187,
    "2016BC"    : 0.180,
    "2016DEFGH" : 0.169,
}

fakeSysDown = {
    "control region" : {
      "2015" : 0.2,
      "2016BC" : 0.0701,
      "2016DEFGH" : 0.0858,
    },
    "sideband region" : {
      "2015" : 0.5,
      "2016BC" : 1.0,
      "2016DEFGH" : 1.0,
    },
    "transfer factor" : {
      "2015" : 0.514,
      "2016BC" : 0.514,
      "2016DEFGH" : 0.514,
    },
    "total" : {},
}

fakeSysUp = {
    "control region" : {
      "2015" : 0.2,
      "2016BC" : 0.0701,
      "2016DEFGH" : 0.0858,
    },
    "sideband region" : {
      "2015" : 0.5,
      "2016BC" : 0.447,
      "2016DEFGH" : 0.142,
    },
    "transfer factor" : {
      "2015" : 0.979,
      "2016BC" : 0.979,
      "2016DEFGH" : 0.979,
    },
    "total" : {},
}

for systematic in fakeSysDown:
    for runPeriod in fakeSysDown[systematic]:
        if runPeriod not in fakeSysDown["total"]:
            fakeSysDown["total"][runPeriod] = 0.0
        fakeSysDown["total"][runPeriod] = math.hypot (fakeSysDown["total"][runPeriod], fakeSysDown[systematic][runPeriod])

for systematic in fakeSysUp:
    for runPeriod in fakeSysUp[systematic]:
        if runPeriod not in fakeSysUp["total"]:
            fakeSysUp["total"][runPeriod] = 0.0
        fakeSysUp["total"][runPeriod] = math.hypot (fakeSysUp["total"][runPeriod], fakeSysUp[systematic][runPeriod])
