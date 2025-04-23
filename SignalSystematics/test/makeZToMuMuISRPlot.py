from array import *

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.utilities import *

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad

writeFile = False # Controls if user wants to make isrWeight_disappTrks_*.root file or PDF plots

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
if not writeFile: gStyle.SetOptStat(0)

dirs = getUser()

mc_condor_dir = dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISR_PostEE'
data_condor_dir = dirs['Breno'] + 'BGMC/Run3/2022/ZtoMuMuISRStudy_Muon2022F'

# Only datasets that have more than 0 entries
mcFiles = {
    'WToLNu_4Jets_2022EE' : 'hist_merged_WtoLNu_ZToMuMuISR_rebinned',
    'DYJetsToLL_M50_2022EE' : 'hist_merged_DYJetsToLL_ZToMuMuISR_rebinned',
    'WW_2022EE' : 'hist_merged_WW_ZToMuMuISR_rebinned',
    'WZ_2022EE' : 'hist_merged_WZ_ZToMuMuISR_rebinned',
    'ZZ_2022EE' : 'hist_merged_ZZ_ZToMuMuISR_rebinned',
    'TTto2L2Nu_2022EE' : 'hist_merged_TTto2L2Nu_ZToMuMuISR_rebinned',
    'TTtoLNu2Q_2022EE' : 'hist_merged_TTtoLNu2Q_ZToMuMuISR_rebinned',
    'TBbartoLplusNuBbar_2022EE' : 'hist_merged_TBbartoLplusNuBbar_ZToMuMuISR_rebinned',
    'TbarBtoLminusNuB_2022EE' : 'hist_merged_TbarBtoLminusNuB_ZToMuMuISR_rebinned',
    'TQbartoLNu_2022EE' : 'hist_merged_TQbartoLNu_ZToMuMuISR_rebinned',
    'TbarQtoLNu_2022EE' : 'hist_merged_TbarQtoLNu_ZToMuMuISR_rebinned',
    'TWminusto2L2Nu_2022EE' : 'hist_merged_TWminusto2L2Nu_ZToMuMuISR_rebinned',
    'TWminustoLNu2Q_2022EE' : 'hist_merged_TWminustoLNu2Q_ZToMuMuISR_rebinned',
    'TbarWplusto2L2Nu_2022EE' : 'hist_merged_TbarWplusto2L2Nu_ZToMuMuISR_rebinned',
    'TbarWplustoLNu2Q_2022EE' : 'hist_merged_TbarWplustoLNu2Q_ZToMuMuISR_rebinned'
}

dataFiles = {
    'Muon_2022F' : 'Muon_2022F',
}

nEvents = {
    'WToLNu_4Jets_2022EE' : 348442033 * 0.964, # Events in AOD * fraction of processed jobs
    'DYJetsToLL_M50_2022EE' : 94947242 * 0.971, # Events in AOD * fraction of processed jobs
    'WW_2022EE' : 53619680 * 0.986, # Events in AOD * fraction of processed jobs
    'WZ_2022EE' : 26887398 * 0.995, # Events in AOD * fraction of processed jobs
    'ZZ_2022EE' : 4043040 * 0.939, # Events in AOD * fraction of processed jobs
    'TTto2L2Nu_2022EE' : 85777130 * 0.970, # Events in AOD * fraction of processed jobs
    'TTtoLNu2Q_2022EE' : 270699232 * 0.982, # Events in AOD * fraction of processed jobs
    'TBbartoLplusNuBbar_2022EE' : 4469700 * 0.978, # Events in AOD * fraction of processed jobs
    'TbarBtoLminusNuB_2022EE' : 276266 * 0.968, # Events in AOD * fraction of processed jobs
    'TQbartoLNu_2022EE' : 32667420 * 0.984, # Events in AOD * fraction of processed jobs
    'TbarQtoLNu_2022EE' : 19537644 * 0.976, # Events in AOD * fraction of processed jobs
    'TWminusto2L2Nu_2022EE' : 8581640 * 0.989, # Events in AOD * fraction of processed jobs
    'TWminustoLNu2Q_2022EE' : 15859351 * 0.974, # Events in AOD * fraction of processed jobs
    'TbarWplusto2L2Nu_2022EE' : 8576050 * 0.977, # Events in AOD * fraction of processed jobs
    'TbarWplustoLNu2Q_2022EE' : 17273607 * 0.993 # Events in AOD * fraction of processed jobs
}

diMuonPtHists = {}
metNoMuHists = {}

