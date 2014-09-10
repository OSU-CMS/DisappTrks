#!/usr/bin/env python
#
# Creates needed slha files for pMSSM signal MC production
# 
# Usage:
# /afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/signalMCGenV3/CMSSW_5_3_11/src/DisappTrks/SignalMC/test/
# > ../scripts/makeCfgFiles_pMSSM.py 

# Copied from makeSlhaFiles.py and makeCfgFilesCharginoMassCTau.py 


import sys
import re


from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--outputName", dest="outputName", default="multicrabPMSSM.cfg", 
                  help="name of output multicrab.cfg file")
(arguments, args) = parser.parse_args()


def getTau(ctau):
    c = 2.99792e1       # cm / ns    
    tau = ctau / c
    return tau

def getWidth(ctau):  
    hbar = 6.58212e-16  # GeV * ns
    tau = getTau(ctau)
    width = hbar / tau
    return width

fMult = open(arguments.outputName, "w")  
fMult.write("[MULTICRAB]\n")  
fMult.write("cfg=crab_AMSB_chargino.cfg\n\n")  
fMult.write("[COMMON]\n\n")  
fMult.write("\n")  


infiles = [
    'pMSSM_328267_chargino100GeV_ctau10cm.slha',   
    'pMSSM_376273_chargino100GeV_ctau30cm.slha',    
    'pMSSM_237489_chargino100GeV_ctau50cm.slha',    
    'pMSSM_438262_chargino100GeV_ctau70cm.slha',    
    'pMSSM_949614_chargino100GeV_ctau91cm.slha',    
    'pMSSM_903606_chargino100GeV_ctau102cm.slha',    
    'pMSSM_579494_chargino100GeV_ctau291cm.slha',    
    'pMSSM_563866_chargino100GeV_ctau509cm.slha',    
    'pMSSM_362332_chargino100GeV_ctau736cm.slha',    
    'pMSSM_879480_chargino100GeV_ctau912cm.slha',    
    'pMSSM_878818_chargino100GeV_ctau1039cm.slha',    
    'pMSSM_192500_chargino700GeV_ctau10cm.slha',    
    'pMSSM_582920_chargino700GeV_ctau30cm.slha',    
    'pMSSM_322298_chargino700GeV_ctau49cm.slha',    
    'pMSSM_622291_chargino700GeV_ctau70cm.slha',    
    'pMSSM_191750_chargino700GeV_ctau89cm.slha',    
    'pMSSM_298525_chargino700GeV_ctau100cm.slha',    
    'pMSSM_525996_chargino700GeV_ctau373cm.slha',    
    'pMSSM_422212_chargino700GeV_ctau466cm.slha',    
    'pMSSM_757185_chargino700GeV_ctau537cm.slha',  
    ]

baseDir = "../data/"  
cfgDir = "../python/"
version = "_8TeV_pythia6_V1"


