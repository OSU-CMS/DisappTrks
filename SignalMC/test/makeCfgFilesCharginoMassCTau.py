#!/usr/bin/env python

# For usage instructions, see:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/DisappearingTracksSearch2012Recipes#Set_up_signal_MC_generation
#
# Usage:
# DisappTrks/SignalMC/test > makeCfgFilesCharginoMassCTau.py 
# DisappTrks/SignalMC/test > multicrab -create -cfg multicrabAuto.cfg 2>&1 | tee multicrabCreate.log



templateFile         = "../python/AMSB_chargino_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU.py"
templateFileNoFilter = "../python/AMSB_chargino_NoFilter_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU.py"

fin = open(templateFile, "r")

configTemplate = fin.read()
fin.close()

mass = [
    100,
    200,
    300,
    400,
    500,
    600
]

ctau = [
    10,
    100, 
    1000
]

massNoFilter = [
    200,
    500,
]

massSystISR = [
    ## "75K",
    ## "150K",
    ]
    

fMult = open("multicrabAuto.cfg", "w")  
fMult.write("[MULTICRAB]\n")  
fMult.write("cfg=crab_AMSB_chargino.cfg\n\n")  
fMult.write("[COMMON]\n\n")  
fMult.write("\n")  
    
cfgDir = "../python/"
version = "_8TeV_pythia6_V1"

def makeOneConfig(newCfg, fMult, m, t):
    fnew = open(newCfg, "w")
    configNew = configTemplate
    configNew = configNew.replace("-999", str(m))
    configNew = configNew.replace("MASSPOINT", str(m))
    configNew = configNew.replace("LIFETIME", str(t))        
    fnew.write(configNew)
    fnew.close()  
    name = newCfg.replace("_GEN-SIM-RECO.py", "") 
    name = name.replace("../python/", "")  
    fMult.write("[" + name + "]\n")  
    fMult.write("CMSSW.pset = " + newCfg + "\n")  
    fMult.write("USER.publish_data_name = " + name + version + "\n\n")
    print "Created new config file:  " + newCfg  
    

for m in mass:
    for t in ctau:
        newCfg = cfgDir + "AMSB_chargino_" + str(m) + "GeV_ctau" + str(t) + "cm_GEN-SIM-RECO.py"
        makeOneConfig(newCfg, fMult, m, t)  
        if m in massNoFilter:
            newCfg = cfgDir + "AMSB_chargino_NoFilter_" + str(m) + "GeV_ctau" + str(t) + "cm_GEN-SIM-RECO.py"
            makeOneConfig(newCfg, fMult, m, t)  
        
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



        