for file in mcFiles:
    diMuonPtHists[file] = getHist(mcFiles[file],mc_condor_dir,'ZtoMuMuISRStudyPlotter','Muon-muon Plots/diMuonPtWide')
    diMuonPtHists[file].Scale(crossSections[file]/nEvents[file])
    if not writeFile: diMuonPtHists[file].Rebin(4)
    metNoMuHists[file] = getHist(mcFiles[file],mc_condor_dir,'ZtoMuMuISRStudyPlotter','Met Plots/metNoMu')
    metNoMuHists[file].Scale(crossSections[file]/nEvents[file])

for file in dataFiles:
    diMuonPtHists[file] = getHist(dataFiles[file],data_condor_dir,'ZtoMuMuISRStudyPlotter','Muon-muon Plots/diMuonPtWide')
    metNoMuHists[file] = getHist(dataFiles[file],data_condor_dir,'ZtoMuMuISRStudyPlotter','Met Plots/metNoMu')
    if not writeFile: diMuonPtHists[file].Rebin(4)

diMuonPtStackedHists = {}

diMuonPtStackedHists['W'] = diMuonPtHists['WToLNu_4Jets_2022EE']

WTopHist_diMuonPt = diMuonPtHists['WToLNu_4Jets_2022EE'].Clone("diMuonWTop")
WTopHist_diMuonPt.SetDirectory(0)
WTopHist_diMuonPt.Add(diMuonPtHists['TBbartoLplusNuBbar_2022EE'])
WTopHist_diMuonPt.Add(diMuonPtHists['TbarBtoLminusNuB_2022EE'])
WTopHist_diMuonPt.Add(diMuonPtHists['TQbartoLNu_2022EE'])
WTopHist_diMuonPt.Add(diMuonPtHists['TbarQtoLNu_2022EE'])
WTopHist_diMuonPt.Add(diMuonPtHists['TWminusto2L2Nu_2022EE'])
WTopHist_diMuonPt.Add(diMuonPtHists['TWminustoLNu2Q_2022EE'])
WTopHist_diMuonPt.Add(diMuonPtHists['TbarWplusto2L2Nu_2022EE'])
WTopHist_diMuonPt.Add(diMuonPtHists['TbarWplustoLNu2Q_2022EE'])
diMuonPtStackedHists['WTop'] = WTopHist_diMuonPt

WTopDiHist_diMuonPt = WTopHist_diMuonPt.Clone("diMuonWTopDi")
WTopDiHist_diMuonPt.SetDirectory(0)
WTopDiHist_diMuonPt.Add(diMuonPtHists['WW_2022EE'])
WTopDiHist_diMuonPt.Add(diMuonPtHists['WZ_2022EE'])
WTopDiHist_diMuonPt.Add(diMuonPtHists['ZZ_2022EE'])
diMuonPtStackedHists['WTopDi'] = WTopDiHist_diMuonPt

WTopDiTTHist_diMuonPt = WTopDiHist_diMuonPt.Clone("diMuonWTopDiTT")
WTopDiTTHist_diMuonPt.SetDirectory(0)
WTopDiTTHist_diMuonPt.Add(diMuonPtHists['TTto2L2Nu_2022EE'])
WTopDiTTHist_diMuonPt.Add(diMuonPtHists['TTtoLNu2Q_2022EE'])
diMuonPtStackedHists['WTopDiTT'] = WTopDiTTHist_diMuonPt

WTopDiTTDYHist_diMuonPt = WTopDiTTHist_diMuonPt.Clone("diMuonWTopDiTTDY")
WTopDiTTDYHist_diMuonPt.SetDirectory(0)
WTopDiTTDYHist_diMuonPt.Add(diMuonPtHists['DYJetsToLL_M50_2022EE'])
diMuonPtStackedHists['WTopDiTTDY'] = WTopDiTTDYHist_diMuonPt

# Just for plotting
QCDHist_diMuonPt = diMuonPtHists['WToLNu_4Jets_2022EE'].Clone("diMuonQCD")
QCDHist_diMuonPt.SetDirectory(0)
QCDHist_diMuonPt.SetFillColor(colors['QCD2022EE'])
QCDHist_diMuonPt.SetLineColor(1)

ZTo2NuHist_diMuonPt = diMuonPtHists['WToLNu_4Jets_2022EE'].Clone("diMuonZTo2Nu")
ZTo2NuHist_diMuonPt.SetDirectory(0)
ZTo2NuHist_diMuonPt.SetFillColor(colors['ZJetsToNuNu2022EE'])
ZTo2NuHist_diMuonPt.SetLineColor(1)

