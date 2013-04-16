import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################


DiMuonHistograms = cms.PSet(
    inputCollection = cms.string("muon-muon pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diMuonInvMass"),
            title = cms.string("Di-Muon Invariant Mass; M_{#mu#mu} [GeV]"),
            bins = cms.vdouble(100, 0, 180),
            inputVariables = cms.vstring("invMass"),
            ),
        cms.PSet (
            name = cms.string("diMuonChargeProduct"),
            title = cms.string("Di-muon Charge Product; charge_{#mu}_{1}*charge_{#mu}_{2}"),
            bins = cms.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("chargeProduct"),
            ),
        cms.PSet (
            name = cms.string("diMuonDeltaEta"),
            title = cms.string("Di-muon Eta Difference; |#Delta(#eta)|"),
            bins = cms.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaEta"),
            ),
        cms.PSet (
            name = cms.string("diMuonDeltaPhi"),
            title = cms.string("Di-muon Phi Difference; |#Delta(#phi)|"),
            bins = cms.vdouble(1000, 0, 3.14),
            inputVariables = cms.vstring("deltaPhi"),
            ),
        cms.PSet (
            name = cms.string("diMuonDeltaR"),
            title = cms.string("Di-muon #DeltaR; #DeltaR"),
            bins = cms.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaR"),
            ),
        
        )
    )
DiTauHistograms = cms.PSet(
    inputCollection = cms.string("tau-tau pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diTauInvMass"),
            title = cms.string("Di-Tau Invariant Mass; M_{#tau#tau} [GeV]"),
            bins = cms.vdouble(100, 0, 180),
            inputVariables = cms.vstring("invMass"),
            ),
        cms.PSet (
            name = cms.string("diTauDeltaEta"),
            title = cms.string("Di-tau Eta Difference; |#Delta(#eta)|"),
            bins = cms.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaEta"),
            ),
        cms.PSet (
            name = cms.string("diTauDeltaPhi"),
            title = cms.string("Di-tau Phi Difference; |#Delta(#phi)|"),
            bins = cms.vdouble(1000, 0, 3.14),
            inputVariables = cms.vstring("deltaPhi"),
                            ),
        cms.PSet (
            name = cms.string("diTauDeltaR"),
            title = cms.string("Di-tau #DeltaR; #DeltaR"),
            bins = cms.vdouble(1000, 0, 10),
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
            bins = cms.vdouble(100, 0, 180),
            inputVariables = cms.vstring("invMass"),
            ),
        cms.PSet (
            name = cms.string("diElectronDeltaEta"),
            title = cms.string("Di-electron Eta Difference; |#Delta(#eta)|"),
            bins = cms.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaEta"),
            ),
        cms.PSet (
            name = cms.string("diElectronDeltaPhi"),
            title = cms.string("Di-electron Phi Difference; |#Delta(#phi)|"),
            bins = cms.vdouble(1000, 0, 3.14),
            inputVariables = cms.vstring("deltaPhi"),
            ),
        cms.PSet (
            name = cms.string("diElectronDeltaR"),
            title = cms.string("Di-electron #DeltaR; #DeltaR"),
            bins = cms.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaR"),
            ),
        
        )
    )

ElectronTrackHistograms = cms.PSet(
        inputCollection = cms.string("electron-track pairs"),
        histograms = cms.VPSet (
             cms.PSet (
                 name = cms.string("ElectronTrackInvMass"),
                 title = cms.string("Electron-Track Invariant Mass; M_{e+track} [GeV]"),
                 bins = cms.vdouble(100, 0, 180),
                 inputVariables = cms.vstring("invMass"),
                 ),
             cms.PSet (
                 name = cms.string("ElectronTrackDeltaEta"),
                 title = cms.string("Electron-Track Eta Difference; |#Delta(#eta)|"),
                 bins = cms.vdouble(1000, 0, 10),
                 inputVariables = cms.vstring("deltaEta"),
                 ),
             cms.PSet (
                name = cms.string("ElectronTrackDeltaPhi"),
                title = cms.string("Electron-Track Phi Difference; |#Delta(#phi)|"),
                bins = cms.vdouble(1000, 0, 3.14),
                inputVariables = cms.vstring("deltaPhi"),
                ),
             cms.PSet (
                name = cms.string("ElectronTrackDeltaR"),
                title = cms.string("Electron-Track #DeltaR; #DeltaR"),
                bins = cms.vdouble(1000, 0, 10),
                inputVariables = cms.vstring("deltaR"),
                ),
             
             
             )
        )

