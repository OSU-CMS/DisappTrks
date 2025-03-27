from array import *

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.miniAOD_124X_Samples import dataset_names_bkgd

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad, TLine

def modHist(h,color):
    h.SetLineColor(color)
    h.SetLineWidth(2)
    h.Scale(1.0/h.Integral())

    return h

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)

signal_condor_dir = '/data/users/borzari/condor/SignalMC/Run3/2022/checkDRTrackLep'
data_condor_dir = '/data/users/borzari/condor/BGData/Run3/2022/checkDRTrackLep'

data_deltaRTrackElectron = modHist(getHist('hist_merged_DRTrackLep_Electron_2022F',data_condor_dir,'NoCutsPlotter/Track Plots','trackDeltaRToClosestElectron',False),1)
data_deltaRTrackMuon = modHist(getHist('hist_merged_DRTrackLep_Muon_2022F',data_condor_dir,'NoCutsPlotter/Track Plots','trackDeltaRToClosestMuon',False),1)
data_deltaRTrackTau = modHist(getHist('hist_merged_DRTrackLep_Tau_2022F',data_condor_dir,'NoCutsPlotter/Track Plots','trackDeltaRToClosestTau',False),1)

signal_800_10_deltaRTrackElectron = modHist(getHist('isoTrkForDRLepTrack_800_10',signal_condor_dir,'IsoTrkSelectionPlotter/Track Plots','trackDeltaRToClosestElectron',False),2)
signal_800_10_deltaRTrackMuon = modHist(getHist('isoTrkForDRLepTrack_800_10',signal_condor_dir,'IsoTrkSelectionPlotter/Track Plots','trackDeltaRToClosestMuon',False),2)
signal_800_10_deltaRTrackTau = modHist(getHist('isoTrkForDRLepTrack_800_10',signal_condor_dir,'IsoTrkSelectionPlotter/Track Plots','trackDeltaRToClosestTau',False),2)

signal_800_100_deltaRTrackElectron = modHist(getHist('isoTrkForDRLepTrack_800_100',signal_condor_dir,'IsoTrkSelectionPlotter/Track Plots','trackDeltaRToClosestElectron',False),8)
signal_800_100_deltaRTrackMuon = modHist(getHist('isoTrkForDRLepTrack_800_100',signal_condor_dir,'IsoTrkSelectionPlotter/Track Plots','trackDeltaRToClosestMuon',False),8)
signal_800_100_deltaRTrackTau = modHist(getHist('isoTrkForDRLepTrack_800_100',signal_condor_dir,'IsoTrkSelectionPlotter/Track Plots','trackDeltaRToClosestTau',False),8)

signal_800_1000_deltaRTrackElectron = modHist(getHist('isoTrkForDRLepTrack_800_1000',signal_condor_dir,'IsoTrkSelectionPlotter/Track Plots','trackDeltaRToClosestElectron',False),4)
signal_800_1000_deltaRTrackMuon = modHist(getHist('isoTrkForDRLepTrack_800_1000',signal_condor_dir,'IsoTrkSelectionPlotter/Track Plots','trackDeltaRToClosestMuon',False),4)
signal_800_1000_deltaRTrackTau = modHist(getHist('isoTrkForDRLepTrack_800_1000',signal_condor_dir,'IsoTrkSelectionPlotter/Track Plots','trackDeltaRToClosestTau',False),4)

data_deltaRTrackElectron.SetMarkerStyle(20)
data_deltaRTrackElectron.SetMarkerColor(1)

data_deltaRTrackMuon.SetMarkerStyle(20)
data_deltaRTrackMuon.SetMarkerColor(1)

data_deltaRTrackTau.SetMarkerStyle(20)
data_deltaRTrackTau.SetMarkerColor(1)

Legend = TLegend(0.45,0.67,0.7,0.85)
Legend.SetBorderSize(0)
Legend.SetFillColor(0)
Legend.SetFillStyle(0)
Legend.SetTextSize(0.04)
Legend.AddEntry(data_deltaRTrackElectron,"Data","P")
Legend.AddEntry(signal_800_10_deltaRTrackElectron,"c#tau = 10 cm","L")
Legend.AddEntry(signal_800_100_deltaRTrackElectron,"c#tau = 100 cm","L")
Legend.AddEntry(signal_800_1000_deltaRTrackElectron,"c#tau = 1000 cm","L")
Legend.SetHeader("AMSB chargino 800 GeV")

c1 = TCanvas("c1","c1",700,700)

c1.cd()
c1.SetLogy()
data_deltaRTrackElectron.GetXaxis().SetRangeUser(0.0,1.0)
data_deltaRTrackElectron.GetYaxis().SetRangeUser(1e-4,data_deltaRTrackElectron.GetBinContent(data_deltaRTrackElectron.GetMaximumBin())*2.0)
LineElectron = TLine(0.15,1e-4,0.15,data_deltaRTrackElectron.GetBinContent(data_deltaRTrackElectron.GetMaximumBin())*2.0)
LineElectron.SetLineWidth(2)
LineElectron.SetLineStyle(2)
data_deltaRTrackElectron.Draw("P")
signal_800_10_deltaRTrackElectron.Draw("SAME,HIST")
signal_800_100_deltaRTrackElectron.Draw("SAME,HIST")
signal_800_1000_deltaRTrackElectron.Draw("SAME,HIST")
Legend.Draw()
LineElectron.Draw()
c1.Print("deltaRTrackElectron.pdf")

c2 = TCanvas("c2","c2",700,700)

c2.cd()
c2.SetLogy()
data_deltaRTrackMuon.GetXaxis().SetRangeUser(0.0,1.0)
data_deltaRTrackMuon.GetYaxis().SetRangeUser(1e-4,signal_800_1000_deltaRTrackMuon.GetBinContent(signal_800_1000_deltaRTrackMuon.GetMaximumBin())*2.0)
LineMuon = TLine(0.15,1e-4,0.15,signal_800_1000_deltaRTrackMuon.GetBinContent(signal_800_1000_deltaRTrackMuon.GetMaximumBin())*2.0)
LineMuon.SetLineWidth(2)
LineMuon.SetLineStyle(2)
data_deltaRTrackMuon.Draw("P")
signal_800_10_deltaRTrackMuon.Draw("SAME,HIST")
signal_800_100_deltaRTrackMuon.Draw("SAME,HIST")
signal_800_1000_deltaRTrackMuon.Draw("SAME,HIST")
Legend.Draw()
LineMuon.Draw()
c2.Print("deltaRTrackMuon.pdf")

c3 = TCanvas("c3","c3",700,700)

c3.cd()
c3.SetLogy()
data_deltaRTrackTau.GetXaxis().SetRangeUser(0.0,1.0)
data_deltaRTrackTau.GetYaxis().SetRangeUser(1e-4,signal_800_1000_deltaRTrackTau.GetBinContent(signal_800_1000_deltaRTrackTau.GetMaximumBin())*2.0)
LineTau = TLine(0.15,1e-4,0.15,signal_800_1000_deltaRTrackTau.GetBinContent(signal_800_1000_deltaRTrackTau.GetMaximumBin())*2.0)
LineTau.SetLineWidth(2)
LineTau.SetLineStyle(2)
data_deltaRTrackTau.Draw("P")
signal_800_10_deltaRTrackTau.Draw("SAME,HIST")
signal_800_100_deltaRTrackTau.Draw("SAME,HIST")
signal_800_1000_deltaRTrackTau.Draw("SAME,HIST")
Legend.Draw()
LineTau.Draw()
c3.Print("deltaRTrackTau.pdf")
