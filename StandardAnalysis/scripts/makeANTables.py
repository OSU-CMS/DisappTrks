#!/usr/bin/env python

# Makes all relevant tables for AN.  

import sys
import os
import re
import math
from array import *
from decimal import *
from optparse import OptionParser
from OSUT3Analysis.Configuration.configurationOptions import *
from OSUT3Analysis.Configuration.processingUtilities import *
from OSUT3Analysis.Configuration.formattingUtilities import *

from ROOT import Double

### parse the command-line options

parser = OptionParser()
parser = set_commandline_arguments(parser)

parser.remove_option("-o")
parser.remove_option("-n")
parser.remove_option("-u")
parser.remove_option("-e")
parser.remove_option("-r")
parser.remove_option("-R")
parser.remove_option("-d")
parser.remove_option("-b")
parser.remove_option("--2D")
parser.remove_option("-y")
parser.remove_option("-p")
parser.remove_option("-c")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.split(".")[0] + " import *")

from ROOT import TFile, TH1F


def getYield(sample,condor_dir,channel):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    cutFlowHistogram = inputFile.Get("OSUAnalysis/"+channel+"CutFlow")
    if not cutFlowHistogram:
        print "WARNING: didn't find cutflow histogram ", channel, "CutFlow in file ", dataset_file  
        return 0

    yield_     = float(cutFlowHistogram.GetBinContent(cutFlowHistogram.GetNbinsX()))
    statError_ = float(cutFlowHistogram.GetBinError  (cutFlowHistogram.GetNbinsX()))
    
    inputFile.Close()
    return (yield_, statError_)  


def getNumEvents(sample,condor_dir,channel):  # Use in place of getYield if the cutflow histogram is not available 
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    numEvtHistogram = inputFile.Get("OSUAnalysis/"+channel+"/numEvents")
    if not numEvtHistogram:
        print "WARNING: didn't find cutflow histogram ", channel, "CutFlow in file ", dataset_file  
        return 0
    statError_ = Double(0.0)
    yield_ = numEvtHistogram.IntegralAndError(1, numEvtHistogram.GetNbinsX(), statError_)    
    inputFile.Close()
    return (yield_, statError_)  

def getUpperLimit(sample,condor_dir,channel):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    cutFlowHistogram = inputFile.Get("OSUAnalysis/"+channel+"CutFlowUpperLimit")
    if not cutFlowHistogram:
        print "WARNING: didn't find cutflow histogram ", channel, "CutFlow in file ", dataset_file  
        return 0
    limit = float(cutFlowHistogram.GetBinContent(cutFlowHistogram.GetNbinsX()))    
    inputFile.Close()
    return (limit)  

def getTruthYield(sample,condor_dir,channel,truthParticle):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    matchHistogram = inputFile.Get("OSUAnalysis/"+channel+"/trackGenMatchId")
    if not matchHistogram:
        print "WARNING: didn't find match histogram ", channel, "/trackGenMatchId in file ", dataset_file  
        return 0

    idx = -1
    for i in range(1,matchHistogram.GetNbinsX()+1):
        if truthParticle == matchHistogram.GetXaxis().GetBinLabel(i):
            idx = i
    if idx < 0:
        print "Error:  could not find bin with label " + truthParticle
        yield_ = -1
        statError_ = -1
    else:
        yield_     = float(matchHistogram.GetBinContent(idx))
        statError_ = float(matchHistogram.GetBinError  (idx))      
    inputFile.Close()
    return (yield_, statError_)  


###################################################
###################################################
###################################################
# End function definitions
###################################################
###################################################
###################################################





hline = "\\hline \n"  
header = "% Table produced with makeANTables.py \n"
JessDir = "JessCondor/"
WellsDir = ""  


