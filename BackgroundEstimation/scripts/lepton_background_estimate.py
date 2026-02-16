# TODOs:
# - implement tau functionality

import argparse
import ctypes
import math

from DisappTrks.BackgroundEstimation.lepton_background_plotter import LeptonBackgroundPlotter
from DisappTrks.BackgroundEstimation.lepton_background_formatter import LeptonBackgroundFormatter
from DisappTrks.BackgroundEstimation.lepton_background_calculations import (
    get_n_ctrl,
    get_prob_pass_veto,
    get_prob_pass_met,
    get_trigger_efficiency_hist,
    get_prob_pass_trigger,
    calculate_lepton_trigger_efficiency,
    get_flat_lepton_trigger_efficiency
)
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import lumi
from DisappTrks.StandardAnalysis.plotUtilities import get_hist


FIDUCIAL_SIGMA_CUT = 2.0
MET_CUT = 120.0
DELTA_PHI_CUT = 0.5

DEFAULT_LEPTON_TRIGGER_EFFICIENCY = {
    "electron": (0.840, 0.005),
    "muon": (0.940, 0.004),
    "tau": (0.900, 0.006),
}

LEPTON_DATASET_NAMES = {
    "electron": "EGamma",
    "muon": "Muon",
    "tau": "Tau",
}


def get_hists(file_name, nlayers, lepton_type):
    """Load all histograms needed for the background estimate.

    Args:
        file_name: Path to the ROOT file containing the histograms.
        nlayers: Number of tracker layers ("4", "5", or "6").
        lepton_type: Type of lepton ("electron" or "muon").

    Returns:
        Dictionary of histogram dictionaries, organized by calculation step:
        - n_ctrl: Histograms for counting tagged leptons
        - pass_veto: Histograms for P(pass veto) calculation
        - pass_met_cut: Histograms for P(pass MET cut) calculation
        - trigger_efficiency: Histograms for MET trigger efficiency
        - pass_trigger: Histograms for P(pass MET trigger) calculation
        - lepton_trigger_efficiency: Histograms for lepton trigger efficiency
    """
    nlayers_str = "6plus" if nlayers == "6" else nlayers

    # Naming conventions differ by lepton type
    # Electron: ElectronTagPt55, ZtoEleProbeTrk, Electron-eventvariable Plots
    # Muon: MuonTagPt55, ZtoMuProbeTrk, Muon-eventvariable Plots
    if lepton_type == "electron":
        tag_name = "ElectronTagPt55"
        probe_name = "ZtoEleProbeTrk"
        flavor = "Electron"
    elif lepton_type == "muon":
        tag_name = "MuonTagPt55"
        probe_name = "ZtoMuProbeTrk"
        flavor = "Muon"
    else:
        raise ValueError(f"Unsupported lepton type: {lepton_type}")

    hists = {}
    hists["n_ctrl"] = {
        "metVsFiducial": get_hist(file_name, f"{tag_name}NLayers{nlayers_str}Plotter/Track-met Plots/metNoMuVsMaxSigmaForFiducial{flavor}Track")
    }
    hists["pass_veto"] = {
        "total_tp_pairs": get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Eventvariable Plots/nGoodTPPairs"),
        "ss_tp_pairs": get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Eventvariable Plots/nGoodSSTPPairs"),
        "passing_veto_probes": get_hist(file_name, f"{probe_name}WithFilterNLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesPassingVeto"),
        "metNoMu": get_hist(file_name, f"{probe_name}WithSSFilterNLayers{nlayers_str}Plotter/Met Plots/metNoMu")
    }
    hists["pass_met_cut"] = {
        "deltaPhiVsMet": get_hist(file_name, f"{tag_name}NLayers{nlayers_str}Plotter/{flavor}-eventvariable Plots/deltaPhiMetJetLeadingVs{flavor}MetNoMuMinusOnePt")
    }
    hists["trigger_efficiency"] = {
        "passes": get_hist(file_name, f"{tag_name}MetTrigNLayers{nlayers_str}Plotter/Met Plots/metNoMu"),
        "total": get_hist(file_name, f"{tag_name}NLayers{nlayers_str}Plotter/Met Plots/metNoMu")
    }
    hists["pass_trigger"] = {
        "deltaPhiVsMet": get_hist(file_name, f"{tag_name}NLayers{nlayers_str}Plotter/{flavor}-eventvariable Plots/deltaPhiMetJetLeadingVs{flavor}MetNoMuMinusOnePt")
    }
    hists["lepton_trigger_efficiency"] = {
        "nProbesPT55": get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesPT55"),
        "nProbesSSPT55": get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesSSPT55"),
        "nProbesFiringTrigger": get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesFiringTrigger"),
        "nSSProbesFiringTrigger": get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Eventvariable Plots/nSSProbesFiringTrigger"),
    }

    flavor_lower = lepton_type
    hists["plotting"] = {
        "deltaPhiVsMetNoMu": get_hist(file_name, f"{tag_name}NLayers{nlayers_str}Plotter/Met-eventvariable Plots/deltaPhiMetJetLeadingVsMetNoMu"),
        "trackPt_before": get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Track Plots/trackPt"),
        "trackPt_after": get_hist(file_name, f"{probe_name}WithFilterNLayers{nlayers_str}Plotter/Track Plots/trackPt"),
    }
    if lepton_type != "tau":
        hists["plotting"]["invMass_before"] = get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Track-{flavor_lower} Plots/invMassNearZ")
        hists["plotting"]["invMass_after"] = get_hist(file_name, f"{probe_name}WithFilterNLayers{nlayers_str}Plotter/Track-{flavor_lower} Plots/invMassNearZ")

    return hists


