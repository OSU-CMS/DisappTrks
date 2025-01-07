import itertools

# all luminosities should be in inverse picobarns

def InsertYear(lumisThisYear, allLumis):
    for k in lumisThisYear.keys():
        # if not already present in allLumis, just add this entry
        if not k in allLumis.keys():
            allLumis[k] = lumisThisYear[k]
        # if this is already present in allLumis, we're on a prescaled path (a dict) and need to update rather than add/overwrite
        if k in allLumis.keys() and isinstance(allLumis[k], dict) and isinstance(lumisThisYear[k], dict):
            mergedDict = {}
            mergedDict.update(allLumis[k])
            mergedDict.update(lumisThisYear[k])
            allLumis[k] = mergedDict
        # if neither of these two cases, no idea what you're trying to do so we skip it
    return allLumis

def CreateCompositeLumis(allLumis, year, allPeriods):
    periods = []
    # in the case of 2015D there are no combinations
    if len(allPeriods) == 1:
        periods.append(allPeriods)
    else:
        # create all unique combinations of 2 or more periods
        for i in range(len(allPeriods) + 1):
            if i < 2:
                continue
            for c in itertools.combinations(allPeriods, i):
                periods.append(''.join(c))

    for pd in ['MET', 'SingleElectron', 'SingleMuon', 'Tau', 'ZeroBias', 'EGamma']:
        for period in periods:
            # define suffix like '_2016'
            suffix = '_' + year
            # if it's not the whole year (ie BC) call it _2016BC, otherwise keep 2016 BCDEFGH as just '_2016'
            if period != allPeriods:
                suffix += period

            # define a value for e.g. 'pd_2016BC' and then add 'pd_2016B' and 'pd_2016C' to it
            allLumis[pd + suffix] = 0.0
            for p in period:
                if not pd + '_' + year + p in allLumis:
                    continue
                allLumis[pd + suffix] += allLumis[pd + '_' + year + p]

    # do the same for specific triggers, e.g. ['HLT_xyz']['Tau_2016BC']
    for period in periods:
        # define suffix like '_2016'
        suffix = '_' + year
        # if it's not the whole year (ie BC) call it _2016BC, otherwise beep 2016 BCDEFGH as just '_2016'
        if period != allPeriods:
            suffix += period
        for tauTrigger in ['HLT_LooseIsoPFTau50_Trk30_eta2p1_v*', 'HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*']:
            if not tauTrigger in allLumis:
                continue
            # define a value for e.g. 'Tau_2016BC' and then add 'Tau_2016B' and 'Tau_2016C' to it
            allLumis[tauTrigger]['Tau' + suffix] = 0.0
            for p in period:
                if not 'Tau_' + year + p in allLumis[tauTrigger]:
                    continue
                allLumis[tauTrigger]['Tau' + suffix] += allLumis[tauTrigger]['Tau_' + year + p]

        if 'HLT_ZeroBias_v*' in allLumis:
            allLumis['HLT_ZeroBias_v*']['ZeroBias' + suffix] = 0.0
            for p in period:
                if not 'ZeroBias_' + year + p in allLumis['HLT_ZeroBias_v*']:
                    continue
                allLumis['HLT_ZeroBias_v*']['ZeroBias' + suffix] += allLumis['HLT_ZeroBias_v*']['ZeroBias_' + year + p]
    return allLumis

# Use PromptReco for 2016 or, if False, use 23Sep2016
usePrompt2016 = True

lumi_2015rereco = {

    "MET_2015D"            : 2672.144,
    "SingleElectron_2015D" : 2669.639,
    "SingleMuon_2015D"     : 2669.752,
    "Tau_2015D"            : 2672.153,

    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v*" : {
        "Tau_2015D"        : 225.172,
    },

    "ZeroBias_2015D"       : 0.0,
    "HLT_ZeroBias_v*" : {
        "ZeroBias_2015D"   : 0.0,
    },

}

