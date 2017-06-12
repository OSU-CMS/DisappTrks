#!/usr/bin/env bash

cat /dev/stdin | grep "^  " | grep -v "(\(Run\|Lumi\))\|TTree" | awk '{print $1,$2,$3}' | sed "s/ /:/g" | sort -h
