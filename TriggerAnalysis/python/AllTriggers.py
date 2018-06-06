import FWCore.ParameterSet.Config as cms
import os

##########################################################################################################
# Trigger filters used in all HLT paths
# For efficiency measurements
# Most of these were easily found with the confDB GUI browser, excepting where noted
##########################################################################################################

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    print "# Trigger filters: 2016"
elif os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_4_"):
    print "# Trigger filters: 2017"
else:
    print "# Trigger filters: 2015"
    
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

        'HLT_PFMET120_PFMHT120_IDTight_v'                      : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120'], # 2016-2017 also
        #'HLT_PFMET130_PFMHT130_IDTight_v'                      : ['hltMET100', 'hltMETClean90', 'hltMHT100', 'hltPFMHTTightID130', 'hltPFMET130'],
        #'HLT_PFMET140_PFMHT140_IDTight_v'                      : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTTightID140', 'hltPFMET140'],
        #'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'              : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'], # 2017 also
        #'HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v'              : ['hltMET100', 'hltMETClean90', 'hltMHT100', 'hltPFMHTNoMuTightID130', 'hltPFMETNoMu130'],
        #'HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v'              : ['hltMET110', 'hltMETClean100', 'hltMHT110', 'hltPFMHTNoMuTightID140', 'hltPFMETNoMu140'],
        #'HLT_PFMET120_PFMHT120_IDTight_HFCleaned_v'            : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120', 'hltPFMETHFCleaned120'],
        #'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_HFCleaned_v'    : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120', 'hltPFMETNoMuHFCleaned120'],
        #'HLT_PFMET250_HBHECleaned_v'                           : ['hltMET90', 'hltMETClean80', 'hltPFMET250'],
        #'HLT_PFMET300_HBHECleaned_v'                           : ['hltMET90', 'hltMETClean80', 'hltPFMET300'],

        #'HLT_PFMET200_HBHE_BeamHaloCleaned_v'                  : [],
        #'HLT_PFMETTypeOne120_PFMHT120_IDTight_v'               : [],
        #'HLT_PFMETTypeOne130_PFMHT130_IDTight_v'               : [],
        #'HLT_PFMETTypeOne140_PFMHT140_IDTight_v'               : [],
        #'HLT_PFMETTypeOne200_HBHE_BeamHaloCleaned_v'           : [],


    }

    triggerFiltersTrack = {
        'HLT_MET105_IsoTrk50_v' : ['hltTrk50Filter'],
        'HLT_MET120_IsoTrk50_v' : ['hltTrk50Filter'],
    }

# Flat cms.vstring of filters for use in EventTriggerVarProducer
triggerFiltersInclusive = cms.vstring()
for filt in [f for fList in (triggerFiltersMet.values() + triggerFiltersTrack.values()) for f in fList]:
    if filt not in triggerFiltersInclusive:
        triggerFiltersInclusive.append(filt)

# Flat cms.vstring of triggers for use in EventTriggerVarProducer
triggerNamesInclusive = cms.vstring()
for trig in triggerFiltersMet:
    triggerNamesInclusive.append(trig)
