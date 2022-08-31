#!/bin/bash

version=1

until [ ! -d "condor/run2022_test_v$version" ]
do
  echo folder: $version
  ((version=version+1))
done

osusub.py -n 10 -m 100 -t Dataset -d /MET/Run2022A-PromptReco-v1/MINIAOD -A -P -l localConfig_2022.py -w run2022_test_v$version/ --redirector FNAL -g -R "Memory > 3000" -J P_Golden22

