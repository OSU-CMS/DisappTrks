import FWCore.ParameterSet.Config as cms
import os
import copy

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Switching to 2016 triggers since we are in " + os.environ["CMSSW_VERSION"] + "..."
else:
    print "# Using 2015 triggers since we are in " + os.environ["CMSSW_VERSION"] + "..."

##########################################################################################################
# Main triggers for signal selection
##########################################################################################################

triggersMetAndIsoTrk = cms.vstring(
    "HLT_MET75_IsoTrk50_v", # trigger designed for disappearing tracks
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

triggersMet = triggersMetAndIsoTrk + triggersMetInclusive

# List of triggers for EventTriggerVarProducer -- distinct from triggersMet since we don't use HLT_MET90_IsoTrk50_v for the main analysis
triggersForEfficiency = copy.deepcopy (triggersMet)
triggersForEfficiency.append("HLT_MET90_IsoTrk50_v")

##########################################################################################################
# Trigger filters used in signal HLT paths
# For efficiency measurements
# Most of these were easily found with the confDB GUI browser, excepting where noted
##########################################################################################################

triggerFiltersMet = {
    'HLT_MET75_IsoTrk50_v'                                  : ['hltMET75'],
    'HLT_MET90_IsoTrk50_v'                                  : ['hltMET90'],

    'HLT_MET250_v'                                         : ['hltMET250'],
    'HLT_PFMET120_PFMHT120_IDTight_v'                      : ['hltMET90', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120'],
    'HLT_PFMET170_HBHECleaned_v'                           : ['hltMET90', 'hltMETClean80', 'hltPFMET170Filter'],
    'HLT_PFMET170_JetIdCleaned_v'                          : ['hltMET90', 'hltMETCleanUsingJetID80', 'hltPFMET170Filter'],
    'HLT_PFMET170_NoiseCleaned_v'                          : ['hltMET90', 'hltMETClean80', 'hltMETCleanUsingJetID80', 'hltPFMET170Filter'],
    'HLT_PFMET170_v'                                       : ['hltMET90', 'hltPFMET170Filter'],
    'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v' : ['hltMET80', 'hltMETCleanUsingJetID70', 'hltMHT80', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
    'HLT_PFMET90_PFMHT90_IDTight_v'                        : ['hltMET70', 'hltMHT70', 'hltPFMHTTightID90', 'hltPFMET90'],
    'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v'   : ['hltMET80', 'hltMETCleanUsingJetID70', 'hltMHT80', 'hltPFMHTNoMuTightID90', 'hltPFMETNoMu90'],
}

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    triggerFiltersMet = {
        'HLT_MET75_IsoTrk50_v'                                  : ['hltMET75', 'hltMETClean65'],
        'HLT_MET90_IsoTrk50_v'                                  : ['hltMET90', 'hltMETClean80'],

        'HLT_MET200_v'                                         : ['hltMET200', 'hltMETClean190'],

        # below found in /dev/CMSSW_8_0_0/GRun/V166
        'HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned_v'      : ['hltMET80', 'hltMETClean70', 'hltMHT80', 'hltPFMHTTightID100', 'hltPFMET100', 'hltMETCleanBH70'],

        'HLT_PFMET120_PFMHT120_IDTight_v'                      : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120'],
        'HLT_PFMET170_HBHECleaned_v'                           : ['hltMET90', 'hltMETClean80', 'hltPFMET170'],
        'HLT_PFMET300_v'                                       : ['hltMET90', 'hltMETClean80', 'hltPFMET300'],
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'              : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
    }

triggerFiltersTrack = {
    'HLT_MET75_IsoTrk50_v' : ['hltTrk50Filter'],
    'HLT_MET90_IsoTrk50_v' : ['hltTrk50Filter'],
}

# Flat cms.vstring of filters for use in EventTriggerVarProducer
triggerFiltersInclusive = cms.vstring()
for filt in [f for fList in (triggerFiltersMet.values() + triggerFiltersTrack.values()) for f in fList]:
    if filt not in triggerFiltersInclusive:
        triggerFiltersInclusive.append(filt)

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

##########################################################################################################
# Single Tau triggers
##########################################################################################################

triggersSingleTau = cms.vstring(
    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v", # prescaled in data
)

triggersZeroBias = cms.vstring(
    "HLT_ZeroBias_v", # very prescaled in data
)
