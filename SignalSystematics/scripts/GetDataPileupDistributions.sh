#!/bin/bash

# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData#Pileup_JSON_Files_For_Run_II

########################################################
# Define JSONs and min-bias xsecs and number of bins
########################################################

json15=Cert_13TeV_16Dec2015ReReco_Collisions15_25ns_JSON_Silver_v2.txt
minBias15=69000
minBiasUncertainty15=0.046

json16=Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
minBias16=69200
minBiasUncertainty16=0.046

json17=Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt
minBias17=69200
minBiasUncertainty17=0.046

nBinsX=100

########################################################
# Set up and get JSONs
########################################################

minBias15Up=`echo "print $minBias15 * (1 + $minBiasUncertainty15)" | python`
minBias15Down=`echo "print $minBias15 * (1 - $minBiasUncertainty15)" | python`

minBias16Up=`echo "print $minBias16 * (1 + $minBiasUncertainty16)" | python`
minBias16Down=`echo "print $minBias16 * (1 - $minBiasUncertainty16)" | python`

minBias17Up=`echo "print $minBias17 * (1 + $minBiasUncertainty17)" | python`
minBias17Down=`echo "print $minBias17 * (1 - $minBiasUncertainty17)" | python`

source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scram runtime -sh`

curl https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/PileUp/pileup_latest.txt > pileup_2015.txt
curl https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/PileUp/pileup_latest.txt > pileup_2016.txt
curl https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/PileUp/pileup_latest.txt > pileup_2017.txt

wget https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions15/13TeV/Reprocessing/$json15
wget https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/$json16
wget https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/$json17

########################################################
# Split up 2016 into BC and DEFGH
########################################################

json16BC=Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2_BC.txt
json16DEFGH=Cert_271036-280385_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2_DEFGH.txt

filterJSON.py --min 272007 --max 276283 $json16 --output $json16BC
filterJSON.py --min 276315 --max 284044 $json16 --output $json16DEFGH

########################################################
# Get data distributions using JSONs as masks
########################################################

pileupCalc.py -i $json15 --inputLumiJSON pileup_2015.txt --calcMode true --minBiasXsec $minBias15 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2015_central.root
pileupCalc.py -i $json15 --inputLumiJSON pileup_2015.txt --calcMode true --minBiasXsec $minBias15Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2015_up.root
pileupCalc.py -i $json15 --inputLumiJSON pileup_2015.txt --calcMode true --minBiasXsec $minBias15Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2015_down.root

pileupCalc.py -i $json16 --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016_central.root
pileupCalc.py -i $json16 --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016_up.root
pileupCalc.py -i $json16 --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016_down.root

pileupCalc.py -i $json16BC --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016BC_central.root
pileupCalc.py -i $json16BC --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016BC_up.root
pileupCalc.py -i $json16BC --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016BC_down.root

pileupCalc.py -i $json16DEFGH --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016DEFGH_central.root
pileupCalc.py -i $json16DEFGH --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016DEFGH_up.root
pileupCalc.py -i $json16DEFGH --inputLumiJSON pileup_2016.txt --calcMode true --minBiasXsec $minBias16Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2016DEFGH_down.root

pileupCalc.py -i $json17 --inputLumiJSON pileup_2017.txt --calcMode true --minBiasXsec $minBias17 --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2017_central.root
pileupCalc.py -i $json17 --inputLumiJSON pileup_2017.txt --calcMode true --minBiasXsec $minBias17Up --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2017_up.root
pileupCalc.py -i $json17 --inputLumiJSON pileup_2017.txt --calcMode true --minBiasXsec $minBias17Down --maxPileupBin $nBinsX --numPileupBins $nBinsX puData_2017_down.root

########################################################
# Combine ROOT files and clean up
########################################################

root -b -q -l combineDataFiles.C

rm *.txt
rm puData_2015_*.root
rm puData_2016_*.root
rm puData_2017_*.root

echo "Created combined file puData.root"
