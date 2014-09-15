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
from ROOT import Double, TMath  


sys.path.append(os.path.abspath(os.environ['CMSSW_BASE']+'/src/DisappTrks/StandardAnalysis/test'))  
from localOptionsBkgd import *  # To get list of datasets 
from amsbLimitConfigNew import *

#from DisappTrks.StandardAnalysis.localOptionsAll import *  # To get list of datasets 


cwd = os.getcwd()
if "wulsin" in cwd:
    WellsDir = ""
    JessDir = "JessCondor/"
elif "jbrinson" in cwd:
    WellsDir = "WellsCondorNew/"
    JessDir = ""
else:
    print "Error:  could not identify user as wulsin or jbrinson."
    os.exit(0)
    
## elecVetoEff.tex and elecEst.tex
preselElecDir           = JessDir+"preselSkim_9Feb"
fullSelecElecIdDir      = JessDir+"fullSelectionChannelsForBkgdEstimates"
fullSelecElecPrevetoDir = JessDir+"fullSelectionChannelsForBkgdEstimates"

## muonVetoEff.tex and muonEst.tex
preselMuDir           = JessDir+"preselSkim_9Feb"
fullSelecMuIdDir      = JessDir+"fullSelectionChannelsForBkgdEstimates"
fullSelecMuPrevetoDir = JessDir+"fullSelectionChannelsForBkgdEstimates"

## tauVetoEff.tex and tauEst.tex

preselTauDir           = JessDir+"preselSkim_9Feb"
fullSelecTauIdDir      = JessDir+"fullSelectionChannelsForBkgdEstimates"
fullSelecTauPrevetoDir = JessDir+"fullSelectionChannelsForBkgdEstimates"

## fakeTrkRate.tex and fakeEst.tex

ztoMuMuDir        = WellsDir+"condor_2014_01_10_ZtoMuMu"
ztoMuMuFakeTrkDir = JessDir+"ztoMuMuFakeTrk_24June"

ztoEEDir          = JessDir+"ZtoEESkim"
ztoEEFakeTrkDir   = JessDir+"ztoEEFakeTrk3456NHit"

metJetDir         = WellsDir+"condor_2014_01_25_MetJetSkim"

## elecIneffSyst.tex
elecSystDir = JessDir+"elecSystSigRegLoosePt_13Feb"

## muonIneffSyst.tex
muSystDir = JessDir+"muSyst_30June"

## tauIneffSyst.tex
tauSystDir = JessDir+"tauSyst_30June"

## fakeRateSyst.tex
fakeMuMuSystDir        = WellsDir+"condor_2014_01_10_ZtoMuMu"
fakeMuMu5HitsSystDir   = WellsDir+"condor_2014_05_24_ZtoMuMuFakeTrkNHits356"

fakeEESystDir          = JessDir+"ZtoEESkim"
fakeEE5HitsSystDir     = JessDir+"ztoEEFakeTrk3456NHit"

fakeSearchSystDir      = WellsDir+"condor_2014_01_25_MetJetSkim"
fakeSearch5HitsSystDir = WellsDir+"condor_2014_05_22_FullSelectionNHits356"

## systNmissIn.tex
systNMissInDir = WellsDir+"condor_2014_06_02_PreSelectionMuonNoMissInMid"

## systNmissMid.tex
systNMissMidDir = WellsDir+"condor_2014_06_02_PreSelectionMuonNoMissInMid"

## systEcalo.tex
systEcaloDir  = JessDir+"ztoMuMuFakeTrkNHits4NoEcalo"  

## bkgdSumm.tex
fullSelectionDir = JessDir+"fullSelectionSkim_24June"

## bkgdValidate.tex
preselDir             = JessDir+"preselSkim_9Feb"
ctrlEcaloDir          = WellsDir+"condor_2014_02_10_BkgdEstPreSelCtrlEcalo"
ctrlNMissDir          = WellsDir+"condor_2014_02_10_BkgdEstPreSelCtrlNMiss"
bkgdFromDataPreselDir = WellsDir+"JessCopy_bkgdFromDataPresel_11Feb"

## trackGenMatchBkgd.tex
preselIdDir = JessDir+"preselId_11Feb"

## for header file for ZtoLL fake trk rate ratio plot
fullSelection3HitsDir = WellsDir+"condor_2014_05_22_FullSelectionNHits356"
fullSelection4HitsDir = WellsDir+"condor_2014_02_12_FullSelectionNHits4"
fullSelection5HitsDir = WellsDir+"condor_2014_05_22_FullSelectionNHits356"
fullSelection6HitsDir = WellsDir+"condor_2014_05_22_FullSelectionNHits356"

ztoMuMu3HitsDir       = WellsDir+"condor_2014_05_24_ZtoMuMuFakeTrkNHits356"
ztoMuMu4HitsDir       = WellsDir+"condor_2014_02_12_ZtoMuMuFakeTrkNHits4"
ztoMuMu5HitsDir       = WellsDir+"condor_2014_05_24_ZtoMuMuFakeTrkNHits356"
ztoMuMu6HitsDir       = WellsDir+"condor_2014_05_24_ZtoMuMuFakeTrkNHits356"

ztoEE3HitsDir         = JessDir+"ztoEEFakeTrk3456NHit"
ztoEE4HitsDir         = JessDir+"ztoEEFakeTrk3456NHit"
ztoEE5HitsDir         = JessDir+"ztoEEFakeTrk3456NHit"
ztoEE6HitsDir         = JessDir+"ztoEEFakeTrk3456NHit"

## test systematic
    
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
# Signal Systematics table:
# tables/sigSyst.tex
###################################################  
outputFile = "tables/sigSyst.tex"
fout = open (outputFile, "w")

content  = header
content += "\\begin{tabular}{lc}\n"
content += hline
content += hline

systTableLines = {}   # Dictionary to hold all the lines for the systematics table

systTotPerSample = {}
tempNameHolder = []
tempSystHolder = []
systTotPerSample['name'] = []
systTotPerSample['value'] = []

## cTauMin = 20
## cTauMax = 900
massMin = 300
massMax = 600

lifetimes = ['10', '20','30','40','50','60','70','80','90','100','200','300','400','500','600','700','800','900', '1000']
masses = ['100','200', '300', '400', '500', '600']

for systematic in external_systematic_uncertainties:
    systFile = os.environ['CMSSW_BASE']+"/src/DisappTrks/StandardAnalysis/data/systematic_values__" + systematic + ".txt"
    fSyst = open (systFile, "r")
    systRange = []
    lifetimeRangeTot = []
    massRangeTot = []
    for line in fSyst:
        for cTau in lifetimes:
            for mass in masses: 
                string = "AMSB_chargino_" + str(mass) + "GeV_RewtCtau" + str(cTau) + "cm"
                if string in line:
                    word = float(line.strip().split()[2])
                    percent = math.fabs((1.0 - word))*100
                    if mass == "100" and float(cTau) > 100 and float(cTau) < 10000 and systematic == 'NMissOut':  # skip outlier 
                        continue
                    if mass == "600" and float(cTau) <= 10  and systematic == 'PDFWt':  # skip outlier
                        continue                    
                    systRange.append(round(percent,2))
                    lifetimeRangeTot.append(cTau)
                    massRangeTot.append(mass)
                    systHolder = round(percent,2)
## set range to be quoted
    idxMax = systRange.index(max(systRange))
    if arguments.verbose:
        print "Index of largest syst of type ", systematic, ":  ", idxMax
        print "lifetime of largest syst:  ", lifetimeRangeTot[idxMax], ", mass = ", massRangeTot[idxMax]                        
                    
    systRange.sort()  
    largest = max(systRange)
    if largest > 50:
        largestTot = 0
    else:
        largestTot = largest
    smallest = min (systRange)

    idx5  = int(0.05 * len(systRange))
    idx95 = int(0.95 * len(systRange))
    smallest90 = systRange[idx5]
    largest90  = systRange[idx95]
    if arguments.verbose:
        print "Debug:  for systematic:  ", systematic, ", full range is: ", smallest, " - ", largest, ", 5% - 95% range is: ", smallest90, " - ", largest90, " num points sampled: ", len(systRange)  
        print systRange
    
## put in format to be used by AN
    if str(systematic) == "Isr":
        fancyString = str(systematic).replace("Isr", "jet radiation (ISR)")
    elif str(systematic) == "JES":
        fancyString = str(systematic).replace("JES", "%jet Energy Scale (JES)")         
    elif str(systematic) == "JER":
        fancyString = str(systematic).replace("JER", "%jet Energy Resolution (JER)")
    elif str(systematic) == "PDFWt":
        fancyString = str(systematic).replace("PDFWt", "PDF")
    elif str(systematic) == "trigEff":
        fancyString = str(systematic).replace("trigEff", "trigger efficiency")
    elif str(systematic) == "Ecalo":
        fancyString = str(systematic).replace("Ecalo", "\calotot modeling")
    elif str(systematic) == "NMissOut":
        fancyString = str(systematic).replace("NMissOut", "\Nmissout modeling")
    elif str(systematic) == "Nmissmid":
        fancyString = str(systematic).replace("Nmissmid", "\Nmissmid modeling")
    elif str(systematic) == "Nmissin":
        fancyString = str(systematic).replace("Nmissin", "\Nmissin modeling")
    elif str(systematic) == "pileup":
        fancyString = str(systematic).replace("pileup", "pileup")
    else:
        print "Error:  unrecognized systematic:  ", systematic
        sys.exit(0)        
    systTableLines[systematic] = '{0: <35}'.format(fancyString) + " & " + "{:.0f}".format(smallest) + "--" + "{:.0f}".format(largestTot) + "\\% \\\\ \n"
    

## retrieve systematics that are a single value for all signal samples
for systematic in signal_systematic_uncertainties:
    if str(systematic) == "lumi":
        fancyString = str(systematic).replace("lumi", "%lumi")
    if str(systematic) == "Nmissin":
        fancyString = str(systematic).replace("Nmissin", "\Nmissin modeling")
    if str(systematic) == "Nmissmid":
        fancyString = str(systematic).replace("Nmissmid", "\Nmissmid modeling")
    if str(systematic) == "Ecalo":
        fancyString = str(systematic).replace("Ecalo", "\calotot modeling")
    if str(systematic) == "trkReco":
        fancyString = str(systematic).replace("trkReco", "track reconstruction efficiency")
    systTableLines[systematic] = '{0: <35}'.format(fancyString) + " & " + "{:.0f}".format((float(signal_systematic_uncertainties[systematic]['value'])-1)*100) + "\\% \\\\ \n"

