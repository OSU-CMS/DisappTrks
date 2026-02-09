# TODOs:
# - need to implement plotting. I think having a plotting class and then pass a --plot flag would be useful. The plots should be ready for the analysis note, i.e. we don't need createBackgroundPlots.py anymore
# - for muon/tau nlayers=4/5, need to use the combined (4+5+6) P(pass MET cut) and P(pass MET trigger) values
# - implement tau functionality

import argparse
import ctypes
from dataclasses import dataclass
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import lumi
from DisappTrks.StandardAnalysis.plotUtilities import get_hist
import logging
import math
import ROOT
from tabulate import tabulate


logging.basicConfig(format="%(message)s")
logger = logging.getLogger(__name__)

FIDUCIAL_SIGMA_CUT = 2.0
DEFAULT_ERROR = 0.5 * ROOT.TMath.ChisquareQuantile(0.68, 2)
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


@dataclass
class IntermediateResult:
    label: str
    value: float
    error: float
    formula: str = ""


class IntermediateResults:
    """Collects results from each calculation step."""

    def __init__(self):
        self._results = []

    def add(self, label, value, error, formula=""):
        self._results.append(IntermediateResult(label, value, error, formula))

    def _format_default(self, result, is_verbose):
        value_str = f"{result.value:.8g} +/- {result.error:.8g}"

        row = [result.label, value_str]
        if is_verbose:
            row.append(result.formula)

        return row

    def _format_latex_value(self, value, error, precision=2, use_sci_notation=False):
        """Format a value and error for LaTeX output.

        If the central value is less than the uncertainty, uses asymmetric
        error format with lower bound clamped at zero. If use_sci_notation
        is set, forces scientific notation of the form
        (X +/- Y) x 10^z (or with asymmetric errors). When the value is
        zero, the exponent is derived from the error.

        Args:
            value: Central value.
            error: Uncertainty on the value.
            precision: Number of decimal places for the mantissa.
            use_sci_notation: Force scientific notation output.

        Returns:
            LaTeX-formatted string like "$1.23 \\pm 0.04$" or
            "$(1.23_{{-1.23}}^{{+2.00}}) \\times 10^{{-3}}$".
        """
        use_asymmetric = value < error

        if use_sci_notation:
            if value != 0:
                exponent = int(math.floor(math.log10(abs(value))))
            else:
                exponent = int(math.floor(math.log10(abs(error))))
            mantissa = value / (10 ** exponent)
            err_mantissa = error / (10 ** exponent)

            if use_asymmetric:
                return (f"$({mantissa:.{precision}f}_{{-{mantissa:.{precision}f}}}"
                        f"^{{+{err_mantissa:.{precision}f}}}) \\times 10^{{{exponent}}}$")
            else:
                return f"$({mantissa:.{precision}f} \\pm {err_mantissa:.{precision}f}) \\times 10^{{{exponent}}}$"
        else:
            if use_asymmetric:
                return f"${value:.{precision}f}_{{-{value:.{precision}f}}}^{{+{error:.{precision}f}}}$"
            else:
                return f"${value:.{precision}f} \\pm {error:.{precision}f}$"

    def print_default(self, nlayers, is_verbose):
        by_label = {r.label: r for r in self._results}
        rows = [
            self._format_default(by_label["Lumi scale factor"], is_verbose),
            self._format_default(by_label["Lepton trigger eff"], is_verbose),
            self._format_default(by_label["N_tagged (unscaled)"], is_verbose),
            self._format_default(by_label["N_tagged"], is_verbose),
            self._format_default(by_label["P(pass lepton veto)"], is_verbose),
            self._format_default(by_label["P(pass MET cut)"], is_verbose),
            self._format_default(by_label["P(pass MET trigger)"], is_verbose),
            self._format_default(by_label["N_est"], is_verbose)
        ]

        headers = [f"NLayers {nlayers}", "Value"]
        if is_verbose:
            headers.append("Details")

        print(tabulate(rows, headers=headers, tablefmt="simple_outline"))
        print()

    def print_latex(self, nlayers, include_year=False):
        by_label = {r.label: r for r in self._results}
        cols = [
            self._format_latex_value(by_label["Lepton trigger eff"].value, by_label["Lepton trigger eff"].error, precision=3),
            self._format_latex_value(by_label["N_tagged"].value, by_label["N_tagged"].error, precision=0),
            self._format_latex_value(by_label["P(pass lepton veto)"].value, by_label["P(pass lepton veto)"].error, precision=2, use_sci_notation=True),
            self._format_latex_value(by_label["P(pass MET cut)"].value, by_label["P(pass MET cut)"].error, precision=3),
            self._format_latex_value(by_label["P(pass MET trigger)"].value, by_label["P(pass MET trigger)"].error, precision=3),
            self._format_latex_value(by_label["N_est"].value, by_label["N_est"].error, precision=2),
        ]
        nlayers_label = r"\geq 6" if nlayers == "6" else nlayers

        if include_year:
            print(r"\multirow{4}{*}{YEAR} & " + f"${nlayers_label}$ & " + " & ".join(cols) + r" \\")
        else:
            print(f"& ${nlayers_label}$ & " + " & ".join(cols) + r" \\")


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
        logger.error(
            f"Luminosity not found for: {', '.join(missing)}. "
            f"Check that era '{era}' is valid for year '{year}', "
            f"or add the luminosity to StandardAnalysis/python/IntegratedLuminosity_cff.py."
        )
        exit(-1)

    return lumi[met_key] / lumi[lepton_key]