lumi_23Sep2016 = {

    "MET_2016B"     :  5738.925,
    "MET_2016C"     :  2573.399,
    "MET_2016D"     :  4248.384,
    "MET_2016E"     :  4008.663,
    "MET_2016F"     :  3096.281,
    "MET_2016G"     :  7525.901,
    "MET_2016H_v2"  :  8390.54,
    "MET_2016H_v3"  :  215.149,

    "SingleElectron_2016B"     :  5678.099,
    "SingleElectron_2016C"     :  2357.325,
    "SingleElectron_2016D"     :  3942.136,
    "SingleElectron_2016E"     :  2924.728,
    "SingleElectron_2016F"     :  1888.193,
    "SingleElectron_2016G"     :  4053.038,
    "SingleElectron_2016H_v2"  :  8390.278,
    "SingleElectron_2016H_v3"  :  215.149,

    "SingleMuon_2016B"     :  5735.866,
    "SingleMuon_2016C"     :  2573.399,
    "SingleMuon_2016D"     :  4248.384,
    "SingleMuon_2016E"     :  3620.690,
    "SingleMuon_2016F"     :  2472.509,
    "SingleMuon_2016G"     :  4870.182,
    "SingleMuon_2016H_v2"  :  8390.540,
    "SingleMuon_2016H_v3"  :  215.149,

    "Tau_2016B"     :  5933.309,
    "Tau_2016C"     :  3.425,
    "Tau_2016D"     :  4353.449,
    "Tau_2016E"     :  4049.255,
    "Tau_2016F"     :  3160.088,
    "Tau_2016G"     :  7552.514,
    "Tau_2016H_v2"  :  8635.591,
    "Tau_2016H_v3"  :  221.442,

    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v*" : {
        "Tau_2016B"     :  712.32,
        "Tau_2016C"     :  81.448,
        "Tau_2016D"     :  135.498,
        "Tau_2016E"     :  116.127,
        "Tau_2016F"     :  66.043,
        "Tau_2016G"     :  114.391,
        "Tau_2016H_v2"  :  116.278,
        "Tau_2016H_v3"  :  3.092,
    },

    # These ZeroBias values are really PromptReco but we never processed the 23Sep2016 rereco for these
    "ZeroBias_2016B"     :  5733.453,
    "ZeroBias_2016C"     :  2573.399,
    "ZeroBias_2016D"     :  4248.383,
    "ZeroBias_2016E"     :  4009.130,
    "ZeroBias_2016F"     :  3079.608,
    "ZeroBias_2016G"     :  7488.562,
    "ZeroBias_2016H_v2"  :  8390.540,
    "ZeroBias_2016H_v3"  :  215.149,

    "HLT_ZeroBias_v*" : {
        "ZeroBias_2016B"     :  0.012195551,
        "ZeroBias_2016C"     :  0.001267369,
        "ZeroBias_2016D"     :  0.001898671,
        "ZeroBias_2016E"     :  0.00301127,
        "ZeroBias_2016F"     :  0.001710604,
        "ZeroBias_2016G"     :  0.003144164,
        "ZeroBias_2016H_v2"  :  0.005520328,
        "ZeroBias_2016H_v3"  :  0.000180316,
    },
}

