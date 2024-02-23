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

# processName = "QCD_PT300to470_PostEE"
# processName = "QCD_PT2400to3200_PostEE"
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

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WToLNu_2Jets_postEE/WToLNu_2Jets/"
# inpFile = "histos_WToLNu_2Jets_postEE.txt"
# outFile = "hist_merged_WToLNu_2Jets_postEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WToLNu_2Jets_PostEE_ElecOnly/"
# inpFile = "histos_WToLNu_2Jets_PostEE_ElecOnly.txt"
# outFile = "hist_merged_WToLNu_2Jets_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WToLNu_2Jets_PostEE_MuOnly/"
# inpFile = "histos_WToLNu_2Jets_PostEE_MuOnly.txt"
# outFile = "hist_merged_WToLNu_2Jets_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/WToLNu_4Jets_PostEE/WToLNu_4Jets_PostEE/"
# inpFile = "histos_WToLNu_4Jets_PostEE.txt"
# outFile = "hist_merged_WToLNu_4Jets_PostEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WToLNu_4Jets_PostEE_ElecOnly/"
# inpFile = "histos_WToLNu_4Jets_PostEE_ElecOnly.txt"
# outFile = "hist_merged_WToLNu_4Jets_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WToLNu_4Jets_PostEE_MuOnly/"
# inpFile = "histos_WToLNu_4Jets_PostEE_MuOnly.txt"
# outFile = "hist_merged_WToLNu_4Jets_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/WToLNu_4Jets_PostEE_MuCR/WToLNu_4Jets_PostEE/"
# inpFile = "histos_WToLNu_4Jets_PostEE_MuCR.txt"
# outFile = "hist_merged_WToLNu_4Jets_PostEE_MuCR"

