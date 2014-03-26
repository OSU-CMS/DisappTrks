#!/bin/sh 

# Use to set up environment for generating signal MC.  
# Instructions:  https://twiki.cern.ch/twiki/bin/viewauth/CMS/DisappearingTracksSearch2012Recipes#Signal_MC_AN1
# Usage: 
#> cmsrel CMSSW_5_3_11 # Use same release used for bkgd MC production
#> cd CMSSW_5_3_11/src/
#CMSSW_5_3_11/src> cmsenv
#CMSSW_5_3_11/src> git clone git@github.com:wulsin/DisappTrks.git
#CMSSW_5_3_11/src> DisappTrks/SignalMC/test/setupForSignalMC.sh  
git cms-addpkg Configuration/Generator
git cms-addpkg SimG4Core/CustomPhysics 
git cms-addpkg SimG4Core/Application
cp DisappTrks/SignalMC/StackingAction.cc  SimG4Core/Application/src/  
cp DisappTrks/SignalMC/CustomPDGParser.h SimG4Core/CustomPhysics/interface/  
cp DisappTrks/SignalMC/CustomPDGParser.cc SimG4Core/CustomPhysics/src/  
cp DisappTrks/SignalMC/CustomParticleFactory.cc SimG4Core/CustomPhysics/src/  
cp DisappTrks/SignalMC/python/Exotica_HSCP_SIM_cfi.py SimG4Core/CustomPhysics/python/  
cp DisappTrks/SignalMC/data/*.*  Configuration/Generator/data/  
echo "Finished copying over relevant files.  Now checking for differences.  Any difference found indicates a problem in copying."  
diff DisappTrks/SignalMC/StackingAction.cc  SimG4Core/Application/src/StackingAction.cc  
diff DisappTrks/SignalMC/CustomPDGParser.h SimG4Core/CustomPhysics/interface/CustomPDGParser.h  
diff DisappTrks/SignalMC/CustomPDGParser.cc SimG4Core/CustomPhysics/src/CustomPDGParser.cc  
diff DisappTrks/SignalMC/CustomParticleFactory.cc SimG4Core/CustomPhysics/src/CustomParticleFactory.cc  
diff DisappTrks/SignalMC/python/Exotica_HSCP_SIM_cfi.py SimG4Core/CustomPhysics/python/Exotica_HSCP_SIM_cfi.py  
echo "Finished checking differences.  If none were found, all is OK."  
echo "Now you are ready to scram b."  











