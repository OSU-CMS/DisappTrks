from array import *
import CMS_lumi

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.miniAOD_124X_Samples import dataset_names_bkgd

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)

def includeOverflow(hist):
    for i in range((hist.GetNbinsX())+2):
        if hist.IsBinOverflow(i): hist.SetBinContent(i-1, hist.GetBinContent(i))

mc_condor_dir = '/data/users/borzari/condor/BGMC/Run3/2022/disTrkPlots'
sig_condor_dir = '/data/users/borzari/condor/SignalMC/Run3/2022/disTrkPlots'

sigFiles = {
    'AMSB_800_10' : 'disTrk_800GeV_10cm',
    'AMSB_800_100' : 'disTrk_800GeV_100cm',
    'AMSB_800_1000' : 'disTrk_800GeV_1000cm',
    'AMSB_800_10000' : 'disTrk_800GeV_10000cm',
}

disTrkEcaloHists = {}
disTrkNOuterHists = {}

nLayers = 'NLayers4'
# nLayers = 'NLayers5'
# nLayers = 'NLayers6plus'

# The QCD datasets are bugged, so this variable makes the plots with and without them
notUsingQCD = True
notUsingZToNuNu = True

for dataset in dataset_names_bkgd:
    if '2022EE' not in dataset: continue
    # Not using datasets with 0 entries
    if notUsingQCD and 'QCD' in dataset:
        continue
    if notUsingQCD and 'Zto2Nu' in dataset:
        continue
    disTrkEcaloHists[dataset] = getHist('hist_merged_' + dataset + '_distrkPlotsv2',mc_condor_dir,'DisTrkNoEcalo' + nLayers + 'Plotter','Track Plots/trackCaloJetEnergy',False)
    nEvents = (getHist('hist_merged_' + dataset + '_distrkPlotsv2',mc_condor_dir,'DisTrkNoEcalo' + nLayers + 'CutFlowPlotter','cutFlow',False)).GetBinContent(1)
    disTrkEcaloHists[dataset].Rebin(8)
    disTrkEcaloHists[dataset].Scale(crossSections[dataset]/nEvents) # For MiniAOD-only processing
    includeOverflow(disTrkEcaloHists[dataset])

    disTrkNOuterHists[dataset] = getHist('hist_merged_' + dataset + '_distrkPlotsv2',mc_condor_dir,'DisTrkNoNMissOut' + nLayers + 'Plotter','Track Plots/trackNHitsMissingOuter',False)
    nEvents = (getHist('hist_merged_' + dataset + '_distrkPlotsv2',mc_condor_dir,'DisTrkNoNMissOut' + nLayers + 'CutFlowPlotter','cutFlow',False)).GetBinContent(1)
    disTrkNOuterHists[dataset].Rebin(1)
    disTrkNOuterHists[dataset].Scale(crossSections[dataset]/nEvents) # For MiniAOD-only processing
    includeOverflow(disTrkNOuterHists[dataset])

for file in sigFiles:
    disTrkEcaloHists[file] = getHist(sigFiles[file],sig_condor_dir,'DisTrkNoEcalo' + nLayers + 'Plotter','Track Plots/trackCaloJetEnergy',False)
    includeOverflow(disTrkEcaloHists[file])
    disTrkEcaloHists[file].Rebin(8)
    disTrkNOuterHists[file] = getHist(sigFiles[file],sig_condor_dir,'DisTrkNoNMissOut' + nLayers + 'Plotter','Track Plots/trackNHitsMissingOuter',False)
    includeOverflow(disTrkNOuterHists[file])

disTrkEcaloStackedHists = {}

DiHist_disTrkEcalo = disTrkEcaloHists['WW_2022EE']
DiHist_disTrkEcalo.Add(disTrkEcaloHists['WZ_2022EE'])
DiHist_disTrkEcalo.Add(disTrkEcaloHists['ZZ_2022EE'])
disTrkEcaloStackedHists['W'] = DiHist_disTrkEcalo

