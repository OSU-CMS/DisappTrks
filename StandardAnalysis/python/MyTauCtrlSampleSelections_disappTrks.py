import FWCore.ParameterSet.Config as cms
import copy

###########################################################
##### Set up the event selections (channels) #####
###########################################################

##### List of valid input collections #####   
# jets, muons, electrons, taus, photons, mets,
# events, tracks, primaryvertexs,
# genjets, mcparticles,
# bxlumis, superclusters

# Selection of control samples
#trigger on mus for all of them 
triggersSingleMu = cms.vstring(
    "HLT_IsoMu24_v",
##         "HLT_Mu12_eta2p1_DiCentral_20_v",
##             "HLT_Mu12_eta2p1_DiCentral_40_20_v",
##             "HLT_Mu12_v",
##             "HLT_Mu13_Mu8_NoDZ_v",
##             "HLT_Mu13_Mu8_v",
##             "HLT_Mu15_eta2p1_DiCentral_20_v",
##             "HLT_Mu15_eta2p1_DiCentral_40_20_v",
##             "HLT_Mu15_eta2p1_L1ETM20_v",
##             "HLT_Mu15_eta2p1_L1Mu10erJetC12WdEtaPhi1DiJetsC_v",
##             "HLT_Mu15_eta2p1_v",
##             "HLT_Mu17_Ele8_CaloIdT_CaloIsoVL_TrkIdVL_TrkIsoVL_v",
##             "HLT_Mu17_Mu8_v",
##             "HLT_Mu17_eta2p1_TriCentralPFNoPUJet45_35_25_v",
##             "HLT_Mu17_v",
##             "HLT_Mu18_CentralPFJet30_CentralPFJet25_v",
##             "HLT_Mu18_PFJet30_PFJet25_Deta3_CentralPFJet25_v",
##             "HLT_Mu22_Photon22_CaloIdL_v",
##             "HLT_Mu24_eta2p1_v",
##             "HLT_Mu24_v",
##             "HLT_Mu30_eta2p1_v",
##             "HLT_Mu30_v",
##             "HLT_Mu40_PFNoPUHT350_v",
##             "HLT_Mu40_eta2p1_v",
##             "HLT_Mu40_v",
##             "HLT_Mu50_eta2p1_v",
##             "HLT_Mu5_v",
##             "HLT_Mu60_PFNoPUHT350_v",
##            "HLT_Mu8_v",
            )
ZtoTauTau = cms.PSet(
    name = cms.string("ZtoTauTau"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = cms.VPSet (
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("pT > 20 GeV")
                            ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("|eta| < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("leadingTrackValidHits > 4"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("Valid Hits > 4")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("numProngs == 1"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("2 1-prong tau")
                    ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("numSignalGammas == 0"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("Sig Gammas = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("numSignalNeutrals == 0"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("Sig Neutrals = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("numSignalPiZeros == 0"),
        numberRequired = cms.string(">= 2"),
        alias = cms.string("Sig Pi0 = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("tau-tau pairs"),
        cutString = cms.string("invMass > 40 & invMass < 160"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("40 < InvMass(T+T) < 160")
        ),
    )  # end cuts = cms.VPSet (
    ) # end ZtoEE = cms.PSet(         

ZtoMuTau = cms.PSet(
    name = cms.string("ZtoMuTau"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("abs(eta) < 2.1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("(T) |eta| < 2.1")
            ),
        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("pt > 20"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("(T) pT > 20 GeV")
            ),
        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("numProngs == 1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("1 1-prong tau")
                                ),
        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("numSignalGammas == 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Sig Gamma = 0")
            ),
        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("numSignalNeutrals == 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Sig Neutral = 0")
            ),
        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("numSignalPiZeros == 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Sig Pi0 = 0")
            ),
        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("HPSagainstElectronTight == 1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("againstElectronTight")
            ),
        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("HPSagainstMuonLoose == 1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("againstMuonLoose")
            ),

        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("HPSagainstMuonTight == 1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("againstMuonTight")
            ),

        cms.PSet (
            inputCollection = cms.string("taus"),
            cutString = cms.string("leadingTrackValidHits > 4"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("(T) Valid Hits > 4")
            ),
        
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("abs(eta) < 2.1"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("(m) |eta| < 2.1")
            ),
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("pt > 20"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("(m) pT > 20 GeV")
            ),
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("tkNumValidHits > 4"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("(m) Valid Hits > 4")
            ),
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("tightID > 0"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("MuonTightID")
            ),
        cms.PSet (
            inputCollection = cms.string("muons"),
            cutString = cms.string("relPFdBetaIso < 0.12"),
            numberRequired = cms.string(">= 1"),
            alias = cms.string("Muon Iso")
            ),
        
            )
            )

ElectronVetoAll =   cms.PSet (
        inputCollection = cms.string("electrons"),
        cutString = cms.string("pt > -1"),
        numberRequired = cms.string("= 0"),  # Require no electron in event.
        alias = cms.string("Electrons = 0")
        )
MuonVetoOneMax =   cms.PSet (
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 1"),  # Require no more than one muon in event
            alias = cms.string("Muons = 1")
    )

deadEcalVeto =  cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isMatchedDeadEcal == 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("deadEcal Veto")
        )

crackVeto =    cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("Crack Veto")
    )

cutMuTauInvMass = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("40 < InvMass(m+T) < 160")
    )
