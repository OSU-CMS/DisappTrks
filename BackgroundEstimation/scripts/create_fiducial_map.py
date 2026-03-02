#!/usr/bin/env python3

import argparse
import os
import numpy as np
import ROOT

EFFICIENCY_THRESHOLD = 2.0

def get_selection_names(year):
    if year in ["2022", "2023", "2024", "2025"]:
        return ["FiducialCalcBeforeOldCuts", "FiducialCalcAfterOldCuts"]
    else:
        return ['FiducialCalcBefore', 'FiducialCalcAfter']

def get_dataset_name(object_type, year):
    if object_type == "Electron":
        if year in ["2016", "2017"]:
            return "SingleEle"
        elif year in ["2017", "2022", "2023", "2024", "2025"]:
            return "EGamma"
    else:
        return "Muon"

def get_hist(file_name, hist_name):
    root_file = ROOT.TFile.Open(file_name)
    hist = root_file.Get(hist_name)
    if not hist:
        print(f"[ERROR]: Histogram {hist_name} not found in {file_name}. Quitting.")
        exit(-1)

    hist = hist.Clone()
    hist.SetDirectory(0)
    root_file.Close()
    return hist

def get_hists(file_name):
    root_file = ROOT.TFile.Open(file_name)
    if root_file.Get("beforeVeto") and root_file.Get("afterVeto"):
        print(f"[INFO]: Found beforeVeto and afterVeto in {file_name} — treating as existing fiducial map.")
        root_file.Close()
        hists = {
            "before": get_hist(file_name, "beforeVeto"),
            "after": get_hist(file_name, "afterVeto")
        }
    else:
        root_file.Close()
        hists = {
            "before": get_hist(file_name, "ElectronFiducialCalcBeforeOldCutsPlotter/Track Plots/trackEtaVsPhi"),
            "after": get_hist(file_name, "ElectronFiducialCalcAfterOldCutsPlotter/Track Plots/trackEtaVsPhi")
        }
    return hists

def th2_to_numpy(h):
    nx = h.GetXaxis().GetNbins()
    ny = h.GetYaxis().GetNbins()

    arr = np.zeros((nx, ny), dtype=float)

    # Bin 0 = underflow
    for ix in range(1, nx + 1):
        for iy in range(1, ny + 1):
            arr[ix-1, iy-1] = h.GetBinContent(ix, iy)

    return arr

def compute_efficiency(hists):
    before_arr = th2_to_numpy(hists["before"])
    after_arr = th2_to_numpy(hists["after"])
    mask = before_arr > 0

    # Weighted mean: total after / total before across all occupied bins
    mean = after_arr[mask].sum() / before_arr[mask].sum()

    # Sample std dev of per-bin inefficiency
    ineff_arr = after_arr[mask] / before_arr[mask]
    std_dev = np.std(ineff_arr, ddof=1)

    # Efficiency TH2 for plotting
    eff_hist = hists["after"].Clone("efficiency")
    eff_hist.SetDirectory(0)
    eff_hist.Divide(hists["before"])

    # Find hot spots: bins where (inefficiency - mean) > threshold * std_dev
    before = hists["before"]
    hot_spots = []
    nx = before.GetXaxis().GetNbins()
    ny = before.GetYaxis().GetNbins()
    for ix in range(1, nx + 1):
        for iy in range(1, ny + 1):
            if before.GetBinContent(ix, iy) <= 0:
                continue
            ineff = eff_hist.GetBinContent(ix, iy)
            if (ineff - mean) > EFFICIENCY_THRESHOLD * std_dev:
                eta = eff_hist.GetXaxis().GetBinCenter(ix)
                phi = eff_hist.GetYaxis().GetBinCenter(iy)
                hot_spots.append((eta, phi))

    print(f"Mean inefficiency: {mean:.4f}")
    print(f"Std dev of inefficiency: {std_dev:.4f}")
    print(f"Hot spots found: {len(hot_spots)}")

    return eff_hist, mean, std_dev, hot_spots

def write_root_file(hists, output_path):
    fout = ROOT.TFile.Open(output_path, "recreate")
    hists["before"].Write("beforeVeto")
    hists["after"].Write("afterVeto")
    fout.Close()

def make_sigma_hist(eff_hist, mean, std_dev):
    """Build a TH2 where each bin is (inefficiency - mean) / std_dev, clamped to 0.
    Also returns the unclamped sigma values for the distribution plot."""
    sigma_hist = eff_hist.Clone("efficiencyInSigma")
    sigma_hist.SetDirectory(0)
    nx = sigma_hist.GetXaxis().GetNbins()
    ny = sigma_hist.GetYaxis().GetNbins()
    sigma_vals = []
    for ix in range(1, nx + 1):
        for iy in range(1, ny + 1):
            ineff = eff_hist.GetBinContent(ix, iy)
            if ineff == 0:
                sigma_hist.SetBinContent(ix, iy, 0)
                continue
            sigma = (ineff - mean) / std_dev
            sigma_vals.append(sigma)
            sigma_hist.SetBinContent(ix, iy, max(sigma, 0))
    return sigma_hist, sigma_vals

def create_plots(hists, eff_hist, mean, std_dev, hot_spots, output_prefix):
    ROOT.gROOT.SetBatch(True)
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetOptTitle(0)
    ROOT.gStyle.SetPalette(56)

    canvas = ROOT.TCanvas("c1", "c1", 800, 800)

    circles = []
    for eta, phi in hot_spots:
        circle = ROOT.TEllipse(eta, phi, 0.06)
        circle.SetLineColor(820)  # kSpring
        circle.SetLineWidth(1)
        circle.SetFillStyle(0)
        circles.append(circle)

    # Plot 1: before-veto raw counts
    hists["before"].Draw("colz")
    canvas.SaveAs(output_prefix + "_beforeVeto.pdf")

    # Plot 2: after-veto raw counts
    hists["after"].Draw("colz")
    canvas.SaveAs(output_prefix + "_afterVeto.pdf")

    # Plot 3: per-bin inefficiency (after/before) with hot spot circles
    eff_hist.Draw("colz")
    for circle in circles:
        circle.Draw("same")
    canvas.SaveAs(output_prefix + "_efficiency.pdf")

    # Plot 4: per-bin deviation from mean in units of sigma, with hot spot circles
    sigma_hist, sigma_vals = make_sigma_hist(eff_hist, mean, std_dev)
    sigma_hist.Draw("colz")
    for circle in circles:
        circle.Draw("same")
    canvas.SaveAs(output_prefix + "_efficiencyInSigma.pdf")

    # Plot 5: distribution of sigma values across all occupied bins
    h_sigma_dist = ROOT.TH1D("sigmaDist", "sigmaDist", 40, -20, 20)
    for val in sigma_vals:
        h_sigma_dist.Fill(val)
    h_sigma_dist.GetXaxis().SetTitle("(Inefficiency - Mean) / #sigma")
    h_sigma_dist.GetYaxis().SetTitle("Bins")
    ROOT.gStyle.SetOptStat(1)
    h_sigma_dist.Draw()
    canvas.SaveAs(output_prefix + "_sigmaDistribution.pdf")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name")
    parser.add_argument("--output", default="fiducialMap.root")
    args = parser.parse_args()

    output_prefix = os.path.splitext(args.output)[0]

    hists = get_hists(args.file_name)
    eff_hist, mean, std_dev, hot_spots = compute_efficiency(hists)
    write_root_file(hists, args.output)
    create_plots(hists, eff_hist, mean, std_dev, hot_spots, output_prefix)


if __name__ == "__main__":
    main()
