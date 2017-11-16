import FWCore.ParameterSet.Config as cms
import os
import copy

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Triggers: 2016"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# Triggers: 2017"
else:
    print "# Triggers: 2015"

##########################################################################################################
# Main triggers for signal selection
##########################################################################################################

triggersMetAndIsoTrk = cms.vstring(
    "HLT_MET75_IsoTrk50_v", # trigger designed for disappearing tracks
)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    triggersMetAndIsoTrk = cms.vstring(
        "HLT_MET105_IsoTrk50_v", # trigger designed for disappearing tracks
    )

triggersMetInclusive = cms.vstring(
    "HLT_MET250_v",
    "HLT_PFMET120_PFMHT120_IDTight_v",
    "HLT_PFMET170_HBHECleaned_v",
    "HLT_PFMET170_JetIdCleaned_v",
    "HLT_PFMET170_NoiseCleaned_v",
    "HLT_PFMET170_v",
    "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v",

    # these two are missing ~10/pb in 2015, but they're close enough
    "HLT_PFMET90_PFMHT90_IDTight_v",
    "HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v",
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    triggersMetInclusive = cms.vstring(
        "HLT_MET200_v",
        "HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned_v",
        "HLT_PFMET120_PFMHT120_IDTight_v",
        "HLT_PFMET170_HBHECleaned_v",
        "HLT_PFMET300_v",
        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v",
    )

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    triggersMetInclusive = cms.vstring(
        # available throughout 2017
        'HLT_PFMET120_PFMHT120_IDTight_v',
        'HLT_PFMET130_PFMHT130_IDTight_v',
        'HLT_PFMET140_PFMHT140_IDTight_v',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
        
        # available starting 2017C
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
        'HLT_PFMET120_PFMHT120_IDTight_HFCleaned_v',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_HFCleaned_v',
        'HLT_PFMET250_HBHECleaned_v',
        'HLT_PFMET300_HBHECleaned_v',
    )

triggersMet = triggersMetAndIsoTrk + triggersMetInclusive

##########################################################################################################
# Single Muon triggers
##########################################################################################################

triggersSingleMu = cms.vstring( # recommended here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Trigger
    "HLT_IsoMu20_v",    # yes available in bkgd MC
    "HLT_IsoTkMu20_v",  # yes available in bkgd MC
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    triggersSingleMu = cms.vstring( # recommended here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Trigger
        "HLT_IsoMu24_v",    # yes available in bkgd MC
        "HLT_IsoTkMu24_v",  # yes available in bkgd MC
    )

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    triggersSingleMu = cms.vstring(
        "HLT_IsoMu27_v",
    )

##########################################################################################################
# Single Electron triggers
##########################################################################################################

triggersSingleEle = cms.vstring(
    "HLT_Ele22_eta2p1_WPLoose_Gsf_v", # available in the data
    "HLT_Ele22_eta2p1_WP75_Gsf_v",    # available in the bkgd MC
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    triggersSingleEle = cms.vstring(
        "HLT_Ele25_eta2p1_WPTight_Gsf_v",
        #"HLT_Ele27_WPTight_Gsf_v", # only in case we need to look at electrons with |eta| >= 2.1
        "HLT_Ele22_eta2p1_WP75_Gsf_v", # available in the 76X bkgd MC
    )

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    triggersSingleEle = cms.vstring(
        "HLT_Ele35_WPTight_Gsf_v",
        "HLT_Ele22_eta2p1_WP75_Gsf_v", # available in the 76X bkgd MC
    )

##########################################################################################################
# Single Tau triggers
##########################################################################################################

triggersSingleTau = cms.vstring(
    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v", # prescaled in data
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    triggersSingleTau = cms.vstring(
        "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v",
    )

triggersZeroBias = cms.vstring(
    "HLT_ZeroBias_v", # very prescaled in data
)
