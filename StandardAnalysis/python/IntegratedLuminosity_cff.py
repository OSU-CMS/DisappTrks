# all luminosities should be in inverse picobarns

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

lumi_2017 = {

    # filterJSON.py --min x --max y Cert_294927-302654_13TeV_PromptReco_Collisions17_JSON.txt --output Run2017x.json
    # 2017B: 297031-299329
    # 2017C: 299368-302029
    # 2017D: 302031-302663
    # brilcalc lumi -b "STABLE BEAMS" -u /pb -i Run2017x.json --hltpath xyz

    # --hltpath "HLT_MET105_IsoTrk50_v*"
    # note: since MET105_IsoTrk50 came online only in run:fill 299368:5962, what should really happen here is
    #       there will be a period before it with some lumi and then a period with it included
    "MET_2017B" : 0.0,
    "MET_2017C" : 9556.386,
    "MET_2017D" : 3679.642,

    # --hltpath "HLT_IsoMu27_v*"
    "SingleMuon_2017B" : 4495.945,
    "SingleMuon_2017C" : 9556.385,
    "SingleMuon_2017D" : 3679.643,

    # --hltpath "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"
    "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*" : {
        "Tau_2017B" : 3811.717 ,
        "Tau_2017C" : 495.724,
        "Tau_2017D" : 266.845,
    },

}

# set 2016 to either the rereco or prompt values depending on usePrompt2016
lumi_2016 = lumi_2016Prompt if usePrompt2016 else lumi_23Sep2016

# now create a single lumi dict, starting with 2015
lumi = lumi_2015rereco

# add 2016
for k in lumi_2016.keys():
    # if not already present, just add this lumi entry
    if not k in lumi.keys():
        lumi[k] = lumi_2016[k]
    # if this is already present, we're on a prescaled path (a dict) and need to update rather than add/overwrite
    if k in lumi.keys() and isinstance(lumi[k], dict) and isinstance(lumi_2016[k], dict):
        mergedDict = {}
        mergedDict.update(lumi[k])
        mergedDict.update(lumi_2016[k])
        lumi[k] = mergedDict
    # if neither of those two cases, no idea what you're trying to do so skip it

# add 2017
for k in lumi_2017.keys():
    # if not already present, just add this lumi entry
    if not k in lumi.keys():
        lumi[k] = lumi_2017[k]
    # if this is already present, we're on a prescaled path (a dict) and need to update rather than add/overwrite
    if k in lumi.keys() and isinstance(lumi[k], dict) and isinstance(lumi_2017[k], dict):
        mergedDict = {}
        mergedDict.update(lumi[k])
        mergedDict.update(lumi_2017[k])
        lumi[k] = mergedDict
    # if neither of those two cases, no idea what you're trying to do so skip it

# set up some composite aliases for convenience
lumi["MET_2015"]                                         =  lumi["MET_2015D"]
lumi["SingleElectron_2015"]                              =  lumi["SingleElectron_2015D"]
lumi["SingleMuon_2015"]                                  =  lumi["SingleMuon_2015D"]
lumi["Tau_2015"]                                         =  lumi["Tau_2015D"]
lumi["ZeroBias_2015"]                                    =  lumi["ZeroBias_2015D"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2015"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2015D"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2015"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2015D"]

# 2016
lumi["MET_2016H"]                                         =  lumi["MET_2016H_v2"] + lumi["MET_2016H_v3"]
lumi["SingleElectron_2016H"]                              =  lumi["SingleElectron_2016H_v2"] + lumi["SingleElectron_2016H_v3"]
lumi["SingleMuon_2016H"]                                  =  lumi["SingleMuon_2016H_v2"] + lumi["SingleMuon_2016H_v3"]
lumi["Tau_2016H"]                                         =  lumi["Tau_2016H_v2"] + lumi["Tau_2016H_v3"]
lumi["ZeroBias_2016H"]                                    =  lumi["ZeroBias_2016H_v2"] + lumi["ZeroBias_2016H_v3"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H_v2"] + lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H_v3"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H_v2"] + lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H_v3"]

for period in {'BC', 'DEF', 'BCDEF', 'GH', 'DEFG', 'DEFGH', 'BCDEFGH'}:

    for pd in {'MET', 'SingleElectron', 'SingleMuon', 'Tau', 'ZeroBias'}:
        key = pd + '_2016' + period if period != 'BCDEFGH' else pd + '_2016'

        lumi[key] = 0.0
        for p in period:
            lumi[key] += lumi[pd + '_2016' + p]

    suffix = '_2016' + period if period != 'BCDEFGH' else '_2016'
    lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]['Tau' + suffix] = 0.0
    lumi["HLT_ZeroBias_v*"]['ZeroBias' + suffix] = 0.0
    for p in period:
        lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]['Tau' + suffix] += lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]['Tau_2016' + p]
        lumi["HLT_ZeroBias_v*"]['ZeroBias' + suffix] += lumi["HLT_ZeroBias_v*"]['ZeroBias_2016' + p]

# 2017
for period in {'BCD'}:

    for pd in {'MET', 'SingleMuon'}:
        key = pd + '_2017' + period if period != 'BCD' else pd + '_2017'

        lumi[key] = 0.0
        for p in period:
            lumi[key] += lumi[pd + '_2017' + p]

    suffix = '_2017' + period if period != 'BCD' else '_2017'
    lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]['Tau' + suffix]  = lumi["HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*"]['Tau_2017' + p]
