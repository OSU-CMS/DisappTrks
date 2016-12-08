#!/bin/bash

source /cvmfs/cms.cern.ch/cmsset_default.sh

workdir=`pwd`

blocks=`ls go*.jdl | wc -l`

cd output/

for (( i=0; i<$blocks; i++ ))
do
        hadd output$i.root output_$i\_*.root
        rm output_$i\_*.root
done

hadd result.root output*.root
rm output*.root

cd $workdir
