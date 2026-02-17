from DisappTrks.StandardAnalysis.plotUtilities import get_hist


class LeptonBackgroundHistograms:
    """Loads histograms for the lepton background estimate using Pt55 naming."""

    TAG_NAMES = {
        "electron": "ElectronTagPt55",
        "muon": "MuonTagPt55",
    }
    PROBE_NAMES = {
        "electron": ("ZtoEleProbeTrk", "Electron"),
        "muon": ("ZtoMuProbeTrk", "Muon"),
    }

    # Lepton types that use combined MET histograms at low nlayers
    COMBINED_MET_LEPTON_TYPES = ("muon", "tau")
    COMBINED_MET_NLAYERS = ("4", "5")

    def __init__(self, file_name, lepton_type):
        if lepton_type not in self.TAG_NAMES:
            raise ValueError(f"Unsupported lepton type: {lepton_type}")
        self._file_name = file_name
        self._lepton_type = lepton_type
        self._tag_name = self.TAG_NAMES[lepton_type]
        self._probe_name, self._flavor = self.PROBE_NAMES[lepton_type]
        self._combined_hists = None

    def _get_hists_raw(self, nlayers):
        """Load histograms from file for one nlayers value, no substitution."""
        nlayers_str = "6plus" if nlayers == "6" else nlayers
        tag = self._tag_name
        probe = self._probe_name
        flavor = self._flavor
        f = self._file_name

        hists = {}
        hists["n_ctrl"] = {
            "metVsFiducial": get_hist(f, f"{tag}NLayers{nlayers_str}Plotter/Track-met Plots/metNoMuVsMaxSigmaForFiducial{flavor}Track")
        }
        hists["pass_veto"] = {
            "total_tp_pairs": get_hist(f, f"{probe}NLayers{nlayers_str}Plotter/Eventvariable Plots/nGoodTPPairs"),
            "ss_tp_pairs": get_hist(f, f"{probe}NLayers{nlayers_str}Plotter/Eventvariable Plots/nGoodSSTPPairs"),
            "passing_veto_probes": get_hist(f, f"{probe}WithFilterNLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesPassingVeto"),
            "metNoMu": get_hist(f, f"{probe}WithSSFilterNLayers{nlayers_str}Plotter/Met Plots/metNoMu")
        }
        hists["pass_met_cut"] = {
            "deltaPhiVsMet": get_hist(f, f"{tag}NLayers{nlayers_str}Plotter/{flavor}-eventvariable Plots/deltaPhiMetJetLeadingVs{flavor}MetNoMuMinusOnePt")
        }
        hists["trigger_efficiency"] = {
            "passes": get_hist(f, f"{tag}MetTrigNLayers{nlayers_str}Plotter/Met Plots/metNoMu"),
            "total": get_hist(f, f"{tag}NLayers{nlayers_str}Plotter/Met Plots/metNoMu")
        }
        hists["pass_trigger"] = {
            "deltaPhiVsMet": get_hist(f, f"{tag}NLayers{nlayers_str}Plotter/{flavor}-eventvariable Plots/deltaPhiMetJetLeadingVs{flavor}MetNoMuMinusOnePt")
        }
        hists["lepton_trigger_efficiency"] = {
            "nProbesPT55": get_hist(f, f"{probe}NLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesPT55"),
            "nProbesSSPT55": get_hist(f, f"{probe}NLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesSSPT55"),
            "nProbesFiringTrigger": get_hist(f, f"{probe}NLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesFiringTrigger"),
            "nSSProbesFiringTrigger": get_hist(f, f"{probe}NLayers{nlayers_str}Plotter/Eventvariable Plots/nSSProbesFiringTrigger"),
        }

        return hists

    def get_hists(self, nlayers):
        """Load histograms for one nlayers value, or all combined if nlayers='combined'.

        For lepton types that use combined MET histograms at low nlayers
        (muon/tau at nlayers 4 and 5), substitutes the MET-related categories
        from the combined histograms and adds a 'combined_met_n_ctrl' key so
        the calculation uses the correct denominator.
        """
        if nlayers == "combined":
            return self.get_combined_hists()

        hists = self._get_hists_raw(nlayers)
        if self._lepton_type in self.COMBINED_MET_LEPTON_TYPES and nlayers in self.COMBINED_MET_NLAYERS:
            combined = self.get_combined_hists()
            hists["pass_met_cut"] = combined["pass_met_cut"]
            hists["trigger_efficiency"] = combined["trigger_efficiency"]
            hists["pass_trigger"] = combined["pass_trigger"]
            hists["lepton_trigger_efficiency"] = combined["lepton_trigger_efficiency"]
            hists["pass_met_cut"]["n_ctrl"] = combined["n_ctrl"]
        else:
            hists["pass_met_cut"]["n_ctrl"] = hists["n_ctrl"]
        return hists

    def get_combined_hists(self):
        """Load and sum histograms across all nlayers (cached)."""
        if self._combined_hists is None:
            hists_4 = self._get_hists_raw("4")
            hists_5 = self._get_hists_raw("5")
            hists_6 = self._get_hists_raw("6")

            combined = {}
            for category in hists_4:
                combined[category] = {}
                for hist_name in hists_4[category]:
                    combined[category][hist_name] = hists_4[category][hist_name].Clone()
                    combined[category][hist_name].SetDirectory(0)
                    combined[category][hist_name].Add(hists_5[category][hist_name])
                    combined[category][hist_name].Add(hists_6[category][hist_name])

            self._combined_hists = combined
        return self._combined_hists


class ClosureTestHistograms(LeptonBackgroundHistograms):
    """Uses MC naming (Pt35NoJetCuts) for closure tests."""

    TAG_NAMES = {
        "electron": "ElectronTagPt35NoJetCuts",
        "muon": "MuonTagPt35NoJetCuts",
    }
