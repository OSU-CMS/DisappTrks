import argparse
import ctypes
import math
import ROOT

# N_est = N_ctrl × prescale × P_pass_veto × P_pass_met × P_pass_trigger / ε_trigger

FIDUCIAL_SIGMA_CUT = 2.0
DEFAULT_ERROR = 0.5 * ROOT.TMath.ChisquareQuantile(0.68, 2)
MET_CUT = 120.0
DELTA_PHI_CUT = 0.5

DEFAULT_LEPTON_TRIGGER_EFFICIENCY = {
    "electron": (0.840, 0.005),
    "muon": (0.940, 0.004),
    "tau": (0.900, 0.006),
}


def get_hist(file_name, hist_name):
    """Retrieve a histogram from a ROOT file.

    Args:
        file_name: Path to the ROOT file.
        hist_name: Full path to the histogram within the file.

    Returns:
        A cloned histogram detached from the file.

    Raises:
        SystemExit: If the histogram is not found.
    """
    root_file = ROOT.TFile.Open(file_name)
    hist = root_file.Get(hist_name)
    if not hist:
        print(f"[ERROR]: Histogram {hist_name} not found in {file_name}. Quitting.")
        exit(-1)

    hist = hist.Clone()
    hist.SetDirectory(0)
    root_file.Close()
    return hist


def get_hists(file_name, nlayers):
    """Load all histograms needed for the background estimate.

    Args:
        file_name: Path to the ROOT file containing the histograms.
        nlayers: Number of tracker layers ("4", "5", or "6").

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

    hists = {}
    hists["n_tagged"] = {
        "metVsFiducial": get_hist(file_name, f"ElectronTagPt55NLayers{nlayers_str}Plotter/Track-met Plots/metNoMuVsMaxSigmaForFiducialElectronTrack")
    }
    hists["pass_veto"] = {
        "total_tp_pairs": get_hist(file_name, f"ZtoEleProbeTrkNLayers{nlayers_str}Plotter/Eventvariable Plots/nGoodTPPairs"),
        "ss_tp_pairs": get_hist(file_name, f"ZtoEleProbeTrkNLayers{nlayers_str}Plotter/Eventvariable Plots/nGoodSSTPPairs"),
        "passing_veto_probes": get_hist(file_name, f"ZtoEleProbeTrkWithFilterNLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesPassingVeto"),
        "metNoMu": get_hist(file_name, f"ZtoEleProbeTrkWithSSFilterNLayers{nlayers_str}Plotter/Met Plots/metNoMu")
    }
    hists["pass_met_cut"] = {
        "deltaPhiVsMet": get_hist(file_name, f"ElectronTagPt55NLayers{nlayers_str}Plotter/Electron-eventvariable Plots/deltaPhiMetJetLeadingVsElectronMetNoMuMinusOnePt")
    }
    hists["trigger_efficiency"] = {
        "passes": get_hist(file_name, f"ElectronTagPt55MetTrigNLayers{nlayers_str}Plotter/Met Plots/metNoMu"),
        "total": get_hist(file_name, f"ElectronTagPt55NLayers{nlayers_str}Plotter/Met Plots/metNoMu")
    }
    hists["pass_trigger"] = {
        "deltaPhiVsMet": get_hist(file_name, f"ElectronTagPt55NLayers{nlayers_str}Plotter/Electron-eventvariable Plots/deltaPhiMetJetLeadingVsElectronMetNoMuMinusOnePt")
    }
    hists["lepton_trigger_efficiency"] = {
        "nProbesPT55": get_hist(file_name, f"ZtoEleProbeTrkNLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesPT55"),
        "nProbesSSPT55": get_hist(file_name, f"ZtoEleProbeTrkNLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesSSPT55"),
        "nProbesFiringTrigger": get_hist(file_name, f"ZtoEleProbeTrkNLayers{nlayers_str}Plotter/Eventvariable Plots/nProbesFiringTrigger"),
        "nSSProbesFiringTrigger": get_hist(file_name, f"ZtoEleProbeTrkNLayers{nlayers_str}Plotter/Eventvariable Plots/nSSProbesFiringTrigger"),
    }
    return hists


def get_combined_hists(file_name):
    """Load and sum histograms across all nlayers for combined estimate.

    Loads histograms for nlayers 4, 5, and 6, then sums them together
    to produce combined histograms for a single background estimate.

    Args:
        file_name: Path to the ROOT file containing the histograms.

    Returns:
        Dictionary of histogram dictionaries with the same structure as
        get_hists(), but with histograms summed across all nlayers.
    """
    hists_4 = get_hists(file_name, "4")
    hists_5 = get_hists(file_name, "5")
    hists_6 = get_hists(file_name, "6")

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
    for bin_idx in range(1, hist.GetNbinsX() + 1):
        # Bin index 1 is the first bin - index 0 is underflow
        total += (bin_idx) * hist.GetBinContent(bin_idx + 1)
        error = math.hypot(error, (bin_idx) * hist.GetBinError(bin_idx + 1))

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


def get_prob_pass_veto(hists):
    """Calculate the probability that a probe track passes the lepton veto.

    Uses tag-and-probe with same-sign subtraction to estimate OS background:
    P_pass_veto = (N_pass_all - N_pass_SS) / (N_total_all - N_total_SS)

    The histograms contain the number of events with N tag-probe pairs, so
    we weight by (bin_idx - 1) to count individual probes.

    Args:
        hists: Dictionary containing total_tp_pairs, ss_tp_pairs,
               passing_veto_probes, and metNoMu histograms.

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
        print("[ERROR]: When calculating P(pass veto), found negative OS tag/probe pairs. Exiting.")
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

    return prob_pass_veto, err_prob_pass_veto