# inpPath = "condor/BGMC/Run3/2022/Muon_2022F_MuCR/Muon_2022F/"
# inpFile = "histos_Muon_2022F_MuCR.txt"
# outFile = "hist_merged_Muon_2022F_MuCR"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_DYJetsToLL_M50_postEE/DYJetsToLL_M50/"
# inpFile = "histos_DYJetsToLL_M50_postEE.txt"
# outFile = "hist_merged_DYJetsToLL_M50_postEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_DYJetsToLL_M50_PostEE_ElecOnly/"
# inpFile = "histos_DYJetsToLL_M50_PostEE_ElecOnly.txt"
# outFile = "hist_merged_DYJetsToLL_M50_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_DYJetsToLL_M50_PostEE_MuOnly/"
# inpFile = "histos_DYJetsToLL_M50_PostEE_MuOnly.txt"
# outFile = "hist_merged_DYJetsToLL_M50_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WW_postEE/WW_PostEE/"
# inpFile = "histos_WW_postEE.txt"
# outFile = "hist_merged_WW_postEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WW_PostEE_ElecOnly/"
# inpFile = "histos_WW_PostEE_ElecOnly.txt"
# outFile = "hist_merged_WW_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WW_PostEE_MuOnly/"
# inpFile = "histos_WW_PostEE_MuOnly.txt"
# outFile = "hist_merged_WW_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WZ_postEE/WZ_PostEE/"
# inpFile = "histos_WZ_postEE.txt"
# outFile = "hist_merged_WZ_postEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WZ_PostEE_ElecOnly/"
# inpFile = "histos_WZ_PostEE_ElecOnly.txt"
# outFile = "hist_merged_WZ_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_WZ_PostEE_MuOnly/"
# inpFile = "histos_WZ_PostEE_MuOnly.txt"
# outFile = "hist_merged_WZ_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_ZZ_postEE/ZZ_PostEE/"
# inpFile = "histos_ZZ_postEE.txt"
# outFile = "hist_merged_ZZ_postEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_ZZ_PostEE_ElecOnly/"
# inpFile = "histos_ZZ_PostEE_ElecOnly.txt"
# outFile = "hist_merged_ZZ_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_ZZ_PostEE_MuOnly/"
# inpFile = "histos_ZZ_PostEE_MuOnly.txt"
# outFile = "hist_merged_ZZ_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/TTto2L2Nu_postEE/TTto2L2Nu_PostEE/"
# inpFile = "histos_TTto2L2Nu_PostEE.txt"
# outFile = "hist_merged_TTto2L2Nu_PostEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_TTto2L2Nu_PostEE_ElecOnly/"
# inpFile = "histos_TTto2L2Nu_PostEE_ElecOnly.txt"
# outFile = "hist_merged_TTto2L2Nu_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_TTto2L2Nu_PostEE_MuOnly/"
# inpFile = "histos_TTto2L2Nu_PostEE_MuOnly.txt"
# outFile = "hist_merged_TTto2L2Nu_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/TTtoLNu2Q_PostEE/TTtoLNu2Q_PostEE/"
# inpFile = "histos_TTtoLNu2Q_PostEE.txt"
# outFile = "hist_merged_TTtoLNu2Q_PostEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_TTtoLNu2Q_PostEE_ElecOnly/"
# inpFile = "histos_TTtoLNu2Q_PostEE_ElecOnly.txt"
# outFile = "hist_merged_TTtoLNu2Q_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_TTtoLNu2Q_PostEE_MuOnly/"
# inpFile = "histos_TTtoLNu2Q_PostEE_MuOnly.txt"
# outFile = "hist_merged_TTtoLNu2Q_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/TTto4Q_PostEE/TTto4Q_PostEE/"
# inpFile = "histos_TTto4Q_PostEE.txt"
# outFile = "hist_merged_TTto4Q_PostEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_TTto4Q_PostEE_ElecOnly/"
# inpFile = "histos_TTto4Q_PostEE_ElecOnly.txt"
# outFile = "hist_merged_TTto4Q_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_TTto4Q_PostEE_MuOnly/"
# inpFile = "histos_TTto4Q_PostEE_MuOnly.txt"
# outFile = "hist_merged_TTto4Q_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT15to30_PostEE/QCD_PT15to30_PostEE/"
# inpFile = "histos_QCD_PT15to30_PostEE.txt"
# outFile = "hist_merged_QCD_PT15to30_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT30to50_PostEE/QCD_PT30to50_PostEE/"
# inpFile = "histos_QCD_PT30to50_PostEE.txt"
# outFile = "hist_merged_QCD_PT30to50_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT50to80_PostEE/QCD_PT50to80_PostEE/"
# inpFile = "histos_QCD_PT50to80_PostEE.txt"
# outFile = "hist_merged_QCD_PT50to80_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT80to120_PostEE/QCD_PT80to120_PostEE/"
# inpFile = "histos_QCD_PT80to120_PostEE.txt"
# outFile = "hist_merged_QCD_PT80to120_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT120to170_PostEE/QCD_PT120to170_PostEE/"
# inpFile = "histos_QCD_PT120to170_PostEE.txt"
# outFile = "hist_merged_QCD_PT120to170_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT170to300_PostEE/QCD_PT170to300_PostEE/"
# inpFile = "histos_QCD_PT170to300_PostEE.txt"
# outFile = "hist_merged_QCD_PT170to300_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT300to470_PostEE/QCD_PT300to470_PostEE/"
# inpFile = "histos_QCD_PT300to470_PostEE.txt"
# outFile = "hist_merged_QCD_PT300to470_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT470to600_PostEE/QCD_PT470to600_PostEE/"
# inpFile = "histos_QCD_PT470to600_PostEE.txt"
# outFile = "hist_merged_QCD_PT470to600_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT600to800_PostEE/QCD_PT600to800_PostEE/"
# inpFile = "histos_QCD_PT600to800_PostEE.txt"
# outFile = "hist_merged_QCD_PT600to800_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT800to1000_PostEE/QCD_PT800to1000_PostEE/"
# inpFile = "histos_QCD_PT800to1000_PostEE.txt"
# outFile = "hist_merged_QCD_PT800to1000_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT1000to1400_PostEE/QCD_PT1000to1400_PostEE/"
# inpFile = "histos_QCD_PT1000to1400_PostEE.txt"
# outFile = "hist_merged_QCD_PT1000to1400_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT1400to1800_PostEE/QCD_PT1400to1800_PostEE/"
# inpFile = "histos_QCD_PT1400to1800_PostEE.txt"
# outFile = "hist_merged_QCD_PT1400to1800_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT1800to2400_PostEE/QCD_PT1800to2400_PostEE/"
# inpFile = "histos_QCD_PT1800to2400_PostEE.txt"
# outFile = "hist_merged_QCD_PT1800to2400_PostEE"

