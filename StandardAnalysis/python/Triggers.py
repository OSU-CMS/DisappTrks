import FWCore.ParameterSet.Config as cms
import os

triggersMetAndIsoTrk = cms.vstring(
    "HLT_MET75_IsoTrk50_v", # trigger designed for disappearing tracks
)

triggersMetInclusive = cms.vstring(
    # monojet triggers in the data, unprescaled for all of 2015, see EXO-15-003 PAS / AN2015_072_v8 Table 6
    "HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v",   # 74X MC
    "HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v",   # 2015D 76X ReReco Part 1
    "HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v",                # 2015D 76X ReReco Part 2  && RunIIFall15MiniAODv2_76X MC

    "HLT_PFMETNoMu100_PFMHTNoMu100_IDTight_v",
    "HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_v",
    "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v",

    "HLT_PFMET170_BeamHaloCleaned_v",
    "HLT_PFMET170_HBHECleaned_v",
    "HLT_PFMET170_JetIdCleaned_v",
    "HLT_PFMET170_NoiseCleaned_v",
    "HLT_PFMET170_NotCleaned_v",
)

triggersMet = triggersMetAndIsoTrk + triggersMetInclusive

triggersSingleMu = cms.vstring( # recommended here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Trigger
    "HLT_IsoMu20_v",    # yes available in bkgd MC
    "HLT_IsoTkMu20_v",  # yes available in bkgd MC
)

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "Switching to 2016 single muon triggers since we are in " + os.environ["CMSSW_VERSION"] + "..."
    triggersSingleMu = cms.vstring( # recommended here: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonIdRun2#Muon_Trigger
        "HLT_IsoMu22_v",    # yes available in bkgd MC
        "HLT_IsoTkMu22_v",  # yes available in bkgd MC
    )
else:
    print "Using 2015 single muon triggers since we are in " + os.environ["CMSSW_VERSION"] + "..."

triggersSingleEle = cms.vstring(
    "HLT_Ele22_eta2p1_WPLoose_Gsf_v", # available in the data
    "HLT_Ele22_eta2p1_WP75_Gsf_v",    # available in the bkgd MC
    "HLT_Ele25_eta2p1_WPLoose_Gsf_v"  # available in the 2016 data
)

triggersSingleTau = cms.vstring(
    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v", # prescaled in data
)
