#!/usr/bin/env python
import os
import sys

c = 299792458.0 * 100.0 # cm/s

if os.environ['CMSSW_VERSION'] != 'CMSSW_11_2_2':
	print
	print 'Private generation of Run 3 samples must proceed in CMSSW_11_2_2, but you are in', os.environ['CMSSW_VERSION']
	print 'Quitting...'
	print
	sys.exit()

baseDir = os.environ['CMSSW_BASE'] + '/src/DisappTrks/SignalMC/'

if not os.path.exists(baseDir + 'data/geant4'):
	os.mkdir(baseDir + 'data/geant4')
if not os.path.exists(baseDir + 'data/geant4_higgsino'):
	os.mkdir(baseDir + 'data/geant4_higgsino')

def findMassValue(fileName, particleName):
	inputFile = open(fileName, 'r')
	for line in inputFile:
		if particleName in line:
			return line.split()[1]

################################################################
# script runs in two steps: 
#	first create the fragments, then the user needs to scram b
# 	then the step1 configs are created
################################################################
scriptStep = 1
if len(sys.argv) > 1:
	scriptStep = 2

# xsecsWino[mass in GeV] = xsec (pb)
xsecsWino = { m : -1. for m in range(100, 1200, 100) }

# xsecsHiggsino[mass in GeV] = xsec (pb)
xsecsHiggsino = { m : -1. for m in range(100, 1000, 100) }

ctaus = [1, 10, 100, 1000, 10000] # cm

################################################################
# step 1: create the gen fragments
################################################################
if scriptStep == 1:
	# first wino-like LSP case
	baseConfigFile   = baseDir + 'data/AMSB_chargino_M-XXXGeV_CTau-YYYcm_TuneCP5_PSweights_14TeV_pythia8_cff.py'
	baseParticleFile = baseDir + 'data/geant4_AMSB_chargino_XXXGeV_ctauYYYcm.slha'
	for mass in xsecsWino:
		for ctau in ctaus:
			outputConfigFile   = baseDir + 'python/pythia8/AMSB_chargino_M%dGeV_CTau%dcm_TuneCP5_PSweights_14TeV_pythia8_cff.py' % (mass, ctau)
			outputParticleFile = baseDir + 'data/geant4/geant4_AMSB_chargino_%dGeV_ctau%dcm.slha' % (mass, ctau)
			slhaFile           = baseDir + 'data/SLHA_withDecay/%dcm/AMSB_chargino_%dGeV_%dcm_Isajet780.slha' % (ctau, mass, ctau)
			os.system('sed "s/XXX/' + str(mass) + '/g" ' + baseConfigFile + ' > ' + outputConfigFile)
			os.system('sed -i "s/YYY/' + str(int(ctau * 10.0)) + '/g" ' + outputConfigFile) # mm
			os.system('sed -i "s/ZZZ/' + str(xsecsWino[mass]) + '/g" ' + outputConfigFile)
			mW1ss = findMassValue(slhaFile, 'w1ss')
			mZ1ss = findMassValue(slhaFile, 'z1ss')
			tau = ctau / c * 1.e9 # ns
			width = (1.97326979e-14 / ctau) # GeV
			os.system('sed "s/_MW1SS/' + str(mW1ss) + '/g" ' + baseParticleFile + ' > ' + outputParticleFile)
			os.system('sed -i "s/_MZ1SS/' + str(mZ1ss) + '/g" ' + outputParticleFile)
			os.system('sed -i "s/_CTAU/' + str(ctau) + '/g" ' + outputParticleFile)
			os.system('sed -i "s/_TAU/' + str(tau) + '/g" ' + outputParticleFile)
			os.system('sed -i "s/_WIDTH/' + str(width) + '/g" ' + outputParticleFile)
	print 'Created electroweak (wino-like) configuration fragments and particle files in directory: ' + baseDir

	# now higgsino-like LSP case
	baseConfigFile   = baseDir + 'data/Higgsino_M-XXXGeV_CTau-YYYcm_TuneCP5_PSweights_14TeV_pythia8_cff.py'
	baseParticleFile = baseDir + 'data/geant4_higgsino_XXXGeV_ctauYYYcm.slha'
	for mass in xsecsHiggsino:
		for ctau in ctaus:
			outputConfigFile   = baseDir + 'python/pythia8/Higgsino_M%dGeV_CTau%dcm_TuneCP5_PSweights_14TeV_pythia8_cff.py' % (mass, ctau)
			outputParticleFile = baseDir + 'data/geant4_higgsino/geant4_higgsino_%dGeV_ctau%dcm.slha' % (mass, ctau)
			slhaFile           = baseDir + 'data/SLHA_withDecay/%dcm/Higgsino_%dGeV_%dcm_Isajet780.slha' % (ctau, mass, ctau)
			os.system('sed "s/XXX/' + str(mass) + '/g" ' + baseConfigFile + ' > ' + outputConfigFile)
			os.system('sed -i "s/YYY/' + str(int(ctau * 10.0)) + '/g" ' + outputConfigFile) # mm
			os.system('sed -i "s/ZZZ/' + str(xsecsHiggsino[mass]) + '/g" ' + outputConfigFile)
			mW1ss = findMassValue(slhaFile, 'w1ss')
			mZ1ss = findMassValue(slhaFile, 'z1ss')
			mZ2ss = findMassValue(slhaFile, 'z2ss')
			tau = ctau / c * 1.e9 # ns
			width = (1.97326979e-14 / ctau) # GeV
			os.system('sed "s/_MW1SS/' + str(mW1ss) + '/g" ' + baseParticleFile + ' > ' + outputParticleFile)
			os.system('sed -i "s/_MZ1SS/' + str(mZ1ss) + '/g" ' + outputParticleFile)
			os.system('sed -i "s/_MZ2SS/' + str(mZ2ss) + '/g" ' + outputParticleFile)
			os.system('sed -i "s/_CTAU/' + str(ctau) + '/g" ' + outputParticleFile)
			os.system('sed -i "s/_TAU/' + str(tau) + '/g" ' + outputParticleFile)
			os.system('sed -i "s/_WIDTH/' + str(width) + '/g" ' + outputParticleFile)
	print 'Created electroweak (higgsino-like) configuration fragments and particle files in directory: ' + baseDir

	print
	print 'Now "scram b" and run this again with argument "2" to create the step 1 configs'
	print