###################################################
# Electron inefficiency table:
# tables/elecVetoEff.tex 
###################################################
outputFile = "tables/elecVetoEff.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("Background", JessDir+"fullSelElecPrevetoSkim",       "FullSelectionElecPreveto")
(NYield, NYieldErr) = getYield("Background", WellsDir+"condor_2014_02_11_FullSelId", "FullSelIdElec")
NLimit              = getUpperLimit("WjetsHighPt", "condor_2014_02_11_FullSelId", "FullSelIdElec")
NYieldErr = math.sqrt(math.pow(NYieldErr,2) + math.pow(NLimit,2))   
P = NYield / NCtrl 
PErr = P * math.sqrt(math.pow(NYieldErr/NYield, 2) + math.pow(NCtrlErr/NCtrl, 2)) 
content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^e_{\\rm ctrl}$  & $" + str(round_sigfigs(NCtrl,5)) + " \\pm " + str(round_sigfigs(NCtrlErr,3)) + "$     \\\\ \n"                               
content += "$N^e$              & $" + str(round_sigfigs(NYield,2))     + " \\pm " + str(round_sigfigs(NYieldErr,2))     + "$     \\\\ \n"                             
content += hline                                                              
content += "$P^e = N^e / N^e_{\\rm ctrl}$ & $(" + str(round_sigfigs(P * 1e5,2)) + " \\pm " + str(round_sigfigs(PErr * 1e5,2)) + ") \\times 10^{-5} $ \\\\  \n"
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close()
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"

(NCtrl, NCtrlErr)   = getYield("MET", JessDir+"fullSelElecPrevetoSkim", "FullSelectionElecPreveto")
Nelec = NCtrl * P
NelecErr = NCtrl * PErr


###################################################
# Muon inefficiency table:
# tables/muonVetoEff.tex 
###################################################
outputFile = "tables/muonVetoEff.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("Background", JessDir+"fullSelMuPrevetoSkim",       "FullSelectionMuPreveto")
(NYield, NYieldErr) = getYield("Background", WellsDir+"condor_2014_02_11_FullSelId", "FullSelIdMuon")
#NLimit              = getUpperLimit("WjetsHighPt", "condor_2014_02_11_FullSelId", "FullSelIdElec")
NYieldErr = math.sqrt(math.pow(NYieldErr,2)) # + math.pow(NLimit,2))   
P = NYield / NCtrl 
PErr = P * math.sqrt(math.pow(NYieldErr/NYield, 2) + math.pow(NCtrlErr/NCtrl, 2)) 
content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^\\mu_{\\rm ctrl}$  & $" + str(round_sigfigs(NCtrl,5)) + " \\pm " + str(round_sigfigs(NCtrlErr,3)) + "$     \\\\ \n"                               
content += "$N^\\mu$              & $" + str(round_sigfigs(NYield,2))     + " \\pm " + str(round_sigfigs(NYieldErr,2))     + "$     \\\\ \n"                             
content += hline                                                              
content += "$P^\\mu = N^\\mu / N^\\mu_{\\rm ctrl}$ & $(" + str(round_sigfigs(P * 1e4,2)) + " \\pm " + str(round_sigfigs(PErr * 1e4,2)) + ") \\times 10^{-4} $ \\\\  \n"
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close()
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"

(NCtrl, NCtrlErr)   = getYield("MET", JessDir+"fullSelMuPrevetoSkim",       "FullSelectionMuPreveto")
Nmuon = NCtrl * P
NmuonErr = NCtrl * PErr


###################################################
# Tau inefficiency table:
# tables/tauVetoEff.tex 
###################################################
outputFile = "tables/tauVetoEff.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("Background", JessDir+"fullSelTauPrevetoSkim",       "FullSelectionTauPreveto")
(NYield, NYieldErr) = getYield("Background", WellsDir+"condor_2014_02_11_FullSelId", "FullSelIdTau")
NLimit              = getUpperLimit("WjetsHighPt", "condor_2014_02_11_FullSelId", "FullSelIdTau")
NYieldErr = math.sqrt(math.pow(NYieldErr,2) + math.pow(NLimit,2))   
P = NYield / NCtrl 
PErr = P * math.sqrt(math.pow(NYieldErr/NYield, 2) + math.pow(NCtrlErr/NCtrl, 2)) 
content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^\\tau_{\\rm ctrl}$  & $" + str(round_sigfigs(NCtrl,3)) + " \\pm " + str(round_sigfigs(NCtrlErr,2)) + "$     \\\\ \n"                               
#content += "$N^\\tau$              & $" + str(round_sigfigs(NYield,2))     + " \\pm " + str(round_sigfigs(NYieldErr,2))     + "$     \\\\ \n"                             
content += "$N^\\tau$              & $" + " \\leq " + str(round_sigfigs(NYieldErr,2))     + "$     \\\\ \n"                             
content += hline                                                              
#content += "$P^\\tau = N^\\tau / N^\\tau_{\\rm ctrl}$ & $(" + str(round_sigfigs(P * 1e5,2)) + " \\pm " + str(round_sigfigs(PErr * 1e5,2)) + ") \\times 10^{-5} $ \\\\  \n"
content += "$P^\\tau = N^\\tau / N^\\tau_{\\rm ctrl}$ & $" + " \\leq " + str(round_sigfigs(PErr,2)) + " $ \\\\  \n"
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close()
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"

