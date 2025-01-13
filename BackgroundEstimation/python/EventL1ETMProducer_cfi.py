#!/usr/bin/env python3

import os
import FWCore.ParameterSet.Config as cms

def customizeForL1ETMProducer (producer, year="2022"):
    producer.filterCategories = cms.vstring (
        "etm",
    )

    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_"):
        print("# Using 2015 MET trigger filters in EventL1ETMProducer_cfi.py...")

        # The items in each vector correspond to the following triggers, in this order:
        # [HLT_MET250_v*, HLT_MET75_IsoTrk50_v*, HLT_PFMET120_PFMHT120_IDTight_v*, HLT_PFMET170_HBHECleaned_v*, HLT_PFMET170_JetIdCleaned_v*, HLT_PFMET170_NoiseCleaned_v*, HLT_PFMET170_v*, HLT_PFMET90_PFMHT90_IDTight_v*, HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*, HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*]

        producer.etmCollections              = cms.vstring ("hltL1extraParticles:MET:HLT")
        producer.etmFilterSubstrings         = cms.vstring ("")
        producer.etmFilterSubstringsToReject = cms.vstring ("HTT")

        producer.additionalCollections  =  cms.vstring  ()
        producer.additionalFilters      =  cms.vstring  ()

        producer.l1Prescales = cms.FileInPath ("DisappTrks/BackgroundEstimation/data/l1ETM_2015.txt")

        if producer.type_ () == "EventElectronL1ETMProducer":
            producer.tagCollection = cms.string ("hltL1extraParticles:Isolated:HLT")
        elif producer.type_ () == "EventMuonL1ETMProducer":
            producer.tagCollection = cms.string ("hltL1extraParticles::HLT")
        elif producer.type_ () == "EventTauL1ETMProducer":
            producer.tagCollection = cms.string ("hltL1extraParticles:Tau:HLT")
        else:
            print("# Unknown producer type! Cannot set collection for tag lepton.")
            exit (1)

    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
        print("# Using 2016 MET trigger filters in EventL1ETMProducer_cfi.py...")

        # The items in each vector correspond to the following triggers, in this order:
        # [HLT_MET200_v*,  HLT_MET75_IsoTrk50_v*,  HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned_v*,  HLT_PFMET120_PFMHT120_IDTight_v*,  HLT_PFMET170_HBHECleaned_v*,  HLT_PFMET300_v*,  HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*]

        producer.etmCollections              = cms.vstring ("hltCaloStage2Digis:EtSum:HLT")
        producer.etmFilterSubstrings         = cms.vstring ("ETM")
        producer.etmFilterSubstringsToReject = cms.vstring ("HTT")

        producer.additionalCollections  =  cms.vstring  ()
        producer.additionalFilters      =  cms.vstring  ()

        producer.l1Prescales = cms.FileInPath ("DisappTrks/BackgroundEstimation/data/l1ETM_2016.txt")

        if producer.type_ () == "EventElectronL1ETMProducer":
            producer.tagCollection = cms.string ("hltCaloStage2Digis:EGamma:HLT")
        elif producer.type_ () == "EventMuonL1ETMProducer":
            producer.tagCollection = cms.string ("hltGmtStage2Digis:Muon:HLT")
        elif producer.type_ () == "EventTauL1ETMProducer":
            producer.tagCollection = cms.string ("hltCaloStage2Digis:Tau:HLT")
        else:
            print("# Unknown producer type! Cannot set collection for tag lepton.")
            exit (1)

    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
        print("# Using 2017 MET trigger filters in EventL1ETMProducer_cfg.py...")

        # The items in each vector correspond to the following triggers, in this order:
        # HLT_MET105_IsoTrk50_v*, HLT_PFMET120_PFMHT120_IDTight_v*

        producer.etmCollections              = cms.vstring ("hltGtStage2Digis:EtSum:HLT")
        producer.etmFilterSubstrings         = cms.vstring ("ETM")
        producer.etmFilterSubstringsToReject = cms.vstring ("HTT", "IsoTau")

        producer.additionalCollections = cms.vstring ()
        producer.additionalFilters     = cms.vstring ()

        producer.l1Prescales = cms.FileInPath ("DisappTrks/BackgroundEstimation/data/l1ETM_2017.txt")

        if producer.type_ () == "EventElectronL1ETMProducer":
            producer.tagCollection = cms.string ("hltGtStage2Digis:EGamma:HLT")
        elif producer.type_ () == "EventMuonL1ETMProducer":
            producer.tagCollection = cms.string ("hltGtStage2Digis:Muon:HLT")
        elif producer.type_ () == "EventTauL1ETMProducer":
            producer.tagCollection = cms.string ("hltGtStage2Digis:Tau:HLT")
        else:
            print("# Unknown producer type! Cannot set collection for tag lepton.")
            exit (1)

    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
        print("# Using 2018 MET trigger filters in EventL1ETMProducer_cfg.py...")

        # The items in each vector correspond to the following triggers, in this order:
        # HLT_MET105_IsoTrk50_v*, HLT_PFMET120_PFMHT120_IDTight_v*

        producer.etmCollections              = cms.vstring ("hltGtStage2Digis:EtSum:HLT")
        producer.etmFilterSubstrings         = cms.vstring ("ETM")
        producer.etmFilterSubstringsToReject = cms.vstring ("HTT", "IsoTau")

        producer.additionalCollections = cms.vstring ()
        producer.additionalFilters     = cms.vstring ()

        producer.l1Prescales = cms.FileInPath ("DisappTrks/BackgroundEstimation/data/l1ETM_2017.txt") #Should be fixed later

        if producer.type_ () == "EventElectronL1ETMProducer":
            producer.tagCollection = cms.string ("hltGtStage2Digis:EGamma:HLT")
        elif producer.type_ () == "EventMuonL1ETMProducer":
            producer.tagCollection = cms.string ("hltGtStage2Digis:Muon:HLT")
        elif producer.type_ () == "EventTauL1ETMProducer":
            producer.tagCollection = cms.string ("hltGtStage2Digis:Tau:HLT")
        else:
            print("# Unknown producer type! Cannot set collection for tag lepton.")
            exit (1)

    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
        print("# Using 2022 MET trigger filters in EventL1ETMProducer_cfg.py...")

        # The items in each vector correspond to the following triggers, in this order:
        # HLT_MET105_IsoTrk50_v*, HLT_PFMET120_PFMHT120_IDTight_v*

        producer.etmCollections              = cms.vstring ("hltGtStage2Digis:EtSum:HLT")
        producer.etmFilterSubstrings         = cms.vstring ("ETM")
        producer.etmFilterSubstringsToReject = cms.vstring ("HTT", "IsoTau")

        producer.additionalCollections = cms.vstring ()
        producer.additionalFilters     = cms.vstring ()

        if year == "2022":
            print("Using l1ETM DisappTrks/BackgroundEstimation/data/l1ETM_2022.txt")
            producer.l1Prescales = cms.FileInPath ("DisappTrks/BackgroundEstimation/data/l1ETM_2022.txt") #Should be fixed later
        else:
            print("Using l1ETM DisappTrks/BackgroundEstimation/data/l1ETM_2023.txt")
            producer.l1Prescales = cms.FileInPath ("DisappTrks/BackgroundEstimation/data/l1ETM_2023.txt") #Should be fixed later


        if producer.type_ () == "EventElectronL1ETMProducer":
            producer.tagCollection = cms.string ("hltGtStage2Digis:EGamma:HLT")
        elif producer.type_ () == "EventMuonL1ETMProducer":
            producer.tagCollection = cms.string ("hltGtStage2Digis:Muon:HLT")
        elif producer.type_ () == "EventTauL1ETMProducer":
            producer.tagCollection = cms.string ("hltGtStage2Digis:Tau:HLT")
        else:
            print("# Unknown producer type! Cannot set collection for tag lepton.")
            exit (1)

    else:
        print("EventL1ETMProducer_cfg.py does not know which MET trigger filters to apply!")
        exit (1)

    return producer
