#!/usr/bin/env python

import FWCore.ParameterSet.Config as cms

def customizeForMETTriggerProducer (producer):
    producer.filterCategories = cms.vstring (
        "met",
        "metClean",
        "metCleanBH",
        "mht",
        "pfMET",
        "pfMHT",
        "pfMETNoMu",
        "pfMHTNoMu",
    )

    # The items in each vector correspond to the following triggers, in this order:
    # [HLT_MET200_v*,  HLT_MET75_IsoTrk50_v*,  HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned_v*,  HLT_PFMET120_PFMHT120_IDTight_v*,  HLT_PFMET170_HBHECleaned_v*,  HLT_PFMET300_v*,  HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*]

    producer.metCollections  =  cms.vstring  ("hltMet::HLT",  "hltMet::HLT",  "hltMet::HLT",  "hltMet::HLT",  "hltMet::HLT",  "hltMet::HLT",  "hltMet::HLT")
    producer.metThresholds   =  cms.vdouble  (200.0,          75.0,           80.0,           90.0,           90.0,           90.0,           90.0)
    producer.metJetsForTag   =  cms.vstring  ("",             "",             "",             "",             "",             "",             "")

    producer.metCleanCollections  =  cms.vstring  ("hltMetClean::HLT",  "hltMetClean::HLT",  "hltMetClean::HLT",  "hltMetClean::HLT",  "hltMetClean::HLT",  "hltMetClean::HLT",  "hltMetClean::HLT")
    producer.metCleanThresholds   =  cms.vdouble  (190.0,               65.0,                70.0,                80.0,                80.0,                80.0,                80.0)
    producer.metCleanJetsForTag   =  cms.vstring  ("",                  "",                  "",                  "",                  "",                  "",                  "")

    producer.metCleanBHCollections  =  cms.vstring  ("",   "",   "hltMetCleanBH::HLT",  "",   "",   "",   "")
    producer.metCleanBHThresholds   =  cms.vdouble  (0.0,  0.0,  70.0,                  0.0,  0.0,  0.0,  0.0)
    producer.metCleanBHJetsForTag   =  cms.vstring  ("",   "",   "",                    "",   "",   "",   "")

    producer.mhtCollections  =  cms.vstring  ("",   "",   "hltMht::HLT",                      "hltMht::HLT",                      "",   "",   "hltMht::HLT")
    producer.mhtThresholds   =  cms.vdouble  (0.0,  0.0,  80.0,                               90.0,                               0.0,  0.0,  90.0)
    producer.mhtJetsForTag   =  cms.vstring  ("",   "",   "hltAK4CaloJetsCorrectedIDPassed",  "hltAK4CaloJetsCorrectedIDPassed",  "",   "",   "hltAK4CaloJetsCorrectedIDPassed")

    producer.pfMETCollections  =  cms.vstring  ("",   "",   "hltPFMETProducer::HLT",  "hltPFMETProducer::HLT",  "hltPFMETProducer::HLT",  "hltPFMETProducer::HLT",  "")
    producer.pfMETThresholds   =  cms.vdouble  (0.0,  0.0,  100.0,                    120.0,                    170.0,                    300.0,                    0.0)
    producer.pfMETJetsForTag   =  cms.vstring  ("",   "",   "",                       "",                       "",                       "",                       "")

    producer.pfMHTCollections  =  cms.vstring  ("",   "",   "hltPFMHTTightID::HLT",          "hltPFMHTTightID::HLT",          "",   "",   "")
    producer.pfMHTThresholds   =  cms.vdouble  (0.0,  0.0,  100.0,                           120.0,                           0.0,  0.0,  0.0)
    producer.pfMHTJetsForTag   =  cms.vstring  ("",   "",   "hltAK4PFJetsTightIDCorrected",  "hltAK4PFJetsTightIDCorrected",  "",   "",   "")

    producer.pfMETNoMuCollections  =  cms.vstring  ("",   "",   "",   "",   "",   "",   "hltPFMETNoMuProducer::HLT")
    producer.pfMETNoMuThresholds   =  cms.vdouble  (0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  120.0)
    producer.pfMETNoMuJetsForTag   =  cms.vstring  ("",   "",   "",   "",   "",   "",   "")

    producer.pfMHTNoMuCollections  =  cms.vstring  ("",   "",   "",   "",   "",   "",   "hltPFMHTNoMuTightID::HLT")
    producer.pfMHTNoMuThresholds   =  cms.vdouble  (0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  120.0)
    producer.pfMHTNoMuJetsForTag   =  cms.vstring  ("",   "",   "",   "",   "",   "",   "hltAK4PFJetsTightIDCorrected")

    producer.additionalCollections  =  cms.vstring  ("",  "hltTrk50Filter::HLT",  "",  "",  "",  "",  "")
    producer.additionalFilters      =  cms.vstring  ("",  "hltTrk50Filter",       "",  "",  "",  "",  "")

    return producer
