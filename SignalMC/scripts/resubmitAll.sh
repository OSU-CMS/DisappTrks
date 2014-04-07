#!/usr/bin/env bash

# Usage:
# /afs/cern.ch/work/w/wulsin/public/disappTrk/signalMCGenV2/CMSSW_5_3_11/src/DisappTrks/SignalMC/test> 
# > ../scripts/resubmitAll.sh  

# Take directories from multicrabAuto.cfg  

# for dir in \
# AMSB_chargino_100GeV_ctau1000cm_FilterSumPt50    

for dir in \
AMSB_chargino_100GeV_ctau1000cm_FilterSumPt50    \
AMSB_chargino_100GeV_ctau100cm_FilterSumPt50    \
AMSB_chargino_100GeV_ctau10cm_FilterSumPt50    \
AMSB_chargino_200GeV_ctau1000cm_FilterSumPt50    \
AMSB_chargino_200GeV_ctau1000cm_NoFilter    \
AMSB_chargino_200GeV_ctau100cm_FilterSumPt50    \
AMSB_chargino_200GeV_ctau100cm_NoFilter    \
AMSB_chargino_200GeV_ctau10cm_FilterSumPt50    \
AMSB_chargino_200GeV_ctau10cm_NoFilter    \
AMSB_chargino_300GeV_ctau1000cm_FilterSumPt50    \
AMSB_chargino_300GeV_ctau100cm_FilterSumPt50    \
AMSB_chargino_300GeV_ctau10cm_FilterSumPt50    \
AMSB_chargino_400GeV_ctau1000cm_FilterSumPt50    \
AMSB_chargino_400GeV_ctau100cm_FilterSumPt50    \
AMSB_chargino_400GeV_ctau10cm_FilterSumPt50    \
AMSB_chargino_500GeV_ctau1000cm_FilterSumPt50    \
AMSB_chargino_500GeV_ctau1000cm_NoFilter    \
AMSB_chargino_500GeV_ctau100cm_FilterSumPt50    \
AMSB_chargino_500GeV_ctau100cm_NoFilter    \
AMSB_chargino_500GeV_ctau10cm_FilterSumPt50    \
AMSB_chargino_500GeV_ctau10cm_NoFilter    \
AMSB_chargino_600GeV_ctau1000cm_FilterSumPt50    \
AMSB_chargino_600GeV_ctau100cm_FilterSumPt50    \
AMSB_chargino_600GeV_ctau10cm_FilterSumPt50
do
    echo "Doing dir: $dir" 
    crab -status -c $dir 
    crab -getoutput -c $dir 
#    crab -status -c $dir  
#    crab -getoutput -c $dir   # Do twice, since sometimes the first time doesn't work.  
    crab -status -c $dir  >  $dir/status.log 
    cat $dir/status.log | ../scripts/resubmitJobs.pl > resubmitOne.sh     # can use resubmitStuckJobs.pl or resubmitStillbornJobs.pl instead
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






