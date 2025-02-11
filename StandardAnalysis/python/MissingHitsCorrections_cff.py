MissingHitsCorrections = {}

MissingHitsCorrections["uncorrected"] = {
    "dropTOBProbability"          :  0.0,
    "preTOBDropHitInefficiency"   :  0.0,
    "postTOBDropHitInefficiency"  :  0.0,
    "hitInefficiency"             :  0.0,
}

MissingHitsCorrections["2015"] = {
    "dropTOBProbability"          :  0.00830971251971,
    "preTOBDropHitInefficiency"   :  0.00515089150972,
    "postTOBDropHitInefficiency"  :  0.27336245212,
    "hitInefficiency"             :  0.0175874821487,
}

MissingHitsCorrections["2016BC"] = {
    "dropTOBProbability"          :  0.0392897956267,
    "preTOBDropHitInefficiency"   :  0.00655833662008,
    "postTOBDropHitInefficiency"  :  0.250983800618,
    "hitInefficiency"             :  0.0392360890179,
}

MissingHitsCorrections["2016DEFGH"] = {
    "dropTOBProbability"          :  0.0249299435201,
    "preTOBDropHitInefficiency"   :  0.00456902326717,
    "postTOBDropHitInefficiency"  :  0.276546736966,
    "hitInefficiency"             :  0.0295033379988,
}

MissingHitsCorrections["2017"] = {
    "dropTOBProbability"          :  0.001453, # PRE_TOB Y()
    "preTOBDropHitInefficiency"   :  0.004991, # PRE_TOB X()
    "postTOBDropHitInefficiency"  :  0.383416, # POST_TOB X()
    "hitInefficiency"             :  0.0, # middle X() -- really 0.999982 (nonsense) so do not apply a correction
}

MissingHitsCorrections["2018"] = {
    "dropTOBProbability"          :  0.0013400719, # PRE_TOB Y()
    "preTOBDropHitInefficiency"   :  0.0022805645, # PRE_TOB X()
    "postTOBDropHitInefficiency"  :  0.40748793, # POST_TOB X()
    "hitInefficiency"             :  0.0055474375, # middle X()
}

MissingHitsCorrections["2022EFG"] = {
    "dropTOBProbability"          :  0.0007151755, # PRE_TOB Y()
    "preTOBDropHitInefficiency"   :  0.0037699605, # PRE_TOB X()
    "postTOBDropHitInefficiency"  :  0.6114408725, # POST_TOB X()
    "hitInefficiency"             :  0.0055455684, # middle X()
}
