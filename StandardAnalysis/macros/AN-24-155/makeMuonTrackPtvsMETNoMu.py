from array import *
import CMS_lumi

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.utilities import *

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad, TLine

def getHist(sample,condor_dir,channel,hist,condorLinked=True):
    dataset_file = ''
    if condorLinked: dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    else: dataset_file = "%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    h0 = inputFile.Get(hist)
    if not h0:
        print("ERROR [getHist]: didn't find histogram ", channel+str("/")+hist, "in file", dataset_file)
        return 0
    h = h0.Clone()
    h.SetDirectory(0)
    inputFile.Close()
    return h

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)
gStyle.SetPalette(112)

SMMC_condor_dir = "/data/users/borzari/condor/BGMC/Run3/2022/muonTrackPtvsMETNoMu"
SigMC_condor_dir = "/data/users/borzari/condor/SignalMC/Run3/2022/muonTrackPtvsMETNoMu"

SMMCHist = getHist('log_right_WToLNu_',SMMC_condor_dir,'','hmet_pt_muon_pt',False)
SigMCHist = getHist('AMSB_700_100',SigMC_condor_dir,'','hmet_pt_muon_pt',False)

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.14
iPeriod = 0

CanvasSMMC = TCanvas("CanvasSMMC","CanvasSMMC",50,50,CMS_lumi.W,CMS_lumi.H)
CanvasSMMC.SetLeftMargin( 0.02 + CMS_lumi.L/CMS_lumi.W )
CanvasSMMC.SetRightMargin( 0.11 + CMS_lumi.R/CMS_lumi.W )
CanvasSMMC.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
CanvasSMMC.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

CanvasSMMC.cd()
CanvasSMMC.SetLogz()
SMMCHist.GetYaxis().SetRangeUser(56,999)
SMMCHist.GetXaxis().SetTitle("E_{T}^{miss, no #mu} [GeV]")
SMMCHist.GetYaxis().SetTitle("muon p_{T} [GeV]")
SMMCHist.SetTitle("")
SMMCHist.SetContour(112)
SMMCHist.Draw("COLZ")

CMS_lumi.CMS_lumi(CanvasSMMC, iPeriod, iPos)
CanvasSMMC.Update()
CanvasSMMC.Print("muonPtVsPFMETNoMu_WJets_2022.pdf")

# Change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Simulation Preliminary"
CMS_lumi.lumi_sqrtS = "13.6 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

# Define position of CMS text and period of lumi to plot
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.13
iPeriod = 0

CanvasSigMC = TCanvas("CanvasSigMC","CanvasSigMC",50,50,CMS_lumi.W,CMS_lumi.H)
CanvasSigMC.SetLeftMargin( 0.02 + CMS_lumi.L/CMS_lumi.W )
CanvasSigMC.SetRightMargin( 0.08 + CMS_lumi.R/CMS_lumi.W )
CanvasSigMC.SetTopMargin( CMS_lumi.T/CMS_lumi.H )
CanvasSigMC.SetBottomMargin( CMS_lumi.B/CMS_lumi.H )

CanvasSigMC.cd()
CanvasSigMC.SetLogz()
SigMCHist.GetYaxis().SetRangeUser(56,999)
SigMCHist.GetXaxis().SetTitle("E_{T}^{miss, no #mu} [GeV]")
SigMCHist.GetYaxis().SetTitle("track p_{T} [GeV]")
SigMCHist.SetTitle("")
SigMCHist.Draw("COLZ")

CMS_lumi.CMS_lumi(CanvasSigMC, iPeriod, iPos)
CanvasSigMC.Update()
CanvasSigMC.Print("trackPtVsPFMETNoMu_signal700GeV1000cm_2022.pdf")