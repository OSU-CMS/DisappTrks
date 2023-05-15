import os
import sys
import commands
from os.path import exists
import time

startDir = "/share/scratch0/borzari/CMSSW_12_4_11_patch3/src/DisappTrks/CandidateTrackProducer/test"
commonDirAOD = "/data/users/borzari/condor/SignalMC/Run3/2022/step3/"
commonDirMiniAOD = "/data/users/borzari/condor/SignalMC/Run3/2022/step4/CandidateTrackProducerNoSkimming/"

mass = 100
ctau = 100
user = "borzari"

condSubAOD = commonDirAOD+str(ctau)+"cm/"+str(mass)+"GeV/AMSB_chargino_M_"+str(mass)+"GeV_CTau_"+str(ctau)+"cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/condor.sub"
condResubAOD = commonDirAOD+str(ctau)+"cm/"+str(mass)+"GeV/AMSB_chargino_M_"+str(mass)+"GeV_CTau_"+str(ctau)+"cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/condor_resub.sub"

condSubMiniAOD = commonDirMiniAOD+str(ctau)+"cm/"+str(mass)+"GeV/condor.sub"
condResubMiniAOD = commonDirMiniAOD+str(ctau)+"cm/"+str(mass)+"GeV/condor_resub.sub"

print(condSubAOD)
print(condResubAOD)
print(condSubMiniAOD)
print(condResubMiniAOD)
cmdListSize = "ls " + condSubMiniAOD.replace("condor.sub","*.err") + " | wc -l"
listSize = commands.getoutput(cmdListSize)

if exists(condResubAOD): os.system("rm "+condResubAOD)
if exists(condResubMiniAOD): os.system("rm "+condResubMiniAOD)

listAOD = []
listMiniAOD = []

for i in range(int(listSize)):

    cmdCheckDeepTau = "sed -n '/Begin Fatal Exception/ p' " + commonDirMiniAOD + str(ctau) +"cm/" + str(mass) + "GeV/condor_"+str(i)+".err"
    deepTauMsg = commands.getoutput(cmdCheckDeepTau)

    if len(deepTauMsg) > 0:

        cmdGetAODFile = "sed -n '/Successfully opened file/ p' " + commonDirMiniAOD + str(ctau) +"cm/" + str(mass) + "GeV/condor_"+str(i)+".err"
        AODFile = commands.getoutput(cmdGetAODFile)
        print(AODFile, i)
        if len(AODFile) == 0: continue
        listAOD.append(int(AODFile.split()[6].split("/")[-1].replace("hist_","").replace(".root","")))
        listMiniAOD.append(i)

print(len(listAOD),len(listMiniAOD))

while(len(listMiniAOD) > 0):

    with open(condSubAOD,'r') as file:
        condLinesAOD = [line for line in file]

    with open(condResubAOD,'w') as file:
        for line in condLinesAOD:
            if line.startswith("Queue"):
                file.write("#"+line)
                file.write("Queue Process in "+','.join(map(str,listAOD))+"\n")
            else:
                file.write(line)

    print("cd " + condResubAOD.replace("/condor_resub.sub","") + " && condor_submit condor_resub.sub && condor_q --allusers && cd " + startDir)
    os.system("cd " + condResubAOD.replace("/condor_resub.sub","") + " && condor_submit condor_resub.sub && condor_q --allusers && cd " + startDir)

    cmdToGetUser = "condor_q --allusers"
    condorOut = commands.getoutput(cmdToGetUser)
    n = 0

    while (user in condorOut):
        cmdToGetUser = "condor_q --allusers"
        condorOut = commands.getoutput(cmdToGetUser)
        if n == 6:
            print(condorOut)
            n = 0
        time.sleep(30)
        n = n + 1
    print("======================= FINISHED AOD!!! =======================")

    with open(condSubMiniAOD,'r') as file:
        condLinesMiniAOD = [line for line in file]

    with open(condResubMiniAOD,'w') as file:
        for line in condLinesMiniAOD:
            if line.startswith("Queue"):
                file.write("#"+line)
                file.write("Queue Process in "+','.join(map(str,listMiniAOD))+"\n")
            else:
                file.write(line)

    print("cd " + condResubMiniAOD.replace("/condor_resub.sub","") + " && condor_submit condor_resub.sub && condor_q --allusers && cd " + startDir)
    os.system("cd " + condResubMiniAOD.replace("/condor_resub.sub","") + " && condor_submit condor_resub.sub && condor_q --allusers && cd " + startDir)

    cmdToGetUser = "condor_q --allusers"
    condorOut = commands.getoutput(cmdToGetUser)
    n = 0

    while (user in condorOut):
        cmdToGetUser = "condor_q --allusers"
        condorOut = commands.getoutput(cmdToGetUser)
        if n == 6:
            print(condorOut)
            n = 0
        time.sleep(30)
        n = n + 1
    print("======================= FINISHED MINIAOD!!! =======================")

    listAOD = []
    listMiniAOD = []

    for i in range(int(listSize)):

        cmdCheckDeepTau = "sed -n '/Begin Fatal Exception/ p' " + commonDirMiniAOD + str(ctau) +"cm/" + str(mass) + "GeV/condor_"+str(i)+".err"
        deepTauMsg = commands.getoutput(cmdCheckDeepTau)

        if len(deepTauMsg) > 20 and len(deepTauMsg) < 100:

            cmdGetAODFile = "sed -n '/Successfully opened file/ p' " + commonDirMiniAOD + str(ctau) +"cm/" + str(mass) + "GeV/condor_"+str(i)+".err"
            AODFile = commands.getoutput(cmdGetAODFile)
            print(AODFile, i)
            if len(AODFile) == 0: continue
            listAOD.append(int(AODFile.split()[6].split("/")[-1].replace("hist_","").replace(".root","")))
            listMiniAOD.append(i)

    print(len(listAOD),len(listMiniAOD))

print("======================= FINISHED EVERYTHING!!! =======================")
