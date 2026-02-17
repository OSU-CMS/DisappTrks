import ctypes
import math
import ROOT

from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import lumi


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


def _get_total_and_error(hist, min_cut=None, max_cut=None):
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


def _get_weighted_total_and_error(hist):
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


def get_n_ctrl(hists):
    """Count the number of tagged leptons in the control region.

    Projects the 2D MET vs fiducial sigma histogram onto the MET axis,
    selecting only tracks within the fiducial region (sigma < FIDUCIAL_SIGMA_CUT).

    Args:
        hists: Dictionary containing the metVsFiducial histogram.

    Returns:
        Tuple of (n_ctrl, error).
    """
    # TODO: Compare this method to the "backup" method. If they are the same, use the easier one
    met_hist_1d = hists["metVsFiducial"].ProjectionY(
        "metNoMu_Projected",
        0,
        hists["metVsFiducial"].GetXaxis().FindBin(FIDUCIAL_SIGMA_CUT) - 1
    )

    total, error = _get_total_and_error(met_hist_1d)
    if total == 0.0:
        error = DEFAULT_ERROR
    return total, error


def get_prob_pass_veto(hists, results):
    """Calculate the probability that a probe track passes the lepton veto.

    Uses tag-and-probe with same-sign subtraction to estimate OS background:
    P_pass_veto = (N_pass_all - N_pass_SS) / (N_total_all - N_total_SS)

    The histograms contain the number of events with N tag-probe pairs, so
    we weight by (bin_idx - 1) to count individual probes.

    Args:
        hists: Dictionary containing total_tp_pairs, ss_tp_pairs,
               passing_veto_probes, and metNoMu histograms.
        results: LeptonBackgroundFormatter object to record the result.

    Returns:
        Tuple of (probability, error).

    Raises:
        SystemExit: If OS pairs would be negative.
    """
    n_total_all, err_total_all = _get_weighted_total_and_error(hists["total_tp_pairs"])
    n_total_ss, err_total_ss = _get_weighted_total_and_error(hists["ss_tp_pairs"])
    n_pass_all, err_pass_all = _get_weighted_total_and_error(hists["passing_veto_probes"])
    n_pass_ss, err_pass_ss = _get_total_and_error(hists["metNoMu"])

    if n_total_all < n_total_ss:
        print("When calculating P(pass veto), found negative OS tag/probe pairs. Exiting.")
        exit(-1)

    numer = n_pass_all - n_pass_ss
    denom = n_total_all - n_total_ss

    if numer < 0:
        prob_pass_veto = 0.0
        err_prob_pass_veto = DEFAULT_ERROR / denom
    else:
        prob_pass_veto = numer / denom
        err_numer = math.sqrt(err_pass_all * err_pass_all + err_pass_ss * err_pass_ss)
        err_denom = math.sqrt(err_total_all * err_total_all + err_total_ss * err_total_ss)
        err_prob_pass_veto = math.sqrt(
            (err_numer * denom)**2 + (numer * err_denom)**2
        ) / (denom * denom)

    formula = f"({n_pass_all:.1f} - {n_pass_ss:.1f}) / ({n_total_all:.1f} - {n_total_ss:.1f})"
    results.add("P(pass lepton veto)", prob_pass_veto, err_prob_pass_veto, formula=formula)
    return prob_pass_veto, err_prob_pass_veto


