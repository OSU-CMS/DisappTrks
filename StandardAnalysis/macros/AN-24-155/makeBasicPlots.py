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

mc_condor_dir = '/data/users/borzari/condor/BGMC/Run3/2022/basicPlots'

# dataFiles = {
#     'Muon_2022F' : 'Muon_2022F',
# }

# This is used in the MiniAOD+AOD processing; for MiniAOD-only the number of events can be extracted from the histograms
# nEvents = {
#     'WToLNu_4Jets_2022EE' : 348442033 * 0.964, # Events in AOD * fraction of processed jobs
#     'DYJetsToLL_M50_2022EE' : 94947242 * 0.971, # Events in AOD * fraction of processed jobs
#     'WW_2022EE' : 53619680 * 0.986, # Events in AOD * fraction of processed jobs
#     'WZ_2022EE' : 26887398 * 0.995, # Events in AOD * fraction of processed jobs
#     'ZZ_2022EE' : 4043040 * 0.939, # Events in AOD * fraction of processed jobs
#     'TTto2L2Nu_2022EE' : 85777130 * 0.970, # Events in AOD * fraction of processed jobs
#     'TTtoLNu2Q_2022EE' : 270699232 * 0.982, # Events in AOD * fraction of processed jobs
#     'TTto4Q_2022EE' : 182664317 * 0.995, # Events in AOD * fraction of processed jobs
#     'TBbartoLplusNuBbar_2022EE' : 4469700 * 0.978, # Events in AOD * fraction of processed jobs
#     'TbarBtoLminusNuB_2022EE' : 276266 * 0.968, # Events in AOD * fraction of processed jobs
#     'TQbartoLNu_2022EE' : 32667420 * 0.984, # Events in AOD * fraction of processed jobs
#     'TbarQtoLNu_2022EE' : 19537644 * 0.976, # Events in AOD * fraction of processed jobs
#     'TWminusto2L2Nu_2022EE' : 8581640 * 0.989, # Events in AOD * fraction of processed jobs
#     'TWminustoLNu2Q_2022EE' : 15859351 * 0.974, # Events in AOD * fraction of processed jobs
#     'TbarWplusto2L2Nu_2022EE' : 8576050 * 0.977, # Events in AOD * fraction of processed jobs
#     'TbarWplustoLNu2Q_2022EE' : 17273607 * 0.993, # Events in AOD * fraction of processed jobs
#     'QCD_PT15to30_2022EE' : 3998528 * 1.000, # Events in AOD * fraction of processed jobs
#     'QCD_PT30to50_2022EE' : 3998508 * 1.000, # Events in AOD * fraction of processed jobs
#     'QCD_PT50to80_2022EE' : 19907875 * 1.000, # Events in AOD * fraction of processed jobs
#     'QCD_PT80to120_2022EE' : 29904828 * 1.000, # Events in AOD * fraction of processed jobs
#     'QCD_PT120to170_2022EE' : 27792681 * 0.998, # Events in AOD * fraction of processed jobs
#     'QCD_PT170to300_2022EE' : 28829984 * 0.998, # Events in AOD * fraction of processed jobs
#     'QCD_PT300to470_2022EE' : 56016158 * 0.943, # Events in AOD * fraction of processed jobs
#     'QCD_PT470to600_2022EE' : 26933590 * 1.000, # Events in AOD * fraction of processed jobs
#     'QCD_PT600to800_2022EE' : 65322580 * 0.991, # Events in AOD * fraction of processed jobs
#     'QCD_PT800to1000_2022EE' : 38576235 * 1.000, # Events in AOD * fraction of processed jobs
#     'QCD_PT1000to1400_2022EE' : 19335155 * 0.998, # Events in AOD * fraction of processed jobs
#     'QCD_PT1400to1800_2022EE' : 5690478 * 1.000, # Events in AOD * fraction of processed jobs
#     'QCD_PT1800to2400_2022EE' : 2914410 * 1.000, # Events in AOD * fraction of processed jobs
#     'QCD_PT2400to3200_2022EE' : 1900526 * 1.000, # Events in AOD * fraction of processed jobs
#     'QCD_PT3200_2022EE' : 799436 * 1.000, # Events in AOD * fraction of processed jobs
#     'Zto2Nu_4Jets_HT100to200_2022EE' : 106149804 * 0.987, # Events in AOD * fraction of processed jobs
#     'Zto2Nu_4Jets_HT200to400_2022EE' : 67339696 * 0.992, # Events in AOD * fraction of processed jobs
#     'Zto2Nu_4Jets_HT400to800_2022EE' : 7096747 * 0.977, # Events in AOD * fraction of processed jobs
#     'Zto2Nu_4Jets_HT800to1500_2022EE' : 1658103 * 1.000, # Events in AOD * fraction of processed jobs
#     'Zto2Nu_4Jets_HT1500to2500_2022EE' : 1790534 * 0.988, # Events in AOD * fraction of processed jobs
#     'Zto2Nu_4Jets_HT2500_2022EE' : 1651711 * 0.992, # Events in AOD * fraction of processed jobs
# }