errorHist_diMuonPt = WTopDiTTDYHist_diMuonPt = diMuonPtStackedHists['WTopDiTTDY'].Clone("error_diMuonWTopDiTTDY")
errorHist_diMuonPt.SetDirectory(0)

DataHist_diMuonPt = diMuonPtHists['Muon_2022F'].Clone("DataHist_diMuonPt")
DataHist_diMuonPt.SetDirectory(0)

errorHist_diMuonPt.Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WTopDiTTDY'].GetMaximum()))
diMuonPtStackedHists['W'].Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WTopDiTTDY'].GetMaximum()))
diMuonPtStackedHists['WTop'].Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WTopDiTTDY'].GetMaximum()))
diMuonPtStackedHists['WTopDi'].Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WTopDiTTDY'].GetMaximum()))
diMuonPtStackedHists['WTopDiTT'].Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WTopDiTTDY'].GetMaximum()))
diMuonPtStackedHists['WTopDiTTDY'].Scale((DataHist_diMuonPt.GetMaximum())/(diMuonPtStackedHists['WTopDiTTDY'].GetMaximum()))

diMuonPtStackedHists['W'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
diMuonPtStackedHists['WTop'].SetFillColor(colors['SingleTop2022EE'])
diMuonPtStackedHists['WTopDi'].SetFillColor(colors['Diboson2022EE'])
diMuonPtStackedHists['WTopDiTT'].SetFillColor(colors['TT2022EE'])
diMuonPtStackedHists['WTopDiTTDY'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
errorHist_diMuonPt.SetFillColor(1)
errorHist_diMuonPt.SetFillStyle(3001)
diMuonPtStackedHists['W'].SetLineColor(1)
diMuonPtStackedHists['WTop'].SetLineColor(1)
diMuonPtStackedHists['WTopDi'].SetLineColor(1)
diMuonPtStackedHists['WTopDiTT'].SetLineColor(1)
diMuonPtStackedHists['WTopDiTTDY'].SetLineColor(1)
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
Legend_diMuonPt.AddEntry(diMuonPtStackedHists['WTopDiTTDY'],labels['DYJetsToLL2022EE'],"F")
Legend_diMuonPt.AddEntry(diMuonPtStackedHists['WTopDiTT'],labels['TT2022EE'],"F")
Legend_diMuonPt.AddEntry(diMuonPtStackedHists['WTopDi'],labels['Diboson2022EE'],"F")
Legend_diMuonPt.AddEntry(diMuonPtStackedHists['WTop'],labels['SingleTop2022EE'],"F")
Legend_diMuonPt.AddEntry(diMuonPtStackedHists['W'],labels['WToLNu_4Jets_2022EE'],"F")

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
diMuonPtStackedHists['WTopDiTTDY'].SetMinimum(0.0002)
diMuonPtStackedHists['WTopDiTTDY'].SetMaximum(10000000.0)
diMuonPtStackedHists['WTopDiTTDY'].SetAxisRange(0,1000,"X")
DataHist_diMuonPt.SetAxisRange(0,1000,"X")
diMuonPtStackedHists['WTopDiTTDY'].GetXaxis().SetTitle("Entries / 4 GeV")
diMuonPtStackedHists['WTopDiTTDY'].SetTitle("")
diMuonPtStackedHists['WTopDiTTDY'].Draw("HIST")
errorHist_diMuonPt.Draw("SAME,E2")
DataHist_diMuonPt.Draw("SAME,P,E")
diMuonPtStackedHists['WTopDiTT'].Draw("SAME,HIST")
diMuonPtStackedHists['WTopDi'].Draw("SAME,HIST")
diMuonPtStackedHists['WTop'].Draw("SAME,HIST")
diMuonPtStackedHists['W'].Draw("SAME,HIST")
Legend_diMuonPt.Draw()

p2_diMuonPt.cd()
p2_diMuonPt.SetGridy()
ratio_diMuonPt = ratioHistogram(DataHist_diMuonPt,diMuonPtStackedHists['WTopDiTTDY'],addOne=True)
ratio_diMuonPt.SetMinimum(0.0)
ratio_diMuonPt.SetMaximum(2.5)
ratio_diMuonPt.GetXaxis().SetRangeUser(0,1000)
ratio_diMuonPt.SetTitle("")
ratio_diMuonPt.GetXaxis().SetTitle("p_{T}(#mu#mu) [GeV]")
ratio_diMuonPt.GetYaxis().SetTitle("Data/MC")
ratio_diMuonPt.GetXaxis().SetTitleOffset(1.12)

if writeFile:
    ratioFile = TFile.Open("isrWeight_disappTrks_run3.root","RECREATE")
    ratio_diMuonPt.SetName("Muon_2022F")
    ratio_diMuonPt.GetXaxis().SetRangeUser(0,932)
    ratio_diMuonPt.Write()
    ratioFile.Close()

else:
    ratio_diMuonPt.GetXaxis().SetTitleSize(0.12)
    ratio_diMuonPt.GetXaxis().SetLabelSize(0.12)
    ratio_diMuonPt.GetYaxis().SetTitleSize(0.12)
    ratio_diMuonPt.GetYaxis().SetLabelSize(0.12)
    ratio_diMuonPt.GetYaxis().SetTitleOffset(0.42)
    ratio_diMuonPt.Draw()

Canvas_diMuonPt.Update()
Canvas_diMuonPt.Print("diMuonPt_ZToMuMuISR.pdf")

metNoMuStackedHists = {}

metNoMuStackedHists['W'] = metNoMuHists['WToLNu_4Jets_2022EE']

WTopHist_metNoMu = metNoMuHists['WToLNu_4Jets_2022EE'].Clone("metNoMuWTop")
WTopHist_metNoMu.SetDirectory(0)
WTopHist_metNoMu.Add(metNoMuHists['TBbartoLplusNuBbar_2022EE'])
WTopHist_metNoMu.Add(metNoMuHists['TbarBtoLminusNuB_2022EE'])
WTopHist_metNoMu.Add(metNoMuHists['TQbartoLNu_2022EE'])
WTopHist_metNoMu.Add(metNoMuHists['TbarQtoLNu_2022EE'])
WTopHist_metNoMu.Add(metNoMuHists['TWminusto2L2Nu_2022EE'])
WTopHist_metNoMu.Add(metNoMuHists['TWminustoLNu2Q_2022EE'])
WTopHist_metNoMu.Add(metNoMuHists['TbarWplusto2L2Nu_2022EE'])
WTopHist_metNoMu.Add(metNoMuHists['TbarWplustoLNu2Q_2022EE'])
metNoMuStackedHists['WTop'] = WTopHist_metNoMu

WTopDiHist_metNoMu = WTopHist_metNoMu.Clone("metNoMuWTopDi")
WTopDiHist_metNoMu.SetDirectory(0)
WTopDiHist_metNoMu.Add(metNoMuHists['WW_2022EE'])
WTopDiHist_metNoMu.Add(metNoMuHists['WZ_2022EE'])
WTopDiHist_metNoMu.Add(metNoMuHists['ZZ_2022EE'])
metNoMuStackedHists['WTopDi'] = WTopDiHist_metNoMu

WTopDiTTHist_metNoMu = WTopDiHist_metNoMu.Clone("metNoMuWTopDiTT")
WTopDiTTHist_metNoMu.SetDirectory(0)
WTopDiTTHist_metNoMu.Add(metNoMuHists['TTto2L2Nu_2022EE'])
WTopDiTTHist_metNoMu.Add(metNoMuHists['TTtoLNu2Q_2022EE'])
metNoMuStackedHists['WTopDiTT'] = WTopDiTTHist_metNoMu

WTopDiTTDYHist_metNoMu = WTopDiTTHist_metNoMu.Clone("metNoMuWTopDiTTDY")
WTopDiTTDYHist_metNoMu.SetDirectory(0)
WTopDiTTDYHist_metNoMu.Add(metNoMuHists['DYJetsToLL_M50_2022EE'])
metNoMuStackedHists['WTopDiTTDY'] = WTopDiTTDYHist_metNoMu

# Just for plotting
QCDHist_metNoMu = metNoMuHists['WToLNu_4Jets_2022EE'].Clone("metNoMuQCD")
QCDHist_metNoMu.SetDirectory(0)
QCDHist_metNoMu.SetFillColor(colors['QCD2022EE'])
QCDHist_metNoMu.SetLineColor(1)

ZTo2NuHist_metNoMu = metNoMuHists['WToLNu_4Jets_2022EE'].Clone("metNoMuZTo2Nu")
ZTo2NuHist_metNoMu.SetDirectory(0)
ZTo2NuHist_metNoMu.SetFillColor(colors['ZJetsToNuNu2022EE'])
ZTo2NuHist_metNoMu.SetLineColor(1)

errorHist_metNoMu = WTopDiTTDYHist_metNoMu = metNoMuStackedHists['WTopDiTTDY'].Clone("error_metNoMuWTopDiTTDY")
errorHist_metNoMu.SetDirectory(0)

DataHist_metNoMu = metNoMuHists['Muon_2022F'].Clone("DataHist_metNoMu")
DataHist_metNoMu.SetDirectory(0)

errorHist_metNoMu.Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WTopDiTTDY'].GetMaximum()))
metNoMuStackedHists['W'].Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WTopDiTTDY'].GetMaximum()))
metNoMuStackedHists['WTop'].Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WTopDiTTDY'].GetMaximum()))
metNoMuStackedHists['WTopDi'].Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WTopDiTTDY'].GetMaximum()))
metNoMuStackedHists['WTopDiTT'].Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WTopDiTTDY'].GetMaximum()))
metNoMuStackedHists['WTopDiTTDY'].Scale((DataHist_metNoMu.GetMaximum())/(metNoMuStackedHists['WTopDiTTDY'].GetMaximum()))

metNoMuStackedHists['W'].SetFillColor(colors['WToLNu_4Jets_2022EE'])
metNoMuStackedHists['WTop'].SetFillColor(colors['SingleTop2022EE'])
metNoMuStackedHists['WTopDi'].SetFillColor(colors['Diboson2022EE'])
metNoMuStackedHists['WTopDiTT'].SetFillColor(colors['TT2022EE'])
metNoMuStackedHists['WTopDiTTDY'].SetFillColor(colors['DYJetsToLL_M50_2022EE'])
errorHist_metNoMu.SetFillColor(1)
errorHist_metNoMu.SetFillStyle(3001)
metNoMuStackedHists['W'].SetLineColor(1)
metNoMuStackedHists['WTop'].SetLineColor(1)
metNoMuStackedHists['WTopDi'].SetLineColor(1)
metNoMuStackedHists['WTopDiTT'].SetLineColor(1)
metNoMuStackedHists['WTopDiTTDY'].SetLineColor(1)
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
Legend_metNoMu.AddEntry(metNoMuStackedHists['WTopDiTTDY'],labels['DYJetsToLL2022EE'],"F")
Legend_metNoMu.AddEntry(metNoMuStackedHists['WTopDiTT'],labels['TT2022EE'],"F")
Legend_metNoMu.AddEntry(metNoMuStackedHists['WTopDi'],labels['Diboson2022EE'],"F")
Legend_metNoMu.AddEntry(metNoMuStackedHists['WTop'],labels['SingleTop2022EE'],"F")
Legend_metNoMu.AddEntry(metNoMuStackedHists['W'],labels['WToLNu_4Jets_2022EE'],"F")
# Legend_metNoMu.AddEntry(QCDHist_metNoMu,labels['QCD2022EE'],"F")
# Legend_metNoMu.AddEntry(ZTo2NuHist_metNoMu,labels['ZJetsToNuNu2022EE'],"F")

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
metNoMuStackedHists['WTopDiTTDY'].SetMinimum(0.000002)
metNoMuStackedHists['WTopDiTTDY'].SetMaximum(10000000.0)
metNoMuStackedHists['WTopDiTTDY'].GetXaxis().SetRangeUser(0,950)
metNoMuStackedHists['WTopDiTTDY'].SetTitle("")
metNoMuStackedHists['WTopDiTTDY'].Draw("HIST")
errorHist_metNoMu.Draw("SAME,E2")
DataHist_metNoMu.Draw("SAME,P,E")
metNoMuStackedHists['WTopDiTT'].Draw("SAME,HIST")
metNoMuStackedHists['WTopDi'].Draw("SAME,HIST")
metNoMuStackedHists['WTop'].Draw("SAME,HIST")
metNoMuStackedHists['W'].Draw("SAME,HIST")
Legend_metNoMu.Draw()

p2_metNoMu.cd()
p2_metNoMu.SetGridy()
ratio_metNoMu = ratioHistogram(DataHist_metNoMu,metNoMuStackedHists['WTopDiTTDY'],addOne=True)
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
del WTopHist_diMuonPt
del WTopDiHist_diMuonPt
del WTopDiTTHist_diMuonPt
del WTopDiTTDYHist_diMuonPt
del QCDHist_diMuonPt
del ZTo2NuHist_diMuonPt

del errorHist_metNoMu
del DataHist_metNoMu
del WTopHist_metNoMu
del WTopDiHist_metNoMu
del WTopDiTTHist_metNoMu
del WTopDiTTDYHist_metNoMu
del QCDHist_metNoMu
del ZTo2NuHist_metNoMu
