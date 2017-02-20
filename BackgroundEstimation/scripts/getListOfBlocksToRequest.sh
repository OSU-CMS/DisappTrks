#!/usr/bin/env bash

if [ $# -lt 1 ]
then
  echo "Usage: $0 LIST_OF_FILES"
  exit 1
fi

list=$1
if [ ! -e $list ]
then
  echo "\"${list}\" does not exist!"
  exit 1
fi

while read file
do
  block=`/cvmfs/cms.cern.ch/common/das_client --query="file file=${file} | grep file.block.name" | grep "^\"\/" | sed "s/\"\(.*\)\"/\1/g"`
  site=`/cvmfs/cms.cern.ch/common/das_client --query="block block=${block} | grep block.replica.site" | grep "^\""`

  isAtT2=0
  echo ${site} | grep "T2_\|_Disk" > /dev/null 2>&1
  if [ $? -eq 0 ]
  then
    isAtT2=1
  fi

  if [ $isAtT2 -eq 0 ]
  then
    echo ${block}
  fi
done <${list}