deltaPhiMetJetLeadingHists = {}
dijetMaxDeltaPhiHists = {}

for dataset in dataset_names_bkgd:
    if dataset == 'DYto2L_4jets_M10to50_2022EE' or dataset == 'DYJetsToLL_M50_merged': continue
    deltaPhiMetJetLeadingHists[dataset] = getHist('hist_merged_' + dataset + '_basicPlotsv2',mc_condor_dir,'BasicSelectionNoAngularCutsPlotter','Met-eventvariable Plots/deltaPhiMetJetLeading',False)
    nEvents = (getHist('hist_merged_' + dataset + '_basicPlotsv2',mc_condor_dir,'BasicSelectionNoAngularCutsCutFlowPlotter','cutFlow',False)).GetBinContent(1)
    # deltaPhiMetJetLeadingHists[dataset].Scale(crossSections[dataset]/nEvents[dataset]) # For MiniAOD+AOD processing
    deltaPhiMetJetLeadingHists[dataset].Scale(crossSections[dataset]/nEvents) # For MiniAOD-only processing
    deltaPhiMetJetLeadingHists[dataset].Rebin(2)
    dijetMaxDeltaPhiHists[dataset] = getHist('hist_merged_' + dataset + '_basicPlotsv2',mc_condor_dir,'BasicSelectionNoAngularCutsPlotter','Eventvariable Plots/dijetMaxDeltaPhi',False)
    # dijetMaxDeltaPhiHists[dataset].Scale(crossSections[dataset]/nEvents[dataset]) # For MiniAOD+AOD processing
    dijetMaxDeltaPhiHists[dataset].Scale(crossSections[dataset]/nEvents) # For MiniAOD-only processing
    dijetMaxDeltaPhiHists[dataset].Rebin(2)

# for dataset in dataset_names_bkgd:
#     deltaPhiMetJetLeadingHists[dataset] = getHist(dataFiles[file],data_condor_dir,'BasicSelectionNoAngularCutsPlotter','Met-eventvariable Plots/deltaPhiMetJetLeading')
#     dijetMaxDeltaPhiHists[dataset] = getHist(dataFiles[file],data_condor_dir,'BasicSelectionNoAngularCutsPlotter','Eventvariable Plots/dijetMaxDeltaPhi')
#     deltaPhiMetJetLeadingHists[dataset].Rebin(2)

deltaPhiMetJetLeadingStackedHists = {}

DiHist_deltaPhiMetJetLeading = deltaPhiMetJetLeadingHists['WW_2022EE']
DiHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['WZ_2022EE'])
DiHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['ZZ_2022EE'])
deltaPhiMetJetLeadingStackedHists['W'] = DiHist_deltaPhiMetJetLeading