def get_combined_hists(file_name, lepton_type):
    """Load and sum histograms across all nlayers for combined estimate.

    Loads histograms for nlayers 4, 5, and 6, then sums them together
    to produce combined histograms for a single background estimate.

    Args:
        file_name: Path to the ROOT file containing the histograms.
        lepton_type: Type of lepton ("electron" or "muon").

    Returns:
        Dictionary of histogram dictionaries with the same structure as
        get_hists(), but with histograms summed across all nlayers.
    """
    hists_4 = get_hists(file_name, "4", lepton_type)
    hists_5 = get_hists(file_name, "5", lepton_type)
    hists_6 = get_hists(file_name, "6", lepton_type)

    combined = {}
    for category in hists_4:
        combined[category] = {}
        for hist_name in hists_4[category]:
            combined[category][hist_name] = hists_4[category][hist_name].Clone()
            combined[category][hist_name].SetDirectory(0)
            combined[category][hist_name].Add(hists_5[category][hist_name])
            combined[category][hist_name].Add(hists_6[category][hist_name])

    return combined


def get_lumi_scale_factor(lepton_type, year, era):
    """Compute the luminosity scale factor between MET and lepton datasets.

    The tagged lepton counts come from the lepton dataset, but the signal
    search uses the MET dataset. This factor corrects for any difference
    in integrated luminosity between the two.

    Args:
        lepton_type: Type of lepton ("electron", "muon", or "tau").
        year: Data-taking year (e.g. "2022").
        era: Run era (e.g. "D", "CD", "EFG").

    Returns:
        Ratio of MET luminosity to lepton dataset luminosity.
    """
    met_key = f"MET_{year}{era}"
    lepton_key = f"{LEPTON_DATASET_NAMES[lepton_type]}_{year}{era}"

    missing = [k for k in (met_key, lepton_key) if k not in lumi]
    if missing:
        print(
            f"Luminosity not found for: {', '.join(missing)}. "
            f"Check that era '{era}' is valid for year '{year}', "
            f"or add the luminosity to StandardAnalysis/python/IntegratedLuminosity_cff.py."
        )
        exit(-1)

    return lumi[met_key] / lumi[lepton_key]


