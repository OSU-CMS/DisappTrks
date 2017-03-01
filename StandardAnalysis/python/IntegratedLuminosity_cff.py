# all luminosities should be in inverse picobarns

lumi = {

    "MET_2015D"     :  2672.144,
    "MET_2016B"     :  5738.925,
    "MET_2016C"     :  2573.399,
    "MET_2016D"     :  4248.384,
    "MET_2016E"     :  4008.663,
    "MET_2016F"     :  3096.281,
    "MET_2016G"     :  7525.901,
    "MET_2016H_v2"  :  8390.54,
    "MET_2016H_v3"  :  215.149,

    #"MET_2016C"     :  2573.399,
    #"MET_2016F"     :  3096.281,
    #"MET_2016G"     :  7525.901,

    "SingleElectron_2015D"     :  2669.639,
    "SingleElectron_2016B"     :  5678.099,
    "SingleElectron_2016C"     :  2357.325,
    "SingleElectron_2016D"     :  3942.136,
    "SingleElectron_2016E"     :  2924.728,
    "SingleElectron_2016F"     :  1888.193,
    "SingleElectron_2016G"     :  4053.038,
    "SingleElectron_2016H_v2"  :  8390.278,
    "SingleElectron_2016H_v3"  :  215.149,

    "SingleMuon_2015D"     :  2669.752,
    "SingleMuon_2016B"     :  5735.866,
    "SingleMuon_2016C"     :  2573.399,
    "SingleMuon_2016D"     :  4248.384,
    "SingleMuon_2016E"     :  3620.690,
    "SingleMuon_2016F"     :  2472.509,
    "SingleMuon_2016G"     :  4870.182,
    "SingleMuon_2016H_v2"  :  8390.540,
    "SingleMuon_2016H_v3"  :  215.149,

    #"SingleMuon_2016C"     :  2573.399,
    #"SingleMuon_2016G"     :  7540.488,

    "Tau_2015D"     :  2672.153,
    "Tau_2016B"     :  5933.309,
    "Tau_2016C"     :  3.425,
    "Tau_2016D"     :  4353.449,
    "Tau_2016E"     :  4049.255,
    "Tau_2016F"     :  3160.088,
    "Tau_2016G"     :  7552.514,
    "Tau_2016H_v2"  :  8635.591,
    "Tau_2016H_v3"  :  221.442,

    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v*" : {
        "Tau_2015D"     :  225.172,
        "Tau_2016B"     :  712.32,
        "Tau_2016C"     :  81.448,
        "Tau_2016D"     :  135.498,
        "Tau_2016E"     :  116.127,
        "Tau_2016F"     :  66.043,
        "Tau_2016G"     :  114.391,
        "Tau_2016H_v2"  :  116.278,
        "Tau_2016H_v3"  :  3.092,
    },

    "ZeroBias_2015D"     :  0.0,
    "ZeroBias_2016B"     :  0.0,
    "ZeroBias_2016C"     :  2573.399,
    "ZeroBias_2016D"     :  4248.383,
    "ZeroBias_2016E"     :  4009.130,
    "ZeroBias_2016F"     :  0.0,
    "ZeroBias_2016G"     :  0.0,
    "ZeroBias_2016H_v2"  :  8390.540,
    "ZeroBias_2016H_v3"  :  215.149,

    "HLT_ZeroBias_v*" : {
        "ZeroBias_2015D"     :  0.0,
        "ZeroBias_2016B"     :  0.0,
        "ZeroBias_2016C"     :  0.001267369,
        "ZeroBias_2016D"     :  0.001898671,
        "ZeroBias_2016E"     :  0.00301127,
        "ZeroBias_2016F"     :  0.0,
        "ZeroBias_2016G"     :  0.0,
        "ZeroBias_2016H_v2"  :  0.005520328,
        "ZeroBias_2016H_v3"  :  0.000180316,
    },
}

# set up some composite aliases for convenience

lumi["MET_2015"]                                         =  lumi["MET_2015D"]
lumi["SingleElectron_2015"]                              =  lumi["SingleElectron_2015D"]
lumi["SingleMuon_2015"]                                  =  lumi["SingleMuon_2015D"]
lumi["Tau_2015"]                                         =  lumi["Tau_2015D"]
lumi["ZeroBias_2015"]                                    =  lumi["ZeroBias_2015D"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2015"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2015D"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2015"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2015D"]

