import FWCore.ParameterSet.Config as cms
import os

##########################################################################################################
# Trigger filters used in all HLT paths
# For efficiency measurements
# Most of these were easily found with the confDB GUI browser, excepting where noted
##########################################################################################################

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print("# Trigger filters: 2016")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print("# Trigger filters: 2017")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    print("# Trigger filters: 2018")
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    print("# Trigger filters: 2022")
else:
    print("# Trigger filters: 2015")
    
# 2015 values by default

triggerFiltersMet = {
    'HLT_MET75_IsoTrk50_v'                                  : ['hltMET75'],
    'HLT_MET90_IsoTrk50_v'                                  : ['hltMET90'],

    'HLT_MET250_v'                                         : ['hltMET250'],
    'HLT_PFMET120_PFMHT120_IDTight_v'                      : ['hltMET90', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120'], # 2016-2017 also
    'HLT_PFMET170_HBHECleaned_v'                           : ['hltMET90', 'hltMETClean80', 'hltPFMET170Filter'],
    'HLT_PFMET170_JetIdCleaned_v'                          : ['hltMET90', 'hltMETCleanUsingJetID80', 'hltPFMET170Filter'],
    'HLT_PFMET170_NoiseCleaned_v'                          : ['hltMET90', 'hltMETClean80', 'hltMETCleanUsingJetID80', 'hltPFMET170Filter'],
    'HLT_PFMET170_v'                                       : ['hltMET90', 'hltPFMET170Filter'],
    'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v' : ['hltMET80', 'hltMETCleanUsingJetID70', 'hltMHT80', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
    'HLT_PFMET90_PFMHT90_IDTight_v'                        : ['hltMET70', 'hltMHT70', 'hltPFMHTTightID90', 'hltPFMET90'],
    'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v'   : ['hltMET80', 'hltMETCleanUsingJetID70', 'hltMHT80', 'hltPFMHTNoMuTightID90', 'hltPFMETNoMu90'],
}

triggerFiltersTrack = {
    'HLT_MET75_IsoTrk50_v' : ['hltTrk50Filter'],
    'HLT_MET90_IsoTrk50_v' : ['hltTrk50Filter'],
}

# durp
triggerFiltersElectron = ("", "")
triggerFiltersMuon = ("", "")
triggerFiltersTau = ("", "")

# 2016
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    triggerFiltersMet = {
        'HLT_MET75_IsoTrk50_v'                                  : ['hltMET75', 'hltMETClean65'],
        'HLT_MET90_IsoTrk50_v'                                  : ['hltMET90', 'hltMETClean80'],

        'HLT_MET200_v'                                         : ['hltMET200', 'hltMETClean190'],
        'HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned_v'      : ['hltMET80', 'hltMETClean70', 'hltMHT80', 'hltPFMHTTightID100', 'hltPFMET100', 'hltMETCleanBH70'], # found in /dev/CMSSW_8_0_0/GRun/V166
        'HLT_PFMET120_PFMHT120_IDTight_v'                      : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120'], # 2016-2017 also
        'HLT_PFMET170_HBHECleaned_v'                           : ['hltMET90', 'hltMETClean80', 'hltPFMET170Filter'],
        'HLT_PFMET300_v'                                       : ['hltMET90', 'hltMETClean80', 'hltPFMET300'],
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'              : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'], # 2017 also
    }

    # triggerFiltersTrack unchanged from 2015

# 2017
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    triggerFiltersMet = {
        'HLT_MET105_IsoTrk50_v'                                 : ['hltMET105', 'hltMETClean65'],
        'HLT_MET120_IsoTrk50_v'                                 : ['hltMET120', 'hltMETClean65'],

        # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/180522_173113/lumis_for_MET_triggers_2017_sorted.pdf

        # this one path adds the most signal acceptance of all single paths
        'HLT_PFMET120_PFMHT120_IDTight_v'                       : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120'], # 2016-2017 also

        # additional paths allowed in the MET ntuples skim, 
        # and acceptable in terms of not being disabled/prescaled
        'HLT_PFMET130_PFMHT130_IDTight_v'                      : ['hltMET100', 'hltMETClean90', 'hltMHT100', 'hltPFMHTTightID130', 'hltPFMET130'],
        'HLT_PFMET140_PFMHT140_IDTight_v'                      : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTTightID140', 'hltPFMET140'], # perfect trigger B-F!
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'              : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v'              : ['hltMET100', 'hltMETClean90', 'hltMHT100', 'hltPFMHTNoMuTightID130', 'hltPFMETNoMu130'],
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v'              : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTNoMuTightID140', 'hltPFMETNoMu140'],
        'HLT_PFMET250_HBHECleaned_v'                           : ['hltMET90', 'hltMETClean80', 'hltPFMET250'],
        'HLT_PFMET300_HBHECleaned_v'                           : ['hltMET90', 'hltMETClean80', 'hltPFMET300'],

        # not allowed in the MET ntuples skim, but could possibly be considered
        # fixme: what are the filters for these?
        #'HLT_PFMETTypeOne140_PFMHT140_IDTight_v'               : [], # perfect trigger B-F!
        #'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v'           : [],
        #'HLT_PFMETTypeOne120_PFMHT120_IDTight_v'               : [],
        #'HLT_PFMETTypeOne130_PFMHT130_IDTight_v'               : [],
    }

    triggerFiltersTrack = {
        'HLT_MET105_IsoTrk50_v' : ['hltTrk50Filter'],
        'HLT_MET120_IsoTrk50_v' : ['hltTrk50Filter'],
    }

    triggerFiltersElectron = ("hltEgammaCandidates::HLT", "hltEle35noerWPTightGsfTrackIsoFilter")
    triggerFiltersMuon = ("hltIterL3MuonCandidates::HLT", "hltL3crIsoL1sMu22Or25L1f0L2f10QL3f27QL3trkIsoFiltered0p07")
    triggerFiltersTau = ("hltSelectedPFTausTrackPt30MediumAbsOrRelIsolation1Prong::HLT", "hltPFTau50TrackPt30MediumAbsOrRelIso1Prong")

