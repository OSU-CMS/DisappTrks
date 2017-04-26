#!/usr/bin/env bash

if [ $# -ne 2 ]
then
  echo "Usage: $0 CONDOR_DIR CHANNEL_NAME"
  exit 1
fi
condorDir=$1
channel=$2

if [ ! -e $condorDir ]
then
  echo "\"$condorDir\" does not exist!"
  exit 1
fi
if [ ! -e "${condorDir}/${channel}" ]
then
  echo "\"$channel\" does not exist as a skim directory!"
  exit 1
fi

logFiles=`ls ${condorDir}/condor_*.log | sort -h`
for logFile in ${logFiles}
do
  jobNumber=`echo $logFile | sed "s/^.*\/condor_\(.*\)\.log$/\1/g"`
  grep "return value 0" $logFile > /dev/null 2>&1
  isFailed=$?
  ls ${condorDir}/${channel}/skim_${jobNumber}.root > /dev/null 2>&1
  isMissing=$?
  if [ $isFailed -eq 0 ] && [ $isMissing -ne 0 ]
  then
    echo "MISSING: ${condorDir}/${channel}/skim_${jobNumber}.root"
  fi
done
