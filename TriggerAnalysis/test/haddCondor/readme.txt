This directory sends the task of "hadd *.root" to condor for ROOT files stored at Purdue's T2 accessed by xrootd.

Usage example:

First, using "gfal-ls", find the SRM directory XYZ such that your files are stored as:
XYZ/0000/*.root
XYZ/0001/*.root
...
Then:

voms-proxy-init -voms cms -hours 120
./makeLists_gfal.sh "srm://srm.rcac.purdue.edu:8443/srm/v2/server?SFN=/mnt/hadoop/store/user/bfrancis/SingleMuon/Run2016B-PromptReco-v2-DisappTrks-v6/161004_164444/"
# wait for condor...
./finish.sh
# now you are left with "output.root" containing the hadd of all files within XYZ
# rename it as desired
