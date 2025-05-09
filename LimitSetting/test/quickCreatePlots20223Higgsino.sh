#!/bin/bash

SUFFIX="TESTING"

echo "Creating 2022-23 plots with suffix ${SUFFIX}..."

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`

echo "-o exp,obs has to be added whenever observed values are available."

# makeLimitPlotsWithCMSLumi.py -e 2022CD_NLayers4 -l higgsino -c limits_2022CD_NLayers4_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2022CD_NLayers5 -l higgsino -c limits_2022CD_NLayers5_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2022CD_NLayers6plus -l higgsino -c limits_2022CD_NLayers6plus_${SUFFIX} -o exp
makeLimitPlotsWithCMSLumi.py -e 2022CD_all -l higgsino -c limits_2022CD_all_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2022EFG_NLayers4 -l higgsino -c limits_2022EFG_NLayers4_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2022EFG_NLayers5 -l higgsino -c limits_2022EFG_NLayers5_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2022EFG_NLayers6plus -l higgsino -c limits_2022EFG_NLayers6plus_${SUFFIX} -o exp
makeLimitPlotsWithCMSLumi.py -e 2022EFG_all -l higgsino -c limits_2022EFG_all_${SUFFIX} -o exp
makeLimitPlotsWithCMSLumi.py -e 2022_all -l higgsino -c limits_2022_all_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2023C_NLayers4 -l higgsino -c limits_2023C_NLayers4_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2023C_NLayers5 -l higgsino -c limits_2023C_NLayers5_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2023C_NLayers6plus -l higgsino -c limits_2023C_NLayers6plus_${SUFFIX} -o exp
makeLimitPlotsWithCMSLumi.py -e 2023C_all -l higgsino -c limits_2023C_all_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2023D_NLayers4 -l higgsino -c limits_2023D_NLayers4_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2023D_NLayers5 -l higgsino -c limits_2023D_NLayers5_${SUFFIX} -o exp
# makeLimitPlotsWithCMSLumi.py -e 2023D_NLayers6plus -l higgsino -c limits_2023D_NLayers6plus_${SUFFIX} -o exp
makeLimitPlotsWithCMSLumi.py -e 2023D_all -l higgsino -c limits_2023D_all_${SUFFIX} -o exp
makeLimitPlotsWithCMSLumi.py -e 2023_all -l higgsino -c limits_2023_all_${SUFFIX} -o exp
makeLimitPlotsWithCMSLumi.py -e run3 -l higgsino -c limits_run3_${SUFFIX} -o exp
makeLimitPlotsWithCMSLumi.py -e run2run3 -l higgsino -c limits_run2run3_${SUFFIX} -o exp

# python3 makeComparisonPlots.py ${SUFFIX}