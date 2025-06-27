#!/bin/bash

echo "Using the date suffix is good to keep track of progress, but it is not ideal when tests are being done."
#SUFFIX=`date +%Y%b%d`
SUFFIX="TESTING"

echo "Creating 2022-3 cards with suffix ${SUFFIX}..."

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

######################

# echo "Creating 2022CD_NLayers6plus..."
# makeDatacards.py -g -e 2022CD_NLayers6plus -c limits_2022CD_NLayers6plus_${SUFFIX}

# echo "Creating 2022CD_NLayers5..."
# makeDatacards.py -g -e 2022CD_NLayers5 -c limits_2022CD_NLayers5_${SUFFIX}

# echo "Creating 2022CD_NLayers4..."
# makeDatacards.py -g -e 2022CD_NLayers4 -c limits_2022CD_NLayers4_${SUFFIX}

# echo "Creating 2022EFG_NLayers6plus..."
# makeDatacards.py -g -e 2022EFG_NLayers6plus -c limits_2022EFG_NLayers6plus_${SUFFIX}

# echo "Creating 2022EFG_NLayers5..."
# makeDatacards.py -g -e 2022EFG_NLayers5 -c limits_2022EFG_NLayers5_${SUFFIX}

# echo "Creating 2022EFG_NLayers4..."
# makeDatacards.py -g -e 2022EFG_NLayers4 -c limits_2022EFG_NLayers4_${SUFFIX}

# echo "Creating 2023C_NLayers6plus..."
# makeDatacards.py -g -e 2023C_NLayers6plus -c limits_2023C_NLayers6plus_${SUFFIX}

# echo "Creating 2023C_NLayers5..."
# makeDatacards.py -g -e 2023C_NLayers5 -c limits_2023C_NLayers5_${SUFFIX}

# echo "Creating 2023C_NLayers4..."
# makeDatacards.py -g -e 2023C_NLayers4 -c limits_2023C_NLayers4_${SUFFIX}

# echo "Creating 2023D_NLayers6plus..."
# makeDatacards.py -g -e 2023D_NLayers6plus -c limits_2023D_NLayers6plus_${SUFFIX}

# echo "Creating 2023D_NLayers5..."
# makeDatacards.py -g -e 2023D_NLayers5 -c limits_2023D_NLayers5_${SUFFIX}

# echo "Creating 2023D_NLayers4..."
# makeDatacards.py -g -e 2023D_NLayers4 -c limits_2023D_NLayers4_${SUFFIX}

######################

echo

echo combineDatacards.py -l wino -s ${SUFFIX}
combineDatacards.py -l wino -s ${SUFFIX}

echo

echo "Now run:"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022CD_NLayers4_${SUFFIX} -e 2022CD_NLayers4"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022CD_NLayers5_${SUFFIX} -e 2022CD_NLayers5"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022CD_NLayers6plus_${SUFFIX} -e 2022CD_NLayers6plus"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022CD_all_${SUFFIX} -e 2022CD_all"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022EFG_NLayers4_${SUFFIX} -e 2022EFG_NLayers4"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022EFG_NLayers5_${SUFFIX} -e 2022EFG_NLayers5"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022EFG_NLayers6plus_${SUFFIX} -e 2022EFG_NLayers6plus"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022EFG_all_${SUFFIX} -e 2022EFG_all"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022_all_${SUFFIX} -e 2022_all"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023C_NLayers4_${SUFFIX} -e 2023C_NLayers4"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023C_NLayers5_${SUFFIX} -e 2023C_NLayers5"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023C_NLayers6plus_${SUFFIX} -e 2023C_NLayers6plus"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023C_all_${SUFFIX} -e 2023C_all"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023D_NLayers4_${SUFFIX} -e 2023D_NLayers4"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023D_NLayers5_${SUFFIX} -e 2023D_NLayers5"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023D_NLayers6plus_${SUFFIX} -e 2023D_NLayers6plus"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023D_all_${SUFFIX} -e 2023D_all"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023_all_${SUFFIX} -e 2023_all"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_run3_${SUFFIX} -e run3"
echo "runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_run2run3_${SUFFIX} -e run2run3"
echo

runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022CD_all_${SUFFIX} -e 2022CD_all
runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022EFG_all_${SUFFIX} -e 2022EFG_all
runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2022_all_${SUFFIX} -e 2022_all
runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023C_all_${SUFFIX} -e 2023C_all
runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023D_all_${SUFFIX} -e 2023D_all
runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_2023_all_${SUFFIX} -e 2023_all
runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_run3_${SUFFIX} -e run3
runLimits.py --noPicky -b -l wino -M AsymptoticLimits -c limits_run2run3_${SUFFIX} -e run2run3

echo "Examples of plotting..."
echo "makeLimitPlots.py -e 2022CD_NLayers4 -l wino -c limits_2022CD_NLayers4_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2022CD_NLayers5 -l wino -c limits_2022CD_NLayers5_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2022CD_NLayers6plus -l wino -c limits_2022CD_NLayers6plus_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2022CD_all -l wino -c limits_2022CD_all_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2022EFG_NLayers4 -l wino -c limits_2022EFG_NLayers4_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2022EFG_NLayers5 -l wino -c limits_2022EFG_NLayers5_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2022EFG_NLayers6plus -l wino -c limits_2022EFG_NLayers6plus_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2022EFG_all -l wino -c limits_2022EFG_all_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2022_all -l wino -c limits_2022_all_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2023C_NLayers4 -l wino -c limits_2023C_NLayers4_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2023C_NLayers5 -l wino -c limits_2023C_NLayers5_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2023C_NLayers6plus -l wino -c limits_2023C_NLayers6plus_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2023C_all -l wino -c limits_2023C_all_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2023D_NLayers4 -l wino -c limits_2023D_NLayers4_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2023D_NLayers5 -l wino -c limits_2023D_NLayers5_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2023D_NLayers6plus -l wino -c limits_2023D_NLayers6plus_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2023D_all -l wino -c limits_2023D_all_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e 2023_all -l wino -c limits_2023_all_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e run3 -l wino -c limits_run3_${SUFFIX} -o exp"
echo "makeLimitPlots.py -e run2run3 -l wino -c limits_run2run3_${SUFFIX} -o exp"
echo "Or try: ./quickCreatePlots20223.sh"
