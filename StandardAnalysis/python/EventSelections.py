import FWCore.ParameterSet.Config as cms
import copy

from DisappTrks.StandardAnalysis.MyCuts_disappTrks import * # Put all the individual cuts in this file 


##########################################################################
##### Preselection #####
##########################################################################

preselection = cms.PSet(
    name = cms.string("Preselection"),
    triggers = cms.vstring(
        "HLT_MET75_IsoTrk50", # trigger designed for disappearing tracks
        "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v1",  # monojet trigger, unprescaled for all of 2015
        "HLT_PFMET120_PFMHT120_IDTight_v1",   
        "HLT_PFMET170_v1", 
    ), 
    cuts = cms.VPSet (
        # EVENT HAS GOOD PV
        cms.PSet (
            inputCollection = cms.vstring("primaryvertexs"),
            cutString = cms.string("isValid > 0 && ndof >= 4"),
            numberRequired = cms.string(">= 1")
        ),
        # MET 
        cms.PSet(
            inputCollection = cms.vstring("mets"),
            cutString = cms.string("pt > 100"),
            numberRequired = cms.string(">= 1"),
        ),
        # JET PT 
        cms.PSet(
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("pt > 110"),
            numberRequired = cms.string(">= 1"),
        ), 
        # JET NOISE CLEANING
        cms.PSet(
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("chargedHadronEnergyFraction > 0.2"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # JET NOISE CLEANING
        cms.PSet(
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("chargedHadronEnergyFraction > 0.2"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # JET NOISE CLEANING
        cms.PSet(
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("chargedEmEnergyFraction < 0.5"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # JET NOISE CLEANING
        cms.PSet(
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("neutralHadronEnergyFraction < 0.7"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # JET NOISE CLEANING
        cms.PSet(
            inputCollection = cms.vstring("jets"),
            cutString = cms.string("neutralEmEnergyFraction < 0.7"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # TRACK PT 
        cms.PSet(
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("pt > 50"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # TRACK ETA
        cms.PSet(
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("fabs ( eta ) < 2.1"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # TRACK ETA:  BARREL-ENDCAP GAP VETO
        cms.PSet(
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("fabs ( eta ) < 1.42 || fabs ( eta ) > 1.65"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # TRACK ETA:  MUON INEFFICIENCY REGION 1
        cms.PSet(
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("fabs ( eta ) < 0.15 || fabs ( eta ) > 0.35"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # TRACK ETA:  MUON INEFFICIENCY REGION 2
        cms.PSet(
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("fabs ( eta ) < 1.55 || fabs ( eta ) > 1.85"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # # TRACK ETA:  NOT IN ECAL CRACKS:  UPDATE CRACK BOUNDARIES
        # cms.PSet(
        #     inputCollection = cms.vstring("tracks"),
        #     cutString = cms.string("fabs ( eta ) "),  
        #     numberRequired = cms.string(">= 1"),
        # ), 
        # TRACK NVALIDHITS
        cms.PSet(
            inputCollection = cms.vstring("tracks"),
            cutString = cms.string("numberOfValidHits >= 7"),  
            numberRequired = cms.string(">= 1"),
        ), 
        # # TRACK MISSING INNER HITS  
        # cms.PSet(
        #     inputCollection = cms.vstring("tracks"),
        #     cutString = cms.string("trackerExpectedHitsInner().numberOfHits() == 0"),  # INVALID SYNTAX
        #     numberRequired = cms.string(">= 1"),
        # ), 
        # # TRACK MISSING MIDDLE HITS  
        # cms.PSet(
        #     inputCollection = cms.vstring("tracks"),
        #     cutString = cms.string("hitPattern().trackerLayersWithoutMeasurement == 0"),  # INVALID SYNTAX
        #     numberRequired = cms.string(">= 1"),
        # ), 
        # # TRACK ISOLATION
        # cms.PSet(
        #     inputCollection = cms.vstring("tracks"),
        #     cutString = cms.string("trackRelIsoRp3 < 0.05"), # NEEDS TO BE CALCULATED IN SPECIAL PRODUCER
        #     numberRequired = cms.string(">= 1"),
        # ), 
        # # CALORIMETER ISOLATION
        # cms.PSet(
        #     inputCollection = cms.vstring("tracks"),
        #     cutString = cms.string("EcaloRp5 < 10"),   # NEEDS TO BE CALCULATED IN SPECIAL PRODUCER
        #     numberRequired = cms.string(">= 1"),
        # ), 
        # # TRACK MISSING OUTER HITS  
        # cms.PSet(
        #     inputCollection = cms.vstring("tracks"),
        #     cutString = cms.string("trackerExpectedHitsOuter().numberOfHits() == 0"),  # INVALID SYNTAX
        #     numberRequired = cms.string(">= 1"),
        # ), 
    )
)
