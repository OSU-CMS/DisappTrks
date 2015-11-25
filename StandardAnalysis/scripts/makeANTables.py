#!/usr/bin/env python

# Makes all relevant tables for AN and other analysis documentation.  

# Usage:  
# DisappTrks/StandardAnalysis/test]$ makeANTables.py  

# Run 1 version of this script is available here:
# https://github.com/OSU-CMS/DisappTrks/blob/V01-00-Run1PublishedJHEP/StandardAnalysis/scripts/makeANTables.py  


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
from ROOT import Double, TMath  


sys.path.append(os.path.abspath(os.environ['CMSSW_BASE']+'/src/DisappTrks/StandardAnalysis/test'))  
from localConfig import *  # To get list of datasets 

os.system("mkdir -p tables/")  

cwd = os.getcwd()
if "wulsin" in cwd:
    WellsDir = ""
    AndrewDir = "hartCondor/"
    user = "wulsin"
elif "hart" in cwd:
    WellsDir = "WellsCondor/"    # FIXME:  must set symlink correctly 
    AndrewDir = ""
    user = "hart"  
else:
    print "Error:  could not identify user as wulsin or hart."
    os.exit(0)
    
## elecVetoEff.tex and elecEst.tex
elecCtrlDir             = WellsDir+"elecCtrlSelection" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/532
# fullSelecElecIdDir      = AndrewDir+"fullSelectionElecId" # not yet done 

## muonVetoEff.tex and muonEst.tex
muonCtrlDir           = WellsDir+"MuonCtrlSelection" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/528
disappTrkDir          = WellsDir+"disTrkSelection" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/529

## tauVetoEff.tex and tauEst.tex
tauCtrlDir             = AndrewDir+"tauCtrlSelection" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/499
fullSelecTauIdDir      = AndrewDir+"fullSelectionChannelsForBkgdEstimates"

## fakeTrkRate.tex and fakeEst.tex
ZtoMuMuDir        = WellsDir + "ZtoMuMuSkim"  
ZtoMuMuDisTrkDir  = WellsDir + "ZtoMuMuDisTrk"  
KinSelDir         = WellsDir + "candTrkSelection"  
    
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

parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                  help="verbose output")

(arguments, args) = parser.parse_args()

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.split(".")[0] + " import *")

from ROOT import TFile, TH1F


def getYield(sample,condor_dir,channel):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    cutFlowHistogram = inputFile.Get(channel + "/cutFlow")  
    if not cutFlowHistogram:
        print "WARNING: didn't find cutflow histogram ", channel, "CutFlow in file ", dataset_file  
        return 0
    yield_     = float(cutFlowHistogram.GetBinContent(cutFlowHistogram.GetNbinsX()))
    statError_ = float(cutFlowHistogram.GetBinError  (cutFlowHistogram.GetNbinsX()))
    
    inputFile.Close()
    return (yield_, statError_)  

def getYieldInBin(sample,condor_dir,channel,ibin):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    cutFlowHistogram = inputFile.Get(channel + "/cutFlow")  
    if not cutFlowHistogram:
        print "WARNING: didn't find cutflow histogram ", channel, "CutFlow in file ", dataset_file  
        return 0
    yield_     = float(cutFlowHistogram.GetBinContent(ibin))
    statError_ = float(cutFlowHistogram.GetBinError  (ibin))      
    inputFile.Close()
    return (yield_, statError_)  


def getBinWithLabel(sample,condor_dir,channel,label):
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    cutFlowHistogram = inputFile.Get(channel + "/cutFlow")  
    if not cutFlowHistogram:
        print "WARNING: didn't find cutflow histogram ", channel, "CutFlow in file ", dataset_file  
        return 0
    # Get the appropriate bin
    ibin = -1
    for i in range(1, cutFlowHistogram.GetNbinsX()+1):
        if label in cutFlowHistogram.GetXaxis().GetBinLabel(i):
            ibin = i
    if ibin < 0:
        print "ERROR:  could not find bin with label containing", label, "for channel", channel
    return ibin  

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