MuonTrackHistograms = cms.PSet(
    inputCollection = cms.string("muon-track pairs"),
    histograms = cms.VPSet (
         cms.PSet (
             name = cms.string("MuonTrackInvMass"),
             title = cms.string("Muon-Track Invariant Mass; M_{#mu+track} [GeV]"),
             bins = cms.vdouble(100, 0, 180),
             inputVariables = cms.vstring("invMass"),
             ),
         cms.PSet (
             name = cms.string("MuonTrackDeltaEta"),
             title = cms.string("Muon-Track Eta Difference; |#Delta(#eta)|"),
             bins = cms.vdouble(1000, 0, 10),
             inputVariables = cms.vstring("deltaEta"),
             ),
         cms.PSet (
             name = cms.string("MuonTrackDeltaPhi"),
             title = cms.string("Muon-Track Phi Difference; |#Delta(#phi)|"),
             bins = cms.vdouble(1000, 0, 3.14),
             inputVariables = cms.vstring("deltaPhi"),
             ),
         cms.PSet (
             name = cms.string("MuonTrackDeltaR"),
             title = cms.string("Muon-Track #DeltaR; #DeltaR"),
             bins = cms.vdouble(1000, 0, 10),
             inputVariables = cms.vstring("deltaR"),
             ),
         
         
         )
    )

MuonTauHistograms = cms.PSet(
    inputCollection = cms.string("muon-tau pairs"),
    histograms = cms.VPSet (
         cms.PSet (
             name = cms.string("MuonTauInvMass"),
             title = cms.string("Muon-Tau Invariant Mass; M_{#mu#tau} [GeV]"),
             bins = cms.vdouble(100, 0, 180),
             inputVariables = cms.vstring("invMass"),
             ),
         cms.PSet (
             name = cms.string("MuonTauDeltaEta"),
             title = cms.string("Muon-Tau Eta Difference; |#Delta(#eta)|"),
             bins = cms.vdouble(1000, 0, 10),
             inputVariables = cms.vstring("deltaEta"),
             ),
         cms.PSet (
             name = cms.string("MuonTauDeltaPhi"),
             title = cms.string("Muon-Tau Phi Difference; |#Delta(#phi)|"),
             bins = cms.vdouble(1000, 0, 3.14),
             inputVariables = cms.vstring("deltaPhi"),
             ),
         cms.PSet (
             name = cms.string("MuonTauDeltaR"),
             title = cms.string("Muon-Tau #DeltaR; #DeltaR"),
             bins = cms.vdouble(1000, 0, 10),
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
            bins = cms.vdouble(100, 0, 500),
            inputVariables = cms.vstring("pt"),
            ),
        cms.PSet (
            name = cms.string("trackEta"),
            title = cms.string("Track Eta; #eta"),
            bins = cms.vdouble(100, -5, 5),
            inputVariables = cms.vstring("eta"),
            ),
        cms.PSet (
            name = cms.string("trackPhi"),
            title = cms.string("Track Phi; #phi"),
            bins = cms.vdouble(100, -5, 5),
            inputVariables = cms.vstring("phi"),
            ),
    )
)  # end ShortTrackHistograms
 



TestEventHistograms = cms.PSet(
    inputCollection = cms.string("events"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("NumberOfPrimaryVertices"),
            title = cms.string("numPV; number of primary vertices"),
            bins = cms.vdouble(51, -0.5, 50.5),
            inputVariables = cms.vstring("numPV"),
            ),
    )
)


TestTrackEventHistograms = cms.PSet(
    inputCollection = cms.string("track-event pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("caloTotVsNumPV"),
            title = cms.string("Isolation energy vs. num. primary vertices; number of primary vertices; E_{iso}^{#DeltaR<0.5}"),
            bins = cms.vdouble(51, -0.5, 50.5, 100, 0, 100),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("caloTotByPVsNumPV"),
            title = cms.string("Isolation energy / p vs. num. primary vertices; number of primary vertices; E_{iso}^{#DeltaR<0.5}/p"),
            bins = cms.vdouble(51, -0.5, 50.5, 100, 0, 2),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("caloTotVsNumPV_RhoCorr"),
            title = cms.string("Isolation energy (PU corr.) vs. num. primary vertices; number of primary vertices; E_{iso}^{#DeltaR<0.5} (PU corr.)"),
            bins = cms.vdouble(51, -0.5, 50.5, 100, 0, 100),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("caloTotByPVsNumPV_RhoCorr"),
            title = cms.string("Isolation energy / p (PU corr.) vs. num. primary vertices; number of primary vertices; E_{iso}^{#DeltaR<0.5}/p (PU corr.)"),
            bins = cms.vdouble(51, -0.5, 50.5, 100, 0, 2),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5ByPRhoCorr"),
            ),
    )
)



TestTrackHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("caloTot"),
            title = cms.string("Isolation energy; E_{iso}^{#DeltaR<0.5}"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("caloTotByP"),
            title = cms.string("Isolation energy / p; E_{iso}^{#DeltaR<0.5}/p"),
            bins = cms.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("caloTot_RhoCorr"),
            title = cms.string("Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5} (PU corr.)"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("caloTotByP_RhoCorr"),
            title = cms.string("Isolation energy / p (PU corr.); E_{iso}^{#DeltaR<0.5}/p (PU corr.)"),
            bins = cms.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByPRhoCorr"),
            ),
    )
)


ExtraTrackHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("d0wrtBS"),
            title = cms.string("Track d_{0} wrt BS; d_{0} wrt BS (cm)"),
            bins = cms.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("d0wrtBS"),
            ),
        cms.PSet (
            name = cms.string("dZwrtBS"),
            title = cms.string("Track d_{z} wrt BS; d_{z} wrt BS (cm)"),
            bins = cms.vdouble(100, -20, 20),
            inputVariables = cms.vstring("dZwrtBS"),
            ),
        cms.PSet (
            name = cms.string("d0wrtPV"),
            title = cms.string("Track d_{0} wrt PV; d_{0} wrt PV (cm)"),
            bins = cms.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring("d0wrtPV"),
            ),
        cms.PSet (
            name = cms.string("dZwrtPV"),
            title = cms.string("Track d_{z} wrt PV; d_{z} wrt PV (cm)"),
            bins = cms.vdouble(2000, -10, 10),
            inputVariables = cms.vstring("dZwrtPV"),
            ),       
        cms.PSet (
            name = cms.string("nHitsMissingOuter"),
            title = cms.string("nHitsMissingOuter; Number of Missing Outer Hits"),
            bins = cms.vdouble(100, 0, 15),
            inputVariables = cms.vstring("nHitsMissingOuter"),
            ),
        cms.PSet (
            name = cms.string("nHitsMissingMiddle"),
            title = cms.string("nHitsMissingMiddle; Number of Missing Middle Hits"),
            bins = cms.vdouble(100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingMiddle"),
            ),
        cms.PSet (
            name = cms.string("nHitsMissingInner"),
            title = cms.string("nHitsMissingInner; Number of Missing Inner Hits"),
            bins = cms.vdouble(100, 0, 5),
            inputVariables = cms.vstring("nHitsMissingInner"),
            ),
        cms.PSet (
            name = cms.string("nTracksRp5"),
            title = cms.string("nTracksRp5; nTracksRp5"),
            bins = cms.vdouble(100, 0, 15),
            inputVariables = cms.vstring("nTracksRp5"),
            ),
        cms.PSet (
            name = cms.string("depTrkRp5"),
            title = cms.string("depTrkRp5; depTrkRp5"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("depTrkRp5"),
            ),
        cms.PSet (
            name = cms.string("caloEMDeltaRp5"),
            title = cms.string("caloEMDeltaRp5; EM Calo Energy (dR < 0.5)"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloEMDeltaRp5"),
        ),
        cms.PSet (
            name = cms.string("caloHadDeltaRp5"),
            title = cms.string("caloHadDeltaRp5; Hadronic Calo Energy (dR < 0.5)"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloHadDeltaRp5"),
        ),
        cms.PSet (
            name = cms.string("caloTot"),
            title = cms.string("Isolation energy; E_{iso}^{#DeltaR<0.5} (GeV)"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("caloTotByP"),
            title = cms.string("Isolation energy / p; E_{iso}^{#DeltaR<0.5}/p"),
            bins = cms.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("caloTot_RhoCorr"),
            title = cms.string("Isolation energy (PU corr.); E_{iso}^{#DeltaR<0.5} (GeV) (PU corr.)"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("caloTotByP_RhoCorr"),
            title = cms.string("Isolation energy / p (PU corr.); E_{iso}^{#DeltaR<0.5}/p (PU corr.)"),
            bins = cms.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByPRhoCorr"),
            ),

        cms.PSet (
            name = cms.string("ptError"),
            title = cms.string("ptError; pT Error [GeV]"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("ptError"),
            ),
        cms.PSet (
            name = cms.string("ptErrorByPt"),
            title = cms.string("ptErrorByPt; pTError/pT"),
            bins = cms.vdouble(100, 0, 1),
            inputVariables = cms.vstring("ptErrorByPt"),
            ),
        cms.PSet (
            name = cms.string("ptRes"),
            title = cms.string("ptRes; (pT-pT_{true})/pT_{true}"),
            bins = cms.vdouble(100, 0, 50),
            inputVariables = cms.vstring("ptRes"),
            ),

        cms.PSet (
            name = cms.string("chi2vsPtErrorByPt"),
            title = cms.string("chi2vsPtErrorByPt; #chi^{2}/DOF;pT_{error}/pT"),
            bins = cms.vdouble(100, 0, 7, 100, 0, 1),
            inputVariables = cms.vstring("normChi2","ptErrorByPt"),
            ),

        cms.PSet (
            name = cms.string("chi2vsPtRes"),
            title = cms.string("chi2vsPtRes; #chi^{2}/DOF; (pT-pT_{true})/pT_{true}"),
            bins = cms.vdouble(100, 0, 7, 100, 0, 50),
            inputVariables = cms.vstring("normChi2","ptRes"),
            ),
        cms.PSet (
            name = cms.string("genDeltaRLowest"),
            title = cms.string("genDeltaRLowest"),
            bins = cms.vdouble(100, 0, 5),
            inputVariables = cms.vstring("genDeltaRLowest"),
            ),
        )
    )

#for bkgd estimation
TrackPtHistograms = cms.PSet(
        inputCollection = cms.string("tracks"),
        histograms = cms.VPSet (
    
        cms.PSet (
            name = cms.string("NHitsVsCaloPt20"),
            title = cms.string("NHitsVsCaloPt20; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (20 GeV < pT < 50 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2 ),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloPt50"),
            title = cms.string("NHitsVsCaloPt50; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (50 GeV < pT < 75 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
                                                ),
        cms.PSet (
            name = cms.string("NHitsVsCaloPt75"),
            title = cms.string("NHitsVsCaloPt75; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (75 GeV < pT < 100 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloPt100"),
            title = cms.string("NHitsVsCaloPt100; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (100 GeV < pT < 125 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
                                                                ),
        cms.PSet (
            name = cms.string("NHitsVsCaloPt125"),
            title = cms.string("NHitsVsCaloPt125; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5}/p (125 GeV < pT)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt20"),
            title = cms.string("NHitsVsCaloTotPt20; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (20 GeV < pT < 50 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt50"),
            title = cms.string("NHitsVsCaloTotPt50; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (50 GeV < pT < 75 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt75"),
            title = cms.string("NHitsVsCaloTotPt75; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (75 GeV < pT < 100 GeV))"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt100"),
            title = cms.string("NHitsVsCaloTotPt100; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (100 GeV < pT < 125 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt125"),
            title = cms.string("NHitsVsCaloTotPt125; Missing Outer Hits ; E_{iso}^{#DeltaR<0.5} (125 GeV < pT)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        
        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt20"),
            title = cms.string("NHitsVsPtErrorPt20; Missing Outer Hits ; pT_{error} (20 GeV < pT < 50 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100 ),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
                                            ),
        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt50"),
            title = cms.string("NHitsVsPtErrorPt50; Missing Outer Hits ; pT_{error} (50 GeV < pT < 75 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt75"),
            title = cms.string("NHitsVsPtErrorPt75; Missing Outer Hits ; pT_{error} (75 GeV < pT < 100 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt100"),
            title = cms.string("NHitsVsPtErrorPt100; Missing Outer Hits ; pT_{error} (100 GeV < pT < 125 GeV)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt125"),
            title = cms.string("NHitsVsPtErrorPt125; Missing Outer Hits ; pT_{error} (125 GeV < pT)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        
        
        

    )
)

