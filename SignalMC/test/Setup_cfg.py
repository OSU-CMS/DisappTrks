#! /usr/bin/python
import os
import sys

masses = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
lifetimes = [1, 10, 100, 1000, 10000]


for mass in masses:
  for lifetime in lifetimes:
    cff_file = "DisappTrks/SignalMC/python/pythia8GeantDecay/AMSB_chargino"+str(mass)+"GeV_ctau"+str(lifetime)+"cm_NoFilter_13TeV.py"
    cmd = "cmsDriver.py  "
    cmd += cff_file
    cmd += " --fileout file:AMSB_chargino%dGeV_ctau%dcm_step1.root"%(mass,lifetime)
    cmd += " --mc --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,SimG4Core/Application/customiseSequentialSim.customiseSequentialSim,DisappTrks/SignalMC/genParticlePlusGeant.customizeProduce,DisappTrks/SignalMC/genParticlePlusGeant.customizeKeep --datatier GEN-SIM --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --geometry DB:Extended --era Run2_2017"
    cmd += " --python_filename step1/pythia8GeantDecay/AMSB_chargino%dGeV_ctau%dcm_step1.py"%(mass,lifetime)
    cmd += " --no_exec -n 10"
    os.system(cmd)
    
