#!/usr/bin/env python

# For usage instructions, see:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/DisappearingTracksSearch2012Recipes#Set_up_signal_MC_generation
#
# Usage:
# DisappTrks/SignalMC/test > ../scripts/makeCfgFilesCharginoMassCTau.py -o multicrabNew.cfg -c 
# DisappTrks/SignalMC/test > multicrab -create -cfg multicrabNew.cfg 2>&1 | tee multicrabCreate.log

from optparse import OptionParser


parser = OptionParser()
parser.add_option("-o", "--outputName", dest="outputName", default="multicrab.cfg", 
                  help="name of output multicrab.cfg file")
parser.add_option("-c", "--createConfigs", action="store_true", dest="createConfigs", default=False,
                  help="create config files; default is to create multicrab files only")
parser.add_option("-n", "--noFilterOnly", action="store_true", dest="noFilterOnly", default=False,
                  help="only create the NoFilter jobs; default is to create Filter and NoFilter jobs")
(arguments, args) = parser.parse_args()



templateFileFilter   = "../python/AMSB_chargino_FilterSumPt50_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU.py"
templateFileNoFilter = "../python/AMSB_chargino_NoFilter_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU.py"

fin = open(templateFileFilter, "r")
configTemplateFilter = fin.read()
fin.close()

fin = open(templateFileNoFilter, "r")
configTemplateNoFilter = fin.read()
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
    30,
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
    

multicrabFilterEffName = arguments.outputName.replace(".cfg", "_FilterEff.cfg")  
fMult = open(arguments.outputName, "w")  
fMEff = open(multicrabFilterEffName, "w")  
fMult.write("[MULTICRAB]\n")  
fMEff.write("[MULTICRAB]\n")  
fMult.write("cfg=crab_AMSB_chargino.cfg\n\n")  
fMEff.write("cfg=crab_FilterEff.cfg\n\n")  
fMult.write("[COMMON]\n\n")  
fMult.write("\n")  
fMEff.write("# Get dataset names from DAS search; add them here by hand \n\n")  
    
cfgDir = "../python/"
version = "_8TeV_pythia6_V1"

def makeOneConfig(newCfg, cfgTemplate, fMult, fMEff, m, t):
    if arguments.createConfigs: 
        fnew = open(newCfg, "w")
        configNew = cfgTemplate
        configNew = configNew.replace("-999", str(m))
        configNew = configNew.replace("MASSPOINT", str(m))
        configNew = configNew.replace("LIFETIME", str(t))        
        fnew.write(configNew)
        fnew.close()  
        print "Created new config file:  " + newCfg  
    name = newCfg.replace("_GEN-SIM-RECO.py", "") 
    name = name.replace("../python/", "")  
    fMult.write("[" + name + "]\n")  
    fMEff.write("[" + name + "__FilterEff]\n")  
    fMult.write("CMSSW.pset = " + newCfg + "\n")  
    fMEff.write("CMSSW.datasetpath =   \n\n")  
    fMult.write("USER.publish_data_name = " + name + version + "\n\n")
    

for m in mass:
    for t in ctau:
        if not arguments.noFilterOnly: 
            newCfg = cfgDir + "AMSB_chargino_" + str(m) + "GeV_ctau" + str(t) + "cm_FilterSumPt50_GEN-SIM-RECO.py"
            makeOneConfig(newCfg, configTemplateFilter, fMult, fMEff, m, t)  
        if m in massNoFilter:
            newCfg = cfgDir + "AMSB_chargino_" + str(m) + "GeV_ctau" + str(t) + "cm_NoFilter_GEN-SIM-RECO.py"
            makeOneConfig(newCfg, configTemplateNoFilter, fMult, fMEff, m, t)  
        
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
fMEff.close()
print "Finished writing multicrab config file: " + arguments.outputName + " and filter efficiency multicrab config: " + multicrabFilterEffName  




        