# 2018
if os.environ["CMSSW_VERSION"].startswith ("CMSSW_10_2_"):
    triggerFiltersMet = {
        'HLT_MET105_IsoTrk50_v'                                 : ['hltMET105', 'hltMETClean65'],
        'HLT_MET120_IsoTrk50_v'                                 : ['hltMET120', 'hltMETClean65'],

        'HLT_PFMET120_PFMHT120_IDTight_v'            : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120'],
        'HLT_PFMET130_PFMHT130_IDTight_v'            : ['hltMET100', 'hltMETClean90', 'hltMHT100', 'hltPFMHTTightID130', 'hltPFMET130'],
        'HLT_PFMET140_PFMHT140_IDTight_v'            : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTTightID140', 'hltPFMET140'],
        'HLT_PFMETTypeOne140_PFMHT140_IDTight_v'     : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTTightID140', 'hltPFMETTypeOne140'],
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'    : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v'    : ['hltMET100', 'hltMETClean90', 'hltMHT100', 'hltPFMHTNoMuTightID130', 'hltPFMETNoMu130'],
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v'    : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTNoMuTightID140', 'hltPFMETNoMu140'],
        'HLT_PFMET250_HBHECleaned_v'                 : ['hltMET90', 'hltMETClean80', 'hltPFMET250'],
        'HLT_PFMET300_HBHECleaned_v'                 : ['hltMET90', 'hltMETClean80', 'hltPFMET300'],
        'HLT_PFMET200_HBHE_BeamHaloCleaned_v'        : ['hltMET90', 'hltMETClean80', 'hltPFMET200', 'hltMETCleanBH80'],
        'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v' : ['hltMET90', 'hltMETClean80', 'hltPFMETTypeOne200', 'hltMETCleanBH80'],
    }

    triggerFiltersTrack = {
        'HLT_MET105_IsoTrk50_v' : ['hltTrk50Filter'],
        'HLT_MET120_IsoTrk50_v' : ['hltTrk50Filter'],
    }

    triggerFiltersElectron = ("hltEgammaCandidates::HLT", "hltEle32WPTightGsfTrackIsoFilter")
    triggerFiltersMuon = ("hltIterL3MuonCandidates::HLT", "hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered0p07")
    triggerFiltersTau = ("hltSelectedPFTausTrackPt30MediumAbsOrRelIsolation1Prong::HLT", "hltPFTau50TrackPt30MediumAbsOrRelIso1Prong")

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_12_4_") or os.environ["CMSSW_VERSION"].startswith ("CMSSW_13_0_"):
    triggerFiltersMet = {
        'HLT_MET105_IsoTrk50_v'                                 : ['hltMET105'],
        'HLT_MET120_IsoTrk50_v'                                 : ['hltMET120'],
        'HLT_PFMET105_IsoTrk50_v'                               : ['hltMET75','hltPFMET105'],


        'HLT_PFMET120_PFMHT120_IDTight_v'                   : ['hltMET90', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120'],
        'HLT_PFMET130_PFMHT130_IDTight_v'                   : ['hltMET100', 'hltMHT100', 'hltPFMHTTightID130', 'hltPFMET130'],
        'HLT_PFMET140_PFMHT140_IDTight_v'                   : ['hltMET110', 'hltMHT110', 'hltPFMHTTightID140', 'hltPFMET140'],

        'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight_FilterHF_v'  : ['hltMET80','hltMHT80','hltPFMHTNoMuTight110HFCleaned','hltPFMETNoMu110'],
        'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'           : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
        'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v'           : ['hltMET100', 'hltMETClean90', 'hltMHT100', 'hltPFMHTNoMuTightID130', 'hltPFMETNoMu130'],
        'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v'           : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTNoMuTightID140', 'hltPFMETNoMu140'],
    }

    triggerFiltersTrack = {
        'HLT_MET105_IsoTrk50_v' : ['hltTrk50Filter'],
        'HLT_MET120_IsoTrk50_v' : ['hltTrk50Filter'],
        'HLT_PFMET105_IsoTrk50_v' : ['hltTrk50Filter']
    }

    triggerFiltersElectron = ("hltEgammaCandidates::HLT", "hltEle32WPTightGsfTrackIsoFilter")
    triggerFiltersMuon = ("hltIterL3MuonCandidates::HLT", "hltL3crIsoL1sSingleMu22L1f0L2f10QL3f24QL3trkIsoFiltered")
    triggerFiltersTau = ("hltHpsSinglePFTau20MediumDitauWPDeepTauNoMatchForVBFIsoTau::HLT", "hltHpsOverlapFilterIsoMu24MediumDeepTauPFTau20")


# Flat cms.vstring of filters for use in EventTriggerVarProducer
triggerFiltersInclusive = cms.vstring()
for filt in [f for fList in (list(triggerFiltersMet.values()) + list(triggerFiltersTrack.values())) for f in fList]:
    if filt not in triggerFiltersInclusive:
        triggerFiltersInclusive.append(filt)

# Flat cms.vstring of triggers for use in EventTriggerVarProducer
triggerNamesInclusive = cms.vstring()
for trig in triggerFiltersMet:
    triggerNamesInclusive.append(trig)
