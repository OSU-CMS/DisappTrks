import FWCore.ParameterSet.Config as cms
import os

##########################################################################################################
# Trigger filters used in all HLT paths
# For efficiency measurements
# Most of these were easily found with the confDB GUI browser, excepting where noted
##########################################################################################################

triggerFiltersMet = {
    # 2015-2016
    'HLT_MET75_IsoTrk50_v'                                  : ['hltMET75'],
    'HLT_MET90_IsoTrk50_v'                                  : ['hltMET90'],

    # 2015
    'HLT_MET250_v'                                         : ['hltMET250'],
    'HLT_PFMET120_PFMHT120_IDTight_v'                      : ['hltMET90', 'hltMHT90', 'hltPFMHTTightID120', 'hltPFMET120'],
    'HLT_PFMET170_HBHECleaned_v'                           : ['hltMET90', 'hltMETClean80', 'hltPFMET170Filter'],
    'HLT_PFMET170_JetIdCleaned_v'                          : ['hltMET90', 'hltMETCleanUsingJetID80', 'hltPFMET170Filter'],
    'HLT_PFMET170_NoiseCleaned_v'                          : ['hltMET90', 'hltMETClean80', 'hltMETCleanUsingJetID80', 'hltPFMET170Filter'],
    'HLT_PFMET170_v'                                       : ['hltMET90', 'hltPFMET170Filter'],
    'HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v' : ['hltMET80', 'hltMETCleanUsingJetID70', 'hltMHT80', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
    'HLT_PFMET90_PFMHT90_IDTight_v'                        : ['hltMET70', 'hltMHT70', 'hltPFMHTTightID90', 'hltPFMET90'],
    'HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v'   : ['hltMET80', 'hltMETCleanUsingJetID70', 'hltMHT80', 'hltPFMHTNoMuTightID90', 'hltPFMETNoMu90'],

    # 2016
    'HLT_MET200_v'                                         : ['hltMET200', 'hltMETClean190'],

    # below found in /dev/CMSSW_8_0_0/GRun/V166
    'HLT_PFMET100_PFMHT100_IDTight_BeamHaloCleaned_v'      : ['hltMET80', 'hltMETClean70', 'hltMHT80', 'hltPFMHTTightID100', 'hltPFMET100', 'hltMETCleanBH70'],

    'HLT_PFMET300_v'                                       : ['hltMET90', 'hltMETClean80', 'hltPFMET300'],
    'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v'              : ['hltMET90', 'hltMETClean80', 'hltMHT90', 'hltPFMHTNoMuTightID120', 'hltPFMETNoMu120'],
}

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_8_0_"):
    triggerFiltersMet['HLT_MET75_IsoTrk50_v'].append('hltMETClean65')
    triggerFiltersMet['HLT_MET90_IsoTrk50_v'].append('hltMETClean80')
    triggerFiltersMet['HLT_PFMET120_PFMHT120_IDTight_v'].append('hltMETClean80')

triggerFiltersTrack = {
    # 2015-2016
    'HLT_MET75_IsoTrk50_v' : ['hltTrk50Filter'],
    'HLT_MET90_IsoTrk50_v' : ['hltTrk50Filter'],
}

if os.environ["CMSSW_VERSION"].startswith ("CMSSW_9_2_"):
    triggerFiltersMet = {
        # 2017
        'HLT_MET105_IsoTrk50_v'                                  : ['hltMET105', 'hltMETClean65'],
        'HLT_MET120_IsoTrk50_v'                                  : ['hltMET120', 'hltMETClean65'],

        # add inclusive MET triggers...
    }

    triggerFiltersTrack = {
        # 2017
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
