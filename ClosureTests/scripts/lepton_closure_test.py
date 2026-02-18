import argparse
import ctypes
import math

import ROOT
from tabulate import tabulate

from DisappTrks.BackgroundEstimation.lepton_background_calculations import (
    DEFAULT_LEPTON_TRIGGER_EFFICIENCY,
    calculate_n_est,
)
from DisappTrks.BackgroundEstimation.lepton_background_histograms import LeptonBackgroundHistograms
from DisappTrks.ClosureTests.closure_test_histograms import ClosureTestHistograms
from DisappTrks.StandardAnalysis.plotUtilities import get_hist


ECAL_ENERGY_CUT = 10.0
DEFAULT_ERROR = 0.5 * ROOT.TMath.ChisquareQuantile(0.68, 2)


class ClosureTestResults:
    """Formatter for closure test output that merges reco, truth, and optional data results."""

    def __init__(self):
        self._results = []

    def add(self, label, value, error, formula=""):
        self._results.append((label, value, error, formula))

    def print_results(self, nlayers, is_verbose):
        rows = []
        for label, value, error, formula in self._results:
            row = [label, f"{value:.8g} +/- {error:.8g}"]
            if is_verbose:
                row.append(formula)
            rows.append(row)

        headers = [f"NLayers {nlayers}", "Value"]
        if is_verbose:
            headers.append("Details")

        print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
        print()


def get_args():
    parser = argparse.ArgumentParser(
        description="""\
Lepton background closure test: compare the estimated background (from the
tag-and-probe method) to the truth background (from gen-matched tracks in MC).

Calculates:
  N_est = N_ctrl * P(pass veto) * P(pass MET cut) * P(pass MET trigger) / ε_lepton_trigger
  N_obs = tracks matching generated leptons with ECAL energy < 10 GeV
  Closure = (N_est - N_obs) / sqrt(σ_est² + σ_obs²) in sigma
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "file_name",
        help="Path to ROOT file containing all required histograms (hadd'd from TTbar + DY)"
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
        "--data-file",
        default=None,
        help="Path to data ROOT file to also run the background estimate on (uses Pt55 naming)"
    )
    parser.add_argument(
        "--flat-lepton-trigger-efficiency",
        type=float,
        nargs="?",
        const=-1,
        default=None,
        help="Use a flat lepton trigger efficiency instead of calculating from histograms"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print verbose output with intermediate calculation values"
    )
    return parser.parse_args()


def _get_total_and_error(hist, max_cut=None):
    max_bin = -1 if max_cut is None else hist.FindBin(max_cut)
    error = ctypes.c_double()
    total = hist.IntegralAndError(0, max_bin, error)
    error = error.value

    if total - error < 0.0:
        error = total

    return total, error


def _get_weight(hist):
    total = float(hist.GetBinContent(1))
    error = float(hist.GetBinError(1))
    return (error * error) / total


def get_truth_background(file_name, nlayers, lepton_type):
    """Get the truth background count from CandTrkId histograms.

    Counts tracks matching the generated lepton that pass the candidate
    track selection with ECAL energy below the cut threshold.
    """
    nlayers_str = "6plus" if nlayers == "6" else nlayers

    if lepton_type == "electron":
        cand_name = "CandTrkIdElecPt35"
    elif lepton_type == "muon":
        cand_name = "CandTrkIdMuPt35"
    else:
        raise ValueError(f"Unsupported lepton type: {lepton_type}")

    ecal_energy_hist = get_hist(file_name, f"{cand_name}NLayers{nlayers_str}Plotter/Track Plots/trackCaloJetEnergy")
    total, error = _get_total_and_error(ecal_energy_hist, ECAL_ENERGY_CUT)

    if total == 0.0:
        cutflow_hist = get_hist(file_name, f"{cand_name}NLayers{nlayers_str}CutFlowPlotter/cutFlow")
        error = DEFAULT_ERROR * _get_weight(cutflow_hist)

    return total, error


def get_combined_truth_background(file_name, lepton_type):
    """Get the truth background summed across all nlayers."""
    total_combined = 0.0
    error_combined = 0.0
    for nlayers in ("4", "5", "6"):
        t, e = get_truth_background(file_name, nlayers, lepton_type)
        total_combined += t
        error_combined = math.hypot(error_combined, e)
    return total_combined, error_combined


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


def main():
    args = get_args()
    trigger_eff_kwargs = resolve_trigger_efficiency_kwargs(args.lepton_type, args.flat_lepton_trigger_efficiency)
    nlayers_to_run = get_nlayers(args.nlayers)
    mc_loader = ClosureTestHistograms(args.file_name, args.lepton_type)

    if args.data_file:
        data_loader = LeptonBackgroundHistograms(args.data_file, args.lepton_type)

    for nlayers in nlayers_to_run:
        output = ClosureTestResults()

        # Reco estimate from MC
        mc_hists = mc_loader.get_hists(nlayers)

        reco_results = ClosureTestResults()
        n_est_reco, err_reco = calculate_n_est(
            mc_hists, args.year, args.era,
            args.lepton_type, reco_results, **trigger_eff_kwargs
        )

        if args.verbose:
            for label, value, error, formula in reco_results._results:
                output.add(f"[reco] {label}", value, error, formula)

        output.add("N_est (reco)", n_est_reco, err_reco)

        # Truth background
        if nlayers == "combined":
            n_obs, err_n_obs = get_combined_truth_background(args.file_name, args.lepton_type)
        else:
            n_obs, err_n_obs = get_truth_background(args.file_name, nlayers, args.lepton_type)
        output.add("N_obs (truth)", n_obs, err_n_obs)

        # Data estimate (optional)
        if args.data_file:
            data_hists = data_loader.get_hists(nlayers)

            data_results = ClosureTestResults()
            n_est_data, err_data = calculate_n_est(
                data_hists, args.year, args.era,
                args.lepton_type, data_results, **trigger_eff_kwargs
            )

            if args.verbose:
                for label, value, error, formula in data_results._results:
                    output.add(f"[data] {label}", value, error, formula)

            output.add("N_est (data)", n_est_data, err_data)

        # Closure: reco - truth
        diff_reco = n_est_reco - n_obs
        err_diff_reco = math.sqrt(err_reco**2 + err_n_obs**2)
        sigma_reco = diff_reco / err_diff_reco if err_diff_reco > 0 else 0.0
        output.add("reco - truth", diff_reco, err_diff_reco, formula=f"{sigma_reco:.2f} sigma")

        # Closure: data - truth (optional)
        if args.data_file:
            diff_data = n_est_data - n_obs
            err_diff_data = math.sqrt(err_data**2 + err_n_obs**2)
            sigma_data = diff_data / err_diff_data if err_diff_data > 0 else 0.0
            output.add("data - truth", diff_data, err_diff_data, formula=f"{sigma_data:.2f} sigma")

        output.print_results(nlayers, args.verbose)


if __name__ == "__main__":
    main()