def getHistIntegral(sample,condor_dir,channel,hist,xlo,xhi):
    # Modeled on getHistIntegrals.py  
    dataset_file = "condor/%s/%s.root" % (condor_dir,sample)
    inputFile = TFile(dataset_file)
    histogram = inputFile.Get("OSUAnalysis/"+channel+"/"+hist)
    if not histogram:
        print "WARNING: didn't find histogram ", hist, " in file ", dataset_file  
        return 0

    Nxbins = histogram.GetNbinsX()
    xmax = histogram.GetBinContent(Nxbins)
    xloBin = histogram.GetXaxis().FindBin(float(xlo))
    xhiBin = histogram.GetXaxis().FindBin(float(xhi))
    if xhi > xmax:
#        print "xhi is outside the range of the histogram, will include all the overflow instead"
        xhiBin = histogram.GetXaxis().FindBin(float(xhi))
        xlo = histogram.GetXaxis().GetBinLowEdge(xloBin) # lo edge is the left edge of the first bin
    if xhi > xmax:
        xhi = "All to infinity"
    else:
        xhi = histogram.GetXaxis().GetBinLowEdge(xhiBin+1)
    intError = Double (0.0)
    integral = histogram.IntegralAndError(xloBin, xhiBin, intError)
            
    inputFile.Close()
    return (integral, intError)  

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


def makeLeptonEst(options):
    # Do the calcultion of the lepton background estimate
    # and produce the associated tables. 


    outputFile = "tables/" + options['type'] + "VetoEff.tex"
    fout = open (outputFile, "w")

    # Eventually we want this:  
    (NCtrl, NCtrlErr)   = getYield("WJetsToLNu_MiniAOD",  options['ctrlDir'],       options['ctrlChannel'])
    (NYield, NYieldErr) = getYield("WJetsToLNu_MiniAOD",  options['disTrkDir'],     options['disTrkChannel'])  

    P = NYield / NCtrl
    if P: 
        PErr = P * (NYieldErr / NYield)  
    else:
        NYieldRaw = round(math.pow(NYield,2) / math.pow(NYieldErr,2)) if NYieldErr else 0  
        NLimitRaw      =           0.5 * TMath.ChisquareQuantile (0.68, 2 * (NYieldRaw + 1)) # 68% CL upper limit 
        PErr = NLimitRaw / NCtrl

    # string for inefficiency probability:  
    if P==0:
        PStr  = "$ (" 
        PStr += str(round_sigfigs(   P * pow(10, options['ineffScale']),3)) + " ^{+ " 
        PStr += str(round_sigfigs(PErr * pow(10, options['ineffScale']),3)) + "}_{-0} ) "
        PStr += "\\times 10^{-" + str(options['ineffScale']) + "} $"   
    else:
        PStr = "ERROR:  This case not yet defined!"  
        
    content  = header 
    content += "\\begin{tabular}{lc}\n"                                                 
    content += hline                                                              
    content += hline                                                              
    content += "$N^" + options['typeStr'] + "_{\\rm ctrl}$ (MC) & $" + str(round_sigfigs(NCtrl,3))  + "$     \\\\ \n"                               
    content += "$N^" + options['typeStr'] + "$ (MC)             & $" + str(round_sigfigs(NYield,3)) + "$     \\\\ \n"                             
    content += hline                                                              
    content += "$P^" + options['typeStr'] + " = N^" + options['typeStr'] + " / N^" + options['typeStr'] + "_{\\rm ctrl}$ & " + PStr + " \\\\  \n"
    content += hline                                                              
    content += hline                                                              
    content += "\\end{tabular}\n"                                                       
    fout.write(content)  
    fout.close()
    os.system("cat " + outputFile)  
    print "Finished writing " + outputFile + "\n\n\n"

    outputFile = "tables/" + options['type'] + "Est.tex"
    fout = open (outputFile, "w")
    (NCtrl, NCtrlErr)   = getYield(options['dataset'], options['ctrlDir'], options['ctrlChannel'])  # data 
    Nlep = NCtrl * P
    NlepErr = NCtrl * PErr

    if Nlep == 0: 
        NlepStr = "$ " + str(round_sigfigs(Nlep,3)) + " ^{+ " + str(round_sigfigs(NlepErr,3)) + "}_{-0} $" 
    else:
        NlepStr = "ERROR:  This case not yet defined"  

    content  = header 
    content += "\\begin{tabular}{lc}\n"                                                 
    content += hline                                                              
    content += hline                                                              
    content += "$N^" + options['typeStr'] + "_{\\rm ctrl}$ (data)  & $"  + str(round_sigfigs(NCtrl,5)).replace(".0","")  +  "$     \\\\ \n"                               
    content += "$P^" + options['typeStr'] + "$ (MC)               & " + PStr + " \\\\  \n"  
    content += hline                                                              
    content += "$N^" + options['typeStr'] + "$                    & " + NlepStr + " \\\\  \n"
    content += hline                                                              
    content += hline                                                              
    content += "\\end{tabular}\n"                                                       
    fout.write(content)  
    fout.close()
    os.system("cat " + outputFile)  
    print "Finished writing " + outputFile + "\n\n\n"