lumi_2016Prompt = {

    "MET_2016B"     :  5740.666,
    "MET_2016C"     :  2573.399,
    "MET_2016D"     :  4241.828,
    "MET_2016E"     :  3967.714,
    "MET_2016F"     :  3096.281,
    "MET_2016G"     :  7522.287,
    "MET_2016H_v2"  :  8390.54,
    "MET_2016H_v3"  :  215.149,

    "SingleElectron_2016B"     :  5740.121,
    "SingleElectron_2016C"     :  2573.399,
    "SingleElectron_2016D"     :  4248.384,
    "SingleElectron_2016E"     :  4007.001,
    "SingleElectron_2016F"     :  3090.341,
    "SingleElectron_2016G"     :  7535.488,
    "SingleElectron_2016H_v2"  :  8390.278,
    "SingleElectron_2016H_v3"  :  215.149,

    "SingleMuon_2016B"     :  5733.079,
    "SingleMuon_2016C"     :  2573.399,
    "SingleMuon_2016D"     :  4071.484,
    "SingleMuon_2016E"     :  4009.132,
    "SingleMuon_2016F"     :  3092.106,
    "SingleMuon_2016G"     :  7540.488,
    "SingleMuon_2016H_v2"  :  8390.540,
    "SingleMuon_2016H_v3"  :  215.149,

    "Tau_2016B"     :  5737.738,
    "Tau_2016C"     :  2573.399,
    "Tau_2016D"     :  4248.384,
    "Tau_2016E"     :  4008.663,
    "Tau_2016F"     :  3099.583,
    "Tau_2016G"     :  7534.265,
    "Tau_2016H_v2"  :  8635.591,
    "Tau_2016H_v3"  :  221.442,

    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v*" : {
        "Tau_2016B"     :  712.32,
        "Tau_2016C"     :  81.448,
        "Tau_2016D"     :  135.498,
        "Tau_2016E"     :  116.127,
        "Tau_2016F"     :  66.043,
        "Tau_2016G"     :  114.311,
        "Tau_2016H_v2"  :  116.278,
        "Tau_2016H_v3"  :  3.092,
    },

    "ZeroBias_2016B"     :  5733.453,
    "ZeroBias_2016C"     :  2573.399,
    "ZeroBias_2016D"     :  4248.383,
    "ZeroBias_2016E"     :  4009.130,
    "ZeroBias_2016F"     :  3079.608,
    "ZeroBias_2016G"     :  7488.562,
    "ZeroBias_2016H_v2"  :  8390.540,
    "ZeroBias_2016H_v3"  :  215.149,

    "HLT_ZeroBias_v*" : {
        "ZeroBias_2016B"     :  0.012195551,
        "ZeroBias_2016C"     :  0.001267369,
        "ZeroBias_2016D"     :  0.001898671,
        "ZeroBias_2016E"     :  0.00301127,
        "ZeroBias_2016F"     :  0.001710604,
        "ZeroBias_2016G"     :  0.003144164,
        "ZeroBias_2016H_v2"  :  0.005520328,
        "ZeroBias_2016H_v3"  :  0.000180316,
    },
}

# set 2016 to either the rereco or prompt values depending on usePrompt2016
lumi_2016 = lumi_2016Prompt if usePrompt2016 else lumi_23Sep2016

lumi_2017 = {

    # filterJSON.py --min x --max y Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt --output Run2017x.json
    # 2017A: 295982-297004 ; no runs certifed
    # 2017B: 297031-299329
    # 2017C: 299368-302029
    # 2017D: 302031-302995
    # 2017E: 303569-304826
    # 2017F: 305033-306460
    # old way: brilcalc lumi -b "STABLE BEAMS" -u /pb -i Run2017x.json --hltpath xyz
    # new way:
    #          (https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2017Analysis)
    #          (https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM)
    # brilcalc lumi --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -u /pb -i Run2017x.json --hltpath xyz
    # below done with brilws version 3.3.0, pip version 9.0.1

    # --hltpath "HLT_PFMET120_PFMHT120_IDTight_v*"
    # note 2017B: several triggers hadn't been added yet, particularly HLT_MET105(120)_IsoTrk50, so B should be considered separately
    # see Triggers.py for details
    "MET_2017B" : 4793.367,
    "MET_2017C" : 9631.324,
    "MET_2017D" : 4247.707,
    "MET_2017E" : 9313.990,
    "MET_2017F" : 13498.143,

    # --hltpath "HLT_Ele35_WPTight_Gsf_v*"
    "SingleElectron_2017B" : 4793.983,
    "SingleElectron_2017C" : 9631.329,
    "SingleElectron_2017D" : 4247.817,
    "SingleElectron_2017E" : 9314.621,
    "SingleElectron_2017F" : 13539.633,

    # --hltpath "HLT_IsoMu27_v*"
    "SingleMuon_2017B" : 4793.983,
    "SingleMuon_2017C" : 9631.329,
    "SingleMuon_2017D" : 4247.817,
    "SingleMuon_2017E" : 9314.621,
    "SingleMuon_2017F" : 13539.633,

    # no hltpath
    "Tau_2017B" : 4793.988,
    "Tau_2017C" : 9632.855,
    "Tau_2017D" : 4247.817,
    "Tau_2017E" : 9314.621,
    "Tau_2017F" : 13539.905,

    # --hltpath "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"
    "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*" : {
        "Tau_2017B" : 4094.153,
        "Tau_2017C" : 498.846,
        "Tau_2017D" : 311.847,
        "Tau_2017E" : 391.614,
        "Tau_2017F" : 465.888,
    },

}

