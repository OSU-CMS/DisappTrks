from array import *
import CMS_lumi

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.miniAOD_124X_Samples import dataset_names_bkgd

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad, TLine

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)

data_condor_dir = '/data/users/borzari/condor/BGData/Run3/2022/MuonSigSyst'
mc_condor_dir = '/data/users/borzari/condor/BGMC/Run3/2022/DYSigSyst'

MCEcaloHist = getHist('hist_merged_DY_ECaloMissHits',mc_condor_dir,'ZtoMuMuDisTrkNLayers4NoECaloCutPlotter','Track Plots/trackCaloJetEnergy',False)
MCEcaloHist.Rebin(8)

DataEcaloHist = getHist('hist_merged_Muon_2022EFG_ECaloMissHits',data_condor_dir,'ZtoMuMuDisTrkNLayers4NoECaloCutPlotter','Track Plots/trackCaloJetEnergy',False)
DataEcaloHist.Rebin(8)

errorHist_MCEcaloHist = MCEcaloHist.Clone("error_MCEcaloHist")
errorHist_MCEcaloHist.SetDirectory(0)

errorHist_MCEcaloHist.Scale((DataEcaloHist.Integral())/(MCEcaloHist.Integral()))
MCEcaloHist.Scale((DataEcaloHist.Integral())/(MCEcaloHist.Integral()))

MCEcaloHist.SetFillColor(colors['DYJetsToLL_M50_2022EE'])
errorHist_MCEcaloHist.SetFillColor(1)
errorHist_MCEcaloHist.SetFillStyle(3001)

MCEcaloHist.SetLineColor(1)
errorHist_MCEcaloHist.SetLineColor(1)

DataEcaloHist.SetMarkerStyle(20)
DataEcaloHist.SetLineColor(1)

Legend_EcaloHist = TLegend(0.66,0.67,0.96,0.87)
Legend_EcaloHist.SetBorderSize(0)
Legend_EcaloHist.SetFillColor(0)
Legend_EcaloHist.SetFillStyle(0)
Legend_EcaloHist.SetTextSize(0.03)
Legend_EcaloHist.SetTextFont(42)
Legend_EcaloHist.AddEntry(DataEcaloHist,"2022EFG data","P")
Legend_EcaloHist.AddEntry(errorHist_MCEcaloHist,"stat. errors","F")
Legend_EcaloHist.AddEntry(MCEcaloHist,labels['DYJetsToLL2022EE'],"F")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 1362

Canvas_EcaloHist = TCanvas("Canvas_EcaloHist","Canvas_EcaloHist",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas_EcaloHist.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas_EcaloHist.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas_EcaloHist.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas_EcaloHist.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas_EcaloHist.SetLogy()
MCEcaloHist.SetMinimum(0.5)
MCEcaloHist.SetMaximum(1e4)
MCEcaloHist.GetXaxis().SetTitle("E_{calo} [GeV]")
MCEcaloHist.GetYaxis().SetTitle("Entries / 8.0 GeV (Bkgd. scaled to data)")
MCEcaloHist.SetTitle("")
MCEcaloHist.Draw("HIST")
DataEcaloHist.Draw("SAME,P,E")
errorHist_MCEcaloHist.Draw("SAME,E2")
Legend_EcaloHist.Draw()

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(Canvas_EcaloHist, iPeriod, iPos)
Canvas_EcaloHist.Update()
Canvas_EcaloHist.Print("fakeTrackECalo_2022.pdf")
