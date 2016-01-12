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
    
## Nominal selection
candTrkDir            = WellsDir+"candTrkSelection" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/568
disappTrkDir          = WellsDir+"disTrkSelection" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/569

## elecVetoEff.tex and elecEst.tex
elecCtrlDir           = WellsDir+"elecCtrlSelection" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/570

## muonVetoEff.tex and muonEst.tex
muonCtrlDir           = WellsDir+"muonCtrlSelection" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/571

## tauVetoEff.tex and tauEst.tex
tauCtrlDir            = WellsDir+"tauCtrlSelection" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/573 

## fakeTrkRate.tex and fakeEst.tex
ZtoMuMuDir         = WellsDir + "ZtoMuMuSkim"  
ZtoMuMuCandTrkDir  = WellsDir + "ZtoMuMuCandTrk"  
ZtoMuMuDisTrkDir   = WellsDir + "ZtoMuMuDisTrk"  
KinSelDir          = WellsDir + "candTrkSelection"  
    
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

parser.add_option("-a", "--all", action="store_true", dest="all", default=False,
                  help="make all tables")
parser.add_option("-t", "--tableSelection", dest="tableSelection", default="", 
                  help="comma-separated list of which tables to produce") 
parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                  help="verbose output")

(arguments, args) = parser.parse_args()

from ROOT import Double, TMath  


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
    histogram = inputFile.Get(channel+"/"+hist)
    if not histogram:
        print "WARNING: didn't find histogram ", channel + "/" + hist, " in file ", dataset_file  
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

# Return a latex string for a number and its uncertainty
def getLatexNumString(val, err, sigfigs=3):  
    if val != 0: 
        expo = int(math.floor(math.log10(val)))  
    elif err != 0:
        expo = int(math.floor(math.log10(err)))          
    else: 
        expo = 0  
    if val==0:  
        if expo >= 0 and expo <= 3: 
            tex  = "$ " 
            tex += str(round_sigfigs(val, sigfigs)) + " ^{+ " 
            tex += str(round_sigfigs(err, sigfigs)) + "}_{-0} $"
        else: 
            tex  = "$ (" 
            tex += str(round_sigfigs(val * pow(10, -1*expo),sigfigs)) + " ^{+ " 
            tex += str(round_sigfigs(err * pow(10, -1*expo),sigfigs)) + "}_{-0} ) "
            tex += "\\times 10^{" + str(expo) + "} $"   
    else:
        if expo >= 0 and expo <= 5:  
            tex = "$ " + str(round_sigfigs(val, sigfigs)) + " \\pm " + str(round_sigfigs(err, sigfigs)) + " $"  
        else:
            tex  = "$ (" 
            tex += str(round_sigfigs(val * pow(10, -1*expo),sigfigs)) + " \\pm " 
            tex += str(round_sigfigs(err * pow(10, -1*expo),sigfigs)) + ") "
            tex += "\\times 10^{" + str(expo) + "} $"   
    return tex  

def makeLeptonEst(options):
    # Do the calcultion of the lepton background estimate
    # and produce the associated tables. 

    leptonEst = {}  # Dictionary of values to return 

    outputFile = "tables/" + options['type'] + "VetoEff.tex"
    fout = open (outputFile, "w")

    (NCtrl, NCtrlErr)   = getYield(options['MCsample'],  options['ctrlDir'],       options['ctrlChannel'])
    (NYield, NYieldErr) = getYield(options['MCsample'],  options['disTrkDir'],     options['disTrkChannel'])  

    if 'histForYield' in options: 
        (NYield, NYieldErr) = getHistIntegral(options['MCsample'], options['disTrkDir'], options['disTrkChannel'].replace("CutFlow",""), options['histForYield'], options['histForYieldLoBin'], options['histForYieldHiBin'])  
        
    P = NYield / NCtrl
    if P: 
        PErr = P * (NYieldErr / NYield)  
        NYieldStr = getLatexNumString(NYield, NYieldErr) 
    else:
        NYieldRaw = round(math.pow(NYield,2) / math.pow(NYieldErr,2)) if NYieldErr else 0  
        NLimitRaw      =           0.5 * TMath.ChisquareQuantile (0.68, 2 * (NYieldRaw + 1)) # 68% CL upper limit 
        PErr = NLimitRaw / NCtrl
        NYieldStr = getLatexNumString(NYield, NLimitRaw) 

    leptonEst["P"]    = P
    leptonEst["PErr"] = PErr
        
    PStr = getLatexNumString(P, PErr)  
    content  = header 
    content += "\\begin{tabular}{lc}\n"                                                 
    content += hline                                                              
    content += hline                                                              
    content += "$N^" + options['typeStr'] + "_{\\rm ctrl}$ (MC) & $" + str(round_sigfigs(NCtrl,3))  + "$     \\\\ \n"  
    content += "$N^" + options['typeStr'] + "$ (MC)             & " + NYieldStr + " \\\\ \n"  
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
    NlepStr = getLatexNumString(Nlep, NlepErr) 
    leptonEst["NStr"] = NlepStr 

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

    return leptonEst  

