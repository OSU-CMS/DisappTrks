## 'Full' recipe including osusub.py

```
cmsrel CMSSW_12_4_7
cd CMSSW_12_4_7/src/
cmsenv
git clone https://github.com/OSU-CMS/OSUT3Analysis.git
git clone https://github.com/OSU-CMS/DisappTrks.git
git clone https://github.com/OSU-CMS/DisappTrksML.git
OSUT3Analysis/AnaTools/scripts/setupFramework.py -f MINI_AOD_2022 -c DisappTrks/StandardAnalysis/interface/CustomDataFormat.h
scram b -j 9
cmsenv
```