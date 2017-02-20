# all luminosities should be in inverse picobarns

lumi = {

    "MET_2015D"     :  2672.144,
    "MET_2016B"     :  5933.309,
    "MET_2016C"     :  2645.968,
    "MET_2016D"     :  4353.449,
    "MET_2016E"     :  4049.255,
    "MET_2016F"     :  3160.088,
    "MET_2016G"     :  7554.454,
    "MET_2016H_v2"  :  8635.591,
    "MET_2016H_v3"  :  221.442,

    #"MET_2016F"     :  3096.281,
    #"MET_2016G"     :  7525.901,

    "SingleElectron_2015D"     :  2669.639,
    "SingleElectron_2016B"     :  5933.313,
    "SingleElectron_2016C"     :  2645.968,
    "SingleElectron_2016D"     :  4353.449,
    "SingleElectron_2016E"     :  4117.098,
    "SingleElectron_2016F"     :  3185.972,
    "SingleElectron_2016G"     :  7721.057,
    "SingleElectron_2016H_v2"  :  8635.321,
    "SingleElectron_2016H_v3"  :  221.442,

    "SingleMuon_2015D"     :  2669.752,
    "SingleMuon_2016B"     :  5929.002,
    "SingleMuon_2016C"     :  2645.968,
    "SingleMuon_2016D"     :  4350.505,
    "SingleMuon_2016E"     :  4117.098,
    "SingleMuon_2016F"     :  3185.972,
    "SingleMuon_2016G"     :  7721.368,
    "SingleMuon_2016H_v2"  :  8635.591,
    "SingleMuon_2016H_v3"  :  221.442,

    #"SingleMuon_2016C"     :  2573.399,

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
        "Tau_2016B"     :  740.713,
        "Tau_2016C"     :  0.128,
        "Tau_2016D"     :  138.891,
        "Tau_2016E"     :  117.140,
        "Tau_2016F"     :  66.659,
        "Tau_2016G"     :  114.196,
        "Tau_2016H_v2"  :  119.675,
        "Tau_2016H_v3"  :  3.182,
    },
}

# set up some composite aliases for convenience

lumi["MET_2015"]                                         =  lumi["MET_2015D"]
lumi["SingleElectron_2015"]                              =  lumi["SingleElectron_2015D"]
lumi["SingleMuon_2015"]                                  =  lumi["SingleMuon_2015D"]
lumi["Tau_2015"]                                         =  lumi["Tau_2015D"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2015"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2015D"]

lumi["MET_2016BC"]                                         =  lumi["MET_2016B"]                                         +  lumi["MET_2016C"]
lumi["SingleElectron_2016BC"]                              =  lumi["SingleElectron_2016B"]                              +  lumi["SingleElectron_2016C"]
lumi["SingleMuon_2016BC"]                                  =  lumi["SingleMuon_2016B"]                                  +  lumi["SingleMuon_2016C"]
lumi["Tau_2016BC"]                                         =  lumi["Tau_2016B"]                                         +  lumi["Tau_2016C"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016B"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016C"]

lumi["MET_2016H"]                                         =  lumi["MET_2016H_v2"]                                         +  lumi["MET_2016H_v3"]
lumi["SingleElectron_2016H"]                              =  lumi["SingleElectron_2016H_v2"]                              +  lumi["SingleElectron_2016H_v3"]
lumi["SingleMuon_2016H"]                                  =  lumi["SingleMuon_2016H_v2"]                                  +  lumi["SingleMuon_2016H_v3"]
lumi["Tau_2016H"]                                         =  lumi["Tau_2016H_v2"]                                         +  lumi["Tau_2016H_v3"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H_v2"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H_v3"]

lumi["MET_2016DEFGH"]                                         =  lumi["MET_2016D"]                                         +  lumi["MET_2016E"]                                         +  lumi["MET_2016F"]                                         +  lumi["MET_2016G"]                                         +  lumi["MET_2016H"]
lumi["SingleElectron_2016DEFGH"]                              =  lumi["SingleElectron_2016D"]                              +  lumi["SingleElectron_2016E"]                              +  lumi["SingleElectron_2016F"]                              +  lumi["SingleElectron_2016G"]                              +  lumi["SingleElectron_2016H"]
lumi["SingleMuon_2016DEFGH"]                                  =  lumi["SingleMuon_2016D"]                                  +  lumi["SingleMuon_2016E"]                                  +  lumi["SingleMuon_2016F"]                                  +  lumi["SingleMuon_2016G"]                                  +  lumi["SingleMuon_2016H"]
lumi["Tau_2016DEFGH"]                                         =  lumi["Tau_2016D"]                                         +  lumi["Tau_2016E"]                                         +  lumi["Tau_2016F"]                                         +  lumi["Tau_2016G"]                                         +  lumi["Tau_2016H"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFGH"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016D"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016E"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016F"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016G"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016H"]

lumi["MET_2016"]                                         =  lumi["MET_2016BC"]                                         +  lumi["MET_2016DEFGH"]
lumi["SingleElectron_2016"]                              =  lumi["SingleElectron_2016BC"]                              +  lumi["SingleElectron_2016DEFGH"]
lumi["SingleMuon_2016"]                                  =  lumi["SingleMuon_2016BC"]                                  +  lumi["SingleMuon_2016DEFGH"]
lumi["Tau_2016"]                                         =  lumi["Tau_2016BC"]                                         +  lumi["Tau_2016DEFGH"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFGH"]
