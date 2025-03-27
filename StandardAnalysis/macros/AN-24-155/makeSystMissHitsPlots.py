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

EGamma_data_condor_dir = '/data/users/borzari/condor/BGData/Run3/2022/EGammaSigSyst'
Muon_data_condor_dir = '/data/users/borzari/condor/BGData/Run3/2022/MuonSigSyst'
mc_condor_dir = '/data/users/borzari/condor/BGMC/Run3/2022/DYSigSyst'

# nLayers = 'NLayers4'
# nLayers = 'NLayers5'
nLayers = 'NLayers6plus'

# missHits = 'Inner'
missHits = 'Middle'

MuonMCMissHitsHist = getHist('hist_merged_DY_ECaloMissHits',mc_condor_dir,'ZtoMuMuTauHitsSystematicSelection' + nLayers + 'Plotter','Track Plots/trackNHitsMissing' + missHits,False)
EGammaMCMissHitsHist = getHist('hist_merged_DY_ECaloMissHits',mc_condor_dir,'ZtoEETauHitsSystematicSelection' + nLayers + 'Plotter','Track Plots/trackNHitsMissing' + missHits,False)

MuonMissHitsHist = getHist('hist_merged_Muon_2022EFG_ECaloMissHits',Muon_data_condor_dir,'ZtoMuMuTauHitsSystematicSelection' + nLayers + 'Plotter','Track Plots/trackNHitsMissing' + missHits,False)
EGammaMissHitsHist = getHist('hist_merged_EGamma_2022EFG_MissHits',EGamma_data_condor_dir,'ZtoEETauHitsSystematicSelection' + nLayers + 'Plotter','Track Plots/trackNHitsMissing' + missHits,False)

MCMissHitsHist = MuonMCMissHitsHist.Clone("MCMissHitsHist")
MCMissHitsHist.Add(EGammaMCMissHitsHist)

DataMissHitsHist = MuonMissHitsHist.Clone("DataMissHitsHist")
DataMissHitsHist.Add(EGammaMissHitsHist)

errorHist_MCMissHitsHist = MCMissHitsHist.Clone("error_MCMissHitsHist")
errorHist_MCMissHitsHist.SetDirectory(0)

errorHist_MCMissHitsHist.Scale((DataMissHitsHist.Integral())/(MCMissHitsHist.Integral()))
MCMissHitsHist.Scale((DataMissHitsHist.Integral())/(MCMissHitsHist.Integral()))

MCMissHitsHist.SetFillColor(colors['DYJetsToLL_M50_2022EE'])
errorHist_MCMissHitsHist.SetFillColor(1)
errorHist_MCMissHitsHist.SetFillStyle(3001)

MCMissHitsHist.SetLineColor(1)
errorHist_MCMissHitsHist.SetLineColor(1)

DataMissHitsHist.SetMarkerStyle(20)
DataMissHitsHist.SetLineColor(1)

Legend_MissHitsHist = TLegend(0.56,0.67,0.86,0.87)
Legend_MissHitsHist.SetBorderSize(0)
Legend_MissHitsHist.SetFillColor(0)
Legend_MissHitsHist.SetFillStyle(0)
Legend_MissHitsHist.SetTextSize(0.03)
Legend_MissHitsHist.SetTextFont(42)
Legend_MissHitsHist.AddEntry(DataMissHitsHist,"EGamma, Muon data","P")
Legend_MissHitsHist.AddEntry(errorHist_MCMissHitsHist,"stat. errors","F")
Legend_MissHitsHist.AddEntry(MCMissHitsHist,labels['DYJetsToLL2022EE'],"F")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.12
iPeriod = 1362

Canvas_MissHitsHist = TCanvas("Canvas_MissHitsHist","Canvas_MissHitsHist",50,50,CMS_lumi.W,CMS_lumi.H)
Canvas_MissHitsHist.SetLeftMargin( CMS_lumi.L/CMS_lumi.W )
Canvas_MissHitsHist.SetRightMargin( CMS_lumi.R/CMS_lumi.W )
Canvas_MissHitsHist.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
Canvas_MissHitsHist.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

Canvas_MissHitsHist.SetLogy()
MCMissHitsHist.SetMinimum(0.5)
MCMissHitsHist.SetMaximum(5e2)
if nLayers == 'NLayers6plus': MCMissHitsHist.SetMaximum(5e3)
MCMissHitsHist.GetYaxis().SetTitle("Entries (Bkgd. scaled to data)")
MCMissHitsHist.SetTitle("")
MCMissHitsHist.Draw("HIST")
DataMissHitsHist.Draw("SAME,P,E")
errorHist_MCMissHitsHist.Draw("SAME,E2")
Legend_MissHitsHist.Draw()

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(Canvas_MissHitsHist, iPeriod, iPos)
Canvas_MissHitsHist.Update()
Canvas_MissHitsHist.Print("tauHitsSyst_" + missHits + "_" + nLayers + "_2022.pdf")
