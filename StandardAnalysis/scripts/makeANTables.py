#!/usr/bin/env python3

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
from OSUT3Analysis.Configuration.histogramUtilities import *

sys.path.append(os.path.abspath(os.environ['CMSSW_BASE']+'/src/DisappTrks/StandardAnalysis/test'))
from localConfig import *  # To get list of datasets

os.system("mkdir -p tables/")

cwd = os.getcwd()
if "wulsin" in cwd:
    WellsDir = ""
    AndrewDir = "hartCondor/"
    user = "wulsin"
elif "hart" in cwd:
    WellsDir = "wellsCondor/"
    AndrewDir = ""
    user = "hart"
else:
    print "Error:  could not identify user as wulsin or hart."
    os.exit(0)

## Nominal selection
candTrkDir            = WellsDir+"bkgdCtrlChannelsWithFiducial_76X" # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/644
disappTrkDir          = WellsDir+"disTrkSelection_76X_V2"
candTrkEcaloSdband    = candTrkDir
candTrkNmissoutSdband = candTrkDir

## elecVetoEff.tex and elecEst.tex
elecCtrlDir           = candTrkDir

## muonVetoEff.tex and muonEst.tex
muonCtrlDir           = candTrkDir

## tauVetoEff.tex and tauEst.tex
tauCtrlDir            = candTrkDir

## fakeTrkRate.tex and fakeEst.tex
ZtoMuMuDir                = WellsDir + "ZtoMuMu"
# ZtoMuMuCandTrkDir         = WellsDir + "ZtoMuMuTrkChannels"
ZtoMuMuCandTrkDir         = WellsDir + "ZtoMuMuTrk_76XOld"
ZtoMuMuCandTrkSdband      = ZtoMuMuCandTrkDir
ZtoMuMuDisTrkDir          = ZtoMuMuCandTrkDir
ZtoMuMuDisTrkNHits3456Dir = ZtoMuMuCandTrkDir
BasicSelDir               = WellsDir + "isoTrkSelection_76X"
BasicSelChan              = "IsoTrkSelection"
DisTrkNHits3456Dir        = WellsDir + "fakeTrkSystChannels_76X"

## Bkgd estimates
bkgdEstBase               = WellsDir + "condor_2016_04_20_BkgdEst"
bkgdEstCandTrk            = bkgdEstBase + "CandTrk"
bkgdEstSdbandEcalo        = bkgdEstBase + "SdbandEcalo"
bkgdEstSdbandNmissout     = bkgdEstBase + "SdbandNmissout"

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

from ROOT import gROOT, gStyle, TFile, TH1F, TGraph, TLegend, TCanvas, Double, TMath, TLine

gROOT.SetBatch()
gStyle.SetOptStat(0)

if arguments.localConfig:
    sys.path.append(os.getcwd())
    exec("from " + arguments.localConfig.split(".")[0] + " import *")


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

# Get the probability and error for events to pass the given cut
# Make the calculation based on the total number of events in the sample of interest, NTot
# and the number of events that pass the cut of interest, NPass
def getProb(yields):
    NTot     = yields["NTot"]
    NTotErr  = yields["NTotErr"]
    NPass    = yields["NPass"]
    NPassErr = yields["NPassErr"]

    P    = NPass    / NTot
    PErr = NPassErr / NTot
    PErrUp = -1
    PErrDn = -1
    NLimit68Raw = -1

    # Handle the case in which there are a small number of raw events corresponding to NPass.
    if "NTotRaw" in yields:
        NTotRaw = yields["NTotRaw"]
    else:
        NTotRaw  = getRawEvts(NTot,  NTotErr)
    NPassRaw = getRawEvts(NPass, NPassErr)


    if NPassRaw < 10:  # Crude estimate of when Poisson approximates a binomial, see https://en.wikipedia.org/wiki/Poisson_distribution
        # print "Debug:  NTotRaw = ", NTotRaw
        NPassRawErr = NPassRaw * (NPassErr / NPass) if NPass else 0
        alpha = 0.84  # choose alpha such that 68% of distribution is within +/-1 sigma
        NPassErrUpRaw = math.fabs(0.5 * TMath.ChisquareQuantile (alpha,       2 * (NPassRaw + 1)) - NPassRaw)
        NPassErrDnRaw = math.fabs(0.5 * TMath.ChisquareQuantile (1.0 - alpha, 2 * (NPassRaw ))    - NPassRaw)

        P    =  NPassRaw / NTotRaw
        PErrUp = NPassErrUpRaw / NTotRaw
        PErrDn = NPassErrDnRaw / NTotRaw
        PErr = PErrUp  # Arbitrary choice; usually PErrUp is larger than PErrDn

        # For the case of NPassRaw, use a one-sided 68% confidence interval
        if NPassRaw == 0:
            NLimit68Raw =         0.5 * TMath.ChisquareQuantile (0.68, 2 * (NPassRaw + 1)) # 68% CL upper limit, see https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp
            PErrUp = NLimit68Raw / NTotRaw
            PErrDn = 0
            PErr = PErrUp  # Arbitrary choice; usually PErrUp is larger than PErrDn


    prob = {}
    prob["P"]      = P
    prob["PErr"]   = PErr
    prob["PErrUp"] = PErrUp
    prob["PErrDn"] = PErrDn
    prob["NLimit68Raw"] = NLimit68Raw

    return prob