def makeBkgdEstimate(options):
    ###################################################
    # Configuration to make background estimate plots  
    # bkgdOptions.py
    ###################################################
    outputFile = options["outputFile"] 
    fout = open (outputFile, "w")

    content  = "# Table produced with makeANTables.py  \n" 
    content += "#!/usr/bin/env python  \n"  
    content += "# ../scripts/bkgdFromData.py -l " + options["outputFile"] + " -w condor_2016_MM_DD_BkgdEstFullSel   \n"
    content += "# mergeOutput.py -q -C -s FakeBkgd -l localConfigBkgdEst.py -w condor_2016_MM_DD_BkgdEstFullSel  # To combine ee and mumu fake track samples (optional) \n"  
    content += "# makePlots.py       -l localConfigBkgdEst.py -w condor_2016_MM_DD_BkgdEstFullSel -o stacked_histograms.root   \n"
    content += "# makePlots.py -P paperPlotsOptions.py      \n" 
    content += "   \n"
    content += "import os   \n"
    content += "   \n"
    content += "cwd = os.getcwd()   \n"
    content += "   \n"
    content += "if 'wulsin' in cwd:   \n"
    content += "    WellsDir = ''     \n"
    content += "    AndrewDir = 'hartCondor/'   \n"
    content += "elif 'hart' in cwd:   \n"
    content += "    WellsDir = 'WellsCondorNew/'   \n"
    content += "    AndrewDir = ''   \n"
    content += "else:   \n"
    content += "    print 'Error: could not identify user as wulsin or hart.'   \n"
    content += "    os.exit(0)   \n"
    content += "       \n"
    content += "impurities = []  # not yet implemented   \n"
    content += "       \n"
    content += "bkgd_sources = {   \n"
    content += "    'MET' :  { 'inputDir'   : '" + options["dataDir"] + "',   \n"
    content += "               'datasetsIn'  : ['" + options["datasetMet"] + "'],   \n"
    content += "               'scale_factor' :       1.0,   \n"
    content += "               'scale_factor_error' : 0.0,   \n"
    content += "               'channel_map' : {   \n"
    content += "    '" + options["fullSelection"] + "' : ['" + options["fullSelection"] + "'],   \n"
    content += "    }   \n"
    content += "               },   \n"
    content += "       \n"
    content += "    'ElecBkgd' :  { 'inputDir'   : '" + options["elecCtrlDir"] + "',   \n"
    content += "                    'datasetsIn'  : ['" + options["datasetMet"] + "'],   \n"
    content += "                    'scale_factor' :        " + str(options["PElec"])    + ",   \n"
    content += "                    'scale_factor_error' :  " + str(options["PElecErr"]) + ",   \n"
    content += "                    'channel_map' : {   \n"
    content += "    '" + options["elecCtrlChannel"] + "' : ['" + options["fullSelection"] + "'],   \n"
    content += "    }   \n"
    content += "                    },   \n"
    content += "       \n"
    content += "    'MuonBkgd' :  { 'inputDir'   : '" + options["muonCtrlDir"] + "',   \n"
    content += "                    'datasetsIn'  : ['" + options["datasetMet"] + "'],   \n"
    content += "                    'scale_factor' :        " + str(options["PMuon"]) + ",   \n"
    content += "                    'scale_factor_error' :  " + str(options["PMuonErr"]) + ",   \n"
    content += "                    'channel_map' : {   \n"
    content += "    '" + options["muonCtrlChannel"] + "' : ['" + options["fullSelection"] + "'],   \n"
    content += "    }   \n"
    content += "                    },   \n"
    content += "       \n"
    content += "    'TauBkgd' :  { 'inputDir'   : '" + options["tauCtrlDir"] + "',   \n"
    content += "                   'datasetsIn'  : ['" + options["datasetMet"] + "'],   \n"
    content += "                   'scale_factor' :        " + str(options["PTau"]) + ",   \n"
    content += "                   'scale_factor_error' :  " + str(options["PTauErr"]) + ",   \n"
    content += "                   'channel_map' : {   \n"
    content += "    '" + options["tauCtrlChannel"] + "' : ['" + options["fullSelection"] + "'],   \n"
    content += "    }   \n"
    content += "                   },   \n"
    content += "       \n"
    content += "       \n"
    content += "       \n"
    content += "    'FakeMuMuBkgd' :  { 'inputDir'   : '" + options["fakeMuMuCtrlDir"] + "',   \n"
    content += "                    'datasetsIn'  : ['" + options["datasetSingleMu"] + "'],   \n"
    content += "                    'scale_factor' :        " + str(options["scaleKin"]) + ",   \n"
    content += "                    'scale_factor_error' :  " + str(options["scaleKinErr"]) + ",   \n"  
    content += "                    'channel_map' : {   \n"
    content += "    '" + options["fakeMuMuCtrlChannel"] + "' : ['" + options["fullSelection"] + "'],   \n"
    content += "    }   \n"
    content += "                    },   \n"
    # EE fake track estimate not yet implemented  
    # content += "    'FakeEEBkgd' :  { 'inputDir'   : JessDir + 'ztoEEFakeTrk3456NHit',   \n"
    # content += "                    'datasetsIn'  : ['SingleElectron'],   \n"
    # content += "                    'scale_factor' :        " + str(ScaleFacFakeTrk5Hits) + ",   \n"
    # content += "                    'scale_factor_error' :  " + str(ScaleFacFakeTrk5HitsErr) + ",   \n"  
    # content += "                    'channel_map' : {   \n"
    # content += "    'ZtoEEFakeTrkNHits5' : ['FullSelection'],   \n"
    # content += "    '" + options["fullSelection"] + "' : ['" + options["fullSelection"] + "'],   \n"
    # content += "    }   \n"
    # content += "                    },   \n"
    content += "       \n"
    content += "       \n"
    content += "    }   \n"
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

