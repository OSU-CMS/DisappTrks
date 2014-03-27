#!/usr/bin/env python

# Usage:
# /afs/cern.ch/user/w/wulsin/workspace/public/disappTrk/signalMCGenV3/CMSSW_5_3_11/src/DisappTrks/SignalMC/test > ../scripts/makeSlhaFiles.py 


# SLHA files for each mass point must be created independently (e.g., with isajet)  
# mass of chargino in GeV
masses = [
    200, 
    ]

# c*lifetime of chargino in cm 
ctaus = [
#    1, 
    10,
#    30, 
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
    text += "DECAY  1000024  " + str(width) + " # chargino decay  \n"  
    text += "#   BR       NDA      ID1      ID2  \n"
    text += "   1.0000    2     1000022    211   \n"
    text += "Block \n"  
    fnew.write(text)  
    fnew.close()


# Make complete slha files for each mass, ctau point 
for m in masses:
    for ctau in ctaus:
        templateMassFile = "../data/AMSB_chargino_" + str(m) + "GeV_template.slha"  
        #        print "Opening template file " + templateMassFile  
        fin = open(templateMassFile, "r")
        configMassTemplate = fin.read()
        fin.close()

        templateCtauFile = "../data/AMSB_chargino" + str(ctau) + "ctau.slha"  
        #        print "Opening template file " + templateCtauFile  
        fin = open(templateCtauFile, "r")
        configCtauTemplate = fin.read()
        fin.close()
        
        newFile = "../data/geant4_AMSB_chargino_" + str(m) + "GeV_ctau" + str(ctau) + "cm.slha"  
        print "Creating new file: " + newFile  
        fnew = open(newFile, "w")
        configNew  = "# This file is read by SimG4Core/CustomPhysics/src/CustomParticleFactory.cc  \n"
        configNew += '# The strings "decay", "pdg code", and "block", with correct capitalization, are used \n'
        configNew += "# to control the data input, so do not use these in any comments.  \n"
        configNew += "# \n"
        configNew += "# \n"
        configNew += "# Get values for chargino and neutralino masses from:  \n"
        configNew += "# " + templateMassFile + "\n"  
        configNew += configMassTemplate
        configNew += "\n"
        configNew += "\n"
        configNew += "\n"
        configNew += configCtauTemplate
        configNew += "\n"  
        configNew += "\n"  
        configNew += "EOF \n"  
        fnew.write(configNew)
        fnew.close()  

print "Finished making all slha files"  



        


        
