import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.invMass import *

###############################################
##### Set up the histograms to be plotted #####
###############################################


TrackExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackPtWide"),
            title = cms.string("Track Transverse Momentum;track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 10, 1010),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("trackIsolation"),
            title = cms.string("Relative Track Isolation;relative track isolation"), 
            binsX = cms.untracked.vdouble(100, 0, 0.3),
            inputVariables = cms.vstring("trackIsoDRp3 / pt"),
            ),
        cms.PSet (
            name = cms.string("trackFitPlane"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};E_{calo}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(100, 0, 100),  
            inputVariables = cms.vstring("missingOuterHits", "caloTotNoPUDRp5CentralCalo"),
            ),        
        cms.PSet (
            name = cms.string("trackNHitsMissingOuter"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("missingOuterHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingMiddle"),
            title = cms.string("Number of Missing Middle Hits;N_{miss}^{middle}"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingMiddleHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingInner"),
            title = cms.string("Number of Missing Inner Hits;N_{miss}^{in}"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingInnerHits"),
            ),
        cms.PSet (
            name = cms.string("trackCaloEMDeltaRp5"),
            title = cms.string("caloEMDeltaRp5;E_{EM}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloEMDRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloHadDeltaRp5"),
            title = cms.string("caloHadDeltaRp5;E_{had}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloHadDRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTot"),
            title = cms.string("Isolation energy;E_{calo}^{#DeltaR<0.5} (no PU corr.) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByP"),
            title = cms.string("Relative isolation energy;E_{calo}^{#DeltaR<0.5}/p (no PU corr.)"),
            binsX = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDRp5 / p"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTot_RhoCorr"),
            title = cms.string("Isolation energy (PU corr.);E_{calo}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotNoPUDRp5CentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByP_RhoCorr"),
            title = cms.string("Relative isolation energy (PU corr.);E_{calo}^{#DeltaR<0.5}/p"),
            binsX = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotNoPUDRp5CentralCalo / p"),
            ),
        cms.PSet (
            name = cms.string("trackPtError"),
            title = cms.string("ptError;#sigma(p_{T}) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("ptError"),
            ),
        cms.PSet (
            name = cms.string("trackPtErrorByPt"),
            title = cms.string("ptErrorByPt;#sigma(p_{T})/p_{T}"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("ptError / pt"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRMinElecLooseMvaId"),
            title = cms.string("deltaRMinElecLooseMvaId;#DeltaR_{min}(track,electron)"), 
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestElectron"),
            ),
        cms.PSet (
            name = cms.string("trackTauDeltaRVsTrackElectronDeltaR"),
            title = cms.string(";#DeltaR_{min}(track,electron);#DeltaR_{min}(track,tau)"), 
            binsX = cms.untracked.vdouble(100, 0, 0.001),
            binsY = cms.untracked.vdouble(100, 0, 0.001),
            inputVariables = cms.vstring("deltaRToClosestElectron", "deltaRToClosestTau"),
            ),
        cms.PSet (
            name = cms.string("trackTauDeltaRVsTrackMuonDeltaR"),
            title = cms.string(";#DeltaR_{min}(track,muon);#DeltaR_{min}(track,tau)"), 
            binsX = cms.untracked.vdouble(100, 0, 0.001),
            binsY = cms.untracked.vdouble(100, 0, 0.001),
            inputVariables = cms.vstring("deltaRToClosestMuon", "deltaRToClosestTau"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRMinMuonLooseId"),
            title = cms.string("deltaRMinMuonLooseId;#DeltaR_{min}(track,muon)"),  
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestMuon"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRMinTauLooseHadronicId"),
            title = cms.string("deltaRMinTauLooseHadronicId;#DeltaR_{min}(track,tau)"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestTau"),   
            ),
        cms.PSet (
            name = cms.string("genMatchedTauDecayProductFinalStateVsPromptFinalStateIsMatched"),
            title = cms.string(";track is matched to generator particle;track is matched to generator #tau decay product"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5), 
            binsY = cms.untracked.vdouble(2.0, -0.5, 1.5), 
            inputVariables = cms.vstring("genMatchedParticle.promptFinalState.isNonnull", "genMatchedParticle.directPromptTauDecayProductFinalState.isNonnull"),  
        ),


        )
    )

TrackMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("invMass"),
            title = cms.string(";M(#mu,track) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 500.0),
            inputVariables = cms.vstring(invMassWithMuon ("muon")),
        ),
        cms.PSet (
            name = cms.string("invMassNearZ"),
            title = cms.string(";M(#mu,track) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring(invMassWithMuon ("muon")),
        ),
        cms.PSet (
            name = cms.string("deltaR"),
            title = cms.string(";#DeltaR(#mu,track) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("deltaR (track, muon)"),
        ),
        cms.PSet (
            name = cms.string("deltaPhi"),
            title = cms.string(";#Delta#phi(#mu,track) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("deltaPhi (track, muon)"),
        ),
        cms.PSet (
            name = cms.string("deltaEta"),
            title = cms.string(";#Delta#eta(#mu,track) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 4.0),
            inputVariables = cms.vstring("fabs (track.eta - muon.eta)"),
        ),
        cms.PSet (
            name = cms.string("chargeProduct"),
            title = cms.string(";q_{#mu}#timesq_{track}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("muon.charge * track.charge"),
        ),
    )
)

TrackElectronHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("invMass"),
            title = cms.string(";M(e,track) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 500.0),
            inputVariables = cms.vstring(invMassWithElectron ("electron")),
        ),
        cms.PSet (
            name = cms.string("invMassNearZ"),
            title = cms.string(";M(e,track) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring(invMassWithElectron ("electron")),
        ),
        cms.PSet (
            name = cms.string("deltaR"),
            title = cms.string(";#DeltaR(e,track) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("deltaR (track, electron)"),
        ),
        cms.PSet (
            name = cms.string("deltaPhi"),
            title = cms.string(";#Delta#phi(e,track) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("deltaPhi (track, electron)"),
        ),
        cms.PSet (
            name = cms.string("deltaEta"),
            title = cms.string(";#Delta#eta(e,track) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 4.0),
            inputVariables = cms.vstring("fabs (track.eta - electron.eta)"),
        ),
        cms.PSet (
            name = cms.string("chargeProduct"),
            title = cms.string(";q_{e}#timesq_{track}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("electron.charge * track.charge"),
        ),
    )
)

histograms = cms.PSet(  # for testing 
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muonPt"),
            title = cms.string("Muon Transverse Momentum; muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("muonEta"),
            title = cms.string("Muon Pseudorapidity; muon #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
        ),
    )
)




TriggerObjectHistograms = cms.PSet(
    inputCollection = cms.vstring("trigobjs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trigObjPtVsMet"),
            title = cms.string("trigObjPtVsMet;E^{miss}_{T} [GeV]; L1 E^{miss}_{T}[GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, 0, 500),
            inputVariables = cms.vstring("metPt", "pt"),
            ),
        cms.PSet (
            name = cms.string("trigObjPtVsTrackPt"),
            title = cms.string("trigObjPtVsTrackPt;track p_{T} [GeV]; L1 elec p_{T} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, 0, 500),
            inputVariables = cms.vstring("trackPt", "pt"),
            ),
        cms.PSet (
            name = cms.string("trigObjPtVsJetPt"),
            title = cms.string("trigObjPtVsJetPt;jet p_{T} [GeV]; L1 jet p_{T} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, 0, 500),
            inputVariables = cms.vstring("jetPt", "pt"),
            ),
                
        cms.PSet (
            name = cms.string("trigObjPt"),
            title = cms.string("trigObjPt; p_{T}"),
            bins = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
            ),
        )
    )



TrackJetHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackJetDeltaR"),
            title = cms.string("Track-Jet #DeltaR; #DeltaR(trk-jet)"),
            bins = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("deltaR ( track , jet ) "),
            ),
        )
    )
        

DiMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diMuonInvMass"),
            title = cms.string("Di-Muon Invariant Mass; M_{#mu#mu} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 180),
            inputVariables = cms.vstring("invMass"),
            ),
        cms.PSet (
            name = cms.string("diMuonChargeProduct"),
            title = cms.string("Di-muon Charge Product; charge_{#mu}_{1}*charge_{#mu}_{2}"),
            bins = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("chargeProduct"),
            ),
        cms.PSet (
            name = cms.string("diMuonDeltaEta"),
            title = cms.string("Di-muon Eta Difference; |#Delta(#eta)|"),
            bins = cms.untracked.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaEta"),
            ),
        cms.PSet (
            name = cms.string("diMuonDeltaPhi"),
            title = cms.string("Di-muon Phi Difference; |#Delta(#phi)|"),
            bins = cms.untracked.vdouble(1000, 0, 3.14),
            inputVariables = cms.vstring("deltaPhi"),
            ),
        cms.PSet (
            name = cms.string("diMuonDeltaR"),
            title = cms.string("Di-muon #DeltaR; #DeltaR"),
            bins = cms.untracked.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaR"),
            ),
        
        )
    )

DiElectronHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons", "electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diElectronInvMass"),
            title = cms.string("Di-electron Invariant Mass; M_{ee} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 180),
            inputVariables = cms.vstring("invMass"),
            ),
        cms.PSet (
            name = cms.string("diElectronChargeProduct"),
            title = cms.string("Di-electron Charge Product; charge_{e}_{1}*charge_{e}_{2}"),
            bins = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("chargeProduct"),
            ),
        cms.PSet (
            name = cms.string("diElectronDeltaEta"),
            title = cms.string("Di-electron Eta Difference; |#Delta(#eta)|"),
            bins = cms.untracked.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaEta"),
            ),
        cms.PSet (
            name = cms.string("diElectronDeltaPhi"),
            title = cms.string("Di-electron Phi Difference; |#Delta(#phi)|"),
            bins = cms.untracked.vdouble(1000, 0, 3.14),
            inputVariables = cms.vstring("deltaPhi"),
            ),
        cms.PSet (
            name = cms.string("diElectronDeltaR"),
            title = cms.string("Di-electron #DeltaR; #DeltaR"),
            bins = cms.untracked.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaR"),
            ),
        
        )
    )


JetExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetEtaVsPhi"),
            title = cms.string("jetEtaVsPhi; jetEtaVsPhi"),
            bins = cms.untracked.vdouble(100, -3, 3, 100, -3, 3),
            inputVariables = cms.vstring("eta" , "phi"),
            ),
        cms.PSet (
            name = cms.string("jetNvtx"),
            title = cms.string("jetsNvtx; jetsNvtx"),
            bins = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("nvtx"),
            ),
        cms.PSet (
            name = cms.string("jetIdLoose"),
            title = cms.string("jetIdLoose; jetIdLoose"),
            bins = cms.untracked.vdouble(100, -0.5, 1.5),
            inputVariables = cms.vstring("jetIDLoose"),
            ),
        cms.PSet (
            name = cms.string("jetD0"),
            title = cms.string("jetD0; jetD0"),
            bins = cms.untracked.vdouble(100, -0.02, 0.02),
            inputVariables = cms.vstring("d0"),
            ),
        cms.PSet (
            name = cms.string("jetDz"),
            title = cms.string("jetDz; jetDz"),
            bins = cms.untracked.vdouble(100, -5, 15),
            inputVariables = cms.vstring("dZ"),
            ),
        cms.PSet (
            name = cms.string("jetBTagProb"),
            title = cms.string("jetBTagProb; jetBTagProb"),
            bins = cms.untracked.vdouble(100, -0.05, 1.5),
            inputVariables = cms.vstring("btagJetProb"),
            ),
        cms.PSet (
            name = cms.string("jetBTagSoftMuon"),
            title = cms.string("jetBTagSoftMuon; jetBTagSoftMuon"),
            bins = cms.untracked.vdouble(100, -0.05, 1.5),
            inputVariables = cms.vstring("btagSoftMuon"),
            ),
        cms.PSet (
            name = cms.string("jetBTagSoftEle"),
            title = cms.string("jetBTagSoftEle; jetBTagSoftEle"),
            bins = cms.untracked.vdouble(100, -0.05, 1.5),
            inputVariables = cms.vstring("btagSoftEle"),
            ),
        
        cms.PSet (
            name = cms.string("jetEmFrac"),
            title = cms.string("jetEmFrac; jetEmFrac"),
            bins = cms.untracked.vdouble(100, -1.5, 1.5),
            inputVariables = cms.vstring("EMfrac"),
            ),
        
        cms.PSet (
            name = cms.string("jetHadFrac"),
            title = cms.string("jetHadFrac; jetHadFrac"),
            bins = cms.untracked.vdouble(100, -1.5, 1.5),
            inputVariables = cms.vstring("Hadfrac"),
            ),
        cms.PSet (
            name = cms.string("jetChHadEnergy"),
            title = cms.string("jetChHadEnergy; jetChHadEnergy"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("chargedHadronEnergy"),
            ),
        cms.PSet (
            name = cms.string("jetChEmEnergy"),
            title = cms.string("jetChEmEnergy; jetChEmEnergy"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("chargedEmEnergy"),
            ),
        cms.PSet (
            name = cms.string("jetNeuEmEnergy"),
            title = cms.string("jetNeuEmEnergy; jetNeuEmEnergy"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("neutralEmEnergy"),
            ),
        cms.PSet (
            name = cms.string("jetNeuHadEnergy"),
            title = cms.string("jetNeuHadEnergy; jetNeuHadEnergy"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("neutralHadronEnergy"),
            ),
        cms.PSet (
            name = cms.string("jetfHPD"),
            title = cms.string("jetfHPD; jetfHPD"),
            bins = cms.untracked.vdouble(100, 0, 3),
            inputVariables = cms.vstring("fHPD"),
            ),
        cms.PSet (
            name = cms.string("jetn90hits"),
            title = cms.string("jetn90hits; jetn90hits"),
            bins = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("n90Hits"),
            ),
        
        
        )
    )


MCParticleExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("mcparticles"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("mcparticlePdgIdSusy"), 
            title = cms.string("mcparticlePdgIdSusy; pdgId of SUSY mcparticles"),
            bins = cms.untracked.vdouble(10, 1000020, 1000030),  
            inputVariables = cms.vstring("id"),
            ),
        cms.PSet (
            name = cms.string("mcparticleAbsPdgIdSusy"), 
            title = cms.string("mcparticlePdgIdSusy; |pdgId| of SUSY mcparticles"),
            bins = cms.untracked.vdouble(10, 1000020, 1000030),  
            inputVariables = cms.vstring("fabs(id)"),
            ),
        cms.PSet (
            name = cms.string("mcparticleMass"), 
            title = cms.string("mcparticleMass; mcparticle mass [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500),   
            inputVariables = cms.vstring("mass"),
            ),
        cms.PSet (
            name = cms.string("mcpartDeltaPhiMaxSubLeadJet"),
            title = cms.string("maximum mcparticle-jet #Delta#phi; #Delta#phi_{max}(mcparticle-jet)"),
            bins = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("deltaPhiMaxSubLeadJet"),
            ),                                              
        )
    )


JetExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetChargedEmEnergyFraction"),
            title = cms.string("Jet Charged EM Energy Fraction;Jet Charged EM Energy Fraction"),
            bins = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("chargedEmEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("jetChargedHadronEnergyFraction"),
            title = cms.string("Jet Charged Hadron Energy Fraction;Jet Charged Hadron Energy Fraction"),
            bins = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("chargedHadronEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("jetNeutralEmEnergyFraction"),
            title = cms.string("Jet Neutral EM Energy Fraction;Jet Neutral EM Energy Fraction"),
            bins = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("neutralEmEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("jetNeutralHadronEnergyFraction"),
            title = cms.string("Jet Neutral Hadron Energy Fraction;Jet Neutral Hadron Energy Fraction"), 
            bins = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("neutralHadronEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("jetDeltaPhiMet"),
            title = cms.string("Jet #Delta #phi E^{miss}_{T};Jet #Delta #phi E^{miss}_{T}"), 
            bins = cms.untracked.vdouble(70, -3.5, 3.5),
            inputVariables = cms.vstring("dPhiMet"),
            ),
        cms.PSet (
            name = cms.string("jetIDLoose"),
            title = cms.string(";Jet loose ID"),   
            bins = cms.untracked.vdouble(2, -0.5, 1.5),  
            inputVariables = cms.vstring("jetIDLoose"),
            ),
        cms.PSet (
            name = cms.string("jetBeta"),
            title = cms.string(";Jet #beta"),   
            bins = cms.untracked.vdouble(100, 0, 1.0),  
            inputVariables = cms.vstring("beta"),
            ),
        cms.PSet (
            name = cms.string("jetBtagCombinedSecVertex"),
            title = cms.string(";Jet CSV"),   
            bins = cms.untracked.vdouble(100, 0, 1.0),  
            inputVariables = cms.vstring("btagCombinedSecVertex"),
            ),
        cms.PSet (
            name = cms.string("jetPtVsMet"),
            title = cms.string("Jet p_{T} vs. E^{miss}_{T};E^{miss}_{T} [GeV]; Jet p_{T} [GeV]"), 
            bins = cms.untracked.vdouble(20, 0, 500, 20, 0, 500),
            inputVariables = cms.vstring("metPt", "pt"),
            ),
        cms.PSet (
            name = cms.string("jetDeltaRMuonPt20"),
            title = cms.string("; #DeltaR(jet-muon)"), 
            bins = cms.untracked.vdouble(100, 0, 5),  
            inputVariables = cms.vstring("deltaRMuonPt20"),
            ),
    )
)

MetExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
         cms.PSet (
             name = cms.string("metSig"),
             title = cms.string("Met Significance ;E^{miss}_{T} Significance"),
             bins = cms.untracked.vdouble(100, 0, 100),
             inputVariables = cms.vstring("significance"),
             ),
         cms.PSet (
            name = cms.string("metVsGenMet"),
            title = cms.string("reco E^{miss}_{T} vs gen  E^{miss}_{T} ; reco E^{miss}_{T} [GeV];gen E^{miss}_{T} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500, 100, 0, 500),
            inputVariables = cms.vstring("pt", "genPT"),
            ),
         cms.PSet (
            name = cms.string("metNoMu"),
            title = cms.string("MetNoMu;MetNoMu [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500),  
            inputVariables = cms.vstring("metNoMu"),
            ),
        cms.PSet (
            name = cms.string("metNoElec"),
            title = cms.string("MetNoElec;MetNoElec [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500),  
            inputVariables = cms.vstring("metNoElec"),
            ),
        cms.PSet (
            name = cms.string("metDeltaPhiMin2Jets"),
            title = cms.string("deltaPhiMin2Jets;#Delta#phi_{min}(E_{T}^{miss}-jet)"),  
            bins = cms.untracked.vdouble(20, 0, 3.15),  
            inputVariables = cms.vstring("deltaPhiMin2Jets"),
            ),
        cms.PSet (
            name = cms.string("metDeltaPhiJet1"),
            title = cms.string("metDeltaPhiJet1;#Delta#phi^{met-leadjet}"),
            bins = cms.untracked.vdouble(20, 0, 3.15),  
            inputVariables = cms.vstring("deltaPhiJet1"),
            ),
        cms.PSet (
            name = cms.string("metDeltaPhiJet2"),
            title = cms.string("metDeltaPhiJet2;#Delta#phi^{met-subleadjet}"),
            bins = cms.untracked.vdouble(20, 0, 3.15),  
            inputVariables = cms.vstring("deltaPhiJet2"),
            ),
        )
    )


DiJetHistograms = cms.PSet(
    inputCollection = cms.vstring("jet", "jet"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("dijetDeltaPhi"),
            title = cms.string(";#Delta#phi(dijet)"),  
            bins = cms.untracked.vdouble(100, 0, 3.15),   
            inputVariables = cms.vstring("deltaPhi ( jet , jet )"),
            ),
    )
)  

############################################################################################
TauExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("taus"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("tauHPSagainstElectronLoose"),
            title = cms.string("Tau HPSagainstElectronLoose;HPSagainstElectronLoose"),
            bins = cms.untracked.vdouble(5, -0.5, 4.5),
            inputVariables = cms.vstring("HPSagainstElectronLoose"),
            ),
        cms.PSet (
            name = cms.string("tauHPSagainstElectronMedium"),
            title = cms.string("Tau HPSagainstElectronMedium;HPSagainstElectronMedium"),
            bins = cms.untracked.vdouble(5, -0.5, 4.5),
            inputVariables = cms.vstring("HPSagainstElectronMedium"),
            ),
        cms.PSet (
            name = cms.string("tauHPSagainstElectronTight"),
            title = cms.string("Tau HPSagainstElectronTight;HPSagainstElectronTight"),
            bins = cms.untracked.vdouble(5, -0.5, 4.5),
            inputVariables = cms.vstring("HPSagainstElectronTight"),
            ),
        cms.PSet (
            name = cms.string("tauHPSagainstElectronMVA"),
            title = cms.string("Tau HPSagainstElectronMVA;HPSagainstElectronMVA"),
            bins = cms.untracked.vdouble(5, -0.5, 4.5),
            inputVariables = cms.vstring("HPSagainstElectronMVA"),
            ),
        cms.PSet (
            name = cms.string("tauHPSagainstMuonTight"),
            title = cms.string("Tau HPSagainstMuonTight;HPSagainstMuonTight"),
            bins = cms.untracked.vdouble(5, -0.5, 4.5),
            inputVariables = cms.vstring("HPSagainstMuonTight"),
            ),
        cms.PSet (
            name = cms.string("tauHPSdecayModeFinding"),
            title = cms.string("Tau HPSdecayModeFinding;HPSdecayModeFinding"),
            bins = cms.untracked.vdouble(5, -0.5, 4.5),
            inputVariables = cms.vstring("HPSdecayModeFinding"),
            ),
        )
    )

############################################################################################

EventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("lifetimeWeight"),
            title = cms.string(";lifetime weight"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("lifetimeWeight"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("ctau"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 50.0),
            inputVariables = cms.vstring("cTau_1000024_0"),
        ),
    )
)
