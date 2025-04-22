import ROOT as r
import cmsstyle as cms
from DisappTrks.StandardAnalysis.IntegratedLuminosity_cff import lumi


def createPlots2022():

    mainDir = '/abyss/users/mcarrigan/fakeTrackEstimates/'

    fin2022EFG_ZtoEE = r.TFile.Open(f'{mainDir}/fakeTrackBkgdEstimate_zToEE_2022EFG_NLayers4.root')
    fin2022CD_ZtoEE = r.TFile.Open(f'{mainDir}/fakeTrackBkgdEstimate_zToEE_2022CD_NLayers4.root')
    fin2022EFG_ZtoMuMu = r.TFile.Open(f'{mainDir}/fakeTrackBkgdEstimate_zToMuMu_2022EFG_NLayers4.root')
    fin2022CD_ZtoMuMu = r.TFile.Open(f'{mainDir}/fakeTrackBkgdEstimate_zToMuMu_2022CD_NLayers4.root')

    d0_2022EFG = fin2022EFG_ZtoEE.Get('d0')
    #d0_2022EFG.RebinX(5)
    d0_2022EFG.SetLineColor(r.kBlack)
    d0_2022EFG.SetMarkerColor(r.kBlack)
    d0_2022EFG.GetYaxis().SetRangeUser(0, d0_2022EFG.GetMaximum()*1.5)
    d0_2022EFG.SetMarkerStyle(2)
    d0_fit2022EFG = fin2022EFG_ZtoEE.Get('d0_fit')

    d0_2022EFG.GetYaxis().SetTitle("Entries / 0.04 cm")

    d0_2022CD = fin2022CD_ZtoEE.Get('d0')
    d0_2022CD.SetLineColor(r.kBlue)
    d0_2022CD.SetMarkerColor(r.kBlue)
    d0_2022CD.SetMarkerStyle(2)
    d0_fit2022CD = fin2022CD_ZtoEE.Get('d0_fit')
    d0_fit2022CD.SetLineColor(r.kBlue)

    cms.SetExtraText('Preliminary')
    cms.SetLumi('')
    cms.SetEnergy("13.6")
    c2 = cms.cmsCanvas('canv', -0.5, 0.5, 0, 45, 'track d_{0} [cm]', 'Entries / 0.04cm', square = True, extraSpace=0.01, with_z_axis=False, iPos=0)
    d0_2022EFG.Draw("same")
    d0_fit2022EFG.Draw("same")
    d0_2022CD.Draw("same")
    d0_fit2022CD.Draw("same")


    t1 = r.TLatex()
    t1.SetTextFont(42)
    t1.SetTextSize(0.03)
    t1.DrawLatexNDC(0.19, 0.88, 'Z#rightarrowee')

    lumi2022EFG = round(lumi['EGamma_2022EFG']/1000, 2)
    lumi2022CD = round(lumi['EGamma_2022CD']/1000, 2)

    leg = cms.cmsLeg(0.17, 0.77, 0.3, 0.87, textSize=0.03)
    leg.AddEntry(d0_2022EFG, '2022 EFG ('+str(lumi2022EFG)+' fb^{-1})')
    leg.AddEntry(d0_2022CD, f'2022 CD ('+str(lumi2022CD)+' fb^{-1})')

    c2.SaveAs("FakeTrackZtoEERun3_2022.png")

    d0_2022EFG = fin2022EFG_ZtoMuMu.Get('d0')
    #d0_2022EFG.RebinX(5)
    d0_2022EFG.SetLineColor(r.kBlack)
    d0_2022EFG.SetMarkerColor(r.kBlack)
    d0_2022EFG.GetYaxis().SetRangeUser(0, d0_2022EFG.GetMaximum()*1.5)
    d0_2022EFG.SetMarkerStyle(2)
    d0_fit2022EFG = fin2022EFG_ZtoMuMu.Get('d0_fit')

    d0_2022EFG.GetYaxis().SetTitle("Entries / 0.04 cm")

    d0_2022CD = fin2022CD_ZtoMuMu.Get('d0')
    d0_2022CD.SetLineColor(r.kBlue)
    d0_2022CD.SetMarkerColor(r.kBlue)
    d0_2022CD.SetMarkerStyle(2)
    d0_fit2022CD = fin2022CD_ZtoMuMu.Get('d0_fit')
    d0_fit2022CD.SetLineColor(r.kBlue)

    cms.SetExtraText('Preliminary')
    c2 = cms.cmsCanvas('canv', -0.5, 0.5, 0, 60, 'track d_{0} [cm]', 'Entries / 0.04cm', square = True, extraSpace=0.01, with_z_axis=False, iPos=0)
    d0_2022EFG.Draw("same")
    d0_fit2022EFG.Draw("same")
    d0_2022CD.Draw("same")
    d0_fit2022CD.Draw("same")
    cms.SetCMSPalette()
    cms.SetLumi('')
    cms.SetEnergy("13.6")

    t1 = r.TLatex()
    t1.SetTextFont(42)
    t1.SetTextSize(0.03)
    t1.DrawLatexNDC(0.19, 0.88, 'Z#rightarrow#mu#mu')

    lumi2022EFG = round(lumi['EGamma_2022EFG']/1000, 2)
    lumi2022CD = round(lumi['EGamma_2022CD']/1000, 2)

    leg = cms.cmsLeg(0.17, 0.77, 0.3, 0.87, textSize=0.03)
    leg.AddEntry(d0_2022EFG, '2022 EFG ('+str(lumi2022EFG)+' fb^{-1})')
    leg.AddEntry(d0_2022CD, f'2022 CD ('+str(lumi2022CD)+' fb^{-1})')

    c2.SaveAs("FakeTrackZtoMuMuRun3_2022.png")