(NCtrl, NCtrlErr)   = getYield("MET", JessDir+"fullSelTauPrevetoSkim",       "FullSelectionTauPreveto")
Ntau = NCtrl * P
NtauErr = NCtrl * PErr



###################################################
# Fake track rate table:
# tables/fakeTrkRate.tex 
###################################################
outputFile = "tables/fakeTrkRate.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("SingleMu", WellsDir+"condor_2014_01_10_ZtoMuMu",        "ZtoMuMu")
(NYield, NYieldErr) = getYield("SingleMu", WellsDir+"condor_2014_02_10_ZtoMuMuFakeTrk", "ZtoMuMuFakeTrk")
P = NYield / NCtrl 
PErr = P * math.sqrt(math.pow(NYieldErr/NYield, 2) + math.pow(NCtrlErr/NCtrl, 2)) 
content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^{\\Zmumu}$  & $" + str(round_sigfigs(NCtrl / 1.e6,3)) + " \\times 10^{6}$     \\\\ \n"                               
content += "$N^{\\rm fake}_{\\rm ctrl}$              & $ "+ str(round_sigfigs(NYield,2))     + "$     \\\\ \n"                             
content += hline                                                              
content += "$P^{\\rm fake} = N^{\\rm fake}_{\\rm ctrl} / N^{\\Zmumu}$ & $ (" + str(round_sigfigs(P * 1e7,2)) + " \\pm " + str(round_sigfigs(PErr * 1e7,2)) + ") \\times 10^{-7} $ \\\\  \n"
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close()
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"

(NCtrl, NCtrlErr)   = getYield("MET", WellsDir+"condor_2014_01_25_MetJetSkim", "MetJet")
Nfake = NCtrl * P
NfakeErr = NCtrl * PErr




###################################################
# Electron inefficiency systematic
# tables/elecIneffSyst.tex  
###################################################
outputFile = "tables/elecIneffSyst.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("Background", JessDir+"elecSystSigRegLoosePt_13Feb", "ZtoETrkEIdLoosePtNoVeto") 
(NYield, NYieldErr) = getYield("Background", JessDir+"elecSystSigRegLoosePt_13Feb", "ZtoETrkEIdLoosePt") 
P = NYield / NCtrl / 2.0
PErr = P * math.sqrt(math.pow(NYieldErr/NYield, 2) + math.pow(NCtrlErr/NCtrl, 2))

(NCtrlData, NCtrlErrData)   = getYield("SingleElectron", JessDir+"elecSystSigRegLoosePt_13Feb", "ZtoETrkEIdLoosePtNoVeto") 
(NYieldData, NYieldErrData) = getYield("SingleElectron", JessDir+"elecSystSigRegLoosePt_13Feb", "ZtoETrkEIdLoosePt") 
PData = NYieldData / NCtrlData / 2.0 
PErrData = PData * math.sqrt(math.pow(NYieldErrData/NYieldData, 2) + math.pow(NCtrlErrData/NCtrlData, 2))

ratio = PData / P
ratioErr = ratio * math.sqrt(math.pow(PErrData/PData, 2) + math.pow(PErr/P, 2))
ratio1SigUp = math.fabs(ratio + ratioErr - 1.0)
ratio1SigDn = math.fabs(ratio - ratioErr - 1.0)
systFracElec = max(ratio1SigUp, ratio1SigDn)