def makeLeptonEst(options):
    # Do the calcultion of the lepton background estimate
    # and produce the associated tables.

    leptonEst = {}  # Dictionary of values to return

    outputFile = "tables/" + options['type'] + "VetoEff.tex"
    fout = open (outputFile, "w")

    (NCtrl, NCtrlErr) = getYield(options['MCsample'],  options['ctrlDir'],       options['ctrlChannel'])
    (NPass, NPassErr) = getYield(options['MCsample'],  options['disTrkDir'],     options['disTrkChannel'])

    if 'histForYield' in options:
        (NPassHist, NPassHistErr) = getHistIntegral(options['MCsample'], options['disTrkDir'], options['disTrkChannel'].replace("CutFlow",""), options['histForYield'], options['histForYieldLoBin'], options['histForYieldHiBin'])
        if 'histForYieldExclude' in options and options['histForYieldExclude'] == True:
            NPass    -= NPassHist
            NPassErr  = math.sqrt(pow(NPassErr, 2) - pow(NPassHistErr, 2))
        else:
            NPass    = NPassHist
            NPassErr = NPassHistErr
    # print "DEBUG:  For sample", options['MCsample'], "dir=", options['disTrkDir'], " and channel=", options['disTrkChannel'], "NPass=", NPass
    yields = {}
    yields["NTot"] = NCtrl
    yields["NTotErr"] = NCtrlErr
    yields["NPass"] = NPass
    leptonEst["NPass"] = NPass
    yields["NPassErr"] = NPassErr
    prob = getProb(yields)

    P      = prob["P"]
    PErr   = prob["PErr"]
    PErrUp = prob["PErrUp"]
    PErrDn = prob["PErrDn"]

    NTotRaw  = getRawEvts(NCtrl, NCtrlErr)
    NPassRaw = getRawEvts(NPass, NPassErr)
    if P:
        NTotStr  = getLatexNumString(NCtrl, NCtrlErr)
        NPassStr = getLatexNumString(NPass, NPassErr)
    else:
        NTotStr  = getLatexNumString(NTotRaw, math.sqrt(NTotRaw))
        NPassStr = getLatexNumString(NPass, prob["NLimit68Raw"])

    leptonEst["P"]    = P
    leptonEst["PErr"] = PErr

    PStr = getLatexNumString(P, PErr)
    content  = header
    content += "\\begin{tabular}{lc}\n"
    content += hline
    content += hline
    content += "$N^" + options['typeStr'] + "_{\\rm ctrl}$ (MC) & " + NTotStr  + "  \\\\ \n"
    content += "$N^" + options['typeStr'] + "$ (MC)             & " + NPassStr + "  \\\\ \n"
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
    leptonEst["gammaN"] = int(NPassRaw)
    if NPassRaw:
        leptonEst["gammaAlpha"] = Nlep / leptonEst["gammaN"]   # Ensure that NLep = N * alpha
    else:
        leptonEst["gammaAlpha"] = NCtrl / NTotRaw  # ratio of size of data and MC control samples

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

def getFakeRate(options):
    yields = {}
    if options['useTotalYield']:
        (yields["NTot"], yields["NTotErr"])  = getYield(options['dataset'], options['BasicSelDir'], options['BasicSelChannel'])
    else:
        # Find the yield before any track cuts have been applied.
        ibin = getFirstBinWithLabel("WJetsToLNu_HT", options['BasicSelDir'], options['BasicSelChannel'] + "CutFlowPlotter", "tracks with") # data cutflow histogram has no labels.  Not sure why.
        ibin -= 1  # Use the yield before any track cuts.
        (yields["NTot"], yields["NTotErr"]) = getYieldInBin("MET_2015D", BasicSelDir, BasicSelChan + "CutFlowPlotter", ibin)

    (yields["NPass"], yields["NPassErr"]) = getYield(options['dataset'], options['DisTrkNHits3456Dir'], options['DisTrkNHits3456Channel'])

    fakeRate = getProb(yields)

    return fakeRate


