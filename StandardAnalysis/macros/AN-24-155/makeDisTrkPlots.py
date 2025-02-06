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

for dataset in dataset_names_bkgd:
    if '2022EE' not in dataset: continue
    if notUsingQCD and 'QCD' in dataset:
        continue
    disTrkEcaloHists[dataset] = getHist('hist_merged_' + dataset + '_distrkPlots',mc_condor_dir,'DisTrkNoEcalo' + nLayers + 'Plotter','Track Plots/trackCaloJetEnergy',False)
    nEvents = (getHist('hist_merged_' + dataset + '_distrkPlots',mc_condor_dir,'DisTrkNoEcalo' + nLayers + 'CutFlowPlotter','cutFlow',False)).GetBinContent(1)
    disTrkEcaloHists[dataset].Rebin(8)
    # disTrkEcaloHists[dataset].Scale((5010.409016184 + 2970.045129108)*crossSections[dataset]/nEvents) # For MiniAOD-only processing considering target lumi; 2022CD as an example
    disTrkEcaloHists[dataset].Scale(crossSections[dataset]/nEvents) # For MiniAOD-only processing
    includeOverflow(disTrkEcaloHists[dataset])

    disTrkNOuterHists[dataset] = getHist('hist_merged_' + dataset + '_distrkPlots',mc_condor_dir,'DisTrkNoNMissOut' + nLayers + 'Plotter','Track Plots/trackNHitsMissingOuter',False)
    nEvents = (getHist('hist_merged_' + dataset + '_distrkPlots',mc_condor_dir,'DisTrkNoNMissOut' + nLayers + 'CutFlowPlotter','cutFlow',False)).GetBinContent(1)
    disTrkNOuterHists[dataset].Rebin(1)
    # disTrkNOuterHists[dataset].Scale((5010.409016184 + 2970.045129108)*crossSections[dataset]/nEvents) # For MiniAOD-only processing considering target lumi; 2022CD as an example
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

WTopDiTTDYHist_disTrkEcalo = WTopDiTTHist_disTrkEcalo.Clone("diMuonWTopDiTTDY")
WTopDiTTDYHist_disTrkEcalo.SetDirectory(0)
WTopDiTTDYHist_disTrkEcalo.Add(disTrkEcaloHists['Zto2Nu_4Jets_HT100to200_2022EE'])
WTopDiTTDYHist_disTrkEcalo.Add(disTrkEcaloHists['Zto2Nu_4Jets_HT200to400_2022EE'])
WTopDiTTDYHist_disTrkEcalo.Add(disTrkEcaloHists['Zto2Nu_4Jets_HT400to800_2022EE'])
WTopDiTTDYHist_disTrkEcalo.Add(disTrkEcaloHists['Zto2Nu_4Jets_HT800to1500_2022EE'])
WTopDiTTDYHist_disTrkEcalo.Add(disTrkEcaloHists['Zto2Nu_4Jets_HT1500to2500_2022EE'])
WTopDiTTDYHist_disTrkEcalo.Add(disTrkEcaloHists['Zto2Nu_4Jets_HT2500_2022EE'])
disTrkEcaloStackedHists['WTopDiTTDY'] = WTopDiTTDYHist_disTrkEcalo

WTopDiTTDYZNNHist_disTrkEcalo = WTopDiTTDYHist_disTrkEcalo.Clone("diMuonWTopDiTTDYZNN")
WTopDiTTDYZNNHist_disTrkEcalo.SetDirectory(0)
WTopDiTTDYZNNHist_disTrkEcalo.Add(disTrkEcaloHists['WToLNu_4Jets_2022EE'])
disTrkEcaloStackedHists['WTopDiTTDYZNN'] = WTopDiTTDYZNNHist_disTrkEcalo