WTopHist_deltaPhiMetJetLeading = DiHist_deltaPhiMetJetLeading.Clone("diMuonWTop")
WTopHist_deltaPhiMetJetLeading.SetDirectory(0)
WTopHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TBbartoLplusNuBbar_2022EE'])
WTopHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TbarBtoLminusNuB_2022EE'])
WTopHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TQbartoLNu_2022EE'])
WTopHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TbarQtoLNu_2022EE'])
WTopHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TWminusto2L2Nu_2022EE'])
WTopHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TWminustoLNu2Q_2022EE'])
WTopHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TbarWplusto2L2Nu_2022EE'])
WTopHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TbarWplustoLNu2Q_2022EE'])
deltaPhiMetJetLeadingStackedHists['WTop'] = WTopHist_deltaPhiMetJetLeading

WTopDiHist_deltaPhiMetJetLeading = WTopHist_deltaPhiMetJetLeading.Clone("diMuonWTopDi")
WTopDiHist_deltaPhiMetJetLeading.SetDirectory(0)
WTopDiHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['DYJetsToLL_M50_2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDi'] = WTopDiHist_deltaPhiMetJetLeading

WTopDiTTHist_deltaPhiMetJetLeading = WTopDiHist_deltaPhiMetJetLeading.Clone("diMuonWTopDiTT")
WTopDiTTHist_deltaPhiMetJetLeading.SetDirectory(0)
WTopDiTTHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TTto2L2Nu_2022EE'])
WTopDiTTHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TTtoLNu2Q_2022EE'])
WTopDiTTHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['TTto4Q_2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDiTT'] = WTopDiTTHist_deltaPhiMetJetLeading

WTopDiTTDYHist_deltaPhiMetJetLeading = WTopDiTTHist_deltaPhiMetJetLeading.Clone("diMuonWTopDiTTDY")
WTopDiTTDYHist_deltaPhiMetJetLeading.SetDirectory(0)
WTopDiTTDYHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['Zto2Nu_4Jets_HT100to200_2022EE'])
WTopDiTTDYHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['Zto2Nu_4Jets_HT200to400_2022EE'])
WTopDiTTDYHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['Zto2Nu_4Jets_HT400to800_2022EE'])
WTopDiTTDYHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['Zto2Nu_4Jets_HT800to1500_2022EE'])
WTopDiTTDYHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['Zto2Nu_4Jets_HT1500to2500_2022EE'])
WTopDiTTDYHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['Zto2Nu_4Jets_HT2500_2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDiTTDY'] = WTopDiTTDYHist_deltaPhiMetJetLeading

WTopDiTTDYZNNHist_deltaPhiMetJetLeading = WTopDiTTDYHist_deltaPhiMetJetLeading.Clone("diMuonWTopDiTTDYZNN")
WTopDiTTDYZNNHist_deltaPhiMetJetLeading.SetDirectory(0)
WTopDiTTDYZNNHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['WToLNu_4Jets_2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNN'] = WTopDiTTDYZNNHist_deltaPhiMetJetLeading

WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading = WTopDiTTDYZNNHist_deltaPhiMetJetLeading.Clone("diMuonWTopDiTTDYZNNQCD")
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.SetDirectory(0)
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT15to30_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT30to50_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT50to80_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT80to120_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT120to170_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT170to300_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT300to470_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT470to600_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT600to800_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT800to1000_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT1000to1400_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT1400to1800_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT1800to2400_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT2400to3200_2022EE'])
WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Add(deltaPhiMetJetLeadingHists['QCD_PT3200_2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'] = WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading

errorHist_deltaPhiMetJetLeading = WTopDiTTDYZNNQCDHist_deltaPhiMetJetLeading.Clone("error_diMuonWTopDiTTDYZNNQCD")
errorHist_deltaPhiMetJetLeading.SetDirectory(0)

# DataHist_deltaPhiMetJetLeading = deltaPhiMetJetLeadingHists['Muon_2022F'].Clone("DataHist_deltaPhiMetJetLeading")
# DataHist_deltaPhiMetJetLeading.SetDirectory(0)

# errorHist_deltaPhiMetJetLeading.Scale((DataHist_deltaPhiMetJetLeading.GetMaximum())/(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# deltaPhiMetJetLeadingStackedHists['W'].Scale((DataHist_deltaPhiMetJetLeading.GetMaximum())/(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# deltaPhiMetJetLeadingStackedHists['WTop'].Scale((DataHist_deltaPhiMetJetLeading.GetMaximum())/(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# deltaPhiMetJetLeadingStackedHists['WTopDi'].Scale((DataHist_deltaPhiMetJetLeading.GetMaximum())/(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# deltaPhiMetJetLeadingStackedHists['WTopDiTT'].Scale((DataHist_deltaPhiMetJetLeading.GetMaximum())/(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# deltaPhiMetJetLeadingStackedHists['WTopDiTTDY'].Scale((DataHist_deltaPhiMetJetLeading.GetMaximum())/(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNN'].Scale((DataHist_deltaPhiMetJetLeading.GetMaximum())/(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].Scale((DataHist_deltaPhiMetJetLeading.GetMaximum())/(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))

deltaPhiMetJetLeadingStackedHists['W'].SetFillColor(colors['Diboson2022EE'])
deltaPhiMetJetLeadingStackedHists['WTop'].SetFillColor(colors['SingleTop2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDi'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDiTT'].SetFillColor(colors['TT2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDiTTDY'].SetFillColor(colors['ZJetsToNuNu2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNN'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].SetFillColor(colors['QCD2022EE'])
errorHist_deltaPhiMetJetLeading.SetFillColor(1)
errorHist_deltaPhiMetJetLeading.SetFillStyle(3001)

deltaPhiMetJetLeadingStackedHists['W'].SetLineColor(1)
deltaPhiMetJetLeadingStackedHists['WTop'].SetLineColor(1)
deltaPhiMetJetLeadingStackedHists['WTopDi'].SetLineColor(1)
deltaPhiMetJetLeadingStackedHists['WTopDiTT'].SetLineColor(1)
deltaPhiMetJetLeadingStackedHists['WTopDiTTDY'].SetLineColor(1)
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNN'].SetLineColor(1)
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].SetLineColor(1)
errorHist_deltaPhiMetJetLeading.SetLineColor(1)

# DataHist_deltaPhiMetJetLeading.SetMarkerStyle(20)
# DataHist_deltaPhiMetJetLeading.SetLineColor(1)

Legend_deltaPhiMetJetLeading = TLegend(0.63,0.66,0.93,0.86)
Legend_deltaPhiMetJetLeading.SetBorderSize(0)
Legend_deltaPhiMetJetLeading.SetFillColor(0)
Legend_deltaPhiMetJetLeading.SetFillStyle(0)
Legend_deltaPhiMetJetLeading.SetTextSize(0.03)
Legend_deltaPhiMetJetLeading.SetTextFont(42)
# Legend_deltaPhiMetJetLeading.AddEntry(DataHist_deltaPhiMetJetLeading,"Muon 2022F data","P")
Legend_deltaPhiMetJetLeading.AddEntry(errorHist_deltaPhiMetJetLeading,"stat. errors","F")
Legend_deltaPhiMetJetLeading.AddEntry(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'],labels['QCD2022EE'],"F")
Legend_deltaPhiMetJetLeading.AddEntry(deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNN'],labels['WToLNu_4Jets_2022EE'],"F")
Legend_deltaPhiMetJetLeading.AddEntry(deltaPhiMetJetLeadingStackedHists['WTopDiTTDY'],labels['ZJetsToNuNu2022EE'],"F")
Legend_deltaPhiMetJetLeading.AddEntry(deltaPhiMetJetLeadingStackedHists['WTopDiTT'],labels['TT2022EE'],"F")
Legend_deltaPhiMetJetLeading.AddEntry(deltaPhiMetJetLeadingStackedHists['WTopDi'],labels['DYJetsToLL2022EE'],"F")
Legend_deltaPhiMetJetLeading.AddEntry(deltaPhiMetJetLeadingStackedHists['WTop'],labels['SingleTop2022EE'],"F")
Legend_deltaPhiMetJetLeading.AddEntry(deltaPhiMetJetLeadingStackedHists['W'],labels['Diboson2022EE'],"F")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 0

Canvas_deltaPhiMetJetLeading = TCanvas("Canvas_deltaPhiMetJetLeading","Canvas_deltaPhiMetJetLeading",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas_deltaPhiMetJetLeading.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas_deltaPhiMetJetLeading.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas_deltaPhiMetJetLeading.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas_deltaPhiMetJetLeading.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas_deltaPhiMetJetLeading.SetLogy()
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].SetMinimum(0.0001)
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].SetMaximum(10000000.0)
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].GetYaxis().SetTitle("Entries per bin (0.1 width)")
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].SetTitle("")
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNNQCD'].Draw("HIST")
# DataHist_deltaPhiMetJetLeading.Draw("SAME,P,E")
errorHist_deltaPhiMetJetLeading.Draw("SAME,E2")
deltaPhiMetJetLeadingStackedHists['WTopDiTTDYZNN'].Draw("SAME,HIST")
deltaPhiMetJetLeadingStackedHists['WTopDiTT'].Draw("SAME,HIST")
deltaPhiMetJetLeadingStackedHists['WTopDi'].Draw("SAME,HIST")
deltaPhiMetJetLeadingStackedHists['WTop'].Draw("SAME,HIST")
deltaPhiMetJetLeadingStackedHists['W'].Draw("SAME,HIST")
Legend_deltaPhiMetJetLeading.Draw()

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(Canvas_deltaPhiMetJetLeading, iPeriod, iPos)
Canvas_deltaPhiMetJetLeading.Update()
Canvas_deltaPhiMetJetLeading.Print("deltaPhiMetJetLeading_ZToMuMuISR.pdf")

dijetMaxDeltaPhiStackedHists = {}

DiHist_dijetMaxDeltaPhi = dijetMaxDeltaPhiHists['WW_2022EE']
DiHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['WZ_2022EE'])
DiHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['ZZ_2022EE'])
dijetMaxDeltaPhiStackedHists['W'] = DiHist_dijetMaxDeltaPhi