lumi_2017_ntuples = {
    # brilcalc on CRAB report JSONs with hltpath

    # --hltpath "HLT_PFMET120_PFMHT120_IDTight_v*"
    # note 2017B: several triggers hadn't been added yet, particularly HLT_MET105(120)_IsoTrk50, so B should be considered separately
    # see Triggers.py for details
    "MET_2017B" : 4793.367,
    "MET_2017C" : 9631.324,
    "MET_2017D" : 4247.707,
    "MET_2017E" : 9313.990,
    "MET_2017F" : 13498.143,

    # --hltpath "HLT_Ele35_WPTight_Gsf_v*"
    "SingleElectron_2017B" : 4710.308,
    "SingleElectron_2017C" : 9631.009,
    "SingleElectron_2017D" : 4247.706,
    "SingleElectron_2017E" : 9313.682,
    "SingleElectron_2017F" : 13538.950,
   
    # --hltpath "HLT_IsoMu27_v*"
    "SingleMuon_2017B" : 4793.980,
    "SingleMuon_2017C" : 9563.500,
    "SingleMuon_2017D" : 4247.706,
    "SingleMuon_2017E" : 9313.682,
    # FIX ME -- holdover from lumi_2017 above, need to use the ntuple crab reports
    "SingleMuon_2017F" : 13539.633,
 
    # no hltpath
    "Tau_2017B" : 4793.980,
    "Tau_2017C" : 9632.850,
    "Tau_2017D" : 4247.707,
    "Tau_2017E" : 9313.990,
    "Tau_2017F" : 13534.185,

    # --hltpath "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"
    "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*" : {
        "Tau_2017B" : 4094.150,
        "Tau_2017C" : 498.846,
        "Tau_2017D" : 311.834,
        "Tau_2017E" : 391.608,
        "Tau_2017F" : 465.854,
    },

}

lumi_2018_ntuples = {
    # brilcalc on CRAB report JSONs with hltpath
    # anything commented below is OLD, using the preliminary normtag on an older golden JSON

    # Normtag: https://twiki.cern.ch/twiki/bin/view/CMS/TWikiLUM, https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2018Analysis
    # brilcalc lumi --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_PHYSICS.json -u /pb -i [your json] --hltpath "xyz"

    # --hltpath "HLT_MET105_IsoTrk50_v*"
    # bril worksuite 3.5.2
    "MET_2018A" : 14024.176505487,
    "MET_2018B" : 7060.764380203,
    "MET_2018C" : 6894.782079681,
    "MET_2018D" : 31742.980644688,

    # --hltpath "HLT_Ele32_WPTight_Gsf_v*"
    "EGamma_2018A" : 14012.067987968,
    "EGamma_2018B" : 7060.617355256,
    "EGamma_2018C" : 6688.523784,
    "EGamma_2018D" : 30955.343627310,

    # --hltpath "HLT_IsoMu24_v*"
    "SingleMuon_2018A" : 13956.7120657598,
    "SingleMuon_2018B" : 7060.622497490,
    "SingleMuon_2018C" : 6894.770971269,
    "SingleMuon_2018D" : 31585.906779588,

    # no hltpath
    "Tau_2018A" : 14022.518202245,
    "Tau_2018B" : 7015.791118,
    "Tau_2018C" : 6873.907668,
    "Tau_2018D" : 31742.631527,

    # --hltpath "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"
    "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*" : {
        "Tau_2018A" : 73.802727380,
        "Tau_2018B" : 36.925216,
        "Tau_2018C" : 36.178461,
        "Tau_2018D" : 167.066482,
    }

}

