from array import *
from statistics import mean

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

minValuesElectron = []
minValuesMuon = []
minValuesECAL = []
minValuesAll = []

for mass in range(100,1300,100):
    mass = str(mass)
    for ctau in ['10','100','1000','10000']:
        for nlayers in ['NLayers4','NLayers5','NLayers6plus']:

            cutFlowHist = getHist('AMSB_chargino_'+mass+'GeV_'+ctau+'cm_130X',condor_dir,'disTrkSelectionSmearedJets'+nlayers+'CutFlowPlotter','cutFlow',False)

            for bin in range(1,cutFlowHist.GetNbinsX()):
                if cutFlowHist.GetXaxis().GetLabels().At(bin).GetName() == '>= 1 tracks with isFiducialElectronTrack':
                    print('Mass: ',mass,' -- CTau: ',ctau,' -- NLayers: ',nlayers, ' -- Fiducial Electron: ',cutFlowHist.GetBinContent(bin+1)/cutFlowHist.GetBinContent(bin))
                    minValuesElectron.append(cutFlowHist.GetBinContent(bin+1)/cutFlowHist.GetBinContent(bin))
                if cutFlowHist.GetXaxis().GetLabels().At(bin).GetName() == '>= 1 tracks with isFiducialMuonTrack':
                    print('Mass: ',mass,' -- CTau: ',ctau,' -- NLayers: ',nlayers, ' -- Fiducial Muon: ',cutFlowHist.GetBinContent(bin+1)/cutFlowHist.GetBinContent(bin))
                    minValuesMuon.append(cutFlowHist.GetBinContent(bin+1)/cutFlowHist.GetBinContent(bin))
                if cutFlowHist.GetXaxis().GetLabels().At(bin).GetName() == '>= 1 tracks with isFiducialECALTrack':
                    print('Mass: ',mass,' -- CTau: ',ctau,' -- NLayers: ',nlayers, ' -- Fiducial ECAL: ',cutFlowHist.GetBinContent(bin+1)/cutFlowHist.GetBinContent(bin))
                    minValuesECAL.append(cutFlowHist.GetBinContent(bin+1)/cutFlowHist.GetBinContent(bin))
                    print('Mass: ',mass,' -- CTau: ',ctau,' -- NLayers: ',nlayers, ' -- Fiducial All: ',cutFlowHist.GetBinContent(bin+1)/cutFlowHist.GetBinContent(bin-2))
                    minValuesAll.append(cutFlowHist.GetBinContent(bin+1)/cutFlowHist.GetBinContent(bin-2))

print('The maximum amount of removed events with the fiducial electron map is: ',100.0*(1.0-min(minValuesElectron)))
print('The average amount of removed events with the fiducial electron map is: ',100.0*(1.0-mean(minValuesElectron)))

print('The maximum amount of removed events with the fiducial muon map is: ',100.0*(1.0-min(minValuesMuon)))
print('The average amount of removed events with the fiducial muon map is: ',100.0*(1.0-mean(minValuesMuon)))

print('The maximum amount of removed events with the fiducial ECAL map is: ',100.0*(1.0-min(minValuesECAL)))
print('The average amount of removed events with the fiducial ECAL map is: ',100.0*(1.0-mean(minValuesECAL)))

print('The maximum amount of removed events with all fiducial maps is: ',100.0*(1.0-min(minValuesAll)))
print('The average amount of removed events with all fiducial maps is: ',100.0*(1.0-mean(minValuesAll)))