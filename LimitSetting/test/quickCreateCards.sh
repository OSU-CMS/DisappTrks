#!/bin/bash

SUFFIX=`date +%Y%b%d`

echo Creating 2015/6/7 cards with suffix ${SUFFIX}...

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

makeDatacards.py -g -e 2017_NLayers6plus -c limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -e 2017_NLayers5 -c limits_2017_NLayers5_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -e 2017_NLayers4 -c limits_2017_NLayers4_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -e 2016BC -c limits_2016BC_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -e 2016DEFGH -c limits_2016DEFGH_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -e 2015 -c limits_2015_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}

combineAllCards.py -d ${SUFFIX} # make 2015-6 in limits_all20156_${SUFFIX}
combineNLayersCards.py -d ${SUFFIX} # make 2017 in limits_2017_all_${SUFFIX}
combineAllCards_run2.py -d ${SUFFIX} # make 2015-7 in limits_run2_${SUFFIX}

echo Examples of running...
echo runLimits.py --noPicky -b -l wino -M Asymptotic -c limits_2017_all_${SUFFIX} -e 2017_all
#echo runLimits.py --noPicky -b -l amsbLimitConfig.py -M Asymptotic -c limits_run2_${SUFFIX} 
echo

echo "Examples of plotting..."
echo makeLimitPlots.py -e 2017_all -l wino -c limits_2017_all_${SUFFIX} -o exp
