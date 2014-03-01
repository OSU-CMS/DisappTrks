#!/usr/bin/env bash

# Usage:
# /afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC> 
# > scripts/resubmitAll.sh  

# Take directories from multicrabAuto.cfg  


for dir in \
AMSBChargino_SystISRDn_mGrav150K_0p5ns     \
AMSBChargino_SystISRDn_mGrav150K_1ns     \
AMSBChargino_SystISRDn_mGrav150K_5ns     \
AMSBChargino_SystISRDn_mGrav75K_0p5ns     \
AMSBChargino_SystISRDn_mGrav75K_1ns     \
AMSBChargino_SystISRDn_mGrav75K_5ns     \
AMSBChargino_SystISRUp_mGrav150K_0p5ns     \
AMSBChargino_SystISRUp_mGrav150K_1ns     \
AMSBChargino_SystISRUp_mGrav150K_5ns     \
AMSBChargino_SystISRUp_mGrav75K_0p5ns     \
AMSBChargino_SystISRUp_mGrav75K_1ns     \
AMSBChargino_SystISRUp_mGrav75K_5ns     \
AMSBChargino_mGrav150K_0p5ns     \
AMSBChargino_mGrav150K_1ns     \
AMSBChargino_mGrav150K_5ns     \
AMSBChargino_mGrav75K_0p5ns     \
AMSBChargino_mGrav75K_1ns     \
AMSBChargino_mGrav75K_5ns       
do
    echo "Doing dir: $dir" 
    crab -status -c $dir 
    crab -getoutput -c $dir 
#    crab -status -c $dir  
#    crab -getoutput -c $dir   # Do twice, since sometimes the first time doesn't work.  
    crab -status -c $dir  >  $dir/status.log 
    cat $dir/status.log | scripts/resubmitJobs.pl > resubmitOne.sh     # can use resubmitStuckJobs.pl or resubmitStillbornJobs.pl instead
    cp resubmitOne.sh $dir/ 
    chmod +x resubmitOne.sh
    ./resubmitOne.sh  >  $dir/resubmitOne.log 
    cat $dir/resubmitOne.log   # so user can see it

#######
# When finished, report and publish:
######
#    crab -report -c $dir
#    crab -publishNoInp -USER.dbs_url_for_publication=https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet -c $dir 

done  






