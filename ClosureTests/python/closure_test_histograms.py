from DisappTrks.BackgroundEstimation.lepton_background_histograms import LeptonBackgroundHistograms

class ClosureTestHistograms(LeptonBackgroundHistograms):
    """Uses MC naming (Pt35NoJetCuts) for closure tests."""

    TAG_NAMES = {
        "electron": "ElectronTagPt35NoJetCuts",
        "muon": "MuonTagPt35NoJetCuts",
    }
