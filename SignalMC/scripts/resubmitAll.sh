#!/usr/bin/env bash

#for dir in \
#CharginoAMSB_LL01_1ns  \
#CharginoAMSB_LL01_0p5ns  \
#CharginoAMSB_LL01_5ns  \
#CharginoAMSB_LL01_mGrav50K_1ns  \
#CharginoAMSB_LL01_mGrav50K_0p5ns  \
#CharginoAMSB_LL01_mGrav50K_5ns  \
#CharginoAMSB_LL01_mGrav75K_1ns  \
#CharginoAMSB_LL01_mGrav75K_0p5ns  \
#CharginoAMSB_LL01_mGrav75K_5ns  \
#CharginoAMSB_LL01_mGrav100K_1ns  \
#CharginoAMSB_LL01_mGrav100K_0p5ns  \
#CharginoAMSB_LL01_mGrav100K_5ns  \
#CharginoAMSB_LL01_mGrav125K_1ns  \
#CharginoAMSB_LL01_mGrav125K_0p5ns  \
#CharginoAMSB_LL01_mGrav125K_5ns  \
#CharginoAMSB_LL01_mGrav150K_1ns  \
#CharginoAMSB_LL01_mGrav150K_0p5ns  \
#CharginoAMSB_LL01_mGrav150K_5ns  \

for dir in \
CharginoAMSB_LL01_1ns  \
CharginoAMSB_LL01_0p5ns  \
CharginoAMSB_LL01_5ns  \
CharginoAMSB_LL01_mGrav50K_1ns  \
CharginoAMSB_LL01_mGrav50K_0p5ns  \
CharginoAMSB_LL01_mGrav50K_5ns  \
CharginoAMSB_LL01_mGrav75K_1ns  \
CharginoAMSB_LL01_mGrav75K_0p5ns  \
CharginoAMSB_LL01_mGrav75K_5ns  \
CharginoAMSB_LL01_mGrav100K_1ns  \
CharginoAMSB_LL01_mGrav100K_0p5ns  \
CharginoAMSB_LL01_mGrav100K_5ns  \
CharginoAMSB_LL01_mGrav125K_1ns  \
CharginoAMSB_LL01_mGrav125K_0p5ns  \
CharginoAMSB_LL01_mGrav125K_5ns  \
CharginoAMSB_LL01_mGrav150K_1ns  \
CharginoAMSB_LL01_mGrav150K_0p5ns  \
CharginoAMSB_LL01_mGrav150K_5ns  \

do
    echo "Doing dir: $dir" 
#    crab -status -c $dir | tee status$dir.log 
#    crab -getoutput -c $dir 
#    crab -status -c $dir | tee status$dir.log 
#    crab -getoutput -c $dir   # Do twice, since sometimes the first time doesn't work.  
#    crab -status -c $dir | tee status$dir.log 
#   cat status.log | ./resubmitStuckJobs.pl > resubmitOne.sh
#    cat status$dir.log | ./resubmitJobs.pl > resubmitOne$dir.sh
#   chmod +x resubmitOne$dir.sh
#    ./resubmitOne$dir.sh

#######
# When finished, report and publish:
######
    crab -report -c $dir
    crab -publishNoInp -USER.dbs_url_for_publication=https://cmsdbsprod.cern.ch:8443/cms_dbs_ph_analysis_02_writer/servlet/DBSServlet -c $dir 

done  






