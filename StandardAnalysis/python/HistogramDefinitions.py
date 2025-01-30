import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.utilities import *
from OSUT3Analysis.Configuration.pdgIdBins import *
from OSUT3Analysis.Configuration.cutUtilities import *

###############################################
##### Set up the histograms to be plotted #####
###############################################

metBins = cms.untracked.vdouble(2000, 0.0, 10000.0)
metBinsSlimmed = cms.untracked.vdouble(500, 0.0, 2500.0)
deltaPhiBins = cms.untracked.vdouble(64, 0.0, 3.2)

TrackDebugEcaloHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("trackCaloNew_RhoCorr"),
            title = cms.string("Isolation energy (new calculation, PU corr.);E_{calo}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloNewNoPUDRp5CentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackCaloNewOldDiff"),
            title = cms.string("Isolation energy (new calculation - old calculation);E_{calo}^{#DeltaR<0.5} [GeV] new calc. - old calc."),
            binsX = cms.untracked.vdouble(100, -10, 100),
            inputVariables = cms.vstring("caloNewNoPUDRp5CentralCalo - caloTotNoPUDRp5CentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackCaloNewVsOld"),
            title = cms.string("Isolation energy (new vs. old);E_{calo}^{#DeltaR<0.5} [GeV] old calc.;E_{calo}^{#DeltaR<0.5} [GeV] new calc."),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloTotNoPUDRp5CentralCalo", "caloNewNoPUDRp5CentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackCaloEM"),
            title = cms.string("Relative EM isolation energy;E_{EM calo}^{#DeltaR<0.5}"),
            binsX = cms.untracked.vdouble(1000, 0, 50),
            inputVariables = cms.vstring("caloNewEMDRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloHad"),
            title = cms.string("Relative Hadronic isolation energy;E_{Had. calo}^{#DeltaR<0.5}"),
            binsX = cms.untracked.vdouble(1000, 0, 50),
            inputVariables = cms.vstring("caloNewHadDRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloNew_RhoCorr_fine"),
            title = cms.string("Isolation energy (new calculation, PU corr.);E_{calo}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0, 50),
            inputVariables = cms.vstring("caloNewNoPUDRp5CentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackRhoPUCorr"),
            title = cms.string("Track rho correction;Rho (all PF candidates) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0, 500),
            inputVariables = cms.vstring("rhoPUCorr"),
            ),
        cms.PSet (
            name = cms.string("trackRhoPUCorrCalo"),
            title = cms.string("Track rho correction;Rho (all calo towers) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0, 500),
            inputVariables = cms.vstring("rhoPUCorrCalo"),
            ),
        cms.PSet (
            name = cms.string("trackRhoPUCorrCentralCalo"),
            title = cms.string("Track rho correction;Rho (all calo towers |#eta| < 2.5) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0, 500),
            inputVariables = cms.vstring("rhoPUCorrCentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotVsRhoPUCorrCentralCalo"),
            title = cms.string("Isolation energy (new calculation) vs rhoPUCorrCentralCalo;Rho (all calo towers |#eta| < 2.5) [GeV];E_{calo}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            binsY = cms.untracked.vdouble(100, 0, 100),            
            inputVariables = cms.vstring("rhoPUCorrCentralCalo", "caloNewNoPUDRp5CentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotVsEta"),
            title = cms.string("Isolation energy (new calculation) vs #eta;Rho (all calo towers |#eta| < 2.5) [GeV];track #eta"),
            binsX = cms.untracked.vdouble(100, -5, 5),
            binsY = cms.untracked.vdouble(100, 0, 100),            
            inputVariables = cms.vstring("eta", "caloNewNoPUDRp5CentralCalo"),
            ),
    )
)

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
            name = cms.string("trackPtWider"),
            title = cms.string("Track Transverse Momentum;track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 10000),
            inputVariables = cms.vstring("pt"),
        ),
        cms.PSet (
            name = cms.string("trackIsolation"),
            title = cms.string("Relative Track Isolation;relative track isolation"),
            binsX = cms.untracked.vdouble(100, 0, 0.3),
            inputVariables = cms.vstring("trackIsoNoPUDRp3 / pt"),
            ),
        cms.PSet (
            name = cms.string("trackIsolationWithPU"),
            title = cms.string("Relative Track Isolation with PU;relative track isolation with PU"),
            binsX = cms.untracked.vdouble(100, 0, 0.3),
            inputVariables = cms.vstring("trackIsoDRp3 / pt"),
            ),
        cms.PSet (
            name = cms.string("trackIsolationNoPUVsWithPU"),
            title = cms.string("Relative Track Isolation;relative track isolation with PU;relative track isolation without PU"),
            binsX = cms.untracked.vdouble(100, 0, 0.3),
            binsY = cms.untracked.vdouble(100, 0, 0.3),
            inputVariables = cms.vstring("trackIsoDRp3 / pt", "trackIsoNoPUDRp3 / pt"),
            ),
        cms.PSet (
            name = cms.string("trackLayersWithMeasurementVsPixelHits"),
            title = cms.string(";number of pixel hits;number of tracker layers with measurement"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            binsY = cms.untracked.vdouble(20, -0.5, 19.5),
            inputVariables = cms.vstring("hitPattern_.numberOfValidPixelHits", "hitPattern_.trackerLayersWithMeasurement"),
            ),
        cms.PSet (
            name = cms.string("trackFitPlane"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};E_{calo}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("bestTrackMissingOuterHits", "caloNewNoPUDRp5CentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackFitPlaneWithCaloJet"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};matchedCaloJetEmEnergy+matchedCaloJetHadEnergy [GeV]"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("bestTrackMissingOuterHits", "matchedCaloJetEmEnergy + matchedCaloJetHadEnergy"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingOuter"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("bestTrackMissingOuterHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingOuterCorrected"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("hitAndTOBDrop_bestTrackMissingOuterHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsStripLayersVsTOBLayersVsMissingOuter"),
            title = cms.string(";N_{miss}^{outer};number of TOB layers with measurement;number of strip layers with measurement"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            binsZ = cms.untracked.vdouble(20, -0.5, 19.5),
            inputVariables = cms.vstring("bestTrackMissingOuterHits", "hitPattern_.stripTOBLayersWithMeasurement", "hitPattern_.stripLayersWithMeasurement"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsStripLayersVsMissingMiddle"),
            title = cms.string(";N_{miss}^{middle};number of strip layers with measurement"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            binsY = cms.untracked.vdouble(20, -0.5, 19.5),
            inputVariables = cms.vstring("missingMiddleHits", "hitPattern_.stripLayersWithMeasurement"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsExpectedTOBVsMissingOuter"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};N_{exp}^{TOB}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("bestTrackMissingOuterHits","expectedStripTOBHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsExpectedTIBVsMissingOuter"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};N_{exp}^{TIB}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("bestTrackMissingOuterHits","expectedStripTIBHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsObservedTOBVsMissingOuter"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};N_{obs}^{TOB}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("bestTrackMissingOuterHits","numberOfStripTOBHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsObservedTIBVsMissingOuter"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};N_{obs}^{TIB}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("bestTrackMissingOuterHits","numberOfStripTIBHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingMiddle"),
            title = cms.string("Number of Missing Middle Hits;N_{miss}^{middle}"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingMiddleHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingInner"),
            title = cms.string("Number of Missing Inner Hits;N_{miss}^{inner}"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingInnerHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingMiddleVsInner"),
            title = cms.string(";N_{miss}^{inner};N_{miss}^{middle}"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            binsY = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingInnerHits", "missingMiddleHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingMiddleCorrected"),
            title = cms.string("Number of Missing Middle Hits;N_{miss}^{middle}"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("hitDrop_missingMiddleHits"),
            ),
        cms.PSet (
            name = cms.string("trackNHitsMissingMiddleCorrectedVsInner"),
            title = cms.string(";N_{miss}^{inner};N_{miss}^{middle}"),
            binsX = cms.untracked.vdouble(6, -0.5, 5.5),
            binsY = cms.untracked.vdouble(6, -0.5, 5.5),
            inputVariables = cms.vstring("missingInnerHits", "hitDrop_missingMiddleHits"),
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
            inputVariables = cms.vstring("caloNewDRp5"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByP"),
            title = cms.string("Relative isolation energy;E_{calo}^{#DeltaR<0.5}/p (no PU corr.)"),
            binsX = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloNewDRp5 / p"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTot_RhoCorr"),
            title = cms.string("Isolation energy (PU corr.);E_{calo}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("caloNewNoPUDRp5CentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTot_RhoCorrWide"),
            title = cms.string("Isolation energy (PU corr.);E_{calo}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("caloNewNoPUDRp5CentralCalo"),
            ),
        cms.PSet (
            name = cms.string("trackCaloTotByP_RhoCorr"),
            title = cms.string("Relative isolation energy (PU corr.);E_{calo}^{#DeltaR<0.5}/p"),
            binsX = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("caloNewNoPUDRp5CentralCalo / p"),
            ),
        cms.PSet (
            name = cms.string("trackCaloJetEnergy"),
            title = cms.string("Isolation energy calculated using matchedCaloJetEmEnergy+matchedCaloJetHadEnergy"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("matchedCaloJetEmEnergy + matchedCaloJetHadEnergy"),
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
            name = cms.string("trackDeltaRToClosestElectron"),
            title = cms.string("deltaRMinElec;#DeltaR_{min}(track,electron)"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestElectron"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRToClosestVetoElectron"),
            title = cms.string("deltaRMinElecVetoId;#DeltaR_{min}(track,electron)"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestVetoElectron"),
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
            name = cms.string("trackDeltaRToClosestMuon"),
            title = cms.string("deltaRMinMuon;#DeltaR_{min}(track,muon)"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestMuon"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRToClosestLooseMuon"),
            title = cms.string("deltaRMinMuonLooseId;#DeltaR_{min}(track,muon)"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestLooseMuon"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRToClosestTau"),
            title = cms.string("deltaRMinTauLooseHadronicId;#DeltaR_{min}(track,tau)"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestTau"),
            ),
        cms.PSet (
            name = cms.string("trackDeltaRToClosestTauHad"),
            title = cms.string("deltaRMinTauLooseHadronicId;#DeltaR_{min}(track,tau)"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestTauHad"),
            ),
        cms.PSet (
            name = cms.string("trackDRMinJet"),
            title = cms.string("trackDRMinJet;#DeltaR_{min}(track,jet)"),
            binsX = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("dRMinJet"),
            ),
        cms.PSet (
            name = cms.string("genMatchedTauDecayProductFinalStateVsPromptFinalStateIsMatched"),
            title = cms.string(";track is matched to generator particle;track is matched to generator #tau decay product"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            binsY = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("genMatchedParticle.promptFinalState.isNonnull", "genMatchedParticle.directPromptTauDecayProductFinalState.isNonnull"),
        ),
        cms.PSet (
            name = cms.string("bestMatchPt"), # N.B. "bestMatch" changed to "promptOrTauDecay" but hist name remains
            title = cms.string(";p_{T} of matched generator particle [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticle.promptOrTauDecay.pt"),
        ),
        cms.PSet (
            name = cms.string("trackNHitsMissingOuterVsEta"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};track #eta"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(60, -3.0, 3.0),
            inputVariables = cms.vstring("bestTrackMissingOuterHits", "eta"),
        ),
        cms.PSet (
            name = cms.string("trackNHitsMissingOuterVsPhi"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};track #phi"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("bestTrackMissingOuterHits", "phi"),
        ),
        cms.PSet (
            name = cms.string("trackIsMatchedToGsfTrack"),
            title = cms.string(";has GSF track"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("matchedGsfTrack.isNonnull"),
        ),
        cms.PSet (
            name = cms.string("trackNumberOfValidHitsVsEta"),
            title = cms.string(";track |#eta|;number of valid hits"),
            binsX = cms.untracked.vdouble(8, 0.0, 2.4),
            binsY = cms.untracked.vdouble(100, -0.5, 99.5),
            inputVariables = cms.vstring("fabs (eta)", "hitPattern_.numberOfValidHits"),
        ),
        cms.PSet (
            name = cms.string("trackNumberOfValidPixelHitsVsEta"),
            title = cms.string(";track |#eta|;number of valid pixel hits"),
            binsX = cms.untracked.vdouble(8, 0.0, 2.4),
            binsY = cms.untracked.vdouble(100, -0.5, 99.5),
            inputVariables = cms.vstring("fabs (eta)", "hitPattern_.numberOfValidPixelHits"),
        ),
        cms.PSet (
            name = cms.string("trackMaxSigmaForFiducialElectronTrack"),
            title = cms.string(";max #sigma for fiducial electron track"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            inputVariables = cms.vstring("maxSigmaForFiducialElectronTrack"),
        ),
        cms.PSet (
            name = cms.string("trackMaxSigmaForFiducialMuonTrack"),
            title = cms.string(";max #sigma for fiducial muon track"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            inputVariables = cms.vstring("maxSigmaForFiducialMuonTrack"),
        ),
        #cms.PSet (
        #    name = cms.string("trackPtVsMaxSigmaForFiducialTracks"),
        #    title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;track p_{T} [GeV]"),
        #    binsX = cms.untracked.vdouble(51, 0.0, 5.1),
        #    binsY = cms.untracked.vdouble(51, 0.0, 5.1),
        #    binsZ = metBinsSlimmed,
        #    inputVariables = cms.vstring("maxSigmaForFiducialElectronTrack", "maxSigmaForFiducialMuonTrack", "pt"),
        #),
        cms.PSet (
            name = cms.string("trackDRMinJetVsIso"),
            title = cms.string(";track rel. iso.;min #DeltaR (jet, track)"),
            binsX = cms.untracked.vdouble(100, 0, 0.3),
            binsY = cms.untracked.vdouble(100, 0, 2),
            inputVariables = cms.vstring("trackIsoNoPUDRp3 / pt", "dRMinJet"),
        ),
        cms.PSet (
            name = cms.string("trackNumberOfValidHitsVsNumberOfValidPixelHits"),
            title = cms.string("Valid Hits vs Valid Pixel Hits;track number of valid pixel hits;track number of valid hits"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            binsY = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("hitPattern_.numberOfValidPixelHits", "hitPattern_.numberOfValidHits"),
        ),
    )
)

ElectronExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOnePt"),
            title = cms.string("Electron MetNoMu Minus One;E_{T}^{miss, no #mu} excluding selected electron [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOneUpPt"),
            title = cms.string("Electron MetNoMu Minus One;E_{T}^{miss, no #mu} excluding selected electron [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOneUpPt"),
        ),
        cms.PSet (
            name = cms.string("elecGenMatchedPromptFinalStateIsMatched"),
            title = cms.string(";electron is matched to generator particle"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("genMatchedParticle.promptFinalState.isNonnull"),
        ),
        cms.PSet (
            name = cms.string("elecGenMatchedPromptFinalStatePdgId"),
            title = cms.string(";PDG ID of matched generator particle"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons", "hadrons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.promptFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("elecGenMatchedPromptFinalStatePdgIdNoHadrons"),
            title = cms.string(";PDG ID of matched generator particle"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.promptFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("elecGenMatchedDirectPromptTauDecayProductFinalStateIsMatched"),
            title = cms.string(";electron is matched to generator #tau decay product"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("genMatchedParticle.directPromptTauDecayProductFinalState.isNonnull"),
        ),
        cms.PSet (
            name = cms.string("elecGenMatchedDirectPromptTauDecayProductFinalStatePdgId"),
            title = cms.string(";PDG ID of matched generator #tau decay product"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons", "hadrons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.directPromptTauDecayProductFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("elecGenMatchedDirectPromptTauDecayProductFinalStatePdgIdNoHadrons"),
            title = cms.string(";PDG ID of matched generator #tau decay product"),
            binsX = cms.untracked.vdouble(getPdgBins(["quarks", "leptons", "bosons"])),
            inputVariables = cms.vstring("abs (genMatchedParticle.directPromptTauDecayProductFinalState.pdgId)"),
        ),
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOnePtVsPt"),
            title = cms.string("Electron MetNoMu Minus One Vs. Pt;electron p_{T} [GeV];E_{T}^{miss, no #mu} excluding selected electron [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = metBins,
            inputVariables = cms.vstring("pt", "electron.metNoMuMinusOnePt"),
        ),
    )
)

TauExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("taus"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("tauMetNoMuMinusOnePt"),
            title = cms.string("Tau MetNoMu Minus One;E_{T}^{miss, no #mu} excluding selected tau [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("tauMetNoMuMinusOneUpPt"),
            title = cms.string("Tau MetNoMu Minus One;E_{T}^{miss, no #mu} excluding selected tau [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOneUpPt"),
        ),
    )
)

TrackTauHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "taus"),
    histograms = cms.VPSet (
    #cms.PSet (
    #    name = cms.string("tauMetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"),
    #    title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;E_{T}^{miss, no #mu} excluding selected tau [GeV]"),
    #    binsX = cms.untracked.vdouble(51, 0.0, 5.1),
    #    binsY = cms.untracked.vdouble(51, 0.0, 5.1),
    #    binsZ = metBinsSlimmed,
    #    inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "track.maxSigmaForFiducialMuonTrack", "tau.metNoMuMinusOnePt"),
    #),
        cms.PSet (
            name = cms.string("tauMetNoMuMinusOnePtVsMaxSigmaForFiducialElectronTrack"),
            title = cms.string(";max #sigma for fiducial electron track;E_{T}^{miss, no #mu} excluding selected tau [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "tau.metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("tauMetNoMuMinusOnePtVsMaxSigmaForFiducialMuonTrack"),
            title = cms.string(";max #sigma for fiducial muon track;E_{T}^{miss, no #mu} excluding selected tau [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialMuonTrack", "tau.metNoMuMinusOnePt"),
        ),
    )
)

MuonExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("isLooseMuon"),
            title = cms.string("is loose muon"),
            binsX = cms.untracked.vdouble (2, -0.5, 1.5),
            inputVariables = cms.vstring("isLooseMuon"),
        ),
        cms.PSet (
            name = cms.string("muonMetNoMuMinusOnePt"),
            title = cms.string("Muon MetNoMu Minus One;E_{T}^{miss, no #mu} excluding selected muon [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("muonMetNoMuMinusOneUpPt"),
            title = cms.string("Muon MetNoMu Minus One;E_{T}^{miss, no #mu} excluding selected muon [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOneUpPt"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfValidHitsVsAbsEta"),
            title = cms.string("Muon Number of Valid Hits;muon number of valid hits;muon |#eta|"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            binsY = cms.untracked.vdouble(40, 0.0, 3.0),
            inputVariables = cms.vstring("numberOfValidHits", "fabs(eta)"),
        ),
        cms.PSet (
            name = cms.string("muonNormalizedChi2VsAbsEta"),
            title = cms.string("Muon Chi Squared;muon #chi^{2}/ndf;muon |#eta|"),
            binsX = cms.untracked.vdouble(40, 0, 20),
            binsY = cms.untracked.vdouble(40, 0.0, 3.0),
            inputVariables = cms.vstring("globalTrack.normalizedChi2", "fabs(eta)"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMatchedStationsVsAbsEta"),
            title = cms.string("Muon Track Number of Matched Stations;muon number of matched stations;muon |#eta|"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            binsY = cms.untracked.vdouble(40, 0.0, 3.0),
            inputVariables = cms.vstring("numberOfMatchedStations", "fabs(eta)"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfValidPixelHitsVsAbsEta"),
            title = cms.string("Muon Number of Valid Pixel Hits;muon number of valid pixel hits;muon |#eta|"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            binsY = cms.untracked.vdouble(40, 0.0, 3.0),
            inputVariables = cms.vstring("innerTrack.hitPattern_.numberOfValidPixelHits", "fabs(eta)"),
        ),
        cms.PSet (
            name = cms.string("muonTrackerLayersWithMeasurementVsAbsEta"),
            title = cms.string("Muon Number of Tracker Layer with Measurement;muon tracker layers with measurement;muon |#eta|"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            binsY = cms.untracked.vdouble(40, 0.0, 3.0),
            inputVariables = cms.vstring("innerTrack.hitPattern_.trackerLayersWithMeasurement", "fabs(eta)"),
            ),
        cms.PSet (
            name = cms.string("muonNumberOfValidHitsVsEta"),
            title = cms.string("Muon Number of Valid Hits;muon number of valid hits;muon #eta"),
            binsX = cms.untracked.vdouble(40, 0, 40),
            binsY = cms.untracked.vdouble(80, -3.0, 3.0),
            inputVariables = cms.vstring("numberOfValidHits", "eta"),
        ),
        cms.PSet (
            name = cms.string("muonNormalizedChi2VsEta"),
            title = cms.string("Muon Chi Squared;muon #chi^{2}/ndf;muon #eta"),
            binsX = cms.untracked.vdouble(40, 0, 20),
            binsY = cms.untracked.vdouble(80, -3.0, 3.0),
            inputVariables = cms.vstring("globalTrack.normalizedChi2", "eta"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfMatchedStationsVsEta"),
            title = cms.string("Muon Track Number of Matched Stations;muon number of matched stations;muon #eta"),
            binsX = cms.untracked.vdouble(10, 0, 10),
            binsY = cms.untracked.vdouble(80, -3.0, 3.0),
            inputVariables = cms.vstring("numberOfMatchedStations", "eta"),
        ),
        cms.PSet (
            name = cms.string("muonNumberOfValidPixelHitsVsEta"),
            title = cms.string("Muon Number of Valid Pixel Hits;muon number of valid pixel hits;muon #eta"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            binsY = cms.untracked.vdouble(80, -3.0, 3.0),
            inputVariables = cms.vstring("innerTrack.hitPattern_.numberOfValidPixelHits", "eta"),
        ),
        cms.PSet (
            name = cms.string("muonTrackerLayersWithMeasurementVsEta"),
            title = cms.string("Muon Number of Tracker Layer with Measurement;muon tracker layers with measurement;muon #eta"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            binsY = cms.untracked.vdouble(80, -3.0, 3.0),
            inputVariables = cms.vstring("innerTrack.hitPattern_.trackerLayersWithMeasurement", "eta"),
            ),
        cms.PSet (
            name = cms.string("muonNHitsStripLayersVsTOBLayersVsMissingOuter"),
            title = cms.string(";N_{miss}^{outer};number of TOB layers with measurement;number of strip layers with measurement"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            binsZ = cms.untracked.vdouble(20, -0.5, 19.5),
            inputVariables = cms.vstring("bestTrackMissingOuterHits", "innerTrack.hitPattern_.stripTOBLayersWithMeasurement", "innerTrack.hitPattern_.stripLayersWithMeasurement"),
            ),
    )
)

ElectronEventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons", "eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeadingVsElectronMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected electron [GeV];|#Delta#phi(E_{T}^{miss, no #mu} excluding selected electron,leading jet)|"),
            binsX = metBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("electron.metNoMuMinusOnePt", "fabs (dPhi (electron.metNoMuMinusOnePhi, eventvariable.phiJetLeading))"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeadingVsElectronMetNoMuMinusOneUpPt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected electron [GeV];|#Delta#phi(E_{T}^{miss, no #mu} excluding selected electron,leading jet)|"),
            binsX = metBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("electron.metNoMuMinusOneUpPt", "fabs (dPhi (electron.metNoMuMinusOneUpPhi, eventvariable.phiJetLeading))"),
        ),
        cms.PSet (
            name = cms.string("passesMETTriggersWithoutElectronVsElectronMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected electron [GeV];passes E_{T}^{miss, no #mu} triggers without selected electron"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(3, -0.5, 1.5),
            inputVariables = cms.vstring("electron.metNoMuMinusOnePt", "eventvariable.passesMETTriggersWithoutElectron"),
        ),
        cms.PSet (
            name = cms.string("passesMETTriggersWithoutElectronUpVsElectronMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected electron [GeV];passes E_{T}^{miss, no #mu} triggers without selected electron"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(3, -0.5, 1.5),
            inputVariables = cms.vstring("electron.metNoMuMinusOnePt", "eventvariable.passesMETTriggersWithoutElectronUp"),
        ),
        cms.PSet (
            name = cms.string("passesL1ETMWithoutElectronVsElectronMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected electron [GeV];passes L1 ETM without selected electron"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("electron.metNoMuMinusOnePt", "eventvariable.etmPrescale_0"),
        ),
        cms.PSet (
            name = cms.string("passesL1ETMWithoutElectronUpVsElectronMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected electron [GeV];passes L1 ETM without selected electron"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("electron.metNoMuMinusOnePt", "eventvariable.etmPrescaleUp_0"),
        ),
    )
)

MuonEventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("muons", "eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeadingVsMuonMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected muon [GeV];|#Delta#phi(E_{T}^{miss, no #mu} excluding selected muon,leading jet)|"),
            binsX = metBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("muon.metNoMuMinusOnePt", "fabs (dPhi (muon.metNoMuMinusOnePhi, eventvariable.phiJetLeading))"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeadingVsMuonMetNoMuMinusOneUpPt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected muon [GeV];|#Delta#phi(E_{T}^{miss, no #mu} excluding selected muon,leading jet)|"),
            binsX = metBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("muon.metNoMuMinusOneUpPt", "fabs (dPhi (muon.metNoMuMinusOneUpPhi, eventvariable.phiJetLeading))"),
        ),
        cms.PSet (
            name = cms.string("passesMETTriggersWithoutMuonVsMuonMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected muon [GeV];passes E_{T}^{miss, no #mu} triggers without selected muon"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(3, -0.5, 1.5),
            inputVariables = cms.vstring("muon.metNoMuMinusOnePt", "eventvariable.passesMETTriggersWithoutMuon"),
        ),
        cms.PSet (
            name = cms.string("passesMETTriggersWithoutMuonUpVsMuonMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected muon [GeV];passes E_{T}^{miss, no #mu} triggers without selected muon"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(3, -0.5, 1.5),
            inputVariables = cms.vstring("muon.metNoMuMinusOnePt", "eventvariable.passesMETTriggersWithoutMuonUp"),
        ),
        cms.PSet (
            name = cms.string("passesL1ETMWithoutMuonVsMuonMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected muon [GeV];passes L1 ETM without selected muon"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("muon.metNoMuMinusOnePt", "eventvariable.etmPrescale_0"),
        ),
        cms.PSet (
            name = cms.string("passesL1ETMWithoutMuonUpVsMuonMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected muon [GeV];passes L1 ETM without selected muon"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("muon.metNoMuMinusOnePt", "eventvariable.etmPrescaleUp_0"),
        ),
    )
)

TauEventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("taus", "eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeadingVsTauMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected tau [GeV];|#Delta#phi(E_{T}^{miss, no #mu} excluding selected tau,leading jet)|"),
            binsX = metBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("tau.metNoMuMinusOnePt", "fabs (dPhi (tau.metNoMuMinusOnePhi, eventvariable.phiJetLeading))"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeadingVsTauMetNoMuMinusOneUpPt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected tau [GeV];|#Delta#phi(E_{T}^{miss, no #mu} excluding selected tau,leading jet)|"),
            binsX = metBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("tau.metNoMuMinusOneUpPt", "fabs (dPhi (tau.metNoMuMinusOneUpPhi, eventvariable.phiJetLeading))"),
        ),
        cms.PSet (
            name = cms.string("passesMETTriggersWithoutTauVsTauMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected tau [GeV];passes E_{T}^{miss, no #mu} triggers without selected tau"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(3, -0.5, 1.5),
            inputVariables = cms.vstring("tau.metNoMuMinusOnePt", "eventvariable.passesMETTriggersWithoutTau"),
        ),
        cms.PSet (
            name = cms.string("passesMETTriggersWithoutTauUpVsTauMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected tau [GeV];passes E_{T}^{miss, no #mu} triggers without selected tau"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(3, -0.5, 1.5),
            inputVariables = cms.vstring("tau.metNoMuMinusOnePt", "eventvariable.passesMETTriggersWithoutTauUp"),
        ),
        cms.PSet (
            name = cms.string("passesL1ETMWithoutTauVsTauMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected tau [GeV];passes L1 ETM without selected tau"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("tau.metNoMuMinusOnePt", "eventvariable.etmPrescale_0"),
        ),
        cms.PSet (
            name = cms.string("passesL1ETMWithoutTauUpVsTauMetNoMuMinusOnePt"),
            title = cms.string(";E_{T}^{miss, no #mu} excluding selected tau [GeV];passes L1 ETM without selected tau"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("tau.metNoMuMinusOnePt", "eventvariable.etmPrescaleUp_0"),
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
            name = cms.string("invMassNearZForTaus"),
            title = cms.string(";M(#mu,track) [GeV]"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            inputVariables = cms.vstring(invMassWithMuon ("muon")),
        ),
        cms.PSet (
            name = cms.string("sumPt"),
            title = cms.string(";p_{T} (#mu,track) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 500.0),
            inputVariables = cms.vstring( "pT (track, muon)"),
        ),
        cms.PSet (
            name = cms.string("deltaR"),
            title = cms.string(";#DeltaR(#mu,track) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("deltaR (track, muon)"),
        ),
        cms.PSet (
            name = cms.string("deltaPhi"),
            title = cms.string(";|#Delta#phi(#mu,track)| [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("fabs (deltaPhi (track, muon))"),
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
        cms.PSet (
            name = cms.string("gsfTrackNMissOutVstrackNMissOut"),
            title = cms.string(";track N_{miss}^{out};GSF track N_{miss}^{out}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("muon.bestTrackMissingOuterHits", "track.matchedGsfTrack.bestTrackMissingOuterHits"),
        ),
        #cms.PSet (
        #    name = cms.string("muonMetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"),
        #    title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;E_{T}^{miss, no #mu} excluding selected muon [GeV]"),
        #    binsX = cms.untracked.vdouble(51, 0.0, 5.1),
        #    binsY = cms.untracked.vdouble(51, 0.0, 5.1),
        #    binsZ = metBinsSlimmed,
        #    inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "track.maxSigmaForFiducialMuonTrack", "muon.metNoMuMinusOnePt"),
        #),
        cms.PSet (
            name = cms.string("muonMetNoMuMinusOnePtVsMaxSigmaForFiducialElectronTrack"),
            title = cms.string(";max #sigma for fiducial electron track;E_{T}^{miss, no #mu} excluding selected muon [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "muon.metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("muonMetNoMuMinusOnePtVsMaxSigmaForFiducialMuonTrack"),
            title = cms.string(";max #sigma for fiducial muon track;E_{T}^{miss, no #mu} excluding selected muon [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialMuonTrack", "muon.metNoMuMinusOnePt"),
        ),
    )
)

JetMetHistograms = cms.PSet(
    inputCollection = cms.vstring("jets", "mets"),
    histograms = cms.VPSet(
        cms.PSet(
            name = cms.string("leadJetPtVsMetNoMu"),
            title = cms.string(";E_{T}^{miss, no #mu} [GeV];leading jet p_{T} [GeV]"),
            binsX = metBinsSlimmed,
            binsY = metBinsSlimmed,
            indexX = cms.untracked.int32(0),
            indexY = cms.untracked.int32(0),
            inputVariables = cms.vstring("met.noMuPt", "jet.pt"),
        ),
        cms.PSet(
            name = cms.string("metPhiVsJetPhi"),
            title = cms.string(";Jet #phi;E_{T}^{miss} #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("jet.phi", "met.phi"),
        ),
        cms.PSet(
            name = cms.string("metNoMuPhiVsJetPhi"),
            title = cms.string(";Jet #phi;E_{T}^{miss, no #mu} #phi"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(64, -3.2, 3.2),
            inputVariables = cms.vstring("jet.phi", "met.noMuPhi"),
        ),
    ),
)

MuonMETHistograms = cms.PSet(
    inputCollection = cms.vstring("muons", "mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("transMass"),
            title = cms.string(";M_{T} (muon, E_{T}^{miss}) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("transMass (muon, met)"),
        ),
        cms.PSet (
            name = cms.string("deltaPhi"),
            title = cms.string(";|#Delta#phi(#mu,#vec{E}_{T}^{miss})|"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("fabs (deltaPhi (muon, met))"),
        ),
    )
)

TrackMETHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("deltaPhi"),
            title = cms.string(";|#Delta#phi(track,#vec{E}_{T}^{miss})|"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("fabs (deltaPhi (track, met))"),
        ),
        #cms.PSet (
        #    name = cms.string("metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"), ## MinusOne is a typo but for the moment let's not change it... OK
        #    title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;E_{T}^{miss, no #mu} [GeV]"),
        #    binsX = cms.untracked.vdouble(51, 0.0, 5.1),
        #    binsY = cms.untracked.vdouble(51, 0.0, 5.1),
        #    binsZ = metBinsSlimmed,
        #    inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "track.maxSigmaForFiducialMuonTrack", "met.noMuPt"),
        #),
        cms.PSet (
            name = cms.string("metNoMuVsMaxSigmaForFiducialElectronTrack"),
            title = cms.string(";max #sigma for fiducial electron track;E_{T}^{miss, no #mu} [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "met.noMuPt"),
        ),
        cms.PSet (
            name = cms.string("metNoMuVsMaxSigmaForFiducialMuonTrack"),
            title = cms.string(";max #sigma for fiducial muon track;E_{T}^{miss, no #mu} [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialMuonTrack", "met.noMuPt"),
        ),
    )
)

TrackMuonMETHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "muons", "mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("energyBalance"),
            title = cms.string(";probe track p_{T} [GeV];W boson p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("track.pt", "hypot (muon.px + met.px, muon.py + met.py)"),
        ),
        cms.PSet (
            name = cms.string("energyBalanceDiff"),
            title = cms.string(";W boson p_{T} - probe track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(1000, -100.0, 100.0),
            inputVariables = cms.vstring("hypot (muon.px + met.px, muon.py + met.py) - track.pt"),
        ),
        cms.PSet (
            name = cms.string("energyBalanceVecDiff"),
            title = cms.string(";|W boson #vec{p}_{T} + probe track #vec{p}_{T}| [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("hypot (muon.px + met.px + track.px, muon.py + met.py + track.py)"),
        ),
        cms.PSet (
            name = cms.string("wBosonAngle"),
            title = cms.string(";|#Delta#phi(W boson, probe track)|"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("fabs (dPhi (compositePhi (muon, met), track.phi))"),
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
            name = cms.string("invMassNearZForTaus"),
            title = cms.string(";M(e,track) [GeV]"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            inputVariables = cms.vstring(invMassWithElectron ("electron")),
        ),
        cms.PSet (
            name = cms.string("sumPt"),
            title = cms.string(";p_{T} (e,track) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 500.0),
            inputVariables = cms.vstring( "pT (track, electron)"),
        ),
        cms.PSet (
            name = cms.string("deltaR"),
            title = cms.string(";#DeltaR(e,track) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("deltaR (track, electron)"),
        ),
        cms.PSet (
            name = cms.string("deltaPhi"),
            title = cms.string(";|#Delta#phi(e,track)| [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("fabs (deltaPhi (track, electron))"),
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
        cms.PSet (
            name = cms.string("electronNMissOutVsTrackNMissOut"),
            title = cms.string(";track N_{miss}^{out};electron N_{miss}^{out}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(16, -0.5, 15.5),
            inputVariables = cms.vstring("track.bestTrackMissingOuterHits", "electron.bestTrackMissingOuterHits"),
        ),
        cms.PSet (
            name = cms.string("electronFBremVsTrackNMissOut"),
            title = cms.string(";track N_{miss}^{out};electron f_{brem}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("track.bestTrackMissingOuterHits", "electron.fbrem"),
        ),
        cms.PSet (
            name = cms.string("electronFBremVsElectronNMissOut"),
            title = cms.string(";electron N_{miss}^{out};electron f_{brem}"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("electron.bestTrackMissingOuterHits", "electron.fbrem"),
        ),
        #cms.PSet (
        #    name = cms.string("electronMetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"),
        #    title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;E_{T}^{miss, no #mu} excluding selected electron [GeV]"),
        #    binsX = cms.untracked.vdouble(51, 0.0, 5.1),
        #    binsY = cms.untracked.vdouble(51, 0.0, 5.1),
        #    binsZ = metBinsSlimmed,
        #    inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "track.maxSigmaForFiducialMuonTrack", "electron.metNoMuMinusOnePt"),
        #),
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOnePtVsMaxSigmaForFiducialElectronTrack"),
            title = cms.string(";max #sigma for fiducial electron track;E_{T}^{miss, no #mu} excluding selected electron [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "electron.metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOnePtVsMaxSigmaForFiducialMuonTrack"),
            title = cms.string(";max #sigma for fiducial muon track;E_{T}^{miss, no #mu} excluding selected electron [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialMuonTrack", "electron.metNoMuMinusOnePt"),
        ),

    )
)

ElectronMETHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons", "mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("transMass"),
            title = cms.string(";M_{T} (electron, E_{T}^{miss}) [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("transMass (electron, met)"),
        ),
        cms.PSet (
            name = cms.string("deltaPhi"),
            title = cms.string(";|#Delta#phi(e,#vec{E}_{T}^{miss})|"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("fabs (deltaPhi (electron, met))"),
        ),
    )
)

TrackElectronMETHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "electrons", "mets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("energyBalance"),
            title = cms.string(";probe track p_{T} [GeV];W boson p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("track.pt", "hypot (electron.px + met.px, electron.py + met.py)"),
        ),
        cms.PSet (
            name = cms.string("energyBalanceDiff"),
            title = cms.string(";W boson p_{T} - probe track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(1000, -100.0, 100.0),
            inputVariables = cms.vstring("hypot (electron.px + met.px, electron.py + met.py) - track.pt"),
        ),
        cms.PSet (
            name = cms.string("energyBalanceVecDiff"),
            title = cms.string(";|W boson #vec{p}_{T} + probe track #vec{p}_{T}| [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("hypot (electron.px + met.px + track.px, electron.py + met.py + track.py)"),
        ),
        cms.PSet (
            name = cms.string("wBosonAngle"),
            title = cms.string(";|#Delta#phi(W boson, probe track)|"),
            binsX = cms.untracked.vdouble(1000, 0.0, 3.2),
            inputVariables = cms.vstring("fabs (dPhi (compositePhi (electron, met), track.phi))"),
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
            binsX = cms.untracked.vdouble(100, 0, 500, 100, 0, 500),
            inputVariables = cms.vstring("metPt", "pt"),
            ),
        cms.PSet (
            name = cms.string("trigObjPtVsTrackPt"),
            title = cms.string("trigObjPtVsTrackPt;track p_{T} [GeV]; L1 elec p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("trackPt", "pt"),
            ),
        cms.PSet (
            name = cms.string("trigObjPtVsJetPt"),
            title = cms.string("trigObjPtVsJetPt;jet p_{T} [GeV]; L1 jet p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            binsY = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("jetPt", "pt"),
            ),

        cms.PSet (
            name = cms.string("trigObjPt"),
            title = cms.string("trigObjPt; p_{T}"),
            binsX = cms.untracked.vdouble(100, 0, 500),
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
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("deltaR ( track , jet ) "),
        ),
    )
)


DiMuonExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diMuonPtWide"),
            title = cms.string("Di-muon pT;p_{T} (#mu#mu)"),
            binsX = cms.untracked.vdouble(5000, 0, 5000),
            inputVariables = cms.vstring("pT (muon, muon)")
        ),
    )
)

JetExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetEtaVsPhi"),
            title = cms.string("jetEtaVsPhi;jetEtaVsPhi"),
            binsX = cms.untracked.vdouble(82, -5.191, 5.191),
            binsY = cms.untracked.vdouble(72, -3.1415927, 3.1415927),
            inputVariables = cms.vstring("eta" , "phi"),
        ),
        cms.PSet (
            name = cms.string("jetNvtx"),
            title = cms.string("jetsNvtx;jetsNvtx"),
            binsX = cms.untracked.vdouble(100, 0, 50),
            inputVariables = cms.vstring("nvtx"),
        ),
        cms.PSet (
            name = cms.string("jetIdLoose"),
            title = cms.string("jetIdLoose;jetIdLoose"),
            binsX = cms.untracked.vdouble(100, -0.5, 1.5),
            inputVariables = cms.vstring("jetIDLoose"),
        ),
        cms.PSet (
            name = cms.string("jetD0"),
            title = cms.string("jetD0;jetD0"),
            binsX = cms.untracked.vdouble(100, -0.02, 0.02),
            inputVariables = cms.vstring("d0"),
        ),
        cms.PSet (
            name = cms.string("jetDz"),
            title = cms.string("jetDz;jetDz"),
            binsX = cms.untracked.vdouble(100, -5, 15),
            inputVariables = cms.vstring("dZ"),
        ),
        cms.PSet (
            name = cms.string("jetBTagProb"),
            title = cms.string("jetBTagProb;jetBTagProb"),
            binsX = cms.untracked.vdouble(100, -0.05, 1.5),
            inputVariables = cms.vstring("btagJetProb"),
        ),
        cms.PSet (
            name = cms.string("jetBTagSoftMuon"),
            title = cms.string("jetBTagSoftMuon;jetBTagSoftMuon"),
            binsX = cms.untracked.vdouble(100, -0.05, 1.5),
            inputVariables = cms.vstring("btagSoftMuon"),
        ),
        cms.PSet (
            name = cms.string("jetBTagSoftEle"),
            title = cms.string("jetBTagSoftEle;jetBTagSoftEle"),
            binsX = cms.untracked.vdouble(100, -0.05, 1.5),
            inputVariables = cms.vstring("btagSoftEle"),
        ),
        cms.PSet (
            name = cms.string("jetEmFrac"),
            title = cms.string("jetEmFrac;jetEmFrac"),
            binsX = cms.untracked.vdouble(100, -1.5, 1.5),
            inputVariables = cms.vstring("EMfrac"),
        ),
        cms.PSet (
            name = cms.string("jetHadFrac"),
            title = cms.string("jetHadFrac;jetHadFrac"),
            binsX = cms.untracked.vdouble(100, -1.5, 1.5),
            inputVariables = cms.vstring("Hadfrac"),
        ),
        cms.PSet (
            name = cms.string("jetChHadEnergy"),
            title = cms.string("jetChHadEnergy;jetChHadEnergy"),
            binsX = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("chargedHadronEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetChEmEnergy"),
            title = cms.string("jetChEmEnergy;jetChEmEnergy"),
            binsX = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("chargedEmEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetNeuEmEnergy"),
            title = cms.string("jetNeuEmEnergy;jetNeuEmEnergy"),
            binsX = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("neutralEmEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetNeuHadEnergy"),
            title = cms.string("jetNeuHadEnergy;jetNeuHadEnergy"),
            binsX = cms.untracked.vdouble(100, 0, 300),
            inputVariables = cms.vstring("neutralHadronEnergy"),
        ),
        cms.PSet (
            name = cms.string("jetfHPD"),
            title = cms.string("jetfHPD;jetfHPD"),
            binsX = cms.untracked.vdouble(100, 0, 3),
            inputVariables = cms.vstring("fHPD"),
        ),
        cms.PSet (
            name = cms.string("jetn90hits"),
            title = cms.string("jetn90hits;jetn90hits"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("n90Hits"),
        ),
        cms.PSet (
            name = cms.string("jecUncertainty"),
            title = cms.string("jecUncertainty;Jet Energy Uncertainty"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("jecUncertainty"),
        ),
        cms.PSet (
            name = cms.string("jer"),
            title = cms.string("jer;Jet Energy Resolution"),
            binsX = cms.untracked.vdouble(200, -100, 100),
            inputVariables = cms.vstring("jer"),
        ),
        cms.PSet (
            name = cms.string("jerSF"),
            title = cms.string("jerSF;Jet Energy Resolution SF"),
            binsX = cms.untracked.vdouble(100, 1, 2),
            inputVariables = cms.vstring("jerSF"),
        ),
        cms.PSet (
            name = cms.string("jerSFUp"),
            title = cms.string("jerSFUp;Jet Energy Resolution SF Up"),
            binsX = cms.untracked.vdouble(100, 1, 2),
            inputVariables = cms.vstring("jerSFUp"),
        ),
        cms.PSet (
            name = cms.string("jerSFDown"),
            title = cms.string("jerSFDown;Jet Energy Resolution SF Down"),
            binsX = cms.untracked.vdouble(100, 1, 2),
            inputVariables = cms.vstring("jerSFDown"),
        ),
        cms.PSet (
            name = cms.string("relDeltaJERSFUp"),
            title = cms.string("relDeltaJERSFUp;(SFup - SF) / SF"),
            binsX = cms.untracked.vdouble(100, 1, 2),
            inputVariables = cms.vstring("(jerSFUp - jerSF) / jerSF"),
        ),
        cms.PSet (
            name = cms.string("relDeltaJERSFDown"),
            title = cms.string("relDeltaJERSFDown;(SF - SFdown) / SF"),
            binsX = cms.untracked.vdouble(100, 1, 2),
            inputVariables = cms.vstring("(jerSF - jerSFDown) / jerSF"),
        ),
        cms.PSet (
            name = cms.string("smearedPt"),
            title = cms.string("smearedPt;Smeared Jet Pt"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("smearedPt"),
        ),
        cms.PSet (
            name = cms.string("smearedPtUp"),
            title = cms.string("smearedPtUp;Smeared Jet Pt Up"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("smearedPtUp"),
        ),
        cms.PSet (
            name = cms.string("smearedPtDown"),
            title = cms.string("smearedPtDown;Smeared Jet Pt Down"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("smearedPtDown"),
        ),
    )
)

MCParticleExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("mcparticles"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("mcparticlePdgIdSusy"),
            title = cms.string("mcparticlePdgIdSusy; pdgId of SUSY mcparticles"),
            binsX = cms.untracked.vdouble(10, 1000020, 1000030),
            inputVariables = cms.vstring("pdgId"),
            ),
        cms.PSet (
            name = cms.string("mcparticlePdgId"),
            title = cms.string("mcparticlePdgId; |pdgId| of mcparticles"),
            binsX = cms.untracked.vdouble(30, 0, 30),
            inputVariables = cms.vstring("fabs(pdgId)"),
            ),
        cms.PSet (
            name = cms.string("mcparticleAbsPdgIdSusy"),
            title = cms.string("mcparticlePdgIdSusy; |pdgId| of SUSY mcparticles"),
            binsX = cms.untracked.vdouble(10, 1000020, 1000030),
            inputVariables = cms.vstring("fabs(pdgId)"),
            ),
        cms.PSet (
            name = cms.string("mcparticleMass"),
            title = cms.string("mcparticleMass; mcparticle mass [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 1000),
            inputVariables = cms.vstring("mass"),
            ),
        cms.PSet (
            name = cms.string("mcparticleVxVy"),
            title = cms.string("mcparticle position; X Position of Mcparticle [cm]; Y Position of Mcparticle [cm]"),
            binsX = cms.untracked.vdouble(100, -0.2, 0.2),
            binsY = cms.untracked.vdouble(100, -0.2, 0.2),
            inputVariables = cms.vstring("vx", "vy"),
            ),
        )
    )


JetExtraExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetChargedEmEnergyFraction"),
            title = cms.string("Jet Charged EM Energy Fraction;Jet Charged EM Energy Fraction"),
            binsX = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("chargedEmEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("jetChargedHadronEnergyFraction"),
            title = cms.string("Jet Charged Hadron Energy Fraction;Jet Charged Hadron Energy Fraction"),
            binsX = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("chargedHadronEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("jetNeutralEmEnergyFraction"),
            title = cms.string("Jet Neutral EM Energy Fraction;Jet Neutral EM Energy Fraction"),
            binsX = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("neutralEmEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("jetNeutralHadronEnergyFraction"),
            title = cms.string("Jet Neutral Hadron Energy Fraction;Jet Neutral Hadron Energy Fraction"),
            binsX = cms.untracked.vdouble(120, -0.1, 1.1),
            inputVariables = cms.vstring("neutralHadronEnergyFraction"),
            ),
        cms.PSet (
            name = cms.string("jetDeltaPhiMet"),
            title = cms.string("Jet #Delta #phi E^{miss}_{T};Jet #Delta #phi E^{miss}_{T}"),
            binsX = cms.untracked.vdouble(70, -3.5, 3.5),
            inputVariables = cms.vstring("dPhiMet"),
            ),
        cms.PSet (
            name = cms.string("jetIDLoose"),
            title = cms.string(";Jet loose ID"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("jetIDLoose"),
            ),
        cms.PSet (
            name = cms.string("jetBeta"),
            title = cms.string(";Jet #beta"),
            binsX = cms.untracked.vdouble(100, 0, 1.0),
            inputVariables = cms.vstring("beta"),
            ),
        cms.PSet (
            name = cms.string("jetBtagCombinedSecVertex"),
            title = cms.string(";Jet CSV"),
            binsX = cms.untracked.vdouble(100, 0, 1.0),
            inputVariables = cms.vstring("btagCombinedSecVertex"),
            ),
        cms.PSet (
            name = cms.string("jetPtVsMet"),
            title = cms.string("Jet p_{T} vs. E^{miss}_{T};E^{miss}_{T} [GeV]; Jet p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(20, 0, 500),
            binsY = cms.untracked.vdouble(20, 0, 500),
            inputVariables = cms.vstring("metPt", "pt"),
            ),
        cms.PSet (
            name = cms.string("jetDeltaRMuonPt20"),
            title = cms.string("; #DeltaR(jet-muon)"),
            binsX = cms.untracked.vdouble(100, 0, 5),
            inputVariables = cms.vstring("deltaRMuonPt20"),
            ),
    )
)

MetExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
         cms.PSet (
            name = cms.string("metNoMu"),
            title = cms.string("MetNoMu;E_{T}^{miss, no #mu} [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt"),
            ),
         cms.PSet (
            name = cms.string("metNoMuVsMET"),
            title = cms.string(";E_{T}^{miss} [GeV];E_{T}^{miss, no #mu} [GeV]"),
            binsX = metBins,
            binsY = metBins,
            inputVariables = cms.vstring("pt", "noMuPt"),
            ),
        )
    )

MetShiftHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
        # shift up +1sigma
        cms.PSet(
            name = cms.string("metNoMu_JetResUp"),
            title = cms.string("MetNoMu_JetResUp;E_{T}^{miss, no #mu} (jet res up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_JetResUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_JetEnUp"),
            title = cms.string("MetNoMu_JetEnUp;E_{T}^{miss, no #mu} (jet energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_JetEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_ElectronEnUp"),
            title = cms.string("MetNoMu_ElectronEnUp;E_{T}^{miss, no #mu} (electron energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_ElectronEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_TauEnUp"),
            title = cms.string("MetNoMu_TauEnUp;E_{T}^{miss, no #mu} (tau energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_TauEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_UnclusteredEnUp"),
            title = cms.string("MetNoMu_UnclusteredEnUp;E_{T}^{miss, no #mu} (unclustered energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_UnclusteredEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_PhotonEnUp"),
            title = cms.string("MetNoMu_PhotonEnUp;E_{T}^{miss, no #mu} (photon energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_PhotonEnUp"),
        ),
        # shift down -1sigma
        cms.PSet(
            name = cms.string("metNoMu_JetResDown"),
            title = cms.string("MetNoMu_JetResDown;E_{T}^{miss, no #mu} (jet res down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_JetResDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_JetEnDown"),
            title = cms.string("MetNoMu_JetEnDown;E_{T}^{miss, no #mu} (jet energy down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_JetEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_ElectronEnDown"),
            title = cms.string("MetNoMu_ElectronEnDown;E_{T}^{miss, no #mu} (electron energy down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_ElectronEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_TauEnDown"),
            title = cms.string("MetNoMu_TauEnDown;E_{T}^{miss, no #mu} (tau energy down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_TauEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_UnclusteredEnDown"),
            title = cms.string("MetNoMu_UnclusteredEnDown;E_{T}^{miss, no #mu} (unclustered energy down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_UnclusteredEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_PhotonEnDown"),
            title = cms.string("MetNoMu_PhotonEnDown;E_{T}^{miss, no #mu} (photon energy down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_PhotonEnDown"),
        ),
    )
)

DiJetHistograms = cms.PSet(
    inputCollection = cms.vstring("jet", "jet"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("dijetDeltaPhi"),
            title = cms.string(";|#Delta#phi(dijet)|"),
            binsX = cms.untracked.vdouble(100, 0, 3.15),
            inputVariables = cms.vstring("fabs (deltaPhi ( jet , jet ))"),
            ),
    )
)

############################################################################################

EventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
           name = cms.string("l1ETM"),
           title = cms.string(";L1 ETM [GeV]"),
           binsX = metBins,
           inputVariables = cms.vstring("l1ETM"),
        ),
        cms.PSet (
            name = cms.string("passesAdditionalFilters"),
            title = cms.string(";passes hltMET75;passes hltTrk50Filter"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            binsY = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("passes_hltMET75", "passes_hltTrk50Filter"),
        ),
        cms.PSet (
            name = cms.string("isrPt"),
            title = cms.string(";ISR pT"),
            binsX = cms.untracked.vdouble(1000, 0.0, 1000.0),
            inputVariables = cms.vstring("isrPt"),
        ),
        cms.PSet (
            name = cms.string("nGoodTPPairs"),
            title = cms.string(";number of good T&P pairs"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nGoodTPPairs"),
        ),
        cms.PSet (
            name = cms.string("nGoodSSTPPairs"),
            title = cms.string(";number of good same-sign T&P pairs"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nGoodSSTPPairs"),
        ),
        cms.PSet (
            name = cms.string("nGoodTagJetPairs"),
            title = cms.string(";number of good tag-jet pairs"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nGoodTagJetPairs"),
        ),
        cms.PSet (
            name = cms.string("nGoodTagPFCHPairs"),
            title = cms.string(";number of good tag-PFCH pairs"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nGoodTagPFCHPairs"),
        ),
        cms.PSet (
            name = cms.string("nProbesPassingVeto"),
            title = cms.string(";number of probes passing veto"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nProbesPassingVeto"),
        ),
        cms.PSet (
            name = cms.string("nProbesPassingLooseVeto"),
            title = cms.string(";number of probes passing loose veto"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nProbesPassingLooseVeto"),
        ),
        cms.PSet (
            name = cms.string("nSSProbesPassingVeto"),
            title = cms.string(";number of same-sign probes passing veto"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nSSProbesPassingVeto"),
        ),
        cms.PSet (
            name = cms.string("nSSProbesPassingLooseVeto"),
            title = cms.string(";number of same-sign probes passing loose veto"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nSSProbesPassingLooseVeto"),
        ),
        cms.PSet (
            name = cms.string("nProbesPassingVetoVsNGoodTPPairs"),
            title = cms.string(";number of good T&P pairs;number of probes passing veto"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            binsY = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nGoodTPPairs", "nProbesPassingVeto"),
        ),
        cms.PSet (
            name = cms.string("nProbesPassingLooseVetoVsNGoodTPPairs"),
            title = cms.string(";number of good T&P pairs;number of probes passing loose veto"),
            binsX = cms.untracked.vdouble(10, -0.5, 9.5),
            binsY = cms.untracked.vdouble(10, -0.5, 9.5),
            inputVariables = cms.vstring("nGoodTPPairs", "nProbesPassingLooseVeto"),
        ),
        cms.PSet (
            name = cms.string("leadingJetPt"),
            title = cms.string(";leading jet p_{T} [GeV]"),
            binsX = metBinsSlimmed,
            inputVariables = cms.vstring("ptJetLeading"),
        ),
        cms.PSet (
            name = cms.string("subleadingJetPt"),
            title = cms.string(";subleading jet p_{T} [GeV]"),
            binsX = metBinsSlimmed,
            inputVariables = cms.vstring("ptJetSubleading"),
        ),
        cms.PSet (
            name = cms.string("lifetimeWeight"),
            title = cms.string(";lifetime weight"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("lifetimeWeight"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("isrWeight"),
            title = cms.string(";ISR weight"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("isrWeight"),
            weight = cms.untracked.bool(False)
        ),
        cms.PSet (
            name = cms.string("isrWeightUp"),
            title = cms.string(";ISR weight +1#sigma"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("isrWeightUp"),
            weight = cms.untracked.bool(False)
        ),
        cms.PSet (
            name = cms.string("isrWeightDown"),
            title = cms.string(";ISR weight -1#sigma"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("isrWeightDown"),
            weight = cms.untracked.bool(False)
        ),
        cms.PSet (
            name = cms.string("puWeight"),
            title = cms.string(";pileup weight"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("puScalingFactor"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("puWeightUp"),
            title = cms.string(";pileup weight +1#sigma"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("puScalingFactorUp"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("puWeightDown"),
            title = cms.string(";pileup weight -1#sigma"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("puScalingFactorDown"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("missingOuterHitsWeight"),
            title = cms.string(";missing outer hits weight"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("trackScalingFactor"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("metLegTriggerWeight"),
            title = cms.string(";trigger weight for E_{T}^{miss} leg"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("metLegWeight"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("trackLegTriggerWeight"),
            title = cms.string(";trigger weight for track leg"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("trackLegWeight"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeight"),
            title = cms.string(";trigger weight for grand OR"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("grandOrWeight"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeightMCUp"),
            title = cms.string(";trigger weight for grand OR +1#sigma (MC)"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("grandOrWeightMCUp"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeightMCDown"),
            title = cms.string(";trigger weight for grand OR -1#sigma (MC)"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("grandOrWeightMCDown"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeightDataUp"),
            title = cms.string(";trigger weight for grand OR +1#sigma (data)"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("grandOrWeightDataUp"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("grandOrTriggerWeightDataDown"),
            title = cms.string(";trigger weight for grand OR -1#sigma (data)"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("grandOrWeightDataDown"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("hem1516weight"),
            title = cms.string(";HEM 15/16 jet #phi weight"),
            binsX = cms.untracked.vdouble(100, 0.0, 2.0),
            inputVariables = cms.vstring("hem1516weight"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("hem1516weightUp"),
            title = cms.string(";HEM 15/16 jet #phi weight +1#sigma"),
            binsX = cms.untracked.vdouble(100, 0.0, 2.0),
            inputVariables = cms.vstring("hem1516weightUp"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("hem1516weightDown"),
            title = cms.string(";HEM 15/16 jet #phi weight -1#sigma"),
            binsX = cms.untracked.vdouble(100, 0.0, 2.0),
            inputVariables = cms.vstring("hem1516weightDown"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("didDecay0"),
            title = cms.string(";did decay"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("didDecay_1000024_0"),
        ),
        cms.PSet (
            name = cms.string("didDecay1"),
            title = cms.string(";did decay"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("didDecay_1000024_1"),
        ),
        cms.PSet (
            name = cms.string("propagator0"),
            title = cms.string(";PDG ID of propagator"),
            binsX = cms.untracked.vdouble(100, 1000000.0, 1000100.0),
            inputVariables = cms.vstring("abs (propagator_1000024_0)"),
        ),
        cms.PSet (
            name = cms.string("propagator1"),
            title = cms.string(";PDG ID of propagator"),
            binsX = cms.untracked.vdouble(100, 1000000.0, 1000100.0),
            inputVariables = cms.vstring("abs (propagator_1000024_1)"),
        ),
        cms.PSet (
            name = cms.string("ctau0_10cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 10.0),
            inputVariables = cms.vstring("cTau_1000024_0"),
        ),
        cms.PSet (
            name = cms.string("ctau1_10cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 10.0),
            inputVariables = cms.vstring("cTau_1000024_1"),
        ),
        cms.PSet (
            name = cms.string("ctau0_100cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("cTau_1000024_0"),
        ),
        cms.PSet (
            name = cms.string("ctau1_100cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("cTau_1000024_1"),
        ),
        cms.PSet (
            name = cms.string("ctau0_1000cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 1000.0),
            inputVariables = cms.vstring("cTau_1000024_0"),
        ),
        cms.PSet (
            name = cms.string("ctau1_1000cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 1000.0),
            inputVariables = cms.vstring("cTau_1000024_1"),
        ),
        cms.PSet (
            name = cms.string("ctau0_10000cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("cTau_1000024_0"),
        ),
        cms.PSet (
            name = cms.string("ctau1_10000cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("cTau_1000024_1"),
        ),
        cms.PSet (
            name = cms.string("ctau0_100000cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100000.0),
            inputVariables = cms.vstring("cTau_1000024_0"),
        ),
        cms.PSet (
            name = cms.string("ctau1_100000cm"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100000.0),
            inputVariables = cms.vstring("cTau_1000024_1"),
        ),
        cms.PSet (
            name = cms.string("nJets"),
            title = cms.string(";Number of jets"),
            binsX = cms.untracked.vdouble(15, 0.0, 15.0),
            inputVariables = cms.vstring("nJets"),
        ),
        cms.PSet (
            name = cms.string("nTracks"),
            title = cms.string(";number of tracks"),
            binsX = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("nTracks"),
        ),
        cms.PSet (
            name = cms.string("nTracksInsideJets"),
            title = cms.string(";number of tracks"),
            binsX = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("nTracksInsideJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksOutsideJets"),
            title = cms.string(";number of tracks"),
            binsX = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("nTracksOutsideJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksInsideJetsVsOutsideJets"),
            title = cms.string(";number of tracks outside jets;number of tracks inside jets"),
            binsX = cms.untracked.vdouble(1000, 0.0, 10000.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("nTracksOutsideJets", "nTracksInsideJets"),
        ),
        cms.PSet (
            name = cms.string("HT"),
            title = cms.string(";HT [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("HT"),
        ),
        cms.PSet (
            name = cms.string("MHT"),
            title = cms.string(";HT_{T}^{miss} [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("MHT"),
        ),
        cms.PSet (
            name = cms.string("HTJets"),
            title = cms.string(";HT^{jets} [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("HTJets"),
        ),
        cms.PSet (
            name = cms.string("MHTJets"),
            title = cms.string(";HT_{T}^{miss, jets} [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("MHTJets"),
        ),
        cms.PSet (
            name = cms.string("HTNoMu"),
            title = cms.string(";HT^{no #mu} [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("HTNoMu"),
        ),
        cms.PSet (
            name = cms.string("MHTNoMu"),
            title = cms.string(";HT_{T}^{miss, no #mu} [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("MHTNoMu"),
        ),
        cms.PSet (
            name = cms.string("trackRho"),
            title = cms.string(";#rho_{track}"),
            binsX = cms.untracked.vdouble(1000, 0.0, 1000.0),
            inputVariables = cms.vstring("trackRho"),
        ),
        cms.PSet (
            name = cms.string("nTracksVsNPV"),
            title = cms.string(";number of primary vertices;number of tracks"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("numPVReco", "nTracks"),
        ),
        cms.PSet (
            name = cms.string("nTracksInsideJetsVsNPV"),
            title = cms.string(";number of primary vertices;number of tracks"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("numPVReco", "nTracksInsideJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksOutsideJetsVsNPV"),
            title = cms.string(";number of primary vertices;number of tracks"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("numPVReco", "nTracksOutsideJets"),
        ),
        cms.PSet (
            name = cms.string("trackRhoVsNPV"),
            title = cms.string(";number of primary vertices;#rho_{track}"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 1000.0),
            inputVariables = cms.vstring("numPVReco", "trackRho"),
        ),
        cms.PSet (
            name = cms.string("dijetMaxDeltaPhi"),
            title = cms.string("Maximum #Delta#phi between two jets;#Delta#phi_{max}(jet pairs)"),
            binsX = deltaPhiBins,
            inputVariables = cms.vstring("dijetMaxDeltaPhi"),
        ),
        cms.PSet (
            name = cms.string("numberOfCharginos"),
            title = cms.string(";number of charginos"),
            binsX = cms.untracked.vdouble(3, -0.5, 2.5),
            inputVariables = cms.vstring("numberOfCharginos"),
        ),
        cms.PSet (
            name = cms.string("jetInHEM1516"),
            title = cms.string(";jet pointing towards HEM 15/16"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("jetInHEM1516"),
        ),
        cms.PSet (
            name = cms.string("jetOppositeHEM1516"),
            title = cms.string(";jet pointing away from HEM 15/16"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("jetOppositeHEM1516"),
        ),
        cms.PSet (
            name = cms.string("metJetHEM1516"),
            title = cms.string(";jet pointing away, met towards HEM 15/16"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("metJetHEM1516"),
        ),
        cms.PSet (
            name = cms.string("vetoJetMap2022"),
            title = cms.string("Jet in Veto Map 2022"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("jetVeto2022"),
        ),
    )
)

EventVariableHistogramsDebug = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_0"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_0", "tagProbeChargeProduct_0"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_0"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_0", "tagProbeChargeProduct_0"),
        ),
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_1"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_1", "tagProbeChargeProduct_1"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_1"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_1", "tagProbeChargeProduct_1"),
        ),
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_2"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_2", "tagProbeChargeProduct_2"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_2"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_2", "tagProbeChargeProduct_2"),
        ),
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_3"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_3", "tagProbeChargeProduct_3"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_3"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_3", "tagProbeChargeProduct_3"),
        ),
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_4"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_4", "tagProbeChargeProduct_4"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_4"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_4", "tagProbeChargeProduct_4"),
        ),
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_5"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_5", "tagProbeChargeProduct_5"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_5"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_5", "tagProbeChargeProduct_5"),
        ),
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_6"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_6", "tagProbeChargeProduct_6"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_6"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_6", "tagProbeChargeProduct_6"),
        ),
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_7"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_7", "tagProbeChargeProduct_7"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_7"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_7", "tagProbeChargeProduct_7"),
        ),
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_8"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_8", "tagProbeChargeProduct_8"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_8"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_8", "tagProbeChargeProduct_8"),
        ),
        cms.PSet (
            name = cms.string("chargeProductVsInvMassNearZ_9"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #times q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_9", "tagProbeChargeProduct_9"),
        ),
        cms.PSet (
            name = cms.string("chargeProductInvMassNearZForTaus_9"),
            title = cms.string(";M(lepton,track) [GeV];q_{track} #cdot q_{lepton}"),
            binsX = cms.untracked.vdouble(100, 40.0, 75.0),
            binsY = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("tagProbeMass_9", "tagProbeChargeProduct_9"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_0"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_0"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_1"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_1"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_2"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_2"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_3"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_3"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_4"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_4"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_5"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_5"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_6"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_6"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_7"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_7"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_8"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_8"),
        ),
        cms.PSet (
            name = cms.string("tagJetMass_9"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 200.0),
            inputVariables = cms.vstring("tagJetMass_9"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_0"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_0"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_1"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_1"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_2"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_2"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_3"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_3"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_4"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_4"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_5"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_5"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_6"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_6"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_7"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_7"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_8"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_8"),
        ),
        cms.PSet (
            name = cms.string("tagJetMassNearZ_9"),
            title = cms.string(";M(lepton,jet) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagJetMass_9"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_0"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_0 + jetNeutralHadronEnergyFraction_0"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_1"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_1 + jetNeutralHadronEnergyFraction_1"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_2"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_2 + jetNeutralHadronEnergyFraction_2"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_3"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_3 + jetNeutralHadronEnergyFraction_3"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_4"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_4 + jetNeutralHadronEnergyFraction_4"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_5"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_5 + jetNeutralHadronEnergyFraction_5"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_6"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_6 + jetNeutralHadronEnergyFraction_6"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_7"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_7 + jetNeutralHadronEnergyFraction_7"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_8"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_8 + jetNeutralHadronEnergyFraction_8"),
        ),
        cms.PSet (
            name = cms.string("jetHadronEnergyFraction_9"),
            title = cms.string(";jet hadron energy fraction"),
            binsX = cms.untracked.vdouble(100, 0.0, 1.01),
            inputVariables = cms.vstring("jetChargedHadronEnergyFraction_9 + jetNeutralHadronEnergyFraction_9"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_0"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_0"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_1"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_1"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_2"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_2"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_3"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_3"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_4"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_4"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_5"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_5"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_6"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_6"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_7"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_7"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_8"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_8"),
        ),
        cms.PSet (
            name = cms.string("tagPFCHMass_9"),
            title = cms.string(";M(lepton,PFCH) [GeV]"),
            binsX = cms.untracked.vdouble(100, 80.0, 100.0),
            inputVariables = cms.vstring("tagPFCHMass_9"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_0"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_0"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_1"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_1"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_2"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_2"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_3"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_3"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_4"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_4"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_5"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_5"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_6"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_6"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_7"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_7"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_8"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_8"),
        ),
        cms.PSet (
            name = cms.string("pfchRelIso_9"),
            title = cms.string(";PFCH relative isolation"),
            binsX = cms.untracked.vdouble(100, 0.0, 0.1),
            inputVariables = cms.vstring("pfchRelIso_9"),
        ),
    )
)

MetEventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("mets", "eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
           name = cms.string("metNoMuVsL1ETM"),
           title = cms.string(";L1 ETM [GeV];E_{T}^{miss, no #mu} [GeV]"),
           binsX = metBins,
           binsY = metBins,
           inputVariables = cms.vstring("eventvariable.l1ETM", "met.noMuPt"),
        ),
        cms.PSet (
            name = cms.string("passesL1ETMVsMetNoMu"),
            title = cms.string(";E_{T}^{miss, no #mu} [GeV];passes L1 ETM seeds"),
            binsX = metBins,
            binsY = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("met.noMuPt", "eventvariable.etmPrescale_0"),
        ),
        cms.PSet (
            name = cms.string("leadingJetPtVsMetNoMu"),
            title = cms.string(";E_{T}^{miss, no #mu} [GeV];leading jet p_{T} [GeV]"),
            binsX = metBinsSlimmed,
            binsY = metBinsSlimmed,
            inputVariables = cms.vstring("met.noMuPt", "eventvariable.ptJetLeading"),
        ),
        cms.PSet (
            name = cms.string("subleadingJetPtVsMetNoMu"),
            title = cms.string(";E_{T}^{miss, no #mu} [GeV];subleading jet p_{T} [GeV]"),
            binsX = metBinsSlimmed,
            binsY = metBinsSlimmed,
            inputVariables = cms.vstring("met.noMuPt", "eventvariable.ptJetSubleading"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeading"),
            title = cms.string(";|#Delta#phi(E_{T}^{miss, no #mu},leading jet)|"),
            binsX = deltaPhiBins,
            inputVariables = cms.vstring("fabs (dPhi (met.noMuPhi, eventvariable.phiJetLeading))"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetSubleading"),
            title = cms.string(";|#Delta#phi(E_{T}^{miss, no #mu},subleading jet)|"),
            binsX = deltaPhiBins,
            inputVariables = cms.vstring("fabs (dPhi (met.noMuPhi, eventvariable.phiJetSubleading))"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeadingVsMET"),
            title = cms.string(";E_{T}^{miss, no #mu} [GeV];|#Delta#phi(E_{T}^{miss, no #mu},leading jet)|"),
            binsX = metBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("met.noMuPt", "fabs (dPhi (met.noMuPhi, eventvariable.phiJetLeading))"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetSubleadingVsMET"),
            title = cms.string(";E_{T}^{miss, no #mu} [GeV];|#Delta#phi(E_{T}^{miss, no #mu},subleading jet)|"),
            binsX = metBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("met.noMuPt", "fabs (dPhi (met.noMuPhi, eventvariable.phiJetSubleading))"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeadingVsdeltaPhiMetJetSubleading"),
            title = cms.string(";|#Delta#phi(E_{T}^{miss, no #mu},subleading jet)|;|#Delta#phi(E_{T}^{miss, no #mu},leading jet)|"),
            binsX = deltaPhiBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("fabs (dPhi (met.noMuPhi, eventvariable.phiJetSubleading))", "fabs (dPhi (met.noMuPhi, eventvariable.phiJetLeading))"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeadingVsMetNoMu"),
            title = cms.string(";E_{T}^{miss, no #mu} [GeV];|#Delta#phi(E_{T}^{miss, no #mu},leading jet)|"),
            binsX = metBins,
            binsY = deltaPhiBins,
            inputVariables = cms.vstring("met.noMuPt", "fabs (dPhi (met.noMuPhi, eventvariable.phiJetLeading))"),
        ),
    )
)

TrackEventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("nJetsVsTrackPhi"),
            title = cms.string(";track #phi;number of jets"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(15, 0.0, 15.0),
            inputVariables = cms.vstring("track.phi", "eventvariable.nJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksVsTrackPhi"),
            title = cms.string(";track #phi;number of tracks"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("track.phi", "eventvariable.nTracks"),
        ),
        cms.PSet (
            name = cms.string("nTracksVsTrackEta"),
            title = cms.string(";track #eta;number of tracks"),
            binsX = cms.untracked.vdouble(60, -3.0, 3.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("track.eta", "eventvariable.nTracks"),
        ),
        cms.PSet (
            name = cms.string("nTracksVsTrackDz"),
            title = cms.string(";track d_{z};number of tracks"),
            binsX = cms.untracked.vdouble(100, -2.0, 2.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring(trackDZWRTPV, "eventvariable.nTracks"),
        ),
        cms.PSet (
            name = cms.string("nTracksInsideJetsVsTrackPhi"),
            title = cms.string(";track #phi;number of tracks"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("track.phi", "eventvariable.nTracksInsideJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksInsideJetsVsTrackEta"),
            title = cms.string(";track #eta;number of tracks"),
            binsX = cms.untracked.vdouble(60, -3.0, 3.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("track.eta", "eventvariable.nTracksInsideJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksInsideJetsVsTrackDz"),
            title = cms.string(";track d_{z};number of tracks"),
            binsX = cms.untracked.vdouble(100, -2.0, 2.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring(trackDZWRTPV, "eventvariable.nTracksInsideJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksOutsideJetsVsTrackPhi"),
            title = cms.string(";track #phi;number of tracks"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("track.phi", "eventvariable.nTracksOutsideJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksOutsideJetsVsTrackEta"),
            title = cms.string(";track #eta;number of tracks"),
            binsX = cms.untracked.vdouble(60, -3.0, 3.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("track.eta", "eventvariable.nTracksOutsideJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksOutsideJetsVsTrackDz"),
            title = cms.string(";track d_{z};number of tracks"),
            binsX = cms.untracked.vdouble(100, -2.0, 2.0),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring(trackDZWRTPV, "eventvariable.nTracksOutsideJets"),
        ),
        cms.PSet (
            name = cms.string("numPVRecoVsTrackEta"),
            title = cms.string(";track #eta;number of primary vertices"),
            binsX = cms.untracked.vdouble(60, -3.0, 3.0),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("track.eta", "eventvariable.numPVReco"),
        ),
        cms.PSet (
            name = cms.string("numPVRecoVsTrackDz"),
            title = cms.string(";track d_{z};number of primary vertices"),
            binsX = cms.untracked.vdouble(100, -2.0, 2.0),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring(trackDZWRTPV, "eventvariable.numPVReco"),
        ),
        cms.PSet (
            name = cms.string("trackEtaVsTrackDz"),
            title = cms.string(";track d_{z};track #eta"),
            binsX = cms.untracked.vdouble(100, -2.0, 2.0),
            binsY = cms.untracked.vdouble(60, -3.0, 3.0),
            inputVariables = cms.vstring(trackDZWRTPV, "track.eta"),
        ),
        cms.PSet (
            name = cms.string("trackRhoVsTrackPhi"),
            title = cms.string(";track #phi;#rho_{track}"),
            binsX = cms.untracked.vdouble(64, -3.2, 3.2),
            binsY = cms.untracked.vdouble(1000, 0.0, 1000.0),
            inputVariables = cms.vstring("track.phi", "eventvariable.trackRho"),
        ),
    )
)


##############################################################################################


BeamspotHistograms = cms.PSet(
    inputCollection = cms.vstring("beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("beamspotXY"),
            title = cms.string("Beamspot position (XY-plane); Beamspot x position [cm]; Beamspot y position [cm]"),
            binsX = cms.untracked.vdouble(100, -0.2, 0.2),
            binsY = cms.untracked.vdouble(100, -0.2, 0.2),
            inputVariables = cms.vstring("beamspot.x0", "beamspot.y0"),
        ),
    )
)


PVHistograms = cms.PSet(
    inputCollection = cms.vstring("beamspots"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("beamspotXY"),
            title = cms.string("Beamspot position (XY-plane); Beamspot x position [cm]; Beamspot y position [cm]"),
            binsX = cms.untracked.vdouble(100, -0.2, 0.2),
            binsY = cms.untracked.vdouble(100, -0.2, 0.2),
            inputVariables = cms.vstring("beamspot.x0", "beamspot.y0"),
        ),
    )
)

##################################################
##### LogX bins for trigger efficiency plots #####
##################################################

binsLogX = []
nBinsLogX = 1000
binsLogXPowerHi = 3.0
binsLogXPowerLo = 0.0

binsLogXPowerWidth = (binsLogXPowerHi - binsLogXPowerLo) / nBinsLogX

for ibin in range(nBinsLogX+1):
    binsLogX.append(pow(10, binsLogXPowerLo + ibin * binsLogXPowerWidth))

MetTriggerHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
         cms.PSet (
            name = cms.string("metNoMuLogX"),
            title = cms.string("MetNoMu;E_{T}^{miss, no #mu} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("noMuPt"),
         ),
         cms.PSet (
            name = cms.string("metLogX"),
            title = cms.string("Met;E_{T}^{miss} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("pt"),
         ),
    )
)

EventTriggerVarHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet(
        cms.PSet(
            name = cms.string("leadMuonPt"),
            title = cms.string("Muon Transverse Momentum; muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("leadMuonPt"),
        ),
        cms.PSet(
            name = cms.string("leadMuonPtVsNPV"),
            title = cms.string(";number of primary vertices;muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            binsY = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("numPVReco", "leadMuonPt"),
        ),
        cms.PSet(
            name = cms.string("leadTrackPt"),
            title = cms.string("Track Transverse Momentum; track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("leadTrackPt"),
        ),
        cms.PSet(
            name = cms.string("leadTrackPtVsNPV"),
            title = cms.string(";number of primary vertices;track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            binsY = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("numPVReco", "leadTrackPt"),
        ),
        cms.PSet (
            name = cms.string("HTLogX"),
            title = cms.string(";HT [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("HT"),
        ),
        cms.PSet (
            name = cms.string("hltMetLogX"),
            title = cms.string(";hltMet [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("hltMet"),
        ),
        cms.PSet (
            name = cms.string("hltMetCleanLogX"),
            title = cms.string(";hltMetClean [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("hltMetClean"),
        ),
        cms.PSet (
            name = cms.string("MHTLogX"),
            title = cms.string(";HT_{T}^{miss} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("MHT"),
        ),
        cms.PSet (
            name = cms.string("HTNoMuLogX"),
            title = cms.string(";HT^{no #mu} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("HTNoMu"),
        ),
        cms.PSet (
            name = cms.string("MHTNoMuLogX"),
            title = cms.string(";HT_{T}^{miss, no #mu} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("MHTNoMu"),
        ),
        cms.PSet (
            name = cms.string("numPVReco"),
            title = cms.string(";Number of Primary Vertices"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("numPVReco"),
        ),
        cms.PSet (
            name = cms.string("numTrueInteractions"),
            title = cms.string(";True Number of Interactions"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("numTrueInteractions"),
        ),
        cms.PSet (
            name = cms.string("leadMuonMatchToHLTTrack"),
            title = cms.string(";Lead muon is matched to hltTrk50Filter object"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("leadMuonMatchToHLTTrack"),
        ),
        cms.PSet (
            name = cms.string("leadTrackMatchToHLTTrack"),
            title = cms.string(";Lead track is matched to hltTrk50Filter object"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("leadTrackMatchToHLTTrack"),
        ),
        cms.PSet (
            name = cms.string("passesHLTTrk50Filter"),
            title = cms.string("passesHLTTrk50Filter"),
            binsX = cms.untracked.vdouble(2.0, -0.5, 1.5),
            inputVariables = cms.vstring("passesHLTTrk50Filter"),
        ),
    )
)

EventTriggerVarVsMetHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables", "mets"),
    histograms = cms.VPSet(
        cms.PSet(
            name = cms.string("leadMuonPtVsMetNoMu"),
            title = cms.string("Muon Transverse Momentum vs MetNoMu;E_{T}^{miss, no #mu} [GeV];muon p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            binsY = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("met.noMuPt", "eventvariable.leadMuonPt"),
        ),
        cms.PSet(
            name = cms.string("leadTrackPtVsMetNoMu"),
            title = cms.string("Track Transverse Momentum vs MetNoMu;E_{T}^{miss, no #mu} [GeV];track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            binsY = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("met.noMuPt", "eventvariable.leadTrackPt"),
        ),
        cms.PSet (
            name = cms.string("MHTVsMet"),
            title = cms.string("MHT vs Met;E_{T}^{miss} [GeV];H_{T}^{miss} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            binsY = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("met.pt", "eventvariable.MHT"),
        ),
        cms.PSet (
            name = cms.string("MHTNoMuVsMetNoMu"),
            title = cms.string("MHTNoMu vs MetNoMu;E_{T}^{miss, no #mu} [GeV];H_{T}^{miss, no #mu} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            binsY = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("met.pt", "eventvariable.MHTNoMu"),
        ),
        cms.PSet (
            name = cms.string("MHTVsMetNoMu"),
            title = cms.string("MHT vs MetNoMu;E_{T}^{miss, no #mu} [GeV];H_{T}^{miss} [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            binsY = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("met.pt", "eventvariable.MHT"),
        ),
        cms.PSet (
            name = cms.string("hltMetVsMetNoMu"),
            title = cms.string("hltMet vs MetNoMu;metNoMu [GeV];hltMet [GeV]"),
            binsX = cms.untracked.vdouble(binsLogX),
            binsY = cms.untracked.vdouble(binsLogX),
            inputVariables = cms.vstring("met.noMuPt", "eventvariable.hltMet"),
        ),
    )
)

MuonIPHistograms = cms.PSet(
    # To produce these histograms, include in your PSet:
    # variableProducers.append("PrimaryVtxVarProducer")
     inputCollection = cms.vstring("muons", "eventvariables"),
     histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("muond0WRTPV"),
            title = cms.string("Muon d_{0} wrt leading PV;muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring(muonD0WRTPV),
        ),
        cms.PSet (
            name = cms.string("muond0WRTPV_Zoom"),
            title = cms.string("Muon d_{0} wrt leading PV;muon d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.1, 0.1),
            inputVariables = cms.vstring(muonD0WRTPV),
        ),
        cms.PSet (
            name = cms.string("muond0WRTPVMag"),
            title = cms.string("Muon d_{0} wrt leading PV;muon |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 0.5),
            inputVariables = cms.vstring("fabs ( " + muonD0WRTPV + " )"),
        ),
        cms.PSet (
            name = cms.string("muondzWRTPV"),
            title = cms.string("Muon d_{z} wrt leading PV;muon d_{z} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(muonDZWRTPV),
        ),
        cms.PSet (
            name = cms.string("muondzWRTPV_Zoom"),
            title = cms.string("Muon d_{z} wrt leading PV;muon d_{z} [cm]"),
            binsX = cms.untracked.vdouble(100, -2, 2),
            inputVariables = cms.vstring(muonDZWRTPV),
        ),
        cms.PSet (
            name = cms.string("muondzWRTPVMag"),
            title = cms.string("Muon d_{z} wrt leading PV;muon |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("fabs( " + muonDZWRTPV + " )" ),
        ),
    )
)

ElectronIPHistograms = cms.PSet(
    # To produce these histograms, include in your PSet:
    # variableProducers.append("PrimaryVtxVarProducer")
     inputCollection = cms.vstring("electrons", "eventvariables"),
     histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electrond0WRTPV"),
            title = cms.string("Electron d_{0} wrt leading PV;electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.5, 0.5),
            inputVariables = cms.vstring(electronD0WRTPV),
        ),
        cms.PSet (
            name = cms.string("electrond0WRTPV_Zoom"),
            title = cms.string("Electron d_{0} wrt leading PV;electron d_{0} [cm]"),
            binsX = cms.untracked.vdouble(100, -0.1, 0.1),
            inputVariables = cms.vstring(electronD0WRTPV),
        ),
        cms.PSet (
            name = cms.string("electrond0WRTPVMag"),
            title = cms.string("Electron d_{0} wrt leading PV;electron |d_{0}| [cm]"),
            binsX = cms.untracked.vdouble(50, 0, 0.5),
            inputVariables = cms.vstring("fabs ( " + electronD0WRTPV + " )"),
        ),
        cms.PSet (
            name = cms.string("electrondzWRTPV"),
            title = cms.string("Electron d_{z} wrt leading PV;electron d_{z} [cm]"),
            binsX = cms.untracked.vdouble(100, -10, 10),
            inputVariables = cms.vstring(electronDZWRTPV),
        ),
        cms.PSet (
            name = cms.string("electrondzWRTPV_Zoom"),
            title = cms.string("Electron d_{z} wrt leading PV;electron d_{z} [cm]"),
            binsX = cms.untracked.vdouble(100, -2, 2),
            inputVariables = cms.vstring(electronDZWRTPV),
        ),
        cms.PSet (
            name = cms.string("electrondzWRTPVMag"),
            title = cms.string("Electron d_{z} wrt leading PV;electron |d_{z}| [cm]"),
            binsX = cms.untracked.vdouble(100, 0, 10),
            inputVariables = cms.vstring("fabs( " + electronDZWRTPV + " )" ),
        ),
    )
)


################################################################################
# Histograms for CandidateTracks for PFisolation sums
################################################################################

CandiadteTrackPFIsolationSums = cms.VPSet(
        cms.PSet (
            name = cms.string("pfIsolationDR03ChHad"),
            title = cms.string("pfIsolationDR03ChHad;pfIsolationDR03,ChargedHad"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfChHadIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03PUChHad"),
            title = cms.string("pfIsolationDR03PUChHad;pfIsolationDR03,PileupChargedHad"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfPUChHadIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03NeuHad"),
            title = cms.string("pfIsolationDR03NeuHad;pfIsolationDR03,NeutralHad"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfNeutralHadIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfPUIsolationDR03NeuHad"),
            title = cms.string("pfPUIsolationDR03NeuHad;pfIsolationDR03,PileupNeutralHad"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfPUNeutralHadIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03Photon"),
            title = cms.string("pfIsolationDR03Photon;pfIsolationDR03,Photon"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfPhotonIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03PUPhoton"),
            title = cms.string("pfIsolationDR03PUPhoton;pfIsolationDR03,PUPhoton"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfPUPhotonIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03Electron"),
            title = cms.string("pfIsolationDR03Electron;pfIsolationDR03,Electron"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfElectronIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03PUElectron"),
            title = cms.string("pfIsolationDR03PUElectron;pfIsolationDR03,PUElectron"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfPUElectronIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03Muon"),
            title = cms.string("pfIsolationDR03Muon;pfIsolationDR03,Muon"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfMuonIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03PUMuon"),
            title = cms.string("pfIsolationDR03PUMuon;pfIsolationDR03,PUMuon"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfPUMuonIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03HF"),
            title = cms.string("pfIsolationDR03HF;pfIsolationDR03,HF"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfHFIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03PUHF"),
            title = cms.string("pfIsolationDR03PUHF;pfIsolationDR03,PUHF"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfPUHFIsoDR03"),
        ), 
        cms.PSet (
            name = cms.string("pfIsolationDR03LostTrack"),
            title = cms.string("pfIsolationDR03LostTrack;pfIsolationDR03,LostTrack"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfLostTrackIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03PULostTrack"),
            title = cms.string("pfIsolationDR03PULostTrack;pfIsolationDR03,PULostTrack"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfPULostTrackIsoDR03"),
        ),
        # Sums of particle type + PU
        cms.PSet (
            name = cms.string("pfIsolationDR03ChHadAndPU"),
            title = cms.string("pfIsolationDR03ChHadAndPU;pfIsolationDR03,ChargedHad&PU"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfChHadIsoDR03 + pfPUChHadIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03NeuHadAndPU"),
            title = cms.string("pfIsolationDR03NeuHadAndPU;pfIsolationDR03,NeutralHad&PU"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfNeutralHadIsoDR03 + pfPUNeutralHadIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03PhotonAndPU"),
            title = cms.string("pfIsolationDR03PhotonAndPU;pfIsolationDR03,Photon&PU"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfPhotonIsoDR03 + pfPUPhotonIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03ElectronAndPU"),
            title = cms.string("pfIsolationDR03ElectronAndPU;pfIsolationDR03,Electron&PU"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfElectronIsoDR03 + pfPUElectronIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03MuonAndPU"),
            title = cms.string("pfIsolationDR03MuonAndPU;pfIsolationDR03,Muon&PU"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfMuonIsoDR03 + pfPUMuonIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03HFAndPU"),
            title = cms.string("pfIsolationDR03HFAndPU;pfIsolationDR03,HF&PU"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfHFIsoDR03 + pfPUHFIsoDR03"),
        ),
        cms.PSet (
            name = cms.string("pfIsolationDR03LostTrackAndPU"),
            title = cms.string("pfIsolationDR03LostTrackAndPU;pfIsolationDR03,LostTrack&PU"),
            binsX = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("pfLostTrackIsoDR03 + pfPULostTrackIsoDR03"),
        ),
)

################################################################################
# HitPattern investigation
################################################################################

TrackDebugHitPatternHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("firstLayerWithValidHit"),
            title = cms.string("First layer with VALID hit (pattern)"),
            binsX = cms.untracked.vdouble(200, 0, 200),
            inputVariables = cms.vstring("firstLayerWithValidHit"),
        ),
        cms.PSet (
            name = cms.string("lastLayerWithValidHit"),
            title = cms.string("Last layer with VALID hit (pattern)"),
            binsX = cms.untracked.vdouble(200, 0, 200),
            inputVariables = cms.vstring("lastLayerWithValidHit"),
        ),
        cms.PSet (
            name = cms.string("hasValidHitInPixelBarrelLayer1"),
            title = cms.string("hasValidHitInPixelBarrelLayer1"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("hasValidHitInPixelBarrelLayer1"),
        ),
        cms.PSet (
            name = cms.string("hasValidHitInPixelBarrelLayer2"),
            title = cms.string("hasValidHitInPixelBarrelLayer2"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("hasValidHitInPixelBarrelLayer2"),
        ),
        cms.PSet (
            name = cms.string("hasValidHitInPixelBarrelLayer3"),
            title = cms.string("hasValidHitInPixelBarrelLayer3"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("hasValidHitInPixelBarrelLayer3"),
        ),
        cms.PSet (
            name = cms.string("hasValidHitInPixelEndcapLayer1"),
            title = cms.string("hasValidHitInPixelEndcapLayer1"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("hasValidHitInPixelEndcapLayer1"),
        ),
        cms.PSet (
            name = cms.string("hasValidHitInPixelEndcapLayer2"),
            title = cms.string("hasValidHitInPixelEndcapLayer2"),
            binsX = cms.untracked.vdouble(2, 0, 2),
            inputVariables = cms.vstring("hasValidHitInPixelEndcapLayer2"),
        ),
        cms.PSet (
            name = cms.string("bestTrackMissingInnerHitsVspackedPixelBarrelHitPattern"),
            title = cms.string("bestTrackMissingInnerHits vs packedPixelBarrelHitPattern"),
            binsX = cms.untracked.vdouble(512, 0, 512),
            binsY = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("packedPixelBarrelHitPattern", "missingInnerHits"),
        ),
        cms.PSet (
            name = cms.string("bestTrackMissingMiddleHitsVspackedPixelBarrelHitPattern"),
            title = cms.string("bestTrackMissingMiddleHits vs packedPixelBarrelHitPattern"),
            binsX = cms.untracked.vdouble(512, 0, 512),
            binsY = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("packedPixelBarrelHitPattern", "hitDrop_missingMiddleHits"),
        ),
        cms.PSet (
            name = cms.string("bestTrackMissingInnerHitsVspackedPixelEndcapHitPattern"),
            title = cms.string("bestTrackMissingInnerHits vs packedPixelEndcapHitPattern"),
            binsX = cms.untracked.vdouble(64, 0, 64),
            binsY = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("packedPixelEndcapHitPattern", "missingInnerHits"),
        ),
        cms.PSet (
            name = cms.string("bestTrackMissingMiddleHitsVspackedPixelEndcapHitPattern"),
            title = cms.string("bestTrackMissingMiddleHits vs packedPixelEndcapHitPattern"),
            binsX = cms.untracked.vdouble(64, 0, 64),
            binsY = cms.untracked.vdouble(50, 0, 50),
            inputVariables = cms.vstring("packedPixelEndcapHitPattern", "hitDrop_missingMiddleHits"),
        ),

    )
)

############################################################################################
# ToyModels histograms
############################################################################################

FakeDecayHistograms = cms.PSet(
    inputCollection = cms.vstring("eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("puScaleFactor"),
            title = cms.string(";puScaleFactor"),
            binsX = cms.untracked.vdouble(50,0,5),
            inputVariables = cms.vstring("puScalingFactor"),   
        ),
        cms.PSet (
            name = cms.string("IsLeptonVeto"),
            title = cms.string(";passesVeto ; Number of Events"),
            binsX = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("passesVeto"),
        ),
        cms.PSet (
            name = cms.string("Overall deviation angle"),
            title = cms.string(";Deviation Angle [rad]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("DeltaAngle"),
        ),
        cms.PSet (
            name = cms.string("MissOuter deviation angle"),
            title = cms.string(";Deviation Angle [rad]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("MissOuterDeltaAngle"),
        ),
        cms.PSet (
            name = cms.string("DisTrk deviation angle"),
            title = cms.string(";Deviation Angle [rad]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("DisTrkDeltaAngle"),
        ),
        cms.PSet (
            name = cms.string("Overall dR"),
            title = cms.string(";dR [rad]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("DeltaR"),
        ),
        cms.PSet (
            name = cms.string("MissOuter dR"),
            title = cms.string(";dR [rad]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("MissOuterDeltaR"),
        ),
        cms.PSet (
            name = cms.string("DisTrk dR"),
            title = cms.string(";dR [rad]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("DisTrkDeltaR"),
        ),
        cms.PSet (
            name = cms.string("Overall Pprime"),
            title = cms.string(";P [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("GenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("MissOuter Pprime"),
            title = cms.string(";P [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("MissOuterGenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("DisTrk Pprime"),
            title = cms.string(";P [GeV]"),
            binsX = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("DisTrkGenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("Overall dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP"),
        ),
        cms.PSet (
            name = cms.string("Overall PpdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 10.0),
            inputVariables = cms.vstring("DeltaAngle", "GenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("Overall rPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#mu}/p^{#chi^{#pm}}"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 1.0),
            inputVariables = cms.vstring("DeltaAngle", "RatioP"),
        ),
        cms.PSet (
            name = cms.string("Overall NLnrPdAngle"),
            title = cms.string(";Deviation Angle [rad]; -Ln(p^{#mu}/p^{#chi^{#pm}})"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 10.0),
            inputVariables = cms.vstring("DeltaAngle", "NLnRatioP"),
        ),
        cms.PSet (
            name = cms.string("MissOuter dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP"),
        ),
        cms.PSet (
            name = cms.string("MissOuter PpdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 10.0),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterGenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("MissOuter rPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#mu}/p^{#chi^{#pm}}"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 1.0),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterRatioP"),
        ),
        cms.PSet (
            name = cms.string("MissOuter NLnrPdAngle"),
            title = cms.string(";Deviation Angle [rad]; -Ln(p^{#mu}/p^{#chi^{#pm}})"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 10.0),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterNLnRatioP"),
        ),
        cms.PSet (
            name = cms.string("DisTrk dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP"),
        ),
        cms.PSet (
            name = cms.string("DisTrk PpdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 10.0),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkGenTrkMu"),
        ),
        cms.PSet (
            name = cms.string("DisTrk rPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#mu}/p^{#chi^{#pm}}"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 1.0),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkRatioP"),
        ),
        cms.PSet (
            name = cms.string("DisTrk NLnrPdAngle"),
            title = cms.string(";Deviation Angle [rad]; -Ln(p^{#mu}/p^{#chi^{#pm}})"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 10.0),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkNLnRatioP"),
        ),
        cms.PSet (
            name = cms.string("Overall dPtdAngle"),
            title = cms.string(";Deviation Angle [rad]; p_{T}^{#chi^{#pm}}-p_{T}^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("DeltaAngle", "DeltaPt"),
        ),
        cms.PSet (
            name = cms.string("MissOuter dPtdAngle"),
            title = cms.string(";Deviation Angle [rad]; p_{T}^{#chi^{#pm}}-p_{T}^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaPt"),
        ),
        cms.PSet (
            name = cms.string("DisTrk dPtdAngle"),
            title = cms.string(";Deviation Angle [rad]; p_{T}^{#chi^{#pm}}-p_{T}^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaPt"),
        ),
        cms.PSet (
            name = cms.string("Overall dPdR"),
            title = cms.string(";dR [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("DeltaR", "DeltaP"),
        ),
        cms.PSet (
            name = cms.string("MissOuter dPdR"),
            title = cms.string(";dR [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("MissOuterDeltaR", "MissOuterDeltaP"),
        ),
        cms.PSet (
            name = cms.string("DisTrk dPdR"),
            title = cms.string(";dR [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("DisTrkDeltaR", "DisTrkDeltaP"),
        ),
        cms.PSet (
            name = cms.string("Overall dPtdR"),
            title = cms.string(";dR [rad]; p_{T}^{#chi^{#pm}}-p_{T}^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("DeltaR", "DeltaPt"),
        ),
        cms.PSet (
            name = cms.string("MissOuter dPtdR"),
            title = cms.string(";dR [rad]; p_{T}^{#chi^{#pm}}-p_{T}^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("MissOuterDeltaR", "MissOuterDeltaPt"),
        ),
        cms.PSet (
            name = cms.string("DisTrk dPtdR"),
            title = cms.string(";dR [rad]; p_{T}^{#chi^{#pm}}-p_{T}^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            inputVariables = cms.vstring("DisTrkDeltaR", "DisTrkDeltaPt"),
        ),
   
        # Binned in eta
        cms.PSet (
            name = cms.string("DisTrk absEta0to0p4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs(GenTrkEta) < 0.4 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk absEta0p4to1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs(GenTrkEta) < 1 && abs(GenTrkEta)>0.4 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk absEta1to1p5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs(GenTrkEta) < 1.5 && abs(GenTrkEta) > 1 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk absEta1p5to2p1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs(GenTrkEta) < 2.1 && abs(GenTrkEta) > 1.5 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter absEta0to0p4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs(GenTrkEta) < 0.4 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter absEta0p4to1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs(GenTrkEta) < 1 && abs(GenTrkEta)>0.4 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter absEta1to1p5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs(GenTrkEta) < 1.5 && abs(GenTrkEta) > 1 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter absEta1p5to2p1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs(GenTrkEta) < 2.1 && abs(GenTrkEta) > 1.5 )"),
        ),
        cms.PSet (
            name = cms.string("Overall absEta0to0p4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs(GenTrkEta) < 0.4 )"),
        ),
        cms.PSet (
            name = cms.string("Overall absEta0p4to1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs(GenTrkEta) < 1 && abs(GenTrkEta)>0.4 )"),
        ),
        cms.PSet (
            name = cms.string("Overall absEta1to1p5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs(GenTrkEta) < 1.5 && abs(GenTrkEta) > 1 )"),
        ),
        cms.PSet (
            name = cms.string("Overall absEta1p5to2p1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs(GenTrkEta) < 2.1 && abs(GenTrkEta) > 1.5 )"),
        ),
          #Low pt range
        cms.PSet (
            name = cms.string("DisTrk GenPt40to60 absEta0to0p4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 0.4 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk GenPt40to60 absEta0p4to1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 1 && abs(GenTrkEta)>0.4 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk GenPt40to60 absEta1to1p5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 1.5 && abs(GenTrkEta) > 1 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk GenPt40to60 absEta1p5to2p1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 2.1 && abs(GenTrkEta) > 1.5 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter GenPt40to60 absEta0to0p4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 0.4 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter GenPt40to60 absEta0p4to1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 1 && abs(GenTrkEta)>0.4 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter GenPt40to60 absEta1to1p5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 1.5 && abs(GenTrkEta) > 1 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter GenPt40to60 absEta1p5to2p1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 2.1 && abs(GenTrkEta) > 1.5 )"),
        ),
        cms.PSet (
            name = cms.string("Overall GenPt40to60 absEta0to0p4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 0.4 )"),
        ),
        cms.PSet (
            name = cms.string("Overall GenPt40to60 absEta0p4to1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 1 && abs(GenTrkEta)>0.4 )"),
        ),
        cms.PSet (
            name = cms.string("Overall GenPt40to60 absEta1to1p5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 1.5 && abs(GenTrkEta) > 1 )"),
        ),
        cms.PSet (
            name = cms.string("Overall GenPt40to60 absEta1p5to2p1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( GenTrkPt < 60 ) && ( GenTrkPt > 40 ) && ( abs(GenTrkEta) < 2.1 && abs(GenTrkEta) > 1.5 )"),
        ),
        # Binned in Momentum
        cms.PSet (
            name = cms.string("DisTrk GenP40to60 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( GenTrkP < 60 ) && ( GenTrkP > 40 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk GenP60to80 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( GenTrkP < 80 ) && ( GenTrkP > 60 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk GenP80to100 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( GenTrkP < 100 ) && ( GenTrkP > 80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk GenP100to120 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( GenTrkP < 120 ) && ( GenTrkP > 100 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter GenP40to60 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( GenTrkP < 60 ) && ( GenTrkP > 40 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter GenP60to80 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( GenTrkP < 80 ) && ( GenTrkP > 60 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter GenP80to100 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( GenTrkP < 100 ) && ( GenTrkP > 80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter GenP100to120 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( GenTrkP < 120 ) && ( GenTrkP > 100 )"),
        ),
        cms.PSet (
            name = cms.string("Overall GenP40to60 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( GenTrkP < 60 ) && ( GenTrkP > 40 )"),
        ),
        cms.PSet (
            name = cms.string("Overall GenP60to80 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( GenTrkP < 80 ) && ( GenTrkP > 60 )"),
        ),
        cms.PSet (
            name = cms.string("Overall GenP80to100 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( GenTrkP < 100 ) && ( GenTrkP > 80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall GenP100to120 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( GenTrkP < 120 ) && ( GenTrkP > 100 )"),
        ),
        # Binned in Layers
        cms.PSet (
            name = cms.string("DisTrk BarrelL1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs(DecayVtxZ) < 30.197 ) && ( DecayVtxRho > 21.7 ) && ( DecayVtxRho < 24.9 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter BarrelL1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs(DecayVtxZ) < 30.197 ) && ( DecayVtxRho > 21.7 ) && ( DecayVtxRho < 24.9 )"),
        ),
        cms.PSet (
            name = cms.string("Overall BarrelL1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs(DecayVtxZ) < 30.197 ) && ( DecayVtxRho > 21.7 ) && ( DecayVtxRho < 24.9 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk BarrelL2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs(DecayVtxZ) < 32.112 ) && ( DecayVtxRho > 30.45 ) && ( DecayVtxRho < 33.65 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter BarrelL2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs(DecayVtxZ) < 32.112 ) && ( DecayVtxRho > 30.45 ) && ( DecayVtxRho < 33.65 )"),
        ),
        cms.PSet (
            name = cms.string("Overall BarrelL2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs(DecayVtxZ) < 32.112 ) && ( DecayVtxRho > 30.45 ) && ( DecayVtxRho < 33.65 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk BarrelL3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs(DecayVtxZ) < 67.846 ) && ( DecayVtxRho > 39.15 ) && ( DecayVtxRho < 42.35 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter BarrelL3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs(DecayVtxZ) < 67.846 ) && ( DecayVtxRho > 39.15 ) && ( DecayVtxRho < 42.35 )"),
        ),
        cms.PSet (
            name = cms.string("Overall BarrelL3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs(DecayVtxZ) < 67.846 ) && ( DecayVtxRho > 39.15 ) && ( DecayVtxRho < 42.35 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk BarrelL4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs(DecayVtxZ) < 68.979 ) && ( DecayVtxRho > 47.9 ) && ( DecayVtxRho < 51.1 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter BarrelL4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs(DecayVtxZ) < 68.979 ) && ( DecayVtxRho > 47.9 ) && ( DecayVtxRho < 51.1 )"),
        ),
        cms.PSet (
            name = cms.string("Overall BarrelL4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs(DecayVtxZ) < 68.979 ) && ( DecayVtxRho > 47.9 ) && ( DecayVtxRho < 51.1 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk BarrelL5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs(DecayVtxZ) < 69.722 ) && ( DecayVtxRho > 56.60 ) && ( DecayVtxRho < 59.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter BarrelL5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs(DecayVtxZ) < 69.722 ) && ( DecayVtxRho > 56.60 ) && ( DecayVtxRho < 59.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall BarrelL5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs(DecayVtxZ) < 69.722 ) && ( DecayVtxRho > 56.60 ) && ( DecayVtxRho < 59.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk MECD1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 51.8 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 35.40 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter MECD1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 51.8 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 35.40 )"),
        ),
        cms.PSet (
            name = cms.string("Overall MECD1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 51.8 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 35.40 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk MECD2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 63.4 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 35.40 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter MECD2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 63.4 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 35.40 )"),
        ),
        cms.PSet (
            name = cms.string("Overall MECD2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 63.4 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 35.40 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk MECD3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 75.0 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 35.40 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter MECD3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 75.0 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 35.40 )"),
        ),
        cms.PSet (
            name = cms.string("Overall MECD3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 75.0 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 35.40 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECA1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 95.2 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECA1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 95.2 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECA1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 95.2 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECA2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 104.2 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECA2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 104.2 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECA2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 104.2 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECA3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 114.7 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECA3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 114.7 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECA3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 114.7 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECA4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 129.3 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECA4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 129.3 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECA4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 129.3 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECA5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 144.1 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECA5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 144.1 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECA5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 144.1 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECA6 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 163.0 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECA6 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 163.0 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECA6 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 163.0 ) < 0.5 ) && ( DecayVtxRho > 21.8 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECB1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 182.3 ) < 0.5 ) && ( DecayVtxRho > 28.5 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECB1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 182.3 ) < 0.5 ) && ( DecayVtxRho > 28.5 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECB1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 182.3 ) < 0.5 ) && ( DecayVtxRho > 28.5 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECB2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 206.8 ) < 0.5 ) && ( DecayVtxRho > 28.5 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECB2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 206.8 ) < 0.5 ) && ( DecayVtxRho > 28.5 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECB2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 206.8 ) < 0.5 ) && ( DecayVtxRho > 28.5 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECC1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 231.9 ) < 0.5 ) && ( DecayVtxRho > 39.0 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECC1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 231.9 ) < 0.5 ) && ( DecayVtxRho > 39.0 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECC1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 231.9 ) < 0.5 ) && ( DecayVtxRho > 39.0 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk ECC2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( abs(DecayVtxZ) - 263.8 ) < 0.5 ) && ( DecayVtxRho > 39.0 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("MissOuter ECC2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( abs(DecayVtxZ) - 263.8 ) < 0.5 ) && ( DecayVtxRho > 39.0 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("Overall ECC2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( abs(DecayVtxZ) - 263.8 ) < 0.5 ) && ( DecayVtxRho > 39.0 ) && ( DecayVtxRho < 60.80 )"),
        ),
        cms.PSet (
            name = cms.string("DisTrk MSGCL1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 74.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("MissOuter MSGCL1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 74.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("Overall MSGCL1 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 74.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("DisTrk MSGCL2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 82.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("MissOuter MSGCL2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 82.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("Overall MSGCL2 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 82.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("DisTrk MSGCL3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 90.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("MissOuter MSGCL3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 90.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("Overall MSGCL3 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 90.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("DisTrk MSGCL4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 98.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("MissOuter MSGCL4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 98.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("Overall MSGCL4 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 98.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("DisTrk MSGCL5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 106.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("MissOuter MSGCL5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 106.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("Overall MSGCL5 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 106.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("DisTrk MSGCL6 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DisTrkDeltaAngle", "DisTrkDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 114.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("MissOuter MSGCL6 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("MissOuterDeltaAngle", "MissOuterDeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 114.7 ) < 1.5 ) "),
        ),
        cms.PSet (
            name = cms.string("Overall MSGCL6 dPdAngle"),
            title = cms.string(";Deviation Angle [rad]; p^{#chi^{#pm}}-p^{#mu} [GeV]"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            binsY = cms.untracked.vdouble(100, 0.0, 100.0),
            binsZ = cms.untracked.vdouble(2, -0.5, 1.5),
            inputVariables = cms.vstring("DeltaAngle", "DeltaP","( abs( DecayVtxZ ) < 120.5 ) && ( abs( DecayVtxRho - 114.7 ) < 1.5 ) "),
        ),
    )
)