if not notUsingQCD:
    WTopDiTTDYZNNQCDHist_disTrkEcalo = WTopDiTTDYZNNHist_disTrkEcalo.Clone("diMuonWTopDiTTDYZNNQCD")
    WTopDiTTDYZNNQCDHist_disTrkEcalo.SetDirectory(0)
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT15to30_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT30to50_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT50to80_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT80to120_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT120to170_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT170to300_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT300to470_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT470to600_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT600to800_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT800to1000_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT1000to1400_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT1400to1800_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT1800to2400_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT2400to3200_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkEcalo.Add(disTrkEcaloHists['QCD_PT3200_2022EE'])
    disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'] = WTopDiTTDYZNNQCDHist_disTrkEcalo

if not notUsingQCD: errorHist_disTrkEcalo = WTopDiTTDYZNNQCDHist_disTrkEcalo.Clone("error_diMuonWTopDiTTDYZNNQCD")
else: errorHist_disTrkEcalo = WTopDiTTDYZNNHist_disTrkEcalo.Clone("error_diMuonWTopDiTTDYZNNQCD")
errorHist_disTrkEcalo.SetDirectory(0)

# DataHist_disTrkEcalo = disTrkEcaloHists['Muon_2022F'].Clone("DataHist_disTrkEcalo")
# DataHist_disTrkEcalo.SetDirectory(0)

