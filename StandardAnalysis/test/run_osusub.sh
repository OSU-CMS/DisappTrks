#!/bin/bash

version=1

until [ ! -d "condor/2022_Datasets/Tau_2022F_$version" ]
do
  echo folder: $version
  ((version=version+1))
done

#osusub.py -n 9999 -m -1 -t Dataset -A -P -l localConfig_2022.py -w run2022_test_v$version/ --redirector FNAL -g -R "request_memory=3000MB request_cpus=4" -J P_Golden22
osusub.py -l localConfig_2022.py -t Dataset -w 2022_Datasets/Tau_2022F_$version/ -A -P -J P_Golden22 -R "request_memory=1500MB request_cpus=2 request_disk=750MB"
