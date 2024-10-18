#!/bin/bash

# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData

########################################################
# Define JSONs and min-bias xsecs and number of bins
########################################################

json22=Cert_Collisions2022_355100_362760_Golden.json
minBias22=69200
minBiasUncertainty22=0.046

json23=Cert_Collisions2023_366442_370790_Golden.json
minBias23=69200
minBiasUncertainty23=0.046

nBinsX=100

########################################################
# Set up and get JSONs
########################################################

minBias22Up=`echo "print($minBias22 * (1 + $minBiasUncertainty22))" | python3`
minBias22Down=`echo "print($minBias22 * (1 - $minBiasUncertainty22))" | python3`

minBias23Up=`echo "print($minBias23 * (1 + $minBiasUncertainty23))" | python3`
minBias23Down=`echo "print($minBias23 * (1 - $minBiasUncertainty23))" | python3`

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scram runtime -sh`

curl https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/PileUp/BCDEFG/pileup_JSON.txt > pileup_2022.txt
curl https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions23/PileUp/BCD/pileup_JSON.txt > pileup_2023.txt

wget https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/$json22
wget https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions23/$json23

########################################################
# Get data distributions using JSONs as masks
########################################################

pileupCalc.py -i $json22 --inputLumiJSON pileup_2022.txt --calcMode true --minBiasXsec $minBias22 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2022_central.root
pileupCalc.py -i $json22 --inputLumiJSON pileup_2022.txt --calcMode true --minBiasXsec $minBias22Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2022_up.root
pileupCalc.py -i $json22 --inputLumiJSON pileup_2022.txt --calcMode true --minBiasXsec $minBias22Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2022_down.root

pileupCalc.py -i $json23 --inputLumiJSON pileup_2023.txt --calcMode true --minBiasXsec $minBias23 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2023_central.root
pileupCalc.py -i $json23 --inputLumiJSON pileup_2023.txt --calcMode true --minBiasXsec $minBias23Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2023_up.root
pileupCalc.py -i $json23 --inputLumiJSON pileup_2023.txt --calcMode true --minBiasXsec $minBias23Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2023_down.root

########################################################
# Combine ROOT files and clean up
########################################################

root -b -q -l combineDataFiles.C

rm *.txt
rm puData_2022_*.root
rm puData_2023_*.root

echo "Created combined file puData.root"
