import ROOT as r
import cmsstyle as cms
import re
from DisappTrks.StandardAnalysis.integrated_luminosity import *

r.gROOT.SetBatch(1)

year = 2022
runPeriod = 'EFG'
mode = 'zToMuMu'

fin = r.TFile.Open(f'../../../BackgroundSystematics/test/fakeTrackEstimateVsD0_{mode}_{year}{runPeriod}.root', 'READ')


h4 = fin.Get(f'est_{mode}_{year}{runPeriod}_NLayers4')
h5 = fin.Get(f'est_{mode}_{year}{runPeriod}_NLayers5')
h6 = fin.Get(f'est_{mode}_{year}{runPeriod}_NLayers6plus')

NLayers = ['NLayers4', 'NLayers5', 'NLayers6plus']

est = []
err = []

for nlayer in NLayers:
    with open(f'../../../BackgroundEstimation/test/fakeTrackBkgdEstimate_{mode}_{year}{runPeriod}_{nlayer}.txt') as tfin:
        for line in tfin:
            if not line.startswith('N_est'): continue
            numbers = re.findall(r"[-+]?\d*\.\d+|\d+", line)
            if len(numbers) >= 2:
                n_est_value = float(numbers[0])
                n_est_error = float(numbers[1])
            break
        est.append(n_est_value)
        err.append(n_est_error)

cms.SetExtraText("Preliminary")
cms.SetLumi("")
cms.SetEnergy("13.6")
this_lumi = round(lumi[f"MET_{year}{runPeriod}"]/1000, 1)
print(this_lumi)
cms.SetLumi(this_lumi)
cms.ResetAdditionalInfo()
canv_ = cms.cmsCanvas("canvas",0,0.5,5e-3,70,"sideband lower bound |d_{xy}|","fake track estimate",square=cms.kSquare,extraSpace=0.01,iPos=0)
#canv_ = cms.cmsCanvas(canv_name,0,0.5,1e-2,50,"X","Y",square=cms.kSquare,extraSpace=0.01,iPos=iPos,with_z_axis=True,scaleLumi=scaleLumi,)


h4.GetYaxis().SetRangeUser(1e-2, 50)
h4.GetXaxis().SetRangeUser(0, 0.5)

h4.SetLineColor(r.kRed)
h4.SetMarkerColor(r.kRed)
h5.SetLineColor(r.kGreen)
h5.SetMarkerColor(r.kGreen)
h6.SetLineColor(r.kBlue)
h6.SetMarkerColor(r.kBlue)
h4.Draw("p")
h5.Draw("p same")
h6.Draw("p same")

l4 = r.TLine(0, est[0], 0.5, est[0])
l4.SetLineColor(r.kRed)
l4.SetLineWidth(3)
l4.Draw("same")

b4 = r.TBox(0, est[0]-err[0], 0.5, est[0]+err[0])
b4.SetLineColor(r.kRed)
b4.SetFillColorAlpha(r.kRed, 0.4)
b4.SetFillStyle(3001)
b4.Draw("same")

l5 = r.TLine(0, est[1], 0.5, est[1])
l5.SetLineColor(r.kGreen)
l5.SetLineWidth(3)
l5.Draw("same")

b5 = r.TBox(0, est[1]-err[1], 0.5, est[1]+err[1])
b5.SetLineColor(r.kGreen)
b5.SetFillColorAlpha(r.kGreen, 0.4)
b5.SetFillStyle(3001)
b5.Draw("same")

l6 = r.TLine(0, est[2], 0.5, est[2])
l6.SetLineColor(r.kBlue)
l6.SetLineWidth(3)
l6.Draw("same")

b6 = r.TBox(0, est[2]-err[2], 0.5, est[2]+err[2])
b6.SetLineColor(r.kBlue)
b6.SetFillColorAlpha(r.kBlue, 0.4)
b6.SetFillStyle(3001)
b6.Draw("same")

leg = cms.cmsLeg(0.75, 0.25, 0.95, 0.35, textSize=0.04)
leg.AddEntry(h4, 'n_{layers} = 4', 'l')
leg.AddEntry(h5, 'n_{layers} = 5', 'l')
leg.AddEntry(h6, 'n_{layers} #geq 6', 'l')

#cms.SetCMSPalette()
r.gPad.SetBottomMargin(0.2)
h = cms.GetcmsCanvasHist(canv_)
h.GetXaxis().SetTitleOffset(1.15)

leg.SetFillColor(r.kWhite)
leg.SetFillStyle(1001)
leg.Draw("same")

canv_.Draw()
canv_.SetLogy()

canv_.SaveAs(f'fakeTrackValidationPlot{year}{runPeriod}.png')