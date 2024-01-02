## 'Full' recipe including osusub.py

```
cmsrel CMSSW_12_4_11_patch3
cd CMSSW_12_4_11_patch3/src
cmsenv
git-cms-init
git cms-addpkg IOPool/Input

sed -i '/assert(readEventSucceeded)/s/^/\/\//' IOPool/Input/src/PoolSource.cc

git clone https://github.com/OSU-CMS/DisappTrksML.git
git clone https://github.com/OSU-CMS/DisappTrks.git
git clone https://github.com/OSU-CMS/OSUT3Analysis.git

OSUT3Analysis/AnaTools/scripts/setupFramework.py -f MINI_AOD_2022 -c DisappTrks/StandardAnalysis/interface/CustomDataFormat.h

scramv1 b -j 9
```