if arguments.all or "candTrkBgkdEst" in arguments.tableSelection:  
    ###################################################
    # Electron inefficiency for candidate track bkgd estimate: 
    ###################################################
    options = {}
    options['type'] = "elec"
    options['typeStr'] = "e"  
    options['ctrlDir'] = elecCtrlDir
    options['ctrlChannel'] = "ElecCtrlSelectionCutFlowPlotter"
    options['disTrkDir'] = candTrkDir 
    options['disTrkChannel'] = "CandTrkSelectionCutFlowPlotter" 
    options['ineffScale'] = 3 
    options['dataset'] = "MET_2015D"  
    options['MCsample'] = "WJetsToLNu_HT" 
    elecEstCandTrk = makeLeptonEst(options)  



    ###################################################
    # Muon inefficiency for candidate track bkgd estimate:
    ###################################################
    options = {}
    options['type'] = "muon"
    options['typeStr'] = "\\mu"  
    options['ctrlDir'] = muonCtrlDir
    options['ctrlChannel'] = "MuonCtrlSelectionCutFlowPlotter"
    options['disTrkDir'] = candTrkDir 
    options['disTrkChannel'] = "CandTrkSelectionCutFlowPlotter" 
    options['ineffScale'] = 4 
    options['dataset'] = "MET_2015D"  
    options['MCsample'] = "WJetsToLNu_HT" 
    muonEstCandTrk = makeLeptonEst(options)  



    ###################################################
    # Tau inefficiency for candidate track bkgd estimate:
    ###################################################
    options = {}
    options['type'] = "tau"
    options['typeStr'] = "\\tau"  
    options['ctrlDir'] = tauCtrlDir 
    options['ctrlChannel'] = "TauCtrlSelectionCutFlowPlotter"
    options['disTrkDir'] = candTrkDir 
    options['disTrkChannel'] = "CandTrkSelectionCutFlowPlotter" 
    options['ineffScale'] = 3 
    options['dataset'] = "MET_2015D"  
    options['MCsample'] = "WJetsToLNu_HT" 
    tauEstCandTrk = makeLeptonEst(options)  