def get_hists(file_name, nlayers, lepton_type):
    """Load all histograms needed for the background estimate.

    Args:
        file_name: Path to the ROOT file containing the histograms.
        nlayers: Number of tracker layers ("4", "5", or "6").
        lepton_type: Type of lepton ("electron" or "muon").

    Returns:
        Dictionary of histogram dictionaries, organized by calculation step:
        - n_tagged: Histograms for counting tagged leptons
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
    hists["n_tagged"] = {
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


def get_total_and_error(hist, min_cut=None, max_cut=None):
    """Integrate a histogram and compute the error.

    Args:
        hist: ROOT histogram to integrate.
        min_cut: Minimum value for integration range (None for underflow).
        max_cut: Maximum value for integration range (None for overflow).

    Returns:
        Tuple of (integral, error). Error is clamped to not exceed the total
        when the difference would be negative.
    """
    min_bin = 0 if min_cut is None else hist.FindBin(min_cut)
    max_bin = -1 if max_cut is None else hist.FindBin(max_cut)
    error = ctypes.c_double()
    total = hist.IntegralAndError(min_bin, max_bin, error) # Error is assigned by reference
    error = error.value # Shed the ctype

    if total - error < 0.0:
        error = total

    return total, error


def get_weighted_total_and_error(hist):
    """Compute weighted sum of histogram where bin content is event counts.

    For histograms where bin N contains the number of events with N probes,
    this computes the total number of probes by weighting each bin by its
    index: total = 1*N(1) + 2*N(2) + 3*N(3) + ...

    Args:
        hist: ROOT histogram where bin index represents multiplicity.

    Returns:
        Tuple of (weighted_total, error).
    """
    total = error = 0.0
    # Bin 0 is underflow, bin 1 is multiplicity 0, bin 2 is multiplicity 1, etc.
    for bin_idx in range(2, hist.GetNbinsX() + 1):
        multiplicity = bin_idx - 1
        total += multiplicity * hist.GetBinContent(bin_idx)
        error = math.hypot(error, multiplicity * hist.GetBinError(bin_idx))

    return total, error

def get_n_tagged(hists):
    """Count the number of tagged leptons in the control region.

    Projects the 2D MET vs fiducial sigma histogram onto the MET axis,
    selecting only tracks within the fiducial region (sigma < FIDUCIAL_SIGMA_CUT).

    Args:
        hists: Dictionary containing the metVsFiducial histogram.

    Returns:
        Tuple of (n_tagged, error).
    """
    # TODO: Compare this method to the "backup" method. If they are the same, use the easier one
    met_hist_1d = hists["metVsFiducial"].ProjectionY(
        "metNoMu_Projected",
        0,
        hists["metVsFiducial"].GetXaxis().FindBin(FIDUCIAL_SIGMA_CUT) - 1
    )

    return get_total_and_error(met_hist_1d)


def get_prob_pass_veto(hists, results):
    """Calculate the probability that a probe track passes the lepton veto.

    Uses tag-and-probe with same-sign subtraction to estimate OS background:
    P_pass_veto = (N_pass_all - N_pass_SS) / (N_total_all - N_total_SS)

    The histograms contain the number of events with N tag-probe pairs, so
    we weight by (bin_idx - 1) to count individual probes.

    Args:
        hists: Dictionary containing total_tp_pairs, ss_tp_pairs,
               passing_veto_probes, and metNoMu histograms.
        results: IntermediateResults object to record the result.

    Returns:
        Tuple of (probability, error).

    Raises:
        SystemExit: If OS pairs would be negative.
    """
    n_total_all, err_total_all = get_weighted_total_and_error(hists["total_tp_pairs"])
    n_total_ss, err_total_ss = get_weighted_total_and_error(hists["ss_tp_pairs"])
    n_pass_all, err_pass_all = get_weighted_total_and_error(hists["passing_veto_probes"])
    n_pass_ss, err_pass_ss = get_total_and_error(hists["metNoMu"])

    if n_total_all < n_total_ss:
        logger.error("When calculating P(pass veto), found negative OS tag/probe pairs. Exiting.")
        exit(-1)

    numer = n_pass_all - n_pass_ss
    denom = n_total_all - n_total_ss

    if numer <= 0:
        prob_pass_veto = 0.0
        err_prob_pass_veto = DEFAULT_ERROR / denom
    else:
        prob_pass_veto = numer / denom
        err_numer = math.sqrt(err_pass_all * err_pass_all + err_pass_ss * err_pass_ss)
        err_denom = math.sqrt(err_total_all * err_total_all + err_total_ss * err_total_ss)
        err_prob_pass_veto = prob_pass_veto * math.sqrt(
            (err_numer / numer)**2 + (err_denom / denom)**2
        )

    formula = f"({n_pass_all:.1f} - {n_pass_ss:.1f}) / ({n_total_all:.1f} - {n_total_ss:.1f})"
    results.add("P(pass lepton veto)", prob_pass_veto, err_prob_pass_veto, formula=formula)
    return prob_pass_veto, err_prob_pass_veto


def get_prob_pass_met(hists, n_tagged, err_n_tagged, results):
    """Calculate probability of passing the MET and delta-phi cuts.

    Integrates the 2D delta-phi vs MET histogram in the signal region
    (MET > MET_CUT and delta-phi > DELTA_PHI_CUT) and normalizes by
    the number of tagged leptons.

    Args:
        hists: Dictionary containing the deltaPhiVsMet histogram.
        n_tagged: Number of tagged leptons (denominator).
        err_n_tagged: Error on n_tagged.
        results: IntermediateResults object to record the result.

    Returns:
        Tuple of (probability, error).
    """
    lower_met_bin = hists["deltaPhiVsMet"].GetXaxis().FindBin(MET_CUT)
    upper_met_bin = hists["deltaPhiVsMet"].GetNbinsX() + 1
    lower_delta_phi_bin = hists["deltaPhiVsMet"].GetYaxis().FindBin(DELTA_PHI_CUT)
    upper_delta_phi_bin = hists["deltaPhiVsMet"].GetNbinsY() + 1

    err_pass = ctypes.c_double(0.0)
    n_pass = hists["deltaPhiVsMet"].IntegralAndError(
        lower_met_bin, upper_met_bin,
        lower_delta_phi_bin, upper_delta_phi_bin,
        err_pass
    )
    err_pass = err_pass.value

    if n_pass <= 0:
        prob_pass_met = 0.0
        err_prob_pass_met = DEFAULT_ERROR / n_tagged
    else:
        prob_pass_met = n_pass / n_tagged
        err_prob_pass_met = prob_pass_met * math.sqrt(
            (err_pass / n_pass) ** 2 + (err_n_tagged / n_tagged) ** 2
        )

    results.add("P(pass MET cut)", prob_pass_met, err_prob_pass_met)
    return prob_pass_met, err_prob_pass_met


def get_trigger_efficiency_hist(hists):
    """Create a MET trigger efficiency histogram.

    Divides the histogram of events passing the MET trigger by the
    total number of events to produce an efficiency vs MET histogram.

    Args:
        hists: Dictionary containing 'passes' and 'total' histograms.

    Returns:
        ROOT histogram of trigger efficiency as a function of MET.
    """
    trigger_eff_hist = hists["passes"].Clone()
    trigger_eff_hist.SetDirectory(0)
    trigger_eff_hist.Divide(hists["total"])
    return trigger_eff_hist


def get_prob_pass_trigger(hists, trigger_efficiency_hist, results):
    """Calculate probability of passing the MET trigger.

    Projects the delta-phi vs MET histogram onto MET, weights each bin
    by the trigger efficiency at that MET value, and computes the
    fraction of events in the signal region that would pass the trigger.

    Args:
        hists: Dictionary containing the deltaPhiVsMet histogram.
        trigger_efficiency_hist: MET trigger efficiency histogram from
            get_trigger_efficiency_hist().
        results: IntermediateResults object to record the result.

    Returns:
        Tuple of (probability, error).
    """
    passes_trig_hist = hists["deltaPhiVsMet"].ProjectionX("met")
    passes_trig_hist.SetDirectory(0)
    passes_trig_hist.Multiply(trigger_efficiency_hist)

    n_passes, err_passes = get_total_and_error(passes_trig_hist, min_cut=MET_CUT)

    lower_met_bin = hists["deltaPhiVsMet"].GetXaxis().FindBin(MET_CUT)
    upper_met_bin = hists["deltaPhiVsMet"].GetNbinsX() + 1
    lower_delta_phi_bin = hists["deltaPhiVsMet"].GetYaxis().FindBin(DELTA_PHI_CUT)
    upper_delta_phi_bin = hists["deltaPhiVsMet"].GetNbinsY() + 1

    err_total = ctypes.c_double(0.0)
    n_total = hists["deltaPhiVsMet"].IntegralAndError(
        lower_met_bin, upper_met_bin,
        lower_delta_phi_bin, upper_delta_phi_bin,
        err_total
    )
    err_total = err_total.value

    if n_passes <= 0:
        prob_pass_trigger = 0.0
        err_prob_pass_trigger = DEFAULT_ERROR / n_total
    else:
        prob_pass_trigger = n_passes / n_total
        err_prob_pass_trigger = prob_pass_trigger * math.sqrt(
            (err_passes / n_passes) ** 2 + (err_total / n_total) ** 2
        )

    results.add("P(pass MET trigger)", prob_pass_trigger, err_prob_pass_trigger)
    return prob_pass_trigger, err_prob_pass_trigger


def calculate_lepton_trigger_efficiency(hists, results):
    """Calculate lepton trigger efficiency from tag-and-probe histograms.

    Uses same-sign pairs to estimate background contamination:
    efficiency = (passes - SS_passes) / (total - SS_total)

    Args:
        hists: Dictionary with nProbesPT55, nProbesSSPT55,
               nProbesFiringTrigger, nSSProbesFiringTrigger histograms
        results: IntermediateResults object to record the result.

    Returns:
        Tuple of (efficiency, error)
    """
    total, err_total = get_weighted_total_and_error(hists["nProbesPT55"])
    total_ss, err_total_ss = get_weighted_total_and_error(hists["nProbesSSPT55"])
    passes, err_passes = get_weighted_total_and_error(hists["nProbesFiringTrigger"])
    passes_ss, err_passes_ss = get_weighted_total_and_error(hists["nSSProbesFiringTrigger"])

    if passes == 0.0:
        err_passes = DEFAULT_ERROR
    if passes_ss == 0.0:
        err_passes_ss = DEFAULT_ERROR

    numer = passes - passes_ss
    denom = total - total_ss

    if denom <= 0:
        logger.error("When calculating lepton trigger efficiency, denominator is <= 0. Exiting.")
        exit(-1)

    if numer <= 0:
        efficiency = 0.0
        err_efficiency = DEFAULT_ERROR / denom
    else:
        efficiency = numer / denom
        err_numer = math.sqrt(err_passes**2 + err_passes_ss**2)
        err_denom = math.sqrt(err_total**2 + err_total_ss**2)
        err_efficiency = efficiency * math.sqrt(
            (err_numer / numer)**2 + (err_denom / denom)**2
        )

    formula = f"({passes:.1f} - {passes_ss:.1f}) / ({total:.1f} - {total_ss:.1f})"
    results.add("Lepton trigger eff", efficiency, err_efficiency, formula=formula)
    return efficiency, err_efficiency


def get_flat_lepton_trigger_efficiency(lepton_type, flat_efficiency, results):
    """Get a flat lepton trigger efficiency.

    Args:
        lepton_type: One of "electron", "muon", or "tau"
        flat_efficiency: User-specified flat efficiency value, or -1 to use
                        the default for the lepton type.
        results: IntermediateResults object to record the result.

    Returns:
        Tuple of (efficiency, error)
    """
    if flat_efficiency == -1:
        eff, err = DEFAULT_LEPTON_TRIGGER_EFFICIENCY[lepton_type]
    else:
        eff, err = flat_efficiency, 0.005

    results.add("Lepton trigger eff", eff, err)
    return eff, err


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
    # TODO: implement tau support
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
        required=True,
        help="Run era (e.g. D, CD, EFG)"
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
    args = parser.parse_args()

    lumi_scale_factor = get_lumi_scale_factor(args.lepton_type, args.year, args.era)

    if args.nlayers == "all":
        nlayers_to_run = ["4", "5", "6", "combined"]
    else:
        nlayers_to_run = [args.nlayers]

    for i, nlayers in enumerate(nlayers_to_run):
        if nlayers == "combined":
            hists = get_combined_hists(args.file_name, args.lepton_type)
        else:
            hists = get_hists(args.file_name, nlayers, args.lepton_type)

        results = IntermediateResults()
        results.add("Lumi scale factor", lumi_scale_factor, 0.0)

        n_tagged, err_n_tagged = get_n_tagged(hists["n_tagged"])
        results.add("N_tagged (unscaled)", n_tagged, err_n_tagged)
        n_tagged *= lumi_scale_factor
        err_n_tagged *= lumi_scale_factor
        results.add("N_tagged", n_tagged, err_n_tagged)

        p_pass_lept_veto, err_pass_lept_veto = get_prob_pass_veto(hists["pass_veto"], results)
        p_pass_met_cut, err_pass_met_cut = get_prob_pass_met(hists["pass_met_cut"], n_tagged, err_n_tagged, results)
        h_met_trig_eff = get_trigger_efficiency_hist(hists["trigger_efficiency"])
        prob_pass_met_trig, err_pass_met_trig = get_prob_pass_trigger(hists["pass_trigger"], h_met_trig_eff, results)

        if args.flat_lepton_trigger_efficiency is None:
            lept_trig_eff, err_lept_trig_eff = calculate_lepton_trigger_efficiency(hists["lepton_trigger_efficiency"], results)
        else:
            lept_trig_eff, err_lept_trig_eff = get_flat_lepton_trigger_efficiency(
                args.lepton_type, args.flat_lepton_trigger_efficiency, results
            )

        n_est = n_tagged * p_pass_lept_veto * p_pass_met_cut * prob_pass_met_trig / lept_trig_eff
        err_n_est = math.sqrt(
            (p_pass_lept_veto * p_pass_met_cut * prob_pass_met_trig / lept_trig_eff * err_n_tagged)**2 +
            (n_tagged * p_pass_met_cut * prob_pass_met_trig / lept_trig_eff * err_pass_lept_veto)**2 +
            (n_tagged * p_pass_lept_veto * prob_pass_met_trig / lept_trig_eff * err_pass_met_cut)**2 +
            (n_tagged * p_pass_lept_veto * p_pass_met_cut / lept_trig_eff * err_pass_met_trig)**2 +
            (n_tagged * p_pass_lept_veto * p_pass_met_cut * prob_pass_met_trig / (lept_trig_eff**2) * err_lept_trig_eff)**2
        )

        n_est_formula = (f"{n_tagged:.4g} * {p_pass_lept_veto:.4g} * {p_pass_met_cut:.4g} * "
                         f"{prob_pass_met_trig:.4g} / {lept_trig_eff:.4g}")
        results.add("N_est", n_est, err_n_est, formula=n_est_formula)

        if args.output_fmt == "default":
            results.print_default(nlayers, args.verbose)
        elif i == 0:
            results.print_latex(nlayers, include_year=True)
        else:
            results.print_latex(nlayers, include_year=False)


if __name__ == "__main__":
    main()
