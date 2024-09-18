from array import *

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.utilities import *

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)

dirs = getUser()

# Only datasets that have more than 0 entries
mcFiles = {
    'WToLNu_4Jets_2022EE' : dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISR_PostEE/hist_merged_WtoLNu_ZToMuMuISR.root',
    'DYJetsToLL_M50_2022EE' : dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISR_PostEE/hist_merged_DYJetsToLL_ZToMuMuISR.root',
    'WW_2022EE' : dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISR_PostEE/hist_merged_WW_ZToMuMuISR.root',
    'WZ_2022EE' : dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISR_PostEE/hist_merged_WZ_ZToMuMuISR.root',
    'ZZ_2022EE' : dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISR_PostEE/hist_merged_ZZ_ZToMuMuISR.root',
    'TTto2L2Nu_2022EE' : dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISR_PostEE/hist_merged_TTto2L2Nu_ZToMuMuISR.root',
    'TTtoLNu2Q_2022EE' : dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISR_PostEE/hist_merged_TTtoLNu2Q_ZToMuMuISR.root'
}

dataFiles = {
    'Muon_2022F' : dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISRStudy_Muon2022F/Muon_2022F.root',
}

nEvents = {
    'WToLNu_4Jets_2022EE' : 348442033 * 0.964, # Events in AOD * fraction of processed jobs
    'DYJetsToLL_M50_2022EE' : 94947242 * 0.971, # Events in AOD * fraction of processed jobs
    'WW_2022EE' : 53619680 * 0.986, # Events in AOD * fraction of processed jobs
    'WZ_2022EE' : 26887398 * 0.995, # Events in AOD * fraction of processed jobs
    'ZZ_2022EE' : 4043040 * 0.939, # Events in AOD * fraction of processed jobs
    'TTto2L2Nu_2022EE' : 85777130 * 0.970, # Events in AOD * fraction of processed jobs
    'TTtoLNu2Q_2022EE' : 270699232 * 0.982, # Events in AOD * fraction of processed jobs
}

compositeCrossSections = {
    'Diboson' : crossSections['WW_2022EE'] + crossSections['WZ_2022EE'] + crossSections['ZZ_2022EE'],
    'TT': crossSections['TTto2L2Nu_2022EE'] + crossSections['TTtoLNu2Q_2022EE'],
}

stackedCrossSections = {
    'WDi' : crossSections['WToLNu_4Jets_2022EE'] + compositeCrossSections['Diboson'],
    'WDiTT' : crossSections['WToLNu_4Jets_2022EE'] + compositeCrossSections['Diboson'] + compositeCrossSections['TT'],
    'WDiTTDY' : crossSections['WToLNu_4Jets_2022EE'] + compositeCrossSections['Diboson'] + compositeCrossSections['TT'] + crossSections['DYJetsToLL_M50_2022EE'],
}

diMuonPtHists = {}
metNoMuHists = {}

for file in mcFiles:
    if 'condor' not in mcFiles[file]: mcFiles[file] = 'condor/' + mcFiles[file] # getUser() doesn't add condor back if Breno is using, so this is needed in that case
    inputFile = TFile(mcFiles[file])
    diMuonPtHists[file] = inputFile.Get("ZtoMuMuISRStudyPlotter/Muon-muon Plots/diMuonPt").Clone('diMuon' + file)
    diMuonPtHists[file].Scale(crossSections[file]/nEvents[file])
    diMuonPtHists[file].SetDirectory(0)
    metNoMuHists[file] = inputFile.Get("ZtoMuMuISRStudyPlotter/Met Plots/metNoMu").Clone('metNoMu' + file)
    metNoMuHists[file].Scale(crossSections[file]/nEvents[file])
    metNoMuHists[file].SetDirectory(0)
    inputFile.Close()
    del inputFile

