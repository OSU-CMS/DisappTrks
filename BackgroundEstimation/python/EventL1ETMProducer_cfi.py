#!/usr/bin/env python

import os
import FWCore.ParameterSet.Config as cms

def customizeForL1ETMProducer (producer):
    producer.filterCategories = cms.vstring (
        "etm",
    )

    if os.environ["CMSSW_VERSION"].startswith ("CMSSW_7_6_"):
        print "# Using 2015 MET trigger filters in EventL1ETMProducer_cfi.py..."

        # The items in each vector correspond to the following triggers, in this order:
        # [HLT_MET250_v*, HLT_MET75_IsoTrk50_v*, HLT_PFMET120_PFMHT120_IDTight_v*, HLT_PFMET170_HBHECleaned_v*, HLT_PFMET170_JetIdCleaned_v*, HLT_PFMET170_NoiseCleaned_v*, HLT_PFMET170_v*, HLT_PFMET90_PFMHT90_IDTight_v*, HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*, HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*]

        producer.etmCollections                 =  cms.vstring  ("hltL1extraParticles:MET:HLT")
        producer.etmFilterPrefixes                 =  cms.vstring  ("")

        producer.additionalCollections  =  cms.vstring  ()
        producer.additionalFilters      =  cms.vstring  ()

        producer.l1Prescales = cms.FileInPath ("DisappTrks/BackgroundEstimation/data/l1ETM_2016BC.txt")

        if producer.type_ () == "EventElectronL1ETMProducer":
            producer.tagCollection = cms.string ("hltL1extraParticles:Isolated:HLT")
        elif producer.type_ () == "EventMuonL1ETMProducer":
            producer.tagCollection = cms.string ("hltL1extraParticles::HLT")
        elif producer.type_ () == "EventTauL1ETMProducer":
            producer.tagCollection = cms.string ("hltL1extraParticles:Tau:HLT")
        else:
            print "# Unknown producer type! Cannot set collection for tag lepton."
            exit (1)

    elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
        print "# Using 2016 MET trigger filters in EventL1ETMProducer_cfi.py..."

        # The items in each vector correspond to the following triggers, in this order:
        # [HLT_MET200_v*,  HLT_MET75_IsoTrk50_v*,  HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned_v*,  HLT_PFMET120_PFMHT120_IDTight_v*,  HLT_PFMET170_HBHECleaned_v*,  HLT_PFMET300_v*,  HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*]

        producer.etmCollections                 =  cms.vstring  ("hltCaloStage2Digis:EtSum:HLT")
        producer.etmFilterPrefixes                 =  cms.vstring  ("hltL1sETM")

        producer.additionalCollections  =  cms.vstring  ()
        producer.additionalFilters      =  cms.vstring  ()

        producer.l1Prescales = cms.FileInPath ("DisappTrks/BackgroundEstimation/data/l1ETM_2016DEFGH.txt")

        if producer.type_ () == "EventElectronL1ETMProducer":
            producer.tagCollection = cms.string ("hltCaloStage2Digis:EGamma:HLT")
        elif producer.type_ () == "EventMuonL1ETMProducer":
            producer.tagCollection = cms.string ("hltGmtStage2Digis:Muon:HLT")
        elif producer.type_ () == "EventTauL1ETMProducer":
            producer.tagCollection = cms.string ("hltCaloStage2Digis:Tau:HLT")
        else:
            print "# Unknown producer type! Cannot set collection for tag lepton."
            exit (1)

    else:
        print "EventL1ETMProducer_cfg.py does not know which MET trigger filters to apply!"
        exit (1)

    return producer
