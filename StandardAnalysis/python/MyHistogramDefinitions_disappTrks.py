import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################

        
TrackJetHistograms = cms.PSet(
    inputCollection = cms.string("track-jet pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackJetDeltaR"),
            title = cms.string("Track-Jet #DeltaR; #DeltaR(trk-jet)"),
            bins = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("deltaR"),
            ),
        )
    )
        

DiMuonHistograms = cms.PSet(
    inputCollection = cms.string("muon-muon pairs"),
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
    inputCollection = cms.string("electron-electron pairs"),
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


ShortTrackHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackPt"),
            title = cms.string("Track Transverse Momentum; p_{T} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
            ),
        cms.PSet (
            name = cms.string("trackEta"),
            title = cms.string("Track Eta; #eta"),
            bins = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
            ),
        cms.PSet (
            name = cms.string("trackPhi"),
            title = cms.string("Track Phi; #phi"),
            bins = cms.untracked.vdouble(100, -5, 5),
            inputVariables = cms.vstring("phi"),
            ),
    )
)  # end ShortTrackHistograms
 


SecMuonHistograms = cms.PSet(
    inputCollection = cms.string("secondary muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("secMuonPt"),
            title = cms.string("Secondary muon transverse momentum; p_{T} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
            ),
    )
)  # end SecMuonHistograms



TestEventHistograms = cms.PSet(
    inputCollection = cms.string("events"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("NumberOfPrimaryVertices"),
            title = cms.string("numPV; number of primary vertices"),
            bins = cms.untracked.vdouble(51, -0.5, 50.5),
            inputVariables = cms.vstring("numPV"),
            ),
    )
)


TestTrackEventHistograms = cms.PSet(
    inputCollection = cms.string("track-event pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackCaloTotVsNumPV"),
            title = cms.string("Isolation energy vs. num. primary vertices; number of primary vertices; E_{iso}^{#DeltaR<0.5}"),
            bins = cms.untracked.vdouble(51, -0.5, 50.5, 100, 0, 100),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByPVsNumPV"),
            title = cms.string("Isolation energy / p vs. num. primary vertices; number of primary vertices; E_{iso}^{#DeltaR<0.5}/p"),
            bins = cms.untracked.vdouble(51, -0.5, 50.5, 100, 0, 2),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotVsNumPV_RhoCorr"),
            title = cms.string("Isolation energy (PU corr.) vs. num. primary vertices; number of primary vertices; E_{iso}^{#DeltaR<0.5} (PU corr.)"),
            bins = cms.untracked.vdouble(51, -0.5, 50.5, 100, 0, 100),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByPVsNumPV_RhoCorr"),
            title = cms.string("Isolation energy / p (PU corr.) vs. num. primary vertices; number of primary vertices; E_{iso}^{#DeltaR<0.5}/p (PU corr.)"),
            bins = cms.untracked.vdouble(51, -0.5, 50.5, 100, 0, 2),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5ByPRhoCorr"),
            ),
    )
)



TestTrackHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackCaloTot"),
            title = cms.string("Isolation energy; E_{iso}^{#DeltaR<0.5}"),
            bins = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByP"),
            title = cms.string("Isolation energy / p; E_{iso}^{#DeltaR<0.5}/p"),
            bins = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTot_RhoCorr"),
            title = cms.string("Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5} (PU corr.)"),
            bins = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByP_RhoCorr"),
            title = cms.string("Isolation energy / p (PU corr.); E_{iso}^{#DeltaR<0.5}/p (PU corr.)"),
            bins = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByPRhoCorr"),
            ),
    )
)


TrackIsolationHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackNTracksRp5"),
            title = cms.string("trackNTracksRp5; # Tracks (#DeltaR<0.5)"),
            bins = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("nTracksRp5"),
            ),
        cms.PSet (
            name = cms.string("trackRelIsoRp3"),
            title = cms.string("trackRelIsoRp3; (#Sigma p_{T}^{#Delta R<0.3} - p_{T})/p_{T}"),
            bins = cms.untracked.vdouble(100, 0, 3),
            inputVariables = cms.vstring("trkRelIsoRp3"),
            ),
        cms.PSet (
            name = cms.string("trackRelIsoRp3Zoom"),
            title = cms.string("trackRelIsoRp3; (#Sigma p_{T}^{#Delta R<0.3} - p_{T})/p_{T}"),
            bins = cms.untracked.vdouble(100, 0, 0.2),
            inputVariables = cms.vstring("trkRelIsoRp3"),
            ),
        cms.PSet (
            name = cms.string("trackDepTrkRp5"),
            title = cms.string("depTrkRp5; #Sigma^{#DeltaR<0.5} p_{T} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("depTrkRp5"),
            ),
        cms.PSet (
            name = cms.string("trackDepTrkRp5MinusPt"),
            title = cms.string("depTrkRp5MinusPt; #Sigma^{#DeltaR<0.5} p_{T} - p_{T}^{cand} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("depTrkRp5MinusPt"),
            ),
        cms.PSet (
            name = cms.string("trackDepEcalRp5"),
            title = cms.string("depEcalRp5; #Sigma^{#DeltaR<0.5} Ecal [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("depEcalRp5"),
            ),
        cms.PSet (
            name = cms.string("trackDepHcalRp5"),
            title = cms.string("depHcalRp5; #Sigma^{#DeltaR<0.5} Hcal [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("depHcalRp5"),
            ),
        cms.PSet (
            name = cms.string("trackDepHoRp5"),
            title = cms.string("depHoRp5; #Sigma^{#DeltaR<0.5} Ho [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("depHoRp5"),
            ),
        cms.PSet (
            name = cms.string("trackTrkVetoPtRp5"),
            title = cms.string("trackerVetoPtRp5; trackerVetoPtRp5"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("trackerVetoPtRp5"),
            ),
        cms.PSet (
            name = cms.string("trackEmVetoEtRp5"),
            title = cms.string("emVetoEtRp5; emVetoEtRp5"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("emVetoEtRp5"),
            ),
        cms.PSet (
            name = cms.string("trackHadVetoEtRp5"),
            title = cms.string("hadVetoEtRp5; hadVetoEtRp5"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("hadVetoEtRp5"),
            ),
        cms.PSet (
            name = cms.string("trackHoVetoEtRp5"),
            title = cms.string("hoVetoEtRp5; hoVetoEtRp5"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("hoVetoEtRp5"),
            ),
        cms.PSet (
            name = cms.string("trackNTracksRp3"),
            title = cms.string("nTracksRp3; # Tracks (#DeltaR<0.3)"),
            bins = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("nTracksRp3"),
            ),
        
        cms.PSet (
            name = cms.string("trackDepTrkRp3"),
            title = cms.string("depTrkRp3; #Sigma^{#DeltaR<0.3} p_{T} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("depTrkRp3"),
            ),
        cms.PSet (
            name = cms.string("trackDepTrkRp3MinusPt"),
            title = cms.string("depTrkRp3MinusPt; #Sigma^{#DeltaR<0.3} p_{T} - p_{T}^{cand} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("depTrkRp3MinusPt"),
            ),
        cms.PSet (
            name = cms.string("trackDepEcalRp3"),
            title = cms.string("depEcalRp3; #Sigma^{#DeltaR<0.3} Ecal [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("depEcalRp3"),
            ),
        cms.PSet (
            name = cms.string("trackDepHcalRp3"),
            title = cms.string("depHcalRp3; #Sigma^{#DeltaR<0.3} Hcal [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("depHcalRp3"),
            ),
        cms.PSet (
            name = cms.string("trackDepHoRp3"),
            title = cms.string("depHoRp3; #Sigma^{#DeltaR<0.3} Ho [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("depHoRp3"),
            ),
        cms.PSet (
            name = cms.string("trackTrkVetoPtRp3"),
            title = cms.string("trackerVetoPtRp3; trackerVetoPtRp3"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("trackerVetoPtRp3"),
            ),
        cms.PSet (
            name = cms.string("trackEmVetoEtRp3"),
            title = cms.string("emVetoEtRp3; emVetoEtRp3"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("emVetoEtRp3"),
            ),
        cms.PSet (
            name = cms.string("trackHadVetoEtRp3"),
            title = cms.string("hadVetoEtRp3; hadVetoEtRp3"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("hadVetoEtRp3"),
            ),
        cms.PSet (
            name = cms.string("trackHoVetoEtRp3"),
            title = cms.string("hoVetoEtRp3; hoVetoEtRp3"),
            bins = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("hoVetoEtRp3"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRMinSubLeadJet"),
            title = cms.string("minimum track-jet #DeltaR; #DeltaR_{min}(trk-jet)"),
            bins = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("deltaRMinSubLeadJet"),
            ),        
        )
    )

TrackDiMuonHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackDeltaPhiDiMuon"),
            title = cms.string("DeltaPhi(Track-Dimuon); |#Delta#phi(track-(#mu^{+}#mu^{-}))|"),
            bins = cms.untracked.vdouble(100, 0, 3.15),
            inputVariables = cms.vstring("fabs(deltaPhiMuMuPair)"),
            ),
        )
    )

ExtraTrackHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackEtaMag"),
            title = cms.string("Track Eta; |#eta|"),
            bins = cms.untracked.vdouble(25, 0, 2.5),
            inputVariables = cms.vstring("fabs(eta)"),
            ),
        cms.PSet (
            name = cms.string("trackEtaMagFine"),
            title = cms.string("Track Eta; |#eta|"),
            bins = cms.untracked.vdouble(50, 0, 2.5),
            inputVariables = cms.vstring("fabs(eta)"),
            ),
        cms.PSet (
            name = cms.string("trackEtaMag"),
            title = cms.string("Track Eta; |#eta|"),
            bins = cms.untracked.vdouble(20, 0, 2.5),
            inputVariables = cms.vstring("fabs(eta)"),
            ),
        cms.PSet (
            name = cms.string("trackPtCoarse"),
            title = cms.string("Track Pt; p_{T} [GeV]"),
            variableBinsX = cms.untracked.vdouble(20, 40, 60, 100, 200, 500), 
            inputVariables = cms.vstring("pt"),   
            ),
        cms.PSet (
            name = cms.string("trackEtaVsPt"),
            title = cms.string("#eta vs p_{T}; #eta; p_{T}"),
            variableBinsX = cms.untracked.vdouble(0, 0.15, 0.35, 0.8, 1.2, 1.5, 1.8, 2.1),  
            variableBinsY = cms.untracked.vdouble(20, 40, 60, 100, 200, 500), 
            inputVariables = cms.vstring("fabs(eta)", "pt"),
            ),
        cms.PSet (
            name = cms.string("trackD0wrtBS"),
            title = cms.string("Track d_{0} wrt BS; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.1, 0.1),
            inputVariables = cms.vstring("d0wrtBS"),
            ),
        cms.PSet (
            name = cms.string("trackDZwrtBS"),
            title = cms.string("Track d_{z} wrt BS; d_{z} [cm]"),
            bins = cms.untracked.vdouble(100, -20, 20),
            inputVariables = cms.vstring("dZwrtBS"),
            ),
##         cms.PSet (
##             name = cms.string("trackDzVsD0"),
##             title = cms.string("|d_{z}| vs |d_{0}|;|d_{0}| [cm];|d_{z}| [cm]"),
##             bins = cms.untracked.vdouble(50, 0.0, 0.5, 100, 0, 10), 
##             inputVariables = cms.vstring("fabs(d0wrtPV)", "fabs(dZwrtPV)"),
##             ),
##         cms.PSet (
##             name = cms.string("trackNHitsVsD0"),
##             title = cms.string("N_{hits} vs |d_{0}|;|d_{0}| [cm];N_{hits}"),
##             bins = cms.untracked.vdouble(50, 0.0, 0.5, 31, -0.5, 30.5), 
##             inputVariables = cms.vstring("fabs(d0wrtPV)", "numValidHits"),
##             ),
##         cms.PSet (
##             name = cms.string("trackNMissMidVsD0"),
##             title = cms.string("N_{miss}^{middle} vs |d_{0}|;|d_{0}| [cm];N_{miss}^{middle}"),
##             bins = cms.untracked.vdouble(50, 0.0, 0.5, 6, -0.5, 5.5), 
##             inputVariables = cms.vstring("fabs(d0wrtPV)", "nHitsMissingMiddle"),
##             ),
##         cms.PSet (
##             name = cms.string("trackNHitsVsDz"),
##             title = cms.string("N_{hits} vs |d_{z}|;|d_{z}| [cm];N_{hits}"),
##             bins = cms.untracked.vdouble(100, 0, 10, 31, -0.5, 30.5), 
##             inputVariables = cms.vstring("fabs(dZwrtPV)", "numValidHits"),
##             ),
##         cms.PSet (
##             name = cms.string("trackNMissMidVsDz"),
##             title = cms.string("N_{miss}^{middle} vs |d_{z}|;|d_{z}| [cm];N_{miss}^{middle}"),
##             bins = cms.untracked.vdouble(100, 0, 10, 6, -0.5, 5.5), 
##             inputVariables = cms.vstring("fabs(dZwrtPV)", "nHitsMissingMiddle"),
##             ),
##         cms.PSet (
##             name = cms.string("trackNMissMidVsNHits"),
##             title = cms.string("N_{miss}^{middle} vs N_{hits};N_{hits};N_{miss}^{middle}"),
##             bins = cms.untracked.vdouble(31, -0.5, 30.5, 6, -0.5, 5.5), 
##             inputVariables = cms.vstring("numValidHits", "nHitsMissingMiddle"),
##             ),
        cms.PSet (
            name = cms.string("trackD0wrtPV"),
            title = cms.string("Track d_{0} wrt PV; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.1, 0.1),
            inputVariables = cms.vstring("d0wrtPV"),
            ),
        cms.PSet (
            name = cms.string("trackD0wrtPVAbs"),
            title = cms.string("Track d_{0} wrt PV; |d_{0}| [cm]"),
            bins = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("fabs(d0wrtPV)"),
            ),
        cms.PSet (
            name = cms.string("trackD0wrtPVWide"),
            title = cms.string("Track d_{0} wrt PV; d_{0} [cm]"),
            bins = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("d0wrtPV"),
            ),
        cms.PSet (
            name = cms.string("trackDZwrtPVAbs"),
            title = cms.string("Track d_{z} wrt PV; |d_{z}| [cm]"),
            bins = cms.untracked.vdouble(50, 0, 0.1),
            inputVariables = cms.vstring("fabs(dZwrtPV)"),
            ),
        cms.PSet (
            name = cms.string("trackDZwrtPV"),
            title = cms.string("Track d_{z} wrt PV; d_{z} [cm]"),
            bins = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("dZwrtPV"),
            ),
        cms.PSet (
            name = cms.string("trackDZSinTheta"),
            title = cms.string("Track d_{z} sin #theta; d_{z} sin(#theta) [cm]"),
            bins = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("dZSinTheta"),
            ),
        cms.PSet (
           name = cms.string("trackDZwrtPVWide"),
           title = cms.string("Track d_{z} wrt PV; d_{z} [cm]"),
           bins = cms.untracked.vdouble(200, -10, 10),
           inputVariables = cms.vstring("dZwrtPV"),
           ),       
        cms.PSet (
            name = cms.string("trackChi2Narrow"),
            title = cms.string("Track Reduced Chi2; #chi^{2} / DOF"),
            bins = cms.untracked.vdouble(100, 0, 6),
            inputVariables = cms.vstring("normChi2"),
        ),
        cms.PSet (
            name = cms.string("trackEtaVsPhi"),
            title = cms.string("#eta vs #phi; #eta; #phi"),
            bins = cms.untracked.vdouble(100, -3, 3, 100, -3.2, 3.2),
            inputVariables = cms.vstring("eta", "phi"),
            ),
        cms.PSet (
            name = cms.string("trackFitPlane"),
            title = cms.string("Number of Missing Outer Hits; N_{miss}^{out};E_{calo}^{#DeltaR<0.5} [GeV]"),
            bins = cms.untracked.vdouble(16, -0.5, 15.5, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter", "caloTotDeltaRp5RhoCorr"),
            ),
##         cms.PSet (
##             name = cms.string("trackNumValidVsEcalo"),
##             title = cms.string("Number of Valid Hits; N_{miss}^{out};E_{calo}^{#DeltaR<0.5} [GeV]"),
##             bins = cms.untracked.vdouble(16, -0.5, 20.5, 100, 0, 100),
##             inputVariables = cms.vstring("numValidHits", "caloTotDeltaRp5RhoCorr"),
##             ),
        
        cms.PSet (
            name = cms.string("trackNHitsMissingOuter"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out}"),
            bins = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("nHitsMissingOuter"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingMiddle"),
            title = cms.string("Number of Missing Middle Hits;N_{miss}^{middle}"),
            bins = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("nHitsMissingMiddle"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingInner"),
            title = cms.string("Number of Missing Inner Hits;N_{miss}^{in}"),
            bins = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("nHitsMissingInner"),
            ),
##         cms.PSet (
##             name = cms.string("trackNTracksRp5"),
##             title = cms.string("nTracksRp5; # Tracks (#DeltaR<0.5)"),
##             bins = cms.untracked.vdouble(16, -0.5, 15.5),
##             inputVariables = cms.vstring("nTracksRp5"),
##             ),
##         cms.PSet (
##             name = cms.string("trackDepTrkRp5"),
##             title = cms.string("depTrkRp5; #Sigma^{#DeltaR<0.5} p_{T} [GeV]"),
##             bins = cms.untracked.vdouble(100, 0, 100),
##             inputVariables = cms.vstring("depTrkRp5"),
##             ),
##         cms.PSet (
##             name = cms.string("trackDepTrkRp5MinusPt"),
##             title = cms.string("depTrkRp5MinusPt; #Sigma^{#DeltaR<0.5} p_{T} - p_{T}^{cand} [GeV]"),
##             bins = cms.untracked.vdouble(100, 0, 100),
##             inputVariables = cms.vstring("depTrkRp5MinusPt"),
##             ),

        cms.PSet (
            name = cms.string("trackdPhiMet"),
            title = cms.string("dPhiMetTrk; #Delta #phi (E^{miss}_{T}, trk))"),
            bins = cms.untracked.vdouble(100, -4, 4),
            inputVariables = cms.vstring("dPhiMet"),
            ),
        cms.PSet (
            name  = cms.string("trackIsBadCSC"),  
            title = cms.string("Track isMatchedBadCSC; isMatchedBadCSC"), 
            bins = cms.untracked.vdouble(2, -0.5, 1.5), 
            inputVariables = cms.vstring("isMatchedBadCSC"), 
            ),
        cms.PSet (
            name  = cms.string("trackIsPassMuonLooseID"),  
            title = cms.string("isPassMuonLooseID; isPassMuonLooseID"), 
            bins = cms.untracked.vdouble(2, -0.5, 1.5), 
            inputVariables = cms.vstring("isPassMuonLooseID"), 
            ),
        cms.PSet (
            name  = cms.string("trackIsPassMuonLooseIDVsNHitsOut"),  
            title = cms.string("muon veto efficiency vs. missing outer hits; N_{miss}^{out}; isPassMuonLooseID"), 
            bins = cms.untracked.vdouble(16, -0.5, 15.5, 2, -0.5, 1.5), 
            inputVariables = cms.vstring("nHitsMissingOuter", "isPassMuonLooseID"), 
            ),
        cms.PSet (
            name  = cms.string("trackIsPassMuonLooseIDVsPt"),  
            title = cms.string("isPassMuonLooseIDVsPt; track p_{T} [GeV]; isPassMuonLooseID"), 
            bins = cms.untracked.vdouble(20, 0, 200, 2, -0.5, 1.5), 
            inputVariables = cms.vstring("pt", "isPassMuonLooseID"), 
            ),
        cms.PSet (
            name  = cms.string("trackIsPassMuonLooseIDVsEta"),  
            title = cms.string("isPassMuonLooseIDVsEta; track #eta; isPassMuonLooseID"), 
            bins = cms.untracked.vdouble(10, -2.5, 2.5, 2, -0.5, 1.5), 
            inputVariables = cms.vstring("eta", "isPassMuonLooseID"), 
            ),  
        cms.PSet (
            name = cms.string("trackCaloEMDeltaRp5"),
            title = cms.string("caloEMDeltaRp5; EM Calo Energy (dR < 0.5)"),
            bins = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloEMDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloHadDeltaRp5"),
            title = cms.string("caloHadDeltaRp5; Hadronic Calo Energy (dR < 0.5)"),
            bins = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloHadDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTot"),
            title = cms.string("Isolation energy; E_{calo}^{#DeltaR<0.5} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotVsNPV"),
            title = cms.string("Isolation energy (no PU corr) vs. Num. PV; # Primary vertices;E_{calo}^{#DeltaR<0.5} [GeV]"),
            bins = cms.untracked.vdouble(50, 0, 50, 100, 0, 100),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByP"),
            title = cms.string("Isolation energy / p; E_{calo}^{#DeltaR<0.5}/p"),
            bins = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTot_RhoCorr"),
            title = cms.string("Isolation energy (PU corr.); E_{calo}^{#DeltaR<0.5} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTot_RhoCorrVsNPV"),
            title = cms.string("Isolation energy (PU corr.) vs. Num. PV; # Primary vertices;E_{calo}^{#DeltaR<0.5} [GeV]"),
            bins = cms.untracked.vdouble(50, 0, 50, 100, 0, 100),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByP_RhoCorr"),
            title = cms.string("Isolation energy / p (PU corr.); E_{calo}^{#DeltaR<0.5}/p"),
            bins = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByPRhoCorr"),
            ),
         cms.PSet (
             name = cms.string("trackCaloTot_RhoCorrWide"),
             title = cms.string("Isolation energy (PU corr.); E_{calo}^{#DeltaR<0.5} [GeV]"),
             bins = cms.untracked.vdouble(100, 0, 400),
             inputVariables = cms.vstring("caloTotDeltaRp5RhoCorr"),
             ),
        cms.PSet (
            name = cms.string("trackCaloTotByP_RhoCorrWide"),
            title = cms.string("Isolation energy / p (PU corr.); E_{calo}^{#DeltaR<0.5}/p"),
            bins = cms.untracked.vdouble(100, 0, 6),
            inputVariables = cms.vstring("caloTotDeltaRp5ByPRhoCorr"),
            ),

        cms.PSet (
            name = cms.string("trackPtError"),
            title = cms.string("ptError; #sigma(p_{T}) [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("ptError"),
            ),
        cms.PSet (
            name = cms.string("trackPtErrorByPt"),
            title = cms.string("ptErrorByPt; #sigma(p_{T})/p_{T}"),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("ptErrorByPt"),
            ),
        cms.PSet (
            name = cms.string("trackPtRes"),
            title = cms.string("ptRes; (p_{T}-p_{T}^{true})/p_{T}^{true}"),
            bins = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring("ptRes"),
            ),
        cms.PSet (
            name = cms.string("trackPtTrue"),
            title = cms.string("ptTrue; p_{T}^{true}"),
            bins = cms.untracked.vdouble(100, 0, 150),
            inputVariables = cms.vstring("ptTrue"),
            ),
        
        cms.PSet (
            name = cms.string("trackChi2vsPtErrorByPt"),
            title = cms.string("chi2vsPtErrorByPt; #chi^{2}/DOF;#sigma(p_{T})/p_{T}"),
            bins = cms.untracked.vdouble(100, 0, 7, 100, 0, 1),
            inputVariables = cms.vstring("normChi2","ptErrorByPt"),
            ),

        cms.PSet (
            name = cms.string("trackChi2vsPtRes"),
            title = cms.string("chi2vsPtRes; #chi^{2}/DOF; (p_{T}-p_{T}^{true})/p_{T}^{true}"),
            bins = cms.untracked.vdouble(100, 0, 7, 100, -10, 10),
            inputVariables = cms.vstring("normChi2","ptRes"),
            ),
        cms.PSet (
            name = cms.string("trackGenDeltaRLowest"),
            title = cms.string("genDeltaRLowest; #Delta R_{min.}"),
            bins = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("genDeltaRLowest"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRMinElecLooseMvaId"),
            title = cms.string("deltaRMinElecLooseMvaId; deltaRMinElecLooseMvaId"),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRMinElecLooseMvaId"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRMinMuonLooseId"),
            title = cms.string("deltaRMinMuonLooseId; deltaRMinMuonLooseId"),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRMinMuonLooseId"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRMinSecMuonLooseId"),
            title = cms.string("deltaRMinSecMuonLooseId; deltaRMinSecMuonLooseId"),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRMinSecMuonLooseId"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRMinTauLooseHadronicId"),
            title = cms.string("deltaRMinTauLooseHadronicId; deltaRMinTauLooseHadronicId"),
            bins = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRMinTauLooseHadronicId"),
            ),

        
        )
    )

#for bkgd estimation
TrackPtHistograms = cms.PSet(
        inputCollection = cms.string("tracks"),
        histograms = cms.VPSet (
    
        cms.PSet (
            name = cms.string("trackNHitsVsCaloPt20"),
            title = cms.string("NHitsVsCaloPt20; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (20 GeV < pT < 50 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 2 ),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsVsCaloPt50"),
            title = cms.string("NHitsVsCaloPt50; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (50 GeV < pT < 75 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
                                                ),
        cms.PSet (
            name = cms.string("trackNHitsVsCaloPt75"),
            title = cms.string("NHitsVsCaloPt75; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (75 GeV < pT < 100 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),

        cms.PSet (
            name = cms.string("trackNHitsVsCaloPt100"),
            title = cms.string("NHitsVsCaloPt100; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (100 GeV < pT < 125 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
                                                                ),
        cms.PSet (
            name = cms.string("trackNHitsVsCaloPt125"),
            title = cms.string("NHitsVsCaloPt125; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (125 GeV < pT)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),

        cms.PSet (
            name = cms.string("trackNHitsVsCaloTotPt20"),
            title = cms.string("NHitsVsCaloTotPt20; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (20 GeV < pT < 50 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsVsCaloTotPt50"),
            title = cms.string("NHitsVsCaloTotPt50; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (50 GeV < pT < 75 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsVsCaloTotPt75"),
            title = cms.string("NHitsVsCaloTotPt75; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (75 GeV < pT < 100 GeV))"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),

        cms.PSet (
            name = cms.string("trackNHitsVsCaloTotPt100"),
            title = cms.string("NHitsVsCaloTotPt100; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (100 GeV < pT < 125 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsVsCaloTotPt125"),
            title = cms.string("NHitsVsCaloTotPt125; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (125 GeV < pT)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        
        cms.PSet (
            name = cms.string("trackNHitsVsPtErrorPt20"),
            title = cms.string("NHitsVsPtErrorPt20; Missing Outer Hits ; pT_{error} (20 GeV < pT < 50 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100 ),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
                                            ),
        cms.PSet (
            name = cms.string("trackNHitsVsPtErrorPt50"),
            title = cms.string("NHitsVsPtErrorPt50; Missing Outer Hits ; pT_{error} (50 GeV < pT < 75 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsVsPtErrorPt75"),
            title = cms.string("NHitsVsPtErrorPt75; Missing Outer Hits ; pT_{error} (75 GeV < pT < 100 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),

        cms.PSet (
            name = cms.string("trackNHitsVsPtErrorPt100"),
            title = cms.string("NHitsVsPtErrorPt100; Missing Outer Hits ; pT_{error} (100 GeV < pT < 125 GeV)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsVsPtErrorPt125"),
            title = cms.string("NHitsVsPtErrorPt125; Missing Outer Hits ; pT_{error} (125 GeV < pT)"),
            bins = cms.untracked.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        
    )
)



JetExtraHistograms = cms.PSet(
    inputCollection = cms.string("jets"),
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
    )
)

MetExtraHistograms = cms.PSet(
    inputCollection = cms.string("mets"),
    histograms = cms.VPSet (
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
            title = cms.string("deltaPhiMin2Jets;#Delta#phi_{min}^{met-jet}"),
            bins = cms.untracked.vdouble(100, 0, 3.15),  
            inputVariables = cms.vstring("deltaPhiMin2Jets"),
            ),


        
        )
    )

SecJetExtraHistograms = cms.PSet(
    inputCollection = cms.string("secondary jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("secJetChargedEmEnergyFraction"),
            title = cms.string("Jet Charged EM Energy Fraction;Jet Charged EM Energy Fraction"),
            bins = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("chargedEmEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("secJetChargedHadronEnergyFraction"),
            title = cms.string("Jet Charged Hadron Energy Fraction;Jet Charged Hadron Energy Fraction"),
            bins = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("chargedHadronEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("secJetNeutralEmEnergyFraction"),
            title = cms.string("Jet Neutral EM Energy Fraction;Jet Neutral EM Energy Fraction"),
            bins = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("neutralEmEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("secJetNeutralHadronEnergyFraction"),
            title = cms.string("Jet Neutral Hadron Energy Fraction;Jet Neutral Hadron Energy Fraction"), 
            bins = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("neutralHadronEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("secJetDeltaPhiMet"),
            title = cms.string("Jet #Delta #phi E^{miss}_{T};Jet #Delta #phi E^{miss}_{T}"), 
            bins = cms.untracked.vdouble(70, -3.5, 3.5),
            inputVariables = cms.vstring("dPhiMet"),
            ),
    )
)


## DiJetHistograms = cms.PSet(
##     inputCollection = cms.string("jet-jet pairs"),
##     histograms = cms.VPSet (
##         cms.PSet (
##             name = cms.string("dijetDeltaPhi"),
##             title = cms.string("Jet-jet #Delta#Phi"),
##             bins = cms.untracked.vdouble(100, 0, 3.15),   
##             inputVariables = cms.vstring("deltaPhi"),
##             ),
##     )
## )  




DebugHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackPt"),
            title = cms.string("Track Transverse Momentum; p_{T} [GeV]"),
            bins = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
        ),
    )
)



