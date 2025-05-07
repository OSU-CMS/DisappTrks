import ROOT as r
import cmsstyle as CMS
import sys
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import lumi

def plotComparrison(file, lepton, era):

    if lepton=="tau":
        this_lumi = lumi[f'Tau_{era}']
    elif lepton=="electron":
        this_lumi = lumi[f'EGamma_{era}']
    else:
        print(f"Lepton {lepton} not recognized")
        sys.exit(0)

    this_lumi = round(this_lumi/1000, 1)

    fin = r.TFile.Open(file, 'READ')

    CMS.SetExtraText("Preliminary")
    iPos = 0
    canv_name = 'hist1d_root'
    CMS.SetLumi(this_lumi)
    CMS.SetEnergy("13.6")
    CMS.ResetAdditionalInfo()

    path = f'{lepton.capitalize()}TagPt55NLayers6plusPlotter/{lepton.capitalize()} Plots/'
    h_met = fin.Get(f'{path}{lepton}MetNoMuMinusOnePt')
    h_metMod = fin.Get(f'{path}{lepton}MetNoMuMinusOneUpPt')

    canv = CMS.cmsCanvas(canv_name,0,1e3,0,h_met.GetMaximum()*1.1,"E_{T}^{miss, no #mu} excluding selected lepton","Events",square=CMS.kSquare,extraSpace=0.05,iPos=iPos)

    h_met.SetLineColor(r.kBlue)
    h_met.SetMarkerColor(r.kBlue)
    h_metMod.SetLineColor(r.kRed)
    h_metMod.SetMarkerColor(r.kRed)

    p1 = r.TF1("p1", "[0] * TMath::Poisson(x, [1])", 0, 20)
    p1.SetParameters(100, 5)  # initial guess: [0]=norm, [1]=mean μ
    p2 = r.TF1("p2", "[0] * TMath::Poisson(x, [1])", 0, 20)
    p2.SetParameters(100, 5)  # initial guess: [0]=norm, [1]=mean μ

    h_met.Fit(p1, "MNL")
    h_metMod.Fit(p2, "MNL")

    mean1 = round(p1.GetParameter(1),2)
    err1 = round(p1.GetParError(1), 2)
    mean2 = round(p2.GetParameter(1), 2)
    err2 = round(p2.GetParError(1), 2)

    leg = CMS.cmsLeg(0.3, 0.90 - 0.05 * 3, 0.8, 0.90, textSize=0.04)
    leg.AddEntry(h_met, f"nominal (#mu={mean1} #pm {err1})","p")
    leg.AddEntry(h_metMod, f"scaled down (#mu={mean2} #pm {err2})","p")

    CMS.cmsDraw(h_met, "LP", lcolor=r.kRed, mcolor=r.kRed)
    CMS.cmsDraw(h_metMod, "LP same", lcolor=r.kBlue, mcolor=r.kBlue)
    leg.Draw("same")

    CMS.GetcmsCanvasHist(canv).GetXaxis().SetLabelSize(0.03)
    CMS.GetcmsCanvasHist(canv).GetXaxis().SetTitleSize(0.04)
    CMS.GetcmsCanvasHist(canv).GetYaxis().SetTitleSize(0.04)
    CMS.GetcmsCanvasHist(canv).GetXaxis().SetTitleOffset(1.2)
    CMS.GetcmsCanvasHist(canv).GetYaxis().SetTitleOffset(1.3)
    if lepton=='electron':
        CMS.GetcmsCanvasHist(canv).GetYaxis().SetLabelSize(0.03)
        CMS.GetcmsCanvasHist(canv).GetYaxis().SetTitleOffset(1.7)

    canv.Draw()
    r.gPad.RedrawAxis()

    canv.SaveAs(f'systematicScaledET_{lepton}{era}.png')

    del canv
    fin.Close()

if __name__ == "__main__":

    r.gROOT.SetBatch(1)

    plotComparrison('/abyss/users/rsantos/TauTagPt55_2022CD_New/Tau_2022CD.root', 'tau', '2022CD')
    plotComparrison('/abyss/users/rsantos/TauTagPt55_2022EFG_New/Tau_2022EFG.root', 'tau', '2022EFG')
    plotComparrison('/abyss/users/mcarrigan/Tau_run3/Tau_2023C_TauTagPt55/Tau_2023C.root', 'tau', '2023C')
    plotComparrison('/abyss/users/mcarrigan/Tau_run3/Tau_2023D_TauTagPt55/Tau_2023D.root', 'tau', '2023D')

    plotComparrison('/abyss/users/mcarrigan/EGamma_run3/EGamma_2022CD_TagPT55NLayers/EGamma_2022CD.root', 'electron', '2022CD')
    plotComparrison('/abyss/users/mcarrigan/EGamma_run3/EGamma_2022EFG_TagPT55NLayers/EGamma_2022EFG.root', 'electron', '2022EFG')
    plotComparrison('/abyss/users/mcarrigan/EGamma_run3/EGamma_2023C_TagPT55NLayers/EGamma_2023C.root', 'electron', '2023C')
    plotComparrison('/abyss/users/mcarrigan/EGamma_run3/EGamma_2023D_TagPT55NLayers/EGamma_2023D.root', 'electron', '2023D')