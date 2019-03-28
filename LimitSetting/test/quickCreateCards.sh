#!/bin/bash

SUFFIX=`date +%Y%b%d`

echo Creating 2015/6/7 cards with suffix ${SUFFIX}...

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

makeDatacards.py -g -l amsbLimitConfig_2017_NLayers6plus.py -c limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -l amsbLimitConfig_2017_NLayers5.py -c limits_2017_NLayers5_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -l amsbLimitConfig_2017_NLayers4.py -c limits_2017_NLayers4_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -l amsbLimitConfig_2016BC.py -c limits_2016BC_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -l amsbLimitConfig_2016DEFGH.py -c limits_2016DEFGH_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}
makeDatacards.py -g -l amsbLimitConfig_2015.py -c limits_2015_${SUFFIX} -s limits_2017_NLayers6plus_${SUFFIX}
combineAllCards.py -d ${SUFFIX} # make 2015-6
combineNLayersCards.py -d ${SUFFIX} # make 2017
combineAllCards_run2.py -d ${SUFFIX} # make 2015-7

#limits_2017_NLayers6plus_2019Mar15
#limits_2017_NLayers5_2019Mar15
#limits_2017_NLayers4_2019Mar15
#limits_2016BC_2019Mar15
#limits_2016DEFGH_2019Mar15
#limits_2015_2019Mar15
#limits_2017_all_2019Mar15
#limits_all20156_2019Mar15
#limits_run2_2019Mar15

echo Examples of running...
echo runLimits.py --noPicky -b -l amsbLimitConfig.py -M Asymptotic -c limits_2017_all_${SUFFIX} 
echo runLimits.py --noPicky -b -l amsbLimitConfig.py -M Asymptotic -c limits_run2_${SUFFIX} 
echo

echo Examples of plotting (remember to set the lumi right!)...
echo makeLimitPlots.py -l amsbLimitPlotConfig.py -c limits_2017_all_${SUFFIX} -s exp