lumi["MET_2016BC"]                                         =  lumi["MET_2016B"]                                         +  lumi["MET_2016C"]
lumi["SingleElectron_2016BC"]                              =  lumi["SingleElectron_2016B"]                              +  lumi["SingleElectron_2016C"]
lumi["SingleMuon_2016BC"]                                  =  lumi["SingleMuon_2016B"]                                  +  lumi["SingleMuon_2016C"]
lumi["Tau_2016BC"]                                         =  lumi["Tau_2016B"]                                         +  lumi["Tau_2016C"]
lumi["ZeroBias_2016BC"]                                    =  lumi["ZeroBias_2016B"]                                    +  lumi["ZeroBias_2016C"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016B"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016C"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2016BC"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016B"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016C"]

lumi["MET_2016DEF"]                                         =  lumi["MET_2016D"]                                         +  lumi["MET_2016E"]                                         +  lumi["MET_2016F"]
lumi["SingleElectron_2016DEF"]                              =  lumi["SingleElectron_2016D"]                              +  lumi["SingleElectron_2016E"]                              +  lumi["SingleElectron_2016F"]
lumi["SingleMuon_2016DEF"]                                  =  lumi["SingleMuon_2016D"]                                  +  lumi["SingleMuon_2016E"]                                  +  lumi["SingleMuon_2016F"]
lumi["Tau_2016DEF"]                                         =  lumi["Tau_2016D"]                                         +  lumi["Tau_2016E"]                                         +  lumi["Tau_2016F"]
lumi["ZeroBias_2016DEF"]                                    =  lumi["ZeroBias_2016D"]                                    +  lumi["ZeroBias_2016E"]                                    +  lumi["ZeroBias_2016F"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEF"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016D"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016E"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016F"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2016DEF"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016D"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016E"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016F"]

lumi["MET_2016H"]                                         =  lumi["MET_2016H_v2"]                                         +  lumi["MET_2016H_v3"]
lumi["SingleElectron_2016H"]                              =  lumi["SingleElectron_2016H_v2"]                              +  lumi["SingleElectron_2016H_v3"]
lumi["SingleMuon_2016H"]                                  =  lumi["SingleMuon_2016H_v2"]                                  +  lumi["SingleMuon_2016H_v3"]
lumi["Tau_2016H"]                                         =  lumi["Tau_2016H_v2"]                                         +  lumi["Tau_2016H_v3"]
lumi["ZeroBias_2016H"]                                    =  lumi["ZeroBias_2016H_v2"]                                    +  lumi["ZeroBias_2016H_v3"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H_v2"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H_v3"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H_v2"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H_v3"]

lumi["MET_2016GH"]                                         =  lumi["MET_2016G"]                                         +  lumi["MET_2016H"]
lumi["SingleElectron_2016GH"]                              =  lumi["SingleElectron_2016G"]                              +  lumi["SingleElectron_2016H"]
lumi["SingleMuon_2016GH"]                                  =  lumi["SingleMuon_2016G"]                                  +  lumi["SingleMuon_2016H"]
lumi["Tau_2016GH"]                                         =  lumi["Tau_2016G"]                                         +  lumi["Tau_2016H"]
lumi["ZeroBias_2016GH"]                                    =  lumi["ZeroBias_2016G"]                                    +  lumi["ZeroBias_2016H"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016GH"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016G"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2016GH"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016G"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H"]

lumi["MET_2016DEFGH"]                                         =  lumi["MET_2016D"]                                         +  lumi["MET_2016E"]                                         +  lumi["MET_2016F"]                                         +  lumi["MET_2016G"]                                         +  lumi["MET_2016H"]
lumi["SingleElectron_2016DEFGH"]                              =  lumi["SingleElectron_2016D"]                              +  lumi["SingleElectron_2016E"]                              +  lumi["SingleElectron_2016F"]                              +  lumi["SingleElectron_2016G"]                              +  lumi["SingleElectron_2016H"]
lumi["SingleMuon_2016DEFGH"]                                  =  lumi["SingleMuon_2016D"]                                  +  lumi["SingleMuon_2016E"]                                  +  lumi["SingleMuon_2016F"]                                  +  lumi["SingleMuon_2016G"]                                  +  lumi["SingleMuon_2016H"]
lumi["Tau_2016DEFGH"]                                         =  lumi["Tau_2016D"]                                         +  lumi["Tau_2016E"]                                         +  lumi["Tau_2016F"]                                         +  lumi["Tau_2016G"]                                         +  lumi["Tau_2016H"]
lumi["ZeroBias_2016DEFGH"]                                    =  lumi["ZeroBias_2016D"]                                    +  lumi["ZeroBias_2016E"]                                    +  lumi["ZeroBias_2016F"]                                    +  lumi["ZeroBias_2016G"]                                    +  lumi["ZeroBias_2016H"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFGH"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016D"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016E"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016F"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016G"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2016DEFGH"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016D"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016E"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016F"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016G"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016H"]

lumi["MET_2016"]                                         =  lumi["MET_2016BC"]                                         +  lumi["MET_2016DEFGH"]
lumi["SingleElectron_2016"]                              =  lumi["SingleElectron_2016BC"]                              +  lumi["SingleElectron_2016DEFGH"]
lumi["SingleMuon_2016"]                                  =  lumi["SingleMuon_2016BC"]                                  +  lumi["SingleMuon_2016DEFGH"]
lumi["Tau_2016"]                                         =  lumi["Tau_2016BC"]                                         +  lumi["Tau_2016DEFGH"]
lumi["ZeroBias_2016"]                                    =  lumi["ZeroBias_2016BC"]                                    +  lumi["ZeroBias_2016DEFGH"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFGH"]
lumi["HLT_ZeroBias_v*"]["ZeroBias_2016"]                 =  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016BC"]                 +  lumi["HLT_ZeroBias_v*"]["ZeroBias_2016DEFGH"]
