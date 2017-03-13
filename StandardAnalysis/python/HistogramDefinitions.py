import FWCore.ParameterSet.Config as cms
from DisappTrks.StandardAnalysis.utilities import *
from OSUT3Analysis.Configuration.pdgIdBins import *
from OSUT3Analysis.Configuration.cutUtilities import *

###############################################
##### Set up the histograms to be plotted #####
###############################################

metBins = cms.untracked.vdouble(2000, 0.0, 10000.0)
metBinsSlimmed = cms.untracked.vdouble(500, 0.0, 2500.0)

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
            name = cms.string("trackFitPlane"),
            title = cms.string("Number of Missing Outer Hits;N_{miss}^{out};E_{calo}^{#DeltaR<0.5} [GeV]"),
            binsX = cms.untracked.vdouble(16, -0.5, 15.5),
            binsY = cms.untracked.vdouble(100, 0, 100),
            inputVariables = cms.vstring("bestTrackMissingOuterHits", "caloNewNoPUDRp5CentralCalo"),
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
            name = cms.string("trackDeltaRToClosestMuon"),
            title = cms.string("deltaRMinMuonLooseId;#DeltaR_{min}(track,muon)"),
            binsX = cms.untracked.vdouble(100, 0, 1),
            inputVariables = cms.vstring("deltaRToClosestMuon"),
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
            name = cms.string("bestMatchPt"),
            title = cms.string(";p_{T} of matched generator particle [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 500),
            inputVariables = cms.vstring("genMatchedParticle.bestMatch.pt"),
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
            inputVariables = cms.vstring("fabs (eta)", "numberOfValidHits"),
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
        cms.PSet (
            name = cms.string("trackPtVsMaxSigmaForFiducialTracks"),
            title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;track p_{T} [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
                binsY = cms.untracked.vdouble(51, 0.0, 5.1),
            binsZ = metBinsSlimmed,
            inputVariables = cms.vstring("maxSigmaForFiducialElectronTrack", "maxSigmaForFiducialMuonTrack", "pt"),
        ),
    )
)

ElectronExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("electronMetMinusOnePt"),
            title = cms.string("Electron Met Minus One;E_{T}^{miss} excluding selected electron [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("electronMetMinusOneUpPt"),
            title = cms.string("Electron Met Minus One;E_{T}^{miss} excluding selected electron [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metMinusOneUpPt"),
        ),
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOnePt"),
            title = cms.string("Electron MetNoMu Minus One;E_{T}^{miss} excluding muons and selected electron [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOneUpPt"),
            title = cms.string("Electron MetNoMu Minus One;E_{T}^{miss} excluding muons and selected electron [GeV]"),
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
            title = cms.string("Electron MetNoMu Minus One Vs. Pt;electron p_{T} [GeV];E_{T}^{miss} excluding muons and selected electron [GeV]"),
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
            name = cms.string("tauMetMinusOnePt"),
            title = cms.string("Tau Met Minus One;E_{T}^{miss} excluding selected tau [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("tauMetMinusOneUpPt"),
            title = cms.string("Tau Met Minus One;E_{T}^{miss} excluding selected tau [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metMinusOneUpPt"),
        ),
        cms.PSet (
            name = cms.string("tauMetNoMuMinusOnePt"),
            title = cms.string("Tau MetNoMu Minus One;E_{T}^{miss} excluding muons and selected tau [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("tauMetNoMuMinusOneUpPt"),
            title = cms.string("Tau MetNoMu Minus One;E_{T}^{miss} excluding muons and selected tau [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOneUpPt"),
        ),
    )
)

TrackTauHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "taus"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("tauMetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"),
            title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;E_{T}^{miss} excluding muons and selected tau [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
                binsY = cms.untracked.vdouble(51, 0.0, 5.1),
            binsZ = metBinsSlimmed,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "track.maxSigmaForFiducialMuonTrack", "tau.metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("tauMetNoMuMinusOnePtVsMaxSigmaForFiducialElectronTrack"),
            title = cms.string(";max #sigma for fiducial electron track;E_{T}^{miss} excluding muons and selected tau [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "tau.metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("tauMetNoMuMinusOnePtVsMaxSigmaForFiducialMuonTrack"),
            title = cms.string(";max #sigma for fiducial muon track;E_{T}^{miss} excluding muons and selected tau [GeV]"),
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
            name = cms.string("muonMetMinusOnePt"),
            title = cms.string("Muon Met Minus One;E_{T}^{miss} excluding selected muon [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("muonMetMinusOneUpPt"),
            title = cms.string("Muon Met Minus One;E_{T}^{miss} excluding selected muon [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metMinusOneUpPt"),
        ),
        cms.PSet (
            name = cms.string("muonMetNoMuMinusOnePt"),
            title = cms.string("Muon MetNoMu Minus One;E_{T}^{miss} excluding muons and selected muon [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("muonMetNoMuMinusOneUpPt"),
            title = cms.string("Muon MetNoMu Minus One;E_{T}^{miss} excluding muons and selected muon [GeV]"),
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
        cms.PSet (
            name = cms.string("muonMetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"),
            title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;E_{T}^{miss} excluding muons and selected muon [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = cms.untracked.vdouble(51, 0.0, 5.1),
            binsZ = metBinsSlimmed,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "track.maxSigmaForFiducialMuonTrack", "muon.metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("muonMetNoMuMinusOnePtVsMaxSigmaForFiducialElectronTrack"),
            title = cms.string(";max #sigma for fiducial electron track;E_{T}^{miss} excluding muons and selected muon [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "muon.metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("muonMetNoMuMinusOnePtVsMaxSigmaForFiducialMuonTrack"),
            title = cms.string(";max #sigma for fiducial muon track;E_{T}^{miss} excluding muons and selected muon [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialMuonTrack", "muon.metNoMuMinusOnePt"),
        ),
    )
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
        cms.PSet (
            name = cms.string("metNoMuMinusOnePtVsMaxSigmaForFiducialTracks"), ## MinusOne is a typo but for the moment let's not change it... OK
            title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;E_{T}^{miss} excluding muons [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = cms.untracked.vdouble(51, 0.0, 5.1),
            binsZ = metBinsSlimmed,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "track.maxSigmaForFiducialMuonTrack", "met.noMuPt"),
        ),
        cms.PSet (
            name = cms.string("metNoMuVsMaxSigmaForFiducialElectronTrack"),
            title = cms.string(";max #sigma for fiducial electron track;E_{T}^{miss} excluding muons [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "met.noMuPt"),
        ),
        cms.PSet (
            name = cms.string("metNoMuVsMaxSigmaForFiducialMuonTrack"),
            title = cms.string(";max #sigma for fiducial muon track;E_{T}^{miss} excluding muons [GeV]"),
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
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOnePtVsMaxSigmaForFiducialTracks"),
            title = cms.string(";max #sigma for fiducial electron track;max #sigma for fiducial muon track;E_{T}^{miss} excluding muons and selected electron [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = cms.untracked.vdouble(51, 0.0, 5.1),
            binsZ = metBinsSlimmed,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "track.maxSigmaForFiducialMuonTrack", "electron.metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOnePtVsMaxSigmaForFiducialElectronTrack"),
            title = cms.string(";max #sigma for fiducial electron track;E_{T}^{miss} excluding muons and selected electron [GeV]"),
            binsX = cms.untracked.vdouble(51, 0.0, 5.1),
            binsY = metBins,
            inputVariables = cms.vstring("track.maxSigmaForFiducialElectronTrack", "electron.metNoMuMinusOnePt"),
        ),
        cms.PSet (
            name = cms.string("electronMetNoMuMinusOnePtVsMaxSigmaForFiducialMuonTrack"),
            title = cms.string(";max #sigma for fiducial muon track;E_{T}^{miss} excluding muons and selected electron [GeV]"),
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


DiMuonHistograms = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diMuonInvMass"),
            title = cms.string("Di-Muon Invariant Mass; M_{#mu#mu} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 180),
            inputVariables = cms.vstring("invMass"),
            ),
        cms.PSet (
            name = cms.string("diMuonChargeProduct"),
            title = cms.string("Di-muon Charge Product; charge_{#mu}_{1}*charge_{#mu}_{2}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("chargeProduct"),
            ),
        cms.PSet (
            name = cms.string("diMuonDeltaEta"),
            title = cms.string("Di-muon Eta Difference; |#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaEta"),
            ),
        cms.PSet (
            name = cms.string("diMuonDeltaPhi"),
            title = cms.string("Di-muon Phi Difference; |#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(1000, 0, 3.14),
            inputVariables = cms.vstring("deltaPhi"),
            ),
        cms.PSet (
            name = cms.string("diMuonDeltaR"),
            title = cms.string("Di-muon #DeltaR; #DeltaR"),
            binsX = cms.untracked.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaR"),
            ),
        )
    )

DiMuonExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("muons", "muons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diMuonPt"),
            title = cms.string("Di-muon pT;p_{T} (#mu#mu)"),
            binsX = cms.untracked.vdouble(1000, 0, 1000),
            inputVariables = cms.vstring("pT (muon, muon)")
            ),
        )
    )

DiElectronHistograms = cms.PSet(
    inputCollection = cms.vstring("electrons", "electrons"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("diElectronInvMass"),
            title = cms.string("Di-electron Invariant Mass; M_{ee} [GeV]"),
            binsX = cms.untracked.vdouble(100, 0, 180),
            inputVariables = cms.vstring("invMass"),
            ),
        cms.PSet (
            name = cms.string("diElectronChargeProduct"),
            title = cms.string("Di-electron Charge Product; charge_{e}_{1}*charge_{e}_{2}"),
            binsX = cms.untracked.vdouble(3, -1.5, 1.5),
            inputVariables = cms.vstring("chargeProduct"),
            ),
        cms.PSet (
            name = cms.string("diElectronDeltaEta"),
            title = cms.string("Di-electron Eta Difference; |#Delta(#eta)|"),
            binsX = cms.untracked.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaEta"),
            ),
        cms.PSet (
            name = cms.string("diElectronDeltaPhi"),
            title = cms.string("Di-electron Phi Difference; |#Delta(#phi)|"),
            binsX = cms.untracked.vdouble(1000, 0, 3.14),
            inputVariables = cms.vstring("deltaPhi"),
            ),
        cms.PSet (
            name = cms.string("diElectronDeltaR"),
            title = cms.string("Di-electron #DeltaR; #DeltaR"),
            binsX = cms.untracked.vdouble(1000, 0, 10),
            inputVariables = cms.vstring("deltaR"),
            ),

        )
    )


JetExtraHistograms = cms.PSet(
    inputCollection = cms.vstring("jets"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("jetEtaVsPhi"),
            title = cms.string("jetEtaVsPhi;jetEtaVsPhi"),
            binsX = cms.untracked.vdouble(100, -3, 3),
            binsY = cms.untracked.vdouble(100, -3, 3),
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
            title = cms.string("MetNoMu;E_{T}^{miss} excluding muons [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt"),
            ),
        )
    )

MetShiftHistograms = cms.PSet(
    inputCollection = cms.vstring("mets"),
    histograms = cms.VPSet (
        # shift up +1sigma
        cms.PSet(
            name = cms.string("metNoMu_JetResUp"),
            title = cms.string("MetNoMu_JetResUp;E_{T}^{miss} excluding muons (jet res up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_JetResUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_JetEnUp"),
            title = cms.string("MetNoMu_JetEnUp;E_{T}^{miss} excluding muons (jet energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_JetEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_ElectronEnUp"),
            title = cms.string("MetNoMu_ElectronEnUp;E_{T}^{miss} excluding muons (electron energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_ElectronEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_TauEnUp"),
            title = cms.string("MetNoMu_TauEnUp;E_{T}^{miss} excluding muons (tau energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_TauEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_UnclusteredEnUp"),
            title = cms.string("MetNoMu_UnclusteredEnUp;E_{T}^{miss} excluding muons (unclustered energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_UnclusteredEnUp"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_PhotonEnUp"),
            title = cms.string("MetNoMu_PhotonEnUp;E_{T}^{miss} excluding muons (photon energy up) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_PhotonEnUp"),
        ),
        # shift down -1sigma
        cms.PSet(
            name = cms.string("metNoMu_JetResDown"),
            title = cms.string("MetNoMu_JetResDown;E_{T}^{miss} excluding muons (jet res down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_JetResDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_JetEnDown"),
            title = cms.string("MetNoMu_JetEnDown;E_{T}^{miss} excluding muons (jet energy down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_JetEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_ElectronEnDown"),
            title = cms.string("MetNoMu_ElectronEnDown;E_{T}^{miss} excluding muons (electron energy down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_ElectronEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_TauEnDown"),
            title = cms.string("MetNoMu_TauEnDown;E_{T}^{miss} excluding muons (tau energy down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_TauEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_UnclusteredEnDown"),
            title = cms.string("MetNoMu_UnclusteredEnDown;E_{T}^{miss} excluding muons (unclustered energy down) [GeV]"),
            binsX = metBins,
            inputVariables = cms.vstring("noMuPt_UnclusteredEnDown"),
        ),
        cms.PSet(
            name = cms.string("metNoMu_PhotonEnDown"),
            title = cms.string("MetNoMu_PhotonEnDown;E_{T}^{miss} excluding muons (photon energy down) [GeV]"),
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
            name = cms.string("lifetimeWeight"),
            title = cms.string(";lifetime weight"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("lifetimeWeight"),
            weight = cms.untracked.bool(False),
        ),
        cms.PSet (
            name = cms.string("puWeight"),
            title = cms.string(";pileup weight"),
            binsX = cms.untracked.vdouble(1000, 0.0, 100.0),
            inputVariables = cms.vstring("puScalingFactor"),
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
            name = cms.string("ctau"),
            title = cms.string(";c#tau [cm]"),
            binsX = cms.untracked.vdouble(1000, 0.0, 50.0),
            inputVariables = cms.vstring("cTau_1000024_0"),
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
            name = cms.string("dijetMaxDeltaPhi"),
            title = cms.string("Maximum #Delta#Phi between two jets;#Delta#Phi_{max}(jet pairs)"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("dijetMaxDeltaPhi"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetLeading"),
            title = cms.string("#Delta#Phi(E_{T}^{miss},leading jet);#Delta#Phi(E_{T}^{miss},leading jet)"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("deltaPhiMetJetLeading"),
        ),
        cms.PSet (
            name = cms.string("deltaPhiMetJetSubleading"),
            title = cms.string("#Delta#Phi(E_{T}^{miss},subleading jet);#Delta#Phi(E_{T}^{miss},subleading jet)"),
            binsX = cms.untracked.vdouble(64, 0.0, 3.2),
            inputVariables = cms.vstring("deltaPhiMetJetSubleading"),
        ),
    )
)

TrackEventVariableHistograms = cms.PSet(
    inputCollection = cms.vstring("tracks", "eventvariables"),
    histograms = cms.VPSet (
        cms.PSet (
            name = cms.string("nJetsVsTrackPhi"),
            title = cms.string(";track #phi;number of jets"),
            binsX = cms.untracked.vdouble(1, -3.2, 3.2),
            binsY = cms.untracked.vdouble(15, 0.0, 15.0),
            inputVariables = cms.vstring("track.phi", "nJets"),
        ),
        cms.PSet (
            name = cms.string("nTracksVsTrackPhi"),
            title = cms.string(";track #phi;number of tracks"),
            binsX = cms.untracked.vdouble(1, -3.2, 3.2),
            binsY = cms.untracked.vdouble(1000, 0.0, 10000.0),
            inputVariables = cms.vstring("track.phi", "nTracks"),
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
