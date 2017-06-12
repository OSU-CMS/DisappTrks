#!/usr/bin/env bash

if [ $# -ne 3 ]
then
  echo "Usage: $(basename $0) CONDOR_DIR SKIM_NAME OUTPUT_FILE"
  exit 1
fi

condorDir=$1
skimName=$2
outputFile=$3

if [ ! -e $condorDir ]
then
  echo "\"$condorDir\" does not exist!"
  exit 1
fi
if [ -e $outputFile ]
then
  echo "\"$outputFile\" already exists!"
  exit 1
fi

nFiles=`find -L $condorDir -type f -regex ".*\/$skimName\/skim_[^/]*\.root$" | wc -l`
if [ $nFiles -ne 0 ]
then
  find -L $condorDir -type f -regex ".*\/$skimName\/skim_[^/]*\.root$" | xargs edmFileUtil -e | cleanEdmFileEvents.sh > $outputFile 2>&1
  nEvents=`wc -l $outputFile | awk '{print $1}'`
  echo "Event numbers written to \"$outputFile\". Now run:"
  echo "  edmPickEvents.py --maxEventsInteractive $nEvents /DATA/SET/NAME $outputFile"
else
  echo "No events found in skim!"
fi
