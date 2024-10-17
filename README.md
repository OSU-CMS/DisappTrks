## 'Full' recipe including osusub.py: AOD+MiniAOD skim
```
cmsrel CMSSW_13_0_13
cd CMSSW_13_0_13/src
cmsenv
git-cms-init

git clone https://github.com/OSU-CMS/DisappTrksML.git
git clone https://github.com/OSU-CMS/DisappTrks.git
git clone https://github.com/OSU-CMS/OSUT3Analysis.git

cd DisappTrksML
git checkout tags/cmssw_13_0_13
cd ../DisappTrks
git checkout update_CMSSW_13
cd ../OSUT3Analysis
git checkout update_CMSSW_13
cd ..

OSUT3Analysis/AnaTools/scripts/setupFramework.py -f MINI_AOD_2022 -c DisappTrks/StandardAnalysis/interface/CustomDataFormat.h

scramv1 b -j 9
```

## 'Full' recipe including osusub.py: MiniAOD only
```
cmsrel CMSSW_13_0_13
cd CMSSW_13_0_13/src
cmsenv
git-cms-init

git clone https://github.com/OSU-CMS/DisappTrksML.git
git clone https://github.com/OSU-CMS/DisappTrks.git
git clone https://github.com/OSU-CMS/OSUT3Analysis.git

cd DisappTrksML
git checkout tags/cmssw_13_0_13
cd ../DisappTrks
git checkout update_CMSSW_13
cd ../OSUT3Analysis
git checkout update_CMSSW_13
cd ..

OSUT3Analysis/AnaTools/scripts/setupFramework.py -f MINI_AOD_ONLY_2022 -c DisappTrks/StandardAnalysis/interface/CustomDataFormat.h

scramv1 b -j 9
```