def makeBkgdEstimate(options):
    ###################################################
    # Configuration to make background estimate plots
    # bkgdOptions.py
    ###################################################
    outputFile = options["outputFile"]
    fout = open (outputFile, "w")

    content  = "# Table produced with makeANTables.py  \n"
    content += "#!/usr/bin/env python3  \n"
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

if arguments.all or "candTrkBkgdEst" in arguments.tableSelection:
    options = {}
    options['disTrkDir'] = candTrkDir
    options['disTrkChannel'] = "CandTrkSelectionCutFlowPlotter"
    options['dataset'] = "MET_2015D"
    options['MCsample'] = "WJetsToLNu_HT"
    options['histForYield'] = "Track Plots/genMatchedPromptFinalStatePdgIdNoHadrons"
    ###################################################
    # Electron inefficiency for candidate track bkgd estimate:
    ###################################################
    options['type'] = "elec"
    options['typeStr'] = "e"
    options['ctrlDir'] = elecCtrlDir
    options['ctrlChannel'] = "ElecCtrlSelectionCutFlowPlotter"
    options['histForYieldLoBin'] = 11
    options['histForYieldHiBin'] = 12
    elecEstCandTrk = makeLeptonEst(options)

    ###################################################
    # Muon inefficiency for candidate track bkgd estimate:
    ###################################################
    options['type'] = "muon"
    options['typeStr'] = "\\mu"
    options['ctrlDir'] = muonCtrlDir
    options['ctrlChannel'] = "MuonCtrlSelectionCutFlowPlotter"
    options['histForYieldLoBin'] = 13
    options['histForYieldHiBin'] = 14
    muonEstCandTrk = makeLeptonEst(options)

    ###################################################
    # Tau inefficiency for candidate track bkgd estimate:
    ###################################################
    options['type'] = "tau"
    options['typeStr'] = "\\tau"
    options['ctrlDir'] = tauCtrlDir
    options['ctrlChannel'] = "TauCtrlSelectionCutFlowPlotter"
    options['histForYieldExclude'] = True # Include everything except tracks matched to electrons, muons
    options['histForYieldLoBin'] = 11
    options['histForYieldHiBin'] = 14
    tauEstCandTrk = makeLeptonEst(options)

if arguments.all or "sdbandEcaloBkgdEst" in arguments.tableSelection:
    options = {}
    options['disTrkDir'] = candTrkEcaloSdband
    options['disTrkChannel'] = "CandTrkEcaloSdbandCutFlowPlotter"
    options['dataset'] = "MET_2015D"
    options['MCsample'] = "WJetsToLNu_HT"
    options['histForYield'] = "Track Plots/genMatchedPromptFinalStatePdgIdNoHadrons"

    ###################################################
    # Electron inefficiency for Ecalo sideband bkgd estimate:
    ###################################################
    options['type'] = "elec"
    options['typeStr'] = "e"
    options['ctrlDir'] = elecCtrlDir
    options['ctrlChannel'] = "ElecCtrlSelectionCutFlowPlotter"
    options['histForYieldLoBin'] = 11
    options['histForYieldHiBin'] = 12
    elecEstEcaloSdband = makeLeptonEst(options)

    ###################################################
    # Muon inefficiency for Ecalo sideband bkgd estimate:
    ###################################################
    options['type'] = "muon"
    options['typeStr'] = "\\mu"
    options['ctrlDir'] = muonCtrlDir
    options['ctrlChannel'] = "MuonCtrlSelectionCutFlowPlotter"
    options['histForYieldLoBin'] = 13
    options['histForYieldHiBin'] = 14
    muonEstEcaloSdband = makeLeptonEst(options)

    ###################################################
    # Tau inefficiency for Ecalo sideband bkgd estimate:
    ###################################################
    options['type'] = "tau"
    options['typeStr'] = "\\tau"
    options['ctrlDir'] = tauCtrlDir
    options['ctrlChannel'] = "TauCtrlSelectionCutFlowPlotter"
    options['histForYieldExclude'] = True # Include everything except tracks matched to electrons, muons
    options['histForYieldLoBin'] = 11
    options['histForYieldHiBin'] = 14
    tauEstEcaloSdband = makeLeptonEst(options)

