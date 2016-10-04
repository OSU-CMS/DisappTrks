#!/bin/bash

#ls /path/to/files/*.root > list.txt
#split --lines=40 -d list.txt list_N.

let number=$1+1
let submitdir=$3

source /cvmfs/cms.cern.ch/cmsset_default.sh

cd $submitdir
eval `scram runtime -sh`

voms-proxy-info

file=`ls lists/list_${2}.* | sed -n "${number}p"`

hadd output/output_$2_$1.root @$file