content  = header
content += "\\begin{tabular}{lcc} \n"
content += hline
content += hline
content += "& Data & MC \\\\ \n"
content += hline
content += "$N^{e, \\rm{T\\&P}}_{\\rm{ctrl}}$: Total yield  & "
content += "$(" + str(round_sigfigs(NCtrlData / 1.e6,4)) + " \\pm " + str(round_sigfigs(NCtrlErrData / 1.e6,1)) + ") \\times 10^{6}$ & "
content += "$(" + str(round_sigfigs(NCtrl     / 1.e6,4)) + " \\pm " + str(round_sigfigs(NCtrlErr     / 1.e6,1)) + ") \\times 10^{6}$    \\\\ \n"  
content += "$N^{e, \\rm{T\\&P}}$: Probe track passes $e$ veto and \\calotot cut     & "
content += "$" + str(round_sigfigs(NYieldData,3)) + " \\pm " + str(round_sigfigs(NYieldErrData,2)) + "$ & "
content += "$" + str(round_sigfigs(NYield    ,3)) + " \\pm " + str(round_sigfigs(NYieldErr    ,2)) + "$    \\\\ \n"  
content += hline
content += "$P^e = N^{e, \\rm{T\\&P}} / (2 N^{e, \\rm{T\\&P}}_{\\rm{ctrl}})$ & "
content += "$(" + str(round_sigfigs(PData * 1.e5,3)) + " \\pm " + str(round_sigfigs(PErrData * 1.e5,2)) + ") \\times 10^{-5}$ & "
content += "$(" + str(round_sigfigs(P     * 1.e5,3)) + " \\pm " + str(round_sigfigs(PErr     * 1.e5,2)) + ") \\times 10^{-5}$  \\\\ \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% data/MC ratio of fake rates:  " + str(round_sigfigs(ratio,5)) + " \\pm " + str(round_sigfigs(ratioErr,5)) + "\n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"

###################################################
# Muon inefficiency systematic
# tables/muonIneffSyst.tex  
###################################################
outputFile = "tables/muonIneffSyst.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("Background", WellsDir+"condor_2014_02_17_ZtoMuTrkNoVetoLoosePt30", "ZtoMuTrkNoVetoLoosePt") 
(NYield, NYieldErr) = getYield("Background", WellsDir+"condor_2014_02_17_ZtoMuTrkNoVetoLoosePt30", "ZtoMuTrkLoosePt")       

(NCtrlData, NCtrlErrData)   = getYield("SingleMu", WellsDir+"condor_2014_02_17_ZtoMuTrkNoVetoLoosePt30", "ZtoMuTrkNoVetoLoosePt") 
(NYieldData, NYieldErrData) = getYield("SingleMu", WellsDir+"condor_2014_02_17_ZtoMuTrkNoVetoLoosePt30", "ZtoMuTrkLoosePt")       

(NMu, NMuErr) = getTruthYield("Background", WellsDir+"condor_2014_02_17_ZtoMuTrkNoVetoLoosePt30", "ZtoMuTrkLoosePt", "#mu")
NNoMu     = NYield     - NMu
NNoMuErr  = math.sqrt(math.pow(NYieldErr,2) - math.pow(NMuErr,2))  # NMuErr and NNoMuErr are uncorrelated, so NYieldErr^2 = NMuErr^2 + NNoMuErr^2
NMuData    = NYieldData - NNoMu
NMuErrData = math.sqrt(math.pow(NYieldErrData,2) + math.pow(NNoMuErr,2))  # NYieldErrData and NNoMuErr are uncorrelated, so sum in quadrature

P = NMu / NCtrl / 2.0
PErr = P * math.sqrt(math.pow(NMuErr/NMu, 2) + math.pow(NCtrlErr/NCtrl, 2))
PData = NMuData / NCtrlData / 2.0
PErrData = PData * math.sqrt(math.pow(NMuErrData/NMuData, 2) + math.pow(NCtrlErrData/NCtrlData, 2))

ratio = PData / P
ratioErr = ratio * math.sqrt(math.pow(PErrData/PData, 2) + math.pow(PErr/P, 2))
ratio1SigUp = math.fabs(ratio + ratioErr - 1.0)
ratio1SigDn = math.fabs(ratio - ratioErr - 1.0)
systFracMuon = max(ratio1SigUp, ratio1SigDn)

