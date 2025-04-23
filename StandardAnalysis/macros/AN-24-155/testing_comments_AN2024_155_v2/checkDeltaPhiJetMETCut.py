from array import *

from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.histogramUtilities import *
from DisappTrks.StandardAnalysis.utilities import *
from DisappTrks.StandardAnalysis.miniAOD_124X_Samples import dataset_names_bkgd

from ROOT import TFile, gROOT, gStyle, TCanvas, TLegend, TPad, TLine

gROOT.SetBatch()
gROOT.ProcessLine( "gErrorIgnoreLevel = 6001;")
gROOT.ProcessLine( "gPrintViaErrorHandler = kTRUE;")
gStyle.SetOptStat(0)

condor_dir = '/data/users/borzari/condor/SignalMC/Run3/2022/signalAcceptance_sigCentralLooseNoMissOut_v2'

minValues = []

for mass in range(100,1300,100):
    mass = str(mass)
    for ctau in ['10','100','1000','10000']:
        for nlayers in ['NLayers4','NLayers5','NLayers6plus']:

            deltaPhiMetJetLeadingHist = getHist('AMSB_chargino_'+mass+'GeV_'+ctau+'cm_130X',condor_dir,'disTrkSelectionSmearedJets'+nlayers+'Plotter','Met-eventvariable Plots/deltaPhiMetJetLeading',False)
            print('Mass: ',mass,' -- CTau: ',ctau,' -- NLayers: ',nlayers, ' -- MinDeltaPhiMetJet: ',deltaPhiMetJetLeadingHist.GetBinCenter(deltaPhiMetJetLeadingHist.FindFirstBinAbove(0.)))

            if deltaPhiMetJetLeadingHist.GetBinCenter(deltaPhiMetJetLeadingHist.FindFirstBinAbove(0.)) > 0.0: minValues.append(deltaPhiMetJetLeadingHist.GetBinCenter(deltaPhiMetJetLeadingHist.FindFirstBinAbove(0.)))


print('The minimum value of deltaPhi(MET,Jet) with more than 0.0 entries is: ',min(minValues))