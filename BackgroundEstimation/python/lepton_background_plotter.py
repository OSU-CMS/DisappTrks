import os
import ROOT
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import lumi
from DisappTrks.StandardAnalysis.plotUtilities import setStyle, setCanvasStyle, setAxisStyle

class LeptonBackgroundPlotter:
    """Produces diagnostic plots for the lepton background estimate.

    Generates delta-phi vs MET, MET projection, veto before/after
    comparison, and trigger efficiency plots as PNGs.

    Args:
        lepton_type: "electron", "muon", or "tau".
        year: Data-taking year (e.g. "2024").
        era: Run era (e.g. "D", "EFG").
        met_cut: MET threshold in GeV for the search region boundary.
        delta_phi_cut: Delta-phi threshold for the search region boundary.
        output_dir: Directory to save PNG files.
    """

    def __init__(self, lepton_type, year, era, met_cut, delta_phi_cut, output_dir="."):
        self._lepton_type = lepton_type
        self._met_cut = met_cut
        self._delta_phi_cut = delta_phi_cut
        self._output_dir = output_dir

        met_key = f"MET_{year}{era}"
        lumi_fb = round(lumi[met_key] / 1000.0, 1)
        self._lumi_str = f"{lumi_fb} fb^{{-1}} (13.6 TeV)"

        if lepton_type == "electron":
            self._plot_str = f"EGamma {year}{era}"
        else:
            self._plot_str = f"{lepton_type.capitalize()} {year}{era}"

        ROOT.gROOT.SetBatch(1)
        ROOT.gStyle.SetOptStat(0)

    def _make_text_label(self, x1, y1, x2, y2, text, font=42, size=0.0387597):
        label = ROOT.TPaveText(x1, y1, x2, y2, "brNDC")
        label.SetBorderSize(0)
        label.SetFillStyle(0)
        label.SetTextFont(font)
        label.SetTextSize(size)
        label.AddText(text)
        return label

    def _cms_label(self):
        return self._make_text_label(0.134085, 0.937984, 0.418546, 0.984496, "CMS Preliminary", font=62)

    def _lumi_label(self):
        return self._make_text_label(0.575188, 0.937339, 0.874687, 0.992894, self._lumi_str)

    def _plot_label(self, x1=0.404762, y1=0.137597, x2=0.805764, y2=0.185401):
        return self._make_text_label(x1, y1, x2, y2, self._plot_str)

    def _save(self, canvas, name):
        canvas.SaveAs(os.path.join(self._output_dir, f"{name}.png"))

    def _clamp_numerator_to_denominator(self, passes, total):
        for i in range(0, passes.GetNbinsX() + 2):
            if passes.GetBinContent(i) > total.GetBinContent(i):
                passes.SetBinContent(i, total.GetBinContent(i))
                passes.SetBinError(i, total.GetBinError(i))

    def plot_delta_phi_vs_met(self, hist_2d, name_suffix="", exclude_lepton=False):
        """Plot 2D delta-phi vs MET.

        When exclude_lepton is True, axis labels indicate the lepton-excluded
        MET and red search region boundary lines are drawn.

        Args:
            hist_2d: 2D ROOT histogram (MET on x-axis, delta-phi on y-axis).
            name_suffix: Appended to the output filename (e.g. "4", "6plus").
            exclude_lepton: If True, use "excluding selected lepton" axis
                labels and draw search region cut lines.
        """
        canvas = ROOT.TCanvas("c_dphi_met", "", 800, 800)
        setCanvasStyle(canvas)
        canvas.cd()

        if exclude_lepton and self._lepton_type != "muon":
            x_title = f"E_{{T}}^{{miss, no #mu}} excluding selected {self._lepton_type} [GeV]"
            y_title = f"|#Delta#Phi(E_{{T}}^{{miss, no #mu}} excluding selected {self._lepton_type}, leading jet)|"
        else:
            x_title = "E_{T}^{miss, no #mu} [GeV]"
            y_title = "|#Delta#Phi(E_{T}^{miss, no #mu}, leading jet)|"

        setStyle(hist_2d)
        setAxisStyle(hist_2d, x_title, y_title)

        hist_2d.GetXaxis().SetRangeUser(0, 1000)
        hist_2d.GetZaxis().SetRangeUser(0, 1000)
        hist_2d.Draw("colz")
        canvas.SetLogz()

        if exclude_lepton:
            line_met = ROOT.TLine(self._met_cut, self._delta_phi_cut, self._met_cut, 3.2)
            line_met.SetLineColor(2)
            line_met.SetLineWidth(3)
            line_met.Draw()

            line_dphi = ROOT.TLine(self._met_cut, self._delta_phi_cut, 1000, self._delta_phi_cut)
            line_dphi.SetLineColor(2)
            line_dphi.SetLineWidth(3)
            line_dphi.Draw()

        cms_label = self._cms_label()
        lumi_label = self._lumi_label()
        plot_label = self._plot_label()
        cms_label.Draw("same")
        lumi_label.Draw("same")
        plot_label.Draw("same")

        suffix = f"_{name_suffix}" if name_suffix else ""
        self._save(canvas, f"delta_phi_vs_met{suffix}")

    def plot_met_projection(self, hist_2d, name_suffix=""):
        """Plot 1D projection of the 2D delta-phi vs MET histogram onto the MET axis.

        Args:
            hist_2d: 2D ROOT histogram (same as plot_delta_phi_vs_met).
            name_suffix: Appended to the output filename.
        """
        canvas = ROOT.TCanvas("c_met_proj", "", 1000, 1000)
        canvas.cd()

        projection = hist_2d.ProjectionX()
        projection.GetXaxis().SetRangeUser(0, 500)

        projection.Draw()

        cms = self._cms_label()
        lumi_label = self._lumi_label()
        cms.Draw("same")
        lumi_label.Draw("same")

        suffix = f"_{name_suffix}" if name_suffix else ""
        self._save(canvas, f"met_projection{suffix}")

    def plot_veto_track_pt(self, track_pt_before, track_pt_after, name_suffix=""):
        """Plot probe track pT before and after the lepton veto.

        Overlays both distributions with a KS test p-value and legend.

        Args:
            track_pt_before: Track pT histogram before veto.
            track_pt_after: Track pT histogram after veto.
            name_suffix: Appended to the output filename.
        """
        canvas = ROOT.TCanvas("c_veto_pt", "", 800, 800)
        setCanvasStyle(canvas)
        canvas.cd()

        setStyle(track_pt_before, 600)
        setAxisStyle(track_pt_before, f"{self._lepton_type} probe track p_{{T}} [GeV]")
        setStyle(track_pt_after, 632)
        setAxisStyle(track_pt_after, f"{self._lepton_type} probe track p_{{T}} [GeV]")

        track_pt_before.Draw("colz")
        track_pt_after.Draw("colz same")

        ks_pvalue = round(track_pt_before.KolmogorovTest(track_pt_after), 3)
        ks_label = self._make_text_label(0.421053, 0.824289, 0.820802, 0.872093,
                                         f"KS test p-value: {ks_pvalue}")

        leg = ROOT.TLegend(0.413534, 0.729328, 0.794486, 0.815891)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextFont(42)
        leg.SetTextSize(0.0387597)
        leg.AddEntry(track_pt_before, "before veto", "p")
        leg.AddEntry(track_pt_after, "after veto", "p")

        cms = self._cms_label()
        lumi_label = self._lumi_label()
        plot_label = self._plot_label()
        cms.Draw("same")
        lumi_label.Draw("same")
        plot_label.Draw("same")
        ks_label.Draw("same")
        leg.Draw("same")

        suffix = f"_{name_suffix}" if name_suffix else ""
        self._save(canvas, f"veto_track_pt{suffix}")

    def plot_veto_inv_mass(self, inv_mass_before, inv_mass_after, name_suffix=""):
        """Plot tag-probe invariant mass before and after the lepton veto.

        Overlays both distributions with a KS test p-value and legend.
        Not applicable for tau (caller should skip).

        Args:
            inv_mass_before: Invariant mass histogram before veto.
            inv_mass_after: Invariant mass histogram after veto.
            name_suffix: Appended to the output filename.
        """
        canvas = ROOT.TCanvas("c_veto_mass", "", 800, 800)
        setCanvasStyle(canvas)
        canvas.cd()

        setStyle(inv_mass_before, 600)
        setAxisStyle(inv_mass_before, "tag-probe invariant mass [GeV]")
        setStyle(inv_mass_after, 632)
        setAxisStyle(inv_mass_after, "tag-probe invariant mass [GeV]")

        inv_mass_before.Draw("colz")
        inv_mass_after.Draw("colz same")

        ks_pvalue = round(inv_mass_before.KolmogorovTest(inv_mass_after), 3)
        ks_label = self._make_text_label(0.421053, 0.824289, 0.820802, 0.872093,
                                         f"KS test p-value: {ks_pvalue}")

        leg = ROOT.TLegend(0.413534, 0.729328, 0.794486, 0.815891)
        leg.SetBorderSize(0)
        leg.SetFillStyle(0)
        leg.SetTextFont(42)
        leg.SetTextSize(0.0387597)
        leg.AddEntry(inv_mass_before, "before veto", "p")
        leg.AddEntry(inv_mass_after, "after veto", "p")

        cms = self._cms_label()
        lumi_label = self._lumi_label()
        plot_label = self._plot_label()
        cms.Draw("same")
        lumi_label.Draw("same")
        plot_label.Draw("same")
        ks_label.Draw("same")
        leg.Draw("same")

        suffix = f"_{name_suffix}" if name_suffix else ""
        self._save(canvas, f"veto_inv_mass{suffix}")

    def plot_trigger_efficiency(self, passes_hist, total_hist, name_suffix="", rebin_factor=4):
        """Plot MET trigger efficiency as a TGraphAsymmErrors.

        Rebins the histograms, clamps passes <= total per bin, then
        constructs a TGraphAsymmErrors for Clopper-Pearson error bars.

        Args:
            passes_hist: MET histogram for events passing the trigger.
            total_hist: MET histogram for all events.
            name_suffix: Appended to the output filename.
            rebin_factor: Factor to rebin both histograms before division.
        """
        canvas = ROOT.TCanvas("c_trig_eff", "", 800, 800)
        setCanvasStyle(canvas)
        canvas.cd()

        passes = passes_hist.Rebin(rebin_factor, "passesHist")
        total = total_hist.Rebin(rebin_factor, "totalHist")

        self._clamp_numerator_to_denominator(passes, total)
        graph = ROOT.TGraphAsymmErrors(passes, total)
        graph.SetEditable(0)

        setStyle(graph)
        graph.Draw("ap")
        setAxisStyle(graph, "E_{T}^{miss, no #mu} [GeV]", "MET trigger efficiency",
                     (0.0, 500.0), (0.0, 1.4))

        cms = self._cms_label()
        lumi_label = self._lumi_label()
        plot_label = self._plot_label(0.409774, 0.843023, 0.809524, 0.890827)
        cms.Draw("same")
        lumi_label.Draw("same")
        plot_label.Draw("same")

        suffix = f"_{name_suffix}" if name_suffix else ""
        self._save(canvas, f"trigger_efficiency{suffix}")
