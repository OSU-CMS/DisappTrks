#!/bin/sh
#
# Script to submit batch cmsRun job.  
# Copied from:  https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookSetComputerNode#ManyLargeFiles  
#
# Usage:
# chargino_slha_GEN_SIM_150GeV_1ns_run.sh 0 
# Note that an argument is required in this case!  
cd /afs/cern.ch/user/w/wulsin/workspace/disappTrk/signalMCGenNew1/CMSSW_5_3_3/src
eval `scram runtime -sh`
cd -
cmsRun /afs/cern.ch/user/w/wulsin/workspace/disappTrk/signalMCGenNew1/CMSSW_5_3_3/src/cfg/chargino_STEP2_RECO_150GeV_1ns_batch.py $1  