lumi_2022_promptReco = {
#command used:
# brilcalc lumi --normtag /cvmfs/cms-bril.cern.ch/cms-lumi-pog/Normtags/normtag_BRIL.json -u /fb -i Cert_Collisions2022_eraD_357538_357900_Golden.json --hlt "HLT_PFMET105_IsoTrk50_*"

# using HLT_PFMET105_IsoTrk50_*
    "MET_2022A" : -1,
    "MET_2022B" : 89.078989610,
    "JetMET_2022C" : 5010.409016184,
    "JetMET_2022D" : 2970.045129108,
    "MET_2022E" : 5806.955207286,
    "MET_2022F" : 17781.598893382,
    "MET_2022G" : 3082.753035617,

# using HLT_IsoMu24_v* with Golden json files
    "Muon_2022A" : -1,
    "Muon_2022B" : 89.078989610,
    "Muon_2022C" : 5010.409016184, 
    "Muon_2022D" : 2970.045129108, 
    "Muon_2022E" : 5806.955207286,
    "Muon_2022F" : 17781.901464250,
    "Muon_2022G" : 3082.753035617,

# using HLT_Ele32_WPTight_Gsf_v*
    "EGamma_2022A" : -1,
    "EGamma_2022B" : 89.07898961,
    "EGamma_2022C" : 5010.409016,
    "EGamma_2022D" : 2970.045129,
    "EGamma_2022E" : 5806.955207,
    "EGamma_2022F" : 17781.59889, #fixme
    "EGamma_2022G" : 3082.753036, #fixme

# using HLT_IsoMu24_eta2p1_MediumDeepTauPFTauHPS20_eta2p1_SingleL1_v*
    "Tau_2022B" : -1,
    "Tau_2022C" : 5010.409016115, 
    "Tau_2022D" : 2970.045129109, 
    "Tau_2022E" : 5806.955207273, 
    "Tau_2022F" : 17781.901464330, 
    "Tau_2022G" : 3082.753035626
}

# now create a single lumi dict, starting with 2015
lumi = lumi_2015rereco

lumi = InsertYear(lumi_2016, lumi)
lumi = InsertYear(lumi_2017_ntuples, lumi)
lumi = InsertYear(lumi_2018_ntuples, lumi)
lumi = InsertYear(lumi_2022_promptReco, lumi)

# set up some composite aliases for convenience
lumi["MET_2016H"]                                         =  lumi["MET_2016H_v2"] + lumi["MET_2016H_v3"]
lumi["SingleElectron_2016H"]                              =  lumi["SingleElectron_2016H_v2"] + lumi["SingleElectron_2016H_v3"]
lumi["SingleMuon_2016H"]                                  =  lumi["SingleMuon_2016H_v2"] + lumi["SingleMuon_2016H_v3"]
lumi["Tau_2016H"]                                         =  lumi["Tau_2016H_v2"] + lumi["Tau_2016H_v3"]
lumi["ZeroBias_2016H"]                                    =  lumi["ZeroBias_2016H_v2"] + lumi["ZeroBias_2016H_v3"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H_v2"] + lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H_v3"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H_v2"] + lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H_v3"]

# Create all combinations including the years' totals
lumi = CreateCompositeLumis(lumi, '2015', 'D')
lumi = CreateCompositeLumis(lumi, '2016', 'BCDEFGH')
lumi = CreateCompositeLumis(lumi, '2017', 'BCDEF')
lumi = CreateCompositeLumis(lumi, '2018', 'ABCD')
