#! /usr/bin/bash
python3 OSUT3Analysis/DBTools/python/getSiblings.py -f EGamma_2022F -s /EGamma/Run2022F-PromptReco-v1/AOD -t 10 -j 1 -m 100
cmsRun DisappTrks/CITests/config_cfg.py True 100 10 /QCD_PT-2400to3200_TuneCP5_13p6TeV_pythia8/Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v2/AODSIM QCD_PT2400to3200_TEST eventList_10.txt