WTopHist_disTrkEcalo = DiHist_disTrkEcalo.Clone("diMuonWTop")
WTopHist_disTrkEcalo.SetDirectory(0)
WTopHist_disTrkEcalo.Add(disTrkEcaloHists['TBbartoLplusNuBbar_2022EE'])
WTopHist_disTrkEcalo.Add(disTrkEcaloHists['TbarBtoLminusNuB_2022EE'])
WTopHist_disTrkEcalo.Add(disTrkEcaloHists['TQbartoLNu_2022EE'])
WTopHist_disTrkEcalo.Add(disTrkEcaloHists['TbarQtoLNu_2022EE'])
WTopHist_disTrkEcalo.Add(disTrkEcaloHists['TWminusto2L2Nu_2022EE'])
WTopHist_disTrkEcalo.Add(disTrkEcaloHists['TWminustoLNu2Q_2022EE'])
WTopHist_disTrkEcalo.Add(disTrkEcaloHists['TbarWplusto2L2Nu_2022EE'])
WTopHist_disTrkEcalo.Add(disTrkEcaloHists['TbarWplustoLNu2Q_2022EE'])
disTrkEcaloStackedHists['WTop'] = WTopHist_disTrkEcalo

WTopDiHist_disTrkEcalo = WTopHist_disTrkEcalo.Clone("diMuonWTopDi")
WTopDiHist_disTrkEcalo.SetDirectory(0)
WTopDiHist_disTrkEcalo.Add(disTrkEcaloHists['DYJetsToLL_M50_2022EE'])
disTrkEcaloStackedHists['WTopDi'] = WTopDiHist_disTrkEcalo

WTopDiTTHist_disTrkEcalo = WTopDiHist_disTrkEcalo.Clone("diMuonWTopDiTT")
WTopDiTTHist_disTrkEcalo.SetDirectory(0)
WTopDiTTHist_disTrkEcalo.Add(disTrkEcaloHists['TTto2L2Nu_2022EE'])
WTopDiTTHist_disTrkEcalo.Add(disTrkEcaloHists['TTtoLNu2Q_2022EE'])
WTopDiTTHist_disTrkEcalo.Add(disTrkEcaloHists['TTto4Q_2022EE'])
disTrkEcaloStackedHists['WTopDiTT'] = WTopDiTTHist_disTrkEcalo

WTopDiTTDYHist_disTrkEcalo = WTopDiTTHist_disTrkEcalo.Clone("diMuonWTopDiTT")
WTopDiTTDYHist_disTrkEcalo.SetDirectory(0)
WTopDiTTDYHist_disTrkEcalo.Add(disTrkEcaloHists['WToLNu_4Jets_2022EE'])
disTrkEcaloStackedHists['WTopDiTTDY'] = WTopDiTTDYHist_disTrkEcalo

errorHist_disTrkEcalo = WTopDiTTDYHist_disTrkEcalo.Clone("error_diMuonWTopDiTTDY")
errorHist_disTrkEcalo.SetDirectory(0)

