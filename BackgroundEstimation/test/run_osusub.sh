#!/bin/bash

version=1

until [ ! -d "condor/2022/EGammaFiducialMap_$version" ]
do
  echo folder: $version
  ((version=version+1))
done

#osusub.py -n 9999 -m -1 -t Dataset -A -P -l localConfig_2022.py -w run2022_test_v$version/ --redirector FNAL -g -R "request_memory=3000MB request_cpus=4" -J P_Golden22
osusub.py -l localConfig_2022.py -t Dataset -w 2022/EGammaFiducialMap_$version/ -A -P -J P_Golden22 -R "request_memory=3000MB request_cpus=4 request_disk=1000MB"
