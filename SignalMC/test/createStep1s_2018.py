#!/usr/bin/env python
import os
import sys

c = 299792458.0 * 100.0 # cm/s

if os.environ['CMSSW_VERSION'] != 'CMSSW_10_2_0':
	print
	print 'Private generation of 2018 samples must proceed in CMSSW_10_2_0, but you are in', os.environ['CMSSW_VERSION']
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
xsecsWino = {
	100 : 34.282,
	200 : 2.709959,
	300 : 0.577095,
	400 : 0.179644,
	500 : 0.06848,
	600 : 0.029636,
	700 : 0.013949,
	800 : 0.0069704,
	900 : 0.00364968,
	1000 : 0.001965386,
	1100 : 0.001082998
}

# xsecsHiggsino[mass in GeV] = xsec (pb)
xsecsHiggsino = {
    100 : 5767.34,
    200 : 488.642,
    300 : 105.138,
    400 : 32.681,
    500 : 12.4325,
    600 : 5.36776,
    700 : 2.51962,
    800 : 1.261932,
    900 : 0.657058,
    #1000 : 0.36461,
    #1100 : 0.1929674,
    #1200 : 0.11266,
    #1300 : 0.0609138,
    #1400 : 0.0406518,
    #1500 : 0.0206072,
}

ctaus = [1, 10, 100, 1000, 10000] # cm

################################################################
# step 1: create the gen fragments
################################################################
if scriptStep == 1:
	# first wino-like LSP case
	baseConfigFile   = baseDir + 'data/AMSB_chargino_M-XXXGeV_CTau-YYYcm_TuneCP5_PSweights_13TeV_pythia8_cff.py'
	baseParticleFile = baseDir + 'data/geant4_AMSB_chargino_XXXGeV_ctauYYYcm.slha'
	for mass in xsecsWino:
		for ctau in ctaus:
			outputConfigFile   = baseDir + 'python/pythia8/AMSB_chargino_M-%dGeV_CTau-%dcm_TuneCP5_PSweights_13TeV_pythia8_cff.py' % (mass, ctau)
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
	baseConfigFile   = baseDir + 'data/Higgsino_M-XXXGeV_CTau-YYYcm_TuneCP5_PSweights_13TeV_pythia8_cff.py'
	baseParticleFile = baseDir + 'data/geant4_higgsino_XXXGeV_ctauYYYcm.slha'
	for mass in xsecsHiggsino:
		for ctau in ctaus:
			outputConfigFile   = baseDir + 'python/pythia8/Higgsino_M-%dGeV_CTau-%dcm_TuneCP5_PSweights_13TeV_pythia8_cff.py' % (mass, ctau)
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
################################################################
if scriptStep == 2:
	# first wino-like LSP case
	cmd = 'cmsDriver.py DisappTrks/SignalMC/python/pythia8/AMSB_chargino_M-{0}GeV_CTau-{1}cm_TuneCP5_PSweights_13TeV_pythia8_cff.py'
	cmd += ' --fileout file:AMSB_chargino{0}GeV_ctau{1}cm_step1.root'
	cmd += ' --mc --eventcontent RAWSIM'
	cmd += ' --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,SimG4Core/Application/customiseSequentialSim.customiseSequentialSim'
	cmd += ' --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v9'
	cmd += ' --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --geometry DB:Extended'
	cmd += ' --era Run2_2018'
	cmd += ' --python_filename step1/pythia8/AMSB_chargino_M-{0}GeV_CTau-{1}cm_TuneCP5_PSweights_13TeV_pythia8_step1.py'
	cmd += ' --no_exec -n 10'

	for mass in xsecsWino:
		for ctau in ctaus:
			os.system(cmd.format(mass, ctau))

	print 'Created electroweak (wino-like) GEN-SIM configuration files in directory: ' + os.getcwd() + '/step1/pythia8'

	# now higgsino-like LSP case
	cmd = 'cmsDriver.py DisappTrks/SignalMC/python/pythia8/Higgsino_M-{0}GeV_CTau-{1}cm_TuneCP5_PSweights_13TeV_pythia8_cff.py'
	cmd += ' --fileout file:Higgsino_M-{0}GeV_ctau{1}cm_step1.root'
	cmd += ' --mc --eventcontent RAWSIM'
	cmd += ' --customise Configuration/DataProcessing/Utils.addMonitoring,SimG4Core/CustomPhysics/Exotica_HSCP_SIM_cfi,SimG4Core/Application/customiseSequentialSim.customiseSequentialSim'
	cmd += ' --datatier GEN-SIM --conditions 102X_upgrade2018_realistic_v9'
	cmd += ' --beamspot Realistic25ns13TeVEarly2018Collision --step GEN,SIM --geometry DB:Extended'
	cmd += ' --era Run2_2018'
	cmd += ' --python_filename step1/pythia8/Higgsino_M-{0}GeV_ctau{1}cm_TuneCP5_PSweights_13TeV_pythia8_step1.py'
	cmd += ' --no_exec -n 10'

	for mass in xsecsHiggsino:
		for ctau in ctaus:
			os.system(cmd.format(mass, ctau))

	print 'Created electroweak (higgsino-like) GEN-SIM configuration files in directory: ' + os.getcwd() + '/step1/pythia8'
