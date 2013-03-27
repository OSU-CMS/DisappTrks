import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################


ExtraMuonHistograms = cms.PSet(
    inputCollection = cms.string("muon-muon pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("invMassMuons"),
            title = cms.string("invMassMuons"),
            bins = cms.vdouble(100, 0, 180),
            inputVariables = cms.vstring("invMass"),
            ),
        )
    )
ExtraElectronHistograms = cms.PSet(
    inputCollection = cms.string("electron-electron pairs"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("invMassElectrons"),
            title = cms.string("invMassElectrons"),
            bins = cms.vdouble(100, 0, 180),
            inputVariables = cms.vstring("invMass"),
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
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5_RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("caloTotByPVsNumPV_RhoCorr"),
            title = cms.string("Isolation energy / p (PU corr.) vs. num. primary vertices; number of primary vertices; E_{iso}^{#DeltaR<0.5}/p (PU corr.)"),
            bins = cms.vdouble(51, -0.5, 50.5, 100, 0, 2),
            inputVariables = cms.vstring("numPV", "caloTotDeltaRp5ByP_RhoCorr"),
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
            inputVariables = cms.vstring("caloTotDeltaRp5_RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("caloTotByP_RhoCorr"),
            title = cms.string("Isolation energy / p (PU corr.); E_{iso}^{#DeltaR<0.5}/p (PU corr.)"),
            bins = cms.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByP_RhoCorr"),
            ),
    )
)


ExtraTrackHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("d0wrtBS"),
            title = cms.string("d0wrtBS"),
            bins = cms.vdouble(100, -1, 1),
            inputVariables = cms.vstring("d0wrtBS"),
                        ),

        cms.PSet (
            name = cms.string("dZwrtBS"),
            title = cms.string("dZwrtBS"),
            bins = cms.vdouble(100, -20, 20),
            inputVariables = cms.vstring("dZwrtBS"),
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
            name = cms.string("caloTotDeltaRp5"),
            title = cms.string("caloTotDeltaRp5; Total Calo Energy (dR < 0.5)"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5"),
        ),

        cms.PSet (
            name = cms.string("caloTotDeltaRp5ByP"),
            title = cms.string("caloTotDeltaRp5ByP; (Total Calo Energy)/p (dR < 0.5)"),
            bins = cms.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("caloTotDeltaRp5_RhoCorr"),
            title = cms.string("caloTotDeltaRp5_RhoCorr; Total Calo Energy (dR < 0.5) (PU corr.)"),
            bins = cms.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotDeltaRp5_RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("caloTotDeltaRp5ByP_RhoCorr"),
            title = cms.string("caloTotDeltaRp5ByP_RhoCorr; (Total Calo Energy)/p (dR < 0.5) (PU corr.)"),
            bins = cms.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloTotDeltaRp5ByP_RhoCorr"),
            ),
        cms.PSet (
            name = cms.string("ptError"),
            title = cms.string("ptError; pT Error"),
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
            title = cms.string("ptRes; ptRes"),
            bins = cms.vdouble(100, 0, 50),
            inputVariables = cms.vstring("ptRes"),
            ),

        cms.PSet (
            name = cms.string("chi2vsPtErrorByPt"),
            title = cms.string("chi2vsPtErrorByPt; chi2vsPtErrorByPt"),
            bins = cms.vdouble(100, 0, 7, 100, 0, 1),
            inputVariables = cms.vstring("normChi2","ptErrorByPt"),
            ),

        cms.PSet (
            name = cms.string("chi2vsPtRes"),
            title = cms.string("chi2vsPtRes; chi2vsPtRes"),
            bins = cms.vdouble(100, 0, 7, 100, 0, 50),
            inputVariables = cms.vstring("normChi2","ptRes"),
            ),
        cms.PSet (
            name = cms.string("genDeltaRLowest"),
            title = cms.string("genDeltaRLowest"),
            bins = cms.vdouble(100, 0, 5),
            inputVariables = cms.vstring("genDeltaRLowest"),
            ),
        
            
#for bkgd estimation
        cms.PSet (
            name = cms.string("NHitsVsCaloPt20"),
            title = cms.string("NHitsVsCaloPt20; Missing Outer Hits ; Total Calo/p (20)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2 ),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloPt50"),
            title = cms.string("NHitsVsCaloPt50; Missing Outer Hits ; Total Calo/p (50)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
                                                ),
        cms.PSet (
            name = cms.string("NHitsVsCaloPt75"),
            title = cms.string("NHitsVsCaloPt75; Missing Outer Hits ; Total Calo/p (75)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloPt100"),
            title = cms.string("NHitsVsCaloPt100; Missing Outer Hits ; Total Calo/p (100)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
                                                                ),
        cms.PSet (
            name = cms.string("NHitsVsCaloPt125"),
            title = cms.string("NHitsVsCaloPt125; Missing Outer Hits ; Total Calo/p (125)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt20"),
            title = cms.string("NHitsVsCaloTotPt20; Missing Outer Hits ; Total Calo (20)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt50"),
            title = cms.string("NHitsVsCaloTotPt50; Missing Outer Hits ; Total Calo (50)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt75"),
            title = cms.string("NHitsVsCaloTotPt75; Missing Outer Hits ; Total Calo (75)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt100"),
            title = cms.string("NHitsVsCaloTotPt100; Missing Outer Hits ; Total Calo (100)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt125"),
            title = cms.string("NHitsVsCaloTotPt125; Missing Outer Hits ; Total Calo (125)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        
        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt20"),
            title = cms.string("NHitsVsPtErrorPt20; Missing Outer Hits ; Pt Error (20)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100 ),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
                                            ),
        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt50"),
            title = cms.string("NHitsVsPtErrorPt50; Missing Outer Hits ; Pt Error (50)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt75"),
            title = cms.string("NHitsVsPtErrorPt75; Missing Outer Hits ; Pt Error (75)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt100"),
            title = cms.string("NHitsVsPtErrorPt100; Missing Outer Hits ; Pt Error (100)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt125"),
            title = cms.string("NHitsVsPtErrorPt125; Missing Outer Hits ; Pt Error (125)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 100),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        
        
        

    )
)

