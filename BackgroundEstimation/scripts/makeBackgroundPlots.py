import ROOT as r
import sys
import os
import shutil
import cmsstyle as cms
import math
import array as arr
import numpy as np
from ctypes import c_double
from DisappTrks.StandardAnalysis.integrated_luminosity import *

def makeMETPlots(f_name):
    
    fin = r.TFile.Open(f_name, 'READ')
    title = '_'.join(f_name.split('_')[-2:]).replace('.root', '')

    c1 = r.TCanvas("c1", "c1", 800, 800)

    r.gStyle.SetOptStat(0)

    l1 = r.TLine(120, 0.5, 1000, 0.5)
    l2 = r.TLine(120, 0.5, 120, 3.2)

    l1.SetLineColor(2)
    l1.SetLineWidth(3)
    l2.SetLineColor(2)
    l2.SetLineWidth(3)

    before = fin.Get('metForNctrl')

    h1 = before.GetPrimitive('deltaPhiMetJetLeadingVsMetNoMu')
    xmin = h1.GetXaxis().FindBin(120)
    ymin = h1.GetYaxis().FindBin(0.5)
    xmax = int(h1.GetXaxis().GetXmax())
    ymax = int(h1.GetYaxis().GetXmax())
    val = h1.Integral(xmin, xmax, ymin, ymax, "width")
    valTot = h1.Integral("width")
    p_offline = val/valTot
    print("Integral Search Region: {} \nIntegral Total: {} \nRatio: {}".format(val, valTot, p_offline))
    h1.GetXaxis().SetRangeUser(0, 1000)
    h1.GetZaxis().SetRangeUser(0, 1000)

    before.SetLogx(0)
    #c1.Draw()
    h1.Draw("colz same")
    before.Draw()
    before.SetLogz()

    before.SaveAs(f'ETMiss_before_{title}.png')

    after = fin.Get('metMinusOneForNctrl')

    h2 = after.GetPrimitive('deltaPhiMetJetLeadingVsElectronMetNoMuMinusOnePt')
    xmin = h1.GetXaxis().FindBin(120)
    ymin = h1.GetYaxis().FindBin(0.5)
    xmax = int(h1.GetXaxis().GetXmax())
    ymax = int(h1.GetYaxis().GetXmax())
    val = h1.Integral(xmin, xmax, ymin, ymax, "width")
    valTot = h1.Integral("width")
    p_offline = val/valTot
    print("Integral Search Region: {} \nIntegral Total: {} \nRatio: {}".format(val, valTot, p_offline))
    h2.GetXaxis().SetRangeUser(0, 1000)
    h2.GetZaxis().SetRangeUser(0, 1000)

    after.SetLogx(0)
    after.Draw()
    h2.Draw("colz same")
    after.SetLogz()
    l1.Draw()
    l2.Draw()

    after.SaveAs(f'ETMiss_after_{title}.png')

    cmsLabel = r.TPaveText(0.134085,0.86,0.418546,0.984496,"brNDC")
    cmsLabel.SetBorderSize(0)
    cmsLabel.SetFillStyle(0)
    cmsLabel.SetTextFont(62)
    cmsLabel.SetTextSize(0.0387597)
    cmsLabel.AddText("CMS Preliminary")

    lumiLabel = r.TPaveText(0.575188,0.86,0.874687,0.992894,"brNDC")
    lumiLabel.SetBorderSize(0)
    lumiLabel.SetFillStyle(0)
    lumiLabel.SetTextFont(42)
    lumiLabel.SetTextSize(0.0387597)
    runPeriod = f_name.split('_')[1]
    lumiEra = str(round(lumi["EGamma_" + runPeriod] / 1000.0, 2))
    lumiStr = f'{lumiEra}' + 'fb^{-1} (13.6 GeV)'
    lumiLabel.AddText(lumiStr)

    p2 = h2.ProjectionX()
    p2.GetXaxis().SetRangeUser(0, 500)
    ymax = p2.GetMaximum() * 1.1

    c2 = r.TCanvas("c2", "c2", 1000, 1000)
    c2.cd()

    p2.Draw("same")
    lumiLabel.Draw("same")
    cmsLabel.Draw("same")
    c2.SaveAs(f'ETMiss_proj_{title}.png')

    fin.Close()

def printTriggerEffPlots(f_name):

    fin = r.TFile.Open(f_name, 'READ')
    title = '_'.join(f_name.split('_')[-2:]).replace('.root', '')

    trigEff = fin.Get('triggerEfficiency_HLT')

    trigEff.SaveAs(f'triggerEfficiency_{title}.png')

    fin.Close()



if __name__ == '__main__':

    r.gROOT.SetBatch(1)
    r.gStyle.SetOptStat(0)

    f_names = ['../test/electronBkgdEstimate_2022EFG_NLayers4.root', '../test/electronBkgdEstimate_2022EFG_NLayers5.root', '../test/electronBkgdEstimate_2022EFG_NLayers6plus.root',
               '../test/electronBkgdEstimate_2022CD_NLayers4.root', '../test/electronBkgdEstimate_2022CD_NLayers5.root', '../test/electronBkgdEstimate_2022CD_NLayers6plus.root',
    ]

    for i, f in enumerate(f_names):
        makeMETPlots(f)
        printTriggerEffPlots(f)
    