def get_prob_pass_met(hists, lumi_scale_factor, results):
    """Calculate probability of passing the MET and delta-phi cuts.

    Integrates the 2D delta-phi vs MET histogram in the signal region
    (MET > MET_CUT and delta-phi > DELTA_PHI_CUT) and normalizes by
    the number of tagged leptons.

    Args:
        hists: Dictionary containing the deltaPhiVsMet histogram and an
            n_ctrl histogram dict used as the denominator.
        lumi_scale_factor: Ratio of MET to lepton dataset luminosity.
        results: LeptonBackgroundResults object to record the result.

    Returns:
        Tuple of (probability, error).
    """
    n_ctrl, err_n_ctrl = get_n_ctrl(hists["n_ctrl"])
    n_ctrl *= lumi_scale_factor
    err_n_ctrl *= lumi_scale_factor

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
        err_prob_pass_met = DEFAULT_ERROR / n_ctrl
    else:
        prob_pass_met = n_pass / n_ctrl
        err_prob_pass_met = prob_pass_met * math.sqrt(
            (err_pass / n_pass) ** 2 + (err_n_ctrl / n_ctrl) ** 2
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

    Selects events passing the delta-phi cut, projects onto the MET
    axis, weights each bin by the trigger efficiency at that MET value,
    and computes the fraction that would pass the trigger.

    Args:
        hists: Dictionary containing the deltaPhiVsMet histogram.
        trigger_efficiency_hist: MET trigger efficiency histogram from
            get_trigger_efficiency_hist().
        results: LeptonBackgroundFormatter object to record the result.

    Returns:
        Tuple of (probability, error).
    """
    dphi_vs_met = hists["deltaPhiVsMet"].Clone("dphi_vs_met_for_trigger")
    dphi_vs_met.SetDirectory(0)
    dphi_vs_met.GetYaxis().SetRangeUser(DELTA_PHI_CUT, 4.0)

    passes_trig_hist = dphi_vs_met.ProjectionX("met")
    passes_trig_hist.SetDirectory(0)
    passes_trig_hist.Multiply(trigger_efficiency_hist)

    n_passes, err_passes = _get_total_and_error(passes_trig_hist, min_cut=MET_CUT)

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
        results: LeptonBackgroundFormatter object to record the result.

    Returns:
        Tuple of (efficiency, error)
    """
    total, err_total = _get_weighted_total_and_error(hists["nProbesPT55"])
    total_ss, err_total_ss = _get_weighted_total_and_error(hists["nProbesSSPT55"])
    passes, err_passes = _get_weighted_total_and_error(hists["nProbesFiringTrigger"])
    passes_ss, err_passes_ss = _get_weighted_total_and_error(hists["nSSProbesFiringTrigger"])

    if passes == 0.0:
        err_passes = DEFAULT_ERROR
    if passes_ss == 0.0:
        err_passes_ss = DEFAULT_ERROR

    numer = passes - passes_ss
    denom = total - total_ss

    if denom <= 0:
        print("When calculating lepton trigger efficiency, denominator is <= 0. Exiting.")
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


def calculate_n_est(hists, year, era,
                    lepton_type, results,
                    lepton_trigger_efficiency=None, lepton_trigger_efficiency_error=None):
    """Calculate the estimated lepton background N_est.

    Computes N_est = N_ctrl * P(pass veto) * P(pass MET cut) * P(pass MET trigger) / ε_lepton_trigger
    with full error propagation. Intermediate results are recorded in the results.

    Args:
        hists: Dictionary of histogram dictionaries for this nlayers. When
            combined MET histograms are needed (muon/tau at nlayers 4 and 5),
            the MET categories and a 'combined_met_n_ctrl' key should already
            be substituted by the histogram loader.
        year: Data-taking year (e.g. "2022").
        era: Run era (e.g. "D", "CD", "EFG").
        lepton_type: Type of lepton ("electron", "muon", or "tau").
        results: Formatter object with add_result(label, value, error, formula="") method.
        lepton_trigger_efficiency: If provided, use this flat value instead of
            calculating from histograms.
        lepton_trigger_efficiency_error: Error on the flat efficiency. Required
            when lepton_trigger_efficiency is provided.

    Returns:
        Tuple of (n_est, err_n_est).
    """
    lumi_scale_factor = get_lumi_scale_factor(lepton_type, year, era)
    results.add("Lumi scale factor", lumi_scale_factor, 0.0)

    n_ctrl, err_n_ctrl = get_n_ctrl(hists["n_ctrl"])
    results.add("N_ctrl (unscaled)", n_ctrl, err_n_ctrl)
    n_ctrl *= lumi_scale_factor
    err_n_ctrl *= lumi_scale_factor
    results.add("N_ctrl", n_ctrl, err_n_ctrl)

    p_pass_lept_veto, err_pass_lept_veto = get_prob_pass_veto(hists["pass_veto"], results)
    p_pass_met_cut, err_pass_met_cut = get_prob_pass_met(hists["pass_met_cut"], lumi_scale_factor, results)
    h_met_trig_eff = get_trigger_efficiency_hist(hists["trigger_efficiency"])
    prob_pass_met_trig, err_pass_met_trig = get_prob_pass_trigger(hists["pass_trigger"], h_met_trig_eff, results)

    if lepton_trigger_efficiency is not None:
        lept_trig_eff = lepton_trigger_efficiency
        err_lept_trig_eff = lepton_trigger_efficiency_error
        results.add("Lepton trigger eff", lept_trig_eff, err_lept_trig_eff)
    else:
        lept_trig_eff, err_lept_trig_eff = calculate_lepton_trigger_efficiency(hists["lepton_trigger_efficiency"], results)

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
    results.add("N_est", n_est, err_n_est, formula=n_est_formula)

    return n_est, err_n_est
