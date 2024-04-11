#! /usr/bin/bash
python3 OSUT3Analysis/DBTools/python/getSiblings.py -f EGamma_2022F -s /EGamma/Run2022F-PromptReco-v1/AOD -t 10 -j 1 -m 100
cmsRun DisappTrks/CITests/config_cfg.py True 100 10 /EGamma/Run2022F-EXODisappTrk-PromptReco-v1/AOD EGamma_2022F eventList_10.txt
