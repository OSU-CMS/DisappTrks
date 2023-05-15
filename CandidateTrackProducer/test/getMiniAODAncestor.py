import os
import sys
import commands
from os.path import exists
import time

startDir = "/share/scratch0/borzari/CMSSW_12_4_11_patch3/src/DisappTrks/CandidateTrackProducer/test"
commonDirMiniAOD = "/data/users/borzari/condor/SignalMC/Run3/2022/step4/CandidateTrackProducerNoSkimming/"
commonDirSkim = "/data/users/borzari/condor/SignalMC/Run3/2022/Cutflows_AMSB_700_100_candidateTracksNoSkimming_candTrkSelection/"

mass = 700
ctau = 100
user = "borzari"

pathMiniAOD = commonDirMiniAOD + str(ctau) + "cm/" + str(mass) + "GeV/condor.sub" # NOT SURE IF NEEDED
pathListMiniAOD = "MiniAODList_" + str(mass) + "GeV_" + str(ctau) + "cm.txt"

pathSkim = commonDirSkim + "condor.sub"
pathListSkim = "SkimList_" + str(mass) + "GeV_" + str(ctau) + "cm.txt"

print(pathMiniAOD)
print(pathListMiniAOD)
print(pathSkim)
print(pathListSkim)
cmdListSize = "ls " + pathSkim.replace("condor.sub","*.err") + " | wc -l"
listSize = commands.getoutput(cmdListSize)

if exists(pathListMiniAOD): os.system("rm "+pathListMiniAOD)
if exists(pathListSkim): os.system("rm "+pathListSkim)

listMiniAOD = open(pathListMiniAOD,'w')
listSkim = open(pathListSkim,'w')

for i in range(int(listSize)):

    if exists(commonDirSkim + "CandTrkSelection/skim_" + str(i) + ".root"):
        cmdGetMiniAODFile = "sed -n '/Successfully opened file/ p' " + commonDirSkim + "/condor_" + str(i) + ".err"
        MiniAODFile = commands.getoutput(cmdGetMiniAODFile)
        SkimFile = commonDirSkim + "CandTrkSelection/skim_" + str(i) + ".root"
        # print(MiniAODFile.split()[6])
        listMiniAOD.write(MiniAODFile.split()[6] + "\n")
        # print("file:" + SkimFile)
        listSkim.write("file:" + SkimFile + "\n")

# print(len(listMiniAOD),len(listSkim))

# with open(condSubAOD,'r') as file:
#     condLinesAOD = [line for line in file]

# with open(condResubAOD,'w') as file:
#     for line in condLinesAOD:
#         if line.startswith("Queue"):
#             file.write("#"+line)
#             file.write("Queue Process in "+','.join(map(str,listMiniAOD))+"\n")
#         else:
#             file.write(line)

# with open(condSubMiniAOD,'r') as file:
#     condLinesMiniAOD = [line for line in file]

# with open(condResubMiniAOD,'w') as file:
#     for line in condLinesMiniAOD:
#         if line.startswith("Queue"):
#             file.write("#"+line)
#             file.write("Queue Process in "+','.join(map(str,listSkim))+"\n")
#         else:
#             file.write(line)

print("======================= FINISHED EVERYTHING!!! =======================")
