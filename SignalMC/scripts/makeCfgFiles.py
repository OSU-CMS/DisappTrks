#!/usr/bin/env python

# For usage instructions, see:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/DisappearingTracksSearch2012Recipes#Set_up_signal_MC_generation
#
# Usage:
# /afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/test > ../scripts/makeCfgFiles.py 
# > multicrab -create -cfg multicrabAuto.cfg 2>&1 | tee multicrabCreate.log

import os 


#templateFile = "AMSB_charginoXXXGeV_YYYctau_8TeV_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU.py"  # Standard
templateFile = "AMSB_charginoXXXGeV_YYYctau_8TeV_pythia6_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO.py"  # Testing only!

fin = open(templateFile, "r")

configTemplate = fin.read()
fin.close()

masses = [
    200, 
    ]

ctaus = [
    1, 
    10,
    30, 
    100,
    1000,    
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

cfgDir = os.environ['CMSSW_BASE']+"/src/DisappTrks/SignalMC/python/"
version = "_8TeV_pythia6_V1"

for m in masses:
    for ctau in ctaus:
        newCfg = cfgDir + "AMSB_chargino" + str(m) + "GeV_" + str(ctau) + "ctau_8TeV_pythia6_GEN_SIM_RECO.py"  
        fnew = open(newCfg, "w")
        configNew = configTemplate
        configNew = configNew.replace("XXX", str(m))
        configNew = configNew.replace("YYY", str(ctau))        
        # Set the ctau of decaying particles to be 10 times larger than the ctau of the chargino:  
        # Note that the units of PARJ(71) are mm, not cm, so this gives an additional factor of 10.  
        configNew = configNew.replace("PARJ(71)=10 .  ! for which ctau  10 mm", "PARJ(71)=" + str(100*ctau) + " .  ! for which ctau  " + str(100*ctau) + " mm") 
        fnew.write(configNew)
        fnew.close()  
        print "Wrote file " + newCfg  
        fMult.write("[AMSB_chargino" + str(m) + "GeV_" + str(ctau) + "ctau]\n")  
        fMult.write("CMSSW.pset = " + newCfg + "\n")  
        fMult.write("USER.publish_data_name = AMSB_chargino" + str(m) + "_" + str(ctau) + "ctau" + version + "\n\n")  

        # Need to fix this if using the TuneZ2Star UE settings, since default PARP(64) is 1, and it is not included by default in the settings.  
        if m in massSystISR:
            newCfgSystISRUp = newCfg.replace("AMSB", "AMSB_SystISRUp")
            newCfgSystISRDn = newCfg.replace("AMSB", "AMSB_SystISRDn")
            fnew = open(newCfgSystISRUp, "w")
            configNewSyst = configNew  
            configNewSyst = configNewSyst.replace("PARP(64)=0.2", "PARP(64)=0.4")  
            fnew.write(configNewSyst)
            fnew.close() 
            fMult.write("[AMSBSystISRUp_chargino" + str(m) + "_" + str(ctau) + "ctau]\n")  
            fMult.write("CMSSW.pset = " + newCfgSystISRUp + "\n")  
            fMult.write("USER.publish_data_name = AMSBSystISRUp_chargino" + str(m) + "_" + str(ctau) + "ctau" + version + "\n\n")  
            fnew = open(newCfgSystISRDn, "w")
            configNewSyst = configNew
            configNewSyst = configNewSyst.replace("PARP(64)=0.2", "PARP(64)=0.1")  
            fnew.write(configNewSyst)
            fnew.close() 
            fMult.write("[AMSBSystISRDn_chargino" + str(m) + "_" + str(ctau) + "ctau]\n")  
            fMult.write("CMSSW.pset = " + newCfgSystISRDn + "\n")  
            fMult.write("USER.publish_data_name = AMSBSystISRDn_chargino" + str(m) + "_" + str(ctau) + "ctau" + version + "\n\n")  

fMult.close()  
print "Wrote file multicrabAuto.cfg"   

print "Finished makeCfgFiles.py"  

        
