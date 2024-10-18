import FWCore.ParameterSet.Config as cms
import OSUT3Analysis.DBTools.osusub_cfg as osusub
from OSUT3Analysis.Configuration.configurationOptions import *
import os

# MET filters recommended for Moriond 2017 here:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#Moriond_2017
metFilters = cms.vstring ([
  "Flag_goodVertices",
  "Flag_globalTightHalo2016Filter",
  "Flag_HBHENoiseFilter",
  "Flag_HBHENoiseIsoFilter",
  "Flag_EcalDeadCellTriggerPrimitiveFilter",
])

if osusub.batchMode and types[osusub.datasetLabel] == "data":
  metFilters.append (
    "Flag_eeBadScFilter",
  )

# In 2018 miniAOD, BadPFMuon and BadChargedCandidate are available already
# Also a new 'bad calibration' filter is added/suggested
# https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2#Moriond_2018
# Updates 4/12/19: BadChargedCandidate is under review; updated recipe for ecalBadCalib
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
  metFilters.append("Flag_BadPFMuonFilter")
  #metFilters.append("Flag_BadChargedCandidateFilter") # not recommended, under review
  #metFilters.append("Flag_ecalBadCalibFilter") # updated recipe, run on the fly
  metFilters.remove("Flag_globalTightHalo2016Filter")
  metFilters.append("Flag_globalSuperTightHalo2016Filter")

# Following recommendations in https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2#Run_3_recommendations
# ecalBadCalibFilter is implemented in protoConfig_cfg.py
if os.environ["CMSSW_VERSION"].startswith("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
  metFilters.remove("Flag_globalTightHalo2016Filter")
  metFilters.remove("Flag_HBHENoiseFilter")
  metFilters.remove("Flag_HBHENoiseIsoFilter")
  metFilters.append("Flag_BadPFMuonFilter")
  metFilters.append("Flag_BadPFMuonDzFilter")
  metFilters.append("Flag_globalSuperTightHalo2016Filter")
  metFilters.append("Flag_hfNoisyHitsFilter")
  metFilters.append("Flag_eeBadScFilter")