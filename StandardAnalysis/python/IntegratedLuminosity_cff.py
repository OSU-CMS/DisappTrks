# all luminosities should be in inverse picobarns

lumi = {
    # luminosities for the 23Sep2016 rereco are commented out for now

    "MET_2015D" : 2672.144,
    "MET_2016B" : 5884.944,
    "MET_2016C" : 2645.968,
    "MET_2016D" : 4350.209,
    "MET_2016E" : 4043.113,
    "MET_2016F" : 3152.673,
    # NOTE: temporary fix with an impartial re-creation of G
    "MET_2016G" : 6685.201,

    #"MET_2016E" : 4049.255,
    #"MET_2016F" : 3160.088,
    #"MET_2016G" : 7554.454,
    #"MET_2016H" : 8761.822,

    "SingleElectron_2015D" : 2669.639,
    "SingleElectron_2016B" : 5883.947,
    "SingleElectron_2016C" : 2645.968,
    "SingleElectron_2016D" : 4352.417,
    "SingleElectron_2016E" : 4049.732,
    "SingleElectron_2016F" : 3148.581,
    "SingleElectron_2016G" : 7108.192,

    "SingleMuon_2015D" : 2669.752,
    "SingleMuon_2016B" : 5874.068,
    "SingleMuon_2016C" : 2628.835,
    "SingleMuon_2016D" : 4353.449,
    "SingleMuon_2016E" : 4049.732,
    "SingleMuon_2016F" : 3150.361,
    "SingleMuon_2016G" : 7115.969,

    #"SingleMuon_2016E" : 4049.732,
    #"SingleMuon_2016F" : 3160.088,
    #"SingleMuon_2016G" : 7553.249,
    #"SingleMuon_2016H" : 8761.822,

    "Tau_2015D" : 2672.153,
    "Tau_2016B" : 5880.362,
    "Tau_2016C" : 2645.968,
    "Tau_2016D" : 4353.449,
    "Tau_2016E" : 4034.766,
    "Tau_2016F" : 3157.974,
    "Tau_2016G" : 7115.969,

    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v*" : {
        "Tau_2015D" : 225.172,
        "Tau_2016B" : 729.733,
        "Tau_2016C" : 83.745,
        "Tau_2016D" : 138.891,
        "Tau_2016E" : 116.665,
        "Tau_2016F" : 66.607,
        "Tau_2016G" : 104.906,
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

lumi["MET_2016DEFG"]                                         =  lumi["MET_2016D"]                                         +  lumi["MET_2016E"]                                         +  lumi["MET_2016F"]                                         +  lumi["MET_2016G"]
lumi["SingleElectron_2016DEFG"]                              =  lumi["SingleElectron_2016D"]                              +  lumi["SingleElectron_2016E"]                              +  lumi["SingleElectron_2016F"]                              +  lumi["SingleElectron_2016G"]
lumi["SingleMuon_2016DEFG"]                                  =  lumi["SingleMuon_2016D"]                                  +  lumi["SingleMuon_2016E"]                                  +  lumi["SingleMuon_2016F"]                                  +  lumi["SingleMuon_2016G"]
lumi["Tau_2016DEFG"]                                         =  lumi["Tau_2016D"]                                         +  lumi["Tau_2016E"]                                         +  lumi["Tau_2016F"]                                         +  lumi["Tau_2016G"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFG"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016D"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016E"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016F"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016G"]

lumi["MET_2016"]                                         =  lumi["MET_2016BC"]                                         +  lumi["MET_2016DEFG"]
lumi["SingleElectron_2016"]                              =  lumi["SingleElectron_2016BC"]                              +  lumi["SingleElectron_2016DEFG"]
lumi["SingleMuon_2016"]                                  =  lumi["SingleMuon_2016BC"]                                  +  lumi["SingleMuon_2016DEFG"]
lumi["Tau_2016"]                                         =  lumi["Tau_2016BC"]                                         +  lumi["Tau_2016DEFG"]
lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016"]  =  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016BC"]  +  lumi["HLT_LooseIsoPFTau50_Trk30_eta2p1_v*"]["Tau_2016DEFG"]
