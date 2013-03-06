import FWCore.ParameterSet.Config as cms


###############################################
##### Set up the histograms to be plotted #####
###############################################


ExtraTrackHistograms = cms.PSet(
    inputCollection = cms.string("tracks"),
    histograms = cms.VPSet (
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
        

    )
)

