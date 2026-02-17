# TODOs:
# - implement tau functionality

import argparse

from DisappTrks.BackgroundEstimation.lepton_background_plotter import LeptonBackgroundPlotter
from DisappTrks.BackgroundEstimation.lepton_background_results import LeptonBackgroundResults
from DisappTrks.BackgroundEstimation.lepton_background_histograms import LeptonBackgroundHistograms
from DisappTrks.BackgroundEstimation.lepton_background_calculations import (
    DEFAULT_LEPTON_TRIGGER_EFFICIENCY,
    calculate_n_est,
)
from DisappTrks.StandardAnalysis.plotUtilities import get_hist


MET_CUT = 120.0
DELTA_PHI_CUT = 0.5

DESCRIPTION = """
Estimate the lepton background contribution to the disappearing track search.

Calculates: N_est = N_ctrl * P(pass veto) * P(pass MET cut) * P(pass MET trigger) / ε_lepton_trigger

where:
  - N_ctrl: Number of tagged leptons in the fiducial region
  - P(pass veto): Probability that a probe track passes the lepton veto (from tag-and-probe)
  - P(pass MET cut): Probability of passing MET > 120 GeV and delta-phi > 0.5 cuts
  - P(pass MET trigger): Probability of passing the MET trigger (weighted by efficiency)
  - ε_lepton_trigger: Lepton trigger efficiency (from tag-and-probe or flat value)
"""


def get_args():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
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
    return parser.parse_args()


def get_plotting_hists(file_name, nlayers, lepton_type):
    """Load plotting-only histograms specific to the data estimate."""
    nlayers_str = "6plus" if nlayers == "6" else nlayers

    if lepton_type == "electron":
        tag_name = "ElectronTagPt55"
        probe_name = "ZtoEleProbeTrk"
    elif lepton_type == "muon":
        tag_name = "MuonTagPt55"
        probe_name = "ZtoMuProbeTrk"
    else:
        raise ValueError(f"Unsupported lepton type: {lepton_type}")

    hists = {
        "deltaPhiVsMetNoMu": get_hist(file_name, f"{tag_name}NLayers{nlayers_str}Plotter/Met-eventvariable Plots/deltaPhiMetJetLeadingVsMetNoMu"),
        "trackPt_before": get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Track Plots/trackPt"),
        "trackPt_after": get_hist(file_name, f"{probe_name}WithFilterNLayers{nlayers_str}Plotter/Track Plots/trackPt"),
    }
    if lepton_type != "tau":
        hists["invMass_before"] = get_hist(file_name, f"{probe_name}NLayers{nlayers_str}Plotter/Track-{lepton_type} Plots/invMassNearZ")
        hists["invMass_after"] = get_hist(file_name, f"{probe_name}WithFilterNLayers{nlayers_str}Plotter/Track-{lepton_type} Plots/invMassNearZ")

    return hists


def resolve_trigger_efficiency_kwargs(lepton_type, flat_value):
    """Resolve the --flat-lepton-trigger-efficiency CLI arg into kwargs for calculate_n_est."""
    if flat_value is None:
        return {}
    if flat_value == -1:
        eff, err = DEFAULT_LEPTON_TRIGGER_EFFICIENCY[lepton_type]
    else:
        eff, err = flat_value, 0.005
    return {"lepton_trigger_efficiency": eff, "lepton_trigger_efficiency_error": err}


def get_nlayers(nlayers_arg):
    if nlayers_arg == "all":
        return ["4", "5", "6", "combined"]
    else:
        return [nlayers_arg]


def make_plots(file_name, hists, nlayers, lepton_type, year, era):
    """Generate diagnostic plots for one nlayers value."""
    plotter = LeptonBackgroundPlotter(lepton_type, year, era, MET_CUT, DELTA_PHI_CUT)
    nlayers_suffix = nlayers if nlayers != "6" else "6plus"
    plotting_hists = get_plotting_hists(file_name, nlayers, lepton_type)

    plotter.plot_delta_phi_vs_met(plotting_hists["deltaPhiVsMetNoMu"], name_suffix=nlayers_suffix)
    plotter.plot_delta_phi_vs_met(hists["pass_met_cut"]["deltaPhiVsMet"], name_suffix=f"minus_one_{nlayers_suffix}", exclude_lepton=True)
    plotter.plot_met_projection(hists["pass_met_cut"]["deltaPhiVsMet"], name_suffix=nlayers_suffix)
    plotter.plot_trigger_efficiency(hists["trigger_efficiency"]["passes"], hists["trigger_efficiency"]["total"], name_suffix=nlayers_suffix)
    plotter.plot_veto_track_pt(plotting_hists["trackPt_before"], plotting_hists["trackPt_after"], name_suffix=nlayers_suffix)
    if lepton_type != "tau":
        plotter.plot_veto_inv_mass(plotting_hists["invMass_before"], plotting_hists["invMass_after"], name_suffix=nlayers_suffix)


def main():
    args = get_args()
    trigger_eff_kwargs = resolve_trigger_efficiency_kwargs(args.lepton_type, args.flat_lepton_trigger_efficiency)
    nlayers_to_run = get_nlayers(args.nlayers)
    hist_loader = LeptonBackgroundHistograms(args.file_name, args.lepton_type)

    for i, nlayers in enumerate(nlayers_to_run):
        hists = hist_loader.get_hists(nlayers)
        results = LeptonBackgroundResults()

        calculate_n_est(
            hists, args.year, args.era,
            args.lepton_type, results,
            **trigger_eff_kwargs
        )

        if args.output_fmt == "default":
            results.print_default(nlayers, args.verbose)
        elif i == 0:
            results.print_latex(nlayers, include_year=True)
        else:
            results.print_latex(nlayers, include_year=False)

        if args.plot:
            make_plots(args.file_name, hists, nlayers, args.lepton_type, args.year, args.era)


if __name__ == "__main__":
    main()