WTopHist_dijetMaxDeltaPhi = DiHist_dijetMaxDeltaPhi.Clone("diMuonWTop")
WTopHist_dijetMaxDeltaPhi.SetDirectory(0)
WTopHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TBbartoLplusNuBbar_2022EE'])
WTopHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TbarBtoLminusNuB_2022EE'])
WTopHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TQbartoLNu_2022EE'])
WTopHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TbarQtoLNu_2022EE'])
WTopHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TWminusto2L2Nu_2022EE'])
WTopHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TWminustoLNu2Q_2022EE'])
WTopHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TbarWplusto2L2Nu_2022EE'])
WTopHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TbarWplustoLNu2Q_2022EE'])
dijetMaxDeltaPhiStackedHists['WTop'] = WTopHist_dijetMaxDeltaPhi

WTopDiHist_dijetMaxDeltaPhi = WTopHist_dijetMaxDeltaPhi.Clone("diMuonWTopDi")
WTopDiHist_dijetMaxDeltaPhi.SetDirectory(0)
WTopDiHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['DYJetsToLL_M50_2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDi'] = WTopDiHist_dijetMaxDeltaPhi

WTopDiTTHist_dijetMaxDeltaPhi = WTopDiHist_dijetMaxDeltaPhi.Clone("diMuonWTopDiTT")
WTopDiTTHist_dijetMaxDeltaPhi.SetDirectory(0)
WTopDiTTHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TTto2L2Nu_2022EE'])
WTopDiTTHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TTtoLNu2Q_2022EE'])
WTopDiTTHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['TTto4Q_2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDiTT'] = WTopDiTTHist_dijetMaxDeltaPhi

