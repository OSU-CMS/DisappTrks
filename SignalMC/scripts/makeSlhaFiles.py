#!/usr/bin/env python
# Usage:
# /afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/signalMCGenV3/CMSSW_5_3_11/src/DisappTrks/SignalMC/test/
# > ../scripts/makeSlhaFiles.py 
# > git add ../data/geant4_AMSB_chargino_*GeV_ctau*cm.slha ../data/AMSB_chargino*ctau.slha  


import sys

from optparse import OptionParser


parser = OptionParser()
parser.add_option("-p", "--pythia", action="store_true", dest="pythia", default=False,
                                    help="create config files for running GEN jobs with chargino decay in pythia")  
(arguments, args) = parser.parse_args()



# SLHA files for each mass point must be created independently (e.g., with isajet)  
# mass of chargino in GeV
masses = [
    100, 
    200, 
    300,
    400,
    500,
    600, 
    ]

# c*lifetime of chargino in cm 
ctaus = [
    1, 
    10,
    30, 
    100,
    1000,
    ]

# Make slha stubs for ctau values  
def getTau(ctau):
    c = 2.99792e1       # cm / ns    
    tau = ctau / c
    return tau

def getWidth(ctau):  
    hbar = 6.58212e-16  # GeV * ns
    tau = getTau(ctau)
    width = hbar / tau
    return width
    

# Create template decay files for different lifetimes 
for ctau in ctaus:  
    templateCtauFile = "../data/AMSB_chargino" + str(ctau) + "ctau.slha"  
    print "Creating template file " + templateCtauFile  
    fnew = open(templateCtauFile, "w")
    width = getWidth(ctau)  
    text  = "# Set chargino lifetime \n"
    text += "# and decay:  chargino -> neutralino + pion \n"  
    text += "# chargino ctau  = " + str(ctau) + " cm \n"
    text += "# chargino  tau  = " + str(getTau(ctau)) + " ns \n"    
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
    fnew.write(text)  
    fnew.close()


# Make complete slha files for each mass, ctau point 
for m in masses:
    for ctau in ctaus:

        templateMassFile = "../data/AMSB_chargino_" + str(m) + "GeV_Isajet780.slha"  
        mChargino = -99
        mNeutralino = -99
        fin = open(templateMassFile, "r")
        for line in fin:
            if "1000022" in line:
                words = line.split()
                mNeutralino = words[1]
            if "1000024" in line:
                words = line.split()
                mChargino = words[1]
        fin.close()
        if mChargino < 0 or mNeutralino < 0:
            print "Error:  incorrect masses found for neutralino=" + str(mNeutralino) + " and chargino=" + str(mChargino)
            sys.exit(1)  
        
        templateCtauFile = "../data/AMSB_chargino" + str(ctau) + "ctau.slha"  
        fin = open(templateCtauFile, "r")
        configCtauTemplate = fin.read()
        fin.close()
        
        if arguments.pythia:
            newFile = "../data/pythiaDecay/AMSB_chargino_" + str(m) + "GeV_ctau" + str(ctau) + "cm.slha"
        else:
            newFile = "../data/geant4_AMSB_chargino_" + str(m) + "GeV_ctau" + str(ctau) + "cm.slha"
        print "Creating new file: " + newFile + " with mChargino = " + mChargino + ", mNeutralino = " + mNeutralino + ", massDiff = " + str(float(mChargino) - float(mNeutralino))   
        fnew = open(newFile, "w")
        if not arguments.pythia:
            configNew  = "# This file is read by SimG4Core/CustomPhysics/src/CustomParticleFactory.cc  \n"
            configNew += '# The strings "decay", "pdg code", and "block", with correct capitalization, are used \n'
            configNew += "# to control the data input, so do not use these in any comments.  \n"
            configNew += "# \n"
            configNew += "# \n"
            configNew += "# Get values for chargino and neutralino masses from:  \n"
            configNew += "# " + templateMassFile + "\n"  
            configNew += "BLOCK MASS   \n" 
            configNew += "#  PDG code   mass   particle \n"
            configNew += "   1000022   " + str(mNeutralino) + "   # ~neutralino(1) \n"
            configNew += "   1000024   " + str(mChargino)   + "   # ~chargino(1)+  \n"
            configNew += "  -1000024   " + str(mChargino)   + "   # ~chargino(1)-  \n"
            configNew += "Block \n"
            configNew += "\n"
            configNew += "\n"
            configNew += "\n"
        else:
            fin = open(templateMassFile, "r")
            configNew = ""
            configNew += fin.read()  
            fin.close()  
        configNew += configCtauTemplate
        configNew += "\n"  
        configNew += "\n"  
        configNew += "EOF \n"
        fnew.write(configNew)
        fnew.close()  

print "Finished making all slha files"  



        


        