content  = header
content += "\\begin{tabular}{lcc} \n"
content += hline
content += hline
content += "& Data & MC \\\\ \n"
content += hline
content += "$N^{\\mu, \\rm{T\\&P}}_{\\rm{ctrl}}$: Total yield  & "
content += "$" + str(round_sigfigs(NCtrlData,6)) + " \\pm " + str(round_sigfigs(NCtrlErrData,3)) + " $ & "
content += "$" + str(round_sigfigs(NCtrl    ,6)) + " \\pm " + str(round_sigfigs(NCtrlErr    ,3)) + " $    \\\\ \n"  
content += hline
content += "$N^{\\mu, \\rm{T\\&P}}$: Probe track passes $\\mu$ veto     & "
content += "$" + str(round_sigfigs(NYieldData,3)) + " \\pm " + str(round_sigfigs(NYieldErrData,2)) + "$ & "
content += "$" + str(round_sigfigs(NYield    ,3)) + " \\pm " + str(round_sigfigs(NYieldErr    ,2)) + "$    \\\\ \n"  
content += "\\hspace{15pt}non-$\\mu$ yield & " 
content += "$" + str(round_sigfigs(NNoMu,2)) + " \\pm " + str(round_sigfigs(NNoMuErr,2)) + "$ & "
content += "$" + str(round_sigfigs(NNoMu,2)) + " \\pm " + str(round_sigfigs(NNoMuErr,2)) + "$    \\\\ \n"  
content += "\\hspace{15pt}$N^{\\mu, \\rm{T\\&P}}$: $\\mu$ yield & "  
content += "$" + str(round_sigfigs(NMuData,3)) + " \\pm " + str(round_sigfigs(NMuErrData,2)) + "$ & "
content += "$" + str(round_sigfigs(NMu    ,3)) + " \\pm " + str(round_sigfigs(NMuErr    ,2)) + "$    \\\\ \n"  
content += hline
content += "$P^\\mu = N^{\\mu, \\rm{T\\&P}} / (2 N^{\\mu, \\rm{T\\&P}}_{\\rm{ctrl}})$ & "
content += "$(" + str(round_sigfigs(PData * 1.e5,3)) + " \\pm " + str(round_sigfigs(PErrData * 1.e5,2)) + ") \\times 10^{-5}$ & "
content += "$(" + str(round_sigfigs(P     * 1.e5,3)) + " \\pm " + str(round_sigfigs(PErr     * 1.e5,2)) + ") \\times 10^{-5}$  \\\\ \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% data/MC ratio of fake rates:  " + str(round_sigfigs(ratio,5)) + " \\pm " + str(round_sigfigs(ratioErr,5)) + "\n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"



###################################################
# Muon inefficiency systematic
# tables/tauIneffSyst.tex  
###################################################
outputFile = "tables/tauIneffSyst.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("Background", JessDir+"tauSyst6May_v3", "ZtoMuTauHadNoTau") 
(NYield, NYieldErr) = getYield("Background", JessDir+"tauSyst6May_v3", "ZtoMuTauHadNoTrkJetDeltaR")       

(NCtrlData, NCtrlErrData)   = getYield("SingleMu", JessDir+"tauSyst6May_v3", "ZtoMuTauHadNoTau") 
(NYieldData, NYieldErrData) = getYield("SingleMu", JessDir+"tauSyst6May_v3", "ZtoMuTauHadNoTrkJetDeltaR")       

(NTau, NTauErr) = getTruthYield("Background", JessDir+"tauSyst6May_v3", "ZtoMuTauHadNoTrkJetDeltaR", "#tau")
NNoTau     = NYield     - NTau
NNoTauErr  = math.sqrt(math.pow(NYieldErr,2) - math.pow(NTauErr,2))  # NTauErr and NNoTauErr are uncorrelated, so NYieldErr^2 = NTauErr^2 + NNoTauErr^2
NTauData    = NYieldData - NNoTau
NTauErrData = math.sqrt(math.pow(NYieldErrData,2) + math.pow(NNoTauErr,2))  # NYieldErrData and NNoTauErr are uncorrelated, so sum in quadrature

P = NTau / NCtrl 
PErr = P * math.sqrt(math.pow(NTauErr/NTau, 2) + math.pow(NCtrlErr/NCtrl, 2))
PData = NTauData / NCtrlData 
PErrData = PData * math.sqrt(math.pow(NTauErrData/NTauData, 2) + math.pow(NCtrlErrData/NCtrlData, 2))

ratio = PData / P
ratioErr = ratio * math.sqrt(math.pow(PErrData/PData, 2) + math.pow(PErr/P, 2))
ratio1SigUp = math.fabs(ratio + ratioErr - 1.0)
ratio1SigDn = math.fabs(ratio - ratioErr - 1.0)
systFracTau = max(ratio1SigUp, ratio1SigDn)