for infile in infiles:
    # First make the base slha files, i.e., comment out the chargino decay
    infile = baseDir + infile 
    newName = infile.replace(".slha", "_noChiDecay.slha") 
    fnew = open(newName, "w")
    fin = open(infile, "r")  
    inCharginoDecayBlock = False
    inMassBlock = False
    for line in fin:
        if "DECAY" in line and "1000024" in line:
            inCharginoDecayBlock = True
        elif "DECAY" in line and inCharginoDecayBlock:
            inCharginoDecayBlock = False
        if "BLOCK" in line and "MASS" in line:
            inMassBlock = True
        elif "DECAY" in line and inMassBlock:
            inMassBlock = False
        if inCharginoDecayBlock:
            line = "#" + line
        if inMassBlock and "1000024" in line:
            words = line.split()
            mChargino = float(words[1])
        if inMassBlock and "1000022" in line:
            words = line.split()
            mNeutralino = float(words[1])
        fnew.write(line)  
    fnew.close()
    print "Finished writing file " + newName + " from " + infile + " in dir: " + baseDir  

    mass     = re.sub (r".*_chargino(.*)GeV_ctau.*", r"\1", infile)    
    ctau     = re.sub (r".*GeV_ctau(.*)cm.*",        r"\1", infile)
    pMSSMIdx = re.sub (r".*pMSSM_(.*)_chargino.*",   r"\1", infile)
    print "ctau = ", ctau, ", mass = ", mass, ", pMSSMIdx = ", pMSSMIdx    

    #    sys.exit(0)
    
    # Now make the geant4 file
    
    text  = "# This file is read by SimG4Core/CustomPhysics/src/CustomParticleFactory.cc  \n"
    text += '# The strings "decay", "pdg code", and "block", with correct capitalization, are used \n'
    text += "# to control the data input, so do not use these in any comments.  \n"
    text += "# \n"
    text += "# \n"
    text += "# Get values for chargino and neutralino masses from:  \n"
    text += "# " + infile + "\n"  
    text += "BLOCK MASS   \n" 
    text += "#  PDG code   mass   particle \n"
    text += "   1000022   " + str(mNeutralino) + "   # ~neutralino(1) \n"
    text += "   1000024   " + str(mChargino)   + "   # ~chargino(1)+  \n"
    text += "  -1000024   " + str(mChargino)   + "   # ~chargino(1)-  \n"
    text += "Block \n"
    text += "\n"
    text += "\n"
    text += "\n"
    
    width = getWidth(float(ctau))  
    text += "# Set chargino lifetime \n"
    text += "# and decay:  chargino -> neutralino + pion \n"  
    text += "# chargino ctau  = " + str(ctau) + " cm \n"
    text += "# chargino  tau  = " + str(getTau(float(ctau))) + " ns \n"    
    text += "# chargino width = " + str(width) + " GeV \n"    
    text += "#       PDG       Width               #\n"
    text += "DECAY  1000024  " + str(width) + " # +chargino decay  \n"  
    text += "#   BR       NDA      ID1      ID2  \n"
    text += "   1.0000    2     1000022    211   \n"
    text += "Block \n"  
    text += "\n"  
    text += "\n"  
    text += "#       PDG       Width               #\n"
    text += "DECAY  -1000024  " + str(width) + " # -chargino decay  \n"  
    text += "#   BR       NDA      ID1      ID2  \n"
    text += "   1.0000    2     1000022    -211  \n"
    text += "Block \n"  
    newName = infile.replace(".slha", "_geant4.slha") 
    fnew = open(newName, "w") 
    fnew.write(text)  
    fnew.close()
    print "Finished writing file " + newName 

    # Now make python config files
    newCfg = cfgDir + "pMSSM_" + pMSSMIdx + "_chargino_" + mass + "GeV_ctau" + ctau + "cm_GEN-SIM-RECO.py"    
    fnew = open(newCfg, "w")
    fin = open("../python/AMSB_chargino_NoFilter_cfi_py_GEN_SIM_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_RECO_PU.py", "r")
    configNew = "" 
    for line in fin:
        if "particleFile" in line:
            myfile = infile.replace(".slha", "_geant4.slha").replace("../data/", "") 
            line = "    particleFile = cms.untracked.string('DisappTrks/SignalMC/data/" + myfile + "'), \n" 
        elif "slhaFile" in line:
            myfile = infile.replace(".slha", "_noChiDecay.slha").replace("../data/", "")
            line = "    slhaFile = cms.untracked.string('DisappTrks/SignalMC/data/" + myfile + "'), \n"
        elif "SLHAFILE" in line:
            myfile = infile.replace(".slha", "_noChiDecay.slha").replace("../data/", "")
            line = "        SLHAParameters = cms.vstring('SLHAFILE = DisappTrks/SignalMC/data/" + myfile + "') \n"
        elif "massPoint" in line:
            line = "    massPoint = cms.untracked.int32(" + mass + "), \n"   
        configNew += line
    fnew.write(configNew)
    fnew.close()  
    print "Created new config file:  " + newCfg  
    name = newCfg.replace("_GEN-SIM-RECO.py", "") 
    name = name.replace("../python/", "")  
    fMult.write("[" + name + "]\n")  
    fMult.write("CMSSW.pset = " + newCfg + "\n")  
    fMult.write("USER.publish_data_name = " + name + version + "\n\n")


    
print "Finished making all slha and python config files"  
print "Finished writing multicrab config file: " + arguments.outputName 



        


        
