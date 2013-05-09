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
    )

## List of cuts ##
tauPairPt = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 2"),
    )
tauPairEta = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 2"),
    )
tauPairValidHits = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("leadingTrackValidHits > 4"),
    numberRequired = cms.string(">= 2"),
    )
tauPairNumProng = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numProngs == 1"),
    numberRequired = cms.string(">= 2"),
    )
tauPairNumSigGamma = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalGammas == 0"),
    numberRequired = cms.string(">= 2"),
    )
tauPairNumSigNeutral = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalNeutrals == 0"),
    numberRequired = cms.string(">= 2"),
    )
tauPairNumPi0 = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalPiZeros == 0"),
    numberRequired = cms.string(">= 2"),
    )
tauPairInvMass = cms.PSet(
    inputCollection = cms.string("tau-tau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    )

electronVetoAll = cms.PSet(
    inputCollection = cms.string("electrons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("= 0"),  # Require no electron in event.
    #alias = cms.string("Electrons = 0")
    )
muonVetoOneMax = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > -1"),
    numberRequired = cms.string("<= 1"), 
    #alias = cms.string("Muons = 1")
            )

deadEcalVeto = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isMatchedDeadEcal == 0"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("deadEcal Veto")
    )
crackVeto = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 1.42 | fabs(eta) > 1.65"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("Crack Veto")
    )

muTauInvMass = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("40 < Muon-Tau InvMass < 160")
    )
muTauCharge = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("Muon-Tau ChargeProduct = -1")
    )
muTauInvMass = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("40 < Muon-Tau InvMass < 160")
    )
muTauCharge = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("chargeProduct == -1"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("Muon-Tau ChargeProduct = -1")
    )
deltaRTauTrack = cms.PSet(
    inputCollection = cms.string("tau-track pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("deltaR (Tau-Track) < 0.15")
    )
deltaRMuTrack = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    cutString = cms.string("deltaR > 0.15"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("deltaR (Mu-Track) > 0.15")
    )
deltaRMuTau = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("deltaR < 0.15"),
    numberRequired = cms.string(">= 1"),
    )
muonInvMass = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("metMT < 40"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("(mu) metMT < 40 GeV")
    )
muonPt = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )

muonEta = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )

muonValidHits = cms.PSet(
        inputCollection = cms.string("muons"),
        cutString = cms.string("tkNumValidHits > 4"),
        numberRequired = cms.string(">= 1"),
        )
muonTightId = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("tightID > 0"),
    numberRequired = cms.string(">= 1"),
    )
muonIso = cms.PSet(
    inputCollection = cms.string("muons"),
    cutString = cms.string("relPFdBetaIso < 0.12"),
    numberRequired = cms.string(">= 1"),
    )
tauPt = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
tauPt = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    )
tauEta = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string(" fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    )
tauNumProng = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numProngs == 1"),
    numberRequired = cms.string(">= 1"),
    )
tauNumSigGamma = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalGammas == 0"),
    numberRequired = cms.string(">= 1"),
    )
tauNumSigNeutral = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalNeutrals == 0"),
    numberRequired = cms.string(">= 1"),
    )
tauNumSigPi0 = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("numSignalPiZeros == 0"),
    numberRequired = cms.string(">= 1"),
    )
tauAgainstElectron = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstElectronTight == 1"),
    numberRequired = cms.string(">= 1"),
    )
tauAgainstMuon = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("HPSagainstMuonTight == 1"),
    numberRequired = cms.string(">= 1"),
    )
tauValidHits = cms.PSet(
    inputCollection = cms.string("taus"),
    cutString = cms.string("leadingTrackValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    )

trackPt = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("pt > 20"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$p_{T}$ > 20 GeV")
    )
trackEta = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(eta) < 2.1"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$|eta|$ < 2.1 ")
    )
trackd0 = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(d0wrtPV) < 0.01"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$|d_{0}|$ < 0.01 cm ")
    )

trackdz = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("fabs(dZwrtPV) < 0.01"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("$|d_{z}|$ < 0.01 cm ")
    )
trackNumValidHits = cms.PSet (
    inputCollection = cms.string("tracks"),
    cutString = cms.string("numValidHits > 4"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Valid Hits > 4 ")
    )
trkIso = cms.PSet(
    inputCollection = cms.string("tracks"),
    cutString = cms.string("isIso == 1"),
    numberRequired = cms.string(">= 1"),
    # alias = cms.string("Track Isolation")
    )

muTauInvMass = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    cutString = cms.string("invMass > 40 & invMass < 160"),
    numberRequired = cms.string(">= 1"),
    #alias = cms.string("40 < Muon-Tau InvMass < 160")
    )
ZtoTauTau = cms.PSet(
    name = cms.string("ZtoTauTau"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = cms.VPSet (
         tauPairPt,
         tauPairEta,
         tauPairValidHits,
         tauPairNumProng,
         tauPairNumSigGamma,
         tauPairNumSigNeutral,
         tauPairNumPi0,
         tauPairInvMass,
         ),
    )
ZtoMuTau = cms.PSet(
    name = cms.string("ZtoMuTau"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = cms.VPSet (
         tauPt,
         tauEta,
         tauNumProng,
         tauNumSigGamma,
         tauNumSigNeutral,
         tauNumSigPi0,
         tauAgainstElectron,
         tauAgainstMuon,
         tauValidHits,
         muonEta,
         muonPt,
         muonValidHits,
         muonTightId,
         muonIso,
         ),
    )
ZtoTauTrack = cms.PSet(
    name = cms.string("ZtoTauTrack"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = cms.VPSet(
         #muon cuts
         muonPt,
         muonEta,
         muonValidHits,
         muonTightId,
         muonIso,
         # tau cuts
         tauPt,
         tauEta,
         tauAgainstElectron,
         tauAgainstMuon,
         # track cuts
         trackPt,
         trackEta,
         trackd0,
         trackdz,
         trackNumValidHits,
         trkIso,
         # electron and extra muon veto
         muonVetoOneMax,
         deadEcalVeto,
         crackVeto,
         # cuts on pairs of objects
         muonInvMass,
         deltaRTauTrack,
         deltaRMuTrack,
         muTauCharge,
         muTauInvMass,
         electronVetoAll,
         ),
    )
ZtoTauTrackFullPreSel = cms.PSet(
    name = cms.string("ZtoTauTrackFullPreSel"),
    triggers = copy.deepcopy(triggersSingleMu),
    cuts = copy.deepcopy(ZtoTauTrack.cuts)
    )

ZtoTauTrackFullPreSel.cuts.append(electronVetoAll)
ZtoTauTrackFullPreSel.cuts.append(muonVetoOneMax)
ZtoTauTrackFullPreSel.cuts.append(deadEcalVeto)
ZtoTauTrackFullPreSel.cuts.append(crackVeto)
ZtoTauTrackFullPreSel.cuts.append(deltaRTauTrack)
ZtoTauTrackFullPreSel.cuts.append(deltaRMuTau)
ZtoTauTrackFullPreSel.cuts.append(muTauInvMass)
