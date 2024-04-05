#!/usr/bin/env bash

(>&2 echo "Starting job on " `date`) # Date/time of start of job
(>&2 echo "Running on: `uname -a`") # Condor job is running on this node
(>&2 echo "System software: `cat /etc/redhat-release`") # Operating System on that node

Process=$4
RunStatus=1
CopyStatus=1
RemoveStatus=1

source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/cms.cern.ch/crab3/crab.sh
tar -xzf CMSSW_12_4_11_patch3.tar.gz
rm -f CMSSW_12_4_11_patch3.tar.gz
SCRAM_ARCH=slc7_amd64_gcc10
cd CMSSW_12_4_11_patch3/src/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/cvmfs/cms.cern.ch/slc7_amd64_gcc10/cms/cmssw-patch/CMSSW_12_4_11_patch3/external/slc7_amd64_gcc10/lib
echo $LD_LIBRARY_PATH
echo $CMSSW_BASE 
echo $PWD 
scram b ProjectRename
eval `scramv1 runtime -sh`
echo $CMSSW_BASE 
cd -

PYTHONPATH=$PYTHONPATH:./CMSSW_12_4_11_patch3/python:.

python3 /share/scratch0/mcarrigan/disTracksML/CMSSW_12_4_11_patch3/src/OSUT3Analysis/DBTools/python/getSiblings.py -f $6 -s /EGamma/Run2022F-EXODisappTrk-PromptReco-v1/AOD -t $3 -j $4 -m 1000
(>&2 echo "Arguments passed to this script are: $@")
/cvmfs/cms.cern.ch/slc7_amd64_gcc10/cms/cmssw/CMSSW_12_4_11/bin/slc7_amd64_gcc10/cmsRun $@
RunStatus=$?
if [ $RunStatus -ne 0 ]
then
  exit $RunStatus
fi

i=0
while [ $CopyStatus -ne 0 ] && [ $i -lt 10 ]
do
  ls hist_${Process}.root eventList_${Process}.txt | sed "s/^/\/data\/users\/mcarrigan\/condor\/EGamma_2022\/EGamma_2022F_test3\/EGamma_2022F\//g" | xargs rm -rf
  ls VertexCutOnly/* | sed "s/^VertexCutOnly\//\/data\/users\/mcarrigan\/condor\/EGamma_2022\/EGamma_2022F_test3\/EGamma_2022F\/VertexCutOnly\//g" | xargs rm -rf
  sleep 10
  cp -rf hist_${Process}.root eventList_${Process}.txt /data/users/mcarrigan/condor/EGamma_2022/EGamma_2022F_test3/EGamma_2022F/ &&
  cp -rf VertexCutOnly/* /data/users/mcarrigan/condor/EGamma_2022/EGamma_2022F_test3/EGamma_2022F/VertexCutOnly/
  CopyStatus=$?
  i=`expr $i + 1`
done

rm -rf hist_${Process}.root eventList_${Process}.txt VertexCutOnly CMSSW_12_4_11_patch3
RemoveStatus=$?

[ $i -eq 10 ] && exit 999
exit 0