for file in dataFiles:
    if 'condor' not in dataFiles[file]: dataFiles[file] = 'condor/' + dataFiles[file] # getUser() doesn't add condor back if Breno is using, so this is needed in that case
    inputFile = TFile(dataFiles[file])
    diMuonPtHists[file] = inputFile.Get("ZtoMuMuISRStudyPlotter/Muon-muon Plots/diMuonPt").Clone('diMuon' + file)
    diMuonPtHists[file].SetDirectory(0)
    metNoMuHists[file] = inputFile.Get("ZtoMuMuISRStudyPlotter/Met Plots/metNoMu").Clone('metNoMu' + file)
    metNoMuHists[file].SetDirectory(0)
    inputFile.Close()
    del inputFile

diMuonPtStackedHists = {}

diMuonPtStackedHists['W'] = diMuonPtHists['WToLNu_4Jets_2022EE']

WDiHist_diMuonPt = diMuonPtHists['WToLNu_4Jets_2022EE'].Clone("diMuonWDi")
WDiHist_diMuonPt.SetDirectory(0)
WDiHist_diMuonPt.Add(diMuonPtHists['WW_2022EE'])
WDiHist_diMuonPt.Add(diMuonPtHists['WZ_2022EE'])
WDiHist_diMuonPt.Add(diMuonPtHists['ZZ_2022EE'])
diMuonPtStackedHists['WDi'] = WDiHist_diMuonPt

WDiTTHist_diMuonPt = WDiHist_diMuonPt.Clone("diMuonWDiTT")
WDiTTHist_diMuonPt.SetDirectory(0)
WDiTTHist_diMuonPt.Add(diMuonPtHists['TTto2L2Nu_2022EE'])
WDiTTHist_diMuonPt.Add(diMuonPtHists['TTtoLNu2Q_2022EE'])
diMuonPtStackedHists['WDiTT'] = WDiTTHist_diMuonPt

WDiTTDYHist_diMuonPt = WDiTTHist_diMuonPt.Clone("diMuonWDiTTDY")
WDiTTDYHist_diMuonPt.SetDirectory(0)
WDiTTDYHist_diMuonPt.Add(diMuonPtHists['DYJetsToLL_M50_2022EE'])
diMuonPtStackedHists['WDiTTDY'] = WDiTTDYHist_diMuonPt

# Just for plotting
singleTopHist_diMuonPt = diMuonPtHists['WToLNu_4Jets_2022EE'].Clone("diMuonsingleTop")
singleTopHist_diMuonPt.SetDirectory(0)
singleTopHist_diMuonPt.SetFillColor(colors['SingleTop2022EE'])
singleTopHist_diMuonPt.SetLineColor(1)

QCDHist_diMuonPt = diMuonPtHists['WToLNu_4Jets_2022EE'].Clone("diMuonQCD")
QCDHist_diMuonPt.SetDirectory(0)
QCDHist_diMuonPt.SetFillColor(colors['QCD2022EE'])
QCDHist_diMuonPt.SetLineColor(1)

ZTo2NuHist_diMuonPt = diMuonPtHists['WToLNu_4Jets_2022EE'].Clone("diMuonZTo2Nu")
ZTo2NuHist_diMuonPt.SetDirectory(0)
ZTo2NuHist_diMuonPt.SetFillColor(colors['ZJetsToNuNu2022EE'])
ZTo2NuHist_diMuonPt.SetLineColor(1)

errorHist_diMuonPt = WDiTTDYHist_diMuonPt = diMuonPtStackedHists['WDiTTDY'].Clone("diMuonWDiTTDY")
errorHist_diMuonPt.SetDirectory(0)

DataHist_diMuonPt = diMuonPtHists['Muon_2022F'].Clone("DataHist_diMuonPt")
DataHist_diMuonPt.SetDirectory(0)