if arguments.all or "sdbandNmissoutBkgdEst" in arguments.tableSelection:
    options = {}
    options['disTrkDir'] = candTrkNmissoutSdband
    options['disTrkChannel'] = "CandTrkNMissOutSdbandCutFlowPlotter"
    options['dataset'] = "MET_2015D"
    options['MCsample'] = "WJetsToLNu_HT"
    options['histForYield'] = "Track Plots/genMatchedPromptFinalStatePdgIdNoHadrons"

    ###################################################
    # Electron inefficiency for NMissOut sideband bkgd estimate:
    ###################################################
    options['type'] = "elec"
    options['typeStr'] = "e"
    options['ctrlDir'] = elecCtrlDir
    options['ctrlChannel'] = "ElecCtrlSelectionCutFlowPlotter"
    options['histForYieldLoBin'] = 11
    options['histForYieldHiBin'] = 12
    elecEstNmissoutSdband = makeLeptonEst(options)

    ###################################################
    # Muon inefficiency for NMissOut sideband bkgd estimate:
    ###################################################
    options['type'] = "muon"
    options['typeStr'] = "\\mu"
    options['ctrlDir'] = muonCtrlDir
    options['ctrlChannel'] = "MuonCtrlSelectionCutFlowPlotter"
    options['histForYieldLoBin'] = 13
    options['histForYieldHiBin'] = 14
    muonEstNmissoutSdband = makeLeptonEst(options)

    ###################################################
    # Tau inefficiency for NMissOut sideband bkgd estimate:
    ###################################################
    options['type'] = "tau"
    options['typeStr'] = "\\tau"
    options['ctrlDir'] = tauCtrlDir
    options['ctrlChannel'] = "TauCtrlSelectionCutFlowPlotter"
    options['histForYieldExclude'] = True # Include everything except tracks matched to electrons, muons
    options['histForYieldLoBin'] = 11
    options['histForYieldHiBin'] = 14
    tauEstNmissoutSdband = makeLeptonEst(options)

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
    options['dataset'] = "MET_2015D"
    options['MCsample'] = "TTJets"
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
    options['dataset'] = "MET_2015D"
    options['MCsample'] = "TTJets"    # More stats than WJetsToLNu_HT"
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
    options['dataset'] = "MET_2015D"
    options['MCsample'] = "TTJets"
    options['histForYield'] = "Track Plots/genMatchedPromptFinalStateIsMatched" # FIXME:  should do this better
    options['histForYieldLoBin'] = 0
    options['histForYieldHiBin'] = 0
    # options['histForYield'] = "Track Plots/genMatchedDirectPromptTauDecayProductFinalStateIsMatched"
    # options['histForYieldLoBin'] = 1
    # options['histForYieldHiBin'] = 1
    tauEst = makeLeptonEst(options)




