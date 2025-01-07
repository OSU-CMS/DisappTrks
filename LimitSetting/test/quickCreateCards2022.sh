#!/bin/bash

SUFFIX=`date +%Y%b%d`

echo "Creating 2022 cards with suffix ${SUFFIX}..."

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

######################

echo "Creating 2022F_NLayers6plus..."
makeDatacards.py -g -e 2022F_NLayers6plus -c limits_2022F_NLayers6plus_${SUFFIX}

echo "Creating 2022F_NLayers5..."
makeDatacards.py -g -e 2022F_NLayers5 -c limits_2022F_NLayers5_${SUFFIX}

echo "Creating 2022F_NLayers4..."
makeDatacards.py -g -e 2022F_NLayers4 -c limits_2022F_NLayers4_${SUFFIX}

######################

echo

echo combineDatacards.py -l wino -s ${SUFFIX}

echo

echo "Now run:"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022F_NLayers4_${SUFFIX} -e 2022F_NLayers4"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022F_NLayers5_${SUFFIX} -e 2022F_NLayers5"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022F_NLayers6plus_${SUFFIX} -e 2022F_NLayers6plus"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_run3_${SUFFIX} -e run3"
echo

echo "Examples of plotting..."
echo "makeLimitPlots.py -e 2022F_NLayers6plus -l wino -c limits_2022F_NLayers6plus_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e run3 -l wino -c limits_run3_${SUFFIX} -o exp"
echo "Or try: ./quickCreatePlots.py"