# Make line for Nmissin, Nmissmid:
systNmissin  = systTableLines["Nmissin"] .split()[3].replace("\\%","")
systNmissmid = systTableLines["Nmissmid"].split()[3].replace("\\%","")
systTableLines["Nmissinmid"] = '{0: <35}'.format("\Nmissin, \Nmissmid modeling") + " & " + systNmissmid + "--" + systNmissin + "\\% \\\\ \n"

    
## calculate the total 
systRangeTot = []
JESJERRangeTot = []
lifetimeRangeTot = []
for cTau in lifetimes:
    for mass in masses: 
        systRangePerSample = []
        JESJERRangePerSample = []
        for systematic in external_systematic_uncertainties:
            systFile = os.environ['CMSSW_BASE']+"/src/DisappTrks/StandardAnalysis/data/systematic_values__" + systematic + ".txt"
            fSyst = open (systFile, "r")
            for line in fSyst:
                string = "AMSB_chargino_" + str(mass) + "GeV_RewtCtau" + str(cTau) + "cm"
                if string in line:
                    word = float(line.strip().split()[2])
                    percent = math.fabs((1.0 - word))*100
                    systRangePerSample.append(round(percent,2))
                    if str(systematic) == "JES" or str(systematic) == "JER":
                        JESJERRangePerSample.append(round(percent,2))
        for systematic in signal_systematic_uncertainties:
            systRangePerSample.append(float(signal_systematic_uncertainties[systematic]['value']))
        #print string
##         print "systRangePerSample, mass=", mass, ", cTau=", cTau, ":  "  
##         print systRangePerSample
        total = 0
        totalJESJER = 0 
        for syst in systRangePerSample:
            total+= math.pow(syst,2)
        for syst in JESJERRangePerSample:
            totalJESJER += math.pow(syst,2)
        JESJERRangeTot.append(math.sqrt(totalJESJER))
        systRangeTot.append(math.sqrt(total))
        lifetimeRangeTot.append(cTau)  
## print "SystRangeTot: " 
## print systRangeTot
largestTot  = max(systRangeTot)
smallestTot = min(systRangeTot)
largestJESJER  = max(JESJERRangeTot)
smallestJESJER = min(JESJERRangeTot)
if arguments.verbose:                                                                                                                      
    # idxMax = systRangeTot.index(max(systRangeTot))
    idxMax = JESJERRangeTot.index(max(JESJERRangeTot))
    print "Index of largest syst:  ", idxMax
    print "lifetime of largest syst:  ", lifetimeRangeTot[idxMax]
    print "Debug:  printing JESJERRangeTot:"
    JESJERRangeTot.sort()
    print JESJERRangeTot
    # print "len(lifetimes) = ", len(lifetimes)
    # print "lifetimes: "
    # print lifetimes


systTableLines["JESJER"] = "jet energy scale / resolution       & " + "{:.0f}".format(smallestJESJER) + "--" + "{:.0f}".format(largestJESJER) + "\\% \\\\ \n"

#content += "total                               & " + "{:.0f}".format(smallestTot) + "--" + "{:.0f}".format(largestTot) + "\\% \\\
systTableLines["total"] = "total                               & " + "{:.0f}".format(smallestTot) + "--" + "{:.0f}".format(largestTot) + "\\% \\\\ \n"


# Now that all the lines are defined, fill the table:
content += systTableLines["Isr"]
content += systTableLines["JESJER"]
content += systTableLines["PDFWt"]
content += systTableLines["trigEff"]
content += systTableLines["NMissOut"]
#content += systTableLines["Nmissmid"]
content += systTableLines["Nmissinmid"]
content += systTableLines["Ecalo"]
content += systTableLines["pileup"]
content += systTableLines["trkReco"]
content += systTableLines["lumi"]
content += hline
content += systTableLines["total"]
content += hline
content += hline
content += "\\end{tabular}\n"
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"

###################################################
# Electron inefficiency table:
# tables/elecVetoEff.tex 
# tables/elecEst.tex 
###################################################


# Get the upper limit for each dataset separately.  
split_datasets = split_composite_datasets(datasets, composite_dataset_definitions)
(NPreselTot, NPreselTotErr) = getYield("Background", preselElecDir, "PreSelection")
print "Debug:  NPreselTot = " + str(NPreselTot)      
NYieldTotErr = 0.0  
fracPreselTot = 0.0
for dataset in split_datasets:
    NLimit                = getUpperLimit(dataset, fullSelecElecIdDir, "FullSelIdElec")
    (NYield,  NYieldErr)  = getYield(dataset,      fullSelecElecIdDir, "FullSelIdElec")
    (NPresel, NPreselErr) = getYield(dataset,   preselElecDir, "PreSelection")
    fracPresel = NPresel / NPreselTot
    fracPreselTot += fracPresel  
    NYieldTotErr += NLimit*fracPresel  
    print "Debug:  checking dataset: " + dataset + "; fracPresel = " + str(fracPresel) + "; NLimit = " + str(NLimit) + "; fracPresel*NLimit = " + str(fracPresel*NLimit)    
print "Debug:  NYieldTotErr = " + str(NYieldTotErr) + "; fracPreselTot = " + str(fracPreselTot)       

outputFile = "tables/elecVetoEff.tex"
fout = open (outputFile, "w")

# Create output with no lumi wt, using:
# fullSelectionChannelsForBkgdEstimates]$ hadd Wjets_PtW100_noLumiWt.root Wjets_PtW100/*root 
# fullSelectionChannelsForBkgdEstimates]$ hadd W4jets_noLumiWt.root W4jets/*root 
# fullSelectionChannelsForBkgdEstimates]$ hadd WjetsHighPt_noLumiWt.root W4jets_noLumiWt.root Wjets_PtW100_noLumiWt.root
# fullSelectionChannelsForBkgdEstimates]$ cutFlowLimits WjetsHighPt_noLumiWt.root  # Must do this last, to get correct upper limits
(NCtrl, NCtrlErr)   = getYield("WjetsHighPt_noLumiWt", fullSelecElecPrevetoDir,       "FullSelectionElecPreveto")
(NYield, NYieldErr) = getYield("WjetsHighPt_noLumiWt",      fullSelecElecIdDir, "FullSelIdElec")
NLimit              = getUpperLimit("WjetsHighPt_noLumiWt", fullSelecElecIdDir, "FullSelIdElec")
NYieldRaw = round(math.pow(NYield,2) / math.pow(NYieldErr,2)) if NYieldErr else 0 
NYieldErrRaw = NYieldRaw * (NYieldErr / NYield) if NYield else 0  
NLimitRaw = 0.5 * TMath.ChisquareQuantile (0.68, 2 * (NYieldRaw + 1)) # 68% CL upper limit, see https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp  

P = NYieldRaw / NCtrl
if NLimitRaw > NYieldErrRaw:
    PErr = NLimitRaw / NCtrl
else:
    PErr = NYieldErrRaw / NCtrl


content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^e_{\\rm ctrl}$ (MC) & $" + str(round(NCtrl)).replace(".0","") + "$     \\\\ \n"                               
content += "$N^e$ (MC)             & $"     + " < " + str(round_sigfigs(NLimitRaw,2))     + "$     \\\\ \n"                             
content += hline                                                              
content += "$P^e = N^e / N^e_{\\rm ctrl}$ & $ < " + str(round_sigfigs(PErr * 1e5,2)) + " \\times 10^{-5} $ \\\\  \n"
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close()
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"

outputFile = "tables/elecEst.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("MET", fullSelecElecPrevetoDir, "FullSelectionElecPreveto")  # data 
Nelec = NCtrl * P
NelecErr = NCtrl * PErr
content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^e_{\\rm ctrl}$ (data)  & $"  + str(round_sigfigs(NCtrl,5)).replace(".0","")  +  "$     \\\\ \n"                               
content += "$P^e$ (MC)               & $ < " + str(round_sigfigs(PErr * 1e5,2)) + " \\times 10^{-5} $ \\\\  \n"  
content += hline                                                              
content += "$N^e$                    & $ < " + str(round_sigfigs(NelecErr,2)) + " $ \\\\  \n"
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close()
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"

# Use these values for bkgdOptions.py below:  
PElec = P
PElecErr = PErr
NeCtrl = NCtrl
NelecErrSM = NelecErr

###################################################
# Muon inefficiency table:
# tables/muonVetoEff.tex 
# tables/muonEst.tex  
###################################################
# Get the upper limit for each dataset separately.  
split_datasets = split_composite_datasets(datasets, composite_dataset_definitions)
(NPreselTot, NPreselTotErr) = getYield("Background", preselMuDir, "PreSelection")
print "Debug:  NPreselTot = " + str(NPreselTot)      
NYieldTotErr = 0.0  
fracPreselTot = 0.0
for dataset in split_datasets:
    NLimit                = getUpperLimit(dataset, fullSelecMuIdDir, "FullSelIdMuon")
    (NYield,  NYieldErr)  = getYield(dataset,      fullSelecMuIdDir, "FullSelIdMuon")
    (NPresel, NPreselErr) = getYield(dataset,   preselMuDir, "PreSelection")
    fracPresel = NPresel / NPreselTot
    fracPreselTot += fracPresel  
    NYieldTotErr += NLimit*fracPresel  
    print "Debug:  checking dataset: " + dataset + "; fracPresel = " + str(fracPresel) + "; NLimit = " + str(NLimit) + "; fracPresel*NLimit = " + str(fracPresel*NLimit)    
print "Debug:  NYieldTotErr = " + str(NYieldTotErr) + "; fracPreselTot = " + str(fracPreselTot)       

outputFile = "tables/muonVetoEff.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("WjetsHighPt_noLumiWt", fullSelecMuPrevetoDir,       "FullSelectionMuPreveto")
(NYield, NYieldErr) = getYield("WjetsHighPt_noLumiWt",      fullSelecMuIdDir, "FullSelIdMuon")
NLimit              = getUpperLimit("WjetsHighPt_noLumiWt", fullSelecMuIdDir, "FullSelIdMuon")
NYieldRaw = round(math.pow(NYield,2) / math.pow(NYieldErr,2)) if NYieldErr else 0
NYieldErrRaw = NYieldRaw * (NYieldErr / NYield) if NYield else 0
NLimitRaw      =           0.5 * TMath.ChisquareQuantile (0.68, 2 * (NYieldRaw + 1)) # 68% CL upper limit, see https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp
alpha = 0.84
NYieldErrUpRaw = math.fabs(0.5 * TMath.ChisquareQuantile (alpha,       2 * (NYieldRaw + 1)) - NYieldRaw)
NYieldErrDnRaw = math.fabs(0.5 * TMath.ChisquareQuantile (1.0 - alpha, 2 * (NYieldRaw ))    - NYieldRaw)
print "Debug:  muon upper limit is ", NLimit
print "Debug:  muon NYieldErr = ", NYieldErr
print "Debug:  muon NYield = ", NYield