if arguments.all or "elecEst" in arguments.tableSelection or "bkgdSumm" in arguments.tableSelection:  
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
    options['dataset'] = "MET_2015D"  
    options['MCsample'] = "WJetsToLNu_HT" 
    options['histForYield'] = "Track Plots/genMatchedPromptFinalStatePdgIdNoHadrons"
    options['histForYieldLoBin'] = 11
    options['histForYieldHiBin'] = 11
    elecEst = makeLeptonEst(options)  


if arguments.all or "muonEst" in arguments.tableSelection or "bkgdSumm" in arguments.tableSelection:  
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
    options['dataset'] = "MET_2015D"  
    options['MCsample'] = "WJetsToLNu_HT" 
    options['histForYield'] = "Track Plots/genMatchedPromptFinalStatePdgIdNoHadrons"
    options['histForYieldLoBin'] = 13
    options['histForYieldHiBin'] = 13
    muonEst = makeLeptonEst(options)  



if arguments.all or "tauEst" in arguments.tableSelection or "bkgdSumm" in arguments.tableSelection:  
    ###################################################
    # Tau inefficiency table:
    # tables/tauVetoEff.tex 
    # tables/tauEst.tex  
    ###################################################
    options = {}
    options['type'] = "tau"
    options['typeStr'] = "\\tau"  
    options['ctrlDir'] = tauCtrlDir 
    options['ctrlChannel'] = "TauCtrlSelectionCutFlowPlotter"
    options['disTrkDir'] = disappTrkDir  
    options['disTrkChannel'] = "DisTrkSelectionCutFlowPlotter" 
    options['ineffScale'] = 3 
    options['dataset'] = "MET_2015D"  
    options['MCsample'] = "WJetsToLNu_HT" 
    options['histForYield'] = "Track Plots/genMatchedPromptFinalStateIsMatched" # FIXME:  should do this better
    options['histForYieldLoBin'] = 0
    options['histForYieldHiBin'] = 0
    # options['histForYield'] = "Track Plots/genMatchedDirectPromptTauDecayProductFinalStateIsMatched"
    # options['histForYieldLoBin'] = 1
    # options['histForYieldHiBin'] = 1
    tauEst = makeLeptonEst(options)  




if arguments.all or "fakeEst" in arguments.tableSelection or "bkgdSumm" in arguments.tableSelection:  
    ###################################################
    # Fake track rate table:
    # tables/fakeTrkRate.tex 
    # tables/fakeEst.tex 
    ###################################################

    fakeEst = {} 

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

    fakeEst["P"]    = P
    fakeEst["PErr"] = PErr

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
    ibin = getBinWithLabel("WJetsToLNu_HT", KinSelDir, "CandTrkSelectionCutFlowPlotter", "neutralEmEnergyFraction") # data cutflow histogram has no labels.  Not sure why.  
    (NCtrlMet, NCtrlMetErr)   = getYieldInBin("MET_2015D", KinSelDir, "CandTrkSelectionCutFlowPlotter", ibin)
    Nfake = NCtrlMet * P
    NfakeErr = NCtrlMet * PErr
    NfakeErrUp = NCtrlMet * PErrUp
    NfakeErrDn = NCtrlMet * PErrDn

    fakeEst["scaleKin"]    = NCtrlMet / NCtrl
    fakeEst["scaleKinErr"] = fakeEst["scaleKin"] * math.sqrt(pow(NCtrlMetErr / NCtrlMet, 2) + pow(NCtrlErr / NCtrl, 2))  # relative error of quotient is sum in quadrature of relative errors of numerator and denominator  
    fakeEst["NStr"] = "$"  + str(round_sigfigs(Nfake,2)) + " ^{+" + str(round_sigfigs(NfakeErrUp,2)) + "}_{-" + str(round_sigfigs(NfakeErrDn,2)) + "} $" 

    content  = header 
    content += "\\begin{tabular}{lc}\n"                                                 
    content += hline                                                              
    content += hline                                                              
    content += "$N^{\\rm fake}_{\\rm ctrl}$ (data) & $"  + str(round_sigfigs(NCtrlMet * 1e-6,3))  +  " \\times 10^{6} $     \\\\ \n"                               
    #content += "$P^{\\rm fake}$ (data)             & $(" + str(round_sigfigs(P * 1e7,2)) + " \\pm " + str(round_sigfigs(PErr * 1e7,2)) + ") \\times 10^{-7} $ \\\\  \n"  
    content += "$P^{\\rm fake}$ (data)             & $(" + str(round_sigfigs(P * 1e7,2)) + " ^{+" + str(round_sigfigs(PErrUp * 1e7,2)) + "}_{-" + str(round_sigfigs(PErrDn * 1e7,2)) + "}) \\times 10^{-7} $ \\\\  \n"  
    content += hline                                                              
    content += "$N^{\\rm fake}$                    & " + fakeEst["NStr"] + " \\\\  \n" 
    #$"  + str(round_sigfigs(Nfake,2)) + " ^{+" + str(round_sigfigs(NfakeErrUp,2)) + "}_{-" + str(round_sigfigs(NfakeErrDn,2)) + "} $ \\\\  \n" 
    content += hline                                                              
    content += hline                                                              
    content += "\\end{tabular}\n"                                                       
    fout.write(content)  
    fout.close() 
    os.system("cat " + outputFile)  
    print "Finished writing " + outputFile + "\n\n\n"