deltaRTauTrack = cms.PSet(
    inputCollection = cms.string("tau-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("deltaRTauTrack < 0.15")
    )
deltaRMuTrack = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR > 0.15"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("deltaRMuTrack > 0.15")
    )
muonInvMass = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("metMT < 50"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("muonMETMT < 50 GeV")
    )

ZtoMuTau.cuts.append(MuonVetoOneMax)
ZtoMuTau.cuts.append(deltaRTauTrack)
ZtoMuTau.cuts.append(deltaRMuTrack)
ZtoMuTau.cuts.append(muonInvMass)
ZtoMuTau.cuts.append(cutMuTauInvMass)




ZtoTauTrack = cms.PSet(
    name = cms.string("ZtoTauTrack"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = cms.VPSet(
    cms.PSet(
        inputCollection = cms.string("taus"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("(T) pT > 20 GeV")
        ),
    cms.PSet(
        inputCollection= cms.string("taus"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(T) |eta| < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("numProngs == 1"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("1 1-prong tau")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("numSignalGammas == 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Sig Gamma = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("numSignalNeutrals == 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Sig Neutral = 0")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("numSignalPiZeros == 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Sig Pi0 = 0")
        ),

    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("HPSagainstElectronTight == 1"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("againstElectronTight")
        ),

    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("HPSagainstMuonLoose == 1"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("againstMuonLoose")
        ),
    cms.PSet (
        inputCollection = cms.string("taus"),
        cutString = cms.string("HPSagainstMuonTight == 1"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("againstMuonTight")
        ),
    
                
    cms.PSet(
        inputCollection= cms.string("taus"),
        cutString = cms.string("leadingTrackValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(T) Valid Hits > 4")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("abs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("(m) |eta| < 2.1")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("(m) pT > 20 GeV")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tkNumValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("(m) Valid Hits > 4")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("tightID > 0"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("MuonTightID")
        ),
    cms.PSet (
        inputCollection = cms.string("muons"),
        cutString = cms.string("relPFdBetaIso < 0.12"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Muon Iso")
        ),
    
    cms.PSet(
        inputCollection = cms.string("tracks"),
        cutString = cms.string("pt > 20"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("(t) pT > 20 GeV")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(eta) < 2.1"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) |eta| < 2.1")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(d0wrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) |d0| < 0.01 cm")
        ),
    cms.PSet(
        inputCollection= cms.string("tracks"),
        cutString = cms.string("fabs(dZwrtPV) < 0.01"),
        numberRequired = cms.string(">= 1"),
        alias =cms.string("(t) |dZ| < 0.01 cm")
        ),
    cms.PSet(
         inputCollection= cms.string("tracks"),
         cutString = cms.string("numValidHits > 4"),
         numberRequired = cms.string(">= 1"),
         alias =cms.string("(t) Valid Hits > 4")
         ),
 ##    cms.PSet (
##         inputCollection = cms.string("tracks"),
##         cutString = cms.string("nHitsMissingMiddle == 0"),
##         numberRequired = cms.string(">= 1"),
##         alias = cms.string("Missing Middle Hits = 0")
##         ),
##     cms.PSet (
##         inputCollection = cms.string("tracks"),
##         cutString = cms.string("nHitsMissingInner == 0"),
##         numberRequired = cms.string(">= 1"),
##         alias = cms.string("Missing Inner Hits = 0")
##        ),
    cms.PSet (
        inputCollection = cms.string("tracks"),
        cutString = cms.string("isIso == 1"),
        numberRequired = cms.string(">= 1"),
        alias = cms.string("Track Isolation")
        ),
    )
    )

ZtoTauTrackPreSel = cms.PSet(
    name = cms.string("ZtoTauTrackPreSel"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = copy.deepcopy(ZtoTauTrack.cuts)
    )
cutMuTauInvMass = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    alias = cms.string("40 < invMass(T+m) < 160")
    )
ZtoTauTrackPreSel.cuts.append(MuonVetoOneMax)
ZtoTauTrackPreSel.cuts.append(deltaRTauTrack)
ZtoTauTrackPreSel.cuts.append(cutMuTauInvMass)

ZtoTauTrackFullPreSel = cms.PSet(
    name = cms.string("ZtoTauTrackFullPreSel"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = copy.deepcopy(ZtoTauTrack.cuts)
    )

ZtoTauTrackFullPreSel.cuts.append(ElectronVetoAll)
ZtoTauTrackFullPreSel.cuts.append(MuonVetoOneMax)
ZtoTauTrackFullPreSel.cuts.append(deadEcalVeto)
ZtoTauTrackFullPreSel.cuts.append(crackVeto)
ZtoTauTrackFullPreSel.cuts.append(deltaRTauTrack)
ZtoTauTrackFullPreSel.cuts.append(deltaRMuTrack)
ZtoTauTrackFullPreSel.cuts.append(muonInvMass)
ZtoTauTrackFullPreSel.cuts.append(cutMuTauInvMass)