P = NYieldRaw / NCtrl
if NLimitRaw > NYieldErrRaw:
    PErr = NLimitRaw / NCtrl
else:
    PErr = NYieldErrRaw / NCtrl

PErrUp = NYieldErrUpRaw / NCtrl
PErrDn = NYieldErrDnRaw / NCtrl


content  = header
content += "\\begin{tabular}{lc}\n"
content += hline
content += hline

content += "$N^\\mu_{\\rm ctrl}$ (MC) & $" + str(round(NCtrl)).replace(".0","") + "$      \\\\ \n"
content += "$N^\\mu$ (MC)             & $" + str(round_sigfigs(NYieldRaw,2)) + " ^{+" + str(round_sigfigs(NYieldErrUpRaw,2)) + "}_{-" + str(round_sigfigs(NYieldErrDnRaw,2)) + "} $ \\\\ \n"                
content += hline
content += "$P^\\mu = N^\\mu / N^\\mu_{\\rm ctrl}$ & $(" + str(round_sigfigs(P * 1e4,2)) + " ^{+" + str(round_sigfigs(PErrUp * 1e4,2)) + "}_{-" + str(round_sigfigs(PErrDn * 1e4,2)) + "}) \\times 10^{-4} $ \\\\  \n"    
content += hline
content += hline
content += "\\end{tabular}\n"
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"
    
outputFile = "tables/muonEst.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("MET", fullSelecMuPrevetoDir,       "FullSelectionMuPreveto")
Nmuon = NCtrl * P
NmuonErr = NCtrl * PErr
NmuonErrUp = NCtrl * PErrUp
NmuonErrDn = NCtrl * PErrDn

content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline
content += "$N^\\mu_{\\rm ctrl}$ (data)  & $"  + str(round_sigfigs(NCtrl,5)).replace(".0","")  +  "$     \\\\ \n"
content += "$P^\\mu$ (MC)  & $(" + str(round_sigfigs(P * 1e4,2)) + " ^{+" + str(round_sigfigs(PErrUp * 1e4,2)) + "}_{-" + str(round_sigfigs(PErrDn * 1e4,2)) + "}) \\times 10^{-4} $ \\\\  \n"    
content += hline
content += "$N^\\mu$                    & $"  + str(round_sigfigs(Nmuon,2)) + " ^{+" + str(round_sigfigs(NmuonErrUp,2)) + "}_{-" + str(round_sigfigs(NmuonErrDn,2)) + "} $ \\\\  \n"
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close()
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"

# Use these values for bkgdOptions.py below:  
PMuon = P
PMuonErr = PErr
PMuonErrUp = PErrUp
PMuonErrDown = PErrDn
NmuCtrl = NCtrl
NmuonSM = Nmuon
NMuonErrorUpSM = NmuonErrUp
NMuonErrorDownSM = NmuonErrDn



###################################################
# Tau inefficiency table:
# tables/tauVetoEff.tex 
# tables/tauEst.tex  
###################################################
# Get the upper limit for each dataset separately.  
split_datasets = split_composite_datasets(datasets, composite_dataset_definitions)
(NPreselTot, NPreselTotErr) = getYield("Background", preselTauDir, "PreSelection")
print "Debug:  NPreselTot = " + str(NPreselTot)      
NYieldTotErr = 0.0  
fracPreselTot = 0.0
for dataset in split_datasets:
    NLimit                = getUpperLimit(dataset, fullSelecTauIdDir, "FullSelIdTau")
    (NYield,  NYieldErr)  = getYield(dataset,      fullSelecTauIdDir, "FullSelIdTau")
    (NPresel, NPreselErr) = getYield(dataset,   preselTauDir, "PreSelection")
    fracPresel = NPresel / NPreselTot
    fracPreselTot += fracPresel  
    NYieldTotErr += NLimit*fracPresel  
    print "Debug:  checking dataset: " + dataset + "; fracPresel = " + str(fracPresel) + "; NLimit = " + str(NLimit) + "; fracPresel*NLimit = " + str(fracPresel*NLimit)    
print "Debug:  NYieldTotErr = " + str(NYieldTotErr) + "; fracPreselTot = " + str(fracPreselTot)       

outputFile = "tables/tauVetoEff.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("WjetsHighPt_noLumiWt", fullSelecTauPrevetoDir,       "FullSelectionTauPreveto")
(NYield, NYieldErr) = getYield("WjetsHighPt_noLumiWt",     fullSelecTauIdDir, "FullSelIdTau")
NLimit              = getUpperLimit("WjetsHighPt_noLumiWt", fullSelecTauIdDir, "FullSelIdTau") 
NYieldRaw = round(math.pow(NYield,2) / math.pow(NYieldErr,2)) if NYieldErr else 0
NYieldErrRaw = NYieldRaw * (NYieldErr / NYield) if NYield else 0  
NLimitRaw = 0.5 * TMath.ChisquareQuantile (0.68, 2 * (NYieldRaw + 1)) # 68% CL upper limit, see https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp
P = NYieldRaw / NCtrl
if NLimitRaw > NYieldErrRaw:
    PErr = NLimitRaw / NCtrl
else:
    PErr = NYieldErrRaw / NCtrl
                
content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^\\tau_{\\rm ctrl}$ (MC)  & $" + str(round(NCtrl)).replace(".0","") + "$     \\\\ \n"                               
content += "$N^\\tau$            (MC)  & $" + " < " + str(round_sigfigs(NLimitRaw,2))   + "$     \\\\ \n"                             
content += hline                                                              
content += "$P^\\tau = N^\\tau / N^\\tau_{\\rm ctrl}$ & $" + " < " + str(round_sigfigs(PErr,2)) + " $ \\\\  \n"
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close()
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"

outputFile = "tables/tauEst.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("MET", fullSelecTauPrevetoDir,       "FullSelectionTauPreveto")
Ntau = NCtrl * P
NtauErr = NCtrl * PErr
content  = header 
content += "\\begin{tabular}{lc}\n"                                                 
content += hline                                                              
content += hline                                                              
content += "$N^\\tau_{\\rm ctrl}$ (data) & $"  + str(round_sigfigs(NCtrl,5)).replace(".0","")  +  "$     \\\\ \n"                               
content += "$P^\\tau$ (MC)               & $ < " + str(round_sigfigs(PErr,2)) + " $ \\\\  \n"  
content += hline                                                              
content += "$N^\\tau$                    & $ < " + str(round_sigfigs(NtauErr,2)) + " $ \\\\  \n"
content += hline                                                              
content += hline                                                              
content += "\\end{tabular}\n"                                                       
fout.write(content)  
fout.close() 
os.system("cat " + outputFile)  
print "Finished writing " + outputFile + "\n\n\n"

# Use these values for bkgdOptions.py below:  
PTau = P
PTauErr = PErr
NtauCtrl = NCtrl
NtauSM = Ntau
NtauErrSM = NtauErr
###################################################
# Fake track rate table:
# tables/fakeTrkRate.tex 
# tables/fakeEst.tex 
###################################################
outputFile = "tables/fakeTrkRate.tex"
fout = open (outputFile, "w")
(NCtrlMuMu, NCtrlErrMuMu)   = getYield("SingleMu", ztoMuMuDir,        "ZtoMuMu")
(NYieldMuMu, NYieldErrMuMu) = getYield("SingleMu", ztoMuMuFakeTrkDir, "ZtoMuMuFakeTrk")

(NCtrlEE, NCtrlErrEE)   = getYield("SingleElectron", ztoEEDir,        "ZtoEE")
(NYieldEE, NYieldErrEE) = getYield("SingleElectron", ztoEEFakeTrkDir, "ZtoEEFakeTrk")

NYield = NYieldMuMu + NYieldEE
NCtrl = NCtrlEE + NCtrlMuMu

NYieldErr = math.sqrt(math.pow(NYieldErrEE, 2) + math.pow(NYieldErrMuMu, 2))
NCtrlErr = math.sqrt(math.pow(NCtrlErrEE, 2) + math.pow(NCtrlErrMuMu, 2))

P = NYield / NCtrl 
PErr = P * math.sqrt(math.pow(NYieldErr/NYield, 2) + math.pow(NCtrlErr/NCtrl, 2)) 



NYieldRaw = round(math.pow(NYield,2) / math.pow(NYieldErr,2)) if NYieldErr else 0  # done for consistency with muon case, but since it's data, there are no weight factors so NYieldRaw = NYield
NfakeRaw = NYieldRaw  # Used for bkgd estimate table  
#NYieldErrRaw = NYieldRaw * (NYieldErr / NYield) if NYield else 0
#NLimitRaw      =           0.5 * TMath.ChisquareQuantile (0.68, 2 * (NYieldRaw + 1)) # 68% CL upper limit, see https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp
alpha = 0.84
NYieldErrUpRaw = math.fabs(0.5 * TMath.ChisquareQuantile (alpha,       2 * (NYieldRaw + 1)) - NYieldRaw)
NYieldErrDnRaw = math.fabs(0.5 * TMath.ChisquareQuantile (1.0 - alpha, 2 * (NYieldRaw ))    - NYieldRaw)

print "Debug:  NYieldRaw = ", NYieldRaw 

P = NYieldRaw / NCtrl
if NLimitRaw > NYieldErrRaw:
    PErr = NLimitRaw / NCtrl
else:
    PErr = NYieldErrRaw / NCtrl

PErrUp = NYieldErrUpRaw / NCtrl
PErrDn = NYieldErrDnRaw / NCtrl



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
(NCtrlMet, NCtrlMetErr)   = getYield("MET", metJetDir, "MetJet")
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

# Use for bkgdOptions.py below:
ScaleFacFakeTrk = NCtrlMet / NCtrl
ScaleFacFakeTrkErr = ScaleFacFakeTrk * math.sqrt(math.pow(NCtrlErr/NCtrl, 2) + math.pow(NCtrlMetErr/NCtrlMet, 2))  

