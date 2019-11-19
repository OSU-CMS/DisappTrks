#!/bin/bash

SUFFIX=`date +%Y%b%d`

echo "Creating 2015-8 plots with suffix ${SUFFIX}..."

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

makeLimitPlots.py -e all20156 -l wino -c limits_all20156_${SUFFIX} -o exp,obs

makeLimitPlots.py -e 2017_NLayers4 -l wino -c limits_2017_NLayers4_${SUFFIX} -o exp,obs
makeLimitPlots.py -e 2017_NLayers5 -l wino -c limits_2017_NLayers5_${SUFFIX} -o exp,obs
makeLimitPlots.py -e 2017_NLayers6plus -l wino -c limits_2017_NLayers6plus_${SUFFIX} -o exp,obs

makeLimitPlots.py -e 2018AB_NLayers4 -l wino -c limits_2018AB_NLayers4_${SUFFIX} -o exp,obs
makeLimitPlots.py -e 2018AB_NLayers5 -l wino -c limits_2018AB_NLayers5_${SUFFIX} -o exp,obs
makeLimitPlots.py -e 2018AB_NLayers6plus -l wino -c limits_2018AB_NLayers6plus_${SUFFIX} -o exp,obs

makeLimitPlots.py -e 2018CD_NLayers4 -l wino -c limits_2018CD_NLayers4_${SUFFIX} -o exp,obs
makeLimitPlots.py -e 2018CD_NLayers5 -l wino -c limits_2018CD_NLayers5_${SUFFIX} -o exp,obs
makeLimitPlots.py -e 2018CD_NLayers6plus -l wino -c limits_2018CD_NLayers6plus_${SUFFIX} -o exp,obs

makeLimitPlots.py -e 2017_all -l wino -c limits_2017_all_${SUFFIX} -o exp,obs
makeLimitPlots.py -e 2018AB_all -l wino -c limits_2018AB_all_${SUFFIX} -o exp,obs
makeLimitPlots.py -e 2018CD_all -l wino -c limits_2018CD_all_${SUFFIX} -o exp,obs
makeLimitPlots.py -e 2018_all -l wino -c limits_2018_all_${SUFFIX} -o exp,obs
makeLimitPlots.py -e all20178 -l wino -c limits_all20178_${SUFFIX} -o exp,obs
makeLimitPlots.py -e run2 -l wino -c limits_run2_${SUFFIX} -o exp,obs

python makeComparisonPlots.py ${SUFFIX}

mkdir plots_${SUFFIX}
mv limitsLifetimeVsMassCompareNLayers.* plots_${SUFFIX}
mv limitsLifetimeVsMassCombinedRun2CompareYears.* plots_${SUFFIX}

mkdir plots_${SUFFIX}/2017
cp limits/limits_2017_all_${SUFFIX}/*.pdf plots_${SUFFIX}/2017
cp limits/limits_2017_all_${SUFFIX}/*.root plots_${SUFFIX}/2017

mkdir plots_${SUFFIX}/2018
cp limits/limits_2018_all_${SUFFIX}/*.pdf plots_${SUFFIX}/2018
cp limits/limits_2018_all_${SUFFIX}/*.root plots_${SUFFIX}/2018

mkdir plots_${SUFFIX}/run2
cp limits/limits_run2_${SUFFIX}/*.pdf plots_${SUFFIX}/run2
cp limits/limits_run2_${SUFFIX}/*.root plots_${SUFFIX}/run2

echo "Copied plots into plots_${SUFFIX}/"