if not notUsingQCD:
    errorHist_disTrkEcalo.Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkEcaloStackedHists['W'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkEcaloStackedHists['WTop'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkEcaloStackedHists['WTopDi'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkEcaloStackedHists['WTopDiTT'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkEcaloStackedHists['WTopDiTTDY'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkEcaloStackedHists['WTopDiTTDYZNN'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Integral()))

else:
    errorHist_disTrkEcalo.Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkEcaloStackedHists['W'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkEcaloStackedHists['WTop'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkEcaloStackedHists['WTopDi'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkEcaloStackedHists['WTopDiTT'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkEcaloStackedHists['WTopDiTTDY'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkEcaloStackedHists['WTopDiTTDYZNN'].Scale(1.0/(disTrkEcaloStackedHists['WTopDiTTDYZNN'].Integral()))

disTrkEcaloHists['AMSB_800_10'].Scale(1.0/(disTrkEcaloHists['AMSB_800_10'].Integral()))
disTrkEcaloHists['AMSB_800_100'].Scale(1.0/(disTrkEcaloHists['AMSB_800_100'].Integral()))
disTrkEcaloHists['AMSB_800_1000'].Scale(1.0/(disTrkEcaloHists['AMSB_800_1000'].Integral()))
disTrkEcaloHists['AMSB_800_10000'].Scale(1.0/(disTrkEcaloHists['AMSB_800_10000'].Integral()))

disTrkEcaloStackedHists['W'].SetFillColor(colors['Diboson2022EE'])
disTrkEcaloStackedHists['WTop'].SetFillColor(colors['SingleTop2022EE'])
disTrkEcaloStackedHists['WTopDi'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
disTrkEcaloStackedHists['WTopDiTT'].SetFillColor(colors['TT2022EE'])
disTrkEcaloStackedHists['WTopDiTTDY'].SetFillColor(colors['ZJetsToNuNu2022EE'])
disTrkEcaloStackedHists['WTopDiTTDYZNN'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
if not notUsingQCD: disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].SetFillColor(colors['QCD2022EE'])
errorHist_disTrkEcalo.SetFillColor(1)
errorHist_disTrkEcalo.SetFillStyle(3001)

disTrkEcaloStackedHists['W'].SetLineColor(1)
disTrkEcaloStackedHists['WTop'].SetLineColor(1)
disTrkEcaloStackedHists['WTopDi'].SetLineColor(1)
disTrkEcaloStackedHists['WTopDiTT'].SetLineColor(1)
disTrkEcaloStackedHists['WTopDiTTDY'].SetLineColor(1)
disTrkEcaloStackedHists['WTopDiTTDYZNN'].SetLineColor(1)
if not notUsingQCD: disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].SetLineColor(1)
errorHist_disTrkEcalo.SetLineColor(1)
disTrkEcaloHists['AMSB_800_10'].SetLineColor(2)
disTrkEcaloHists['AMSB_800_100'].SetLineColor(3)
disTrkEcaloHists['AMSB_800_1000'].SetLineColor(4)
disTrkEcaloHists['AMSB_800_10000'].SetLineColor(1)
disTrkEcaloHists['AMSB_800_10'].SetLineWidth(2)
disTrkEcaloHists['AMSB_800_100'].SetLineWidth(2)
disTrkEcaloHists['AMSB_800_1000'].SetLineWidth(2)
disTrkEcaloHists['AMSB_800_10000'].SetLineWidth(2)

# DataHist_disTrkEcalo.SetMarkerStyle(20)
# DataHist_disTrkEcalo.SetLineColor(1)

Legend_disTrkEcalo = TLegend(0.63,0.66,0.93,0.86)
Legend_disTrkEcalo.SetBorderSize(0)
Legend_disTrkEcalo.SetFillColor(0)
Legend_disTrkEcalo.SetFillStyle(0)
Legend_disTrkEcalo.SetTextSize(0.03)
Legend_disTrkEcalo.SetTextFont(42)
# Legend_disTrkEcalo.AddEntry(DataHist_disTrkEcalo,"Muon 2022F data","P")
Legend_disTrkEcalo.AddEntry(errorHist_disTrkEcalo,"stat. errors","F")
if not notUsingQCD: Legend_disTrkEcalo.AddEntry(disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'],labels['QCD2022EE'],"F")
Legend_disTrkEcalo.AddEntry(disTrkEcaloStackedHists['WTopDiTTDYZNN'],labels['WToLNu_4Jets_2022EE'],"F")
Legend_disTrkEcalo.AddEntry(disTrkEcaloStackedHists['WTopDiTTDY'],labels['ZJetsToNuNu2022EE'],"F")
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

# Canvas_disTrkEcalo.SetLogy()
if not notUsingQCD:
    disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].SetMinimum(0.0)
    disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].SetMaximum(1.5)
    disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].GetYaxis().SetTitle("Entries / 8.0 GeV (Unit Area Norm.)")
    disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].SetTitle("")
    disTrkEcaloStackedHists['WTopDiTTDYZNNQCD'].Draw("HIST")
    disTrkEcaloStackedHists['WTopDiTTDYZNN'].Draw("SAME,HIST")
else:
    disTrkEcaloStackedHists['WTopDiTTDYZNN'].SetMinimum(1e-10)
    disTrkEcaloStackedHists['WTopDiTTDYZNN'].SetMaximum(1.5)
    disTrkEcaloStackedHists['WTopDiTTDYZNN'].GetYaxis().SetTitle("Entries / 8.0 GeV (Unit Area Norm.)")
    disTrkEcaloStackedHists['WTopDiTTDYZNN'].SetTitle("")
    disTrkEcaloStackedHists['WTopDiTTDYZNN'].Draw("HIST")
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
Canvas_disTrkEcalo.Print("disTrkEcalo_" + nLayers + ".pdf")

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
WTopDiTTDYHist_disTrkNOuter.Add(disTrkNOuterHists['Zto2Nu_4Jets_HT100to200_2022EE'])
WTopDiTTDYHist_disTrkNOuter.Add(disTrkNOuterHists['Zto2Nu_4Jets_HT200to400_2022EE'])
WTopDiTTDYHist_disTrkNOuter.Add(disTrkNOuterHists['Zto2Nu_4Jets_HT400to800_2022EE'])
WTopDiTTDYHist_disTrkNOuter.Add(disTrkNOuterHists['Zto2Nu_4Jets_HT800to1500_2022EE'])
WTopDiTTDYHist_disTrkNOuter.Add(disTrkNOuterHists['Zto2Nu_4Jets_HT1500to2500_2022EE'])
WTopDiTTDYHist_disTrkNOuter.Add(disTrkNOuterHists['Zto2Nu_4Jets_HT2500_2022EE'])
disTrkNOuterStackedHists['WTopDiTTDY'] = WTopDiTTDYHist_disTrkNOuter

WTopDiTTDYZNNHist_disTrkNOuter = WTopDiTTDYHist_disTrkNOuter.Clone("diMuonWTopDiTTDYZNN")
WTopDiTTDYZNNHist_disTrkNOuter.SetDirectory(0)
WTopDiTTDYZNNHist_disTrkNOuter.Add(disTrkNOuterHists['WToLNu_4Jets_2022EE'])
disTrkNOuterStackedHists['WTopDiTTDYZNN'] = WTopDiTTDYZNNHist_disTrkNOuter

if not notUsingQCD:
    WTopDiTTDYZNNQCDHist_disTrkNOuter = WTopDiTTDYZNNHist_disTrkNOuter.Clone("diMuonWTopDiTTDYZNNQCD")
    WTopDiTTDYZNNQCDHist_disTrkNOuter.SetDirectory(0)
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT15to30_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT30to50_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT50to80_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT80to120_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT120to170_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT170to300_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT300to470_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT470to600_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT600to800_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT800to1000_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT1000to1400_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT1400to1800_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT1800to2400_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT2400to3200_2022EE'])
    WTopDiTTDYZNNQCDHist_disTrkNOuter.Add(disTrkNOuterHists['QCD_PT3200_2022EE'])
    disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'] = WTopDiTTDYZNNQCDHist_disTrkNOuter

if not notUsingQCD: errorHist_disTrkNOuter = WTopDiTTDYZNNQCDHist_disTrkNOuter.Clone("error_diMuonWTopDiTTDYZNNQCD")
else: errorHist_disTrkNOuter = WTopDiTTDYZNNHist_disTrkNOuter.Clone("error_diMuonWTopDiTTDYZNNQCD")
errorHist_disTrkNOuter.SetDirectory(0)

# DataHist_disTrkNOuter = disTrkNOuterHists['Muon_2022F'].Clone("DataHist_disTrkNOuter")
# DataHist_disTrkNOuter.SetDirectory(0)

if not notUsingQCD:
    errorHist_disTrkNOuter.Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkNOuterStackedHists['W'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkNOuterStackedHists['WTop'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkNOuterStackedHists['WTopDi'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkNOuterStackedHists['WTopDiTT'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkNOuterStackedHists['WTopDiTTDY'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkNOuterStackedHists['WTopDiTTDYZNN'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Integral()))
    disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Integral()))

else:
    disTrkNOuterStackedHists['W'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkNOuterStackedHists['WTop'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkNOuterStackedHists['WTopDi'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkNOuterStackedHists['WTopDiTT'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkNOuterStackedHists['WTopDiTTDY'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNN'].Integral()))
    disTrkNOuterStackedHists['WTopDiTTDYZNN'].Scale(1.0/(disTrkNOuterStackedHists['WTopDiTTDYZNN'].Integral()))

disTrkNOuterHists['AMSB_800_10'].Scale(1.0/(disTrkNOuterHists['AMSB_800_10'].Integral()))
disTrkNOuterHists['AMSB_800_100'].Scale(1.0/(disTrkNOuterHists['AMSB_800_100'].Integral()))
disTrkNOuterHists['AMSB_800_1000'].Scale(1.0/(disTrkNOuterHists['AMSB_800_1000'].Integral()))
disTrkNOuterHists['AMSB_800_10000'].Scale(1.0/(disTrkNOuterHists['AMSB_800_10000'].Integral()))

disTrkNOuterStackedHists['W'].SetFillColor(colors['Diboson2022EE'])
disTrkNOuterStackedHists['WTop'].SetFillColor(colors['SingleTop2022EE'])
disTrkNOuterStackedHists['WTopDi'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
disTrkNOuterStackedHists['WTopDiTT'].SetFillColor(colors['TT2022EE'])
disTrkNOuterStackedHists['WTopDiTTDY'].SetFillColor(colors['ZJetsToNuNu2022EE'])
disTrkNOuterStackedHists['WTopDiTTDYZNN'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
if not notUsingQCD: disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].SetFillColor(colors['QCD2022EE'])
errorHist_disTrkNOuter.SetFillColor(1)
errorHist_disTrkNOuter.SetFillStyle(3001)

disTrkNOuterStackedHists['W'].SetLineColor(1)
disTrkNOuterStackedHists['WTop'].SetLineColor(1)
disTrkNOuterStackedHists['WTopDi'].SetLineColor(1)
disTrkNOuterStackedHists['WTopDiTT'].SetLineColor(1)
disTrkNOuterStackedHists['WTopDiTTDY'].SetLineColor(1)
disTrkNOuterStackedHists['WTopDiTTDYZNN'].SetLineColor(1)
if not notUsingQCD: disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].SetLineColor(1)
errorHist_disTrkNOuter.SetLineColor(1)
disTrkNOuterHists['AMSB_800_10'].SetLineColor(2)
disTrkNOuterHists['AMSB_800_100'].SetLineColor(3)
disTrkNOuterHists['AMSB_800_1000'].SetLineColor(4)
disTrkNOuterHists['AMSB_800_10000'].SetLineColor(1)
disTrkNOuterHists['AMSB_800_10'].SetLineWidth(2)
disTrkNOuterHists['AMSB_800_100'].SetLineWidth(2)
disTrkNOuterHists['AMSB_800_1000'].SetLineWidth(2)
disTrkNOuterHists['AMSB_800_10000'].SetLineWidth(2)

# DataHist_disTrkNOuter.SetMarkerStyle(20)
# DataHist_disTrkNOuter.SetLineColor(1)

Legend_disTrkNOuter = TLegend(0.63,0.66,0.93,0.86)
Legend_disTrkNOuter.SetBorderSize(0)
Legend_disTrkNOuter.SetFillColor(0)
Legend_disTrkNOuter.SetFillStyle(0)
Legend_disTrkNOuter.SetTextSize(0.03)
Legend_disTrkNOuter.SetTextFont(42)
# Legend_disTrkNOuter.AddEntry(DataHist_disTrkNOuter,"Muon 2022F data","P")
Legend_disTrkNOuter.AddEntry(errorHist_disTrkNOuter,"stat. errors","F")
if not notUsingQCD: Legend_disTrkNOuter.AddEntry(disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'],labels['QCD2022EE'],"F")
Legend_disTrkNOuter.AddEntry(disTrkNOuterStackedHists['WTopDiTTDYZNN'],labels['WToLNu_4Jets_2022EE'],"F")
Legend_disTrkNOuter.AddEntry(disTrkNOuterStackedHists['WTopDiTTDY'],labels['ZJetsToNuNu2022EE'],"F")
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

# Canvas_disTrkNOuter.SetLogy()
if not notUsingQCD: 
    disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].SetMinimum(0.0)
    disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].SetMaximum(1.5)
    disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].GetYaxis().SetTitle("Entries per bin (1.0 width) (Unit Area Norm.)")
    disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].SetTitle("")
    disTrkNOuterStackedHists['WTopDiTTDYZNNQCD'].Draw("HIST")
    disTrkNOuterStackedHists['WTopDiTTDYZNN'].Draw("SAME,HIST")
else:
    disTrkNOuterStackedHists['WTopDiTTDYZNN'].SetMinimum(0.0)
    disTrkNOuterStackedHists['WTopDiTTDYZNN'].SetMaximum(1.5)
    disTrkNOuterStackedHists['WTopDiTTDYZNN'].GetYaxis().SetTitle("Entries per bin (1.0 width) (Unit Area Norm.)")
    disTrkNOuterStackedHists['WTopDiTTDYZNN'].SetTitle("")
    disTrkNOuterStackedHists['WTopDiTTDYZNN'].Draw("HIST")
# DataHist_disTrkNOuter.Draw("SAME,P,E")
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
Canvas_disTrkNOuter.Print("disTrkNOuter_" + nLayers + ".pdf")