(NCtrlMuMu, NCtrlErrMuMu)   = getYield("SingleMu", JessDir + 'ztoMuMuFakeTrkNHits5',       "ZtoMuMuFakeTrkNHits5")
(NCtrlEE, NCtrlErrEE)   = getYield("SingleElectron", JessDir + 'ztoEEFakeTrk3456NHit',     "ZtoEEFakeTrkNHits5")  
NCtrl = NCtrlEE + NCtrlMuMu

ScaleFacFakeTrk5Hits = Nfake / NCtrl
ScaleFacFakeTrk5HitsErr = NfakeErr / Nfake * ScaleFacFakeTrk5Hits 



###################################################
# Fake track ratio rates:
# tables/fakeTrkRateRatioLL.h
###################################################
outputFile = "tables/fakeTrkRateRatioLL.h"
fout = open (outputFile, "w")

(NSearchCtrl, NSearchCtrlErr)   = getYield("MET", metJetDir,        "MetJet")
(NYieldSearch_3, NYieldSearchErr_3) = getYield("MET", fullSelection3HitsDir, "FullSelectionNHits3");
(NYieldSearch_4, NYieldSearchErr_4) = getYield("MET", fullSelection4HitsDir, "FullSelectionNHits4");
(NYieldSearch_5, NYieldSearchErr_5) = getYield("MET", fullSelection5HitsDir, "FullSelectionNHits5");
(NYieldSearch_6, NYieldSearchErr_6) = getYield("MET", fullSelection6HitsDir, "FullSelectionNHits6");


(NCtrlEE, NCtrlErrEE)   = getYield("SingleElectron", ztoEEDir,        "ZtoEE")
(NYieldEE_3, NYieldErrEE_3) = getYield("SingleElectron", ztoEE3HitsDir, "ZtoEEFakeTrkNHits3")
(NYieldEE_4, NYieldErrEE_4) = getYield("SingleElectron", ztoEE4HitsDir, "ZtoEEFakeTrkNHits4")
(NYieldEE_5, NYieldErrEE_5) = getYield("SingleElectron", ztoEE5HitsDir, "ZtoEEFakeTrkNHits5")
(NYieldEE_6, NYieldErrEE_6) = getYield("SingleElectron", ztoEE6HitsDir, "ZtoEEFakeTrkNHits6")

(NCtrlMuMu, NCtrlErrMuMu)   = getYield("SingleMu", ztoMuMuDir,        "ZtoMuMu")
(NYieldMuMu_3, NYieldErrMuMu_3) = getYield("SingleMu", ztoMuMu3HitsDir, "ZtoMuMuFakeTrkNHits3")
(NYieldMuMu_4, NYieldErrMuMu_4) = getYield("SingleMu", ztoMuMu4HitsDir, "ZtoMuMuFakeTrkNHits4")
(NYieldMuMu_5, NYieldErrMuMu_5) = getYield("SingleMu", ztoMuMu5HitsDir, "ZtoMuMuFakeTrkNHits5")
(NYieldMuMu_6, NYieldErrMuMu_6) = getYield("SingleMu", ztoMuMu6HitsDir, "ZtoMuMuFakeTrkNHits6")

PSearch_3 = NYieldSearch_3 / NSearchCtrl
PSearchErr_3 = PSearch_3 * math.sqrt(math.pow(NYieldSearchErr_3/NYieldSearch_3, 2) + math.pow(NSearchCtrlErr/NSearchCtrl, 2))

PSearch_4 = NYieldSearch_4 / NSearchCtrl
PSearchErr_4 = PSearch_4 * math.sqrt(math.pow(NYieldSearchErr_4/NYieldSearch_4, 2) + math.pow(NSearchCtrlErr/NSearchCtrl, 2))

PSearch_5 = NYieldSearch_5 / NSearchCtrl
PSearchErr_5 = PSearch_5 * math.sqrt(math.pow(NYieldSearchErr_5/NYieldSearch_5, 2) + math.pow(NSearchCtrlErr/NSearchCtrl, 2))

PSearch_6 = NYieldSearch_6 / NSearchCtrl
PSearchErr_6 = PSearch_6 * math.sqrt(math.pow(NYieldSearchErr_6/NYieldSearch_6, 2) + math.pow(NSearchCtrlErr/NSearchCtrl, 2))

PEE_3 = NYieldEE_3 / NCtrlEE
PEE_4 = NYieldEE_4 / NCtrlEE
PEE_5 = NYieldEE_5 / NCtrlEE
PEE_6 = NYieldEE_6 / NCtrlEE

PLL_3 = (NYieldEE_3 + NYieldMuMu_3) / (NCtrlEE + NCtrlMuMu)
PLL_4 = (NYieldEE_4 + NYieldMuMu_4) / (NCtrlEE + NCtrlMuMu)
PLL_5 = (NYieldEE_5 + NYieldMuMu_5) / (NCtrlEE + NCtrlMuMu)
PLL_6 = (NYieldEE_6 + NYieldMuMu_6) / (NCtrlEE + NCtrlMuMu)

NYieldLL_3 = NYieldEE_3 + NYieldMuMu_3
NYieldLL_4 = NYieldEE_4 + NYieldMuMu_4
NYieldLL_5 = NYieldEE_5 + NYieldMuMu_5
NYieldLL_6 = NYieldEE_6 + NYieldMuMu_6


NCtrlLL = NCtrlEE + NCtrlMuMu
NCtrlErrLL = NCtrlLL * (math.sqrt(math.pow(NCtrlErrEE/NCtrlEE,2) + math.pow(NCtrlErrMuMu/NCtrlMuMu,2)))

NYieldErrLL_3 = NYieldLL_3 * math.sqrt(math.pow(NYieldErrEE_3/NYieldEE_3,2) + math.pow(NYieldErrMuMu_3/NYieldMuMu_3,2))
NYieldErrLL_4 = NYieldLL_4 * math.sqrt(math.pow(NYieldErrEE_4/NYieldEE_4,2) + math.pow(NYieldErrMuMu_4/NYieldMuMu_4,2))
NYieldErrLL_5 = NYieldLL_5 * math.sqrt(math.pow(NYieldErrEE_5/NYieldEE_5,2) + math.pow(NYieldErrMuMu_5/NYieldMuMu_5,2))
NYieldErrLL_6 = NYieldLL_6 * math.sqrt(math.pow(NYieldErrEE_6/NYieldEE_6,2) + math.pow(NYieldErrMuMu_6/NYieldMuMu_6,2))

ratioEE_3 = PSearch_3 / PEE_3
ratioEE_4 = PSearch_4 / PEE_4
ratioEE_6 = PSearch_6 / PEE_6
ratioEE_5 = PSearch_5 / PEE_5

ratioLL_3 = PSearch_3 / PLL_3
ratioLL_4 = PSearch_4 / PLL_4
ratioLL_5 = PSearch_5 / PLL_5
ratioLL_6 = PSearch_6 / PLL_6


PErrEE_3 = PEE_3 * math.sqrt(math.pow(NYieldErrEE_3/NYieldEE_3, 2) + math.pow(NCtrlErrEE/NCtrlEE, 2))
PErrEE_4 = PEE_4 * math.sqrt(math.pow(NYieldErrEE_4/NYieldEE_4, 2) + math.pow(NCtrlErrEE/NCtrlEE, 2))
PErrEE_5 = PEE_5 * math.sqrt(math.pow(NYieldErrEE_5/NYieldEE_5, 2) + math.pow(NCtrlErrEE/NCtrlEE, 2))
PErrEE_6 = PEE_6 * math.sqrt(math.pow(NYieldErrEE_6/NYieldEE_6, 2) + math.pow(NCtrlErrEE/NCtrlEE, 2))



PErrLL_3 = PLL_3 * math.sqrt(math.pow(NYieldErrLL_3/NYieldLL_3, 2) + math.pow(NCtrlErrLL/NCtrlLL, 2))
PErrLL_4 = PLL_4 * math.sqrt(math.pow(NYieldErrLL_4/NYieldLL_4, 2) + math.pow(NCtrlErrLL/NCtrlLL, 2))
PErrLL_5 = PLL_5 * math.sqrt(math.pow(NYieldErrLL_5/NYieldLL_5, 2) + math.pow(NCtrlErrLL/NCtrlLL, 2))
PErrLL_6 = PLL_6 * math.sqrt(math.pow(NYieldErrLL_6/NYieldLL_6, 2) + math.pow(NCtrlErrLL/NCtrlLL, 2))

ratioErrEE_3 = ratioEE_3 * math.sqrt(math.pow(PErrEE_3/PEE_3, 2) + math.pow(PSearchErr_3/PSearch_3, 2))
ratioErrEE_4 = ratioEE_4 * math.sqrt(math.pow(PErrEE_4/PEE_4, 2) + math.pow(PSearchErr_4/PSearch_4, 2))
ratioErrEE_5 = ratioEE_5 * math.sqrt(math.pow(PErrEE_5/PEE_5, 2) + math.pow(PSearchErr_5/PSearch_5, 2))
ratioErrEE_6 = ratioEE_6 * math.sqrt(math.pow(PErrEE_6/PEE_6, 2) + math.pow(PSearchErr_6/PSearch_6, 2))

ratioErrLL_3 = ratioLL_3 * math.sqrt(math.pow(PErrLL_3/PLL_3, 2) + math.pow(PSearchErr_3/PSearch_3, 2))
ratioErrLL_4 = ratioLL_4 * math.sqrt(math.pow(PErrLL_4/PLL_4, 2) + math.pow(PSearchErr_4/PSearch_4, 2))
ratioErrLL_5 = ratioLL_5 * math.sqrt(math.pow(PErrLL_5/PLL_5, 2) + math.pow(PSearchErr_5/PSearch_5, 2))
ratioErrLL_6 = ratioLL_6 * math.sqrt(math.pow(PErrLL_6/PLL_6, 2) + math.pow(PSearchErr_6/PSearch_6, 2))

content = "double ratioEE_3 = " + str(round_sigfigs(ratioEE_3,2)) + " ; " 
content += "double ratioEE_4 = " + str(round_sigfigs(ratioEE_4,2)) + " ; " 
content += "double ratioEE_5 = " + str(round_sigfigs(ratioEE_5,2)) + " ; " 
content += "double ratioEE_6 = " + str(round_sigfigs(ratioEE_6,2)) + " ; "

