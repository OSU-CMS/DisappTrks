import argparse
import math
import ROOT

DESCRIPTION="Estimates the probability an outer hit is missing."

DATA_HIST_NAME = "MuonCtrlSelectionPlotter/Track Plots/trackNHitsMissingOuter"
MC_HIST_NAME = "MuonCtrlSelectionPlotter/Track Plots/trackNHitsStripLayersVsTOBLayersVsMissingOuter"
CORRECTED_PRE_TOB_HITS_HIST_NAME = "CorrectedOuterHitsPreTOB"
CORRECTED_POST_TOB_HITS_HIST_NAME = "CorrectedOuterHitsPostTOB"

PRE_TOB_BIN_RANGE = range(1, 7)
POST_TOB_BIN_RANGE = range(6, 10)

def getargs():
  parser = argparse.ArgumentParser(description=DESCRIPTION)
  parser.add_argument("data_file", help="The root file containing data histograms")
  parser.add_argument("mc_file", help="The root file containing Monte Carlo histograms")
  parser.add_argument("--output", default="correctedOuterHists.root", help="The name for the corrected Monte Carlo data histograms that will be saved")
  return parser.parse_args()

def get_hist_from_file(filename, hist_name):
  tfile = ROOT.TFile.Open(filename)
  hist = tfile.Get(hist_name)
  hist.SetDirectory(0) # Detach from tfile so we can close it without deleting hist
  tfile.Close()
  return hist

def get_chi2(data_pdf, mc_pdf, bin_range):
  chi2 = 0.0
  bins_used = 0

  for number_missing_hits in bin_range:
    data_bin = data_pdf.FindBin(number_missing_hits)
    data_prob = data_pdf.GetBinContent(data_bin)
    data_err = data_pdf.GetBinError(data_bin)

    mc_bin = mc_pdf.FindBin(number_missing_hits)
    mc_prob = mc_pdf.GetBinContent(mc_bin)
    mc_err = mc_pdf.GetBinError(mc_bin)

    total_err = math.hypot(data_err, mc_err)
    if total_err > 1e-5:
      chi2 += ((data_prob - mc_prob) * (data_prob - mc_prob)) / (total_err * total_err)
      bins_used += 1

  return chi2 / bins_used

def get_missing_hits_pdf(number_hits, miss_prob):
  """
  Finds the probability distribution to miss outer hits given a total number
  of layers hit and the probability that any individual hit is missed.

  Parameters:
    - number_hits: the number of layers that are hit for this track
    - miss_prob: the probability that any hit is missed

  Returns:
    - The PDF histogram that contains the probability to miss
      a different number of outer hits

  For there to be k missing outer hits, the outer-most k hits need to be missed,
  while the (k+1) hit needs to not be missed. If the probability to miss a hit
  is given by p, the probability to miss k outer hits is p^k * (1-p).

  In the case that all hits are missed, there is no (1-p) factor that corresponds
  to the innermost non-missed hit. At that point, the probability is p^n, where n
  is the total number of hits on the track
  """
  pdf = ROOT.TH1D("PDF", ";missing outer hits", 16, -0.5, 15.5)
  pdf.SetDirectory(0)

  for number_missed_hits in range(number_hits + 1):
    prob = (miss_prob**number_missed_hits) * (1-miss_prob)
    pdf.SetBinContent(pdf.FindBin(number_missed_hits), prob)

  # All hits are missed
  pdf.SetBinContent(pdf.FindBin(number_hits), miss_prob**number_hits)

  pdf.Scale(1.0 / pdf.Integral())
  return pdf

def get_corrected_pdf(miss_prob, miss_all_tob_prob, unnorm_mc_hist, tob_status, should_normalize=True):
  corr_hist = ROOT.TH1D("OuterHitsCorrected", ";number of missing outer hits", 16, -0.5, 15.5)
  corr_hist.SetDirectory(0)

  for num_hits in range(1, 20):
    pdf = get_missing_hits_pdf(num_hits, miss_prob)

    for orig_miss_hits in range(0, 16):
      for tob_hits in range(0, 16):
        mc_bin = unnorm_mc_hist.FindBin(orig_miss_hits, tob_hits, num_hits)
        num_tracks = unnorm_mc_hist.GetBinContent(mc_bin)
        num_tracks_err = unnorm_mc_hist.GetBinError(mc_bin)

        for extra_miss_hits in range(0, 16):
          extra_miss_prob = pdf.GetBinContent(pdf.FindBin(extra_miss_hits))

          if tob_status == "pre":
            total_miss_hits = orig_miss_hits + extra_miss_hits
            total_miss_hits_with_miss_tob = orig_miss_hits + tob_hits
          else:
            total_miss_hits = orig_miss_hits
            total_miss_hits_with_miss_tob = orig_miss_hits + extra_miss_hits + tob_hits

          # Not missing all TOB hits
          corr_bin = corr_hist.FindBin(total_miss_hits)

          old_track_count = corr_hist.GetBinContent(corr_bin)
          old_track_err = corr_hist.GetBinError(corr_bin)

          new_track_count = old_track_count + num_tracks * extra_miss_prob * (1.0 - miss_all_tob_prob)
          new_track_err = math.hypot(old_track_err, num_tracks_err * extra_miss_prob * (1.0 - miss_all_tob_prob))

          corr_hist.SetBinContent(corr_bin, new_track_count)
          corr_hist.SetBinError(corr_bin, new_track_err)

          # Missing all TOB hits
          corr_bin = corr_hist.FindBin(total_miss_hits_with_miss_tob)

          old_track_count = corr_hist.GetBinContent(corr_bin)
          old_track_err = corr_hist.GetBinError(corr_bin)

          new_track_count = old_track_count + num_tracks * extra_miss_prob * miss_all_tob_prob
          new_track_err = math.hypot(old_track_err, num_tracks_err * extra_miss_prob * miss_all_tob_prob)

          corr_hist.SetBinContent(corr_bin, new_track_count)
          corr_hist.SetBinError(corr_bin, new_track_err)

  if corr_hist.Integral() > 0.0 and should_normalize:
    corr_hist.Scale(1.0 / corr_hist.Integral())

  return corr_hist