###################################################
###################################################
###################################################
# End function definitions
###################################################
###################################################
###################################################





hline = "\\hline \n"  
header = "% Table produced with makeANTables.py \n"


###################################################
# Electron inefficiency table:
# tables/elecVetoEff.tex 
# tables/elecEst.tex 
###################################################
options = {}
options['type'] = "elec"
options['typeStr'] = "e"  
options['ctrlDir'] = elecCtrlDir
options['ctrlChannel'] = "ElecCtrlSelectionCutFlowPlotter"
options['disTrkDir'] = disappTrkDir 
options['disTrkChannel'] = "DisTrkSelectionCutFlowPlotter" 
options['ineffScale'] = 3 
options['dataset'] = "MET_2015D_05Oct2015"  
makeLeptonEst(options)  



###################################################
# Muon inefficiency table:
# tables/muonVetoEff.tex 
# tables/muonEst.tex 
###################################################
options = {}
options['type'] = "muon"
options['typeStr'] = "\\mu"  
options['ctrlDir'] = muonCtrlDir
options['ctrlChannel'] = "MuonCtrlSelectionCutFlowPlotter"
options['disTrkDir'] = disappTrkDir 
options['disTrkChannel'] = "DisTrkSelectionCutFlowPlotter" 
options['ineffScale'] = 4 
options['dataset'] = "MET_2015D_05Oct2015"  
makeLeptonEst(options)  



###################################################
# Tau inefficiency table:
# tables/tauVetoEff.tex 
# tables/tauEst.tex  
###################################################
options = {}
options['type'] = "tau"
options['typeStr'] = "\\tau"  
options['ctrlDir'] = tauCtrlDir # Fixme:  specify this.  
options['ctrlChannel'] = "TauCtrlSelectionCutFlowPlotter"
options['disTrkDir'] = disappTrkDir 
options['disTrkChannel'] = "DisTrkSelectionCutFlowPlotter" 
options['ineffScale'] = 3 
options['dataset'] = "MET_2015D_05Oct2015"  
makeLeptonEst(options)  





###################################################
# Fake track rate table:
# tables/fakeTrkRate.tex 
# tables/fakeEst.tex 
###################################################
outputFile = "tables/fakeTrkRate.tex"
fout = open (outputFile, "w")
(NCtrlMuMu, NCtrlErrMuMu)   = getYield("SingleMu_2015D", ZtoMuMuDir,        "ZtoMuMuCutFlowPlotter")
(NYieldMuMu, NYieldErrMuMu) = getYield("SingleMu_2015D", ZtoMuMuDisTrkDir,  "ZtoMuMuDisTrkCutFlowPlotter")

# (NCtrlEE, NCtrlErrEE)   = getYield("SingleElectron", ztoEEDir,        "ZtoEE")
# (NYieldEE, NYieldErrEE) = getYield("SingleElectron", ztoEEFakeTrkDir, "ZtoEEFakeTrk")

# NYield = NYieldMuMu + NYieldEE
# NCtrl = NCtrlEE + NCtrlMuMu
NYield = NYieldMuMu 
NCtrl = NCtrlMuMu

# NYieldErr = math.sqrt(math.pow(NYieldErrEE, 2) + math.pow(NYieldErrMuMu, 2))
# NCtrlErr = math.sqrt(math.pow(NCtrlErrEE, 2) + math.pow(NCtrlErrMuMu, 2))
NYieldErr = NYieldErrMuMu
NCtrlErr = NCtrlErrMuMu

if NYieldErr == 0: 
    NYieldErr = 0.5 * TMath.ChisquareQuantile (0.68, 2 * (NYield + 1)) 