content += "double ratioErrEE_3 = " + str(round_sigfigs(ratioErrEE_3,2)) + " ; "
content += "double ratioErrEE_4 = " + str(round_sigfigs(ratioErrEE_4,2)) + " ; "
content += "double ratioErrEE_5 = " + str(round_sigfigs(ratioErrEE_5,2)) + " ; "
content += "double ratioErrEE_6 = " + str(round_sigfigs(ratioErrEE_6,2)) + " ; "

content += "double ratioLL_3 = " + str(round_sigfigs(ratioLL_3,2)) + " ; "
content += "double ratioLL_4 = " + str(round_sigfigs(ratioLL_4,2)) + " ; "
content += "double ratioLL_5 = " + str(round_sigfigs(ratioLL_5,2)) + " ; "
content += "double ratioLL_6 = " + str(round_sigfigs(ratioLL_6,2)) + " ; "

content += "double ratioErrLL_3 = " + str(round_sigfigs(ratioErrLL_3,2)) + " ; "
content += "double ratioErrLL_4 = " + str(round_sigfigs(ratioErrLL_4,2)) + " ; "
content += "double ratioErrLL_5 = " + str(round_sigfigs(ratioErrLL_5,2)) + " ; "
content += "double ratioErrLL_6 = " + str(round_sigfigs(ratioErrLL_6,2)) + " ; "

#content += hline
#content += hline
#content += "\\end{tabular}\n"
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"


###################################################
# Electron inefficiency systematic
# tables/elecIneffSyst.tex  
# tables/elecIneffSystShort.tex  
###################################################
outputFile = "tables/elecIneffSyst.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("Background", elecSystDir, "ZtoETrkEIdLoosePtNoVeto") 
(NYield, NYieldErr) = getYield("Background", elecSystDir, "ZtoETrkEIdLoosePt") 
print NYield
print NCtrl
P = NYield / NCtrl / 2.0

PErr = P * math.sqrt(math.pow(NYieldErr/NYield, 2) + math.pow(NCtrlErr/NCtrl, 2))

(NCtrlData, NCtrlErrData)   = getYield("SingleElectron", elecSystDir, "ZtoETrkEIdLoosePtNoVeto") 
(NYieldData, NYieldErrData) = getYield("SingleElectron", elecSystDir, "ZtoETrkEIdLoosePt") 
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


outputFile = "tables/elecIneffSystShort.tex"
fout = open (outputFile, "w")
content  = header
content += "\\begin{tabular}{lcc} \n"
content += hline
content += hline
content += "$P^e$ (data)       & $(" + str(round_sigfigs(PData * 1.e5,3)) + " \\pm " + str(round_sigfigs(PErrData * 1.e5,2)) + ") \\times 10^{-5}$  \\\\ \n "
content += "$P^e$ (MC)         & $(" + str(round_sigfigs(P     * 1.e5,3)) + " \\pm " + str(round_sigfigs(PErr     * 1.e5,2)) + ") \\times 10^{-5}$  \\\\ \n" 
content += hline
content += "data/MC  & $" + str(round_sigfigs(ratio,2)) + " \\pm " + str(round_sigfigs(ratioErr,2)) + "$ \\\\  \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
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
(NCtrl, NCtrlErr)   = getYield("Background", muSystDir, "ZtoMuTrkNoVetoLoosePt") 
(NYield, NYieldErr) = getYield("Background", muSystDir, "ZtoMuTrkLoosePt")       

(NCtrlData, NCtrlErrData)   = getYield("SingleMu", muSystDir, "ZtoMuTrkNoVetoLoosePt") 
(NYieldData, NYieldErrData) = getYield("SingleMu", muSystDir, "ZtoMuTrkLoosePt")       

(NMu, NMuErr) = getTruthYield("Background", muSystDir, "ZtoMuTrkLoosePt", "#mu")
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
content += "$(" + "{:0.2f}".format(PData * 1.e5) + " \\pm " + "{:0.2f}".format(PErrData * 1.e5) + ") \\times 10^{-5} $ & "
content += "$(" + "{:0.2f}".format(P     * 1.e5) + " \\pm " + "{:0.2f}".format(PErr     * 1.e5) + ") \\times 10^{-5} $  \\\\ \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% data/MC ratio of fake rates:  " + str(round_sigfigs(ratio,5)) + " \\pm " + str(round_sigfigs(ratioErr,5)) + "\n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"



outputFile = "tables/muonIneffSystShort.tex"
fout = open (outputFile, "w")
content  = header
content += "\\begin{tabular}{lcc} \n"
content += hline
content += hline
content += "$P^\\mu$ (data)       & $(" + str(round_sigfigs(PData * 1.e5,3)) + " \\pm " + str(round_sigfigs(PErrData * 1.e5,2)) + ") \\times 10^{-5}$  \\\\ \n "
content += "$P^\\mu$ (MC)         & $(" + str(round_sigfigs(P     * 1.e5,3)) + " \\pm " + str(round_sigfigs(PErr     * 1.e5,2)) + ") \\times 10^{-5}$  \\\\ \n" 
content += hline
content += "data/MC  & $" + str(round_sigfigs(ratio,2)) + " \\pm " + str(round_sigfigs(ratioErr,2)) + "$ \\\\  \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"


###################################################
# Tau inefficiency systematic
# tables/tauIneffSyst.tex  
###################################################
outputFile = "tables/tauIneffSyst.tex"
fout = open (outputFile, "w")
(NCtrl, NCtrlErr)   = getYield("Background", tauSystDir, "ZtoMuTauHadNoTau") 
(NYield, NYieldErr) = getYield("Background", tauSystDir, "ZtoMuTauHadNoTrkJetDeltaR")       

(NCtrlData, NCtrlErrData)   = getYield("SingleMu", tauSystDir, "ZtoMuTauHadNoTau") 
(NYieldData, NYieldErrData) = getYield("SingleMu", tauSystDir, "ZtoMuTauHadNoTrkJetDeltaR")       

(NTau, NTauErr) = getTruthYield("Background", tauSystDir, "ZtoMuTauHadNoTrkJetDeltaR", "#tau")
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
content += "$" + "{:0.3f}".format(PData) + " \\pm " + "{:0.3f}".format(PErrData) + " $ & "
content += "$" + "{:0.3f}".format(P)     + " \\pm " + "{:0.3f}".format(PErr)     + " $  \\\\ \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% data/MC ratio of fake rates:  " + str(round_sigfigs(ratio,5)) + " \\pm " + str(round_sigfigs(ratioErr,5)) + "\n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"


outputFile = "tables/tauIneffSystShort.tex"
fout = open (outputFile, "w")
content  = header
content += "\\begin{tabular}{lcc} \n"
content += hline
content += hline
content += "$P^\\tau$ (data)       & $" + str(round_sigfigs(PData,3)) + " \\pm " + str(round_sigfigs(PErrData,2)) + "$  \\\\ \n "
content += "$P^\\tau$ (MC)         & $" + str(round_sigfigs(P    ,3)) + " \\pm " + str(round_sigfigs(PErr    ,2)) + "$  \\\\ \n" 
content += hline
content += "data/MC  & $" + str(round_sigfigs(ratio,3)) + " \\pm " + str(round_sigfigs(ratioErr,2)) + "$ \\\\  \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
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

(NCtrl, NCtrlErr)   = getYield("SingleMu", fakeMuMuSystDir,              "ZtoMuMu")
(NYield, NYieldErr) = getYield("SingleMu", fakeMuMu5HitsSystDir, "ZtoMuMuFakeTrkNHits5")

(NCtrlEE, NCtrlErrEE)   = getYield("SingleElectron", fakeEESystDir,        "ZtoEE")
(NYieldEE, NYieldErrEE) = getYield("SingleElectron", fakeEE5HitsSystDir, "ZtoEEFakeTrkNHits5")

NYield = NYield + NYieldEE
NCtrl = NCtrl + NCtrlEE
P = NYield / NCtrl

NYieldErr = math.sqrt(math.pow(NYieldErrEE, 2) + math.pow(NYieldErr, 2))
NCtrlErr = math.sqrt(math.pow(NCtrlErrEE, 2) + math.pow(NCtrlErr, 2))

PErr = P * math.sqrt(math.pow(NYieldErr/NYield, 2) + math.pow(NCtrlErr/NCtrl, 2))

