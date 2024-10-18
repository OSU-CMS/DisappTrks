#!/usr/bin/env python3

import os
import FWCore.ParameterSet.Config as cms

def customizeForMETTriggerProducer (producer):
    producer.filterCategories = cms.vstring (
        "met",
        "metClean",
        "metCleanBH",
        "metCleanUsingJetID",
        "mht",
        "pfMHTTightID",
        "pfMET",
        "pfMHT",
        "pfMETNoMu",
        "pfMHTNoMu",
    )

    if producer.type_ () == "EventElectronMETTriggerProducer":
        producer.tagCollection = cms.string ("hltEgammaCandidates::HLT")
    elif producer.type_ () == "EventMuonMETTriggerProducer":
        producer.tagCollection = cms.string ("hltL3MuonCandidates::HLT")
    elif producer.type_ () == "EventTauMETTriggerProducer":
        producer.tagCollection = cms.string ("hltSelectedPFTausTrackPt30AbsOrRelIsolation::HLT")
    else:
        print("# Unknown producer type! Cannot set collection for tag lepton.")
        exit (1)

    producer.metMuonsCountedAsVisible                 =  cms.bool  (False)
    producer.metCleanMuonsCountedAsVisible            =  cms.bool  (False)
    producer.metCleanBHMuonsCountedAsVisible          =  cms.bool  (False)
    producer.metCleanUsingJetIDMuonsCountedAsVisible  =  cms.bool  (False)
    producer.mhtMuonsCountedAsVisible                 =  cms.bool  (False)
    producer.pfMHTTightIDMuonsCountedAsVisible        =  cms.bool  (True)
    producer.pfMETMuonsCountedAsVisible               =  cms.bool  (True)
    producer.pfMHTMuonsCountedAsVisible               =  cms.bool  (True)
    producer.pfMETNoMuMuonsCountedAsVisible           =  cms.bool  (False)
    producer.pfMHTNoMuMuonsCountedAsVisible           =  cms.bool  (False)

    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_"):
        print("# Using 2015 MET trigger filters in EventMETTriggerProducer_cfi.py...")

        # The items in each vector correspond to the following triggers, in this order:
        # [HLT_MET250_v*, HLT_MET75_IsoTrk50_v*, HLT_PFMET120_PFMHT120_IDTight_v*, HLT_PFMET170_HBHECleaned_v*, HLT_PFMET170_JetIdCleaned_v*, HLT_PFMET170_NoiseCleaned_v*, HLT_PFMET170_v*, HLT_PFMET90_PFMHT90_IDTight_v*, HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*, HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*]

        producer.metCollections                 =  cms.vstring  ("hltMet::HLT",  "hltMet::HLT",  "hltMet::HLT",                           "hltMet::HLT",            "hltMet::HLT",                 "hltMet::HLT",                 "hltMet::HLT",            "hltMet::HLT",                           "hltMet::HLT",                           "hltMet::HLT")
        producer.metThresholds                  =  cms.vdouble  (250.0,          75.0,           90.0,                                    90.0,                     90.0,                          90.0,                          90.0,                     70.0,                                    80.0,                                    80.0)
        producer.metJetsForTag                  =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "",                                      "")

        producer.metCleanCollections            =  cms.vstring  ("",             "",             "",                                      "hltMetClean::HLT",       "",                            "hltMetClean::HLT",            "",                       "",                                      "",                                      "")
        producer.metCleanThresholds             =  cms.vdouble  (0.0,            0.0,            0.0,                                     80.0,                     0.0,                           80.0,                          0.0,                      0.0,                                     0.0,                                     0.0)
        producer.metCleanJetsForTag             =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "",                                      "")

        producer.metCleanBHCollections          =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "",                                      "")
        producer.metCleanBHThresholds           =  cms.vdouble  (0.0,            0.0,            0.0,                                     0.0,                      0.0,                           0.0,                           0.0,                      0.0,                                     0.0,                                     0.0)
        producer.metCleanBHJetsForTag           =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "",                                      "")

        producer.metCleanUsingJetIDCollections  =  cms.vstring  ("",             "",             "",                                      "",                       "hltMetCleanUsingJetID::HLT",  "hltMetCleanUsingJetID::HLT",  "",                       "",                                      "hltMetCleanUsingJetID::HLT",            "hltMetCleanUsingJetID::HLT")
        producer.metCleanUsingJetIDThresholds   =  cms.vdouble  (0.0,            0.0,            0.0,                                     0.0,                      80.0,                          80.0,                          0.0,                      0.0,                                     70.0,                                    70.0)
        producer.metCleanUsingJetIDJetsForTag   =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "",                                      "")

        producer.mhtCollections                 =  cms.vstring  ("",             "",             "hltMht::HLT",                           "",                       "",                            "",                            "",                       "hltMht::HLT",                           "hltMht::HLT",                           "hltMht::HLT")
        producer.mhtThresholds                  =  cms.vdouble  (0.0,            0.0,            90.0,                                    0.0,                      0.0,                           0.0,                           0.0,                      70.0,                                    80.0,                                    80.0)
        producer.mhtJetsForTag                  =  cms.vstring  ("",             "",             "hltAK4CaloJetsCorrectedIDPassed::HLT",  "",                       "",                            "",                            "",                       "hltAK4CaloJetsCorrectedIDPassed::HLT",  "hltAK4CaloJetsCorrectedIDPassed::HLT",  "hltAK4CaloJetsCorrectedIDPassed::HLT")

        producer.pfMHTTightIDCollections        =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "",                                      "")
        producer.pfMHTTightIDThresholds         =  cms.vdouble  (0.0,            0.0,            0.0,                                     0.0,                      0.0,                           0.0,                           0.0,                      0.0,                                     0.0,                                     0.0)
        producer.pfMHTTightIDJetsForTag         =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "",                                      "")

        producer.pfMETCollections               =  cms.vstring  ("",             "",             "hltPFMETProducer::HLT",                 "hltPFMETProducer::HLT",  "hltPFMETProducer::HLT",       "hltPFMETProducer::HLT",       "hltPFMETProducer::HLT",  "hltPFMETProducer::HLT",                 "",                                      "")
        producer.pfMETThresholds                =  cms.vdouble  (0.0,            0.0,            120.0,                                   170.0,                    170.0,                         170.0,                         170.0,                    90.0,                                    0.0,                                     0.0)
        producer.pfMETJetsForTag                =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "",                                      "")

        producer.pfMHTCollections               =  cms.vstring  ("",             "",             "hltPFMHTTightID::HLT",                  "",                       "",                            "",                            "",                       "hltPFMHTTightID::HLT",                  "",                                      "")
        producer.pfMHTThresholds                =  cms.vdouble  (0.0,            0.0,            120.0,                                   0.0,                      0.0,                           0.0,                           0.0,                      90.0,                                    0.0,                                     0.0)
        producer.pfMHTJetsForTag                =  cms.vstring  ("",             "",             "hltAK4PFJetsTightIDCorrected::HLT",     "",                       "",                            "",                            "",                       "hltAK4PFJetsTightIDCorrected::HLT",     "",                                      "")

        producer.pfMETNoMuCollections           =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "hltPFMETNoMuProducer::HLT",             "hltPFMETNoMuProducer::HLT")
        producer.pfMETNoMuThresholds            =  cms.vdouble  (0.0,            0.0,            0.0,                                     0.0,                      0.0,                           0.0,                           0.0,                      0.0,                                     120.0,                                   90.0)
        producer.pfMETNoMuJetsForTag            =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "",                                      "")

        producer.pfMHTNoMuCollections           =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "hltPFMHTNoMuTightID::HLT",              "hltPFMHTNoMuTightID::HLT")
        producer.pfMHTNoMuThresholds            =  cms.vdouble  (0.0,            0.0,            0.0,                                     0.0,                      0.0,                           0.0,                           0.0,                      0.0,                                     120.0,                                   90.0)
        producer.pfMHTNoMuJetsForTag            =  cms.vstring  ("",             "",             "",                                      "",                       "",                            "",                            "",                       "",                                      "hltAK4PFJetsTightIDCorrected::HLT",     "hltAK4PFJetsTightIDCorrected::HLT")

        producer.additionalCollections  =  cms.vstring  ("",  "hltTrk50Filter::HLT",  "",  "",  "",  "",  "",  "",  "",  "")
        producer.additionalFilters      =  cms.vstring  ("",  "hltTrk50Filter",       "",  "",  "",  "",  "",  "",  "",  "")

    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
        print("# Using 2016 MET trigger filters in EventMETTriggerProducer_cfi.py...")

        # The items in each vector correspond to the following triggers, in this order:
        # [HLT_MET200_v*,  HLT_MET75_IsoTrk50_v*,  HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned_v*,  HLT_PFMET120_PFMHT120_IDTight_v*,  HLT_PFMET170_HBHECleaned_v*,  HLT_PFMET300_v*,  HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*]

        producer.metCollections                 =  cms.vstring  ("hltMet::HLT",       "hltMet::HLT",       "hltMet::HLT",                           "hltMet::HLT",                           "hltMet::HLT",            "hltMet::HLT",            "hltMet::HLT")
        producer.metThresholds                  =  cms.vdouble  (200.0,               75.0,                80.0,                                    90.0,                                    90.0,                     90.0,                     90.0)
        producer.metJetsForTag                  =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "")

        producer.metCleanCollections            =  cms.vstring  ("hltMetClean::HLT",  "hltMetClean::HLT",  "hltMetClean::HLT",                      "hltMetClean::HLT",                      "hltMetClean::HLT",       "hltMetClean::HLT",       "hltMetClean::HLT")
        producer.metCleanThresholds             =  cms.vdouble  (190.0,               65.0,                70.0,                                    80.0,                                    80.0,                     80.0,                     80.0)
        producer.metCleanJetsForTag             =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "")

        producer.metCleanBHCollections          =  cms.vstring  ("",                  "",                  "hltMetCleanBH::HLT",                    "",                                      "",                       "",                       "")
        producer.metCleanBHThresholds           =  cms.vdouble  (0.0,                 0.0,                 70.0,                                    0.0,                                     0.0,                      0.0,                      0.0)
        producer.metCleanBHJetsForTag           =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "")

        producer.metCleanUsingJetIDCollections  =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "")
        producer.metCleanUsingJetIDThresholds   =  cms.vdouble  (0.0,                 0.0,                 0.0,                                     0.0,                                     0.0,                      0.0,                      0.0)
        producer.metCleanUsingJetIDJetsForTag   =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "")

        producer.mhtCollections                 =  cms.vstring  ("",                  "",                  "hltMht::HLT",                           "hltMht::HLT",                           "",                       "",                       "hltMht::HLT")
        producer.mhtThresholds                  =  cms.vdouble  (0.0,                 0.0,                 80.0,                                    90.0,                                    0.0,                      0.0,                      90.0)
        producer.mhtJetsForTag                  =  cms.vstring  ("",                  "",                  "hltAK4CaloJetsCorrectedIDPassed::HLT",  "hltAK4CaloJetsCorrectedIDPassed::HLT",  "",                       "",                       "hltAK4CaloJetsCorrectedIDPassed::HLT")

        producer.pfMHTTightIDCollections        =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "")
        producer.pfMHTTightIDThresholds         =  cms.vdouble  (0.0,                 0.0,                 0.0,                                     0.0,                                     0.0,                      0.0,                      0.0)
        producer.pfMHTTightIDJetsForTag         =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "")

        producer.pfMETCollections               =  cms.vstring  ("",                  "",                  "hltPFMETProducer::HLT",                 "hltPFMETProducer::HLT",                 "hltPFMETProducer::HLT",  "hltPFMETProducer::HLT",  "")
        producer.pfMETThresholds                =  cms.vdouble  (0.0,                 0.0,                 100.0,                                   120.0,                                   170.0,                    300.0,                    0.0)
        producer.pfMETJetsForTag                =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "")

        producer.pfMHTCollections               =  cms.vstring  ("",                  "",                  "hltPFMHTTightID::HLT",                  "hltPFMHTTightID::HLT",                  "",                       "",                       "")
        producer.pfMHTThresholds                =  cms.vdouble  (0.0,                 0.0,                 100.0,                                   120.0,                                   0.0,                      0.0,                      0.0)
        producer.pfMHTJetsForTag                =  cms.vstring  ("",                  "",                  "hltAK4PFJetsTightIDCorrected::HLT",     "hltAK4PFJetsTightIDCorrected::HLT",     "",                       "",                       "")

        producer.pfMETNoMuCollections           =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "hltPFMETNoMuProducer::HLT")
        producer.pfMETNoMuThresholds            =  cms.vdouble  (0.0,                 0.0,                 0.0,                                     0.0,                                     0.0,                      0.0,                      120.0)
        producer.pfMETNoMuJetsForTag            =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "")

        producer.pfMHTNoMuCollections           =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "hltPFMHTNoMuTightID::HLT")
        producer.pfMHTNoMuThresholds            =  cms.vdouble  (0.0,                 0.0,                 0.0,                                     0.0,                                     0.0,                      0.0,                      120.0)
        producer.pfMHTNoMuJetsForTag            =  cms.vstring  ("",                  "",                  "",                                      "",                                      "",                       "",                       "hltAK4PFJetsTightIDCorrected::HLT")

        producer.additionalCollections  =  cms.vstring  ("",  "hltTrk50Filter::HLT",  "",  "",  "",  "",  "")
        producer.additionalFilters      =  cms.vstring  ("",  "hltTrk50Filter",       "",  "",  "",  "",  "")

    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        print("# Using 2017-8 MET trigger filters in EventMETTriggerProducer_cfi.py...")

        # Copied from AllTriggers.py, all triggers in the Grand Or selection
        # The following vectors are each aligned to these triggers, in this order, and describes the contents of their filters:
        #'HLT_MET105_IsoTrk50_v'                                : ['hltMET105', 'hltMETClean65'],
        #'HLT_PFMET120_PFMHT120_IDTight_v'                      : ['hltMET90',  'hltMETClean80',  'hltMHT90',  'hltPFMHTTightID120', 'hltPFMET120'], # 2016-2017 also
        #'HLT_PFMET130_PFMHT130_IDTight_v'                      : ['hltMET100', 'hltMETClean90',  'hltMHT100', 'hltPFMHTTightID130', 'hltPFMET130'],
        #'HLT_PFMET140_PFMHT140_IDTight_v'                      : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTTightID140', 'hltPFMET140'], # perfect trigger B-F!
        #'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'              : ['hltMET90',  'hltMETClean80',  'hltMHT90',                                       'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
        #'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v'              : ['hltMET100', 'hltMETClean90',  'hltMHT100',                                      'hltPFMHTNoMuTightID130', 'hltPFMETNoMu130'],
        #'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v'              : ['hltMET110', 'hltMETClean100', 'hltMHT110',                                      'hltPFMHTNoMuTightID140', 'hltPFMETNoMu140'],
        #'HLT_PFMET250_HBHECleaned_v'                           : ['hltMET90',  'hltMETClean80',                                     'hltPFMET250'],
        #'HLT_PFMET300_HBHECleaned_v'                           : ['hltMET90',  'hltMETClean80',                                     'hltPFMET300'],

        producer.metCollections                  = cms.vstring(["hltMet::HLT"] * 9)
        producer.metThresholds                   = cms.vdouble(105.0, 90.0, 100.0, 110.0, 90.0, 100.0, 110.0, 90.0, 90.0)
        producer.metJetsForTag                   = cms.vstring([""] * 9)

        producer.metCleanCollections             = cms.vstring(["hltMetClean::HLT"] * 9)
        producer.metCleanThresholds              = cms.vdouble(65.0, 80.0, 90.0, 100.0, 80.0, 90.0, 100.0, 80.0, 80.0)
        producer.metCleanJetsForTag              = cms.vstring([""] * 9)

        producer.metCleanBHCollections           = cms.vstring([""] * 9)
        producer.metCleanBHThresholds            = cms.vdouble([0.0] * 9)
        producer.metCleanBHJetsForTag            = cms.vstring([""] * 9)

        producer.metCleanUsingJetIDCollections   = cms.vstring([""] * 9)
        producer.metCleanUsingJetIDThresholds    = cms.vdouble([0.0] * 9)
        producer.metCleanUsingJetIDJetsForTag    = cms.vstring([""] * 9)

        producer.mhtCollections                  = cms.vstring([""] + ["hltMht::HLT"] * 6 + ["", ""])
        producer.mhtThresholds                   = cms.vdouble(0.0, 90.0, 100.0, 110.0, 90.0, 100.0, 110.0, 0.0, 0.0)
        producer.mhtJetsForTag                   = cms.vstring([""] + ["hltAK4CaloJetsCorrectedIDPassed::HLT"] * 6 + ["", ""])

        producer.pfMHTTightIDCollections         = cms.vstring([""] + ["hltPFMHTTightID::HLT"] * 3 + [""] * 5)
        producer.pfMHTTightIDThresholds          = cms.vdouble([0.0, 120.0, 130.0, 140.0] + [0.0] * 5)
        producer.pfMHTTightIDJetsForTag          = cms.vstring([""] + ["hltAK4PFJetsTightIDCorrected::HLT"] * 3 + [""] * 5)

        producer.pfMETCollections                = cms.vstring([""] + ["hltPFMETProducer::HLT"] * 3 + [""] * 3 + ["hltPFMETProducer::HLT"] * 2)
        producer.pfMETThresholds                 = cms.vdouble([0.0, 120.0, 130.0, 140.0] + [0.0] * 3 + [250.0, 300.0])
        producer.pfMETJetsForTag                 = cms.vstring([""] * 9)

        producer.pfMHTCollections                = cms.vstring([""] * 9)
        producer.pfMHTThresholds                 = cms.vdouble([0.0] * 9)
        producer.pfMHTJetsForTag                 = cms.vstring([""] * 9)

        producer.pfMETNoMuCollections            = cms.vstring([""] * 4 + ["hltPFMETNoMuProducer::HLT"] * 3 + [""] * 2)
        producer.pfMETNoMuThresholds             = cms.vdouble([0.0] * 4 + [120.0, 130.0, 140.0] + [0.0] * 2)
        producer.pfMETNoMuJetsForTag             = cms.vstring([""] * 9)

        producer.pfMHTNoMuCollections            = cms.vstring([""] * 4 + ["hltPFMHTNoMuTightID::HLT"] * 3 + [""] * 2)
        producer.pfMHTNoMuThresholds             = cms.vdouble([0.0] * 4 + [120.0, 130.0, 140.0] + [0.0] * 2)
        producer.pfMHTNoMuJetsForTag             = cms.vstring([""] * 9)

        producer.additionalCollections           = cms.vstring(["hltTrk50Filter::HLT"] + [""] * 8)
        producer.additionalFilters               = cms.vstring(["hltTrk50Filter"] + [""] * 8)

    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
        print("# Using 2022 MET trigger filters in EventMETTriggerProducer_cfi.py...") #Should be fixed later

        # Copied from AllTriggers.py, all triggers in the Grand Or selection
        # The following vectors are each aligned to these triggers, in this order, and describes the contents of their filters:
        #'HLT_MET105_IsoTrk50_v'                                : ['hltMET105', 'hltMETClean65'],
        #'HLT_PFMET120_PFMHT120_IDTight_v'                      : ['hltMET90',  'hltMETClean80',  'hltMHT90',  'hltPFMHTTightID120', 'hltPFMET120'], # 2016-2017 also
        #'HLT_PFMET130_PFMHT130_IDTight_v'                      : ['hltMET100', 'hltMETClean90',  'hltMHT100', 'hltPFMHTTightID130', 'hltPFMET130'],
        #'HLT_PFMET140_PFMHT140_IDTight_v'                      : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTTightID140', 'hltPFMET140'], # perfect trigger B-F!
        #'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'              : ['hltMET90',  'hltMETClean80',  'hltMHT90',                                       'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
        #'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v'              : ['hltMET100', 'hltMETClean90',  'hltMHT100',                                      'hltPFMHTNoMuTightID130', 'hltPFMETNoMu130'],
        #'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v'              : ['hltMET110', 'hltMETClean100', 'hltMHT110',                                      'hltPFMHTNoMuTightID140', 'hltPFMETNoMu140'],
        #'HLT_PFMET250_HBHECleaned_v'                           : ['hltMET90',  'hltMETClean80',                                     'hltPFMET250'],
        #'HLT_PFMET300_HBHECleaned_v'                           : ['hltMET90',  'hltMETClean80',                                     'hltPFMET300'],

        producer.metCollections                  = cms.vstring(["hltMet::HLT"] * 9)
        producer.metThresholds                   = cms.vdouble(105.0, 90.0, 100.0, 110.0, 90.0, 100.0, 110.0, 90.0, 90.0)
        producer.metJetsForTag                   = cms.vstring([""] * 9)

        producer.metCleanCollections             = cms.vstring(["hltMetClean::HLT"] * 9)
        producer.metCleanThresholds              = cms.vdouble(65.0, 80.0, 90.0, 100.0, 80.0, 90.0, 100.0, 80.0, 80.0)
        producer.metCleanJetsForTag              = cms.vstring([""] * 9)

        producer.metCleanBHCollections           = cms.vstring([""] * 9)
        producer.metCleanBHThresholds            = cms.vdouble([0.0] * 9)
        producer.metCleanBHJetsForTag            = cms.vstring([""] * 9)

        producer.metCleanUsingJetIDCollections   = cms.vstring([""] * 9)
        producer.metCleanUsingJetIDThresholds    = cms.vdouble([0.0] * 9)
        producer.metCleanUsingJetIDJetsForTag    = cms.vstring([""] * 9)

        producer.mhtCollections                  = cms.vstring([""] + ["hltMht::HLT"] * 6 + ["", ""])
        producer.mhtThresholds                   = cms.vdouble(0.0, 90.0, 100.0, 110.0, 90.0, 100.0, 110.0, 0.0, 0.0)
        producer.mhtJetsForTag                   = cms.vstring([""] + ["hltAK4CaloJetsCorrectedIDPassed::HLT"] * 6 + ["", ""])

        producer.pfMHTTightIDCollections         = cms.vstring([""] + ["hltPFMHTTightID::HLT"] * 3 + [""] * 5)
        producer.pfMHTTightIDThresholds          = cms.vdouble([0.0, 120.0, 130.0, 140.0] + [0.0] * 5)
        producer.pfMHTTightIDJetsForTag          = cms.vstring([""] + ["hltAK4PFJetsTightIDCorrected::HLT"] * 3 + [""] * 5)

        producer.pfMETCollections                = cms.vstring([""] + ["hltPFMETProducer::HLT"] * 3 + [""] * 3 + ["hltPFMETProducer::HLT"] * 2)
        producer.pfMETThresholds                 = cms.vdouble([0.0, 120.0, 130.0, 140.0] + [0.0] * 3 + [250.0, 300.0])
        producer.pfMETJetsForTag                 = cms.vstring([""] * 9)

        producer.pfMHTCollections                = cms.vstring([""] * 9)
        producer.pfMHTThresholds                 = cms.vdouble([0.0] * 9)
        producer.pfMHTJetsForTag                 = cms.vstring([""] * 9)

        producer.pfMETNoMuCollections            = cms.vstring([""] * 4 + ["hltPFMETNoMuProducer::HLT"] * 3 + [""] * 2)
        producer.pfMETNoMuThresholds             = cms.vdouble([0.0] * 4 + [120.0, 130.0, 140.0] + [0.0] * 2)
        producer.pfMETNoMuJetsForTag             = cms.vstring([""] * 9)

        producer.pfMHTNoMuCollections            = cms.vstring([""] * 4 + ["hltPFMHTNoMuTightID::HLT"] * 3 + [""] * 2)
        producer.pfMHTNoMuThresholds             = cms.vdouble([0.0] * 4 + [120.0, 130.0, 140.0] + [0.0] * 2)
        producer.pfMHTNoMuJetsForTag             = cms.vstring([""] * 9)

        producer.additionalCollections           = cms.vstring(["hltTrk50Filter::HLT"] + [""] * 8)
        producer.additionalFilters               = cms.vstring(["hltTrk50Filter"] + [""] * 8)

    else:
        print("EventMETTriggerProducer_cfg.py does not know which MET trigger filters to apply!")
        exit (1)

    return producer
