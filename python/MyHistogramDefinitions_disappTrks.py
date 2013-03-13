import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################


ExtraTrackHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("nHitsMissingOuter"),
            title = cms.string("nHitsMissingOuter; Number of Missing Outer Hits"),
            bins = cms.vdouble(100, 0, 20),
            inputVariables = cms.vstring("nHitsMissingOuter"),
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
            name = cms.string("ptError"),
            title = cms.string("ptError; pT Error"),
            bins = cms.vdouble(100, 0, 2),
            inputVariables = cms.vstring("ptError"),
            ),
#for bkgd estimation
        cms.PSet (
            name = cms.string("NHitsVsCaloPt20"),
            title = cms.string("NHitsVsCaloPt20; Number of Valid Hits ; Total Calo/p (20)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2 ),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloPt50"),
            title = cms.string("NHitsVsCaloPt50; Number of Valid Hits ; Total Calo/p (50)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
                                                ),
        cms.PSet (
            name = cms.string("NHitsVsCaloPt75"),
            title = cms.string("NHitsVsCaloPt75; Number of Valid Hits ; Total Calo/p (75)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloPt100"),
            title = cms.string("NHitsVsCaloPt100; Number of Valid Hits ; Total Calo/p (100)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
                                                                ),
        cms.PSet (
            name = cms.string("NHitsVsCaloPt125"),
            title = cms.string("NHitsVsCaloPt125; Number of Valid Hits ; Total Calo/p (125)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5ByP"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt20"),
            title = cms.string("NHitsVsCaloTotPt20; Number of Valid Hits ; Total Calo (20)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2 ),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt50"),
            title = cms.string("NHitsVsCaloTotPt50; Number of Valid Hits ; Total Calo (50)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt75"),
            title = cms.string("NHitsVsCaloTotPt75; Number of Valid Hits ; Total Calo (75)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt100"),
            title = cms.string("NHitsVsCaloTotPt100; Number of Valid Hits ; Total Calo (100)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt125"),
            title = cms.string("NHitsVsCaloTotPt125; Number of Valid Hits ; Total Calo (125)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","caloTotDeltaRp5"),
            ),
        
        cms.PSet (
            name = cms.string("NHitsVsPtErrorPt20"),
            title = cms.string("NHitsVsCaloTotPt20; Number of Valid Hits ; Total Calo (20)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2 ),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
                                            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt50"),
            title = cms.string("NHitsVsCaloTotPt50; Number of Valid Hits ; Total Calo (50)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt75"),
            title = cms.string("NHitsVsCaloTotPt75; Number of Valid Hits ; Total Calo (75)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),

        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt100"),
            title = cms.string("NHitsVsCaloTotPt100; Number of Valid Hits ; Total Calo (100)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        cms.PSet (
            name = cms.string("NHitsVsCaloTotPt125"),
            title = cms.string("NHitsVsCaloTotPt125; Number of Valid Hits ; Total Calo (125)"),
            bins = cms.vdouble(100, 0, 15, 100, 0, 2),
            inputVariables = cms.vstring("nHitsMissingOuter","ptError"),
            ),
        
        
        

    )
)