def get_prob_pass_met(hists, n_tagged, err_n_tagged):
    """Calculate probability of passing the MET and delta-phi cuts.

    Integrates the 2D delta-phi vs MET histogram in the signal region
    (MET > MET_CUT and delta-phi > DELTA_PHI_CUT) and normalizes by
    the number of tagged leptons.

    Args:
        hists: Dictionary containing the deltaPhiVsMet histogram.
        n_tagged: Number of tagged leptons (denominator).
        err_n_tagged: Error on n_tagged.

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


def get_prob_pass_trigger(hists, trigger_efficiency_hist):
    """Calculate probability of passing the MET trigger.

    Projects the delta-phi vs MET histogram onto MET, weights each bin
    by the trigger efficiency at that MET value, and computes the
    fraction of events in the signal region that would pass the trigger.

    Args:
        hists: Dictionary containing the deltaPhiVsMet histogram.
        trigger_efficiency_hist: MET trigger efficiency histogram from
            get_trigger_efficiency_hist().

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

    return prob_pass_trigger, err_prob_pass_trigger


def calculate_lepton_trigger_efficiency(hists):
    """Calculate lepton trigger efficiency from tag-and-probe histograms.

    Uses same-sign pairs to estimate background contamination:
    efficiency = (passes - SS_passes) / (total - SS_total)

    Args:
        hists: Dictionary with nProbesPT55, nProbesSSPT55,
               nProbesFiringTrigger, nSSProbesFiringTrigger histograms

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
        print("[ERROR]: When calculating lepton trigger efficiency, denominator is <= 0. Exiting.")
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

    return efficiency, err_efficiency


def format_latex_value(value, error, precision=2):
    """Format a value and error for LaTeX output.

    If the central value is less than the uncertainty, uses asymmetric
    error format with lower bound clamped at zero. For very small values
    (< 0.01), uses scientific notation.

    Args:
        value: Central value.
        error: Uncertainty on the value.
        precision: Number of decimal places for the mantissa.

    Returns:
        LaTeX-formatted string like "$1.23 \\pm 0.04$" or
        "$(1.23_{{-1.23}}^{{+2.00}}) \\times 10^{{-3}}$".
    """
    use_asymmetric = value < error

    # Check if we need scientific notation
    if value != 0 and abs(value) < 0.01:
        exponent = int(math.floor(math.log10(abs(value))))
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


def get_flat_lepton_trigger_efficiency(lepton_type, flat_efficiency):
    """Get a flat lepton trigger efficiency.

    Args:
        lepton_type: One of "electron", "muon", or "tau"
        flat_efficiency: User-specified flat efficiency value, or -1 to use
                        the default for the lepton type.

    Returns:
        Tuple of (efficiency, error)
    """
    if flat_efficiency == -1:
        return DEFAULT_LEPTON_TRIGGER_EFFICIENCY[lepton_type]

    return flat_efficiency, 0.005


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
    # TODO: Change what histograms we look for depending on lepton type
    # TODO: implement tau stuff
    parser.add_argument(
        "--lepton-type",
        choices=["electron", "muon", "tau"],
        required=True,
        help="Type of lepton background to estimate"
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
    args = parser.parse_args()

    if args.nlayers == "all":
        nlayers_to_run = ["4", "5", "6", "combined"]
    else:
        nlayers_to_run = [args.nlayers]

    for nlayers in nlayers_to_run:
        if nlayers == "combined":
            hists = get_combined_hists(args.file_name)
        else:
            hists = get_hists(args.file_name, nlayers)

        n_tagged, err_n_tagged = get_n_tagged(hists["n_tagged"])
        p_pass_lept_veto, err_pass_lept_veto = get_prob_pass_veto(hists["pass_veto"])
        p_pass_met_cut, err_pass_met_cut = get_prob_pass_met(hists["pass_met_cut"], n_tagged, err_n_tagged)
        h_met_trig_eff = get_trigger_efficiency_hist(hists["trigger_efficiency"])
        prob_pass_met_trig, err_pass_met_trig = get_prob_pass_trigger(hists["pass_trigger"], h_met_trig_eff)

        if args.flat_lepton_trigger_efficiency is None:
            lept_trig_eff, err_lept_trig_eff = calculate_lepton_trigger_efficiency(hists["lepton_trigger_efficiency"])
        else:
            lept_trig_eff, err_lept_trig_eff = get_flat_lepton_trigger_efficiency(
                args.lepton_type, args.flat_lepton_trigger_efficiency
            )

        n_est = n_tagged * p_pass_lept_veto * p_pass_met_cut * prob_pass_met_trig / lept_trig_eff
        err_n_est = math.sqrt(
            (p_pass_lept_veto * p_pass_met_cut * prob_pass_met_trig / lept_trig_eff * err_n_tagged)**2 +
            (n_tagged * p_pass_met_cut * prob_pass_met_trig / lept_trig_eff * err_pass_lept_veto)**2 +
            (n_tagged * p_pass_lept_veto * prob_pass_met_trig / lept_trig_eff * err_pass_met_cut)**2 +
            (n_tagged * p_pass_lept_veto * p_pass_met_cut / lept_trig_eff * err_pass_met_trig)**2 +
            (n_tagged * p_pass_lept_veto * p_pass_met_cut * prob_pass_met_trig / (lept_trig_eff**2) * err_lept_trig_eff)**2
        )

        # TODO: use scientific notation if necessary
        if args.output_fmt == "default":
            print(f"=== NLayers {nlayers} ===")
            print(f"N_tagged:              {n_tagged:.1f} +/- {err_n_tagged:.1f}")
            print(f"P(pass lepton veto):   {p_pass_lept_veto:.4f} +/- {err_pass_lept_veto:.4f}")
            print(f"P(pass MET cut):       {p_pass_met_cut:.6f} +/- {err_pass_met_cut:.6f}")
            print(f"P(pass MET trigger):   {prob_pass_met_trig:.4f} +/- {err_pass_met_trig:.4f}")
            print(f"Lepton trigger eff:    {lept_trig_eff:.4f} +/- {err_lept_trig_eff:.4f}")
            print(f"N_est:                 {n_est:.4f} +/- {err_n_est:.4f}")
            print()
        else:
            cols = [
                format_latex_value(lept_trig_eff, err_lept_trig_eff, precision=3),
                format_latex_value(n_tagged, err_n_tagged, precision=0),
                format_latex_value(p_pass_lept_veto, err_pass_lept_veto, precision=4),
                format_latex_value(p_pass_met_cut, err_pass_met_cut, precision=2),
                format_latex_value(prob_pass_met_trig, err_pass_met_trig, precision=3),
                format_latex_value(n_est, err_n_est, precision=2),
            ]
            nlayers_label = r"\geq 6" if nlayers == "6" else nlayers
            print(r"\multirow{4}{*}{YEAR} & " + f"${nlayers_label}$ & " + " & ".join(cols) + r" \\")


if __name__ == "__main__":
    main()