def createPlots2023():

    mainDir = '/abyss/users/mcarrigan/fakeTrackEstimates/'

    fin2023C_ZtoEE = r.TFile.Open(f'{mainDir}/fakeTrackBkgdEstimate_zToEE_2023C_NLayers4.root')
    fin2023D_ZtoEE = r.TFile.Open(f'{mainDir}/fakeTrackBkgdEstimate_zToEE_2023D_NLayers4.root')
    fin2023C_ZtoMuMu = r.TFile.Open(f'{mainDir}/fakeTrackBkgdEstimate_zToMuMu_2023C_NLayers4.root')
    fin2023D_ZtoMuMu = r.TFile.Open(f'{mainDir}/fakeTrackBkgdEstimate_zToMuMu_2023D_NLayers4.root')

    d0_2023C = fin2023C_ZtoEE.Get('d0')
    #d0_2023C.RebinX(5)
    d0_2023C.SetLineColor(r.kBlack)
    d0_2023C.SetMarkerColor(r.kBlack)
    d0_2023C.GetYaxis().SetRangeUser(0, d0_2023C.GetMaximum()*1.5)
    d0_2023C.SetMarkerStyle(2)
    d0_fit2023C = fin2023C_ZtoEE.Get('d0_fit')

    d0_2023C.GetYaxis().SetTitle("Entries / 0.04 cm")

    d0_2023D = fin2023D_ZtoEE.Get('d0')
    d0_2023D.SetLineColor(r.kBlue)
    d0_2023D.SetMarkerColor(r.kBlue)
    d0_2023D.SetMarkerStyle(2)

    d0_fit2023D = fin2023D_ZtoEE.Get('d0_fit')
    d0_fit2023D.SetLineColor(r.kBlue)

    cms.SetExtraText('Preliminary')
    cms.SetLumi('')
    cms.SetEnergy("13.6")
    c2 = cms.cmsCanvas('canv', -0.5, 0.5, 0, 30, 'track d_{0} [cm]', 'Entries / 0.04cm', square = True, extraSpace=0.01, with_z_axis=False, iPos=0)
    d0_2023C.Draw("same")
    d0_fit2023C.Draw("same")
    d0_2023D.Draw("same")
    d0_fit2023D.Draw("same")


    t1 = r.TLatex()
    t1.SetTextFont(42)
    t1.SetTextSize(0.03)
    t1.DrawLatexNDC(0.19, 0.88, 'Z#rightarrowee')

    lumi2023C = round(lumi['EGamma_2023C'], 2)
    lumi2023D = round(lumi['EGamma_2023D'], 2)

    leg = cms.cmsLeg(0.17, 0.77, 0.3, 0.87, textSize=0.03)
    leg.AddEntry(d0_2023C, '2023 C ('+str(lumi2023C)+' fb^{-1})')
    leg.AddEntry(d0_2023D, f'2023 D ('+str(lumi2023D)+' fb^{-1})')

    c2.SaveAs("FakeTrackZtoEERun3_2023.png")

    d0_2023C = fin2023C_ZtoMuMu.Get('d0')
    #d0_2023C.RebinX(5)
    d0_2023C.SetLineColor(r.kBlack)
    d0_2023C.SetMarkerColor(r.kBlack)
    d0_2023C.GetYaxis().SetRangeUser(0, d0_2023C.GetMaximum()*1.5)
    d0_2023C.SetMarkerStyle(2)
    d0_fit2023C = fin2023C_ZtoMuMu.Get('d0_fit')

    d0_2023C.GetYaxis().SetTitle("Entries / 0.04 cm")

    d0_2023D = fin2023D_ZtoMuMu.Get('d0')
    d0_2023D.SetLineColor(r.kBlue)
    d0_2023D.SetMarkerColor(r.kBlue)
    d0_2023D.SetMarkerStyle(2)

    d0_fit2023D = fin2023D_ZtoMuMu.Get('d0_fit')
    d0_fit2023D.SetLineColor(r.kBlue)

    cms.SetExtraText('Preliminary')
    cms.SetLumi('')
    cms.SetEnergy("13.6")
    c2 = cms.cmsCanvas('canv', -0.5, 0.5, 0, 30, 'track d_{0} [cm]', 'Entries / 0.04cm', square = True, extraSpace=0.01, with_z_axis=False, iPos=0)
    d0_2023C.Draw("same")
    d0_fit2023C.Draw("same")
    d0_2023D.Draw("same")
    d0_fit2023D.Draw("same")


    t1 = r.TLatex()
    t1.SetTextFont(42)
    t1.SetTextSize(0.03)
    t1.DrawLatexNDC(0.19, 0.88, 'Z#rightarrow#mu#mu')

    lumi2023C = round(lumi['Muon_2023C'], 2)
    lumi2023D = round(lumi['Muon_2023D'], 2)

    leg = cms.cmsLeg(0.17, 0.77, 0.3, 0.87, textSize=0.03)
    leg.AddEntry(d0_2023C, '2023 C ('+str(lumi2023C)+' fb^{-1})')
    leg.AddEntry(d0_2023D, f'2023 D ('+str(lumi2023D)+' fb^{-1})')

    c2.SaveAs("FakeTrackZtoMuMuRun3_2023.png")


if __name__ == "__main__":

    r.gROOT.SetBatch(1)
    createPlots2022()
    createPlots2023()