if arguments.all \
   or "fakeEst"        in arguments.tableSelection \
   or "BkgdEst"        in arguments.tableSelection \
   or "bkgdSumm"       in arguments.tableSelection:
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
    NYieldRawErr = NYieldRaw * (NYieldErr / NYield) if NYield else 0
    NLimitRaw      =           0.5 * TMath.ChisquareQuantile (0.68, 2 * (NYieldRaw + 1)) # 68% CL upper limit, see https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp
    alpha = 0.84
    NYieldErrUpRaw = math.fabs(0.5 * TMath.ChisquareQuantile (alpha,       2 * (NYieldRaw + 1)) - NYieldRaw)
    NYieldErrDnRaw = math.fabs(0.5 * TMath.ChisquareQuantile (1.0 - alpha, 2 * (NYieldRaw ))    - NYieldRaw)

    P = NYieldRaw / NCtrl
    if NLimitRaw > NYieldRawErr:
        PErr = NLimitRaw / NCtrl
    else:
        PErr = NYieldRawErr / NCtrl

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
    content += "$P^{\\rm fake} = N^{\\rm fake}_{\\rm ctrl} / N^{\\Z \\rightarrow ll }$ & $ (" + str(round_sigfigs(P * 1e6,2)) + " ^{+" + str(round_sigfigs(PErrUp * 1e6,2)) + "}_{-" + str(round_sigfigs(PErrDn * 1e6,2)) + "}) \\times 10^{-6} $ \\\\  \n"
    content += hline
    content += hline
    content += "\\end{tabular}\n"
    fout.write(content)
    fout.close()
    os.system("cat " + outputFile)
    print "Finished writing " + outputFile + "\n\n\n"


    outputFile = "tables/fakeEst.tex"
    fout = open (outputFile, "w")
    ibin = getFirstBinWithLabel("WJetsToLNu_HT", BasicSelDir, BasicSelChan + "CutFlowPlotter", "tracks with") # data cutflow histogram has no labels.  Not sure why.
    ibin -= 1  # Use the yield before any track cuts.
    (NCtrlMet, NCtrlMetErr)   = getYieldInBin("MET_2015D", BasicSelDir, BasicSelChan + "CutFlowPlotter", ibin)
    Nfake = NCtrlMet * P
    NfakeErr = NCtrlMet * PErr
    NfakeErrUp = NCtrlMet * PErrUp
    NfakeErrDn = NCtrlMet * PErrDn

    fakeEst["scaleKin"]    = NCtrlMet / NCtrl
    fakeEst["scaleKinErr"] = fakeEst["scaleKin"] * math.sqrt(pow(NCtrlMetErr / NCtrlMet, 2) + pow(NCtrlErr / NCtrl, 2)) if NCtrl and NCtrlMet else 0  # relative error of quotient is sum in quadrature of relative errors of numerator and denominator
    fakeEst["NStr"] = "$"  + str(round_sigfigs(Nfake,2)) + " ^{+" + str(round_sigfigs(NfakeErrUp,2)) + "}_{-" + str(round_sigfigs(NfakeErrDn,2)) + "} $"
    fakeEst["gammaN"] = int(NfakeRaw)
    fakeEst["gammaAlpha"] = fakeEst["scaleKin"]

    content  = header
    content += "\\begin{tabular}{lc}\n"
    content += hline
    content += hline
    content += "$N^{\\rm fake}_{\\rm ctrl}$ (data) & $"  + str(round_sigfigs(NCtrlMet * 1e-6,3))  +  " \\times 10^{6} $     \\\\ \n"
    #content += "$P^{\\rm fake}$ (data)             & $(" + str(round_sigfigs(P * 1e7,2)) + " \\pm " + str(round_sigfigs(PErr * 1e7,2)) + ") \\times 10^{-7} $ \\\\  \n"
    content += "$P^{\\rm fake}$ (data)             & $(" + str(round_sigfigs(P * 1e6,2)) + " ^{+" + str(round_sigfigs(PErrUp * 1e6,2)) + "}_{-" + str(round_sigfigs(PErrDn * 1e6,2)) + "}) \\times 10^{-6} $ \\\\  \n"
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


    content = "# Bkgd configuration file for limit-setting produced with makeANTables.py \n"
    content += "#!/usr/bin/env python3  \n"

    content += "backgrounds = {\n"
    content += "'Elec' : {\n"
    content += "    'N' : '"     + str(elecEst["gammaN"])     + "',\n"
    content += "    'alpha' : '" + str(elecEst["gammaAlpha"]) + "',\n"
    content += "        },\n"
    content += "'Muon' : {\n"
    content += "    'N' : '"     + str(muonEst["gammaN"])     + "',\n"
    content += "    'alpha' : '" + str(muonEst["gammaAlpha"]) + "',\n"
    content += "        },\n"
    content += "'Tau' : {\n"
    content += "    'N' : '"     +  str(tauEst["gammaN"])     + "',\n"
    content += "    'alpha' : '" +  str(tauEst["gammaAlpha"]) + "',\n"
    content += "        },\n"
    content += "'Fake' : {\n"
    content += "    'N' : '"     + str(fakeEst["gammaN"])     + "',\n"
    content += "    'alpha' : '" + str(fakeEst["gammaAlpha"]) + "',\n"
    content += "        },\n"
    content += "    }\n"

    # Put in the bkgd systematic uncertainties by hand
    # FIXME:  calculate systematic uncertainties in script!
    content += "background_systematics = { \n"
    content += "    'Elec' : {\n"
    content += "    'value' : '2.5',     # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/637 \n"
    content += "                 },\n"
    content += "    'Muon' : {\n"
    content += "    'value' : '2.5',     # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/635 \n"
    content += "                 },\n"
    content += "    'Tau' : {\n"
    content += "    'value' : '1.71',    # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/621 \n"
    content += "                 },\n"
    content += "    'Fake' : {\n"
    content += "    'value' : '1.22',    # https://cmshead.mps.ohio-state.edu:8080/DisappearingTracks/659 \n"
    content += "                 },\n"
    content += "    }\n"

    outputFile = "amsbLimitConfigBkgds.py"
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
    # print "DEBUG:  Total MC yield = ", elecEstCandTrk["NPass"], muonEstCandTrk["NPass"], tauEstCandTrk["NPass"]


    makeBkgdEstimate(options)

