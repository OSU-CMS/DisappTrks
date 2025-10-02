import argparse
import math
import ROOT

DESCRIPTION="Estimates the probability a middle hit is missing."
DATA_HIST_NAME = "HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsMissingMiddle"
MC_HIST_NAME = "HitsSystematicsCtrlSelectionPlotter/Track Plots/trackNHitsStripLayersVsMissingMiddle"
CORRECTED_HIST_NAME = "CorrectedMiddleHits"
BIN_RANGE = range(0, 6)

def getargs():
  parser = argparse.ArgumentParser(description=DESCRIPTION)
  parser.add_argument("data_file", help="The root file containing data histograms")
  parser.add_argument("mc_file", help="The root file containing Monte Carlo histograms")
  parser.add_argument("--output", default="correctedMiddleHist.root", help="The name for the corrected Monte Carlo data histograms that will be saved")
  return parser.parse_args()

def get_hist_from_file(filename, hist_name):
  tfile = ROOT.TFile.Open(filename)
  hist = tfile.Get(hist_name)
  hist.SetDirectory(0) # Detach from tfile so we can close it without deleting hist
  tfile.Close()
  return hist

def get_chi2(data_pdf, mc_pdf):
  chi2 = 0.0
  bins_used = 0

  for number_missing_hits in BIN_RANGE:
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
  Finds the probability distribution to miss middle hits given a total number of layers
  hit and the probability that any individual hit is missed.

  Missing inner hits are excluded, i.e. we are only counting misses when there has
  already been a hit.

  Parameters:
    - number_hits: the number of layers that are hit for this track
    - miss_prob: the probability any hit is missed

  Returns:
    - The PDF histogram that contains the probability to miss different number of middle hits

  We seek to find the total probability for there to be k missing hits on a track with
  n total layers hit, where i is the first layer hit and p is the probability that
  any layer misses a hit.

  The probability for the first layer i to be the inner-most hit layer is give by
  p^(i-1)*(1-p). Here, p^(i-1) is the probability all previous layers are missed,
  and (1-p) is the probability that this layer is hit.

  After the first hit at layer i, there are n-i layers remaining. The number of ways
  for k misses to be distributed among these layers is (n-i choose k). Each layer has
  a probability p to be missed, so there is a total probability p^k that all layers are
  missed. There is then (1-p)^(n-i-k) probabilility that the remaining layers are hit.
  """
  pdf = ROOT.TH1D("PDF", ";missing middle hits", number_hits + 1, -0.5, number_hits + 0.5)
  pdf.SetDirectory(0)

  # Shorthands for convenience
  n = number_hits
  p = miss_prob

  for number_missed_hits in range(number_hits + 1):
    k = number_missed_hits
    prob = 0.0

    for first_hit_layer in range(1, number_hits + 1):
      i = first_hit_layer
      if k > n - i:
        # More missing hits than available layers, skipping...
        continue

      first_hit_prob = (p**(i-1)) * (1-p)
      remaining_prob = math.comb(n-i, k) * (p**k) * ((1-p)**(n-i-k))
      prob += first_hit_prob * remaining_prob

    pdf.SetBinContent(pdf.FindBin(k), prob)

  pdf.Scale(1.0 / pdf.Integral())
  return pdf

def get_corrected_pdf(miss_prob, unnorm_mc_hist, should_normalize=True):
  corrected_hist = ROOT.TH1D("MiddleHitsCorrected", ";number of missing middle hits", 6, -0.5, 5.5)
  corrected_hist.SetDirectory(0)

  for num_hits in range(1, 20):
    pdf = get_missing_hits_pdf(num_hits, miss_prob)

    for original_miss_hits in BIN_RANGE:
      num_tracks = unnorm_mc_hist.GetBinContent(unnorm_mc_hist.FindBin(original_miss_hits, num_hits))
      num_tracks_err = unnorm_mc_hist.GetBinError(unnorm_mc_hist.FindBin(original_miss_hits, num_hits))

      for extra_miss_hits in BIN_RANGE:
        pdf_bin = pdf.FindBin(extra_miss_hits)
        extra_miss_prob = pdf.GetBinContent(pdf_bin)

        corrected_bin = corrected_hist.FindBin(original_miss_hits + extra_miss_hits)
        old_track_count = corrected_hist.GetBinContent(corrected_bin)
        old_track_err = corrected_hist.GetBinError(corrected_bin)

        new_track_count = old_track_count + num_tracks * extra_miss_prob
        new_track_err = math.hypot(old_track_err, num_tracks_err * extra_miss_prob)

        corrected_hist.SetBinContent(corrected_bin, new_track_count)
        corrected_hist.SetBinError(corrected_bin, new_track_err)

  if corrected_hist.Integral() > 0.0 and should_normalize:
    corrected_hist.Scale(1.0 / corrected_hist.Integral())

  return corrected_hist

def find_best_miss_prob(data_pdf, unnorm_mc_hist):
  def chi2_wrapper(params):
    miss_prob = params[0]
    corrected_pdf = get_corrected_pdf(miss_prob, unnorm_mc_hist)
    return get_chi2(data_pdf, corrected_pdf)

  minimizer = ROOT.Math.Factory.CreateMinimizer("Minuit2", "Migrad")
  minimizer.SetMaxFunctionCalls(10000)
  minimizer.SetMaxIterations(1000)

  # Tolerance is set on the chi2 value, not miss_prob
  minimizer.SetTolerance(1e-3)

  func = ROOT.Math.Functor(chi2_wrapper, 1)
  minimizer.SetFunction(func)

  # Start searching at .5% probability in .1% steps
  minimizer.SetVariable(0, "miss_prob", 0.005, 0.001)
  minimizer.SetVariableLimits(0, 0.0, 1.0)

  minimizer.Minimize()

  best_miss_prob = minimizer.X()[0]
  corrected_pdf = get_corrected_pdf(best_miss_prob, unnorm_mc_hist, should_normalize=False)

  return best_miss_prob, corrected_pdf

def main():
  args = getargs()
  fout = ROOT.TFile.Open(args.output, "recreate")

  # Data is 1D hist
  #   X-Axis: number missing middle hits
  data_pdf = get_hist_from_file(args.data_file, DATA_HIST_NAME)

  # MC is 2D hist
  #   X-Axis: number missing middle hits
  #   Y-Axis: number strip layers with hits
  mc_hist = get_hist_from_file(args.mc_file, MC_HIST_NAME)

  # Projecting to just X axis (number missing middle hits) makes
  # MC and data directly comparable
  mc_proj_pdf = mc_hist.ProjectionX()
  mc_proj_pdf.SetDirectory(0)

  # Scale to unit area so we can compare data and MC with diff. # events
  mc_proj_pdf.Scale(1.0 / mc_proj_pdf.Integral())
  data_pdf.Scale(1.0 / data_pdf.Integral())

  original_chi2 = get_chi2(data_pdf, mc_proj_pdf)
  print(f"Uncorrected chi^2: {original_chi2}")

  miss_prob, unnorm_corr_hist = find_best_miss_prob(data_pdf, mc_hist)

  corr_pdf = unnorm_corr_hist.Clone()
  corr_pdf.SetDirectory(0)
  corr_pdf.Scale(1.0 / corr_pdf.Integral())
  print(f"Corrected chi^2: {get_chi2(data_pdf, corr_pdf)}")
  print(f"Missing middle hits probability: {miss_prob}")

  fout.cd()
  unnorm_corr_hist.SetName(CORRECTED_HIST_NAME)
  unnorm_corr_hist.Write()
  fout.Close()

if __name__ == "__main__":
  main()