WTopDiTTDYHist_dijetMaxDeltaPhi = WTopDiTTHist_dijetMaxDeltaPhi.Clone("diMuonWTopDiTTDY")
WTopDiTTDYHist_dijetMaxDeltaPhi.SetDirectory(0)
WTopDiTTDYHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['Zto2Nu_4Jets_HT100to200_2022EE'])
WTopDiTTDYHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['Zto2Nu_4Jets_HT200to400_2022EE'])
WTopDiTTDYHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['Zto2Nu_4Jets_HT400to800_2022EE'])
WTopDiTTDYHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['Zto2Nu_4Jets_HT800to1500_2022EE'])
WTopDiTTDYHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['Zto2Nu_4Jets_HT1500to2500_2022EE'])
WTopDiTTDYHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['Zto2Nu_4Jets_HT2500_2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDiTTDY'] = WTopDiTTDYHist_dijetMaxDeltaPhi

WTopDiTTDYZNNHist_dijetMaxDeltaPhi = WTopDiTTDYHist_dijetMaxDeltaPhi.Clone("diMuonWTopDiTTDYZNN")
WTopDiTTDYZNNHist_dijetMaxDeltaPhi.SetDirectory(0)
WTopDiTTDYZNNHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['WToLNu_4Jets_2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNN'] = WTopDiTTDYZNNHist_dijetMaxDeltaPhi

WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi = WTopDiTTDYZNNHist_dijetMaxDeltaPhi.Clone("diMuonWTopDiTTDYZNNQCD")
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.SetDirectory(0)
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT15to30_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT30to50_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT50to80_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT80to120_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT120to170_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT170to300_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT300to470_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT470to600_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT600to800_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT800to1000_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT1000to1400_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT1400to1800_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT1800to2400_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT2400to3200_2022EE'])
WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Add(dijetMaxDeltaPhiHists['QCD_PT3200_2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'] = WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi

errorHist_dijetMaxDeltaPhi = WTopDiTTDYZNNQCDHist_dijetMaxDeltaPhi.Clone("error_diMuonWTopDiTTDYZNNQCD")
errorHist_dijetMaxDeltaPhi.SetDirectory(0)

# DataHist_dijetMaxDeltaPhi = dijetMaxDeltaPhiHists['Muon_2022F'].Clone("DataHist_dijetMaxDeltaPhi")
# DataHist_dijetMaxDeltaPhi.SetDirectory(0)

# errorHist_dijetMaxDeltaPhi.Scale((DataHist_dijetMaxDeltaPhi.GetMaximum())/(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# dijetMaxDeltaPhiStackedHists['W'].Scale((DataHist_dijetMaxDeltaPhi.GetMaximum())/(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# dijetMaxDeltaPhiStackedHists['WTop'].Scale((DataHist_dijetMaxDeltaPhi.GetMaximum())/(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# dijetMaxDeltaPhiStackedHists['WTopDi'].Scale((DataHist_dijetMaxDeltaPhi.GetMaximum())/(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# dijetMaxDeltaPhiStackedHists['WTopDiTT'].Scale((DataHist_dijetMaxDeltaPhi.GetMaximum())/(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# dijetMaxDeltaPhiStackedHists['WTopDiTTDY'].Scale((DataHist_dijetMaxDeltaPhi.GetMaximum())/(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNN'].Scale((DataHist_dijetMaxDeltaPhi.GetMaximum())/(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))
# dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].Scale((DataHist_dijetMaxDeltaPhi.GetMaximum())/(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].GetMaximum()))

dijetMaxDeltaPhiStackedHists['W'].SetFillColor(colors['Diboson2022EE'])
dijetMaxDeltaPhiStackedHists['WTop'].SetFillColor(colors['SingleTop2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDi'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDiTT'].SetFillColor(colors['TT2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDiTTDY'].SetFillColor(colors['ZJetsToNuNu2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNN'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].SetFillColor(colors['QCD2022EE'])
errorHist_dijetMaxDeltaPhi.SetFillColor(1)
errorHist_dijetMaxDeltaPhi.SetFillStyle(3001)

dijetMaxDeltaPhiStackedHists['W'].SetLineColor(1)
dijetMaxDeltaPhiStackedHists['WTop'].SetLineColor(1)
dijetMaxDeltaPhiStackedHists['WTopDi'].SetLineColor(1)
dijetMaxDeltaPhiStackedHists['WTopDiTT'].SetLineColor(1)
dijetMaxDeltaPhiStackedHists['WTopDiTTDY'].SetLineColor(1)
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNN'].SetLineColor(1)
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].SetLineColor(1)
errorHist_dijetMaxDeltaPhi.SetLineColor(1)

# DataHist_dijetMaxDeltaPhi.SetMarkerStyle(20)
# DataHist_dijetMaxDeltaPhi.SetLineColor(1)

Legend_dijetMaxDeltaPhi = TLegend(0.63,0.66,0.93,0.86)
Legend_dijetMaxDeltaPhi.SetBorderSize(0)
Legend_dijetMaxDeltaPhi.SetFillColor(0)
Legend_dijetMaxDeltaPhi.SetFillStyle(0)
Legend_dijetMaxDeltaPhi.SetTextSize(0.03)
Legend_dijetMaxDeltaPhi.SetTextFont(42)
# Legend_dijetMaxDeltaPhi.AddEntry(DataHist_dijetMaxDeltaPhi,"Muon 2022F data","P")
Legend_dijetMaxDeltaPhi.AddEntry(errorHist_dijetMaxDeltaPhi,"stat. errors","F")
Legend_dijetMaxDeltaPhi.AddEntry(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'],labels['QCD2022EE'],"F")
Legend_dijetMaxDeltaPhi.AddEntry(dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNN'],labels['WToLNu_4Jets_2022EE'],"F")
Legend_dijetMaxDeltaPhi.AddEntry(dijetMaxDeltaPhiStackedHists['WTopDiTTDY'],labels['ZJetsToNuNu2022EE'],"F")
Legend_dijetMaxDeltaPhi.AddEntry(dijetMaxDeltaPhiStackedHists['WTopDiTT'],labels['TT2022EE'],"F")
Legend_dijetMaxDeltaPhi.AddEntry(dijetMaxDeltaPhiStackedHists['WTopDi'],labels['DYJetsToLL2022EE'],"F")
Legend_dijetMaxDeltaPhi.AddEntry(dijetMaxDeltaPhiStackedHists['WTop'],labels['SingleTop2022EE'],"F")
Legend_dijetMaxDeltaPhi.AddEntry(dijetMaxDeltaPhiStackedHists['W'],labels['Diboson2022EE'],"F")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 0

Canvas_dijetMaxDeltaPhi = TCanvas("Canvas_dijetMaxDeltaPhi","Canvas_dijetMaxDeltaPhi",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas_dijetMaxDeltaPhi.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas_dijetMaxDeltaPhi.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas_dijetMaxDeltaPhi.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas_dijetMaxDeltaPhi.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas_dijetMaxDeltaPhi.SetLogy()
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].SetMinimum(0.0001)
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].SetMaximum(10000000.0)
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].GetYaxis().SetTitle("Entries per bin (0.1 width)")
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].SetTitle("")
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNNQCD'].Draw("HIST")
# DataHist_dijetMaxDeltaPhi.Draw("SAME,P,E")
errorHist_dijetMaxDeltaPhi.Draw("SAME,E2")
dijetMaxDeltaPhiStackedHists['WTopDiTTDYZNN'].Draw("SAME,HIST")
dijetMaxDeltaPhiStackedHists['WTopDiTT'].Draw("SAME,HIST")
dijetMaxDeltaPhiStackedHists['WTopDi'].Draw("SAME,HIST")
dijetMaxDeltaPhiStackedHists['WTop'].Draw("SAME,HIST")
dijetMaxDeltaPhiStackedHists['W'].Draw("SAME,HIST")
Legend_dijetMaxDeltaPhi.Draw()

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(Canvas_dijetMaxDeltaPhi, iPeriod, iPos)
Canvas_dijetMaxDeltaPhi.Update()
Canvas_dijetMaxDeltaPhi.Print("dijetMaxDeltaPhi_ZToMuMuISR.pdf")

