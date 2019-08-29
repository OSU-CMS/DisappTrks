#!/bin/bash

SUFFIX=`date +%Y%b%d`

echo "Creating 2015/6/7/8 cards with suffix ${SUFFIX}..."

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

######################

echo "Creating 2018_NLayers6plus..."
makeDatacards.py -g -e 2018_NLayers6plus -c limits_2018_NLayers6plus_${SUFFIX}

echo "Creating 2018_NLayers5..."
makeDatacards.py -g -e 2018_NLayers5 -c limits_2018_NLayers5_${SUFFIX}

echo "Creating 2018_NLayers4..."
makeDatacards.py -g -e 2018_NLayers4 -c limits_2018_NLayers4_${SUFFIX}

######################

echo "Creating 2017_NLayers6plus..."
makeDatacards.py -g -e 2017_NLayers6plus -c limits_2017_NLayers6plus_${SUFFIX}

echo "Creating 2017_NLayers5..."
makeDatacards.py -g -e 2017_NLayers5 -c limits_2017_NLayers5_${SUFFIX}

echo "Creating 2017_NLayers4..."
makeDatacards.py -g -e 2017_NLayers4 -c limits_2017_NLayers4_${SUFFIX}

######################

echo "Creating 2016 BC..."
makeDatacards.py -g -e 2016BC -c limits_2016BC_${SUFFIX}

echo "Creating 2016 D-H..."
makeDatacards.py -g -e 2016DEFGH -c limits_2016DEFGH_${SUFFIX}

######################

echo "Creating 2015..."
makeDatacards.py -g -e 2015 -c limits_2015_${SUFFIX}

######################

echo

combineDatacards.py -l wino -s ${SUFFIX}

echo

echo "Now run:"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_all20156_${SUFFIX} -e 20156"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2017_all_${SUFFIX} -e 2017_all"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2017_NLayers4_${SUFFIX} -e 2017_NLayers4"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2017_NLayers5_${SUFFIX} -e 2017_NLayers5"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2017_NLayers6plus_${SUFFIX} -e 2017_NLayers6plus"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2018_all_${SUFFIX} -e 2018_all"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2018_NLayers4_${SUFFIX} -e 2018_NLayers4"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2018_NLayers5_${SUFFIX} -e 2018_NLayers5"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2018_NLayers6plus_${SUFFIX} -e 2018_NLayers6plus"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_run2_${SUFFIX} -e run2"
echo

echo "Examples of plotting..."
echo "makeLimitPlots.py -e 2017_all -l wino -c limits_2017_all_${SUFFIX} -o exp"
echo "Or try: ./quickCreatePlots.py"
