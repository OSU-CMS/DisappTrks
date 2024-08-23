import FWCore.ParameterSet.Config as cms
import os
import copy

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print("# Triggers: 2016")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print("# Triggers: 2017")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print("# Triggers: 2018")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    print("# Triggers: 2022 FIXME")
else:
    print("# Triggers: 2015")

##########################################################################################################
# Main triggers for signal selection
##########################################################################################################

triggersMetAndIsoTrk = cms.vstring(
    "HLT_MET75_IsoTrk50_v", # trigger designed for disappearing tracks
)
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    triggersMetAndIsoTrk = cms.vstring(
        "HLT_MET105_IsoTrk50_v", # trigger designed for disappearing tracks
    )
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    triggersMetAndIsoTrk = cms.vstring(
        "HLT_MET105_IsoTrk50_v", # trigger designed for disappearing tracks
        "HLT_MET120_IsoTrk50_v",
        "HLT_PFMET105_IsoTrk50_v", # trigger designed for disappearing tracks
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

        # https://milliqanelog.asc.ohio-state.edu:8080/DisappearingTracks/935

        # this one path adds the most signal acceptance of all single paths
        'HLT_PFMET120_PFMHT120_IDTight_v',

        # additional paths allowed in the MET ntuples skim, 
        # and acceptable in terms of not being disabled/prescaled
        'HLT_PFMET130_PFMHT130_IDTight_v',
        'HLT_PFMET140_PFMHT140_IDTight_v', # perfect trigger B-F!
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
        'HLT_PFMET250_HBHECleaned_v',
        'HLT_PFMET300_HBHECleaned_v',

        # not allowed in the MET ntuples skim, but could possibly be considered
        #'HLT_PFMETTypeOne140_PFMHT140_IDTight_v', # perfect trigger B-F!
        #'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v',
        #'HLT_PFMETTypeOne120_PFMHT120_IDTight_v',
        #'HLT_PFMETTypeOne130_PFMHT130_IDTight_v',
    )

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    triggersMetInclusive = cms.vstring(
        "HLT_PFMET120_PFMHT120_IDTight_v",
        "HLT_PFMET130_PFMHT130_IDTight_v",
        "HLT_PFMET140_PFMHT140_IDTight_v",
        "HLT_PFMETTypeOne140_PFMHT140_IDTight_v",
        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v",
        "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v",
        "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v",
        "HLT_PFMET250_HBHECleaned_v",
        "HLT_PFMET300_HBHECleaned_v",
        "HLT_PFMET200_HBHE_BeamHaloCleaned_v",
        "HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v",
    )

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    triggersMetInclusive = cms.vstring(
        'HLT_PFMET120_PFMHT120_IDTight_v',
        'HLT_PFMET130_PFMHT130_IDTight_v',
        'HLT_PFMET140_PFMHT140_IDTight_v',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v',
        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_FilterHF_v',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_FilterHF_v',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_FilterHF_v',
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
        'HLT_PFMET120_PFMHT120_IDTight_PFHT60_v',
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

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    triggersSingleMu = cms.vstring(
        "HLT_IsoMu24_v",
    )

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"): #FIXME
    triggersSingleMu = cms.vstring(
        "HLT_IsoMu24_v",
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

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    triggersSingleEle = cms.vstring(
        "HLT_Ele32_WPTight_Gsf_v",
    )

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"): #FIXME
    triggersSingleEle = cms.vstring(
        "HLT_Ele32_WPTight_Gsf_v",
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

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    triggersSingleTau = cms.vstring(
        "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v",
    )

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"): #FIXME
    triggersSingleTau = cms.vstring(
        "HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v",
    )

triggersZeroBias = cms.vstring(
    "HLT_ZeroBias_v", # very prescaled in data
)

##########################################################################################################
# Single Tau triggers
##########################################################################################################

triggersMetAllYes = cms.vstring(
    'HLT_MET105_IsoTrk50_v',
    #'HLT_MET120_IsoTrk50_v',
    'HLT_PFMET140_PFMHT140_IDTight_v',
    'HLT_PFMET250_HBHECleaned_v',
    'HLT_PFMET300_HBHECleaned_v',
    'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
    'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
    'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v',
)

triggersMetAllYesNoDisabledB = cms.vstring(
    'HLT_PFMET140_PFMHT140_IDTight_v',
    'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
)

triggersMetAllMaybes = cms.vstring(
    'HLT_PFMET120_PFMHT120_IDTight_v',
    'HLT_PFMET130_PFMHT130_IDTight_v',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
    'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
    'HLT_PFMETTypeOne120_PFMHT120_IDTight_v',
    'HLT_PFMETTypeOne130_PFMHT130_IDTight_v',
)

triggersMetAllMaybesNoDisabledB = cms.vstring(
    'HLT_PFMET120_PFMHT120_IDTight_v',
    'HLT_PFMET130_PFMHT130_IDTight_v',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
    'HLT_PFMETTypeOne120_PFMHT120_IDTight_v',
    'HLT_PFMETTypeOne130_PFMHT130_IDTight_v',
)

triggersMetJustMain = cms.vstring(
    'HLT_MET105_IsoTrk50_v',
)

triggersMetOnlyPerfectNoMain2017 = cms.vstring(
    'HLT_PFMET140_PFMHT140_IDTight_v',
    'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
)

triggersMetOnlyPerfectAndMain2017 = cms.vstring(
    'HLT_MET105_IsoTrk50_v',
    'HLT_PFMET140_PFMHT140_IDTight_v',
    'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
)

triggersMetAllUnprescaled2017 = cms.vstring(
    'HLT_MET105_IsoTrk50_v',
    'HLT_PFMET140_PFMHT140_IDTight_v',
    'HLT_PFMET250_HBHECleaned_v',
    'HLT_PFMET300_HBHECleaned_v',
    'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
    'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
    'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v',
)

triggersMetAllowDisabledHighPU2017 = cms.vstring(
    'HLT_MET105_IsoTrk50_v',
    'HLT_PFMET140_PFMHT140_IDTight_v',
    'HLT_PFMET250_HBHECleaned_v',
    'HLT_PFMET300_HBHECleaned_v',
    'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v',
    'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
    'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v',
    'HLT_PFMET120_PFMHT120_IDTight_v',
    'HLT_PFMET130_PFMHT130_IDTight_v',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
    'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v',
    'HLT_PFMETTypeOne120_PFMHT120_IDTight_v',
    'HLT_PFMETTypeOne130_PFMHT130_IDTight_v',
)

triggersMetAllGoodInB = cms.vstring(
    'HLT_PFMET140_PFMHT140_IDTight_v',
    'HLT_PFMETTypeOne140_PFMHT140_IDTight_v',
    'HLT_PFMET120_PFMHT120_IDTight_v',
    'HLT_PFMET130_PFMHT130_IDTight_v',
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v',
    'HLT_PFMETTypeOne120_PFMHT120_IDTight_v',
    'HLT_PFMETTypeOne130_PFMHT130_IDTight_v',
)

# Although the EXO_DisappTrks selection uses many more triggers, since this is just for BG MC samples
# which will be subjected to one of the single lepton triggers at some point, the choice to only use
# these is to select/save fewer events to keep the files size manageable
triggersAllSkimming = triggersSingleMu + triggersSingleEle + triggersSingleTau
