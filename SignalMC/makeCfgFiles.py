#!/usr/bin/env python

# For usage instructions, see:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/DisappearingTracksSearch2012Recipes#Set_up_signal_MC_generation
#
# Usage:
# /afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC > makeCfgFiles.py 
# > multicrab -create -cfg multicrabAuto.cfg 2>&1 | tee multicrabCreate.log



templateFile = "amsb_mGravXXX_YYYns_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU.py"

fin = open(templateFile, "r")

configTemplate = fin.read()
fin.close()

mass = [
    ## "32K",
    ## "50K",
    "75K",
    ## "100K",
    ## "125K",
    "150K",
    ]

tau = [
    "0p5",
    "1",
    "5",
    ]

massSystISR = [
    "75K",
    "150K",
    ]
    
fMult = open("multicrabAuto.cfg", "w")  
fMult.write("[MULTICRAB]\n")  
fMult.write("cfg=cfg/crabMC_amsbChargino.cfg\n\n")  
fMult.write("[COMMON]\n\n")  
fMult.write("\n")  

cfgDir = "cfg/"
version = "_8TeV_pythia6_V1"

for m in mass:
    for t in tau:
        newCfg = cfgDir + "amsbChargino_mGrav" + m + "_" + t + "ns_GEN-SIM-RECO.py"
        fnew = open(newCfg, "w")
        configNew = configTemplate
        configNew = configNew.replace("XXX", m)
        configNew = configNew.replace("YYY", t)        
        fnew.write(configNew)
        fnew.close()  
        fMult.write("[AMSBChargino_mGrav" + m + "_" + t + "ns]\n")  
        fMult.write("CMSSW.pset = " + newCfg + "\n")  
        fMult.write("USER.publish_data_name = AMSBChargino_mGrav" + m + "_" + t + "ns" + version + "\n\n")

        if m in massSystISR:
            newCfgSystISRUp = newCfg.replace("Chargino", "Chargino_SystISRUp")
            newCfgSystISRDn = newCfg.replace("Chargino", "Chargino_SystISRDn")
            fnew = open(newCfgSystISRUp, "w")
            configNewSyst = configNew  
            configNewSyst = configNewSyst.replace("PARP(64)=0.2", "PARP(64)=0.4")  
            fnew.write(configNewSyst)
            fnew.close() 
            fMult.write("[AMSBChargino_SystISRUp_mGrav" + m + "_" + t + "ns]\n")  
            fMult.write("CMSSW.pset = " + newCfgSystISRUp + "\n")  
            fMult.write("USER.publish_data_name = AMSBChargino_SystISRUp_mGrav" + m + "_" + t + "ns" + version + "\n\n")
            fnew = open(newCfgSystISRDn, "w")
            configNewSyst = configNew
            configNewSyst = configNewSyst.replace("PARP(64)=0.2", "PARP(64)=0.1")  
            fnew.write(configNewSyst)
            fnew.close() 
            fMult.write("[AMSBChargino_SystISRDn_mGrav" + m + "_" + t + "ns]\n")  
            fMult.write("CMSSW.pset = " + newCfgSystISRDn + "\n")  
            fMult.write("USER.publish_data_name = AMSBChargino_SystISRDn_mGrav" + m + "_" + t + "ns" + version + "\n\n")

fMult.close()  



        
