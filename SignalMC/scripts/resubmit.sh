#!/usr/bin/env bash

crab -kill 1-41,43-75,77-128,130-184,186-200 -c /afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenNew1/CMSSW_5_3_3/src/CharginoAMSB_LL01_1ns/
sleep 60
crab -forceResubmit 1-41,43-75,77-128,130-184,186-200 -GRID.ce_white_list= -c /afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenNew1/CMSSW_5_3_3/src/CharginoAMSB_LL01_1ns/