################################################################
# step 2: create the GEN-SIM configs
# https://its.cern.ch/jira/browse/PDMVMCPROD-21
################################################################
if scriptStep == 2:
	# first wino-like LSP case
	cmd = 'cmsDriver.py DisappTrks/SignalMC/python/pythia8/AMSB_chargino_M{0}GeV_CTau{1}cm_TuneCP5_PSweights_14TeV_pythia8_cff.py'
	cmd += ' --fileout file:AMSB_chargino{0}GeV_ctau{1}cm_step1.root'
	cmd += ' --mc --eventcontent RAWSIM'
	cmd += ' --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,SimG4Core/Application/customiseSequentialSim.customiseSequentialSim'
	cmd += ' --datatier GEN-SIM --conditions 112X_mcRun3_2021_realistic_v15'
	cmd += ' --beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step GEN,SIM --geometry DB:Extended'
	cmd += ' --era Run3'
	cmd += ' --python_filename step1/pythia8/AMSB_chargino_M{0}GeV_CTau{1}cm_TuneCP5_PSweights_14TeV_pythia8_step1.py'
	cmd += ' --no_exec -n 10'

	for mass in xsecsWino:
		for ctau in ctaus:
			os.system(cmd.format(mass, ctau))

	print 'Created electroweak (wino-like) GEN-SIM configuration files in directory: ' + os.getcwd() + '/step1/pythia8'

	# now higgsino-like LSP case
	cmd = 'cmsDriver.py DisappTrks/SignalMC/python/pythia8/Higgsino_M{0}GeV_CTau{1}cm_TuneCP5_PSweights_14TeV_pythia8_cff.py'
	cmd += ' --fileout file:Higgsino_M{0}GeV_ctau{1}cm_step1.root'
	cmd += ' --mc --eventcontent RAWSIM'
	cmd += ' --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,SimG4Core/Application/customiseSequentialSim.customiseSequentialSim'
	cmd += ' --datatier GEN-SIM --conditions 112X_mcRun3_2021_realistic_v15'
	cmd += ' --beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step GEN,SIM --geometry DB:Extended'
	cmd += ' --era Run3'
	cmd += ' --python_filename step1/pythia8/Higgsino_M{0}GeV_ctau{1}cm_TuneCP5_PSweights_14TeV_pythia8_step1.py'
	cmd += ' --no_exec -n 10'

	for mass in xsecsHiggsino:
		for ctau in ctaus:
			os.system(cmd.format(mass, ctau))

	print 'Created electroweak (higgsino-like) GEN-SIM configuration files in directory: ' + os.getcwd() + '/step1/pythia8'