def main():
    parser = argparse.ArgumentParser(
        description="""
Estimate the lepton background contribution to the disappearing track search.

Calculates: N_est = N_ctrl * P(pass veto) * P(pass MET cut) * P(pass MET trigger) / ε_lepton_trigger

where:
  - N_ctrl: Number of tagged leptons in the fiducial region
  - P(pass veto): Probability that a probe track passes the lepton veto (from tag-and-probe)
  - P(pass MET cut): Probability of passing MET > 120 GeV and delta-phi > 0.5 cuts
  - P(pass MET trigger): Probability of passing the MET trigger (weighted by efficiency)
  - ε_lepton_trigger: Lepton trigger efficiency (from tag-and-probe or flat value)
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "file_name",
        help="Path to ROOT file containing the required histograms"
    )
    parser.add_argument(
        "--nlayers",
        choices=["4", "5", "6", "all", "combined"],
        default="all",
        help="Number of tracker layers to run estimate for (default: all)"
    )
    parser.add_argument(
        "--lepton-type",
        choices=["electron", "muon"],
        required=True,
        help="Type of lepton background to estimate"
    )
    parser.add_argument(
        "--year",
        required=True,
        help="Data-taking year (e.g. 2022, 2023, 2024)"
    )
    parser.add_argument(
        "--era",
        default="",
        help="Run era (e.g. D, CD, EFG). If not specified, assume the entire year."
    )
    parser.add_argument(
        "--output-fmt",
        choices=["default", "latex"],
        default="default",
        help="Output format: 'default' for human-readable, 'latex' for analysis note table rows"
    )
    parser.add_argument(
        "--flat-lepton-trigger-efficiency",
        type=float,
        nargs="?",
        const=-1,
        default=None,
        help=f"Use a flat lepton trigger efficiency instead of calculating from histograms. "
             f"If no value given, uses default for the lepton type "
             f"(electron: {DEFAULT_LEPTON_TRIGGER_EFFICIENCY['electron'][0]}, "
             f"muon: {DEFAULT_LEPTON_TRIGGER_EFFICIENCY['muon'][0]}, "
             f"tau: {DEFAULT_LEPTON_TRIGGER_EFFICIENCY['tau'][0]})"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print verbose output with intermediate calculation values"
    )
    parser.add_argument(
        "-p", "--plot",
        action="store_true",
        help="Generate diagnostic plots (delta-phi vs MET, MET projection, trigger efficiency, veto comparisons)"
    )
    args = parser.parse_args()

    lumi_scale_factor = get_lumi_scale_factor(args.lepton_type, args.year, args.era)

    if args.nlayers == "all":
        nlayers_to_run = ["4", "5", "6", "combined"]
    else:
        nlayers_to_run = [args.nlayers]

    combined_hists = get_combined_hists(args.file_name, args.lepton_type)

    for i, nlayers in enumerate(nlayers_to_run):
        if nlayers == "combined":
            hists = combined_hists
        else:
            hists = get_hists(args.file_name, nlayers, args.lepton_type)

        use_combined_met = args.lepton_type in ("muon", "tau") and nlayers in ("4", "5")
        if use_combined_met:
            hists["pass_met_cut"] = combined_hists["pass_met_cut"]
            hists["trigger_efficiency"] = combined_hists["trigger_efficiency"]
            hists["pass_trigger"] = combined_hists["pass_trigger"]
            hists["lepton_trigger_efficiency"] = combined_hists["lepton_trigger_efficiency"]

        formatter = LeptonBackgroundFormatter()
        formatter.add_result("Lumi scale factor", lumi_scale_factor, 0.0)

        n_ctrl, err_n_ctrl = get_n_ctrl(hists["n_ctrl"])
        formatter.add_result("N_ctrl (unscaled)", n_ctrl, err_n_ctrl)
        n_ctrl *= lumi_scale_factor
        err_n_ctrl *= lumi_scale_factor
        formatter.add_result("N_ctrl", n_ctrl, err_n_ctrl)

        # P(pass MET cut) uses n_ctrl as its denominator. When using
        # combined MET histograms, the denominator must also be the combined
        # n_ctrl to get the correct probability.
        if use_combined_met:
            met_n_ctrl, met_err_n_ctrl = get_n_ctrl(combined_hists["n_ctrl"])
            met_n_ctrl *= lumi_scale_factor
            met_err_n_ctrl *= lumi_scale_factor
        else:
            met_n_ctrl, met_err_n_ctrl = n_ctrl, err_n_ctrl

        p_pass_lept_veto, err_pass_lept_veto = get_prob_pass_veto(hists["pass_veto"], formatter)
        p_pass_met_cut, err_pass_met_cut = get_prob_pass_met(hists["pass_met_cut"], met_n_ctrl, met_err_n_ctrl, formatter)
        h_met_trig_eff = get_trigger_efficiency_hist(hists["trigger_efficiency"])
        prob_pass_met_trig, err_pass_met_trig = get_prob_pass_trigger(hists["pass_trigger"], h_met_trig_eff, formatter)

        if args.flat_lepton_trigger_efficiency is None:
            lept_trig_eff, err_lept_trig_eff = calculate_lepton_trigger_efficiency(hists["lepton_trigger_efficiency"], formatter)
        else:
            lept_trig_eff, err_lept_trig_eff = get_flat_lepton_trigger_efficiency(args.lepton_type, args.flat_lepton_trigger_efficiency, formatter)

        n_est = n_ctrl * p_pass_lept_veto * p_pass_met_cut * prob_pass_met_trig / lept_trig_eff
        err_n_est = math.sqrt(
            (p_pass_lept_veto * p_pass_met_cut * prob_pass_met_trig / lept_trig_eff * err_n_ctrl)**2 +
            (n_ctrl * p_pass_met_cut * prob_pass_met_trig / lept_trig_eff * err_pass_lept_veto)**2 +
            (n_ctrl * p_pass_lept_veto * prob_pass_met_trig / lept_trig_eff * err_pass_met_cut)**2 +
            (n_ctrl * p_pass_lept_veto * p_pass_met_cut / lept_trig_eff * err_pass_met_trig)**2 +
            (n_ctrl * p_pass_lept_veto * p_pass_met_cut * prob_pass_met_trig / (lept_trig_eff**2) * err_lept_trig_eff)**2
        )

        # When multiple factors are zero (e.g. both N_ctrl and P_veto),
        # first-order error propagation gives zero because every partial
        # derivative term contains at least one zero central value. Use
        # the second-order cross-term as the leading uncertainty estimate.
        if n_est == 0.0 and err_n_est == 0.0:
            err_n_est = (err_n_ctrl * err_pass_lept_veto
                         * p_pass_met_cut * prob_pass_met_trig
                         / lept_trig_eff)

        n_est_formula = (f"{n_ctrl:.4g} * {p_pass_lept_veto:.4g} * {p_pass_met_cut:.4g} * "
                         f"{prob_pass_met_trig:.4g} / {lept_trig_eff:.4g}")
        formatter.add_result("N_est", n_est, err_n_est, formula=n_est_formula)

        if args.output_fmt == "default":
            formatter.print_default(nlayers, args.verbose)
        elif i == 0:
            formatter.print_latex(nlayers, include_year=True)
        else:
            formatter.print_latex(nlayers, include_year=False)

        if args.plot:
            plotter = LeptonBackgroundPlotter(args.lepton_type, args.year, args.era, MET_CUT, DELTA_PHI_CUT)
            nlayers_suffix = nlayers if nlayers != "6" else "6plus"

            plotter.plot_delta_phi_vs_met(hists["plotting"]["deltaPhiVsMetNoMu"], name_suffix=nlayers_suffix)
            plotter.plot_delta_phi_vs_met(hists["pass_met_cut"]["deltaPhiVsMet"], name_suffix=f"minus_one_{nlayers_suffix}", exclude_lepton=True)
            plotter.plot_met_projection(hists["pass_met_cut"]["deltaPhiVsMet"], name_suffix=nlayers_suffix)
            plotter.plot_trigger_efficiency(hists["trigger_efficiency"]["passes"], hists["trigger_efficiency"]["total"], name_suffix=nlayers_suffix)
            plotter.plot_veto_track_pt(hists["plotting"]["trackPt_before"], hists["plotting"]["trackPt_after"], name_suffix=nlayers_suffix)
            if args.lepton_type != "tau":
                plotter.plot_veto_inv_mass(hists["plotting"]["invMass_before"], hists["plotting"]["invMass_after"], name_suffix=nlayers_suffix)


if __name__ == "__main__":
    main()