if arguments.all or "sdbandEcaloBkgdEst" in arguments.tableSelection:
    ###################################################
    # Background estimate plots:  Ecalo sideband
    ###################################################
    options = {}
    options["outputFile"]      = "bkgdOptionsSdbandEcalo.py"
    options["datasetMet"]      = "MET_2015D"
    options["datasetSingleMu"] = "SingleMu_2015D"
    options["dataDir"]         = candTrkEcaloSdband
    options["elecCtrlDir"]     = elecCtrlDir
    options["muonCtrlDir"]     = muonCtrlDir
    options["tauCtrlDir"]      = tauCtrlDir
    options["fakeMuMuCtrlDir"] = ZtoMuMuCandTrkSdband
    options["fullSelection"]   = "CandTrkEcaloSdbandPlotter"
    options["elecCtrlChannel"] = "ElecCtrlSelectionPlotter"
    options["muonCtrlChannel"] = "MuonCtrlSelectionPlotter"
    options["tauCtrlChannel"]  = "TauCtrlSelectionPlotter"
    options["fakeMuMuCtrlChannel"]  = "ZtoMuMuCandTrkEcaloSdbandPlotter"
    options["PElec"]    = elecEstEcaloSdband["P"]
    options["PElecErr"] = elecEstEcaloSdband["PErr"]
    options["PMuon"]    = muonEstEcaloSdband["P"]
    options["PMuonErr"] = muonEstEcaloSdband["PErr"]
    options["PTau"]     =  tauEstEcaloSdband["P"]
    options["PTauErr"]  =  tauEstEcaloSdband["PErr"]
    options["scaleKin"]     = fakeEst["scaleKin"]
    options["scaleKinErr"]  = fakeEst["scaleKinErr"]
    makeBkgdEstimate(options)
    # print "DEBUG:  Total MC yield = ", elecEstEcaloSdband["NPass"], muonEstEcaloSdband["NPass"], tauEstEcaloSdband["NPass"]

if arguments.all or "sdbandNmissoutBkgdEst" in arguments.tableSelection:
    ###################################################
    # Background estimate plots:  Ecalo sideband
    ###################################################
    options = {}
    options["outputFile"]      = "bkgdOptionsSdbandNmissout.py"
    options["datasetMet"]      = "MET_2015D"
    options["datasetSingleMu"] = "SingleMu_2015D"
    options["dataDir"]         = candTrkNmissoutSdband
    options["elecCtrlDir"]     = elecCtrlDir
    options["muonCtrlDir"]     = muonCtrlDir
    options["tauCtrlDir"]      = tauCtrlDir
    options["fakeMuMuCtrlDir"] = ZtoMuMuCandTrkSdband
    options["fullSelection"]   = "CandTrkNMissOutSdbandPlotter"
    options["elecCtrlChannel"] = "ElecCtrlSelectionPlotter"
    options["muonCtrlChannel"] = "MuonCtrlSelectionPlotter"
    options["tauCtrlChannel"]  = "TauCtrlSelectionPlotter"
    options["fakeMuMuCtrlChannel"]  = "ZtoMuMuCandTrkNMissOutSdbandPlotter"
    options["PElec"]    = elecEstNmissoutSdband["P"]
    options["PElecErr"] = elecEstNmissoutSdband["PErr"]
    options["PMuon"]    = muonEstNmissoutSdband["P"]
    options["PMuonErr"] = muonEstNmissoutSdband["PErr"]
    options["PTau"]     =  tauEstNmissoutSdband["P"]
    options["PTauErr"]  =  tauEstNmissoutSdband["PErr"]
    options["scaleKin"]     = fakeEst["scaleKin"]
    options["scaleKinErr"]  = fakeEst["scaleKinErr"]
    makeBkgdEstimate(options)
    # print "DEBUG:  Total MC yield = ", elecEstNmissoutSdband["NPass"], muonEstNmissoutSdband["NPass"], tauEstNmissoutSdband["NPass"]