(NCtrlData, NCtrlErrData)   = getYield("MET", fakeSearchSystDir, "MetJet") 
(NYieldData, NYieldErrData) = getYield("MET", fakeSearch5HitsSystDir, "FullSelectionNHits5") 
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
content += "$N^{\\rm fake}_{\\rm 5 hits}$ & "
content += "$" + str(round_sigfigs(NYieldData,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NYieldErrData,2)).rstrip("0").rstrip(".") + "$ & "
content += "$" + str(round_sigfigs(NYield    ,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NYieldErr    ,2)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
content += hline
content += "$P^{\\rm fake}_{\\rm 5 hits}$  & " 
content += "$(" + str(round_sigfigs(PData * 1.e6,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErrData * 1.e6,2)).rstrip("0").rstrip(".") + ") \\times 10^{-6}$ & "
content += "$(" + str(round_sigfigs(P     * 1.e6,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErr     * 1.e6,1)).rstrip("0").rstrip(".") + ") \\times 10^{-6}$  \\\\ \n" 
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% data/MC ratio of fake rates:  " + str(round_sigfigs(ratio,5)) + " \\pm " + str(round_sigfigs(ratioErr,5)) + "\n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"



###################################################
# Ecalo systematic
# tables/systEcalo.tex
# Can do cross check with: > getHistIntegrals.py -l configHistIntegralsSystEcalo.py  
###################################################
outputFile = "tables/systEcalo.tex"
fout = open (outputFile, "w")

(NTot, NTotErr)   = getHistIntegral("Background", systEcaloDir, "ZtoMuMuFakeTrkNHits4NoEcalo", "trackCaloTot_RhoCorr",0,110)
(NPass, NPassErr) = getHistIntegral("Background", systEcaloDir, "ZtoMuMuFakeTrkNHits4NoEcalo", "trackCaloTot_RhoCorr",0,9.9)
P = NPass / NTot 
PErr = P * math.sqrt(math.pow(NPassErr/NPass, 2) + math.pow(NTotErr/NTot, 2))

(NTotData, NTotErrData)   = getHistIntegral("SingleMu", systEcaloDir, "ZtoMuMuFakeTrkNHits4NoEcalo", "trackCaloTot_RhoCorr",0,110)
(NPassData, NPassErrData) = getHistIntegral("SingleMu", systEcaloDir, "ZtoMuMuFakeTrkNHits4NoEcalo", "trackCaloTot_RhoCorr",0,9.9)
PData = NPassData / NTotData 
PErrData = PData * math.sqrt(math.pow(NPassErrData/NPassData, 2) + math.pow(NTotErrData/NTotData, 2))

ratio = PData / P
ratioErr = ratio * math.sqrt(math.pow(PErrData/PData, 2) + math.pow(PErr/P, 2))
ratio1SigUp = math.fabs(ratio + ratioErr - 1.0)
ratio1SigDn = math.fabs(ratio - ratioErr - 1.0)
syst = math.fabs(1.0 - ratio)  # relative systematic uncertainty  

content  = header
content += "\\begin{tabular}{lcc} \n"
content += hline
content += hline
# Comment out lines below, don't need all this info.  
content += "%& data   & MC   \\\\ \n"
#content += hline
content += "%$N^{\\rm tot}$   & " 
content += "$" + str(round_sigfigs(NTotData,6)).rstrip("0").rstrip(".")  + " \\pm " + str(round_sigfigs(NTotErrData,3)).rstrip("0").rstrip(".") + "$ & "          
content += "$" + str(round_sigfigs(NTot    ,6)).rstrip("0").rstrip(".")  + " \\pm " + str(round_sigfigs(NTotErr    ,3)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
content += "%$Ecalo < 10 $ & "
content += "$" + str(round_sigfigs(NPassData,6)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NPassErrData,3)).rstrip("0").rstrip(".") + "$ & "
content += "$" + str(round_sigfigs(NPass    ,6)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NPassErr    ,3)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
#content += hline
content += "%$\\epsilon$  & " 
content += "$" + str(round_sigfigs(PData,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErrData,2)).rstrip("0").rstrip(".") + " $ & "
content += "$" + str(round_sigfigs(P    ,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErr    ,2)).rstrip("0").rstrip(".") + " $ & "  
content += "$" + str(round_sigfigs(ratio,3)) + " \\pm " + str(round_sigfigs(ratioErr,3)) + "$  \\\\ \n"
content += " & $\\epsilon(Ecalo < 10 GeV)$ \\\\ \n" 
content += hline
content += "data    & " + "$" + "{:0.3f}".format(PData)  + " \\pm " + "{:0.3f}".format(PErrData) + " $ \\\\ \n"
content += "MC      & " + "$" + "{:0.3f}".format(P)      + " \\pm " + "{:0.3f}".format(PErr)     + " $ \\\\ \n"
content += "data/MC & " + "$" + "{:0.3f}".format(ratio)  + " \\pm " + "{:0.3f}".format(ratioErr) + "$  \\\\ \n"  
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% For amsbLimitConfigNew.py Ecalo systematic:     'value' : '" + "{:0.3f}".format(1.0 + syst) + "', \n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"


###################################################
# NmissInner systematic
# tables/systNmissIn.tex  
###################################################
outputFile = "tables/systNmissIn.tex"
fout = open (outputFile, "w")

(NTot, NTotErr)   = getHistIntegral("Background", systNMissInDir, "PreSelectionMuonNoMissInMid", "trackNHitsMissingInner",0,5)
(NPass, NPassErr) = getHistIntegral("Background", systNMissInDir, "PreSelectionMuonNoMissInMid", "trackNHitsMissingInner",0,0)
P = NPass / NTot 
PErr = P * math.sqrt(math.pow(NPassErr/NPass, 2) + math.pow(NTotErr/NTot, 2))

(NTotData, NTotErrData)   = getHistIntegral("MET", systNMissInDir, "PreSelectionMuonNoMissInMid", "trackNHitsMissingInner",0,5)
(NPassData, NPassErrData) = getHistIntegral("MET", systNMissInDir, "PreSelectionMuonNoMissInMid", "trackNHitsMissingInner",0,0)
PData = NPassData / NTotData 
PErrData = PData * math.sqrt(math.pow(NPassErrData/NPassData, 2) + math.pow(NTotErrData/NTotData, 2))

ratio = PData / P
ratioErr = ratio * math.sqrt(math.pow(PErrData/PData, 2) + math.pow(PErr/P, 2))
ratio1SigUp = math.fabs(ratio + ratioErr - 1.0)
ratio1SigDn = math.fabs(ratio - ratioErr - 1.0)
syst = math.fabs(1.0 - ratio)  # relative systematic uncertainty  

content  = header
content += "\\begin{tabular}{lcc} \n"
content += hline
content += hline
# Comment out lines below, don't need all this info.  
content += "%& data   & MC   \\\\ \n"
#content += hline
content += "%$N^{\\rm tot}$   & " 
content += "$" + str(round_sigfigs(NTotData,6)).rstrip("0").rstrip(".")  + " \\pm " + str(round_sigfigs(NTotErrData,3)).rstrip("0").rstrip(".") + "$ & "          
content += "$" + str(round_sigfigs(NTot    ,6)).rstrip("0").rstrip(".")  + " \\pm " + str(round_sigfigs(NTotErr    ,3)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
content += "%$N^{\\rm inner}_{\\rm miss} == 0$ & "
content += "$" + str(round_sigfigs(NPassData,6)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NPassErrData,3)).rstrip("0").rstrip(".") + "$ & "
content += "$" + str(round_sigfigs(NPass    ,6)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NPassErr    ,3)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
#content += hline
content += "%$\\epsilon$  & " 
content += "$" + str(round_sigfigs(PData,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErrData,2)).rstrip("0").rstrip(".") + " $ & "
content += "$" + str(round_sigfigs(P    ,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErr    ,2)).rstrip("0").rstrip(".") + " $ & "  
content += "$" + str(round_sigfigs(ratio,3)) + " \\pm " + str(round_sigfigs(ratioErr,3)) + "$  \\\\ \n"
content += " & $\\epsilon(N^{\\rm inner}_{\\rm miss} == 0)$ \\\\ \n" 
content += hline
content += "data    & " + "$" + "{:0.3f}".format(PData)  + " \\pm " + "{:0.3f}".format(PErrData) + " $ \\\\ \n"
content += "MC      & " + "$" + "{:0.3f}".format(P)      + " \\pm " + "{:0.3f}".format(PErr)     + " $ \\\\ \n"
content += "data/MC & " + "$" + "{:0.3f}".format(ratio)  + " \\pm " + "{:0.3f}".format(ratioErr) + "$  \\\\ \n"
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% For amsbLimitConfigNew.py Nmissin systematic:     'value' : '" + "{:0.3f}".format(1.0 + syst) + "', \n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"


###################################################
# NmissMiddle systematic
# tables/systNmissMid.tex  
###################################################
outputFile = "tables/systNmissMid.tex"
fout = open (outputFile, "w")

(NTot, NTotErr)   = getHistIntegral("Background", systNMissMidDir, "PreSelectionMuonNoMissInMid", "trackNHitsMissingMiddle",0,5)
(NPass, NPassErr) = getHistIntegral("Background", systNMissMidDir, "PreSelectionMuonNoMissInMid", "trackNHitsMissingMiddle",0,0)
P = NPass / NTot 
PErr = P * math.sqrt(math.pow(NPassErr/NPass, 2) + math.pow(NTotErr/NTot, 2))

(NTotData, NTotErrData)   = getHistIntegral("MET", systNMissMidDir, "PreSelectionMuonNoMissInMid", "trackNHitsMissingMiddle",0,5)
(NPassData, NPassErrData) = getHistIntegral("MET", systNMissMidDir, "PreSelectionMuonNoMissInMid", "trackNHitsMissingMiddle",0,0)
PData = NPassData / NTotData 
PErrData = PData * math.sqrt(math.pow(NPassErrData/NPassData, 2) + math.pow(NTotErrData/NTotData, 2))

ratio = PData / P
ratioErr = ratio * math.sqrt(math.pow(PErrData/PData, 2) + math.pow(PErr/P, 2))
ratio1SigUp = math.fabs(ratio + ratioErr - 1.0)
ratio1SigDn = math.fabs(ratio - ratioErr - 1.0)
syst = math.fabs(1.0 - ratio)  # relative systematic uncertainty

content  = header
content += "\\begin{tabular}{lccc} \n"
content += hline
content += hline
#content += "& data   & MC  & data/MC  \\\\ \n"
#content += hline
content += "%$N^{\\rm tot}$   & " 
content += "$" + str(round_sigfigs(NTotData,6)).rstrip("0").rstrip(".")  + " \\pm " + str(round_sigfigs(NTotErrData,3)).rstrip("0").rstrip(".") + "$ & "          
content += "$" + str(round_sigfigs(NTot    ,6)).rstrip("0").rstrip(".")  + " \\pm " + str(round_sigfigs(NTotErr    ,3)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
content += "%$N^{\\rm mid}_{\\rm miss} == 0$ & "
content += "$" + str(round_sigfigs(NPassData,6)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NPassErrData,3)).rstrip("0").rstrip(".") + "$ & "
content += "$" + str(round_sigfigs(NPass    ,6)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(NPassErr    ,3)).rstrip("0").rstrip(".") + "$    \\\\ \n"  
#content += hline
content += "%$\\epsilon$  & " 
content += "$" + str(round_sigfigs(PData,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErrData,2)).rstrip("0").rstrip(".") + " $ & "
content += "$" + str(round_sigfigs(P    ,3)).rstrip("0").rstrip(".") + " \\pm " + str(round_sigfigs(PErr    ,2)).rstrip("0").rstrip(".") + " $ & "  
content += "$" + str(round_sigfigs(ratio,3)) + " \\pm " + str(round_sigfigs(ratioErr,3)) + "$  \\\\ \n"  
content += " & $\\epsilon(N^{\\rm mid}_{\\rm miss} == 0)$ \\\\ \n" 
content += hline
content += "data    & " + "$" + "{:0.3f}".format(PData)  + " \\pm " + "{:0.3f}".format(PErrData) + " $ \\\\ \n"
content += "MC      & " + "$" + "{:0.3f}".format(P)      + " \\pm " + "{:0.3f}".format(PErr)     + " $ \\\\ \n"
content += "data/MC & " + "$" + "{:0.3f}".format(ratio)  + " \\pm " + "{:0.3f}".format(ratioErr) + "$  \\\\ \n"
content += hline
content += hline
content += "\\end{tabular}\n"                                                       
content += "% For amsbLimitConfigNew.py Nmissmid systematic:     'value' : '" + "{:0.3f}".format(1.0 + syst) + "', \n"  
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"


###################################################
# Configuration to make background estimate plots  
# bkgdOptions.py
###################################################
outputFile = "bkgdOptions.py" 
fout = open (outputFile, "w")

content  = "# Table produced with makeANTables.py  \n" 
content += "#!/usr/bin/env python  \n"  
content += "# ../scripts/bkgdFromData.py -l bkgdOptions.py -c condor_2014_MM_DD_BkgdEstFullSel   \n"
content += "# mergeOutput.py -q -C -s FakeBkgd -l localOptionsBkgdEst.py -c condor_2014_MM_DD_BkgdEstFullSel   \n"  
content += "# makePlots.py       -l localOptionsBkgdEst.py -c condor_2014_MM_DD_BkgdEstFullSel -o stacked_histograms.root   \n"
content += "# makePlots.py -P paperPlotsOptions.py      \n" 
content += "   \n"
content += "import os   \n"
content += "   \n"
content += "cwd = os.getcwd()   \n"
content += "   \n"
content += "if 'wulsin' in cwd:   \n"
content += "    WellsDir = ''     \n"
content += "    JessDir = 'JessCondor/'   \n"
content += "elif 'jbrinson' in cwd:   \n"
content += "    WellsDir = 'WellsCondorNew/'   \n"
content += "    JessDir = ''   \n"
content += "else:   \n"
content += "    print 'Error: could not identify user as wulsin or jbrinson.'   \n"
content += "    os.exit(0)   \n"
content += "       \n"
content += "impurities = []  # not yet implemented   \n"
content += "       \n"

content += "bkgd_sources = {   \n"
content += "    'MET' :  { 'inputDir'   : JessDir+'fullSelectionSkim_24June',   \n"
content += "               'datasetsIn'  : ['MET'],   \n"
content += "               'scale_factor' :       1.0,   \n"
content += "               'scale_factor_error' : 0.0,   \n"
content += "               'channel_map' : {   \n"
content += "    'FullSelection' : ['FullSelection'],   \n"
content += "    }   \n"
content += "               },   \n"
content += "       \n"
content += "    'ElecBkgd' :  { 'inputDir'   : JessDir + 'fullSelectionElecPrevetoSkim_24June',   \n"
content += "                    'datasetsIn'  : ['MET'],   \n"
content += "                    'scale_factor' :        " + str(PElec)    + ",   \n"
content += "                    'scale_factor_error' :  " + str(PElecErr) + ",   \n"
content += "                    'channel_map' : {   \n"
content += "    'FullSelectionElecPreveto' : ['FullSelection'],   \n"
content += "    }   \n"
content += "                    },   \n"
content += "       \n"
content += "    'MuonBkgd' :  { 'inputDir'   : JessDir + 'fullSelectionMuPrevetoSkim_24June',   \n"
content += "                    'datasetsIn'  : ['MET'],   \n"
content += "                    'scale_factor' :        " + str(PMuon) + ",   \n"
content += "                    'scale_factor_error' :  " + str(PMuonErr) + ",   \n"
content += "                    'channel_map' : {   \n"
content += "    'FullSelectionMuPreveto' : ['FullSelection'],   \n"
content += "    }   \n"
content += "                    },   \n"
content += "       \n"
content += "    'TauBkgd' :  { 'inputDir'   : JessDir +  'fullSelectionTauPrevetoSkim_24June',   \n"
content += "                   'datasetsIn'  : ['MET'],   \n"
content += "                   'scale_factor' :        " + str(PTau) + ",   \n"
content += "                   'scale_factor_error' :  " + str(PTauErr) + ",   \n"
content += "                   'channel_map' : {   \n"
content += "    'FullSelectionTauPreveto' : ['FullSelection'],   \n"
content += "    }   \n"
content += "                   },   \n"
content += "       \n"
content += "       \n"
content += "       \n"
content += "    'FakeMuMuBkgd' :  { 'inputDir'   : JessDir + 'ztoMuMuFakeTrkNHits5',   \n"
content += "                    'datasetsIn'  : ['SingleMu'],   \n"
content += "                    'scale_factor' :        " + str(ScaleFacFakeTrk5Hits) + ",   \n"
content += "                    'scale_factor_error' :  " + str(ScaleFacFakeTrk5HitsErr) + ",   \n"  
content += "                    'channel_map' : {   \n"
content += "    'ZtoMuMuFakeTrkNHits5' : ['FullSelection'],   \n"
content += "    }   \n"
content += "                    },   \n"
content += "    'FakeEEBkgd' :  { 'inputDir'   : JessDir + 'ztoEEFakeTrk3456NHit',   \n"
content += "                    'datasetsIn'  : ['SingleElectron'],   \n"
content += "                    'scale_factor' :        " + str(ScaleFacFakeTrk5Hits) + ",   \n"
content += "                    'scale_factor_error' :  " + str(ScaleFacFakeTrk5HitsErr) + ",   \n"  
content += "                    'channel_map' : {   \n"
content += "    'ZtoEEFakeTrkNHits5' : ['FullSelection'],   \n"
content += "    }   \n"
content += "                    },   \n"
content += "       \n"
content += "       \n"
content += "    }   \n"
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
# amsbLimitConfigBkgds.py (Must do this one first, since it is used by toyUpperLimitBkgdSum.py  
# tables/bkgdSumm.tex
###################################################

outputFile = "amsbLimitConfigBkgds.py"  
fout = open (outputFile, "w")

# Calculate the number of raw events, based on the yield and the error
# Y = w * N
# sigma = w * sqrt(N)
# N = Y^2 / sigma^2
# N: number of raw events
# w: weight
# Y: weighted yield
# sigma:  error on weighted yield
# Then round to nearest integer.  
(NelecMC, NelecMCErr) = getYield("Background", fullSelecElecIdDir, "FullSelIdElec")
(NmuonMC, NmuonMCErr) = getYield("Background", fullSelecMuIdDir, "FullSelIdMuon")
(NtauMC,  NtauMCErr)  = getYield("WjetsHighPt", fullSelecTauIdDir, "FullSelIdTau")  # Do not include TTbar event  


#NfakeRaw = round(math.pow(Nfake,2)   / math.pow(NfakeErr,2))   if NfakeErr   else 0 # Can use the fake track estimate, since the error is scaled by the same weight as the central value
NelecRaw = round(math.pow(NelecMC,2) / math.pow(NelecMCErr,2)) if NelecMCErr else 0 
NmuonRaw = round(math.pow(NmuonMC,2) / math.pow(NmuonMCErr,2)) if NmuonMCErr else 0 
NtauRaw  = round(math.pow(NtauMC,2)  / math.pow(NtauMCErr,2))  if NtauMCErr  else 0 
print "NfakeRaw = " + str(NfakeRaw)  
print "NmuonRaw = " + str(NmuonRaw)  

CL68factor = 1.139  # See https://github.com/OSU-CMS/OSUT3Analysis/blob/master/AnaTools/bin/cutFlowLimits.cpp for PDG reference  
alphaElec = NelecErr / CL68factor
alphaMuon = Nmuon / NmuonRaw  
alphaTau  = NtauErr / CL68factor
alphaFake = Nfake / NfakeRaw


content  = "#!/usr/bin/env python   \n"
content += "# Produced with ../scripts/makeANTables.py  \n" 
content += "\n"  
content += "backgrounds = { \n"
content += "'Elec' : {    \n"
content += "    'N' : '" + str(NelecRaw).replace(".0","") + "',    \n"  
content += "    'alpha' : '" + str(round_sigfigs(alphaElec,4)) + "',    \n"
content += "        },    \n"
content += "'Muon' : {    \n"
content += "    'N' : '" + str(NmuonRaw).replace(".0","") + "',    \n"  
content += "    'alpha' : '" + str(round_sigfigs(alphaMuon,4)) + "',    \n"
content += "        },    \n"
content += "'Tau' : {    \n"
content += "    'N' : '" + str(NtauRaw).replace(".0","") + "',    \n"  
content += "    'alpha' : '" + str(round_sigfigs(alphaTau,4)) + "',    \n"
content += "        },    \n"
content += "'Fake' : {    \n"
content += "    'N' : '" + str(NfakeRaw).replace(".0","") + "',    \n"  
content += "    'alpha' : '" + str(round_sigfigs(alphaFake,4)) + "',    \n"
content += "        },    \n"
content += "    }    \n"
content += "\n"  
content += "\n"  
content += "\n"  
content += "background_systematics = {    \n"
content += "    'Elec' : {     \n" 
content += "    'value' : '" + str(round_sigfigs(1.0 + systFracElec,3)) + "',    \n"
content += "                 },   \n"
content += "    'Muon' : {   \n"
content += "    'value' : '" + str(round_sigfigs(1.0 + systFracMuon,3)) + "',    \n"
content += "                 },   \n"
content += "    'Tau' : {   \n"
content += "    'value' : '" + str(round_sigfigs(1.0 + systFracTau,3)) + "',    \n"
content += "                 },   \n"
content += "    'Fake' : {   \n"
content += "    'value' : '" + str(round_sigfigs(1.0 + systFracFake,3)) + "',    \n"
content += "                 },   \n"
content += "\n"
content += "\n"
content += "    }    \n"
content += "\n"  
content += "\n"  


fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"




outputFile = "tables/bkgdSumm.tex" 
fout = open (outputFile, "w")

# Calculate upper limit with stat and systematic errors, using Cousins/Highland, NIM A320, 331 (1992). http://www.sciencedirect.com/science/article/pii/0168900292907945.
# Eqn 21:  Un = Un0 * (1 + (Un0 - n) * syst^2 / 2)
NelecSyst = NelecErr * (1.0 + (NelecErr) * math.pow(systFracElec,2)/2.0)  
NtauSyst  = NtauErr  * (1.0 + (NtauErr)  * math.pow(systFracElec,2)/2.0)  

#NelecSyst = NelecErr * systFracElec
NmuonSyst = Nmuon    * systFracMuon
#NtauSyst  = NtauErr  * systFracTau
NfakeSyst = Nfake    * systFracFake
Ntot = Nelec + Nmuon + Ntau + Nfake
NtotStat = math.sqrt(math.pow(NelecErr,2)  + math.pow(NmuonErr,2) + math.pow(NtauErr,2) + math.pow(NfakeErr,2))
NtotSyst = math.sqrt(math.pow(NelecSyst,2) + math.pow(NmuonSyst,2) + math.pow(NtauSyst,2) + math.pow(NfakeSyst,2))
NtotErr  = math.sqrt(math.pow(NtotStat,2)  + math.pow(NtotSyst,2))   

(NData, NDataErr) = getYield("MET", fullSelectionDir, "FullSelection")

# Account for the rounding of Ntau:  
NtauErrRounded = round_sigfigs(NtauErr,2)
Ntau = modifyByPrecision(Ntau, NtauErr, NtauErrRounded)

content  = header
content += "\\begin{tabular}{lccc} \n"
content += hline
content += hline
content += "Event source    &  \\multicolumn{2}{c}{Yield}                  \\\\ \n"  
content += hline
content += "electrons      & $ < " + "{:0.2f}".format(NelecErr) + "_{\\rm stat}$  & $ < " + "{:0.2f}".format(NelecSyst) + "_{\\rm stat+syst} $ \\\\  \n"  
content += "muons          & \\multicolumn{2}{c}{$" + "{:0.2f}".format(Nmuon) + "(^{+" + "{:0.2f}".format(NmuonErrUp) + "}_{-" + "{:0.2f}".format(NmuonErrDn) + "})_{\\rm stat}  \\pm " + "{:0.2f}".format(NmuonSyst) + "_{\\rm syst} $ }  \\\\  \n"
content += "taus           & $ < " + "{:0.2f}".format(NtauErr) + "_{\\rm stat} $ & $ < " + "{:0.2f}".format(NtauSyst) + "_{\\rm stat+syst} $ \\\\  \n"
content += "fake tracks    & \\multicolumn{2}{c}{$" + "{:0.2f}".format(Nfake) + "(^{+" + "{:0.2f}".format(NfakeErrUp) + "}_{-" + "{:0.2f}".format(NfakeErrDn) + "})_{\\rm stat}  \\pm " + "{:0.2f}".format(NfakeSyst) + "_{\\rm syst}   $ }  \\\\  \n" 
content += hline
## from toyUpperLimitsBkgdSum import * 
## line = getBkgdSummLineForTable()
## content += line  
## content += hline
content += "data           & \\multicolumn{2}{c}{ $ " + str(round_sigfigs(NData, 1)).rstrip("0").rstrip(".") + " $ }  \\\\ \n"
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

(NPreselData, NPreselDataErr) = getYield("MET", preselDir, "PreSelection")
(NEcaloData,  NEcaloDataErr)  = getYield("MET", ctrlEcaloDir, "PreSelCtrlEcalo")
(NNmissData,  NNmissDataErr)  = getYield("MET", ctrlNMissDir, "PreSelCtrlNMiss")

(NPreselEst, NPreselEstErr) = getNumEvents("Background", bkgdFromDataPreselDir, "PreSelection")
(NEcaloEst,  NEcaloEstErr)  = getNumEvents("Background", ctrlEcaloDir, "PreSelCtrlEcalo")
(NNmissEst,  NNmissEstErr)  = getNumEvents("Background", ctrlNMissDir, "PreSelCtrlNMiss")

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
content += "sample                                  &  data   &  estimate  & data/estimate  \\\\ \n"  
content += hline
content += "\\candtrk sample           & " + str(NPreselData).rstrip("0").rstrip(".") + " & $" + str(round_sigfigs(NPreselEst,3)) + " \\pm " + str(round_sigfigs(NPreselEstErr,2)) + "$ & $" + "{:0.2f}".format(ratioPresel) + " \\pm  " + "{:0.2f}".format(ratioPreselErr) + "$ \\\\ \n"
content += "\\calotot sideband sample  & " + str(NEcaloData).rstrip("0").rstrip(".")  + " & $" + str(round_sigfigs(NEcaloEst,4))  + " \\pm " + str(round_sigfigs(NEcaloEstErr,2))  + "$ & $" + "{:0.2f}".format(ratioEcalo)  + " \\pm  " + "{:0.2f}".format(ratioEcaloErr)  + "$ \\\\  \n"
content += "\\Nmissout sideband sample & " + str(NNmissData).rstrip("0").rstrip(".")  + " & $" + str(round_sigfigs(NNmissEst,4))  + " \\pm " + str(round_sigfigs(NNmissEstErr,2))  + "$ & $" + "{:0.2f}".format(ratioNmiss)  + " \\pm  " + "{:0.2f}".format(ratioNmissErr)  + "$ \\\\  \n"
content += hline
content += hline
content += "\\end{tabular} \\\\  \n"
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"




###################################################
# Bkgd contribution table 
# tables/trackGenMatchBkgd
###################################################
outputFile = "tables/trackGenMatchBkgd.tex"
fout = open (outputFile, "w")

(Nelec, NelecErr) = getYield("Background", preselIdDir, "PreSelIdElec")
(Nmuon, NmuonErr) = getYield("Background", preselIdDir, "PreSelIdMuon")
(Ntau,  NtauErr)  = getYield("Background", preselIdDir, "PreSelIdTau")
(Nothr, NothrErr) = getYield("Background", preselIdDir, "PreSelIdOther")
(Nfake, NfakeErr) = getYield("Background", preselIdDir, "PreSelIdFake")

Nhad = Ntau + Nothr
Ntot = Nelec + Nmuon + Nhad + Nfake
percentelec = float(Nelec) / Ntot * 100
percentmuon = float(Nmuon) / Ntot * 100
percenthad  = float(Nhad)  / Ntot * 100 
percentfake = float(Nfake) / Ntot * 100 
percenttau  = float(Ntau)  / Ntot * 100 
percentothr = float(Nothr) / Ntot * 100 

content  = header
content += "\\begin{tabular}{lccc} \n"
content += hline
content += hline
content += "source                            & contribution \\\\   \n"  
content += hline
content += "electrons   & " + str(round_sigfigs(percentelec,2)).replace(".0","") + "\\%  \\\\  \n"
content += "muons       & " + str(round_sigfigs(percentmuon,2)).replace(".0","") + "\\%  \\\\  \n"  
content += "hadrons     & " + str(round_sigfigs(percenthad, 2)).replace(".0","") + "\\%  \\\\  \n"  
content += "fake tracks & " + str(round_sigfigs(percentfake,1)).replace(".0","") + "\\%  \\\\  \n"  
content += "% tau       & " + str(round_sigfigs(percenttau, 2)).replace(".0","") + "\\%  \\\\  \n"  
content += "% other had & " + str(round_sigfigs(percentothr,2)).replace(".0","") + "\\%  \\\\  \n"  
content += hline
content += hline
content += "\\end{tabular}\n"
fout.write(content)
fout.close()
os.system("cat " + outputFile)
print "Finished writing " + outputFile + "\n\n\n"



###################################################
# SM Bkgd table
# tables/smBkgd
###################################################
outputFile = "tables/smBkgd.tex"
fout = open (outputFile, "w")
content  = header
content += "\\begin{tabular}{llll}\n"
content += hline
content += hline
content += "& electrons & muons & taus \\\\ \n"
content += hline
content += "criteria removed to   & $\Pe$ veto & $\Pgm$ veto & $\Pgt$ veto \\\\ \n" 
content += "select control sample  & $\calotot < 10\GeV$ &            & $\calotot < 10\GeV$\\\\ \n"
content += hline
content += "$N^{i}_\\text{ctrl}$ from data & $" + str(round_sigfigs(NeCtrl,5)).replace(".0","")  +  "$ & $" + str(round_sigfigs(NmuCtrl,5)).replace(".0","")  +  "$  & $" + str(round_sigfigs(NtauCtrl,5)).replace(".0","")  +  "$ \\\\ \n"
content += "$P^{i}$ from simulation & $<" + str(round_sigfigs(PElecErr * 1e5,2))+ "\\times 10^{-5}"  +  "$ & $" + str(round_sigfigs(PMuon * 1e4,2)) + " (^{+" + str(round_sigfigs(PMuonErrUp * 1e4,3)) + "}_{-" + str(round_sigfigs(PMuonErrDown * 1e4,2)) + "}) \\times 10^{-4} " +  "$  & $<" + str(round_sigfigs(PTauErr,2))  +  "$ \\\\ \n"
content += "$N^{i} = N^{i}_\\text{ctrl} P^{i} $ & $<" + str(round_sigfigs(NelecErrSM,2))  +  "_\\text{stat}$ & $" + str(round_sigfigs(NmuonSM,2)) + " (^{+" + str(round_sigfigs(NMuonErrorUpSM,3)) + "}_{-" + str(round_sigfigs(NMuonErrorDownSM,2)) +  "})_\\text{stat} $  & $<" + str(round_sigfigs(NtauErrSM,2))  +  "_\\text{stat}$ \\\\ \n"
content += "$P^{i}$ systematic uncertainty  & $"  + str(round_sigfigs(systFracElec * 1.e2,2)).rstrip("0").rstrip(".") +"$\% & $" + str(round_sigfigs(systFracMuon * 1.e2,2)).rstrip("0").rstrip(".") +  "$\% & $" + str(round_sigfigs(systFracTau  * 1.e2,2)).rstrip("0").rstrip(".")  +  "\%$ \\\\ \n"
content += "$N^{i}$  & $<" + str(round_sigfigs(NelecSyst,2))  +  "0_\\text{stat+syst}$ & $" + str(round_sigfigs(NmuonSM,2)) + " (^{+" + str(round_sigfigs(NMuonErrorUpSM,3)) + "}_{-" + str(round_sigfigs(NMuonErrorDownSM,2)) + "})_\\text{stat} \pm" + str(round_sigfigs(NmuonSyst,2)) +  "_\\text{syst}$  & $<" + str(round_sigfigs(NtauSyst,2))  +  "_\\text{stat+syst}$ \\\\ \n"
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
print "scp tables/*tex wulsin@lxplus5.cern.ch:/afs/cern.ch/user/w/wulsin/docs/cmsdocs/notes/AN-12-400/trunk/tables/"
print "OR: "
print "notes/AN-12-400/trunk> scp wulsin@cms-in0.mps.ohio-state.edu:\"~/workdirTemplateDisTrk/tables/*tex\" tables/" 
print "scp tables/*tex jbrinson@lxplus5.cern.ch:/afs/cern.ch/user/j/jbrinson/myDir/notes/AN-12-400/trunk/tables/"




