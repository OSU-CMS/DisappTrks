#!/bin/bash

# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData#Pileup_JSON_Files_For_Run_II

########################################################
# Define JSONs and min-bias xsecs and number of bins
########################################################

json15=Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver_v2.txt
minBias15=69000
minBiasUncertainty15=0.046

json16=Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2.txt
minBias16=69200
minBiasUncertainty16=0.046

nBinsX=100

########################################################
# Set up and get JSONs
########################################################

minBias15Up=`echo "print $minBias15 * (1 + $minBiasUncertainty15)" | python`
minBias15Down=`echo "print $minBias15 * (1 - $minBiasUncertainty15)" | python`

minBias16Up=`echo "print $minBias16 * (1 + $minBiasUncertainty16)" | python`
minBias16Down=`echo "print $minBias16 * (1 - $minBiasUncertainty16)" | python`

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scram runtime -sh`

curl https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/PileUp/pileup_latest.txt > pileup_2015.txt
curl https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/PileUp/pileup_latest.txt > pileup_2016.txt

wget https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Reprocessing/$json15
wget https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/$json16

########################################################
# Get data distributions using JSONs as masks
########################################################

pileupCalc.py -i $json15 --inputLumiJSON pileup_2015.txt --calcMode true --minBiasXsec $minBias15 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2015_central.root
pileupCalc.py -i $json15 --inputLumiJSON pileup_2015.txt --calcMode true --minBiasXsec $minBias15Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2015_up.root
pileupCalc.py -i $json15 --inputLumiJSON pileup_2015.txt --calcMode true --minBiasXsec $minBias15Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2015_down.root

pileupCalc.py -i $json16 --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016_central.root
pileupCalc.py -i $json16 --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016_up.root
pileupCalc.py -i $json16 --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016_down.root

########################################################
# Combine ROOT files and clean up
########################################################

root -b -q -l combineDataFiles.C

rm *.txt
rm puData_2015_*.root
rm puData_2016_*.root

echo "Created combined file puData.root"
