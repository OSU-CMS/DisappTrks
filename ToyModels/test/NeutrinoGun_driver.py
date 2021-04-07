import os

os.system('cmsDriver.py DisappTrks/ToyModels/python/NeutrinoGun_TuneCP5_13TeV_pythia8_cff.py --fileout file:NeutrinoGun_step1.root --fileout file:NeutrinoGun_step1.root --mc --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/Application/customiseSequentialSim.customiseSequentialSim --datatier GEN-SIM --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --geometry DB:Extended --era Run2_2017 --python_filename NeutrinoGun_step1.py --no_exec -n 10')