# inpPath = "condor/BGMC/Run3/2022/QCD_PT2400to3200_PostEE/QCD_PT2400to3200_PostEE/"
# inpFile = "histos_QCD_PT2400to3200_PostEE.txt"
# outFile = "hist_merged_QCD_PT2400to3200_PostEE"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_QCD_PT80to120_PostEE_ElecOnly/"
# inpFile = "histos_QCD_PT80to120_PostEE_ElecOnly.txt"
# outFile = "hist_merged_QCD_PT80to120_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_QCD_PT120to170_PostEE_ElecOnly/"
# inpFile = "histos_QCD_PT120to170_PostEE_ElecOnly.txt"
# outFile = "hist_merged_QCD_PT120to170_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_QCD_PT170to300_PostEE_ElecOnly/"
# inpFile = "histos_QCD_PT170to300_PostEE_ElecOnly.txt"
# outFile = "hist_merged_QCD_PT170to300_PostEE_ElecOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_QCD_PT80to120_PostEE_MuOnly/"
# inpFile = "histos_QCD_PT80to120_PostEE_MuOnly.txt"
# outFile = "hist_merged_QCD_PT80to120_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_QCD_PT120to170_PostEE_MuOnly/"
# inpFile = "histos_QCD_PT120to170_PostEE_MuOnly.txt"
# outFile = "hist_merged_QCD_PT120to170_PostEE_MuOnly"

# inpPath = "condor/BGMC/Run3/2022/Cutflows_QCD_PT170to300_PostEE_MuOnly/"
# inpFile = "histos_QCD_PT170to300_PostEE_MuOnly.txt"
# outFile = "hist_merged_QCD_PT170to300_PostEE_MuOnly"

# inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_700_1000_Basic/"
# inpFile = "histos_1000_700_Basic.txt"
# outFile = "hist_merged_1000_700_Basic"

# inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_700_1000_BasicISRChangedChanged/"
# inpFile = "histos_1000_700_BasicISRChangedChanged.txt"
# outFile = "hist_merged_1000_700_BasicISR"

# inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_700_100_DisTrkNoISR/"
# inpFile = "histos_100_700_DisTrkNoISR.txt"
# outFile = "hist_merged_100_700_DisTrkNoISR"

# inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_100_100_DisTrkWiISR/"
# inpFile = "histos_100_100_DisTrkWiISR.txt"
# outFile = "hist_merged_100_100_DisTrkWiISR"

# inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_Pythia700_100_DisTrkNoISR/"
# inpFile = "histos_100_Pythia700_DisTrkNoISR.txt"
# outFile = "hist_merged_100_Pythia700_DisTrkNoISR"

# inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_700_100_DisTrkWiISR/"
# inpFile = "histos_100_700_DisTrkWiISR.txt"
# outFile = "hist_merged_100_700_DisTrkWiISR"

# inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_Pythia700_100_DisTrkWiISR/"
# inpFile = "histos_100_Pythia700_DisTrkWiISR.txt"
# outFile = "hist_merged_100_Pythia700_DisTrkWiISR"

# inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_Pythia100_100_DisTrkWiISR/"
# inpFile = "histos_100_Pythia100_DisTrkWiISR.txt"
# outFile = "hist_merged_100_Pythia100_DisTrkWiISR"

# inpPath = "condor/SignalMC/Run3/2022/CharginoValidator/100cm/Pythia50GeV/"
# inpFile = "histos_100_Pythia50.txt"
# outFile = "hist_merged_100_Pythia50"

# inpPath = "condor/SignalMC/Run3/2022/CharginoValidator/100cm/50GeV/"
# inpFile = "histos_100_50.txt"
# outFile = "hist_merged_100_50"

# inpPath = "condor/SignalMC/Run3/2022/Cutflows_AMSB_700_100_basicSelection/"
# inpFile = "histos_100_700_basicSel.txt"
# outFile = "hist_merged_100_700_basicSel"