def find_best_miss_prob(data_pdf, unnorm_mc_hist, tob_status, bin_range):
  def chi2_wrapper(params):
    miss_prob = params[0]
    miss_tob_prob = params[1]
    corrected_pdf = get_corrected_pdf(miss_prob, miss_tob_prob, unnorm_mc_hist, tob_status)
    return get_chi2(data_pdf, corrected_pdf, bin_range)

  minimizer = ROOT.Math.Factory.CreateMinimizer("Minuit2", "Migrad")
  minimizer.SetMaxFunctionCalls(20000)
  minimizer.SetMaxIterations(2000)

  # Tolerance is set on the chi2 value, not miss_prob
  minimizer.SetTolerance(1e-3)

  func = ROOT.Math.Functor(chi2_wrapper, 2)
  minimizer.SetFunction(func)

  # Start searching at .5% probability in .1% steps
  minimizer.SetVariable(0, "miss_prob", 5e-3, 1e-3)
  minimizer.SetVariableLimits(0, 0.0, 1.0)

  minimizer.SetVariable(1, "miss_tob_prob", 5e-4, 1e-4)
  minimizer.SetVariableLimits(1, 0.0, 1.0)

  minimizer.Minimize()

  best_miss_prob = minimizer.X()[0]
  best_miss_tob_prob = minimizer.X()[1]
  corrected_pdf = get_corrected_pdf(best_miss_prob, best_miss_tob_prob, unnorm_mc_hist, tob_status, should_normalize=False)

  return best_miss_prob, best_miss_tob_prob, corrected_pdf

def main():
  args = getargs()
  fout = ROOT.TFile.Open(args.output, "recreate")

  # Data is 1D hist
  #   X-Axis: number missing outer hits
  data_pdf = get_hist_from_file(args.data_file, DATA_HIST_NAME)

  # MC is 3D hist
  #   X-Axis: number missing outer hits
  #   Y-Axis: number TOB (tracker outer barrel) layers hit
  #   Z-Axis: total number strip layers hit
  mc_hist = get_hist_from_file(args.mc_file, MC_HIST_NAME)

  # Projected to just X axis (number missing outer hits) makes
  # MC and data directly comparable
  mc_proj_pdf = mc_hist.ProjectionX()
  mc_proj_pdf.SetDirectory(0)

  # Scale to unit area so we can compare data and MC with diff. # events
  mc_proj_pdf.Scale(1.0 / mc_proj_pdf.Integral())
  data_pdf.Scale(1.0 / data_pdf.Integral())

  original_chi2_pre = get_chi2(data_pdf, mc_proj_pdf, PRE_TOB_BIN_RANGE)
  print(f"Uncorrected chi^2 (pre-TOB): {original_chi2_pre}")

  p_pre_tob, p_tob, unnorm_corr_hist_pre = find_best_miss_prob(data_pdf, mc_hist, "pre", PRE_TOB_BIN_RANGE)

  corr_pdf_pre = unnorm_corr_hist_pre.Clone()
  corr_pdf_pre.SetDirectory(0)
  corr_pdf_pre.Scale(1.0 / corr_pdf_pre.Integral())
  print(f"Corrected chi^2 (pre-TOB): {get_chi2(data_pdf, corr_pdf_pre, PRE_TOB_BIN_RANGE)}")

  original_chi2_post = get_chi2(data_pdf, mc_proj_pdf, POST_TOB_BIN_RANGE)
  print(f"Uncorrected chi^2 (post-TOB): {original_chi2_post}")

  p_post_tob, _, unnorm_corr_hist_post = find_best_miss_prob(data_pdf, mc_hist, "post", POST_TOB_BIN_RANGE)

  corr_pdf_post = unnorm_corr_hist_post.Clone()
  corr_pdf_post.SetDirectory(0)
  corr_pdf_post.Scale(1.0 / corr_pdf_post.Integral())
  print(f"Corrected chi^2 (post-TOB): {get_chi2(data_pdf, corr_pdf_post, POST_TOB_BIN_RANGE)}")

  print(f"P_pre-TOB: {p_pre_tob}, P_TOB: {p_tob}, P_post-TOB: {p_post_tob}")

  fout.cd()
  corr_hist = ROOT.TH1D("CorrectedOuterHits", ";number of missing outer hits", 16, -0.5, 15.5)

  for bin_idx in range(0, 6):
    corr_hist.SetBinContent(bin_idx, unnorm_corr_hist_pre.GetBinContent(bin_idx))

  for bin_idx in range(6, 13):
    corr_hist.SetBinContent(bin_idx, unnorm_corr_hist_post.GetBinContent(bin_idx))

  corr_hist.Write()
  fout.Close()

if __name__ == "__main__":
  main()