errorHist_disTrkEcalo.Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDY'].Integral()))
disTrkEcaloStackedHists['W'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDY'].Integral()))
disTrkEcaloStackedHists['WTop'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDY'].Integral()))
disTrkEcaloStackedHists['WTopDi'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDY'].Integral()))
disTrkEcaloStackedHists['WTopDiTT'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDY'].Integral()))
disTrkEcaloStackedHists['WTopDiTTDY'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDY'].Integral()))

disTrkEcaloHists['AMSB_800_10'].Scale(1.0/(disTrkEcaloHists['AMSB_800_10'].Integral()))
disTrkEcaloHists['AMSB_800_100'].Scale(1.0/(disTrkEcaloHists['AMSB_800_100'].Integral()))
disTrkEcaloHists['AMSB_800_1000'].Scale(1.0/(disTrkEcaloHists['AMSB_800_1000'].Integral()))
disTrkEcaloHists['AMSB_800_10000'].Scale(1.0/(disTrkEcaloHists['AMSB_800_10000'].Integral()))

disTrkEcaloStackedHists['W'].SetFillColor(colors['Diboson2022EE'])
disTrkEcaloStackedHists['WTop'].SetFillColor(colors['SingleTop2022EE'])
disTrkEcaloStackedHists['WTopDi'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
disTrkEcaloStackedHists['WTopDiTT'].SetFillColor(colors['TT2022EE'])
disTrkEcaloStackedHists['WTopDiTTDY'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
errorHist_disTrkEcalo.SetFillColor(1)
errorHist_disTrkEcalo.SetFillStyle(3001)

disTrkEcaloStackedHists['W'].SetLineColor(1)
disTrkEcaloStackedHists['WTop'].SetLineColor(1)
disTrkEcaloStackedHists['WTopDi'].SetLineColor(1)
disTrkEcaloStackedHists['WTopDiTT'].SetLineColor(1)
disTrkEcaloStackedHists['WTopDiTTDY'].SetLineColor(1)
errorHist_disTrkEcalo.SetLineColor(1)
disTrkEcaloHists['AMSB_800_10'].SetLineColor(2)
disTrkEcaloHists['AMSB_800_100'].SetLineColor(3)
disTrkEcaloHists['AMSB_800_1000'].SetLineColor(4)
disTrkEcaloHists['AMSB_800_10000'].SetLineColor(1)
disTrkEcaloHists['AMSB_800_10'].SetLineWidth(2)
disTrkEcaloHists['AMSB_800_100'].SetLineWidth(2)
disTrkEcaloHists['AMSB_800_1000'].SetLineWidth(2)
disTrkEcaloHists['AMSB_800_10000'].SetLineWidth(2)

Legend_disTrkEcalo = TLegend(0.63,0.66,0.93,0.86)
Legend_disTrkEcalo.SetBorderSize(0)
Legend_disTrkEcalo.SetFillColor(0)
Legend_disTrkEcalo.SetFillStyle(0)
Legend_disTrkEcalo.SetTextSize(0.03)
Legend_disTrkEcalo.SetTextFont(42)
Legend_disTrkEcalo.AddEntry(errorHist_disTrkEcalo,"stat. errors","F")
Legend_disTrkEcalo.AddEntry(disTrkEcaloStackedHists['WTopDiTTDY'],labels['WToLNu_4Jets_2022EE'],"F")
Legend_disTrkEcalo.AddEntry(disTrkEcaloStackedHists['WTopDiTT'],labels['TT2022EE'],"F")
Legend_disTrkEcalo.AddEntry(disTrkEcaloStackedHists['WTopDi'],labels['DYJetsToLL2022EE'],"F")
Legend_disTrkEcalo.AddEntry(disTrkEcaloStackedHists['WTop'],labels['SingleTop2022EE'],"F")
Legend_disTrkEcalo.AddEntry(disTrkEcaloStackedHists['W'],labels['Diboson2022EE'],"F")

Legend2_disTrkEcalo = TLegend(0.15,0.71,0.45,0.86)
Legend2_disTrkEcalo.SetBorderSize(0)
Legend2_disTrkEcalo.SetFillColor(0)
Legend2_disTrkEcalo.SetFillStyle(0)
Legend2_disTrkEcalo.SetTextSize(0.03)
Legend2_disTrkEcalo.SetTextFont(42)
Legend2_disTrkEcalo.AddEntry(disTrkEcaloHists['AMSB_800_10'],"800 GeV #tilde{#chi}^{#pm} (c#tau = 10 cm)","L")
Legend2_disTrkEcalo.AddEntry(disTrkEcaloHists['AMSB_800_100'],"800 GeV #tilde{#chi}^{#pm} (c#tau = 100 cm)","L")
Legend2_disTrkEcalo.AddEntry(disTrkEcaloHists['AMSB_800_1000'],"800 GeV #tilde{#chi}^{#pm} (c#tau = 1000 cm)","L")
Legend2_disTrkEcalo.AddEntry(disTrkEcaloHists['AMSB_800_10000'],"800 GeV #tilde{#chi}^{#pm} (c#tau = 10000 cm)","L")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 0

Canvas_disTrkEcalo = TCanvas("Canvas_disTrkEcalo","Canvas_disTrkEcalo",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas_disTrkEcalo.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas_disTrkEcalo.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas_disTrkEcalo.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas_disTrkEcalo.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

disTrkEcaloStackedHists['WTopDiTTDY'].SetMinimum(1e-10)
disTrkEcaloStackedHists['WTopDiTTDY'].SetMaximum(1.5)
disTrkEcaloStackedHists['WTopDiTTDY'].GetXaxis().SetTitle("E_{calo} [GeV]")
disTrkEcaloStackedHists['WTopDiTTDY'].GetYaxis().SetTitle("Entries / 8.0 GeV (Unit Area Norm.)")
disTrkEcaloStackedHists['WTopDiTTDY'].SetTitle("")
disTrkEcaloStackedHists['WTopDiTTDY'].Draw("HIST")
errorHist_disTrkEcalo.Draw("SAME,E2")
disTrkEcaloStackedHists['WTopDiTT'].Draw("SAME,HIST")
disTrkEcaloStackedHists['WTopDi'].Draw("SAME,HIST")
disTrkEcaloStackedHists['WTop'].Draw("SAME,HIST")
disTrkEcaloStackedHists['W'].Draw("SAME,HIST")
disTrkEcaloHists['AMSB_800_10'].Draw("SAME,HIST")
disTrkEcaloHists['AMSB_800_100'].Draw("SAME,HIST")
disTrkEcaloHists['AMSB_800_1000'].Draw("SAME,HIST")
disTrkEcaloHists['AMSB_800_10000'].Draw("SAME,HIST")
Legend_disTrkEcalo.Draw()
Legend2_disTrkEcalo.Draw()

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(Canvas_disTrkEcalo, iPeriod, iPos)
Canvas_disTrkEcalo.Update()
Canvas_disTrkEcalo.Print("nMinusOne_eCalo_" + nLayers + ".pdf")

disTrkNOuterStackedHists = {}

DiHist_disTrkNOuter = disTrkNOuterHists['WW_2022EE']
DiHist_disTrkNOuter.Add(disTrkNOuterHists['WZ_2022EE'])
DiHist_disTrkNOuter.Add(disTrkNOuterHists['ZZ_2022EE'])
disTrkNOuterStackedHists['W'] = DiHist_disTrkNOuter

WTopHist_disTrkNOuter = DiHist_disTrkNOuter.Clone("diMuonWTop")
WTopHist_disTrkNOuter.SetDirectory(0)
WTopHist_disTrkNOuter.Add(disTrkNOuterHists['TBbartoLplusNuBbar_2022EE'])
WTopHist_disTrkNOuter.Add(disTrkNOuterHists['TbarBtoLminusNuB_2022EE'])
WTopHist_disTrkNOuter.Add(disTrkNOuterHists['TQbartoLNu_2022EE'])
WTopHist_disTrkNOuter.Add(disTrkNOuterHists['TbarQtoLNu_2022EE'])
WTopHist_disTrkNOuter.Add(disTrkNOuterHists['TWminusto2L2Nu_2022EE'])
WTopHist_disTrkNOuter.Add(disTrkNOuterHists['TWminustoLNu2Q_2022EE'])
WTopHist_disTrkNOuter.Add(disTrkNOuterHists['TbarWplusto2L2Nu_2022EE'])
WTopHist_disTrkNOuter.Add(disTrkNOuterHists['TbarWplustoLNu2Q_2022EE'])
disTrkNOuterStackedHists['WTop'] = WTopHist_disTrkNOuter

WTopDiHist_disTrkNOuter = WTopHist_disTrkNOuter.Clone("diMuonWTopDi")
WTopDiHist_disTrkNOuter.SetDirectory(0)
WTopDiHist_disTrkNOuter.Add(disTrkNOuterHists['DYJetsToLL_M50_2022EE'])
disTrkNOuterStackedHists['WTopDi'] = WTopDiHist_disTrkNOuter

WTopDiTTHist_disTrkNOuter = WTopDiHist_disTrkNOuter.Clone("diMuonWTopDiTT")
WTopDiTTHist_disTrkNOuter.SetDirectory(0)
WTopDiTTHist_disTrkNOuter.Add(disTrkNOuterHists['TTto2L2Nu_2022EE'])
WTopDiTTHist_disTrkNOuter.Add(disTrkNOuterHists['TTtoLNu2Q_2022EE'])
WTopDiTTHist_disTrkNOuter.Add(disTrkNOuterHists['TTto4Q_2022EE'])
disTrkNOuterStackedHists['WTopDiTT'] = WTopDiTTHist_disTrkNOuter

WTopDiTTDYHist_disTrkNOuter = WTopDiTTHist_disTrkNOuter.Clone("diMuonWTopDiTTDY")
WTopDiTTDYHist_disTrkNOuter.SetDirectory(0)
WTopDiTTDYHist_disTrkNOuter.Add(disTrkNOuterHists['WToLNu_4Jets_2022EE'])
disTrkNOuterStackedHists['WTopDiTTDY'] = WTopDiTTDYHist_disTrkNOuter

errorHist_disTrkNOuter = WTopDiTTDYHist_disTrkNOuter.Clone("error_diMuonWTopDiTTDY")
errorHist_disTrkNOuter.SetDirectory(0)

disTrkNOuterStackedHists['W'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDY'].Integral()))
disTrkNOuterStackedHists['WTop'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDY'].Integral()))
disTrkNOuterStackedHists['WTopDi'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDY'].Integral()))
disTrkNOuterStackedHists['WTopDiTT'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDY'].Integral()))
disTrkNOuterStackedHists['WTopDiTTDY'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDY'].Integral()))

disTrkNOuterHists['AMSB_800_10'].Scale(1.0/(disTrkNOuterHists['AMSB_800_10'].Integral()))
disTrkNOuterHists['AMSB_800_100'].Scale(1.0/(disTrkNOuterHists['AMSB_800_100'].Integral()))
disTrkNOuterHists['AMSB_800_1000'].Scale(1.0/(disTrkNOuterHists['AMSB_800_1000'].Integral()))
disTrkNOuterHists['AMSB_800_10000'].Scale(1.0/(disTrkNOuterHists['AMSB_800_10000'].Integral()))

disTrkNOuterStackedHists['W'].SetFillColor(colors['Diboson2022EE'])
disTrkNOuterStackedHists['WTop'].SetFillColor(colors['SingleTop2022EE'])
disTrkNOuterStackedHists['WTopDi'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
disTrkNOuterStackedHists['WTopDiTT'].SetFillColor(colors['TT2022EE'])
disTrkNOuterStackedHists['WTopDiTTDY'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
errorHist_disTrkNOuter.SetFillColor(1)
errorHist_disTrkNOuter.SetFillStyle(3001)

disTrkNOuterStackedHists['W'].SetLineColor(1)
disTrkNOuterStackedHists['WTop'].SetLineColor(1)
disTrkNOuterStackedHists['WTopDi'].SetLineColor(1)
disTrkNOuterStackedHists['WTopDiTT'].SetLineColor(1)
disTrkNOuterStackedHists['WTopDiTTDY'].SetLineColor(1)
errorHist_disTrkNOuter.SetLineColor(1)
disTrkNOuterHists['AMSB_800_10'].SetLineColor(2)
disTrkNOuterHists['AMSB_800_100'].SetLineColor(3)
disTrkNOuterHists['AMSB_800_1000'].SetLineColor(4)
disTrkNOuterHists['AMSB_800_10000'].SetLineColor(1)
disTrkNOuterHists['AMSB_800_10'].SetLineWidth(2)
disTrkNOuterHists['AMSB_800_100'].SetLineWidth(2)
disTrkNOuterHists['AMSB_800_1000'].SetLineWidth(2)
disTrkNOuterHists['AMSB_800_10000'].SetLineWidth(2)

Legend_disTrkNOuter = TLegend(0.63,0.66,0.93,0.86)
Legend_disTrkNOuter.SetBorderSize(0)
Legend_disTrkNOuter.SetFillColor(0)
Legend_disTrkNOuter.SetFillStyle(0)
Legend_disTrkNOuter.SetTextSize(0.03)
Legend_disTrkNOuter.SetTextFont(42)
Legend_disTrkNOuter.AddEntry(errorHist_disTrkNOuter,"stat. errors","F")
Legend_disTrkNOuter.AddEntry(disTrkNOuterStackedHists['WTopDiTTDY'],labels['WToLNu_4Jets_2022EE'],"F")
Legend_disTrkNOuter.AddEntry(disTrkNOuterStackedHists['WTopDiTT'],labels['TT2022EE'],"F")
Legend_disTrkNOuter.AddEntry(disTrkNOuterStackedHists['WTopDi'],labels['DYJetsToLL2022EE'],"F")
Legend_disTrkNOuter.AddEntry(disTrkNOuterStackedHists['WTop'],labels['SingleTop2022EE'],"F")
Legend_disTrkNOuter.AddEntry(disTrkNOuterStackedHists['W'],labels['Diboson2022EE'],"F")

Legend2_disTrkNOuter = TLegend(0.15,0.71,0.45,0.86)
Legend2_disTrkNOuter.SetBorderSize(0)
Legend2_disTrkNOuter.SetFillColor(0)
Legend2_disTrkNOuter.SetFillStyle(0)
Legend2_disTrkNOuter.SetTextSize(0.03)
Legend2_disTrkNOuter.SetTextFont(42)
Legend2_disTrkNOuter.AddEntry(disTrkEcaloHists['AMSB_800_10'],"800 GeV #tilde{#chi}^{#pm} (c#tau = 10 cm)","L")
Legend2_disTrkNOuter.AddEntry(disTrkEcaloHists['AMSB_800_100'],"800 GeV #tilde{#chi}^{#pm} (c#tau = 100 cm)","L")
Legend2_disTrkNOuter.AddEntry(disTrkEcaloHists['AMSB_800_1000'],"800 GeV #tilde{#chi}^{#pm} (c#tau = 1000 cm)","L")
Legend2_disTrkNOuter.AddEntry(disTrkEcaloHists['AMSB_800_10000'],"800 GeV #tilde{#chi}^{#pm} (c#tau = 10000 cm)","L")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 0

Canvas_disTrkNOuter = TCanvas("Canvas_disTrkNOuter","Canvas_disTrkNOuter",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas_disTrkNOuter.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas_disTrkNOuter.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas_disTrkNOuter.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas_disTrkNOuter.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

disTrkNOuterStackedHists['WTopDiTTDY'].SetMinimum(0.0)
disTrkNOuterStackedHists['WTopDiTTDY'].SetMaximum(1.5)
disTrkNOuterStackedHists['WTopDiTTDY'].GetYaxis().SetTitle("Entries per bin (1.0 width) (Unit Area Norm.)")
disTrkNOuterStackedHists['WTopDiTTDY'].SetTitle("")
disTrkNOuterStackedHists['WTopDiTTDY'].Draw("HIST")
errorHist_disTrkNOuter.Draw("SAME,E2")
disTrkNOuterStackedHists['WTopDiTT'].Draw("SAME,HIST")
disTrkNOuterStackedHists['WTopDi'].Draw("SAME,HIST")
disTrkNOuterStackedHists['WTop'].Draw("SAME,HIST")
disTrkNOuterStackedHists['W'].Draw("SAME,HIST")
disTrkNOuterHists['AMSB_800_10'].Draw("SAME,HIST")
disTrkNOuterHists['AMSB_800_100'].Draw("SAME,HIST")
disTrkNOuterHists['AMSB_800_1000'].Draw("SAME,HIST")
disTrkNOuterHists['AMSB_800_10000'].Draw("SAME,HIST")
Legend_disTrkNOuter.Draw()
Legend2_disTrkNOuter.Draw()

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(Canvas_disTrkNOuter, iPeriod, iPos)
Canvas_disTrkNOuter.Update()
Canvas_disTrkNOuter.Print("nMinusOne_missingOuterHits_" + nLayers + ".pdf")

