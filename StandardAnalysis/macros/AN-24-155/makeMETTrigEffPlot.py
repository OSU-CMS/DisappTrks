import argparse
import CMS_lumi as CMS
import ROOT

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
        print(f"Histogram {hist_name} not found in {file_name}. Quitting.")
        exit(-1)

    hist = hist.Clone()
    hist.SetDirectory(0)
    root_file.Close()
    return hist

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file_name")
    parser.add_argument("mc_file_name")
    args = parser.parse_args()

    data_numer = get_hist(args.data_file_name, "GrandOrNumeratorPlotter/Met Plots/metNoMuLogX")
    data_denom = get_hist(args.data_file_name, "GrandOrDenominatorPlotter/Met Plots/metNoMuLogX")

    mc_numer = get_hist(args.mc_file_name, "GrandOrNumeratorPlotter/Met Plots/metNoMuLogX")
    mc_denom = get_hist(args.mc_file_name, "GrandOrDenominatorPlotter/Met Plots/metNoMuLogX")

    ROOT.gStyle.SetOptStat(0)

    data_numer.Rebin(10)
    data_denom.Rebin(10)
    mc_numer.Rebin(10)
    mc_denom.Rebin(10)

    data_eff = ROOT.TGraphAsymmErrors(data_numer, data_denom)
    data_eff.SetMarkerStyle(20)
    data_eff.SetLineColor(1)
    data_eff.SetMarkerColor(1)

    mc_eff = ROOT.TGraphAsymmErrors(mc_numer, mc_denom)
    mc_eff.SetMarkerStyle(20)
    mc_eff.SetLineColor(4)
    mc_eff.SetMarkerColor(4)

    CMS.writeExtraTest = 1
    CMS.extraText = "Preliminary"
    CMS.lumi_sqrtS = "13.6 TeV"
    CMS.relPosX = 0.12

    canvas = ROOT.TCanvas("canvas", "canvas", 50, 50, CMS.W, CMS.H)
    canvas.SetLeftMargin(CMS.L / CMS.W)
    canvas.SetRightMargin(CMS.R / CMS.W)
    canvas.SetTopMargin(CMS.T / CMS.H)
    canvas.SetBottomMargin(CMS.B / CMS.H)

    canvas.cd()
    canvas.SetLogx()

    data_eff.SetTitle("")
    data_eff.GetXaxis().SetTitle("Title")
    data_eff.GetXaxis().SetTitleOffset(1.4)
    data_eff.GetXaxis().SetLimits(9, 1000)
    data_eff.GetXaxis().SetTitle("PF E_{T}^{miss, no #mu} [GeV]")

    data_eff.GetYaxis().SetTitle("Trigger Efficiency")
    data_eff.GetYaxis().SetTitleOffset(1.4)
    data_eff.GetYaxis().SetRangeUser(0.0, 1.4)
    data_eff.Draw()

    mc_eff.Draw("SAME,P,L")

    max_eff_line = ROOT.TLine(9, 1.0, 1000, 1.0)
    max_eff_line.SetLineWidth(2)
    max_eff_line.SetLineStyle(2)
    max_eff_line.Draw()

    legend = ROOT.TLegend(0.65, 0.75, 0.9, 0.85)
    legend.SetBorderSize(0)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetTextSize(0.035)
    legend.SetHeader("OR of Signal Paths")
    legend.AddEntry(data_eff, "2024 Data", "P")
    legend.AddEntry(mc_eff, "W #rightarrow l#nu MC", "P")
    legend.Draw()

    CMS.CMS_lumi(canvas, 2024, 0)
    canvas.Update()

    # TODO: have output
    canvas.Print("testing.pdf")

if __name__ == "__main__":
    main()

