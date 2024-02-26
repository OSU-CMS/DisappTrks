import os
import sys
from os.path import exists

def mergeHistos(inpPath, inpFile, outFile):

    if exists(outFile + "1.root"): os.system("rm " + outFile + "1.root")
    if exists(outFile + "2.root"): os.system("rm " + outFile + "2.root")
    if exists(outFile + "3.root"): os.system("rm " + outFile + "3.root")
    if exists(outFile + "4.root"): os.system("rm " + outFile + "4.root")
    if exists(outFile + "5.root"): os.system("rm " + outFile + "5.root")
    if exists(outFile + "6.root"): os.system("rm " + outFile + "6.root")
    if exists(outFile + ".root"): os.system("rm " + outFile + ".root")

    os.system("ls " + inpPath + "*.root > " + inpFile)

    # Using readlines()
    file1 = open(inpFile, 'r')
    Lines = file1.readlines()

    histos = ''
    histos2 = ''
    histos3 = ''
    histos4 = ''
    histos5 = ''
    histos6 = ''

    n = 0

    # Strips the newline character
    print(len(Lines))
    for line in Lines:
        if n < int(len(Lines)/6): histos += line.strip()+' '
        else:
            if n >= int(len(Lines)/6) and n < int((2*len(Lines))/6): histos2 += line.strip()+' '
            else:
                if n >= int(2*len(Lines)/6) and n < int((3*len(Lines))/6): histos3 += line.strip()+' '
                else:
                    if n >= int(3*len(Lines)/6) and n < int((4*len(Lines))/6): histos4 += line.strip()+' '
                    else:
                        if n >= int(4*len(Lines)/6) and n < int((5*len(Lines))/6): histos5 += line.strip()+' '
                        else: histos6 += line.strip()+' '
        n = n + 1

    os.system("hadd -k -j 8 " + outFile + "1.root " + histos)
    os.system("hadd -k -j 8 " + outFile + "2.root " + histos2)
    os.system("hadd -k -j 8 " + outFile + "3.root " + histos3)
    os.system("hadd -k -j 8 " + outFile + "4.root " + histos4)
    os.system("hadd -k -j 8 " + outFile + "5.root " + histos5)
    os.system("hadd -k -j 8 " + outFile + "6.root " + histos6)
    os.system("hadd -k -j 8 " + outFile + ".root " + outFile + "1.root " + outFile + "2.root " + outFile + "3.root " + outFile + "4.root " + outFile + "5.root " + outFile + "6.root ")

    if exists(outFile + "1.root"): os.system("rm " + outFile + "1.root")
    if exists(outFile + "2.root"): os.system("rm " + outFile + "2.root")
    if exists(outFile + "3.root"): os.system("rm " + outFile + "3.root")
    if exists(outFile + "4.root"): os.system("rm " + outFile + "4.root")
    if exists(outFile + "5.root"): os.system("rm " + outFile + "5.root")
    if exists(outFile + "6.root"): os.system("rm " + outFile + "6.root")

# processTypes = [""]
# processTypes = ["_ElecOnly"]
processTypes = ["_MuOnly"]
# processTypes = ["_ElecOnly","_MuOnly"]

hasCutFlow = True
# hasCutFlow = False

# processNames = ["QCD_PT300to470_PostEE"]
# processNames = ["QCD_PT2400to3200_PostEE"]
# processNames = ["QCD_PT300to470_PostEE","QCD_PT470to600_PostEE","QCD_PT600to800_PostEE","QCD_PT800to1000_PostEE","QCD_PT1000to1400_PostEE","QCD_PT1400to1800_PostEE","QCD_PT1800to2400_PostEE","QCD_PT2400to3200_PostEE"]
# processNames = ["Zto2Nu_4Jets_HT100to200_PostEE","Zto2Nu_4Jets_HT200to400_PostEE","Zto2Nu_4Jets_HT400to800_PostEE","Zto2Nu_4Jets_HT800to1500_PostEE","Zto2Nu_4Jets_HT1500to2500_PostEE"]
# processNames = ["DYJetsToLL_M50_PostEE_ZMuMuCR"]
processNames = ["WtoMuNu_M100to200","WtoMuNu_M200to500","WtoMuNu_M500to1000"]

for processName in processNames:
    for processType in processTypes:

        inpPath = ""
        inpFile = ""
        outFile = ""

        if hasCutFlow: inpPath = "condor/BGMC/Run3/2022/Cutflows_" + processName + processType + "/"
        else: inpPath = "condor/BGMC/Run3/2022/" + processName + "/" + processName + "/"
        inpFile = "histos_" + processName + processType + ".txt"
        outFile = "hist_merged_" + processName + processType

        print(inpPath)
        print(inpFile)
        print(outFile)

        mergeHistos(inpPath,inpFile,outFile)