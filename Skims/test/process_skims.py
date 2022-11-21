import os
import sys

masses = [100, 200, 300, 400, 500]
lifetimes = [1, 10, 100, 1000, 10000]

skip = {}

step2_dataset = [
	'/Higgsino_M-100GeV_CTau-1cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-100GeV_CTau-10cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-100GeV_CTau-100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-100GeV_CTau-1000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER', 
	'/Higgsino_M-100GeV_CTau-10000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-200GeV_CTau-1cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-200GeV_CTau-10cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-200GeV_CTau-100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-200GeV_CTau-1000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-200GeV_CTau-10000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',	
	'/Higgsino_M-300GeV_CTau-1cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-300GeV_CTau-10cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-300GeV_CTau-100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',	
	'/Higgsino_M-300GeV_CTau-1000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-300GeV_CTau-10000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-400GeV_CTau-1cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-400GeV_CTau-10cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-400GeV_CTau-100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-400GeV_CTau-1000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-400GeV_CTau-10000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-500GeV_CTau-1cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-500GeV_CTau-10cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-500GeV_CTau-100cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-500GeV_CTau-1000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
	'/Higgsino_M-500GeV_CTau-10000cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/micarrig-Run3Summer22DRPremixMiniAOD-124X_mcRun3_2021_realistic_v1-v1_step2-f5721861cc423f32ed0ccb709732d61f/USER',
]

for imass, mass in enumerate(masses):
	if mass != 500: continue
	for ilifetime, lifetime in enumerate(lifetimes):
		#if lifetime == 1 or lifetime==10: continue
		if mass in skip.keys():
			if lifetime in skip[mass]:
				continue
		#input_dataset = step2_dataset[imass * len(lifetimes) + ilifetime]
		print("Submitting dataset:", mass, lifetime)
		cmd = 'osusub.py -n 999999 -t UserDir -f process.SKIMStreamEXODisappTrk.fileName -d /data/users/mcarrigan/condor/signalMC/Run3/step3/higgsino_{1}GeV_{2}cm/Higgsino_M_{1}GeV_CTau_{2}cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/ --inputDirectory=/data/users/mcarrigan/condor/signalMC/Run3/step3/higgsino_{1}GeV_{2}cm/Higgsino_M_{1}GeV_CTau_{2}cm_TuneCP5_PSweights_13p6TeV_madgraph5_pythia8/ -c test_EXODisappTrk_MC2022.py -w signalMC/Run3/skim/higgsino_{1}GeV_{2}cm -g'.format(-1, mass, lifetime)
		os.system(cmd)