errorHist_diMuonPt.Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WDiTTDY'].GetMaximum()))
diMuonPtStackedHists['W'].Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WDiTTDY'].GetMaximum()))
diMuonPtStackedHists['WDi'].Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WDiTTDY'].GetMaximum()))
diMuonPtStackedHists['WDiTT'].Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WDiTTDY'].GetMaximum()))
diMuonPtStackedHists['WDiTTDY'].Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WDiTTDY'].GetMaximum()))

diMuonPtStackedHists['W'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
diMuonPtStackedHists['WDi'].SetFillColor(colors['Diboson2022EE'])
diMuonPtStackedHists['WDiTT'].SetFillColor(colors['TT2022EE'])
diMuonPtStackedHists['WDiTTDY'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
errorHist_diMuonPt.SetFillColor(1)
errorHist_diMuonPt.SetFillStyle(3001)
diMuonPtStackedHists['W'].SetLineColor(1)
diMuonPtStackedHists['WDi'].SetLineColor(1)
diMuonPtStackedHists['WDiTT'].SetLineColor(1)
diMuonPtStackedHists['WDiTTDY'].SetLineColor(1)
errorHist_diMuonPt.SetLineColor(1)

DataHist_diMuonPt.SetMarkerStyle(20)
DataHist_diMuonPt.SetLineColor(1)

Legend_diMuonPt = TLegend(0.7,0.65,0.9,0.9)
Legend_diMuonPt.SetBorderSize(0)
Legend_diMuonPt.SetFillColor(0)
Legend_diMuonPt.SetFillStyle(0)
Legend_diMuonPt.SetTextSize(0.03)
Legend_diMuonPt.AddEntry(DataHist_diMuonPt,"Muon 2022F data","P")
Legend_diMuonPt.AddEntry(errorHist_diMuonPt,"stat. errors","F")
Legend_diMuonPt.AddEntry(diMuonPtStackedHists['WDiTTDY'],labels['DYJetsToLL2022EE'],"F")
Legend_diMuonPt.AddEntry(diMuonPtStackedHists['WDiTT'],labels['TT2022EE'],"F")
Legend_diMuonPt.AddEntry(diMuonPtStackedHists['WDi'],labels['Diboson2022EE'],"F")
Legend_diMuonPt.AddEntry(diMuonPtStackedHists['W'],labels['WToLNu_4Jets_2022EE'],"F")
Legend_diMuonPt.AddEntry(singleTopHist_diMuonPt,labels['SingleTop2022EE'],"F")
Legend_diMuonPt.AddEntry(QCDHist_diMuonPt,labels['QCD2022EE'],"F")
Legend_diMuonPt.AddEntry(ZTo2NuHist_diMuonPt,labels['ZJetsToNuNu2022EE'],"F")

Canvas_diMuonPt = TCanvas("oia","oia",700,700)
p1_diMuonPt = TPad("p1_diMuonPt", "", 0.0, 0.20, 1.0, 1.0, 21)
p2_diMuonPt = TPad("p2_diMuonPt", "", 0.0, 0.0, 1.0, 0.205, 21)
Canvas_diMuonPt.cd()
p1_diMuonPt.SetFillColor(0)
p2_diMuonPt.SetFillColor(0)
p1_diMuonPt.SetTopMargin(0.08)
p1_diMuonPt.SetBottomMargin(0.013)
p1_diMuonPt.SetLeftMargin(0.15)
p1_diMuonPt.SetRightMargin(0.05)
p2_diMuonPt.SetTopMargin(0.05)
p2_diMuonPt.SetBottomMargin(0.3)
p2_diMuonPt.SetLeftMargin(0.15)
p2_diMuonPt.SetRightMargin(0.05)
p1_diMuonPt.Draw()
p2_diMuonPt.Draw()
p1_diMuonPt.cd()
p1_diMuonPt.SetLogy()
diMuonPtStackedHists['WDiTTDY'].SetMinimum(0.000002)
diMuonPtStackedHists['WDiTTDY'].SetMaximum(10000000.0)
diMuonPtStackedHists['WDiTTDY'].SetTitle("")
diMuonPtStackedHists['WDiTTDY'].Draw("HIST")
errorHist_diMuonPt.Draw("SAME,E2")
DataHist_diMuonPt.Draw("SAME,P,E")
diMuonPtStackedHists['WDiTT'].Draw("SAME,HIST")
diMuonPtStackedHists['WDi'].Draw("SAME,HIST")
diMuonPtStackedHists['W'].Draw("SAME,HIST")
Legend_diMuonPt.Draw()

p2_diMuonPt.cd()
p2_diMuonPt.SetGridy()
ratio_diMuonPt = ratioHistogram(DataHist_diMuonPt,diMuonPtStackedHists['WDiTTDY'],addOne=True)
ratio_diMuonPt.SetMinimum(0.0)
ratio_diMuonPt.SetMaximum(2.5)
ratio_diMuonPt.SetTitle("")
ratio_diMuonPt.GetXaxis().SetTitleSize(0.12)
ratio_diMuonPt.GetXaxis().SetLabelSize(0.12)
ratio_diMuonPt.GetXaxis().SetTitle("p_{T}(#mu#mu) [GeV]")
ratio_diMuonPt.GetXaxis().SetTitleOffset(1.12)
ratio_diMuonPt.GetYaxis().SetTitle("Data/MC")
ratio_diMuonPt.GetYaxis().SetTitleSize(0.12)
ratio_diMuonPt.GetYaxis().SetLabelSize(0.12)
ratio_diMuonPt.GetYaxis().SetTitleOffset(0.42)
ratio_diMuonPt.Draw()

Canvas_diMuonPt.Update()
Canvas_diMuonPt.Print("diMuonPt_ZToMuMuISR.pdf")



metNoMuStackedHists = {}

metNoMuStackedHists['W'] = metNoMuHists['WToLNu_4Jets_2022EE']

WDiHist_metNoMu = metNoMuHists['WToLNu_4Jets_2022EE'].Clone("metNoMuWDi")
WDiHist_metNoMu.SetDirectory(0)
WDiHist_metNoMu.Add(metNoMuHists['WW_2022EE'])
WDiHist_metNoMu.Add(metNoMuHists['WZ_2022EE'])
WDiHist_metNoMu.Add(metNoMuHists['ZZ_2022EE'])
metNoMuStackedHists['WDi'] = WDiHist_metNoMu

WDiTTHist_metNoMu = WDiHist_metNoMu.Clone("metNoMuWDiTT")
WDiTTHist_metNoMu.SetDirectory(0)
WDiTTHist_metNoMu.Add(metNoMuHists['TTto2L2Nu_2022EE'])
WDiTTHist_metNoMu.Add(metNoMuHists['TTtoLNu2Q_2022EE'])
metNoMuStackedHists['WDiTT'] = WDiTTHist_metNoMu

WDiTTDYHist_metNoMu = WDiTTHist_metNoMu.Clone("metNoMuWDiTTDY")
WDiTTDYHist_metNoMu.SetDirectory(0)
WDiTTDYHist_metNoMu.Add(metNoMuHists['DYJetsToLL_M50_2022EE'])
metNoMuStackedHists['WDiTTDY'] = WDiTTDYHist_metNoMu

# Just for plotting
singleTopHist_metNoMu = metNoMuHists['WToLNu_4Jets_2022EE'].Clone("metNoMusingleTop")
singleTopHist_metNoMu.SetDirectory(0)
singleTopHist_metNoMu.SetFillColor(colors['SingleTop2022EE'])
singleTopHist_metNoMu.SetLineColor(1)

QCDHist_metNoMu = metNoMuHists['WToLNu_4Jets_2022EE'].Clone("metNoMuQCD")
QCDHist_metNoMu.SetDirectory(0)
QCDHist_metNoMu.SetFillColor(colors['QCD2022EE'])
QCDHist_metNoMu.SetLineColor(1)

ZTo2NuHist_metNoMu = metNoMuHists['WToLNu_4Jets_2022EE'].Clone("metNoMuZTo2Nu")
ZTo2NuHist_metNoMu.SetDirectory(0)
ZTo2NuHist_metNoMu.SetFillColor(colors['ZJetsToNuNu2022EE'])
ZTo2NuHist_metNoMu.SetLineColor(1)

errorHist_metNoMu = WDiTTDYHist_metNoMu = metNoMuStackedHists['WDiTTDY'].Clone("metNoMuWDiTTDY")
errorHist_metNoMu.SetDirectory(0)

DataHist_metNoMu = metNoMuHists['Muon_2022F'].Clone("DataHist_metNoMu")
DataHist_metNoMu.SetDirectory(0)

errorHist_metNoMu.Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WDiTTDY'].GetMaximum()))
metNoMuStackedHists['W'].Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WDiTTDY'].GetMaximum()))
metNoMuStackedHists['WDi'].Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WDiTTDY'].GetMaximum()))
metNoMuStackedHists['WDiTT'].Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WDiTTDY'].GetMaximum()))
metNoMuStackedHists['WDiTTDY'].Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WDiTTDY'].GetMaximum()))

metNoMuStackedHists['W'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
metNoMuStackedHists['WDi'].SetFillColor(colors['Diboson2022EE'])
metNoMuStackedHists['WDiTT'].SetFillColor(colors['TT2022EE'])
metNoMuStackedHists['WDiTTDY'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
errorHist_metNoMu.SetFillColor(1)
errorHist_metNoMu.SetFillStyle(3001)
metNoMuStackedHists['W'].SetLineColor(1)
metNoMuStackedHists['WDi'].SetLineColor(1)
metNoMuStackedHists['WDiTT'].SetLineColor(1)
metNoMuStackedHists['WDiTTDY'].SetLineColor(1)
errorHist_metNoMu.SetLineColor(1)

DataHist_metNoMu.SetMarkerStyle(20)
DataHist_metNoMu.SetLineColor(1)

Legend_metNoMu = TLegend(0.7,0.65,0.9,0.9)
Legend_metNoMu.SetBorderSize(0)
Legend_metNoMu.SetFillColor(0)
Legend_metNoMu.SetFillStyle(0)
Legend_metNoMu.SetTextSize(0.03)
Legend_metNoMu.AddEntry(DataHist_metNoMu,"Muon 2022F data","P")
Legend_metNoMu.AddEntry(errorHist_metNoMu,"stat. errors","F")
Legend_metNoMu.AddEntry(metNoMuStackedHists['WDiTTDY'],labels['DYJetsToLL2022EE'],"F")
Legend_metNoMu.AddEntry(metNoMuStackedHists['WDiTT'],labels['TT2022EE'],"F")
Legend_metNoMu.AddEntry(metNoMuStackedHists['WDi'],labels['Diboson2022EE'],"F")
Legend_metNoMu.AddEntry(metNoMuStackedHists['W'],labels['WToLNu_4Jets_2022EE'],"F")
Legend_metNoMu.AddEntry(singleTopHist_metNoMu,labels['SingleTop2022EE'],"F")
Legend_metNoMu.AddEntry(QCDHist_metNoMu,labels['QCD2022EE'],"F")
Legend_metNoMu.AddEntry(ZTo2NuHist_metNoMu,labels['ZJetsToNuNu2022EE'],"F")

Canvas_metNoMu = TCanvas("oia","oia",700,700)
p1_metNoMu = TPad("p1_metNoMu", "", 0.0, 0.20, 1.0, 1.0, 21)
p2_metNoMu = TPad("p2_metNoMu", "", 0.0, 0.0, 1.0, 0.205, 21)
Canvas_metNoMu.cd()
p1_metNoMu.SetFillColor(0)
p2_metNoMu.SetFillColor(0)
p1_metNoMu.SetTopMargin(0.08)
p1_metNoMu.SetBottomMargin(0.013)
p1_metNoMu.SetLeftMargin(0.15)
p1_metNoMu.SetRightMargin(0.05)
p2_metNoMu.SetTopMargin(0.05)
p2_metNoMu.SetBottomMargin(0.3)
p2_metNoMu.SetLeftMargin(0.15)
p2_metNoMu.SetRightMargin(0.05)
p1_metNoMu.Draw()
p2_metNoMu.Draw()
p1_metNoMu.cd()
p1_metNoMu.SetLogy()
metNoMuStackedHists['WDiTTDY'].SetMinimum(0.000002)
metNoMuStackedHists['WDiTTDY'].SetMaximum(10000000.0)
metNoMuStackedHists['WDiTTDY'].GetXaxis().SetRangeUser(0,950)
metNoMuStackedHists['WDiTTDY'].SetTitle("")
metNoMuStackedHists['WDiTTDY'].Draw("HIST")
errorHist_metNoMu.Draw("SAME,E2")
DataHist_metNoMu.Draw("SAME,P,E")
metNoMuStackedHists['WDiTT'].Draw("SAME,HIST")
metNoMuStackedHists['WDi'].Draw("SAME,HIST")
metNoMuStackedHists['W'].Draw("SAME,HIST")
Legend_metNoMu.Draw()

p2_metNoMu.cd()
p2_metNoMu.SetGridy()
ratio_metNoMu = ratioHistogram(DataHist_metNoMu,metNoMuStackedHists['WDiTTDY'],addOne=True)
ratio_metNoMu.SetMinimum(0.0)
ratio_metNoMu.SetMaximum(2.5)
ratio_metNoMu.GetXaxis().SetRangeUser(0,950)
ratio_metNoMu.SetTitle("")
ratio_metNoMu.GetXaxis().SetTitleSize(0.12)
ratio_metNoMu.GetXaxis().SetLabelSize(0.12)
ratio_metNoMu.GetXaxis().SetTitle("E_{T}^{miss, no #mu} [GeV]")
ratio_metNoMu.GetXaxis().SetTitleOffset(1.12)
ratio_metNoMu.GetYaxis().SetTitle("Data/MC")
ratio_metNoMu.GetYaxis().SetTitleSize(0.12)
ratio_metNoMu.GetYaxis().SetLabelSize(0.12)
ratio_metNoMu.GetYaxis().SetTitleOffset(0.42)
ratio_metNoMu.Draw()

Canvas_metNoMu.Update()
Canvas_metNoMu.Print("metNoMu_ZToMuMuISR.pdf")

auxList = []
for key in diMuonPtStackedHists:
    auxList.append(key)
for key in auxList:
    del diMuonPtStackedHists[key]

auxList = []
for key in metNoMuStackedHists:
    auxList.append(key)
for key in auxList:
    del metNoMuStackedHists[key]

auxList = []    
for key in diMuonPtHists:
    auxList.append(key)
for key in auxList:
    del diMuonPtHists[key]

auxList = []
for key in metNoMuHists:
    auxList.append(key)
for key in auxList:
    del metNoMuHists[key]

del errorHist_diMuonPt
del DataHist_diMuonPt
del WDiHist_diMuonPt
del WDiTTHist_diMuonPt
del WDiTTDYHist_diMuonPt
del singleTopHist_diMuonPt
del QCDHist_diMuonPt
del ZTo2NuHist_diMuonPt

del errorHist_metNoMu
del DataHist_metNoMu
del WDiHist_metNoMu
del WDiTTHist_metNoMu
del WDiTTDYHist_metNoMu
del singleTopHist_metNoMu
del QCDHist_metNoMu
del ZTo2NuHist_metNoMu
