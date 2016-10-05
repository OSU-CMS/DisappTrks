#!/bin/bash

if [ $# -eq 0 ]
  then
		echo
    echo "Usage: ./makeLists_gfal.sh SRM_directory"
		echo
		exit
fi

dir=$1

xrootd_dir="root://cmsxrootd.fnal.gov//"
#xrootd_dir="root://xrootd.rcac.purdue.edu:8443//"

destdir=`echo $dir | sed -e "s|srm://srm.rcac.purdue.edu:8443/srm/v2/server?SFN=/mnt/hadoop|$xrootd_dir|g"`

block=0

rm JobOut/*
rm output/*
rm go*.jdl
rm lists/*

for x in `gfal-ls $1`
do
	for file in `gfal-ls "$dir$x/" | grep ".root"`
	do
		echo "$destdir$x/$file" >> list$block.txt
	done

	split --lines=15 -d list$block.txt lists/list_$block.
	rm list$block.txt

	number=`ls -1 lists/list_$block.* | wc -l`

	cat template_go.jdl | sed -e "s/BLOCK/$block/g" | sed -e "s/NUMBER/$number/g" | sed -e "s|INITIALDIR|$PWD|g" | sed -e "s|USERID|`id -u`|g" > go$block.jdl
	echo "Created go$block.jdl"
	condor_submit go$block.jdl

	let block=$block+1
done