content  = header
content += "\\begin{tabular}{lcc} \n"
content += hline
content += hline
content += "& Data & MC \\\\ \n"
content += hline
content += "$N^{\\tau, \\rm{T\\&P}}_{\\rm{ctrl}}$: Total yield  & "
content += "$" + str(round_sigfigs(NCtrlData,6)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NCtrlErrData,2)).rstrip("0").rstrip(".") + " $ & "
content += "$" + str(round_sigfigs(NCtrl    ,4)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NCtrlErr    ,3)).rstrip("0").rstrip(".") + " $    \\\\ \n"  
content += hline
content += "$N^{\\tau, \\rm{T\\&P}}$: Probe track passes $\\tau$ veto     & "
content += "$" + str(round_sigfigs(NYieldData,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NYieldErrData,2)).rstrip("0").rstrip(".") + "$ & "
content += "$" + str(round_sigfigs(NYield    ,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NYieldErr    ,2)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
content += "\\hspace{15pt}non-$\\tau$ yield & " 
content += "$" + str(round_sigfigs(NNoTau,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NNoTauErr,2)).rstrip("0").rstrip(".") + "$ & "
content += "$" + str(round_sigfigs(NNoTau,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NNoTauErr,2)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
content += "\\hspace{15pt}$N^{\\tau, \\rm{T\\&P}}$: $\\tau$ yield & "  
content += "$" + str(round_sigfigs(NTauData,4)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NTauErrData,2)).rstrip("0").rstrip(".") + "$ & "
content += "$" + str(round_sigfigs(NTau    ,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NTauErr    ,2)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
content += hline
content += "$P^\\tau = N^{\\tau, \\rm{T\\&P}} / N^{\\tau, \\rm{T\\&P}}_{\\rm{ctrl}}$ & "
content += "$" + str(round_sigfigs(PData,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErrData,2)).rstrip("0").rstrip(".") + " $ & "
content += "$" + str(round_sigfigs(P    ,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErr    ,1)).rstrip("0").rstrip(".") + " $  \\\\ \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% data/MC ratio of fake rates:  " + str(round_sigfigs(ratio,5)) + " \\pm " + str(round_sigfigs(ratioErr,5)) + "\n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"



###################################################
# Fake track rate systematic
# tables/fakeRateSyst.tex  
###################################################
outputFile = "tables/fakeRateSyst.tex"
fout = open (outputFile, "w")

(NCtrl, NCtrlErr)   = getYield("SingleMu", WellsDir+"condor_2014_01_10_ZtoMuMu",              "ZtoMuMu")
(NYield, NYieldErr) = getYield("SingleMu", WellsDir+"condor_2014_02_12_ZtoMuMuFakeTrkNHits4", "ZtoMuMuFakeTrkNHits4")
P = NYield / NCtrl 
PErr = P * math.sqrt(math.pow(NYieldErr/NYield, 2) + math.pow(NCtrlErr/NCtrl, 2))

(NCtrlData, NCtrlErrData)   = getYield("MET", WellsDir+"condor_2014_01_25_MetJetSkim", "MetJet") 
(NYieldData, NYieldErrData) = getYield("MET", WellsDir+"condor_2014_02_12_FullSelectionNHits4", "FullSelectionNHits4") 
PData = NYieldData / NCtrlData 
PErrData = PData * math.sqrt(math.pow(NYieldErrData/NYieldData, 2) + math.pow(NCtrlErrData/NCtrlData, 2))

ratio = PData / P
ratioErr = ratio * math.sqrt(math.pow(PErrData/PData, 2) + math.pow(PErr/P, 2))
ratio1SigUp = math.fabs(ratio + ratioErr - 1.0)
ratio1SigDn = math.fabs(ratio - ratioErr - 1.0)
systFracFake = max(ratio1SigUp, ratio1SigDn)

content  = header
content += "\\begin{tabular}{lcc} \n"
content += hline
content += hline
content += "& \\kinsel  & \\Zmumuctrl   \\\\ \n"
content += hline
content += "$N^{\\rm kin}$ / $N^{\\Zmumu}$  & " 
content += "$" + str(round_sigfigs(NCtrlData / 1.e6,4)).rstrip("0").rstrip(".") + " \\times 10^{6}$ & "          # + " \\pm " + str(round_sigfigs(NCtrlErrData / 1.e6,1))
content += "$" + str(round_sigfigs(NCtrl     / 1.e6,4)).rstrip("0").rstrip(".") + " \\times 10^{6}$    \\\\ \n"  # + " \\pm " + str(round_sigfigs(NCtrlErr     / 1.e6,1))
content += "$N^{\\rm fake}_{\\rm 4 hits}$ & "
content += "$" + str(round_sigfigs(NYieldData,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NYieldErrData,2)).rstrip("0").rstrip(".") + "$ & "
content += "$" + str(round_sigfigs(NYield    ,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NYieldErr    ,2)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
content += hline
content += "$P^{\\rm fake}_{\\rm 4 hits}$  & " 
content += "$(" + str(round_sigfigs(PData * 1.e4,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErrData * 1.e4,2)).rstrip("0").rstrip(".") + ") \\times 10^{-4}$ & "
content += "$(" + str(round_sigfigs(P     * 1.e4,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErr     * 1.e4,1)).rstrip("0").rstrip(".") + ") \\times 10^{-4}$  \\\\ \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% data/MC ratio of fake rates:  " + str(round_sigfigs(ratio,5)) + " \\pm " + str(round_sigfigs(ratioErr,5)) + "\n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"


###################################################
# Systematic summary table 
# tables/systSumm.tex 
###################################################
outputFile = "tables/systSumm.tex" 
fout = open (outputFile, "w")

content  = header
content += "\\begin{tabular}{lccc} \n"
content += hline
content += hline
content += "& Systematic uncertainty \\\\ \n"
content += hline
content += "electron estimate     & " + str(round_sigfigs(systFracElec * 1.e2,2)).rstrip("0").rstrip(".") + "\% \\\\  \n"
content += "muon estimate         & " + str(round_sigfigs(systFracMuon * 1.e2,2)).rstrip("0").rstrip(".") + "\% \\\\  \n"
content += "tau estimate          & " + str(round_sigfigs(systFracTau  * 1.e2,2)).rstrip("0").rstrip(".") + "\% \\\\  \n"
content += "fake track estimate   & " + str(round_sigfigs(systFracFake * 1.e2,2)).rstrip("0").rstrip(".") + "\% \\\\  \n"
content += hline
content += hline
content += "\\end{tabular} \n"
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"



###################################################
# Bkgd summary table 
# tables/bkgdSumm.tex 
###################################################
outputFile = "tables/bkgdSumm.tex" 
fout = open (outputFile, "w")

NelecSyst = Nelec   * systFracElec
NmuonSyst = Nmuon   * systFracMuon
NtauSyst  = NtauErr * systFracTau
NfakeSyst = Nfake   * systFracFake
Ntot = Nelec + Nmuon + Ntau + Nfake
NtotStat = math.sqrt(math.pow(NelecErr,2) + math.pow(NmuonErr,2) + math.pow(NtauErr,2) + math.pow(NfakeErr,2))
NtotSyst = math.sqrt(math.pow(NelecSyst,2) + math.pow(NmuonSyst,2) + math.pow(NtauSyst,2) + math.pow(NfakeSyst,2))

(NData, NDataErr) = getYield("MET", WellsDir+"condor_2014_04_29_FullSelectionUnBlinded", "FullSelection")

# Account for the rounding of Ntau:  
NtauErrRounded = round_sigfigs(NtauErr,2)
Ntau = modifyByPrecision(Ntau, NtauErr, NtauErrRounded)

content  = header
content += "\\begin{tabular}{lccc} \n"
content += hline
content += hline
content += "Event source                                           & Yield                  \\\\ \n"
content += hline
content += "electrons      & $" + str(round_sigfigs(Nelec,2)) + " \\pm " + str(round_sigfigs(NelecErr,2)) + "_{\\rm stat}  \\pm " + str(round_sigfigs(NelecSyst,2)) + "_{\\rm syst} $ \\\\  \n"
content += "muons          & $" + str(round_sigfigs(Nmuon,2)) + " \\pm " + str(round_sigfigs(NmuonErr,2)) + "_{\\rm stat}  \\pm " + str(round_sigfigs(NmuonSyst,2)) + "_{\\rm syst} $ \\\\  \n"
content += "taus           & $" + str(Ntau)                   + " \\pm " + str(round_sigfigs(NtauErr, 2)) + "_{\\rm stat}  \\pm " + str(round_sigfigs(NtauSyst, 2)) + "_{\\rm syst} $ \\\\  \n"
content += "fake tracks    & $" + str(round_sigfigs(Nfake,2)) + " \\pm " + str(round_sigfigs(NfakeErr,2)) + "_{\\rm stat}  \\pm " + str(round_sigfigs(NfakeSyst,2)) + "_{\\rm syst} $ \\\\  \n"
content += hline
content += "background sum & $" + str(round_sigfigs(Ntot, 3)) + " \\pm " + str(round_sigfigs(NtotStat,3)) + "_{\\rm stat}  \\pm " + str(round_sigfigs(NtotSyst,2))  + "_{\\rm syst} $ \\\\  \n"
content += hline
content += "data           & " + str(round_sigfigs(Ntot, 1)).rstrip("0").rstrip(".") + "   \\\\ \n"
content += hline
content += hline
content += "\\end{tabular} \n"
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"



###################################################
# Bkgd estimate validation table 
# tables/bkgdValidate.tex 
###################################################
outputFile = "tables/bkgdValidate.tex" 
fout = open (outputFile, "w")

(NPreselData, NPreselDataErr) = getYield("MET", JessDir+"preselSkim_9Feb", "PreSelection")
(NEcaloData,  NEcaloDataErr)  = getYield("MET", WellsDir+"condor_2014_02_10_BkgdEstPreSelCtrlEcalo", "PreSelCtrlEcalo")
(NNmissData,  NNmissDataErr)  = getYield("MET", WellsDir+"condor_2014_02_10_BkgdEstPreSelCtrlNMiss", "PreSelCtrlNMiss")

(NPreselEst, NPreselEstErr) = getNumEvents("Background", WellsDir+"JessCopy_bkgdFromDataPresel_11Feb", "PreSelection")
(NEcaloEst,  NEcaloEstErr)  = getNumEvents("Background", WellsDir+"condor_2014_02_10_BkgdEstPreSelCtrlEcalo", "PreSelCtrlEcalo")
(NNmissEst,  NNmissEstErr)  = getNumEvents("Background", WellsDir+"condor_2014_02_10_BkgdEstPreSelCtrlNMiss", "PreSelCtrlNMiss")

ratioPresel = NPreselData / NPreselEst
ratioEcalo  = NEcaloData / NEcaloEst
ratioNmiss  = NNmissData / NNmissEst  

ratioPreselErr = ratioPresel * math.sqrt(math.pow(NPreselDataErr/NPreselData, 2) + math.pow(NPreselEstErr/NPreselEst, 2)) 
ratioEcaloErr  = ratioEcalo  * math.sqrt(math.pow(NEcaloDataErr/NEcaloData, 2) + math.pow(NEcaloEstErr/NEcaloEst, 2)) 
ratioNmissErr  = ratioNmiss  * math.sqrt(math.pow(NNmissDataErr/NNmissData, 2) + math.pow(NNmissEstErr/NNmissEst, 2)) 



content  = header
content += "\\begin{tabular}{lccc} \n"
content += hline
content += hline
content += "Sample                                  &  data   &  estimate  & data/estimate  \\\\ \n"  
content += hline
content += "\\candtrk sub-sample       & " + str(NPreselData).rstrip("0").rstrip(".") + " & $" + str(round_sigfigs(NPreselEst,3)) + " \\pm " + str(round_sigfigs(NPreselEstErr,2)) + "$ & $" + str(round_sigfigs(ratioPresel,3)) + " \\pm  " + str(round_sigfigs(ratioPreselErr,2)) + "$ \\\\ \n"
content += "\\calotot sideband sample  & " + str(NEcaloData).rstrip("0").rstrip(".")  + " & $" + str(round_sigfigs(NEcaloEst,4))  + " \\pm " + str(round_sigfigs(NEcaloEstErr,2))  + "$ & $" + str(round_sigfigs(ratioEcalo,3)) + " \\pm  " + str(round_sigfigs(ratioEcaloErr,2)) + "$          \\\\  \n"
content += "\\Nmissout sideband sample & " + str(NNmissData).rstrip("0").rstrip(".")  + " & $" + str(round_sigfigs(NNmissEst,4))  + " \\pm " + str(round_sigfigs(NNmissEstErr,2))  + "$ & $" + str(round_sigfigs(ratioNmiss,3)) + " \\pm  " + str(round_sigfigs(ratioNmissErr,2)) + "$          \\\\  \n"
content += hline
content += hline
content += "\\end{tabular} \\\\  \n"
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"




###################################################
###################################################
###################################################

print "Finished running makeANTables.py"

print "Copy tables to AN area with: "
print "scp tables/*tex wulsin@lxplus5.cern.ch:/afs/cern.ch/user/w/wulsin/docs/cmsdocs/notes/AN-12-400/trunk/tables/" 