if arguments.all or "bkgdSumm" in arguments.tableSelection:  
    ###################################################
    # Background summary table  
    ###################################################
    content  = header 
    content += "\\begin{tabular}{lc}\n"                                                 
    content += hline                                                              
    content += hline                                                              
    content += "Source  &  Background Prediction (Events) \\\\ \n"  
    content += hline                                                              
    content += "Electrons   & " + elecEst["NStr"] + " \\\\ \n" 
    content += "Muons       & " + muonEst["NStr"] + " \\\\ \n" 
    content += "Taus        & " +  tauEst["NStr"] + " \\\\ \n" 
    content += "Fake tracks & " + fakeEst["NStr"] + " \\\\ \n" 
    content += hline                                                              
    content += hline                                                              
    content += "\\end{tabular}\n"                                                       
    outputFile = "tables/bkgdSumm.tex" 
    fout = open(outputFile, "w")
    fout.write(content)
    fout.close()  
    os.system("cat " + outputFile)  

if arguments.all or "candTrkBkgdEst" in arguments.tableSelection:  
    ###################################################
    # Background estimate plots: candidate track selection  
    ###################################################
    options = {}  
    options["outputFile"]      = "bkgdOptionsCandTrk.py" 
    options["datasetMet"]      = "MET_2015D"  
    options["datasetSingleMu"] = "SingleMu_2015D"  
    options["dataDir"]         = candTrkDir
    options["elecCtrlDir"]     = elecCtrlDir
    options["muonCtrlDir"]     = muonCtrlDir
    options["tauCtrlDir"]      = tauCtrlDir 
    options["fakeMuMuCtrlDir"] = ZtoMuMuCandTrkDir 
    options["fullSelection"]   = "CandTrkSelectionPlotter" 
    options["elecCtrlChannel"] = "ElecCtrlSelectionPlotter" 
    options["muonCtrlChannel"] = "MuonCtrlSelectionPlotter" 
    options["tauCtrlChannel"]  = "TauCtrlSelectionPlotter" 
    options["fakeMuMuCtrlChannel"]  = "ZtoMuMuCandTrkPlotter"   
    options["PElec"]    = elecEstCandTrk["P"] 
    options["PElecErr"] = elecEstCandTrk["PErr"] 
    options["PMuon"]    = muonEstCandTrk["P"] 
    options["PMuonErr"] = muonEstCandTrk["PErr"] 
    options["PTau"]     =  tauEstCandTrk["P"] 
    options["PTauErr"]  =  tauEstCandTrk["PErr"]  
    options["scaleKin"]     = fakeEst["scaleKin"] 
    options["scaleKinErr"]  = fakeEst["scaleKinErr"]  
    makeBkgdEstimate(options)  



##################################################

###################################################
###################################################
###################################################

print "Finished running makeANTables.py"

print "Copy tables to AN area with: "
if user == "wulsin":  
    print "scp tables/*tex wulsin@lxplus.cern.ch:/afs/cern.ch/user/w/wulsin/docs/cmsdocs/notes/AN-15-213/trunk/tables/"
    print "OR: "
    print "notes/AN-15-213/trunk> scp wulsin@cms-in0.mps.ohio-state.edu:\"~/workdir/tables/*tex\" tables/" 
elif user == "hart":  
    print "scp tables/*tex hart@lxplus5.cern.ch:/afs/cern.ch/user/h/hart/myDir/notes/AN-15-213/trunk/tables/"  