if arguments.all or "bkgdChk" in arguments.tableSelection:
    ###################################################
    # Table of comparison of bkgd estimates vs observations
    # in control regions.
    # This table can only be produced if the bkgd estimates
    # have already been performed!
    ###################################################
    def getOneLine(dirname, label):
        yieldsFile = "condor/" + dirname + "/yields.txt"
        yields = open(yieldsFile, "r")
        yieldObs    = -99
        yieldObsErr = -99
        yieldEst    = -99
        yieldEstErr = -99
        for line in yields.readlines():
            # Form of line is:
            # MET Yield = 129.0 +- 11.3578166916
            # Total bkgd yield = 61.4615057127 +- 6.711
            words = line.split(" ")
            if "MET Yield" in line:
                for i in range(len(words)):
                    if "=" in words[i]:
                        yieldObs    = float(words[i+1])
                        yieldObsErr = float(words[i+3])
            if "Total bkgd yield" in line:
                for i in range(len(words)):
                    if "=" in words[i]:
                        yieldEst    = float(words[i+1])
                        yieldEstErr = float(words[i+3])
        ratio = yieldObs / yieldEst
        ratioErr = ratio * math.sqrt(pow(yieldObsErr/yieldObs, 2) + pow(yieldEstErr/yieldEst, 2))
        lineStr =  ('{0:<30}').format(label)
        lineStr += " &   " + str(int(yieldObs)) + " &  "
        lineStr += " $ " + str(round_sigfigs(yieldEst, 3)) + " \\pm " + str(round_sigfigs(yieldEstErr, 3)) + " $ &  "
        lineStr += " $ " + str(round_sigfigs(ratio, 2))    + " \\pm " + str(round_sigfigs(ratioErr, 2)) + " $ \\\\  \n"
        return lineStr

    outputFile = "tables/bkgdValidate.tex"
    fout = open(outputFile, "w")
    content = header
    content += "\\begin{tabular}{lccc}\n"
    content += hline
    content += hline
    content += "Sample                                  &  Data   &  Estimate  & Data/Estimate  \\\\ \n"
    content += hline
    content += getOneLine(bkgdEstCandTrk,         "Candidate track sample")
    content += getOneLine(bkgdEstSdbandEcalo,     "\\calotot sideband sample")
    content += getOneLine(bkgdEstSdbandNmissout,  "\\Nmissout sideband sample")
    content += hline
    content += hline
    content += "\\end{tabular}\n"
    fout.write(content)
    fout.close()
    os.system("cat " + outputFile)
    print "Finished writing " + outputFile + "\n\n\n"