NYieldRaw = round(math.pow(NYield,2) / math.pow(NYieldErr,2)) if NYieldErr else 0  # done for consistency with muon case, but since it's data, there are no weight factors so NYieldRaw = NYield
NfakeRaw = NYieldRaw  # Used for bkgd estimate table  
NYieldErrRaw = NYieldRaw * (NYieldErr / NYield) if NYield else 0
NLimitRaw      =           0.5 * TMath.ChisquareQuantile (0.68, 2 * (NYieldRaw + 1)) # 68% CL upper limit, see https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp
alpha = 0.84
NYieldErrUpRaw = math.fabs(0.5 * TMath.ChisquareQuantile (alpha,       2 * (NYieldRaw + 1)) - NYieldRaw)
NYieldErrDnRaw = math.fabs(0.5 * TMath.ChisquareQuantile (1.0 - alpha, 2 * (NYieldRaw ))    - NYieldRaw)

P = NYieldRaw / NCtrl
if NLimitRaw > NYieldErrRaw:
    PErr = NLimitRaw / NCtrl
else:
    PErr = NYieldErrRaw / NCtrl

PErrUp = NYieldErrUpRaw / NCtrl
PErrDn = NYieldErrDnRaw / NCtrl

if P == 0:
    PErrUp = NLimitRaw / NCtrl


content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^{\\Z \\rightarrow ll}$  & $" + str(round_sigfigs(NCtrl / 1.e6,3)) + " \\times 10^{6}$     \\\\ \n"                               
content += "$N^{\\rm fake}_{\\rm ctrl}$              & $ "+ str(round_sigfigs(NYield,2))     + "$     \\\\ \n"                             
content += hline                                                              
content += "$P^{\\rm fake} = N^{\\rm fake}_{\\rm ctrl} / N^{\\Z \\rightarrow ll }$ & $ (" + str(round_sigfigs(P * 1e7,2)) + " ^{+" + str(round_sigfigs(PErrUp * 1e7,2)) + "}_{-" + str(round_sigfigs(PErrDn * 1e7,2)) + "}) \\times 10^{-7} $ \\\\  \n"  
content += hline                                                           
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close()
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"


outputFile = "tables/fakeEst.tex"
fout = open (outputFile, "w")
ibin = getBinWithLabel("WJetsToLNu_MiniAOD", KinSelDir, "CandTrkSelectionCutFlowPlotter", "neutralEmEnergyFraction") # data cutflow histogram has no labels.  Not sure why.  
(NCtrlMet, NCtrlMetErr)   = getYieldInBin("MET_2015D_05Oct2015", KinSelDir, "CandTrkSelectionCutFlowPlotter", ibin)
Nfake = NCtrlMet * P
NfakeErr = NCtrlMet * PErr
NfakeErrUp = NCtrlMet * PErrUp
NfakeErrDn = NCtrlMet * PErrDn
content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^{\\rm fake}_{\\rm ctrl}$ (data) & $"  + str(round_sigfigs(NCtrlMet * 1e-6,3))  +  " \\times 10^{6} $     \\\\ \n"                               
#content += "$P^{\\rm fake}$ (data)             & $(" + str(round_sigfigs(P * 1e7,2)) + " \\pm " + str(round_sigfigs(PErr * 1e7,2)) + ") \\times 10^{-7} $ \\\\  \n"  
content += "$P^{\\rm fake}$ (data)             & $(" + str(round_sigfigs(P * 1e7,2)) + " ^{+" + str(round_sigfigs(PErrUp * 1e7,2)) + "}_{-" + str(round_sigfigs(PErrDn * 1e7,2)) + "}) \\times 10^{-7} $ \\\\  \n"  
content += hline                                                              
content += "$N^{\\rm fake}$                    & $"  + str(round_sigfigs(Nfake,2)) + " ^{+" + str(round_sigfigs(NfakeErrUp,2)) + "}_{-" + str(round_sigfigs(NfakeErrDn,2)) + "} $ \\\\  \n" 
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close() 
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"




##################################################

###################################################
###################################################
###################################################

print "Finished running makeANTables.py"

print "Copy tables to AN area with: "
if user == "wulsin":  
    print "scp tables/*tex wulsin@lxplus5.cern.ch:/afs/cern.ch/user/w/wulsin/docs/cmsdocs/notes/AN-12-400/trunk/tables/"
    print "OR: "
    print "notes/AN-12-400/trunk> scp wulsin@cms-in0.mps.ohio-state.edu:\"~/workdirTemplateDisTrk/tables/*tex\" tables/" 
elif user == "hart":  
    print "scp tables/*tex hart@lxplus5.cern.ch:/afs/cern.ch/user/h/hart/myDir/notes/AN-12-400/trunk/tables/"