# inpPath = "condor/SignalMC/Run3/2022/CutFlowsISR_AMSB_700_100_candidateTracksNoSkimming/"
# inpFile = "histos_CutFlowsISR_AMSB_700_100.txt"
# outFile = "hist_merged_CutFlowsISR_AMSB_700_100"

# inpPath = "condor/SignalMC/Run3/2022/CharginoValidator/100cm/TWOJETSGENONLYMG5700GeV2/TWOJETS_AMSB_chargino_M_700GeV_CTau_100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/"
# inpFile = "histos_100_TWOJETSGENONLYMadgraph7002.txt"
# outFile = "hist_merged_100_TWOJETSGENONLYMadgraph7002"

# inpPath = "condor/SignalMC/Run3/2022/CharginoValidator/100cm/GENONLYPY8700GeV2/GENONLY_PYTHIA_AMSB_chargino_M_700GeV_CTau_100cm_TuneCP5_PSweights_13p6TeV_pythia8/"
# inpFile = "histos_100_GENONLYPythia7002.txt"
# outFile = "hist_merged_100_GENONLYPythia7002"

# inpPath = "condor/SignalMC/Run3/2022/CharginoValidator/100cm/GENONLYMG5700GeV2/GENONLY_MADGRAPH_AMSB_chargino_M_700GeV_CTau_100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/"
# inpFile = "histos_100_GENONLYMadgraph7002.txt"
# outFile = "hist_merged_100_GENONLYMadgraph7002"










# if exists(outFile + "1.root"): os.system("rm " + outFile + "1.root")
# if exists(outFile + "2.root"): os.system("rm " + outFile + "2.root")
# if exists(outFile + "3.root"): os.system("rm " + outFile + "3.root")
# if exists(outFile + "4.root"): os.system("rm " + outFile + "4.root")
# if exists(outFile + "5.root"): os.system("rm " + outFile + "5.root")
# if exists(outFile + "6.root"): os.system("rm " + outFile + "6.root")
# if exists(outFile + ".root"): os.system("rm " + outFile + ".root")

# os.system("ls " + inpPath + "*.root > " + inpFile)

# # Using readlines()
# file1 = open(inpFile, 'r')
# Lines = file1.readlines()

# histos = ''
# histos2 = ''
# histos3 = ''
# histos4 = ''
# histos5 = ''
# histos6 = ''

# n = 0

# # Strips the newline character
# print(len(Lines))
# for line in Lines:
#     if n < int(len(Lines)/6): histos += line.strip()+' '
#     else:
#         if n >= int(len(Lines)/6) and n < int((2*len(Lines))/6): histos2 += line.strip()+' '
#         else:
#             if n >= int(2*len(Lines)/6) and n < int((3*len(Lines))/6): histos3 += line.strip()+' '
#             else:
#                 if n >= int(3*len(Lines)/6) and n < int((4*len(Lines))/6): histos4 += line.strip()+' '
#                 else:
#                     if n >= int(4*len(Lines)/6) and n < int((5*len(Lines))/6): histos5 += line.strip()+' '
#                     else: histos6 += line.strip()+' '
#     n = n + 1

# os.system("hadd -k -j 8 " + outFile + "1.root " + histos)
# os.system("hadd -k -j 8 " + outFile + "2.root " + histos2)
# os.system("hadd -k -j 8 " + outFile + "3.root " + histos3)
# os.system("hadd -k -j 8 " + outFile + "4.root " + histos4)
# os.system("hadd -k -j 8 " + outFile + "5.root " + histos5)
# os.system("hadd -k -j 8 " + outFile + "6.root " + histos6)
# os.system("hadd -k -j 8 " + outFile + ".root " + outFile + "1.root " + outFile + "2.root " + outFile + "3.root " + outFile + "4.root " + outFile + "5.root " + outFile + "6.root ")

# if exists(outFile + "1.root"): os.system("rm " + outFile + "1.root")
# if exists(outFile + "2.root"): os.system("rm " + outFile + "2.root")
# if exists(outFile + "3.root"): os.system("rm " + outFile + "3.root")
# if exists(outFile + "4.root"): os.system("rm " + outFile + "4.root")
# if exists(outFile + "5.root"): os.system("rm " + outFile + "5.root")
# if exists(outFile + "6.root"): os.system("rm " + outFile + "6.root")