if arguments.all or "fakeSyst" in arguments.tableSelection:
    ###################################################
    # Fake track rate table:
    # tables/fakeEstSyst.tex
    # tables/fakeEstSyst.py
    ###################################################
    fakeRateCtrl   = {}
    fakeRateSearch = {}
    options = {}
    options['dataset'] = "MET_2015D"

    outputFile = "tables/fakeEstSyst.tex"
    outputPy   = "tables/fakeEstSyst.py"
    fout   = open (outputFile, "w")
    foutPy = open (outputPy,   "w")
    content = header
    content += "\\begin{tabular}{lccc}\n"
    content += hline
    content += hline
    content += "Number of hits on track & Basic Selection & Z $\\rightarrow \\ell \\ell$ control sample \\\\ \n"
    content += hline
    textPy  = "fakeRateCtrl   = {} \n"
    textPy += "fakeRateSearch = {} \n"
    textPy += "ratioSToC      = {} \n"
    hC   = TH1F("hC", ";Number of hits on track;P^{fake}_{Z#rightarrowll}", 4, 2.5, 6.5)
    hS   = TH1F("hS", ";Number of hits on track;P^{fake}_{Basic}",          4, 2.5, 6.5)
    hrat = TH1F("hrat", ";Number of hits on track;P^{fake}_{Basic} / P^{fake}_{Z#rightarrowll}", 4, 2.5, 6.5)
    fakeTrkSystErr = -1
    for n in range(3, 7):   # n is number of hits on candidate track
        options['dataset'] = "SingleMu_2015D"
        options['BasicSelDir']     =  ZtoMuMuDir
        options['BasicSelChannel'] = "ZtoMuMuCutFlowPlotter"
        options['DisTrkNHits3456Dir']     =  ZtoMuMuDisTrkNHits3456Dir
        options['DisTrkNHits3456Channel'] = "ZtoMuMuDisTrkNHits" + str(n) + "CutFlowPlotter"
        options['useTotalYield'] = True
        fakeRateCtrl = getFakeRate(options)
        options['dataset'] = "MET_2015D"
        options['BasicSelDir'] = BasicSelDir
        options['BasicSelChannel']   = BasicSelChan
        options['DisTrkNHits3456Dir'] = DisTrkNHits3456Dir
        options['DisTrkNHits3456Channel'] = "DisTrkSelectionNHits" + str(n) + "CutFlowPlotter"
        options['useTotalYield'] = False
        fakeRateSearch = getFakeRate(options)
        content += str(n) + " & "
        content += getLatexNumString(fakeRateCtrl  ["P"], fakeRateCtrl  ["PErr"]) + " & "
        content += getLatexNumString(fakeRateSearch["P"], fakeRateSearch["PErr"]) + " & "
        ratio = fakeRateSearch["P"] / fakeRateCtrl["P"]
        ratioErr = ratio * math.sqrt(pow(fakeRateCtrl  ["PErr"] / fakeRateCtrl  ["P"], 2) +   \
                                     pow(fakeRateSearch["PErr"] / fakeRateSearch["P"], 2))
        devFromUnity = max(ratio + ratioErr - 1.0, 1.0 - (ratio - ratioErr))
        # print "Debug:  for nhits = ", n, ", fakeRateSearch = ", fakeRateSearch, ", fakeRateCtrl = ", fakeRateCtrl
        print "Deviation from unity for number of hits = ", n, ": ", devFromUnity
        if n == 5:
            fakeTrkSystErr = devFromUnity
        content += getLatexNumString(ratio, ratioErr) + " \\\\ \n"
        textPy += "fakeRateCtrl[" + str(n) + "] = {  \n"
        textPy += "  'P'     : " + str(fakeRateCtrl["P"])      + ",  \n"
        textPy += "  'PErr'  : " + str(fakeRateCtrl["PErr"])   + ",  \n"
        textPy += "  'PErrUp': " + str(fakeRateCtrl["PErrUp"]) + ",  \n"
        textPy += "  'PErrDn': " + str(fakeRateCtrl["PErrDn"]) + ",  \n"
        textPy += "] \n"
        textPy += "fakeRateSearch[" + str(n) + "] = {  \n"
        textPy += "  'P'     : " + str(fakeRateSearch["P"])      + ",  \n"
        textPy += "  'PErr'  : " + str(fakeRateSearch["PErr"])   + ",  \n"
        textPy += "  'PErrUp': " + str(fakeRateSearch["PErrUp"]) + ",  \n"
        textPy += "  'PErrDn': " + str(fakeRateSearch["PErrDn"]) + ",  \n"
        textPy += "] \n"
        textPy += "ratioSToC[" + str(n) + "] = {  \n"
        textPy += "  'ratio'     : " + str(ratio)    + ",  \n"
        textPy += "  'ratioErr'  : " + str(ratioErr) + ",  \n"
        textPy += "] \n"
        ibin = hC.FindBin(n)
        hC  .SetBinContent(ibin, fakeRateCtrl["P"])
        hC  .SetBinError  (ibin, fakeRateCtrl["PErr"])
        hS  .SetBinContent(ibin, fakeRateSearch["P"])
        hS  .SetBinError  (ibin, fakeRateSearch["PErr"])
        hrat.SetBinContent(ibin, ratio)
        hrat.SetBinError  (ibin, ratioErr)


    content += hline
    content += hline
    content += "\\end{tabular}\n"
    fout.write(content)
    fout.close()
    foutPy.write(textPy)
    foutPy.close()
    os.system("cat " + outputFile)
    print "Finished writing " + outputFile + "\n\n\n"

    ##################################################
    # Make associated plots
    ##################################################
    from DisappTrks.StandardAnalysis.tdrstyle import *
    setTDRStyle()
    c = TCanvas()
    c.SetLogy(1)
    hC.SetLineColor(4)
    hC.SetLineWidth(4)
    hC.SetMarkerColor(4)
    hC.SetMarkerStyle(21)
    hC.Draw("pe x0")
    hS.SetLineColor(2)
    hS.SetLineWidth(4)
    hS.SetMarkerColor(2)
    hS.SetMarkerStyle(21)
    hS.Draw("pe x0 same")
    leg = TLegend(0.7, 0.7, 0.9, 0.9)
    leg.AddEntry(hC, "Z#rightarrowll")
    leg.AddEntry(hS, "Basic")
    leg.SetBorderSize(0)
    leg.Draw()
    os.system("mkdir -p plots/")
    c.SaveAs("plots/fakeTrkRate.pdf")
    c.Clear()
    c.SetLogy(0)
    hrat.SetLineColor(1)
    hrat.SetLineWidth(4)
    hrat.SetMarkerColor(1)
    hrat.SetMarkerStyle(21)
    hrat.Draw("pe x0")
    l = TLine()
    l.SetLineColor(2)
    l.DrawLine(2.5,1.0,6.5,1.0)
    c.SaveAs("plots/fakeTrkRatio.pdf")


##################################################

###################################################
###################################################
###################################################

print "Finished running makeANTables.py"

print "Copy tables to AN area with: "
if user == "wulsin":
    print "scp tables/*tex wulsin@lxplus.cern.ch:/afs/cern.ch/user/w/wulsin/docs/cmsdocs/notes/AN-15-213/trunk/tables/"
    print "OR: "
    print "notes/AN-15-213/trunk> scp wulsin@cms-in0.mps.ohio-state.edu:\"~/workdir76/tables/*tex\" tables/"
elif user == "hart":
    print "scp tables/*tex hart@lxplus5.cern.ch:/afs/cern.ch/user/h/hart/myDir/notes/AN-15-213/trunk/tables/"





