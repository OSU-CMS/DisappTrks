#! /usr/bin/bash
wget https://distrktest.web.cern.ch/DisTksTest/7e90e65b-10b7-40f0-8d8e-5c2b3e6649ec.root

python3 ../../OSUT3Analysis/DBTools/python/getSiblings.py -f EGamma_2022F -s 7e90e65b-10b7-40f0-8d8e-5c2b3e6649ec.root -t 10 -j 1 -m 100
cmsRun config_cfg.py True 100 10 7e90e65b-10b7-40f0-8d8e-5c2b3e6649ec.root EGamma_2022F eventList_1.txt
