#!/bin/bash

version=1

until [ ! -d "condor/Muon_2022/Muon_2022D_v$version" ]
do
  echo folder: $version
  ((version=version+1))
done

#osusub.py -n 9999 -m -1 -t Dataset -A -P -l localConfig_2022.py -w run2022_test_v$version/ --redirector FNAL -g -R "request_memory=3000MB request_cpus=4" -J P_Golden22
#osusub.py -l localConfig_2022.py -t Dataset -w 2022/basicSelection_Muon_v$version/ -A -P -J P_Golden22 -R "request_memory=4000MB request_cpus=4 request_disk=1000MB"
osusub.py -l localConfig_2022.py -s 2022/basicSelection_Muon_v11 -a BasicSelection -w Muon_2022/Muon_2022D_v$version/ -A -P -J P_Golden22 -R "request_memory=4000MB request_cpus=4 request_disk=1000MB"